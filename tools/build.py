"""Assemble le cours à partir des fichiers de src/.

Usage :
    python3 tools/build.py index.html --standalone   # page HTML complète, à ouvrir dans un navigateur
    python3 tools/build.py cours.html                 # contenu seul (sans <html>/<head>), pour une publication en artifact

Les fichiers src/*.html sont lus dans l'ordre alphabétique et concaténés :
- 00_styles.html contient le <title>, les polices et toute la feuille de style ;
- 10_ à 60_ contiennent les modules, dans l'ordre du cours ;
- 90_ et 91_ contiennent les scripts (quiz, progression, démos).
Le code placé dans les balises <code> est écrit tel quel dans les sources
et échappé ici. Le sommaire et le pied de chaque module sont générés.
"""
import argparse
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

STANDALONE_HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
"""


def escape_code(doc: str) -> str:
    def esc(m):
        inner = html.escape(html.unescape(m.group(2)), quote=False)
        return m.group(1) + inner + m.group(3)
    return re.sub(r"(<code\b[^>]*>)(.*?)(</code>)", esc, doc, flags=re.S)


def add_navigation(doc: str) -> tuple[str, int]:
    mods = re.findall(r'<section class="module" id="(m\d\d)" data-short="([^"]+)">', doc)
    nav = "\n".join(
        f'      <li><a href="#{mid}" data-id="{mid}"><span class="toc-num">{mid[1:]}</span>'
        f'<span class="toc-label">{label}</span><span class="toc-check" aria-hidden="true"></span></a></li>'
        for mid, label in mods
    )
    doc = doc.replace("<!--NAV-->", nav)
    for i, (mid, _label) in enumerate(mods):
        if i + 1 < len(mods):
            nid, nlabel = mods[i + 1]
            nxt = f'<a class="next-link" href="#{nid}">Module suivant : {nid[1:]} · {nlabel} →</a>'
        else:
            nxt = '<a class="next-link" href="#top">Revenir au début ↑</a>'
        end = (
            f'<div class="module-end"><button type="button" class="mark-read" data-id="{mid}" '
            f'aria-pressed="false">Marquer ce module comme lu</button>{nxt}</div>\n</section>'
        )
        marker = f"</section><!--/{mid}-->"
        assert marker in doc, f"marqueur manquant : {marker}"
        doc = doc.replace(marker, end)
    return doc, len(mods)


def build(standalone: bool) -> tuple[str, int]:
    parts = sorted(SRC.glob("*.html"))
    doc = "".join(p.read_text(encoding="utf-8") for p in parts)
    doc = escape_code(doc)
    doc, count = add_navigation(doc)
    if standalone:
        split = doc.index('<div class="shell">')
        head, body = doc[:split], doc[split:]
        doc = STANDALONE_HEAD + head + "</head>\n<body>\n" + body + "</body>\n</html>\n"
    return doc, count


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("output", help="fichier HTML à produire")
    parser.add_argument("--standalone", action="store_true", help="produire une page HTML complète")
    args = parser.parse_args()
    doc, count = build(args.standalone)
    out = pathlib.Path(args.output)
    out.write_text(doc, encoding="utf-8")
    print(f"{out} : {count} modules, {len(doc.encode()) // 1024} Ko")


if __name__ == "__main__":
    main()
