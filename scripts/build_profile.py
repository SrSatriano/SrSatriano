#!/usr/bin/env python3
"""Gera os visuais e o catálogo do README do perfil a partir de data/projects.json.

Uso:
    python3 scripts/build_profile.py

O que ele escreve:
    assets/banner.svg            cabeçalho do perfil
    assets/overview.svg          números principais
    assets/categories.svg        projetos por frente
    assets/languages.svg         projetos por linguagem principal
    assets/timeline.svg          linha do tempo de criação
    assets/sections/<id>.svg     faixa de título de cada frente
    assets/cards/<repo>.svg      card de cada repositório
    README.md                    trechos entre os marcadores <!-- X:START --> e <!-- X:END -->

Só usa a biblioteca padrão. Para adicionar ou mudar um projeto, edite o JSON e rode de novo.
"""
from __future__ import annotations

import json
import re
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data" / "projects.json").read_text(encoding="utf-8"))
OWNER = DATA["owner"]
CATS = OrderedDict((c["id"], c) for c in DATA["categories"])
PROJECTS = DATA["projects"]
GH = f"https://github.com/{OWNER}"

SANS = "'Segoe UI', Ubuntu, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"

LANG_COLORS = {
    "Python": "#3572A5", "C++": "#f34b7d", "Rust": "#dea584", "Go": "#00ADD8",
    "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "Solidity": "#AA6746",
    "Kotlin": "#A97BFF", "Java": "#b07219", "Shell": "#89e051", "HTML": "#e34c26",
}

MONTHS = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

# Rótulos da linha do tempo, por ano-mês de criação.
MILESTONES = {
    "2023-06": "Primeiros projetos de IA e finanças",
    "2025-02": "Curso de Python (Senac Rio)",
    "2026-04": "LHN Sovereign V90 público",
    "2026-05": "Módulos open source + portfólio",
    "2026-10": "Site do Satriano Studio",
    "2026-11": "Ferramentas de produto e apps",
}


def x(s: str) -> str:
    return escape(s, {'"': "&quot;"})


def text_width(s: str, size: float, bold: bool = False) -> float:
    """Largura aproximada de um texto em fonte sans-serif."""
    w = 0.0
    for ch in s:
        if ch in "il.,:;|!'’ ":
            w += 0.30
        elif ch in "mwMW@":
            w += 0.86
        elif ch.isupper() or ch.isdigit():
            w += 0.64
        else:
            w += 0.53
    return w * size * (1.06 if bold else 1.0)


def wrap(s: str, size: float, max_w: float, max_lines: int) -> list[str]:
    words, lines, cur = s.split(), [], ""
    for wd in words:
        trial = f"{cur} {wd}".strip()
        if text_width(trial, size) <= max_w:
            cur = trial
            continue
        lines.append(cur)
        cur = wd
        if len(lines) == max_lines:
            break
    else:
        lines.append(cur)
        return [l for l in lines if l]
    last = lines[-1]
    while last and text_width(last + " …", size) > max_w:
        last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
    lines[-1] = last.rstrip(",;:") + " …"
    return lines


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# --------------------------------------------------------------------------- cards

def card_svg(p: dict) -> str:
    cat = CATS[p["cat"]]
    color = cat["color"]
    W, H = 460, 190
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-label="{x(p["title"])}: {x(p["summary"])}">',
        "<defs>",
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/>'
        f'<stop offset="1" stop-color="#111a2e"/></linearGradient>',
        f'<radialGradient id="glow" cx="1" cy="0" r="0.9"><stop offset="0" stop-color="{color}" stop-opacity="0.22"/>'
        f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>',
        "</defs>",
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#bg)" stroke="#1f2a44"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#glow)"/>',
        f'<rect x="0" y="18" width="4" height="{H-36}" rx="2" fill="{color}"/>',
    ]
    # topo: frente + selos
    out.append(f'<text x="22" y="30" fill="{color}" font-family="{SANS}" font-size="11" font-weight="700" '
               f'letter-spacing="1.2">{x(cat["short"].upper())}</text>')
    pills = []
    if p.get("featured"):
        pills.append(("DESTAQUE", "#fbbf24"))
    if p.get("ci"):
        pills.append(("CI", "#22c55e"))
    if p.get("demo"):
        pills.append(("ONLINE", "#38bdf8"))
    if p.get("license"):
        pills.append((p["license"].upper(), "#94a3b8"))
    px = W - 18
    for label, c in pills:
        w = text_width(label, 9.5, True) + 14
        px -= w
        out.append(f'<rect x="{px:.1f}" y="17" width="{w:.1f}" height="18" rx="9" fill="{c}" fill-opacity="0.14" '
                   f'stroke="{c}" stroke-opacity="0.55"/>')
        out.append(f'<text x="{px + w/2:.1f}" y="29.5" text-anchor="middle" fill="{c}" font-family="{SANS}" '
                   f'font-size="9.5" font-weight="700">{x(label)}</text>')
        px -= 6
    # título e repo
    out.append(f'<text x="22" y="58" fill="#f8fafc" font-family="{SANS}" font-size="19" font-weight="700">'
               f'{x(p["title"])}</text>')
    repo = f'{OWNER}/{p["name"]}'
    if text_width(repo, 11.5) > W - 44:
        repo = repo[: int((W - 44) / 6.4)] + "…"
    out.append(f'<text x="22" y="77" fill="#64748b" font-family="{MONO}" font-size="11.5">{x(repo)}</text>')
    # resumo
    for i, line in enumerate(wrap(p["summary"], 12.5, W - 44, 3)):
        out.append(f'<text x="22" y="{101 + i*17}" fill="#cbd5e1" font-family="{SANS}" font-size="12.5">'
                   f'{x(line)}</text>')
    # rodapé: linguagem + stack
    lc = LANG_COLORS.get(p["lang"], "#94a3b8")
    out.append(f'<circle cx="28" cy="{H-22}" r="5.5" fill="{lc}"/>')
    out.append(f'<text x="39" y="{H-18}" fill="#e2e8f0" font-family="{SANS}" font-size="12" font-weight="600">'
               f'{x(p["lang"])}</text>')
    sx = 39 + text_width(p["lang"], 12, True) + 14
    for s in p["stack"]:
        if s == p["lang"]:
            continue
        w = text_width(s, 10.5) + 14
        if sx + w > W - 16:
            break
        out.append(f'<rect x="{sx:.1f}" y="{H-33}" width="{w:.1f}" height="20" rx="6" fill="#1e293b" stroke="#334155"/>')
        out.append(f'<text x="{sx + w/2:.1f}" y="{H-19}" text-anchor="middle" fill="#94a3b8" font-family="{SANS}" '
                   f'font-size="10.5">{x(s)}</text>')
        sx += w + 6
    out.append("</svg>")
    return "\n".join(out)


# --------------------------------------------------------------------------- banner

def banner_svg(n_public: int, n_langs: int) -> str:
    W, H = 1200, 320
    # candles decorativos determinísticos
    seq = [3, -2, 4, 1, -3, 5, 2, -1, 4, -4, 3, 6, -2, 2, 5, -3, 4, 1, 3, -2, 5, 2, -1, 6, 3, -2, 4, 2]
    closes, acc = [], 0
    for d in seq:
        acc += d
        closes.append(acc)
    lo_v, hi_v = min(closes + [0]), max(closes)
    top, bottom = 70, 230

    def py(v: float) -> float:
        return bottom - (v - lo_v) / (hi_v - lo_v) * (bottom - top)

    candles, prev = [], 0
    for i, c_v in enumerate(closes):
        o, c = py(prev), py(c_v)
        hi, lo = min(o, c) - 6 - (i % 3) * 3, max(o, c) + 5 + (i % 4) * 2
        cx = 700 + i * 17
        col = "#22c55e" if c < o else "#ef4444"
        candles.append(f'<line x1="{cx}" y1="{hi:.0f}" x2="{cx}" y2="{lo:.0f}" stroke="{col}" stroke-opacity="0.5"/>')
        candles.append(f'<rect x="{cx-5}" y="{min(o,c):.0f}" width="10" height="{max(abs(o-c),2):.0f}" rx="1.5" '
                       f'fill="{col}" fill-opacity="0.5"/>')
        prev = c_v
    ma = []
    for i in range(len(closes)):
        win = closes[max(0, i - 3): i + 1]
        ma.append((700 + i * 17, py(sum(win) / len(win))))
    ma_pts = " ".join(f"{a},{b:.0f}" for a, b in ma)
    end_x, end_y = ma[-1]
    grid = "".join(
        f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="#1e293b" stroke-opacity="0.6"/>' for gx in range(0, W, 40)
    ) + "".join(
        f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="#1e293b" stroke-opacity="0.6"/>' for gy in range(0, H, 40)
    )
    chips = [("C++", "#f34b7d"), ("Rust", "#dea584"), ("Python", "#3572A5"), ("TypeScript", "#3178c6"),
             ("Go", "#00ADD8"), ("Kotlin", "#A97BFF"), ("Solidity", "#AA6746")]
    chip_svg, cx = [], 60
    for label, c in chips:
        w = text_width(label, 13, True) + 34
        chip_svg.append(f'<rect x="{cx}" y="232" width="{w:.0f}" height="30" rx="15" fill="#0f172a" stroke="{c}" '
                        f'stroke-opacity="0.7"/><circle cx="{cx+15}" cy="247" r="5" fill="{c}"/>'
                        f'<text x="{cx+26}" y="252" fill="#e2e8f0" font-family="{SANS}" font-size="13" '
                        f'font-weight="600">{label}</text>')
        cx += w + 10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Matheus Rodrigues Satriano: back-end, sistemas quant, IA local e infraestrutura soberana">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#050816"/><stop offset="0.55" stop-color="#0b1324"/><stop offset="1" stop-color="#0c3b3a"/>
  </linearGradient>
  <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#f8fafc"/><stop offset="1" stop-color="#7dd3fc"/>
  </linearGradient>
  <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#38bdf8" stop-opacity="0"/><stop offset="0.5" stop-color="#38bdf8" stop-opacity="0.35"/><stop offset="1" stop-color="#38bdf8" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="halo" cx="0.85" cy="0.4" r="0.6"><stop offset="0" stop-color="#0891b2" stop-opacity="0.35"/><stop offset="1" stop-color="#0891b2" stop-opacity="0"/></radialGradient>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  {grid}
  <rect width="{W}" height="{H}" fill="url(#halo)"/>
  <g>{"".join(candles)}</g>
  <polyline points="{ma_pts}" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" stroke-opacity="0.9"/>
  <circle cx="{end_x}" cy="{end_y:.0f}" r="5" fill="#38bdf8"><animate attributeName="r" values="4;9;4" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0.35;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <rect x="-200" y="0" width="200" height="{H}" fill="url(#scan)"><animate attributeName="x" from="-200" to="{W}" dur="6s" repeatCount="indefinite"/></rect>
  <text x="60" y="78" fill="#38bdf8" font-family="{MONO}" font-size="15" letter-spacing="2">$ whoami --perfil SrSatriano</text>
  <text x="60" y="134" fill="url(#title)" font-family="{SANS}" font-size="46" font-weight="800">Matheus Rodrigues Satriano</text>
  <text x="60" y="174" fill="#cbd5e1" font-family="{SANS}" font-size="21">Back-end · sistemas quant · IA local · infraestrutura soberana</text>
  <text x="60" y="210" fill="#64748b" font-family="{SANS}" font-size="15">{n_public} projetos públicos · {len(CATS)} frentes · {n_langs} linguagens · documentação em português</text>
  {"".join(chip_svg)}
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#1f2a44"/>
</g>
</svg>'''


# --------------------------------------------------------------------------- charts

def frame(W: int, H: int, title: str, subtitle: str, label: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{x(label)}">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#0f1b2d"/></linearGradient></defs>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#bg)" stroke="#1f2a44"/>
<text x="28" y="40" fill="#f8fafc" font-family="{SANS}" font-size="18" font-weight="700">{x(title)}</text>
<text x="28" y="62" fill="#64748b" font-family="{SANS}" font-size="12.5">{x(subtitle)}</text>
{body}
</svg>'''


def overview_svg(stats: list[tuple[str, str, str]]) -> str:
    W, H = 1000, 170
    n = len(stats)
    gap, pad = 14, 28
    tw = (W - 2 * pad - gap * (n - 1)) / n
    body = []
    for i, (val, label, color) in enumerate(stats):
        tx = pad + i * (tw + gap)
        body.append(f'<rect x="{tx:.1f}" y="82" width="{tw:.1f}" height="64" rx="12" fill="#0f172a" stroke="#1e293b"/>')
        body.append(f'<rect x="{tx:.1f}" y="82" width="4" height="64" rx="2" fill="{color}"/>')
        body.append(f'<text x="{tx+18:.1f}" y="115" fill="{color}" font-family="{SANS}" font-size="26" '
                    f'font-weight="800">{x(val)}</text>')
        body.append(f'<text x="{tx+18:.1f}" y="134" fill="#94a3b8" font-family="{SANS}" font-size="11.5">{x(label)}</text>')
    label = "; ".join(f"{v} {l}" for v, l, _ in stats)
    return frame(W, H, "Em números", f"Retrato dos repositórios públicos em {fmt_date(DATA['updated'])}", label,
                 "\n".join(body))


def bars_svg(title: str, subtitle: str, rows: list[tuple[str, int, str]], label_w: int = 260) -> str:
    W = 1000
    row_h = 34
    H = 92 + row_h * len(rows) + 14
    mx = max(v for _, v, _ in rows)
    bar_max = W - label_w - 90
    body = []
    for i, (name, v, c) in enumerate(rows):
        y = 92 + i * row_h
        w = max(bar_max * v / mx, 6)
        body.append(f'<text x="28" y="{y+16}" fill="#e2e8f0" font-family="{SANS}" font-size="13.5">{x(name)}</text>')
        body.append(f'<rect x="{label_w}" y="{y+2}" width="{bar_max}" height="20" rx="6" fill="#111c30"/>')
        body.append(f'<rect x="{label_w}" y="{y+2}" width="{w:.1f}" height="20" rx="6" fill="{c}" fill-opacity="0.9"/>')
        body.append(f'<text x="{label_w + w + 10:.1f}" y="{y+17}" fill="#f8fafc" font-family="{SANS}" font-size="13" '
                    f'font-weight="700">{v}</text>')
    label = f"{title}: " + ", ".join(f"{n} {v}" for n, v, _ in rows)
    return frame(W, H, title, subtitle, label, "\n".join(body))


def timeline_svg() -> str:
    by_month: dict[str, list[dict]] = {}
    for p in PROJECTS:
        by_month.setdefault(p["created"][:7], []).append(p)
    keys = sorted(by_month)
    W, H = 1000, 300
    pad = 105
    step = (W - 2 * pad) / (len(keys) - 1)
    axis_y = 150
    body = [f'<line x1="{pad-20}" y1="{axis_y}" x2="{W-pad+20}" y2="{axis_y}" stroke="#334155" stroke-width="2"/>']
    for i, k in enumerate(keys):
        cx = pad + i * step
        items = sorted(by_month[k], key=lambda p: list(CATS).index(p["cat"]))
        y, m = k.split("-")
        body.append(f'<circle cx="{cx:.1f}" cy="{axis_y}" r="8" fill="#0b1220" stroke="#38bdf8" stroke-width="2.5"/>')
        body.append(f'<text x="{cx:.1f}" y="{axis_y-22}" text-anchor="middle" fill="#f8fafc" font-family="{SANS}" '
                    f'font-size="14" font-weight="700">{MONTHS[int(m)-1]} {y}</text>')
        body.append(f'<text x="{cx:.1f}" y="{axis_y-40}" text-anchor="middle" fill="#38bdf8" font-family="{SANS}" '
                    f'font-size="12" font-weight="700">+{len(items)} repo{"s" if len(items) > 1 else ""}</text>')
        # pontos coloridos por frente
        per_row = 8
        for j, p in enumerate(items):
            r_, c_ = divmod(j, per_row)
            n_in_row = min(per_row, len(items) - r_ * per_row)
            dx = cx - (n_in_row - 1) * 7 + c_ * 14
            body.append(f'<circle cx="{dx:.1f}" cy="{axis_y + 30 + r_*14}" r="5" fill="{CATS[p["cat"]]["color"]}"/>')
        lines = wrap(MILESTONES.get(k, ""), 11.5, step - 8, 2)
        base = axis_y + 30 + ((len(items) - 1) // per_row) * 14 + 26
        for li, line in enumerate(lines):
            body.append(f'<text x="{cx:.1f}" y="{base + li*15}" text-anchor="middle" fill="#94a3b8" '
                        f'font-family="{SANS}" font-size="11.5">{x(line)}</text>')
    # legenda
    lx = 28
    for c in CATS.values():
        body.append(f'<circle cx="{lx+5}" cy="{H-22}" r="5" fill="{c["color"]}"/>')
        body.append(f'<text x="{lx+15}" y="{H-18}" fill="#94a3b8" font-family="{SANS}" font-size="11">{x(c["short"])}</text>')
        lx += text_width(c["short"], 11) + 34
    label = "Linha do tempo: " + "; ".join(f"{k}: {len(by_month[k])} repositórios" for k in keys)
    return frame(W, H, "Linha do tempo", "Quando cada repositório público nasceu (um ponto por projeto, cor = frente)",
                 label, "\n".join(body))


def section_svg(cat: dict, n: int) -> str:
    W, H = 1000, 74
    c = cat["color"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{x(cat["title"])}: {n} projetos">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c}" stop-opacity="0.28"/><stop offset="0.6" stop-color="#0b1220" stop-opacity="1"/></linearGradient></defs>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="#0b1220" stroke="#1f2a44"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#g)"/>
<rect x="0" y="16" width="5" height="{H-32}" rx="2.5" fill="{c}"/>
<text x="28" y="46" fill="#f8fafc" font-family="{SANS}" font-size="22" font-weight="700">{x(cat["title"])}</text>
<rect x="{W-150}" y="21" width="124" height="32" rx="16" fill="{c}" fill-opacity="0.15" stroke="{c}" stroke-opacity="0.6"/>
<text x="{W-88}" y="42" text-anchor="middle" fill="{c}" font-family="{SANS}" font-size="14" font-weight="700">{n} projeto{"s" if n > 1 else ""}</text>
</svg>'''


# --------------------------------------------------------------------------- README

def fmt_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day} {MONTHS[d.month-1]} {d.year}"


def _esc(t: str) -> str:
    return quote(t.replace("-", "--").replace("_", "__"), safe="")


def shield(label: str, message: str | None, color: str, style: str = "flat-square") -> str:
    """URL do shields.io; sem message gera o selo de uma parte só."""
    path = _esc(label) if message is None else f"{_esc(label)}-{_esc(message)}"
    return f"https://img.shields.io/badge/{path}-{color.lstrip('#')}?style={style}"


def repo_links(p: dict) -> str:
    url = f"{GH}/{p['name']}"
    links = [f'<a href="{url}">📂 Código</a>', f'<a href="{url}#readme">📖 README</a>']
    if p.get("demo"):
        links.append(f'<a href="{p["demo"]}">🌐 Online</a>')
    links.append(f'<a href="{url}/commits">🕒 Commits</a>')
    links.append(f'<a href="{url}/issues">💬 Issues</a>')
    return " · ".join(links)


def detail_cell(p: dict) -> str:
    url = f"{GH}/{p['name']}"
    hl = "\n".join(f"<li>{x(h)}</li>" for h in p["highlights"])
    stack = " ".join(f"<code>{x(s)}</code>" for s in p["stack"])
    ci = ""
    if p.get("ci"):
        wf = f"{url}/actions/workflows/{p['ci']}"
        ci = f'<a href="{wf}"><img src="{wf}/badge.svg" alt="CI de {x(p["name"])}" /></a> '
    lic = f'<img src="{shield("licença", p["license"], "#334155")}" alt="Licença {x(p["license"])}" /> ' \
        if p.get("license") else ""
    return (f'<b><a href="{url}">{x(p["title"])}</a></b><br/>\n'
            f'{ci}{lic}\n'
            f'<ul>\n{hl}\n</ul>\n'
            f'<sub><b>Stack:</b> {stack}</sub><br/>\n'
            f'<sub>{repo_links(p)}</sub>')


def catalog_md() -> str:
    parts = []
    for cid, cat in CATS.items():
        items = [p for p in PROJECTS if p["cat"] == cid]
        parts.append(f'<a id="frente-{cid}"></a>\n')
        parts.append(f'<img src="assets/sections/{cid}.svg" alt="{x(cat["title"])}: {len(items)} projetos" width="100%" />\n')
        parts.append(f'> {cat["intro"]}\n')
        parts.append(f'<details open>\n<summary><b>{cat["emoji"]} Ver os {len(items)} projetos de {x(cat["short"])}</b></summary>\n<br/>\n')
        parts.append('<table>')
        for p in items:
            url = f"{GH}/{p['name']}"
            parts.append(
                '<tr>\n'
                f'<td width="48%" valign="top"><a href="{url}"><img src="assets/cards/{p["name"]}.svg" '
                f'alt="{x(p["title"])}: {x(p["summary"])}" width="100%" /></a></td>\n'
                f'<td valign="top">\n\n{detail_cell(p)}\n\n</td>\n'
                '</tr>')
        parts.append('</table>\n\n</details>\n\n<p align="right"><a href="#topo">⬆ voltar ao topo</a></p>\n')
    return "\n".join(parts)


def featured_md() -> str:
    feats = [p for p in PROJECTS if p.get("featured") and p["name"] != "LHN-V90-IA"]
    rows = []
    for i in range(0, len(feats), 2):
        pair = feats[i:i + 2]
        cells = "".join(
            f'<td width="50%"><a href="{GH}/{p["name"]}"><img src="assets/cards/{p["name"]}.svg" '
            f'alt="{x(p["title"])}: {x(p["summary"])}" width="100%" /></a></td>' for p in pair)
        rows.append(f"<tr>{cells}</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def nav_md() -> str:
    cells = []
    for cid, cat in CATS.items():
        n = sum(1 for p in PROJECTS if p["cat"] == cid)
        cells.append(f'<a href="#frente-{cid}"><img src="{shield(cat["emoji"] + " " + cat["short"], str(n), cat["color"], "for-the-badge")}" '
                     f'alt="{x(cat["title"])}: {n} projetos" /></a>')
    return "\n".join(cells)


def index_md() -> str:
    lines = ["| Projeto | Frente | Linguagem | O que é | Links |", "|---|---|:---:|---|---|"]
    for cid, cat in CATS.items():
        for p in [q for q in PROJECTS if q["cat"] == cid]:
            first = p["summary"].split(". ")[0].split(": ")[0].rstrip(".")
            if len(first) > 110:
                first = first[:107].rsplit(" ", 1)[0] + "…"
            ci = " · ✅ CI" if p.get("ci") else ""
            demo = f" · [🌐]({p['demo']})" if p.get("demo") else ""
            lines.append(f"| [{p['title']}]({GH}/{p['name']}) | {cat['emoji']} {cat['short']} | {p['lang']} | "
                         f"{first} | [código]({GH}/{p['name']}){demo}{ci} |")
    return "\n".join(lines)


def stats_badges_md(n: int, n_langs: int, n_ci: int, n_mit: int) -> str:
    items = [
        ("repos públicos", str(n), "#22c55e"),
        ("frentes", str(len(CATS)), "#38bdf8"),
        ("linguagens", str(n_langs), "#a78bfa"),
        ("CI no GitHub Actions", str(n_ci), "#2dd4bf"),
        ("licença MIT", str(n_mit), "#f59e0b"),
        ("docs", "pt-BR", "#64748b"),
    ]
    return "\n".join(f'<img src="{shield(l, m, c)}" alt="{x(l)}: {x(m)}" />' for l, m, c in items)


def replace_block(readme: str, key: str, content: str) -> str:
    pat = re.compile(rf"(<!-- {key}:START -->)(.*?)(<!-- {key}:END -->)", re.S)
    if not pat.search(readme):
        raise SystemExit(f"Marcador {key} não encontrado no README.md")
    return pat.sub(lambda m: f"{m.group(1)}\n{content}\n{m.group(3)}", readme)


def main() -> None:
    names = [p["name"] for p in PROJECTS]
    assert len(names) == len(set(names)), "projeto duplicado no JSON"
    for p in PROJECTS:
        assert p["cat"] in CATS, f"frente desconhecida em {p['name']}"

    n = len(PROJECTS)
    langs = Counter(p["lang"] for p in PROJECTS)
    n_ci = sum(1 for p in PROJECTS if p.get("ci"))
    n_mit = sum(1 for p in PROJECTS if p.get("license") == "MIT")

    assets = ROOT / "assets"
    for old in (assets / "cards").glob("*.svg"):
        old.unlink()
    for p in PROJECTS:
        write(assets / "cards" / f"{p['name']}.svg", card_svg(p))
    for cid, cat in CATS.items():
        write(assets / "sections" / f"{cid}.svg", section_svg(cat, sum(1 for p in PROJECTS if p["cat"] == cid)))

    write(assets / "banner.svg", banner_svg(n, len(langs)))
    write(assets / "overview.svg", overview_svg([
        (str(n), "repositórios públicos", "#22c55e"),
        (str(len(CATS)), "frentes de trabalho", "#38bdf8"),
        (str(len(langs)), "linguagens principais", "#a78bfa"),
        (str(n_ci), "com CI automatizado", "#2dd4bf"),
        (str(n_mit), "licenciados como MIT", "#f59e0b"),
        ("100%", "docs em português", "#f472b6"),
    ]))
    write(assets / "categories.svg", bars_svg(
        "Projetos por frente", "Cada repositório público aparece em uma frente principal",
        [(c["title"], sum(1 for p in PROJECTS if p["cat"] == cid), c["color"]) for cid, c in CATS.items()],
        label_w=330))
    write(assets / "languages.svg", bars_svg(
        "Linguagem principal", "Linguagem predominante de cada repositório, segundo o GitHub",
        [(lang, v, LANG_COLORS.get(lang, "#94a3b8")) for lang, v in langs.most_common()], label_w=150))
    write(assets / "timeline.svg", timeline_svg())

    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme = replace_block(readme, "STATS", stats_badges_md(n, len(langs), n_ci, n_mit))
    readme = replace_block(readme, "NAV", nav_md())
    readme = replace_block(readme, "FEATURED", featured_md())
    readme = replace_block(readme, "CATALOG", catalog_md())
    readme = replace_block(readme, "INDEX", index_md())
    readme_path.write_text(readme, encoding="utf-8")
    print(f"ok: {n} projetos, {len(langs)} linguagens, {n_ci} com CI, {n_mit} MIT")


if __name__ == "__main__":
    main()
