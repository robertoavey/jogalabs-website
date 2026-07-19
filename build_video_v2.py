#!/usr/bin/env python3
# V2-shell video posts (3) + /video-blog/ hub page -> payload PNG.
import io, os, re, json, gzip, struct, zlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))

src = io.open('locations.html', encoding='utf-8').read()
CSS = src.split('<style>', 1)[1].split('</style>', 1)[0]
body = src.split('<body>', 1)[1]
TICKER_HEADER = body[body.index('<div class="ticker">'):body.index('</header>') + 9]
FOOT_JS = body[body.index('<footer>'):body.rindex('</body>')]

LINKMAP = {'jogalabs-website.html': '/', 'team-labs.html': '/futsal-teams/', 'soccer-classes.html': '/classes-and-training/',
 'inspire-labs.html': '/autism-soccer-lessons-keller-north-fort-worth/', 'about.html': '/about/', 'faq.html': '/faq/',
 'contact.html': '/contact/', 'locations.html': '/locations/', 'results.html': '/results/'}
for c in ['keller','north-fort-worth','haslet','watauga','roanoke','justin','saginaw','northlake','westlake',
          'trophy-club','argyle','colleyville','arlington']:
    LINKMAP[c + '-tx-futsal.html'] = '/' + c + '-tx-futsal/'
def to_wp(s):
    for k, v in LINKMAP.items(): s = s.replace(k, v)
    return s

TICKER_HEADER = to_wp(TICKER_HEADER)
FOOT_JS = to_wp(FOOT_JS)

FIXP = '''<!-- wp:html -->
<style>
  h1.main_title,.entry-title,.post-title,#sidebar,#secondary,.widget-area,aside.sidebar,#right-sidebar{display:none!important;}
  #main-content .container,#content-area,#left-area,#primary,#content,article,.entry-content,.post-content{width:100%!important;max-width:100%!important;padding:0!important;margin:0!important;float:none!important;}
  #main-header,#top-header,#et-top-navigation,header.et-l,.et-l--header,footer.et-l,.et-l--footer,#main-footer,.post-meta,.et_post_meta_wrapper .post-meta,#comment-wrap,#respond,.comments-area,#comment-section,.nav-single,.et_post_nav{display:none!important;}
  article.et_pb_post{background:transparent!important;border:0!important;box-shadow:none!important;}
  html{height:100%;overflow:hidden;}body{height:100%;overflow-y:auto;overflow-x:clip;}
  body.admin-bar .ticker{margin-top:0;}
</style>'''

POST_CSS = '''
  .vhero{background:linear-gradient(160deg,var(--deep),var(--navy));color:#fff;padding:120px 26px 54px;}
  .vhero-in{max-width:900px;margin:0 auto;}
  .vhero .yt-h2{font-family:var(--bfont);font-weight:600;font-size:17px;color:var(--cream);opacity:.92;margin:14px 0 0;line-height:1.5;}
  .vhero .yt-h2 span{color:var(--sky);font-weight:800;text-transform:uppercase;font-size:11.5px;letter-spacing:2px;display:block;margin-bottom:5px;}
  .vmeta{margin-top:18px;font-size:12.5px;letter-spacing:1.6px;text-transform:uppercase;color:#9aa3c0;font-weight:700;}
  .vmeta a{color:var(--sky);text-decoration:none;}
  .vwrap{max-width:900px;margin:0 auto;padding:0 26px;}
  .vid-wrap{position:relative;padding-top:56.25%;margin:-38px auto 40px;max-width:900px;box-shadow:0 24px 60px -20px rgba(7,10,51,.5);z-index:5;}
  .vid-wrap iframe{position:absolute;inset:0;width:100%;height:100%;border:0;}
  .vbody{padding:10px 0 30px;}
  .vbody p{margin:0 0 18px;font-size:16.5px;line-height:1.8;color:var(--ink);}
  .vbody h2{font-family:var(--dfont);font-weight:700;text-transform:uppercase;letter-spacing:1.4px;color:var(--navy);font-size:30px;margin:40px 0 14px;}
  .tkbox{background:var(--cream);border-left:4px solid var(--sky);padding:22px 26px;margin:28px 0;}
  .tkbox b{color:var(--navy);}
  .tkbox ul{margin:10px 0 0 18px;}
  .tkbox li{margin:8px 0;line-height:1.6;}
  .vbody details{border:1px solid var(--line);background:#fff;margin:32px 0;box-shadow:var(--shadow);}
  .vbody summary{cursor:pointer;padding:18px 22px;font-family:var(--dfont);text-transform:uppercase;letter-spacing:1.6px;font-weight:700;color:var(--navy);background:var(--soft);font-size:20px;}
  .vbody .tr-body{padding:10px 26px 22px;}
  .vbody .tr-body h4{color:var(--sky-d);text-transform:uppercase;letter-spacing:1.2px;font-size:14px;margin:20px 0 6px;font-family:var(--bfont);font-weight:800;}
  .cta-line{background:var(--navy);color:#fff;padding:26px 30px;margin:34px 0;}
  .cta-line a{color:var(--sky);font-weight:700;text-decoration:none;}
  .vgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;}
  .vcard{background:#fff;border:1px solid var(--line);box-shadow:var(--shadow);display:flex;flex-direction:column;text-decoration:none;color:var(--ink);transition:transform .25s;}
  .vcard:hover{transform:translateY(-5px);}
  .vcard img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;}
  .vcard-body{padding:20px 22px 24px;display:flex;flex-direction:column;gap:8px;flex:1;}
  .vcard h3{font-family:var(--dfont);font-weight:700;text-transform:uppercase;letter-spacing:1.2px;font-size:22px;color:var(--navy);line-height:1.15;}
  .vcard .ytt{font-size:12.5px;color:var(--muted);font-weight:600;}
  .vcard p{font-size:14px;color:var(--muted);line-height:1.6;flex:1;}
  .vcard .go{color:var(--sky-d);font-weight:800;font-size:13px;letter-spacing:1.2px;text-transform:uppercase;}
  @media (max-width:900px){.vgrid{grid-template-columns:1fr!important;}.vhero{padding:96px 20px 46px;}.vwrap{padding:0 20px;}}
'''

def shell(hero, content):
    return (FIXP + '\n<div class="jl-break">\n<style>' + CSS + POST_CSS + '</style>\n'
            + TICKER_HEADER + '\n' + hero + '\n' + content + '\n' + FOOT_JS + '\n</div>\n<!-- /wp:html -->')

def vhero(kicker, h1a, h1sky, yt_title, meta):
    return ('<section class="vhero"><div class="vhero-in rv">'
            '<span class="lbl on-dark">' + kicker + '</span>'
            '<h1 class="d1">' + h1a + ' <span class="sky">' + h1sky + '</span></h1>'
            '<h2 class="yt-h2"><span>From the video</span>' + yt_title + '</h2>'
            '<div class="vmeta">' + meta + '</div>'
            '</div></section>')

def embed(vid):
    return ('<div class="vwrap"><div class="vid-wrap"><iframe src="https://www.youtube.com/embed/' + vid + '" title="Joga Labs video" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe></div></div>')

def schema(vid, name, desc, up):
    return ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "VideoObject", "name": name, "description": desc,
        "thumbnailUrl": "https://img.youtube.com/vi/%s/hqdefault.jpg" % vid, "uploadDate": up,
        "embedUrl": "https://www.youtube.com/embed/%s" % vid, "contentUrl": "https://www.youtube.com/watch?v=%s" % vid,
        "publisher": {"@type": "Organization", "name": "Joga Labs", "logo": {"@type": "ImageObject", "url": "https://jogalab.com/wp-content/uploads/2025/10/JOGALABS-PlayMore-e1761587146210.png"}},
        "author": {"@type": "Person", "name": "Roberto Avey"}}, ensure_ascii=False) + '</script>')

CTA = ('<div class="cta-line rv"><b>Watch more soccer breakdowns.</b> New videos on tactics, leadership, futsal development '
       'and Brazilian football — <a href="https://www.youtube.com/@jogalabs?sub_confirmation=1" target="_blank" rel="noopener">subscribe to Joga Labs on YouTube</a>. '
       'Want your player training this way? <a href="/futsal-teams/">Join our competitive futsal club in Keller, TX</a>.</div>')

# Pull existing article bodies (takeaways/sections/transcript) from published v1 content is complex;
# instead we re-emit them here (same text as v1, classes match new CSS).
V1 = json.load(io.open('videoposts_v1.json', encoding='utf-8')) if os.path.exists('videoposts_v1.json') else None

posts = json.load(io.open('videoposts_bodies.json', encoding='utf-8'))
out_posts = []
for p in posts['posts']:
    hero = vhero(p['kicker'], p['h1a'], p['h1sky'], p['yt_title'], p['meta'])
    content = (schema(p['vid'], p['yt_title_plain'], p['desc'], p['up']) + hero + embed(p['vid'])
               + '<div class="vwrap vbody">' + p['article'] + CTA + p['transcript'] + '</div>')
    full = FIXP + '\n<div class="jl-break">\n<style>' + CSS + POST_CSS + '</style>\n' + TICKER_HEADER + '\n' + content + '\n' + FOOT_JS + '\n</div>\n<!-- /wp:html -->'
    out_posts.append({'id': p['id'], 'title': p['wp_title'], 'content': full})

# ---------------- HUB PAGE ----------------
cards = ''
for p in posts['posts']:
    cards += ('<a class="vcard rv" href="/' + p['slug'] + '/">'
              '<img src="https://img.youtube.com/vi/' + p['vid'] + '/hqdefault.jpg" alt="' + p['yt_title_plain'].replace('"','') + '" loading="lazy">'
              '<div class="vcard-body"><h3>' + p['h1a'] + ' ' + p['h1sky'] + '</h3>'
              '<div class="ytt">&#9654; ' + p['yt_title'] + '</div>'
              '<p>' + p['card_desc'] + '</p>'
              '<span class="go">Watch + Read &rarr;</span></div></a>')

hub_hero = ('<section class="vhero"><div class="vhero-in rv">'
            '<span class="lbl on-dark">Joga Labs on YouTube</span>'
            '<h1 class="d1">The Video <span class="sky">Blog.</span></h1>'
            '<p class="sub">Every Joga Labs soccer video, broken down and fully transcribed &mdash; tactics, leadership, futsal development and Brazilian football from Coach Roberto Avey.</p>'
            '<div class="vmeta"><a href="https://www.youtube.com/@jogalabs?sub_confirmation=1" target="_blank" rel="noopener">Subscribe on YouTube &rarr;</a></div>'
            '</div></section>')
hub_schema = ('<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org", "@graph": [
      {"@type": "CollectionPage", "@id": "https://jogalab.com/video-blog/", "url": "https://jogalab.com/video-blog/",
       "name": "Joga Labs Video Blog — Soccer Videos & Transcripts", "about": {"@id": "https://jogalab.com/#org"}},
      {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://jogalab.com/"},
        {"@type": "ListItem", "position": 2, "name": "Video Blog", "item": "https://jogalab.com/video-blog/"}]},
      {"@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": p['yt_title_plain'], "url": "https://jogalab.com/" + p['slug'] + '/'}
        for i, p in enumerate(posts['posts'])]}]}, ensure_ascii=False) + '</script>')
hub_content = (hub_schema + hub_hero
               + '<section class="sec"><div class="wrap"><div class="shead center rv">'
               '<span class="lbl">Watch &amp; Read</span><h2 class="d2">Every video, transcribed.</h2>'
               '<p>Each breakdown comes with key takeaways, full analysis, and a complete transcript &mdash; searchable, skimmable, and subtitled by us, not the robots.</p></div>'
               '<div class="vgrid">' + cards + '</div></div></section>')
hub_full = FIXP + '\n<div class="jl-break">\n<style>' + CSS + POST_CSS + '</style>\n' + TICKER_HEADER + '\n' + hub_content + '\n' + FOOT_JS + '\n</div>\n<!-- /wp:html -->'

FOOT_OLD = '<a href="/results/">Past Results</a>'
FOOT_NEW = FOOT_OLD + '\n      <a href="/video-blog/">Video Blog</a>'

payload = {'posts': out_posts,
           'hub': {'slug': 'video-blog', 'title': 'Video Blog', 'content': hub_full,
                   'yoast_title': 'Video Blog | Soccer Videos & Transcripts — Joga Labs Keller, TX',
                   'yoast_desc': "Joga Labs' soccer video blog — tactics, leadership, futsal development and Brazilian football from Coach Roberto Avey. Every video fully transcribed."},
           'foot': [FOOT_OLD, FOOT_NEW]}
raw = gzip.compress(json.dumps(payload, ensure_ascii=False).encode('utf-8'))

def chunk(typ, data):
    return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
       + chunk(b'IDAT', zlib.compress(b'\x00\x00\x00\x00')) + chunk(b'IEND', b''))
io.open('jl-videov2-data.png', 'wb').write(png + b'JLDATA' + raw)
print('gz bytes:', len(raw), '| per-post KB:', [round(len(p['content'])/1024) for p in out_posts], '| hub KB:', round(len(hub_full)/1024))

# local footer sweep (add Video Blog after Past Results in local files)
import glob
LOC_OLD = '<a href="results.html">Past Results</a>'
LOC_NEW = LOC_OLD + '\n      <a href="video-blog.html">Video Blog</a>'
n = 0
for f in glob.glob('*.html'):
    if '-old' in f or f.startswith('email-'): continue
    s = io.open(f, encoding='utf-8').read()
    if LOC_OLD in s and 'video-blog.html">Video Blog' not in s:
        io.open(f, 'w', encoding='utf-8').write(s.replace(LOC_OLD, LOC_NEW)); n += 1
print('local footer updated:', n)
