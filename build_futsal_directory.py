#!/usr/bin/env python3
# Build futsal-directory.html (searchable, SEO) + WP payload PNG + footer link updates.
import io, os, re, json, gzip, struct, zlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))

E = json.load(io.open('usa_futsal_directory.json', encoding='utf-8'))
E.sort(key=lambda e: (e['Type'], e['State'], e['Name']))

src = io.open('locations.html', encoding='utf-8').read()
CSS = src.split('<style>', 1)[1].split('</style>', 1)[0]
body = src.split('<body>', 1)[1]
TICKER_HEADER = body[body.index('<div class="ticker">'):body.index('</header>') + 9]
FOOT_JS = body[body.index('<footer>'):body.rindex('</body>')]

LINKMAP = {'jogalabs-website.html': '/', 'team-labs.html': '/futsal-teams/', 'soccer-classes.html': '/classes-and-training/',
 'inspire-labs.html': '/autism-soccer-lessons-keller-north-fort-worth/', 'about.html': '/about/', 'faq.html': '/faq/',
 'contact.html': '/contact/', 'locations.html': '/locations/', 'results.html': '/results/',
 'video-blog.html': '/video-blog/', 'futsal-directory.html': '/futsal-directory/'}
for c in ['keller','north-fort-worth','haslet','watauga','roanoke','justin','saginaw','northlake','westlake',
          'trophy-club','argyle','colleyville','arlington']:
    LINKMAP[c + '-tx-futsal.html'] = '/' + c + '-tx-futsal/'
def to_wp(s):
    for k, v in LINKMAP.items(): s = s.replace(k, v)
    return s

FIXP = '''<!-- wp:html -->
<style>
  h1.main_title,.entry-title,.post-title,#sidebar,#secondary,.widget-area,aside.sidebar,#right-sidebar{display:none!important;}
  #main-content .container,#content-area,#left-area,#primary,#content,article,.entry-content,.post-content{width:100%!important;max-width:100%!important;padding:0!important;margin:0!important;float:none!important;}
  html{height:100%;overflow:hidden;}body{height:100%;overflow-y:auto;overflow-x:clip;}
</style>'''

DCSS = '''
  .dirhero{background:linear-gradient(160deg,var(--deep),var(--navy));color:#fff;padding:120px 26px 54px;}
  .dirhero-in{max-width:1100px;margin:0 auto;}
  .dirhero .d1{color:#fff!important;}
  .dirhero .sub{color:#e2e7f7!important;}
  .dir-tools{max-width:1100px;margin:-30px auto 26px;background:#fff;border:1px solid var(--line);box-shadow:var(--shadow);padding:20px;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:12px;position:relative;z-index:5;}
  .dir-tools input,.dir-tools select{font-family:var(--bfont);font-size:15px;padding:12px 14px;border:1px solid var(--line);background:var(--soft);color:var(--ink);width:100%;}
  .dir-tools input:focus,.dir-tools select:focus{outline:2px solid var(--sky);}
  .dir-count{max-width:1100px;margin:0 auto 14px;font-size:12.5px;letter-spacing:1.4px;text-transform:uppercase;color:var(--muted);font-weight:700;padding:0 2px;}
  .dir-list{max-width:1100px;margin:0 auto 50px;display:flex;flex-direction:column;gap:10px;}
  .dir-row{background:#fff;border:1px solid var(--line);padding:16px 20px;display:grid;grid-template-columns:1.5fr 1fr auto;gap:8px 18px;align-items:center;}
  .dir-row:hover{box-shadow:var(--shadow);}
  .dir-row b{font-size:16px;color:var(--navy);}
  .dr-badge{display:inline-block;font-size:10px;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:3px 8px;margin-left:8px;color:#fff;vertical-align:2px;}
  .dr-badge.t-club{background:#1795e0;}
  .dr-badge.t-league{background:#1e9e57;}
  .dr-badge.t-tournament{background:#e07a17;}
  .dr-badge.t-organization{background:#7b3fd4;}
  .dr-loc{font-size:13.5px;color:var(--muted);}
  .dr-notes{grid-column:1/3;font-size:13px;color:#77809a;line-height:1.5;}
  .dr-link{font-size:12px;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--sky-d);text-decoration:none;white-space:nowrap;}
  .dir-row.hide{display:none;}
  .dir-cta{max-width:1100px;margin:0 auto 60px;background:var(--cream);border-left:4px solid var(--sky);padding:22px 26px;font-size:15px;line-height:1.7;}
  .dir-cta a{color:var(--sky-d);font-weight:700;text-decoration:none;}
  @media (max-width:860px){
    .dir-tools{grid-template-columns:1fr!important;margin-top:-20px;}
    .dir-row{grid-template-columns:1fr!important;}
    .dr-notes{grid-column:1;}
    .dirhero{padding:96px 20px 46px;}
    .dir-list,.dir-count,.dir-cta{padding-left:20px;padding-right:20px;}
  }
'''

states = sorted(set(e['State'] for e in E if e['State'] != 'National'))
regions = ['West','Southwest','Midwest','South','Southeast','Mid-Atlantic','Northeast','National']

rows = []
for e in E:
    tcls = 't-' + e['Type'].split(' ')[0].replace('/', '').lower()
    search = (e['Name'] + ' ' + e['City'] + ' ' + e['State'] + ' ' + e['Region'] + ' ' + e['Organization'] + ' ' + e['Type']).lower().replace('"', '')
    loc = (e['City'] + ', ' + e['State']) if e['State'] != 'National' else 'Nationwide'
    rows.append(
        '<div class="dir-row" data-type="%s" data-state="%s" data-region="%s" data-q="%s">'
        '<div><b>%s</b><span class="dr-badge %s">%s</span></div>'
        '<div class="dr-loc">%s &middot; %s</div>'
        '<a class="dr-link" href="%s" target="_blank" rel="noopener nofollow">Website &rarr;</a>'
        '<div class="dr-notes">%s</div></div>'
        % (e['Type'], e['State'], e['Region'], search, e['Name'], tcls,
           e['Type'], loc, e['Organization'], e['Website'], e['Notes']))

schema = {"@context": "https://schema.org", "@graph": [
 {"@type": "WebPage", "@id": "https://jogalab.com/futsal-directory/", "url": "https://jogalab.com/futsal-directory/",
  "name": "USA Futsal Directory — Teams, Leagues & Tournaments",
  "description": "Searchable national directory of futsal clubs, leagues and tournaments in the United States, maintained by Joga Labs.",
  "about": {"@id": "https://jogalab.com/#org"}},
 {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://jogalab.com/"},
   {"@type": "ListItem", "position": 2, "name": "USA Futsal Directory", "item": "https://jogalab.com/futsal-directory/"}]},
 {"@type": "ItemList", "name": "USA Futsal Directory", "numberOfItems": len(E),
  "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": e['Name'], "url": e['Website']} for i, e in enumerate(E)]},
 {"@type": "FAQPage", "mainEntity": [
   {"@type": "Question", "name": "How do I find a futsal league near me in the USA?",
    "acceptedAnswer": {"@type": "Answer", "text": "Search this directory by state or region. US Youth Futsal alone oversees 100+ leagues in 30 states; US Futsal (USFF) and independent leagues like the Chaos Indoor Futsal League in Keller, TX add many more."}},
   {"@type": "Question", "name": "What are the biggest futsal tournaments in the United States?",
    "acceptedAnswer": {"@type": "Answer", "text": "The USYF National Championships (Richmond, VA), the U.S. Futsal National Championships, and United Futsal's World Futsal Championships in Orlando are the flagship events, fed by 13+ regional championships across the country."}},
   {"@type": "Question", "name": "Is there professional futsal in the USA?",
    "acceptedAnswer": {"@type": "Answer", "text": "Yes — the National Futsal Premier League (NFPL), founded in 2018, is the top semi-professional league with men's and women's divisions across California, Southwest and Midwest conferences."}}]}]}

body_html = ('<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>'
 + TICKER_HEADER + '''
<section class="dirhero"><div class="dirhero-in rv">
  <div class="crumbs"><a href="jogalabs-website.html">Home</a> / <b>USA Futsal Directory</b></div>
  <span class="lbl on-dark">''' + str(len(E)) + ''' Entries &middot; ''' + str(len(states)) + ''' States</span>
  <h1 class="d1">The USA Futsal <span class="sky">Directory.</span></h1>
  <p class="sub">Every futsal club, league and tournament we can find in America &mdash; searchable by name, city, state and region. From US Youth Futsal's 100+ leagues to the NFPL and the national championships. Maintained by Joga Labs, a competitive youth futsal club in Keller, TX.</p>
</div></section>
<style>''' + DCSS + '''</style>
<div class="dir-tools rv">
  <input id="dirq" type="search" placeholder="Search name, city, state&hellip;" aria-label="Search directory">
  <select id="dirtype" aria-label="Filter by type"><option value="">All Types</option><option>Club / Team</option><option>League</option><option>Tournament</option><option>Organization</option></select>
  <select id="dirstate" aria-label="Filter by state"><option value="">All States</option>'''
 + ''.join('<option>%s</option>' % s for s in states) + '''</select>
  <select id="dirregion" aria-label="Filter by region"><option value="">All Regions</option>'''
 + ''.join('<option>%s</option>' % r for r in regions) + '''</select>
</div>
<div class="dir-count"><span id="dircount">''' + str(len(E)) + '''</span> results</div>
<div class="dir-list" id="dirlist">''' + ''.join(rows) + '''</div>
<div class="dir-cta rv"><b>Run a futsal club, league or tournament that's missing?</b> Email <a href="mailto:info@jogalab.com?subject=USA%20Futsal%20Directory%20Listing">info@jogalab.com</a> and we'll add you for free. In North Texas? <a href="team-labs.html">Come play with Joga Labs in Keller</a> &mdash; competitive U9&ndash;U15 futsal in the Chaos Indoor League.</div>
''' + FOOT_JS + '''
<script>
(function(){
  var q=document.getElementById('dirq'),t=document.getElementById('dirtype'),s=document.getElementById('dirstate'),r=document.getElementById('dirregion');
  var rows=[].slice.call(document.querySelectorAll('.dir-row')),c=document.getElementById('dircount');
  function run(){
    var qq=q.value.toLowerCase().trim(),tt=t.value,ss=s.value,rr=r.value,n=0;
    rows.forEach(function(el){
      var ok=(!qq||el.getAttribute('data-q').indexOf(qq)>-1)&&(!tt||el.getAttribute('data-type')===tt)&&(!ss||el.getAttribute('data-state')===ss)&&(!rr||el.getAttribute('data-region')===rr);
      el.classList.toggle('hide',!ok); if(ok)n++;
    });
    c.textContent=n;
  }
  [q,t,s,r].forEach(function(el){el.addEventListener('input',run);el.addEventListener('change',run);});
})();
</script>''')

TITLE = 'USA Futsal Directory &mdash; Teams, Leagues &amp; Tournaments | Joga Labs'
DESC = "Searchable directory of futsal in the United States — 100+ clubs, leagues and tournaments from USYF, US Futsal, United Futsal and the NFPL, state by state."

# local file
head = src[:src.index('<body>') + 6]
head = re.sub(r'<title>.*?</title>', '<title>' + TITLE + '</title>', head, flags=re.S)
head = re.sub(r'name="description" content="[^"]*"', 'name="description" content="' + DESC + '"', head)
head = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="https://jogalab.com/futsal-directory">', head)
io.open('futsal-directory.html', 'w', encoding='utf-8').write(head + '\n' + body_html + '\n</body>\n</html>')
print('wrote futsal-directory.html', len(body_html) // 1024, 'KB body')

# WP payload
wp_content = FIXP + '\n<div class="jl-break">\n<style>' + CSS + '</style>\n' + to_wp(body_html) + '\n</div>\n<!-- /wp:html -->'
FOOT_OLD_WP = '<a href="/video-blog/">Video Blog</a>'
FOOT_NEW_WP = '<a href="/video-blog/">Futsal Blog</a>\n      <a href="/futsal-directory/">Futsal Directory</a>'
payload = {'page': {'slug': 'futsal-directory', 'title': 'USA Futsal Directory', 'content': wp_content},
           'yoast_title': 'USA Futsal Directory — Teams, Leagues & Tournaments | Joga Labs',
           'yoast_desc': DESC, 'foot': [FOOT_OLD_WP, FOOT_NEW_WP]}
raw = gzip.compress(json.dumps(payload, ensure_ascii=False).encode('utf-8'))
def chunk(typ, data):
    return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
       + chunk(b'IDAT', zlib.compress(b'\x00\x00\x00\x00')) + chunk(b'IEND', b''))
io.open('jl-dir-data.png', 'wb').write(png + b'JLDATA' + raw)
print('payload gz:', len(raw))

# local footer sweep: rename Video Blog -> Futsal Blog + add directory link
import glob
LOC_OLD = '<a href="video-blog.html">Video Blog</a>'
LOC_NEW = '<a href="video-blog.html">Futsal Blog</a>\n      <a href="futsal-directory.html">Futsal Directory</a>'
n = 0
for f in glob.glob('*.html'):
    if '-old' in f or f.startswith('email-'): continue
    s = io.open(f, encoding='utf-8').read()
    if LOC_OLD in s:
        io.open(f, 'w', encoding='utf-8').write(s.replace(LOC_OLD, LOC_NEW)); n += 1
print('local footers updated:', n)
