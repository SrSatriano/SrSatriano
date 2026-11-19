#!/usr/bin/env python3
"""Gera os visuais e o README do perfil a partir de data/projects.json.

Uso:
    python3 scripts/build_profile.py

Entradas:
    data/projects.json       projetos, frentes, cores e textos
    templates/README.md      texto do README com marcadores {{...}}

Saídas (cada SVG existe em assets/dark/ e assets/light/):
    banner.svg  terminal.svg  cortalive.svg  overview.svg  categories.svg  languages.svg  timeline.svg
    lhn-architecture.svg  constellation.svg  footer.svg
    nav/<id>.svg  sections/<id>.svg  cards/<repo>.svg
    README.md (gerado a partir do template; não edite à mão)

Marcadores do template:
    {{pic:caminho.svg|texto alternativo|largura}}   <picture> com versão clara e escura
    {{STATS}} {{NAV}} {{FEATURED}} {{CATALOG}} {{INDEX}} {{COUNT}} {{UPDATED}}

Só usa a biblioteca padrão.
"""
from __future__ import annotations

import json
import math
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
    "TypeScript": "#3178c6", "JavaScript": "#e3c81b", "Solidity": "#AA6746",
    "Kotlin": "#A97BFF", "Java": "#b07219", "Shell": "#5fb829", "HTML": "#e34c26",
}

MONTHS = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]

MILESTONES = {
    "2023-06": "Primeiros projetos de IA e finanças",
    "2025-02": "Curso de Python (Senac Rio)",
    "2026-04": "LHN Sovereign V90 público",
    "2026-05": "Módulos open source + portfólio",
    "2026-10": "Site do Satriano Studio",
    "2026-11": "CortaLive, ferramentas de produto e apps",
}

THEMES = {
    "dark": dict(
        bg0="#0b1220", bg1="#0f1b2d", panel="#0f172a", track="#111c30", stroke="#1f2a44", stroke2="#334155",
        text="#f8fafc", text2="#e2e8f0", body="#cbd5e1", muted="#94a3b8", faint="#64748b", pill="#1e293b",
        accent="#38bdf8", accent2="#22c55e", glow=0.22, grid="#1e293b", grid_op=0.6,
        hero0="#050816", hero1="#0b1324", hero2="#0c3b3a", title0="#f8fafc", title1="#7dd3fc", halo="#0891b2",
        term="#0a0f1c", term_bar="#111827",
    ),
    "light": dict(
        bg0="#ffffff", bg1="#f4f7fb", panel="#ffffff", track="#eef2f7", stroke="#d0d7de", stroke2="#cbd5e1",
        text="#0f172a", text2="#1e293b", body="#334155", muted="#475569", faint="#64748b", pill="#f1f5f9",
        accent="#0284c7", accent2="#16a34a", glow=0.14, grid="#cbd5e1", grid_op=0.45,
        hero0="#f8fafc", hero1="#eff6ff", hero2="#ccfbf1", title0="#0f172a", title1="#0369a1", halo="#38bdf8",
        term="#0f172a", term_bar="#1e293b",
    ),
}

# Ícones de traço em grade 24x24.
ICONS = {
    "chart": '<path d="M3 17l5-5 4 4 8-8"/><path d="M14 8h6v6"/><path d="M3 21h18"/>',
    "chip": '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/>',
    "play": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
    "cube": '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M12 12l9-5M12 12v10M12 12L3 7"/>',
    "server": '<rect x="4" y="3" width="16" height="7" rx="1.5"/><rect x="4" y="14" width="16" height="7" rx="1.5"/><path d="M8 6.5h.01M8 17.5h.01M12 6.5h4M12 17.5h4"/>',
    "sprout": '<path d="M12 21v-9"/><path d="M12 12c0-4 3-7 8-7 0 4-3 7-8 7z"/><path d="M12 14c0-3-2-6-7-6 0 3 2 6 7 6z"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13"/><path d="M3.5 6h.01M3.5 12h.01M3.5 18h.01"/>',
    "film": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 4v16M17 4v16M3 9h4M3 15h4M17 9h4M17 15h4"/>',
    "wave": '<path d="M3 12h1.5M7 8v8M11 4v16M15 9v6M19 11v2"/>',
    "captions": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 13h4M13 13h4M7 16h10"/>',
    "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16.5l.6 1.7 1.7.6-1.7.6-.6 1.7-.6-1.7-1.7-.6 1.7-.6z"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/>',
    "scissors": '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.1 8.1L20 20M8.1 15.9L20 4"/>',
    "star": '<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z"/>',
}


# --------------------------------------------------------------------------- utilidades

def x(s: str) -> str:
    return escape(s, {'"': "&quot;"})


def ccolor(cat: dict, theme: str) -> str:
    return cat["color"] if theme == "dark" else cat["color_light"]


def icon(name: str, cx: float, cy: float, size: float, color: str, sw: float = 2.0) -> str:
    s = size / 24
    return (f'<g transform="translate({cx - size/2:.1f} {cy - size/2:.1f}) scale({s:.3f})" fill="none" '
            f'stroke="{color}" stroke-width="{sw / s * s:.2f}" stroke-linecap="round" stroke-linejoin="round">'
            f'{ICONS[name]}</g>')


def text_width(s: str, size: float, bold: bool = False) -> float:
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


def svg_open(W: int, H: int, label: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="{x(label)}">')


def panel_bg(t: dict, W: int, H: int, rx: int = 16) -> str:
    return (f'<defs><linearGradient id="pbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg0"]}"/>'
            f'<stop offset="1" stop-color="{t["bg1"]}"/></linearGradient></defs>'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{rx}" fill="url(#pbg)" stroke="{t["stroke"]}"/>')


def frame(t: dict, W: int, H: int, title: str, subtitle: str, label: str, body: str, ico: str | None = None) -> str:
    tx = 28
    head = ""
    if ico:
        head = (f'<rect x="24" y="22" width="38" height="38" rx="10" fill="{t["accent"]}" fill-opacity="0.12" '
                f'stroke="{t["accent"]}" stroke-opacity="0.4"/>' + icon(ico, 43, 41, 20, t["accent"]))
        tx = 76
    return (svg_open(W, H, label) + panel_bg(t, W, H) + head +
            f'<text x="{tx}" y="40" fill="{t["text"]}" font-family="{SANS}" font-size="18" font-weight="700">{x(title)}</text>'
            f'<text x="{tx}" y="60" fill="{t["faint"]}" font-family="{SANS}" font-size="12.5">{x(subtitle)}</text>'
            f'{body}</svg>')


def fmt_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day} {MONTHS[d.month-1]} {d.year}"


def cat_count(cid: str) -> int:
    return sum(1 for p in PROJECTS if p["cat"] == cid)


# --------------------------------------------------------------------------- banner e terminal

def banner_svg(t: dict, n_public: int, n_langs: int) -> str:
    W, H = 1200, 320
    seq = [3, -2, 4, 1, -3, 5, 2, -1, 4, -4, 3, 6, -2, 2, 5, -3, 4, 1, 3, -2, 5, 2, -1, 6, 3, -2, 4, 2]
    closes, acc = [], 0
    for d in seq:
        acc += d
        closes.append(acc)
    lo_v, hi_v = min(closes + [0]), max(closes)

    def py(v: float) -> float:
        return 230 - (v - lo_v) / (hi_v - lo_v) * 160

    up, down = ("#22c55e", "#ef4444") if t is THEMES["dark"] else ("#16a34a", "#dc2626")
    candles, prev = [], 0
    for i, c_v in enumerate(closes):
        o, c = py(prev), py(c_v)
        hi, lo = min(o, c) - 6 - (i % 3) * 3, max(o, c) + 5 + (i % 4) * 2
        cx = 700 + i * 17
        col = up if c < o else down
        candles.append(f'<line x1="{cx}" y1="{hi:.0f}" x2="{cx}" y2="{lo:.0f}" stroke="{col}" stroke-opacity="0.5"/>'
                       f'<rect x="{cx-5}" y="{min(o,c):.0f}" width="10" height="{max(abs(o-c),2):.0f}" rx="1.5" '
                       f'fill="{col}" fill-opacity="0.5"/>')
        prev = c_v
    ma = []
    for i in range(len(closes)):
        win = closes[max(0, i - 3): i + 1]
        ma.append((700 + i * 17, py(sum(win) / len(win))))
    ma_pts = " ".join(f"{a},{b:.0f}" for a, b in ma)
    area_pts = ma_pts + f" {ma[-1][0]},{H} {ma[0][0]},{H}"
    end_x, end_y = ma[-1]
    grid = "".join(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}"/>' for gx in range(0, W, 40)) + \
        "".join(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}"/>' for gy in range(0, H, 40))
    chips = [("C++", "#f34b7d"), ("Rust", "#dea584"), ("Python", "#3572A5"), ("TypeScript", "#3178c6"),
             ("Go", "#00ADD8"), ("Kotlin", "#A97BFF"), ("Solidity", "#AA6746")]
    chip_svg, cx = [], 60
    for label, c in chips:
        w = text_width(label, 13, True) + 34
        chip_svg.append(f'<rect x="{cx}" y="232" width="{w:.0f}" height="30" rx="15" fill="{t["panel"]}" '
                        f'fill-opacity="0.85" stroke="{c}" stroke-opacity="0.75"/><circle cx="{cx+15}" cy="247" r="5" '
                        f'fill="{c}"/><text x="{cx+26}" y="252" fill="{t["text2"]}" font-family="{SANS}" font-size="13" '
                        f'font-weight="600">{label}</text>')
        cx += w + 10
    return f'''{svg_open(W, H, "Matheus Rodrigues Satriano: back-end, sistemas quant, IA local e infraestrutura soberana")}
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t['hero0']}"/><stop offset="0.55" stop-color="{t['hero1']}"/><stop offset="1" stop-color="{t['hero2']}"/></linearGradient>
  <linearGradient id="title" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['title0']}"/><stop offset="1" stop-color="{t['title1']}"/></linearGradient>
  <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t['accent']}" stop-opacity="0"/><stop offset="0.5" stop-color="{t['accent']}" stop-opacity="0.22"/><stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/></linearGradient>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t['accent']}" stop-opacity="0.28"/><stop offset="1" stop-color="{t['accent']}" stop-opacity="0"/></linearGradient>
  <radialGradient id="halo" cx="0.85" cy="0.35" r="0.6"><stop offset="0" stop-color="{t['halo']}" stop-opacity="0.35"/><stop offset="1" stop-color="{t['halo']}" stop-opacity="0"/></radialGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0.15"/><stop offset="0.5" stop-color="#fff" stop-opacity="1"/></linearGradient>
  <mask id="gm"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <g stroke="{t['grid']}" stroke-opacity="{t['grid_op']}" mask="url(#gm)">{grid}</g>
  <rect width="{W}" height="{H}" fill="url(#halo)"/>
  <polygon points="{area_pts}" fill="url(#area)"/>
  <g>{"".join(candles)}</g>
  <polyline points="{ma_pts}" fill="none" stroke="{t['accent']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="{end_x}" cy="{end_y:.0f}" r="12" fill="{t['accent']}" fill-opacity="0.2"><animate attributeName="r" values="6;16;6" dur="2.4s" repeatCount="indefinite"/><animate attributeName="fill-opacity" values="0.35;0;0.35" dur="2.4s" repeatCount="indefinite"/></circle>
  <circle cx="{end_x}" cy="{end_y:.0f}" r="5" fill="{t['accent']}"/>
  <rect x="-200" y="0" width="200" height="{H}" fill="url(#scan)"><animate attributeName="x" from="-200" to="{W}" dur="7s" repeatCount="indefinite"/></rect>
  <text x="60" y="78" fill="{t['accent']}" font-family="{MONO}" font-size="15" letter-spacing="2">$ whoami --perfil {OWNER}<tspan fill="{t['accent']}">▍<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan></text>
  <text x="60" y="134" fill="url(#title)" font-family="{SANS}" font-size="46" font-weight="800">Matheus Rodrigues Satriano</text>
  <text x="60" y="174" fill="{t['body']}" font-family="{SANS}" font-size="21">Back-end · sistemas quant · IA local · infraestrutura soberana</text>
  <text x="60" y="210" fill="{t['faint']}" font-family="{SANS}" font-size="15">{n_public} projetos públicos · {len(CATS)} frentes · {n_langs} linguagens · documentação em português</text>
  {"".join(chip_svg)}
</g>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{t['stroke']}"/>
</svg>'''


def terminal_svg(t: dict) -> str:
    W = 1000
    green, blue, amber = "#4ade80", "#7dd3fc", "#fbbf24"
    lines = [
        ("$ ", "cat foco.txt", amber, "#e2e8f0"),
        ("› ", "LHN Sovereign V90 · terminal quant local com IA e risco", blue, "#e2e8f0"),
        ("› ", "C++ · Rust · Python · TypeScript · Go · Kotlin", blue, "#e2e8f0"),
        ("› ", "baixa latência · RAG offline · fiscal BR · Web3 · apps Android", blue, "#e2e8f0"),
        ("$ ", "cortalive cortar live.mp4", amber, "#e2e8f0"),
        ("› ", "10 cortes verticais prontos · legenda, capa e texto do post", "#f472b6", "#e2e8f0"),
        ("$ ", "echo $PRINCIPIO", amber, "#e2e8f0"),
        ("› ", "Se o problema não precisa sair da máquina, ele roda local.", green, "#f8fafc"),
    ]
    total = 20.0
    H = 60 + len(lines) * 29 + 34
    out = [svg_open(W, H, "Terminal: " + " / ".join(l[1] for l in lines)),
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{t["term"]}" stroke="{t["stroke"]}"/>',
           f'<path d="M0.5 14.5a14 14 0 0 1 14-14h{W-29}a14 14 0 0 1 14 14v19.5h-{W-1}z" fill="{t["term_bar"]}"/>',
           '<circle cx="24" cy="17" r="6" fill="#ff5f57"/><circle cx="44" cy="17" r="6" fill="#febc2e"/>'
           '<circle cx="64" cy="17" r="6" fill="#28c840"/>',
           f'<text x="{W/2}" y="22" text-anchor="middle" fill="#94a3b8" font-family="{MONO}" font-size="12">'
           f'satriano@lhn: ~/perfil</text>', "<defs>"]
    starts, cur = [], 0.4
    for prompt, body, _, _ in lines:
        full = len(prompt + body) * 9.4 + 24
        dur = max(0.5, len(body) * 0.035)
        starts.append((cur, cur + dur, full))
        cur += dur + (0.6 if prompt == "$ " else 0.25)
    for i, (a, b, full) in enumerate(starts):
        out.append(f'<clipPath id="c{i}"><rect x="30" y="{48 + i*29}" width="{full:.0f}" height="26">'
                   f'<animate attributeName="width" values="0;0;{full:.0f};{full:.0f}" '
                   f'keyTimes="0;{a/total:.3f};{b/total:.3f};1" dur="{total}s" repeatCount="indefinite"/></rect></clipPath>')
    out.append("</defs>")
    for i, (prompt, body, pc, bc) in enumerate(lines):
        y = 66 + i * 29
        out.append(f'<g clip-path="url(#c{i})"><text x="34" y="{y}" font-family="{MONO}" font-size="15">'
                   f'<tspan fill="{pc}" font-weight="700">{x(prompt)}</tspan><tspan fill="{bc}">{x(body)}</tspan></text></g>')
    out.append(f'<rect x="34" y="{66 + len(lines)*29 - 15}" width="9" height="18" fill="{green}">'
               f'<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    out.append("</svg>")
    return "\n".join(out)


def footer_svg(t: dict) -> str:
    W, H = 1200, 130
    def wave(amp: float, y0: float, period: float) -> str:
        pts = [f"M0 {H}", f"L0 {y0}"]
        xx = 0.0
        while xx <= W * 2 + period:
            pts.append(f"Q{xx + period/4:.0f} {y0 - amp} {xx + period/2:.0f} {y0} T{xx + period:.0f} {y0}")
            xx += period
        pts.append(f"L{W*2 + period:.0f} {H}Z")
        return " ".join(pts)
    cols = [t["accent"], "#14b8a6", "#0891b2"]
    layers = []
    for i, (amp, y0, per, dur, op) in enumerate([(14, 58, 300, 16, 0.25), (10, 74, 240, 11, 0.4), (8, 92, 200, 8, 0.85)]):
        layers.append(f'<path d="{wave(amp, y0, per)}" fill="{cols[i]}" fill-opacity="{op}">'
                      f'<animateTransform attributeName="transform" type="translate" from="0 0" to="-{per*2} 0" '
                      f'dur="{dur}s" repeatCount="indefinite"/></path>')
    return (svg_open(W, H, "") + f'<defs><clipPath id="c"><rect width="{W}" height="{H}"/></clipPath></defs>'
            f'<g clip-path="url(#c)">{"".join(layers)}</g>'
            f'<text x="{W/2}" y="{H-14}" text-anchor="middle" fill="#ffffff" font-family="{SANS}" font-size="13" '
            f'font-weight="600" letter-spacing="2">OBRIGADO PELA VISITA · {OWNER.upper()}</text></svg>')


# --------------------------------------------------------------------------- cards, faixas e navegação

def card_svg(t: dict, p: dict, theme: str) -> str:
    cat = CATS[p["cat"]]
    color = ccolor(cat, theme)
    W, H = 460, 200
    out = [svg_open(W, H, f'{p["title"]}: {p["summary"]}'),
           "<defs>",
           f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg0"]}"/>'
           f'<stop offset="1" stop-color="{t["bg1"]}"/></linearGradient>',
           f'<radialGradient id="glow" cx="1" cy="0" r="0.9"><stop offset="0" stop-color="{color}" '
           f'stop-opacity="{t["glow"]}"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>',
           f'<pattern id="dots" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" '
           f'fill="{color}" fill-opacity="0.35"/></pattern>',
           '<linearGradient id="fd" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.9"/>'
           '<stop offset="0.6" stop-color="#fff" stop-opacity="0"/></linearGradient>',
           f'<mask id="m"><rect width="{W}" height="{H}" fill="url(#fd)"/></mask>',
           "</defs>",
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#bg)" stroke="{t["stroke"]}"/>',
           f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="url(#glow)"/>',
           f'<rect x="{W-200}" y="1" width="199" height="{H-2}" rx="14" fill="url(#dots)" mask="url(#m)"/>',
           f'<rect x="0" y="20" width="4" height="{H-40}" rx="2" fill="{color}"/>',
           f'<rect x="20" y="16" width="30" height="30" rx="8" fill="{color}" fill-opacity="0.14" stroke="{color}" '
           f'stroke-opacity="0.45"/>', icon(cat["icon"], 35, 31, 17, color),
           f'<text x="60" y="36" fill="{color}" font-family="{SANS}" font-size="11" font-weight="700" '
           f'letter-spacing="1.2">{x(cat["short"].upper())}</text>']
    pills = []
    if p.get("new"):
        pills.append(("NOVO", "#ef4444" if theme == "dark" else "#dc2626"))
    if p.get("featured") and not p.get("new"):
        pills.append(("★ DESTAQUE", "#f59e0b"))
    if p.get("ci"):
        pills.append(("CI", t["accent2"]))
    if p.get("demo"):
        pills.append(("ONLINE", t["accent"]))
    if p.get("license"):
        pills.append((p["license"].upper(), t["muted"]))
    px = W - 18
    for label, c in pills:
        w = text_width(label, 9.5, True) + 14
        px -= w
        out.append(f'<rect x="{px:.1f}" y="21" width="{w:.1f}" height="19" rx="9.5" fill="{c}" fill-opacity="0.13" '
                   f'stroke="{c}" stroke-opacity="0.55"/><text x="{px + w/2:.1f}" y="34" text-anchor="middle" '
                   f'fill="{c}" font-family="{SANS}" font-size="9.5" font-weight="700">{x(label)}</text>')
        px -= 6
    out.append(f'<text x="22" y="74" fill="{t["text"]}" font-family="{SANS}" font-size="19" font-weight="700">'
               f'{x(p["title"])}</text>')
    repo = f'{OWNER}/{p["name"]}'
    if text_width(repo, 11.5) > W - 44:
        repo = repo[: int((W - 44) / 6.4)] + "…"
    out.append(f'<text x="22" y="93" fill="{t["faint"]}" font-family="{MONO}" font-size="11.5">{x(repo)}</text>')
    for i, line in enumerate(wrap(p["summary"], 12.5, W - 44, 3)):
        out.append(f'<text x="22" y="{117 + i*17}" fill="{t["body"]}" font-family="{SANS}" font-size="12.5">'
                   f'{x(line)}</text>')
    lc = LANG_COLORS.get(p["lang"], "#94a3b8")
    out.append(f'<line x1="20" y1="{H-44}" x2="{W-20}" y2="{H-44}" stroke="{t["stroke"]}"/>')
    out.append(f'<circle cx="28" cy="{H-22}" r="5.5" fill="{lc}"/>')
    out.append(f'<text x="39" y="{H-18}" fill="{t["text2"]}" font-family="{SANS}" font-size="12" font-weight="600">'
               f'{x(p["lang"])}</text>')
    sx = 39 + text_width(p["lang"], 12, True) + 14
    for s in p["stack"]:
        if s == p["lang"]:
            continue
        w = text_width(s, 10.5) + 14
        if sx + w > W - 16:
            break
        out.append(f'<rect x="{sx:.1f}" y="{H-33}" width="{w:.1f}" height="20" rx="6" fill="{t["pill"]}" '
                   f'stroke="{t["stroke2"]}"/><text x="{sx + w/2:.1f}" y="{H-19}" text-anchor="middle" '
                   f'fill="{t["muted"]}" font-family="{SANS}" font-size="10.5">{x(s)}</text>')
        sx += w + 6
    out.append("</svg>")
    return "\n".join(out)


def section_svg(t: dict, cat: dict, theme: str) -> str:
    W, H = 1000, 112
    c = ccolor(cat, theme)
    n = cat_count(cat["id"])
    intro = wrap(cat["intro"], 12.5, W - 290, 2)
    return (svg_open(W, H, f'{cat["title"]}: {n} projetos') +
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c}" '
            f'stop-opacity="0.22"/><stop offset="0.65" stop-color="{c}" stop-opacity="0"/></linearGradient></defs>'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="{t["bg0"]}" stroke="{t["stroke"]}"/>'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#g)"/>'
            f'<rect x="0" y="20" width="5" height="{H-40}" rx="2.5" fill="{c}"/>'
            f'<circle cx="56" cy="{H/2}" r="27" fill="{c}" fill-opacity="0.14" stroke="{c}" stroke-opacity="0.5"/>'
            + icon(cat["icon"], 56, H / 2, 26, c) +
            f'<text x="98" y="44" fill="{t["text"]}" font-family="{SANS}" font-size="23" font-weight="700">{x(cat["title"])}</text>'
            + "".join(f'<text x="98" y="{68 + i*17}" fill="{t["muted"]}" font-family="{SANS}" font-size="12.5">{x(l)}</text>'
                      for i, l in enumerate(intro)) +
            f'<rect x="{W-152}" y="{H/2-17}" width="126" height="34" rx="17" fill="{c}" fill-opacity="0.14" '
            f'stroke="{c}" stroke-opacity="0.6"/><text x="{W-89}" y="{H/2+5}" text-anchor="middle" fill="{c}" '
            f'font-family="{SANS}" font-size="14" font-weight="700">{n} projeto{"s" if n > 1 else ""}</text></svg>')


def nav_svg(t: dict, title: str, sub: str, ico: str, c: str) -> str:
    W, H = 250, 104
    return (svg_open(W, H, f"{title}: {sub}") +
            f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c}" '
            f'stop-opacity="0.2"/><stop offset="0.7" stop-color="{c}" stop-opacity="0"/></linearGradient></defs>'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="{t["bg0"]}" stroke="{t["stroke"]}"/>'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="url(#g)"/>'
            f'<rect x="0.5" y="{H-5}" width="{W-1}" height="4.5" rx="2" fill="{c}" fill-opacity="0.8"/>'
            f'<rect x="18" y="18" width="40" height="40" rx="12" fill="{c}" fill-opacity="0.15" stroke="{c}" '
            f'stroke-opacity="0.5"/>' + icon(ico, 38, 38, 22, c) +
            f'<text x="18" y="83" fill="{t["text"]}" font-family="{SANS}" font-size="15" font-weight="700">{x(title)}</text>'
            f'<text x="70" y="36" fill="{c}" font-family="{SANS}" font-size="22" font-weight="800">{x(sub.split()[0])}</text>'
            f'<text x="70" y="52" fill="{t["muted"]}" font-family="{SANS}" font-size="11">{x(" ".join(sub.split()[1:]))}</text>'
            f'<text x="{W-22}" y="42" text-anchor="end" fill="{c}" font-family="{SANS}" font-size="20">→</text></svg>')


# --------------------------------------------------------------------------- gráficos

def overview_svg(t: dict, stats: list[tuple[str, str, str, str]]) -> str:
    W, H = 1000, 176
    n, gap, pad = len(stats), 14, 24
    tw = (W - 2 * pad - gap * (n - 1)) / n
    body = []
    for i, (val, label, color, ico) in enumerate(stats):
        tx = pad + i * (tw + gap)
        body.append(f'<rect x="{tx:.1f}" y="84" width="{tw:.1f}" height="70" rx="12" fill="{t["panel"]}" '
                    f'stroke="{t["stroke"]}"/><rect x="{tx:.1f}" y="84" width="4" height="70" rx="2" fill="{color}"/>')
        body.append(icon(ico, tx + tw - 22, 104, 16, color, 2.2))
        body.append(f'<text x="{tx+18:.1f}" y="119" fill="{color}" font-family="{SANS}" font-size="27" '
                    f'font-weight="800">{x(val)}</text>')
        body.append(f'<text x="{tx+18:.1f}" y="140" fill="{t["muted"]}" font-family="{SANS}" font-size="11.5">{x(label)}</text>')
    label = "; ".join(f"{v} {l}" for v, l, _, _ in stats)
    return frame(t, W, H, "Em números", f"Retrato dos repositórios públicos em {fmt_date(DATA['updated'])}", label,
                 "\n".join(body), "chart")


def bars_svg(t: dict, title: str, subtitle: str, rows: list[tuple[str, int, str, str | None]],
             label_w: int, ico: str) -> str:
    W, row_h = 1000, 36
    H = 96 + row_h * len(rows) + 12
    mx = max(v for _, v, _, _ in rows)
    bar_max = W - label_w - 80
    body = []
    for i, (name, v, c, ic) in enumerate(rows):
        y = 94 + i * row_h
        w = max(bar_max * v / mx, 8)
        tx = 28
        if ic:
            body.append(icon(ic, 38, y + 12, 16, c))
            tx = 56
        body.append(f'<text x="{tx}" y="{y+17}" fill="{t["text2"]}" font-family="{SANS}" font-size="13.5">{x(name)}</text>')
        body.append(f'<rect x="{label_w}" y="{y+2}" width="{bar_max}" height="20" rx="10" fill="{t["track"]}"/>')
        body.append(f'<rect x="{label_w}" y="{y+2}" width="{w:.1f}" height="20" rx="10" fill="{c}"/>')
        body.append(f'<text x="{label_w + w + 10:.1f}" y="{y+17}" fill="{t["text"]}" font-family="{SANS}" '
                    f'font-size="13" font-weight="700">{v}</text>')
    label = f"{title}: " + ", ".join(f"{n} {v}" for n, v, _, _ in rows)
    return frame(t, W, H, title, subtitle, label, "\n".join(body), ico)


def timeline_svg(t: dict, theme: str) -> str:
    by_month: dict[str, list[dict]] = {}
    for p in PROJECTS:
        by_month.setdefault(p["created"][:7], []).append(p)
    keys = sorted(by_month)
    W, H, pad, axis_y = 1000, 310, 105, 160
    step = (W - 2 * pad) / (len(keys) - 1)
    body = [f'<line x1="{pad-30}" y1="{axis_y}" x2="{W-pad+30}" y2="{axis_y}" stroke="{t["stroke2"]}" stroke-width="2" '
            f'stroke-dasharray="2 6" stroke-linecap="round"/>']
    for i, k in enumerate(keys):
        cx = pad + i * step
        items = sorted(by_month[k], key=lambda p: list(CATS).index(p["cat"]))
        y, m = k.split("-")
        body.append(f'<circle cx="{cx:.1f}" cy="{axis_y}" r="9" fill="{t["bg0"]}" stroke="{t["accent"]}" stroke-width="3"/>'
                    f'<circle cx="{cx:.1f}" cy="{axis_y}" r="3.5" fill="{t["accent"]}"/>')
        body.append(f'<text x="{cx:.1f}" y="{axis_y-24}" text-anchor="middle" fill="{t["text"]}" font-family="{SANS}" '
                    f'font-size="14" font-weight="700">{MONTHS[int(m)-1]} {y}</text>')
        tag = f'+{len(items)} repo{"s" if len(items) > 1 else ""}'
        tw = text_width(tag, 11.5, True) + 16
        body.append(f'<rect x="{cx - tw/2:.1f}" y="{axis_y-66}" width="{tw:.1f}" height="20" rx="10" fill="{t["accent"]}" '
                    f'fill-opacity="0.14"/><text x="{cx:.1f}" y="{axis_y-52}" text-anchor="middle" fill="{t["accent"]}" '
                    f'font-family="{SANS}" font-size="11.5" font-weight="700">{tag}</text>')
        per_row = 8
        for j, p in enumerate(items):
            r_, c_ = divmod(j, per_row)
            n_in_row = min(per_row, len(items) - r_ * per_row)
            dx = cx - (n_in_row - 1) * 7 + c_ * 14
            body.append(f'<circle cx="{dx:.1f}" cy="{axis_y + 30 + r_*14}" r="5" fill="{ccolor(CATS[p["cat"]], theme)}"/>')
        base = axis_y + 30 + ((len(items) - 1) // per_row) * 14 + 26
        for li, line in enumerate(wrap(MILESTONES.get(k, ""), 11.5, step - 8, 2)):
            body.append(f'<text x="{cx:.1f}" y="{base + li*15}" text-anchor="middle" fill="{t["muted"]}" '
                        f'font-family="{SANS}" font-size="11.5">{x(line)}</text>')
    lx = 28
    for c in CATS.values():
        body.append(f'<circle cx="{lx+5}" cy="{H-22}" r="5" fill="{ccolor(c, theme)}"/>'
                    f'<text x="{lx+15}" y="{H-18}" fill="{t["muted"]}" font-family="{SANS}" font-size="11">{x(c["short"])}</text>')
        lx += text_width(c["short"], 11) + 34
    label = "Linha do tempo: " + "; ".join(f"{k}: {len(by_month[k])} repositórios" for k in keys)
    return frame(t, W, H, "Linha do tempo", "Quando cada repositório público nasceu (um ponto por projeto, cor = frente)",
                 label, "\n".join(body), "star")


# --------------------------------------------------------------------------- diagramas

def box(t: dict, bx: float, by: float, w: float, h: float, title: str, sub: str, c: str, ico: str) -> str:
    return (f'<rect x="{bx}" y="{by}" width="{w}" height="{h}" rx="12" fill="{t["panel"]}" stroke="{c}" '
            f'stroke-opacity="0.65" stroke-width="1.5"/>'
            f'<rect x="{bx}" y="{by}" width="{w}" height="{h}" rx="12" fill="{c}" fill-opacity="0.07"/>'
            + icon(ico, bx + 24, by + h / 2, 18, c) +
            f'<text x="{bx+44}" y="{by + h/2 - 3}" fill="{t["text"]}" font-family="{SANS}" font-size="14" '
            f'font-weight="700">{x(title)}</text>'
            f'<text x="{bx+44}" y="{by + h/2 + 14}" fill="{t["muted"]}" font-family="{SANS}" font-size="11">{x(sub)}</text>')


def flow(x1, y1, x2, y2, c, dash=True, dur=1.2) -> str:
    mx = (x1 + x2) / 2
    d = f"M{x1} {y1} C{mx} {y1} {mx} {y2} {x2} {y2}"
    anim = (f'<animate attributeName="stroke-dashoffset" from="20" to="0" dur="{dur}s" repeatCount="indefinite"/>'
            if dash else "")
    return (f'<path d="{d}" fill="none" stroke="{c}" stroke-opacity="0.25" stroke-width="5"/>'
            f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="6 4">{anim}</path>'
            f'<circle cx="{x2}" cy="{y2}" r="3.5" fill="{c}"/>')


def cortalive_svg(t: dict, theme: str) -> str:
    """Arte de destaque do CortaLive: fluxo de corte + celular com o corte vertical."""
    W, H = 1000, 430
    dark = theme == "dark"
    pink = "#f472b6" if dark else "#db2777"
    amber = "#fbbf24" if dark else "#d97706"
    red = "#ef4444" if dark else "#dc2626"
    bg0, bg1, bg2 = ("#12091a", "#1a0f24", "#2a1020") if dark else ("#fff7fb", "#fdf2f8", "#ffedd5")
    out = [svg_open(W, H, "CortaLive: transforma vídeos e lives em cortes verticais com legenda e IA. "
                          "Fluxo: vídeo ou live, picos de áudio, transcrição local com Whisper, IA dá nota de 0 a 10, "
                          "corte vertical 1080x1920. Básico grátis e MIT; Pro grava lives e publica sozinho."),
           f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="0.6" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
  <linearGradient id="tt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{pink}"/><stop offset="1" stop-color="{amber}"/></linearGradient>
  <radialGradient id="halo" cx="0.8" cy="0.5" r="0.45"><stop offset="0" stop-color="{pink}" stop-opacity="{0.35 if dark else 0.25}"/><stop offset="1" stop-color="{pink}" stop-opacity="0"/></radialGradient>
  <linearGradient id="game" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1e3a8a"/><stop offset="1" stop-color="#7c3aed"/></linearGradient>
  <linearGradient id="cam" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#334155"/><stop offset="1" stop-color="#0f172a"/></linearGradient>
  <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.1" fill="{pink}" fill-opacity="0.22"/></pattern>
  <clipPath id="clip"><rect width="{W}" height="{H}" rx="20"/></clipPath>
  <clipPath id="scr"><rect x="702" y="44" width="212" height="352" rx="22"/></clipPath>
</defs>''',
           '<g clip-path="url(#clip)">',
           f'<rect width="{W}" height="{H}" fill="url(#bg)"/><rect width="{W}" height="{H}" fill="url(#dots)" opacity="0.6"/>',
           f'<rect width="{W}" height="{H}" fill="url(#halo)"/>']
    # selo e título
    out.append(f'<rect x="40" y="34" width="176" height="28" rx="14" fill="{red}" fill-opacity="0.14" stroke="{red}" '
               f'stroke-opacity="0.6"/><circle cx="56" cy="48" r="4.5" fill="{red}"><animate attributeName="opacity" '
               f'values="1;0.25;1" dur="1.4s" repeatCount="indefinite"/></circle>'
               f'<text x="68" y="53" fill="{red}" font-family="{SANS}" font-size="12.5" font-weight="800" '
               f'letter-spacing="1.5">NOVO · {MONTHS[10].upper()} 2026</text>')
    out.append(icon("scissors", 62, 104, 34, pink, 2.2))
    out.append(f'<text x="90" y="118" fill="url(#tt)" font-family="{SANS}" font-size="50" font-weight="900">CortaLive</text>')
    out.append(f'<text x="40" y="156" fill="{t["text"]}" font-family="{SANS}" font-size="19" font-weight="600">'
               f'Vídeos e lives viram cortes verticais com legenda e IA.</text>')
    out.append(f'<text x="40" y="180" fill="{t["muted"]}" font-family="{SANS}" font-size="13.5">'
               f'Prontos para TikTok, YouTube Shorts e Instagram Reels · roda no seu PC</text>')
    # fluxo em 5 passos
    steps = [("film", "Vídeo ou", "live gravada"), ("wave", "Picos de", "áudio"), ("captions", "Whisper", "no seu PC"),
             ("spark", "IA dá nota", "de 0 a 10"), ("phone", "Corte 9:16", "1080×1920")]
    bw, gap, sx, sy = 92, 15, 40, 206
    for i, (ic, l1, l2) in enumerate(steps):
        bx = sx + i * (bw + gap)
        out.append(f'<rect x="{bx}" y="{sy}" width="{bw}" height="98" rx="14" fill="{t["panel"]}" fill-opacity="0.8" '
                   f'stroke="{pink}" stroke-opacity="0.45"/>')
        out.append(f'<circle cx="{bx + bw/2}" cy="{sy + 30}" r="18" fill="{pink}" fill-opacity="0.14"/>'
                   + icon(ic, bx + bw / 2, sy + 30, 20, pink))
        out.append(f'<text x="{bx + bw/2}" y="{sy + 68}" text-anchor="middle" fill="{t["text"]}" font-family="{SANS}" '
                   f'font-size="12" font-weight="700">{x(l1)}</text><text x="{bx + bw/2}" y="{sy + 84}" '
                   f'text-anchor="middle" fill="{t["muted"]}" font-family="{SANS}" font-size="11">{x(l2)}</text>')
        out.append(f'<text x="{bx + 10}" y="{sy + 17}" fill="{pink}" font-family="{MONO}" font-size="10" '
                   f'font-weight="700" opacity="0.8">0{i+1}</text>')
        if i < len(steps) - 1:
            ax = bx + bw + gap / 2
            out.append(f'<path d="M{ax-3} {sy+44} l5 5 -5 5" fill="none" stroke="{pink}" stroke-width="2" '
                       f'stroke-linecap="round" stroke-linejoin="round"><animate attributeName="opacity" '
                       f'values="0.3;1;0.3" dur="1.5s" begin="{i*0.3}s" repeatCount="indefinite"/></path>')
    # planos
    plans = [("Básico", "grátis · código aberto (MIT)", "corta vídeos e lives que você já tem", t["accent2"]),
             ("Pro", f'{DATA["cortalive"]["price"]} · até 4K', "grava lives, lê o chat e publica sozinho", amber)]
    for i, (name, tag, desc, c) in enumerate(plans):
        px = 40 + i * 268
        out.append(f'<rect x="{px}" y="324" width="256" height="70" rx="14" fill="{t["panel"]}" fill-opacity="0.85" '
                   f'stroke="{c}" stroke-opacity="0.6"/><rect x="{px}" y="324" width="5" height="70" rx="2.5" fill="{c}"/>'
                   f'<text x="{px+20}" y="350" fill="{c}" font-family="{SANS}" font-size="16" font-weight="800">{name}</text>'
                   f'<text x="{px+20 + text_width(name, 16, True) + 10:.0f}" y="350" fill="{t["muted"]}" '
                   f'font-family="{SANS}" font-size="11.5">{x(tag)}</text>'
                   f'<text x="{px+20}" y="374" fill="{t["body"]}" font-family="{SANS}" font-size="12.5">{x(desc)}</text>')
    # celular
    out.append(f'<rect x="692" y="34" width="232" height="372" rx="32" fill="#0b0b10" stroke="{pink}" '
               f'stroke-opacity="0.55" stroke-width="2"/>')
    out.append('<g clip-path="url(#scr)">')
    # webcam
    out.append('<rect x="702" y="44" width="212" height="150" fill="url(#cam)"/>'
               '<circle cx="808" cy="112" r="26" fill="#94a3b8"/><ellipse cx="808" cy="186" rx="52" ry="38" fill="#94a3b8"/>'
               '<circle cx="799" cy="108" r="3" fill="#0f172a"/><circle cx="817" cy="108" r="3" fill="#0f172a"/>'
               '<ellipse cx="808" cy="124" rx="7" ry="5" fill="#0f172a"><animate attributeName="ry" values="5;8;5" '
               'dur="1.2s" repeatCount="indefinite"/></ellipse>')
    # jogo
    out.append('<rect x="702" y="194" width="212" height="202" fill="url(#game)"/>'
               '<polygon points="702,330 750,280 790,312 840,262 914,326 914,396 702,396" fill="#312e81" opacity="0.9"/>'
               '<polygon points="702,360 770,322 830,352 880,330 914,346 914,396 702,396" fill="#1e1b4b"/>'
               f'<circle cx="850" cy="300" r="16" fill="{amber}" opacity="0.9"><animate attributeName="r" values="10;24;10" '
               f'dur="1.6s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.95;0.2;0.95" dur="1.6s" '
               f'repeatCount="indefinite"/></circle>')
    # título de gancho
    out.append('<rect x="716" y="58" width="184" height="26" rx="6" fill="#000" fill-opacity="0.55"/>'
               f'<text x="808" y="76" text-anchor="middle" fill="#fff" font-family="{SANS}" font-size="12.5" '
               f'font-weight="900" letter-spacing="0.5">ELE NÃO ACREDITOU</text>')
    # legenda palavra a palavra
    words = [("QUE", 731), ("JOGADA", 791), ("INSANA", 866)]
    for i, (w_, wx) in enumerate(words):
        vals = ";".join("#fde047" if j == i else "#ffffff" for j in range(3)) + ";" + ("#fde047" if i == 0 else "#ffffff")
        out.append(f'<text x="{wx}" y="236" text-anchor="middle" fill="#ffffff" stroke="#000" stroke-width="3" '
                   f'paint-order="stroke" font-family="{SANS}" font-size="15" font-weight="900">{w_}'
                   f'<animate attributeName="fill" values="{vals}" dur="2.4s" calcMode="discrete" '
                   f'repeatCount="indefinite"/></text>')
    # reações
    out.append(f'<path d="M896 300c-4-5-12-1-9 5l9 8 9-8c3-6-5-10-9-5z" fill="{red}"><animateTransform '
               f'attributeName="transform" type="translate" values="0 10;0 -40" dur="2.2s" repeatCount="indefinite"/>'
               f'<animate attributeName="opacity" values="1;0" dur="2.2s" repeatCount="indefinite"/></path>')
    # barra de progresso
    out.append('<rect x="716" y="380" width="184" height="4" rx="2" fill="#ffffff" fill-opacity="0.25"/>'
               f'<rect x="716" y="380" width="120" height="4" rx="2" fill="{pink}"><animate attributeName="width" '
               f'values="0;184" dur="6s" repeatCount="indefinite"/></rect>')
    out.append('</g>')
    out.append('<rect x="776" y="38" width="64" height="10" rx="5" fill="#0b0b10"/>')
    # etiquetas ao lado do celular
    for i, (lbl, c) in enumerate([("9:16", pink), ("legenda", amber), ("capa + post", t["accent"])]):
        ty = 120 + i * 48
        w_ = text_width(lbl, 11.5, True) + 22
        out.append(f'<rect x="{678 - w_:.0f}" y="{ty}" width="{w_:.0f}" height="26" rx="13" fill="{t["panel"]}" '
                   f'stroke="{c}" stroke-opacity="0.7"/><text x="{678 - w_/2:.0f}" y="{ty+17}" text-anchor="middle" '
                   f'fill="{c}" font-family="{SANS}" font-size="11.5" font-weight="700">{x(lbl)}</text>')
    out.append('</g>')
    out.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="{pink}" stroke-opacity="0.45"/>')
    out.append("</svg>")
    return "\n".join(out)


def lhn_svg(t: dict, theme: str) -> str:
    W, H = 1000, 400
    q = ccolor(CATS["quant"], theme)
    a = ccolor(CATS["ai"], theme)
    inf = ccolor(CATS["infra"], theme)
    amber = "#f59e0b" if theme == "dark" else "#d97706"
    red = "#ef4444" if theme == "dark" else "#dc2626"
    body = []
    # clientes
    body.append(box(t, 30, 110, 210, 62, "Painel Next.js", "porta 9090 · operação", q, "chart"))
    body.append(box(t, 30, 228, 210, 62, "LHN Mirror", "Android · rede local", q, "play"))
    # núcleo
    body.append(f'<rect x="350" y="120" width="250" height="160" rx="18" fill="{q}" fill-opacity="0.10" stroke="{q}" '
                f'stroke-width="2"/>' + icon("server", 475, 158, 30, q) +
                f'<text x="475" y="200" text-anchor="middle" fill="{t["text"]}" font-family="{SANS}" font-size="19" '
                f'font-weight="800">Core FastAPI</text>'
                f'<text x="475" y="222" text-anchor="middle" fill="{t["muted"]}" font-family="{SANS}" font-size="12">'
                f'porta 9002 · orquestração e execução</text>'
                f'<text x="475" y="250" text-anchor="middle" fill="{q}" font-family="{MONO}" font-size="11">'
                f'replay · backfill · radar · labeler</text>')
    # serviços
    right = [("Bybit V5", "REST + WebSocket", amber, "chart", 40),
             ("Motor de risco", "limites e kill switch", red, "cube", 128),
             ("IA local", "Keras / TensorFlow", a, "chip", 216),
             ("Workspace local", "persistência e auditoria", inf, "server", 304)]
    for title, sub, c, ic, by in right:
        body.append(box(t, 720, by, 250, 58, title, sub, c, ic))
        body.append(flow(600, 200, 720, by + 29, c))
    body.append(flow(240, 141, 350, 180, q))
    body.append(flow(240, 259, 350, 220, q))
    body.append(f'<text x="30" y="40" fill="{t["text"]}" font-family="{SANS}" font-size="18" font-weight="700">'
                f'Arquitetura do LHN Sovereign V90</text>'
                f'<text x="30" y="62" fill="{t["faint"]}" font-family="{SANS}" font-size="12.5">'
                f'O operador decide; o sistema mede, executa e registra tudo localmente.</text>')
    body.append(f'<text x="30" y="{H-22}" fill="{t["faint"]}" font-family="{SANS}" font-size="11.5">'
                f'Logs, replay e auditoria ficam no workspace local · licença PolyForm Noncommercial</text>')
    label = ("Arquitetura do LHN: painel Next.js e app Android falam com o core FastAPI, que integra Bybit V5, "
             "motor de risco, IA local e workspace local")
    return svg_open(W, H, label) + panel_bg(t, W, H) + "".join(body) + "</svg>"


def short_title(p: dict) -> str:
    s = p["title"].split(":")[0]
    return s if len(s) <= 25 else s[:24] + "…"


def constellation_svg(t: dict, theme: str) -> str:
    W, H = 1000, 940
    cx, cy, R_hub, R_node = 500, 478, 150, 262
    cats = list(CATS.values())
    slots = len(PROJECTS) + len(cats)
    step = 2 * math.pi / slots
    body = [f'<circle cx="{cx}" cy="{cy}" r="{R_node}" fill="none" stroke="{t["stroke2"]}" stroke-dasharray="2 8"/>',
            f'<circle cx="{cx}" cy="{cy}" r="{R_hub}" fill="none" stroke="{t["stroke"]}" stroke-dasharray="3 7"/>']
    hubs, slot = [], 0.5
    for cat in cats:
        c = ccolor(cat, theme)
        items = [p for p in PROJECTS if p["cat"] == cat["id"]]
        angs = [-math.pi / 2 + (slot + j) * step for j in range(len(items))]
        slot += len(items) + 1
        ha = sum(angs) / len(angs)
        hx, hy = cx + R_hub * math.cos(ha), cy + R_hub * math.sin(ha)
        hubs.append((cat, c, hx, hy))
        # arco da frente
        a0, a1 = angs[0] - step * 0.45, angs[-1] + step * 0.45
        ra = R_node + 2
        large = 1 if a1 - a0 > math.pi else 0
        body.append(f'<path d="M{cx + ra*math.cos(a0):.1f} {cy + ra*math.sin(a0):.1f} A{ra} {ra} 0 {large} 1 '
                    f'{cx + ra*math.cos(a1):.1f} {cy + ra*math.sin(a1):.1f}" fill="none" stroke="{c}" '
                    f'stroke-width="4" stroke-linecap="round" stroke-opacity="0.55"/>')
        body.append(f'<line x1="{cx}" y1="{cy}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{c}" stroke-opacity="0.45" '
                    f'stroke-width="1.5" stroke-dasharray="4 5"/>')
        for p, a in zip(items, angs):
            px, py = cx + R_node * math.cos(a), cy + R_node * math.sin(a)
            mx, my = cx + (R_hub + 50) * math.cos(a), cy + (R_hub + 50) * math.sin(a)
            body.append(f'<path d="M{hx:.1f} {hy:.1f} Q{mx:.1f} {my:.1f} {px:.1f} {py:.1f}" fill="none" stroke="{c}" '
                        f'stroke-opacity="0.35"/>')
            feat = p.get("featured")
            if feat:
                body.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="10" fill="{c}" fill-opacity="0.18"/>')
            body.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{6 if feat else 4.5}" fill="{c}" '
                        f'stroke="{t["bg0"]}" stroke-width="1.5"/>')
            deg = math.degrees(a)
            right = math.cos(a) >= 0
            lr = R_node + 16
            lx, ly = cx + lr * math.cos(a), cy + lr * math.sin(a)
            rot = deg if right else deg + 180
            body.append(f'<text x="{lx:.1f}" y="{ly:.1f}" transform="rotate({rot:.1f} {lx:.1f} {ly:.1f})" '
                        f'text-anchor="{"start" if right else "end"}" dominant-baseline="central" '
                        f'fill="{t["text2"] if feat else t["muted"]}" font-family="{SANS}" font-size="11.5" '
                        f'font-weight="{700 if feat else 400}">{x(short_title(p))}</text>')
    for cat, c, hx, hy in hubs:
        body.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="25" fill="{t["bg0"]}" stroke="{c}" stroke-width="2"/>'
                    f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="25" fill="{c}" fill-opacity="0.15"/>'
                    + icon(cat["icon"], hx, hy, 22, c))
    q = ccolor(CATS["quant"], theme)
    body.append(f'<circle cx="{cx}" cy="{cy}" r="64" fill="{q}" fill-opacity="0.08"><animate attributeName="r" '
                f'values="58;72;58" dur="4s" repeatCount="indefinite"/></circle>'
                f'<circle cx="{cx}" cy="{cy}" r="50" fill="{t["bg0"]}" stroke="{q}" stroke-width="2.5"/>'
                f'<text x="{cx}" y="{cy-4}" text-anchor="middle" fill="{t["text"]}" font-family="{SANS}" font-size="18" '
                f'font-weight="800">LHN</text><text x="{cx}" y="{cy+14}" text-anchor="middle" fill="{q}" '
                f'font-family="{SANS}" font-size="10.5" font-weight="700">SOVEREIGN V90</text>')
    lx = 28
    for cat in cats:
        c = ccolor(cat, theme)
        body.append(icon(cat["icon"], lx + 8, H - 26, 14, c) +
                    f'<text x="{lx+20}" y="{H-22}" fill="{t["muted"]}" font-family="{SANS}" font-size="11.5">'
                    f'{x(cat["short"])} ({cat_count(cat["id"])})</text>')
        lx += text_width(f'{cat["short"]} (00)', 11.5) + 40
    head = (f'<text x="28" y="40" fill="{t["text"]}" font-family="{SANS}" font-size="18" font-weight="700">'
            f'Constelação de projetos</text><text x="28" y="62" fill="{t["faint"]}" font-family="{SANS}" '
            f'font-size="12.5">{len(PROJECTS)} repositórios públicos em {len(CATS)} frentes, em órbita do LHN · '
            f'nomes em destaque = projetos recomendados</text>')
    return svg_open(W, H, f"Constelação dos {len(PROJECTS)} repositórios públicos por frente") + \
        panel_bg(t, W, H) + head + "".join(body) + "</svg>"


# --------------------------------------------------------------------------- README

def pic(path: str, alt: str, width: str = "100%") -> str:
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/dark/{path}" />'
            f'<source media="(prefers-color-scheme: light)" srcset="assets/light/{path}" />'
            f'<img src="assets/dark/{path}" alt="{x(alt)}" width="{width}" /></picture>')


def _esc(s: str) -> str:
    return quote(s.replace("-", "--").replace("_", "__"), safe="")


def shield(label: str, message: str | None, color: str, style: str = "flat-square") -> str:
    path = _esc(label) if message is None else f"{_esc(label)}-{_esc(message)}"
    return f"https://img.shields.io/badge/{path}-{color.lstrip('#')}?style={style}"


def repo_links(p: dict) -> str:
    url = f"{GH}/{p['name']}"
    links = [f'<a href="{url}">📂 Código</a>', f'<a href="{url}#readme">📖 README</a>']
    if p.get("download"):
        links.append(f'<a href="{p["download"]}">⬇️ Baixar</a>')
    if p.get("demo"):
        links.append(f'<a href="{p["demo"]}">🌐 Site</a>')
    links += [f'<a href="{url}/commits">🕒 Commits</a>', f'<a href="{url}/issues">💬 Issues</a>']
    return " · ".join(links)


def detail_cell(p: dict) -> str:
    url = f"{GH}/{p['name']}"
    hl = "\n".join(f"<li>{x(h)}</li>" for h in p["highlights"])
    stack = " ".join(f"<code>{x(s)}</code>" for s in p["stack"])
    ci = ""
    if p.get("ci"):
        wf = f"{url}/actions/workflows/{p['ci']}"
        ci = f'<a href="{wf}"><img src="{wf}/badge.svg" alt="CI de {x(p["name"])}" /></a> '
    lic = (f'<img src="{shield("licença", p["license"], "#475569")}" alt="Licença {x(p["license"])}" /> '
           if p.get("license") else "")
    return (f'<h4><a href="{url}">{x(p["title"])}</a></h4>\n{ci}{lic}\n<ul>\n{hl}\n</ul>\n'
            f'<sub><b>Stack:</b> {stack}</sub><br/>\n<sub>{repo_links(p)}</sub>')


def catalog_md() -> str:
    parts = []
    for cid, cat in CATS.items():
        items = [p for p in PROJECTS if p["cat"] == cid]
        parts.append(f'<a id="frente-{cid}"></a>\n\n{pic(f"sections/{cid}.svg", cat["title"] + ": " + str(len(items)) + " projetos")}\n')
        parts.append(f'<details open>\n<summary><b>{cat["emoji"]} {x(cat["title"])}: ver os {len(items)} projetos</b></summary>\n<br/>\n')
        parts.append('<table>')
        for p in items:
            parts.append(
                f'<tr>\n<td width="48%" valign="top"><a href="{GH}/{p["name"]}">'
                f'{pic(f"cards/{p["name"]}.svg", p["title"] + ": " + p["summary"])}</a></td>\n'
                f'<td valign="top">\n\n{detail_cell(p)}\n\n</td>\n</tr>')
        parts.append('</table>\n\n</details>\n\n<p align="right"><a href="#topo">⬆ voltar ao topo</a></p>\n')
    return "\n".join(parts)


def featured_md() -> str:
    feats = [p for p in PROJECTS if p.get("featured") and p["name"] != "LHN-V90-IA"]
    feats.sort(key=lambda p: not p.get("new"))
    rows = []
    for i in range(0, len(feats), 2):
        cells = "".join(f'<td width="50%"><a href="{GH}/{p["name"]}">'
                        f'{pic(f"cards/{p["name"]}.svg", p["title"] + ": " + p["summary"])}</a></td>'
                        for p in feats[i:i + 2])
        rows.append(f"<tr>{cells}</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def nav_md() -> str:
    tiles = [(f"#frente-{cid}", f"nav/{cid}.svg", f'{c["title"]}: {cat_count(cid)} projetos') for cid, c in CATS.items()]
    tiles.append(("#indice", "nav/indice.svg", f"Índice A–Z: {len(PROJECTS)} projetos"))
    return "\n".join(f'<a href="{href}">{pic(path, alt, "24%")}</a>' for href, path, alt in tiles)


def index_md() -> str:
    lines = ["| Projeto | Frente | Linguagem | O que é | Links |", "|---|---|:---:|---|---|"]
    for cid, cat in CATS.items():
        for p in [q for q in PROJECTS if q["cat"] == cid]:
            first = p["summary"].split(". ")[0].split(": ")[0].rstrip(".")
            if len(first) > 110:
                first = first[:107].rsplit(" ", 1)[0] + "…"
            ci = " · ✅ CI" if p.get("ci") else ""
            if p.get("new"):
                first = "🔥 **Novo.** " + first
            demo = f" · [🌐]({p['demo']})" if p.get("demo") else ""
            lines.append(f"| [{p['title']}]({GH}/{p['name']}) | {cat['emoji']} {cat['short']} | {p['lang']} | "
                         f"{first} | [código]({GH}/{p['name']}){demo}{ci} |")
    return "\n".join(lines)


def stats_md(n: int, n_langs: int, n_ci: int, n_mit: int) -> str:
    items = [("repos públicos", str(n), "#22c55e"), ("frentes", str(len(CATS)), "#38bdf8"),
             ("linguagens", str(n_langs), "#a78bfa"), ("CI no GitHub Actions", str(n_ci), "#2dd4bf"),
             ("licença MIT", str(n_mit), "#f59e0b"), ("docs", "pt-BR", "#64748b")]
    return "\n".join(f'<img src="{shield(l, m, c)}" alt="{x(l)}: {x(m)}" />' for l, m, c in items)


def promo_active(today: date | None = None) -> dict | None:
    """Cupom do CortaLive, só enquanto estiver no prazo."""
    promo = DATA.get("cortalive", {}).get("promo")
    if not promo:
        return None
    return promo if (today or date.today()) <= date.fromisoformat(promo["until"]) else None


def cortalive_blocks() -> dict[str, str]:
    cl = DATA["cortalive"]
    promo = promo_active()
    sc = cl["showcase"]
    price_cell = f'{cl["price"]}<br/><sub>pagamento único</sub>'
    promo_md = ""
    buy_label = f'Comprar o Pro · {cl["price"]}'
    if promo:
        d, m = promo["until"][8:10], promo["until"][5:7]
        price_cell = (f'~~{cl["price"]}~~ **{promo["price"]}**<br/><sub>com o cupom <code>{promo["code"]}</code> '
                      f'até {d}/{m}</sub>')
        promo_md = (f'> [!TIP]\n> **Cupom `{promo["code"]}`:** {promo["discount"]} de desconto no Pro até '
                    f'{promo["until_label"]}. Sai por **{promo["price"]}** à vista ou {promo["installments"]} '
                    f'(preço cheio: {cl["price"]} ou {cl["installments"]}). No checkout, clique em '
                    f'“Aplicar cupom” e digite o código.\n')
        buy_label = f'Comprar o Pro · {promo["price"]} com cupom'
    return {
        "CL_PRICE_CELL": price_cell,
        "CL_PROMO": promo_md,
        "CL_BUY_BADGE": (f'<a href="{cl["site"]}"><img src="{shield(buy_label, None, "#d97706", "for-the-badge")}'
                         f'&logo=githubpages&logoColor=white" alt="{x(buy_label)}" /></a>'),
        "CL_SITE": cl["site"],
        "CL_SINCE": cl["live_since"],
        "CL_SHOWCASE": sc["name"],
        "CL_TIKTOK": sc["tiktok"],
        "CL_YOUTUBE": sc["youtube"],
        "CL_INSTAGRAM": sc["instagram"],
    }


def render_readme(blocks: dict[str, str]) -> str:
    tpl = (ROOT / "templates" / "README.md").read_text(encoding="utf-8")

    def sub_pic(m: re.Match) -> str:
        parts = [s.strip() for s in m.group(1).split("|")]
        return pic(parts[0], parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else "100%")

    out = re.sub(r"\{\{pic:([^}]*)\}\}", sub_pic, tpl)
    for k, v in blocks.items():
        out = out.replace("{{" + k + "}}", v)
    left = re.findall(r"\{\{[^}]*\}\}", out)
    if left:
        raise SystemExit(f"marcadores sem valor no template: {left}")
    return ("<!-- Gerado por scripts/build_profile.py a partir de templates/README.md e data/projects.json. "
            "Não edite à mão. -->\n" + out)


def main() -> None:
    names = [p["name"] for p in PROJECTS]
    assert len(names) == len(set(names)), "projeto duplicado no JSON"
    for p in PROJECTS:
        assert p["cat"] in CATS, f"frente desconhecida em {p['name']}"

    n = len(PROJECTS)
    langs = Counter(p["lang"] for p in PROJECTS if not p.get("no_lang"))
    n_ci = sum(1 for p in PROJECTS if p.get("ci"))
    n_mit = sum(1 for p in PROJECTS if p.get("license") == "MIT")

    for theme, t in THEMES.items():
        base = ROOT / "assets" / theme
        files: dict[str, str] = {
            "banner.svg": banner_svg(t, n, len(langs)),
            "terminal.svg": terminal_svg(t),
            "footer.svg": footer_svg(t),
            "overview.svg": overview_svg(t, [
                (str(n), "repositórios públicos", "#22c55e" if theme == "dark" else "#16a34a", "list"),
                (str(len(CATS)), "frentes de trabalho", t["accent"], "cube"),
                (str(len(langs)), "linguagens principais", "#a78bfa" if theme == "dark" else "#7c3aed", "chip"),
                (str(n_ci), "com CI automatizado", "#2dd4bf" if theme == "dark" else "#0d9488", "server"),
                (str(n_mit), "licenciados como MIT", "#f59e0b" if theme == "dark" else "#d97706", "briefcase"),
                ("100%", "docs em português", "#f472b6" if theme == "dark" else "#db2777", "sprout"),
            ]),
            "categories.svg": bars_svg(t, "Projetos por frente", "Cada repositório público aparece em uma frente principal",
                                       [(c["title"], cat_count(cid), ccolor(c, theme), c["icon"]) for cid, c in CATS.items()],
                                       350, "cube"),
            "languages.svg": bars_svg(t, "Linguagem principal", "Linguagem predominante de cada repositório, segundo o GitHub",
                                      [(lang, v, LANG_COLORS.get(lang, "#94a3b8"), None) for lang, v in langs.most_common()],
                                      150, "chip"),
            "timeline.svg": timeline_svg(t, theme),
            "lhn-architecture.svg": lhn_svg(t, theme),
            "cortalive.svg": cortalive_svg(t, theme),
            "constellation.svg": constellation_svg(t, theme),
        }
        for p in PROJECTS:
            files[f"cards/{p['name']}.svg"] = card_svg(t, p, theme)
        for cid, cat in CATS.items():
            files[f"sections/{cid}.svg"] = section_svg(t, cat, theme)
            files[f"nav/{cid}.svg"] = nav_svg(t, cat["short"], f"{cat_count(cid)} projetos", cat["icon"], ccolor(cat, theme))
        files["nav/indice.svg"] = nav_svg(t, "Índice A–Z", f"{n} projetos", "list", t["text2"] if theme == "light" else "#e2e8f0")
        for sub in ("cards", "sections", "nav"):
            for old in (base / sub).glob("*.svg"):
                old.unlink()
        for rel, content in files.items():
            path = base / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    readme = render_readme({
        "STATS": stats_md(n, len(langs), n_ci, n_mit),
        "NAV": nav_md(),
        "FEATURED": featured_md(),
        "CATALOG": catalog_md(),
        "INDEX": index_md(),
        "COUNT": str(n),
        "UPDATED": fmt_date(DATA["updated"]),
        **cortalive_blocks(),
    })
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"ok: {n} projetos, {len(langs)} linguagens, {n_ci} com CI, {n_mit} MIT, temas: {', '.join(THEMES)}")


if __name__ == "__main__":
    main()
