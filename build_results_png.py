#!/usr/bin/env python3
# Package results page WP payload + link sweeps into PNG (JLDATA smuggle).
import io, os, json, gzip, re, struct, zlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))

src = io.open('results.html', encoding='utf-8').read()

css = src.split('<style>', 1)[1].split('</style>', 1)[0]
body = src.split('<body>', 1)[1].rsplit('</body>', 1)[0]

LINKMAP = {'jogalabs-website.html': '/', 'team-labs.html': '/futsal-teams/', 'soccer-classes.html': '/classes-and-training/',
 'inspire-labs.html': '/autism-soccer-lessons-keller-north-fort-worth/', 'about.html': '/about/', 'faq.html': '/faq/',
 'contact.html': '/contact/', 'locations.html': '/locations/', 'results.html': '/results/'}
for c in ['keller','north-fort-worth','haslet','watauga','roanoke','justin','saginaw','northlake','westlake',
          'trophy-club','argyle','colleyville','arlington']:
    LINKMAP[c + '-tx-futsal.html'] = '/' + c + '-tx-futsal/'

def to_wp(s):
    for k, v in LINKMAP.items(): s = s.replace(k, v)
    s = re.sub(r"assets/(img_\d+(?:_prev)?\.(?:jpg|png))", r"https://jogalab.com/wp-content/uploads/2026/07/\1", s)
    return s

FIX = '''<!-- wp:html -->
<style>
  h1.main_title,.entry-title,.post-title,#sidebar,#secondary,.widget-area,aside.sidebar,#right-sidebar{display:none!important;}
  #main-content .container,#content-area,#left-area,#primary,#content,article,.entry-content,.post-content{width:100%!important;max-width:100%!important;padding:0!important;margin:0!important;float:none!important;}
  html,body{overflow-x:clip;}
  '''
# NOTE: exact FIX text is taken live in-browser (window fetch of an existing page) to avoid drift.

content = '<div class="jl-break">\n<style>' + css + '</style>\n' + to_wp(body) + '\n</div>\n<!-- /wp:html -->'

FOOT_OLD = to_wp('<a href="jogalabs-website.html#schedule">Game Schedule</a>')
FOOT_NEW = FOOT_OLD + '\n      <a href="/results/">Past Results</a>'
SN_OLD = '<div class="stand-note">Updated Jul 19 &middot; <a href="https://scheduler.leaguelobster.com/2727211/" target="_blank" rel="noopener">Full standings &rarr;</a></div>'
SN_NEW = '<div class="stand-note">Updated Jul 19 &middot; <a href="https://scheduler.leaguelobster.com/2727211/" target="_blank" rel="noopener">Full standings &rarr;</a> &middot; <a href="/results/">Past Results &rarr;</a></div>'

payload = {
 'newpage': {'slug': 'results', 'title': 'Past Results', 'content': content},
 'meta': "Joga Labs FC results and standings from the Chaos Indoor Futsal League in Keller, TX — the current U13 season plus full 2026 Winter and Summer archives.",
 'foot': [FOOT_OLD, FOOT_NEW],
 'standnote': [SN_OLD, SN_NEW],
}
raw = gzip.compress(json.dumps(payload, ensure_ascii=False).encode('utf-8'))

def chunk(typ, data):
    return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
png = (b'\\x89PNG\\r\\n\\x1a\\n'.decode('unicode_escape').encode('latin1')
       + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
       + chunk(b'IDAT', zlib.compress(b'\\x00\\x00\\x00\\x00'.decode('unicode_escape').encode('latin1')))
       + chunk(b'IEND', b''))
io.open('jl-results-data.png', 'wb').write(png + b'JLDATA' + raw)
print('png bytes:', len(png) + 6 + len(raw), 'payload gz:', len(raw))
