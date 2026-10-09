"""Generates the flat-colour editorial illustrations used as image placeholders.
Solid fills only (no gradients). Replace any file in frontend/img with a real photograph of the same name."""
import os, sys, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.utils.text import slugify
from blog.seed_data import ARTICLES

OUT = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'img')
os.makedirs(OUT, exist_ok=True)
W, H = 1600, 1000
P = dict(ivory='#F4EEE4', stone='#D9CDBB', clay='#B9795A', terra='#A8553A', olive='#6E6B3F', sage='#A9B39A', brown='#6B4A38', esp='#2A1F1A', sand='#E6D9C3')
SETS = {
 'mind': ('clay', 'ivory', 'brown', 'sand'), 'body': ('sage', 'terra', 'esp', 'ivory'),
 'nourish': ('sand', 'olive', 'terra', 'brown'), 'ritual': ('brown', 'sand', 'clay', 'ivory'),
 'relationships': ('stone', 'terra', 'olive', 'ivory'), 'rest': ('olive', 'sand', 'sage', 'esp'),
}
def svg(body, bg, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
            f'<rect width="{W}" height="{H}" fill="{P[bg]}"/>{body}</svg>')
def comp(style, c):
    a, b, d = P[c[1]], P[c[2]], P[c[3]]
    if style == 0:  # arch + sun
        return f'<rect x="0" y="720" width="{W}" height="280" fill="{b}"/><path d="M420 720V420a230 230 0 0 1 460 0v300z" fill="{a}"/><circle cx="1150" cy="300" r="120" fill="{d}"/>'
    if style == 1:  # horizon bands
        return f'<rect y="560" width="{W}" height="140" fill="{a}"/><rect y="700" width="{W}" height="300" fill="{b}"/><circle cx="520" cy="400" r="190" fill="{d}"/>'
    if style == 2:  # overlapping circles
        return f'<circle cx="640" cy="500" r="330" fill="{a}"/><circle cx="1010" cy="520" r="260" fill="{b}"/><rect x="0" y="860" width="{W}" height="140" fill="{d}"/>'
    if style == 3:  # tall arches
        return f'<path d="M260 1000V480a160 160 0 0 1 320 0v520z" fill="{a}"/><path d="M660 1000V320a200 200 0 0 1 400 0v680z" fill="{b}"/><path d="M1160 1000V560a140 140 0 0 1 280 0v440z" fill="{d}"/>'
    if style == 4:  # window frame
        return f'<rect x="420" y="140" width="760" height="720" fill="{d}"/><rect x="450" y="170" width="340" height="320" fill="{a}"/><rect x="810" y="170" width="340" height="320" fill="{b}"/><rect x="450" y="510" width="700" height="320" fill="{a}"/><rect y="860" width="{W}" height="140" fill="{b}"/>'
    return f'<path d="M0 760C300 640 600 860 900 740S1400 700 1600 760V1000H0z" fill="{a}"/><path d="M0 860C300 760 700 940 1000 840S1450 820 1600 860V1000H0z" fill="{b}"/><circle cx="1180" cy="330" r="140" fill="{d}"/>'
n = 0
for i, (title, cat, ed, days, feat, exc, alt, body) in enumerate(ARTICLES):
    slug = slugify(title)[:50].rstrip('-'); c = SETS[cat]
    open(os.path.join(OUT, slug + '.svg'), 'w').write(svg(comp(i % 6, c), c[0], alt)); n += 1
extras = {'hero': ('rest', 0, 'Soft morning light over a quiet room'), 'about': ('ritual', 3, 'A calm interior with warm tones'),
          'practice': ('nourish', 4, 'A window with warm afternoon light')}
for k, (cat, st, alt) in extras.items():
    c = SETS[cat]; open(os.path.join(OUT, k + '.svg'), 'w').write(svg(comp(st, c), c[0], alt)); n += 1
for j, cat in enumerate(SETS):
    c = SETS[cat]; open(os.path.join(OUT, 'cat-' + cat + '.svg'), 'w').write(svg(comp((j + 1) % 6, c), c[0], cat.title())); n += 1
for j, k in enumerate(['therapy', 'nutrition', 'movement', 'mindfulness', 'consultation']):
    c = list(SETS.values())[j]; open(os.path.join(OUT, 'svc-' + k + '.svg'), 'w').write(svg(comp((j + 2) % 6, c), c[0], k)); n += 1
for j, k in enumerate(['p1', 'p2', 'p3', 'p4']):
    c = list(SETS.values())[(j + 2) % 6]; open(os.path.join(OUT, 'person-' + k + '.svg'), 'w').write(svg(comp((j + 3) % 6, c), c[0], 'Portrait placeholder')); n += 1
print('wrote', n, 'images')
