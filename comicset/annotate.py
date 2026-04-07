"""comicset annotate — local web UI for dataset annotation.

Serves a localhost web page that shows each comic's photo alongside
a form with dropdowns populated from the defect chart.
"""
from __future__ import annotations

import json
import http.server
import webbrowser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .schema import load_dataset, save_dataset, DefectAnnotation, StructuralAssessments


def _get_defect_keywords(args) -> list[str]:
    """Get valid defect chart keywords from the backend."""
    try:
        from .backend import resolve_backend_dir, get_defect_keywords
        backend_dir = resolve_backend_dir(getattr(args, "backend_dir", None))
        if backend_dir:
            return sorted(get_defect_keywords(backend_dir))
    except Exception:
        pass
    return []


def _build_html(dataset_dir: Path, entries: dict, keywords: list[str]) -> str:
    """Build the single-page annotation app HTML."""
    slugs = json.dumps(list(entries.keys()))
    entries_json = json.dumps({
        slug: {
            "title": e.title,
            "ai_draft_grade": e.ai_draft_grade,
            "ai_confidence": e.ai_confidence,
            "ai_defects": [{"description": d.description, "severity": d.severity, "zone": d.zone} for d in e.ai_defects],
            "expected_grade_low": e.expected_grade_low,
            "expected_grade_high": e.expected_grade_high,
            "annotator_confidence": e.annotator_confidence,
            "grading_difficulty": e.grading_difficulty,
            "specimen_type": e.specimen_type,
            "known_defects": [
                {"description": d.description, "defect_chart_keyword": d.defect_chart_keyword,
                 "severity": d.severity, "zone": d.zone, "annotator_confidence": d.annotator_confidence}
                for d in e.known_defects
            ],
            "structural_assessments": {
                "spine_condition": e.structural_assessments.spine_condition if e.structural_assessments else None,
                "corner_condition": e.structural_assessments.corner_condition if e.structural_assessments else None,
                "edge_condition": e.structural_assessments.edge_condition if e.structural_assessments else None,
                "staple_condition": e.structural_assessments.staple_condition if e.structural_assessments else None,
                "page_quality": e.structural_assessments.page_quality if e.structural_assessments else None,
            },
            "notes": e.notes,
            "image_path": e.views[0].image_path if e.views else f"images/{slug}_front.jpg",
        }
        for slug, e in entries.items()
    })
    keywords_json = json.dumps(keywords)

    zones = json.dumps([
        "spine", "top_left_corner", "top_right_corner", "bottom_left_corner",
        "bottom_right_corner", "top_edge", "bottom_edge", "right_edge",
        "upper_staple", "lower_staple", "cover_center", "full_cover",
    ])

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>comicset annotate</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, system-ui, sans-serif; background: #1a1a2e; color: #e0e0e0; padding: 20px; }}
.container {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }}
.photo-panel {{ position: sticky; top: 20px; align-self: start; }}
.photo-panel img {{ width: 100%; border-radius: 8px; border: 2px solid #333; }}
.form-panel {{ background: #16213e; padding: 24px; border-radius: 8px; }}
h1 {{ grid-column: 1/-1; font-size: 18px; color: #94a3b8; }}
h2 {{ font-size: 16px; margin: 16px 0 8px; color: #60a5fa; }}
.ai-draft {{ background: #1e3a5f; padding: 12px; border-radius: 6px; margin: 8px 0; font-size: 13px; }}
.ai-draft .grade {{ font-size: 24px; font-weight: bold; color: #34d399; }}
label {{ display: block; margin: 8px 0 4px; font-size: 13px; color: #94a3b8; }}
select, input, textarea {{ width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #333; background: #0f172a; color: #e0e0e0; font-size: 14px; }}
textarea {{ height: 60px; resize: vertical; }}
.defect-row {{ background: #1e293b; padding: 12px; margin: 8px 0; border-radius: 6px; position: relative; }}
.defect-row .remove {{ position: absolute; top: 8px; right: 8px; cursor: pointer; color: #ef4444; }}
.btn {{ padding: 10px 20px; border-radius: 6px; border: none; cursor: pointer; font-size: 14px; font-weight: 600; }}
.btn-primary {{ background: #3b82f6; color: white; }}
.btn-secondary {{ background: #374151; color: #e0e0e0; }}
.btn-success {{ background: #10b981; color: white; }}
.btn:hover {{ opacity: 0.9; }}
.nav {{ display: flex; gap: 12px; align-items: center; justify-content: space-between; margin-top: 16px; }}
.progress {{ font-size: 13px; color: #6b7280; }}
.row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
</style></head><body>
<div class="container">
<h1 id="header">comicset annotate</h1>
<div class="photo-panel"><img id="photo" src="" alt="Comic photo"></div>
<div class="form-panel">
<div class="ai-draft" id="ai-info"></div>

<h2>Human Grade</h2>
<div class="row">
<div><label>Grade Low</label><input type="number" id="grade_low" step="0.1" min="0.5" max="10"></div>
<div><label>Grade High</label><input type="number" id="grade_high" step="0.1" min="0.5" max="10"></div>
</div>
<div class="row">
<div><label>Confidence</label><select id="annotator_confidence"><option value="">-</option><option>high</option><option>medium</option><option>low</option></select></div>
<div><label>Difficulty</label><select id="grading_difficulty"><option value="">-</option><option>trivial</option><option>easy</option><option>moderate</option><option>hard</option><option>ambiguous</option></select></div>
</div>

<h2>Structural</h2>
<div class="row">
<div><label>Spine</label><select id="spine_condition"><option value="">-</option><option>mint</option><option>near_mint</option><option>good</option><option>fair</option><option>poor</option></select></div>
<div><label>Corners</label><select id="corner_condition"><option value="">-</option><option>sharp</option><option>slight_blunting</option><option>blunted</option><option>rolled</option><option>worn</option></select></div>
</div>
<div class="row">
<div><label>Edges</label><select id="edge_condition"><option value="">-</option><option>clean</option><option>slight_wear</option><option>moderate_wear</option><option>heavy_wear</option></select></div>
<div><label>Pages</label><select id="page_quality"><option value="">-</option><option>white</option><option>off_white</option><option>cream</option><option>tanning</option><option>brittle</option></select></div>
</div>

<h2>Defects <button class="btn btn-secondary" onclick="addDefect()" style="float:right;padding:4px 12px;font-size:12px">+ Add</button></h2>
<div id="defects-list"></div>

<label>Notes</label>
<textarea id="notes"></textarea>

<div class="nav">
<button class="btn btn-secondary" onclick="prev()">← Previous</button>
<span class="progress" id="progress"></span>
<button class="btn btn-success" onclick="saveAndNext()">Save & Next →</button>
</div>
</div></div>

<script>
const SLUGS = {slugs};
const ENTRIES = {entries_json};
const KEYWORDS = {keywords_json};
const ZONES = {zones};
let currentIdx = 0;

function load(idx) {{
    currentIdx = idx;
    const slug = SLUGS[idx];
    const e = ENTRIES[slug];
    document.getElementById('header').textContent = e.title || slug;
    document.getElementById('photo').src = e.image_path;
    document.getElementById('progress').textContent = (idx+1) + ' / ' + SLUGS.length;

    // AI draft info
    const ai = document.getElementById('ai-info');
    if (e.ai_draft_grade !== null) {{
        ai.innerHTML = '<span class="grade">' + e.ai_draft_grade + '</span> (AI draft, ' + (e.ai_confidence||'?') + ' confidence)'
            + '<br><small>' + (e.ai_defects||[]).map(d => d.severity + ' ' + d.description).join('; ') + '</small>';
    }} else {{
        ai.innerHTML = '<em>No AI grade available</em>';
    }}

    document.getElementById('grade_low').value = e.expected_grade_low || '';
    document.getElementById('grade_high').value = e.expected_grade_high || '';
    document.getElementById('annotator_confidence').value = e.annotator_confidence || '';
    document.getElementById('grading_difficulty').value = e.grading_difficulty || '';
    document.getElementById('notes').value = e.notes || '';

    const sa = e.structural_assessments || {{}};
    document.getElementById('spine_condition').value = sa.spine_condition || '';
    document.getElementById('corner_condition').value = sa.corner_condition || '';
    document.getElementById('edge_condition').value = sa.edge_condition || '';
    document.getElementById('page_quality').value = sa.page_quality || '';

    const dl = document.getElementById('defects-list');
    dl.innerHTML = '';
    (e.known_defects || []).forEach((d, i) => addDefectRow(d));
}}

function addDefect() {{ addDefectRow({{}}); }}
function addDefectRow(d) {{
    const dl = document.getElementById('defects-list');
    const div = document.createElement('div');
    div.className = 'defect-row';
    const kwOpts = KEYWORDS.map(k => '<option' + (k===d.defect_chart_keyword?' selected':'') + '>' + k + '</option>').join('');
    const zOpts = ZONES.map(z => '<option' + (z===d.zone?' selected':'') + '>' + z + '</option>').join('');
    div.innerHTML = '<span class="remove" onclick="this.parentElement.remove()">✕</span>'
        + '<label>Keyword</label><select class="dk"><option value="">-</option>' + kwOpts + '</select>'
        + '<label>Zone</label><select class="dz"><option value="">-</option>' + zOpts + '</select>'
        + '<div class="row"><div><label>Severity</label><select class="ds"><option' + (d.severity==='minor'?' selected':'') + '>minor</option><option' + (d.severity==='moderate'?' selected':'') + '>moderate</option><option' + (d.severity==='major'?' selected':'') + '>major</option></select></div>'
        + '<div><label>Description</label><input class="dd" value="' + (d.description||'').replace(/"/g,'&quot;') + '"></div></div>';
    dl.appendChild(div);
}}

function gather() {{
    const slug = SLUGS[currentIdx];
    const e = ENTRIES[slug];
    e.expected_grade_low = parseFloat(document.getElementById('grade_low').value) || null;
    e.expected_grade_high = parseFloat(document.getElementById('grade_high').value) || null;
    e.annotator_confidence = document.getElementById('annotator_confidence').value || null;
    e.grading_difficulty = document.getElementById('grading_difficulty').value || null;
    e.notes = document.getElementById('notes').value || null;
    e.structural_assessments = {{
        spine_condition: document.getElementById('spine_condition').value || null,
        corner_condition: document.getElementById('corner_condition').value || null,
        edge_condition: document.getElementById('edge_condition').value || null,
        page_quality: document.getElementById('page_quality').value || null,
    }};
    const rows = document.querySelectorAll('.defect-row');
    e.known_defects = Array.from(rows).map(r => ({{
        description: r.querySelector('.dd').value,
        defect_chart_keyword: r.querySelector('.dk').value || null,
        severity: r.querySelector('.ds').value,
        zone: r.querySelector('.dz').value || null,
    }})).filter(d => d.description || d.defect_chart_keyword);
    return e;
}}

function saveAndNext() {{
    const data = gather();
    fetch('/save', {{method:'POST', headers:{{'Content-Type':'application/json'}}, body:JSON.stringify({{slug:SLUGS[currentIdx], data:data}})}})
        .then(() => {{ if (currentIdx < SLUGS.length-1) load(currentIdx+1); else alert('Done! All comics annotated.'); }});
}}
function prev() {{ if (currentIdx > 0) {{ gather(); load(currentIdx-1); }} }}

load(0);
</script></body></html>"""


class AnnotationHandler(http.server.BaseHTTPRequestHandler):
    dataset_dir: Path = None
    dataset = None
    keywords: list[str] = []

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            html = _build_html(self.dataset_dir, self.dataset.entries, self.keywords)
            self._respond(200, "text/html", html.encode())
        elif parsed.path.startswith("/images/") or parsed.path.startswith("/reference_covers/"):
            file_path = self.dataset_dir / parsed.path.lstrip("/")
            if file_path.exists():
                self._respond(200, "image/jpeg", file_path.read_bytes())
            else:
                self._respond(404, "text/plain", b"Not found")
        else:
            self._respond(404, "text/plain", b"Not found")

    def do_POST(self):
        if self.path == "/save":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            slug = body["slug"]
            data = body["data"]

            entry = self.dataset.entries.get(slug)
            if entry:
                entry.expected_grade_low = data.get("expected_grade_low")
                entry.expected_grade_high = data.get("expected_grade_high")
                entry.annotator_confidence = data.get("annotator_confidence")
                entry.grading_difficulty = data.get("grading_difficulty")
                entry.notes = data.get("notes")

                sa = data.get("structural_assessments", {})
                if sa:
                    entry.structural_assessments = StructuralAssessments(
                        spine_condition=sa.get("spine_condition"),
                        corner_condition=sa.get("corner_condition"),
                        edge_condition=sa.get("edge_condition"),
                        page_quality=sa.get("page_quality"),
                    )

                entry.known_defects = [
                    DefectAnnotation(
                        description=d.get("description", ""),
                        defect_chart_keyword=d.get("defect_chart_keyword"),
                        severity=d.get("severity", "minor"),
                        zone=d.get("zone"),
                    )
                    for d in data.get("known_defects", [])
                ]

                save_dataset(self.dataset, self.dataset_dir)

            self._respond(200, "application/json", b'{"ok":true}')
        else:
            self._respond(404, "text/plain", b"Not found")

    def _respond(self, code, content_type, body):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # suppress request logs


def run_annotate(args):
    dataset_dir = Path(args.dataset_dir).resolve()
    dataset = load_dataset(dataset_dir)
    keywords = _get_defect_keywords(args)

    port = args.port

    AnnotationHandler.dataset_dir = dataset_dir
    AnnotationHandler.dataset = dataset
    AnnotationHandler.keywords = keywords

    server = http.server.HTTPServer(("127.0.0.1", port), AnnotationHandler)
    url = f"http://127.0.0.1:{port}"
    print(f"\nAnnotation UI running at {url}")
    print(f"Dataset: {dataset_dir.name} ({len(dataset.entries)} entries)")
    print(f"Defect keywords: {len(keywords)} loaded from backend")
    print(f"Press Ctrl+C to stop\n")
    webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()
