"""Собирает дело в один самодостаточный index.html.

Запуск:  python3 engine/build.py case-001
Берёт engine/template.html, подставляет стикеры из cases/<дело>/stickers/*.png
вместо {{имя}}, {{имя.w}}, {{имя.h}} и пишет результат в <дело>/index.html.
Нужен Pillow: pip install pillow
"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
case = sys.argv[1] if len(sys.argv) > 1 else "case-001"
template = (ROOT / "engine" / "template.html").read_text(encoding="utf-8")

imgs = {}
for png in sorted((ROOT / "cases" / case / "stickers").glob("*.png")):
    im = Image.open(png).convert("RGBA")
    box = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    im = im.crop(box)
    if im.width > 600:
        im = im.resize((600, round(im.height * 600 / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=76, method=6)
    imgs[png.stem] = {"uri": "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode(), "w": im.width, "h": im.height}

def sub(m):
    item = imgs[m.group(1)]
    return str(item[m.group(2)]) if m.group(2) else item["uri"]

body = re.sub(r"\{\{(\w+)(?:\.(w|h))?\}\}", sub, template)
page = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="theme-color" content="#382C29">\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
out = ROOT / case / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"{out.relative_to(ROOT)}: {len(page.encode()) // 1024} KB, стикеров: {len(imgs)}")
