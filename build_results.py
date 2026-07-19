#!/usr/bin/env python3
# Build results.html from the locations.html shell (current CSS/header/footer).
import io, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src = io.open('locations.html', encoding='utf-8').read()

head_end = src.index('</header>') + len('</header>')
shell_top = src[:head_end]              # head + schema + ticker + header
foot_start = src.index('<footer>')
shell_bottom = src[foot_start:]         # footer + reveal js + close tags

TITLE = "Past Results &amp; Standings | Joga Labs FC &mdash; Chaos Futsal League Keller, TX"
DESC = "Joga Labs FC results and standings from the Chaos Indoor Futsal League in Keller, TX — the current U13 season plus full 2026 Winter and Summer archives."
CANON = "https://jogalab.com/results"

shell_top = re.sub(r'<title>.*?</title>', '<title>%s</title>' % TITLE, shell_top, flags=re.S)
shell_top = re.sub(r'name="description" content="[^"]*"', 'name="description" content="%s"' % DESC, shell_top)
shell_top = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % CANON, shell_top)

SCHEMA = '''{"@context": "https://schema.org", "@graph": [{"@type": "WebPage", "@id": "https://jogalab.com/results/", "url": "https://jogalab.com/results/", "name": "Joga Labs FC — Past Results & Standings", "description": "Game results and league standings for Joga Labs FC in the Chaos Indoor Futsal League, Keller TX — 2026 Winter, Summer 1 and current Summer 2 seasons.", "about": {"@id": "https://jogalab.com/#org"}}, {"@type": "SportsOrganization", "@id": "https://jogalab.com/#org", "name": "Joga Labs", "alternateName": "Joga Labs FC", "url": "https://jogalab.com/", "logo": "https://jogalab.com/wp-content/uploads/2025/10/JOGALABS-PlayMore-e1761587146210.png", "telephone": "+1-817-546-5994", "email": "info@jogalab.com", "sport": "Futsal", "address": {"@type": "PostalAddress", "streetAddress": "4200 Keller Haslet Rd", "addressLocality": "Keller", "addressRegion": "TX", "postalCode": "76244", "addressCountry": "US"}}, {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://jogalab.com/"}, {"@type": "ListItem", "position": 2, "name": "Past Results", "item": "https://jogalab.com/results/"}]}, {"@type": "ItemList", "name": "Joga Labs FC seasons — Chaos Indoor Futsal League", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "2026 Futsal Summer 2 (in progress)", "url": "https://scheduler.leaguelobster.com/2727211/"}, {"@type": "ListItem", "position": 2, "name": "2026 Futsal Summer 1", "url": "https://scheduler.leaguelobster.com/2675393/"}, {"@type": "ListItem", "position": 3, "name": "2026 Futsal Winter 2", "url": "https://scheduler.leaguelobster.com/2507847/"}]}]}'''
shell_top = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">'+SCHEMA+'</script>', shell_top, count=1, flags=re.S)

CSS = '''<style>
  .res-season{border:1px solid var(--line);background:#fff;box-shadow:var(--shadow);margin-bottom:34px;}
  .res-head{display:flex;justify-content:space-between;align-items:center;gap:14px;background:var(--navy);color:#fff;padding:18px 28px;flex-wrap:wrap;}
  .res-head h3{font-family:var(--dfont);font-weight:700;text-transform:uppercase;letter-spacing:1.6px;font-size:22px;color:#fff;margin:0;}
  .res-head .res-dates{font-size:12.5px;letter-spacing:1.6px;text-transform:uppercase;color:var(--sky);font-weight:700;}
  .res-live{display:inline-block;background:var(--sky);color:var(--navy);font-size:10.5px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;padding:4px 10px;margin-left:10px;vertical-align:middle;}
  .res-body{display:grid;grid-template-columns:1.1fr 1fr;gap:0;}
  .res-cell{padding:22px 26px;min-width:0;}
  .res-cell + .res-cell{border-left:1px solid var(--line);}
  .res-cell h4{font-family:var(--dfont);font-weight:700;text-transform:uppercase;letter-spacing:1.4px;font-size:16px;color:var(--navy);margin:0 0 12px;}
  .rtable{width:100%;border-collapse:collapse;}
  .rtable th{font-size:10.5px;letter-spacing:1.2px;text-transform:uppercase;color:#66707f;text-align:left;padding:8px 6px;border-bottom:1px solid var(--line);}
  .rtable td{font-size:13.5px;padding:8px 6px;border-bottom:1px solid var(--line);color:var(--ink);}
  .rtable tr:last-child td{border-bottom:0;}
  .rtable th.num,.rtable td.num{text-align:center;}
  .rtable td:nth-child(2),.rtable th:nth-child(2){white-space:nowrap;width:99%;}
  .rtable td:first-child{color:#66707f;}
  .rtable td:last-child{font-weight:700;text-align:center;}
  .rtable tr.jl td{background:#eaf6ff;font-weight:700;color:var(--navy);}
  .gline{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--line);font-size:13.5px;color:var(--ink);}
  .gline:last-child{border-bottom:0;}
  .gline .gd{color:#66707f;font-size:12px;min-width:52px;}
  .gline .gs{font-family:var(--dfont);font-weight:700;font-size:16px;color:var(--navy);min-width:44px;text-align:center;}
  .gline .go2{flex:1;min-width:0;}
  .badge{display:inline-block;min-width:20px;text-align:center;font-size:11px;font-weight:800;padding:3px 0;color:#fff;}
  .badge.w{background:#1e9e57;}
  .badge.l{background:#c0392b;}
  .badge.d{background:#8a93a3;}
  .derby{display:inline-block;background:var(--sky);color:var(--navy);font-size:10px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;padding:2px 7px;margin-left:6px;}
  .res-note{font-size:12px;color:#8a93a3;padding:12px 26px 16px;border-top:1px solid var(--line);}
  .res-note a{color:var(--sky-d);font-weight:700;text-decoration:none;}
  .squad-split{display:grid;grid-template-columns:1fr 1fr;gap:22px;}
  .climb{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:8px;}
  .climb .cstat{background:var(--cream);padding:24px 20px;text-align:center;}
  .climb .cstat b{display:block;font-family:var(--dfont);font-weight:700;font-size:34px;color:var(--navy);line-height:1;}
  .climb .cstat span{font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#66707f;font-weight:700;}
  @media (max-width:860px){
    .res-body{grid-template-columns:1fr!important;}
    .res-cell + .res-cell{border-left:0;border-top:1px solid var(--line);}
    .squad-split{grid-template-columns:1fr!important;}
    .climb{grid-template-columns:1fr!important;}
    .res-head{padding:14px 16px;}
    .res-cell{padding:18px 16px;}
  }
</style>'''

def srow(pos, team, gp, w, l, d, pts, jl=False):
    cls = ' class="jl"' if jl else ''
    return f'<tr{cls}><td>{pos}</td><td>{team}</td><td class="num">{gp}</td><td class="num">{w}</td><td class="num">{l}</td><td class="num">{d}</td><td>{pts}</td></tr>'

def table(rows):
    return ('<table class="rtable"><tr><th>#</th><th>Team</th><th class="num">GP</th><th class="num">W</th>'
            '<th class="num">L</th><th class="num">D</th><th>Pts</th></tr>' + ''.join(rows) + '</table>')

def gline(date, res, score, opp, derby=False):
    d = '<span class="derby">Club Derby</span>' if derby else ''
    return (f'<div class="gline"><span class="gd">{date}</span><span class="badge {res.lower()}">{res}</span>'
            f'<span class="gs">{score}</span><span class="go2">{opp}{d}</span></div>')

# ---------------- Summer 2 (current) ----------------
s2_stand = table([
 srow(1,'Sting Royal',3,3,0,0,9), srow(2,'Sting White',3,2,1,0,6),
 srow(3,'Joga Labs Red',3,2,1,0,6,True), srow(4,'Joga Labs Black',3,1,2,0,3,True),
 srow(5,'Hurst United White',3,1,2,0,3), srow(6,'Hurst United Red',3,0,3,0,0)])
s2_red = (gline('Jun 27','W','14&ndash;4','Hurst United Red') + gline('Jul 12','L','3&ndash;17','Sting Royal') +
          gline('Jul 18','W','6&ndash;4','Hurst United White'))
s2_black = (gline('Jun 27','L','4&ndash;16','Sting Royal') + gline('Jul 12','L','4&ndash;8','Sting White') +
            gline('Jul 18','W','7&ndash;2','Hurst United Red'))

# ---------------- Summer 1 ----------------
s1_stand = table([
 srow(1,'Sting Royal',6,6,0,0,18), srow(2,'Atletico Dallas Blue',6,5,1,0,15),
 srow(3,'Joga Labs Red',6,4,2,0,12,True), srow(4,'Atletico Dallas Black',6,3,2,1,10),
 srow(5,'Surf',6,3,2,1,10), srow(6,'Sting',6,2,4,0,6),
 srow(7,'Joga Labs Black',6,1,5,0,3,True), srow(8,'Hurst United White',6,1,5,0,3),
 srow(9,'Hurst United Red',6,1,5,0,3)])
s1_red = (gline('May 8','L','9&ndash;12','Sting Royal') + gline('May 16','W','10&ndash;6','Sting') +
          gline('Jun 5','W','5&ndash;3','Hurst United Red') + gline('Jun 6','W','6&ndash;1','Hurst United White') +
          gline('Jun 7','L','6&ndash;7','Joga Labs Black',True) + gline('Jun 13','W','5&ndash;4','Surf'))
s1_black = (gline('May 16','L','7&ndash;11','Sting Royal') + gline('May 23','L','6&ndash;7','Hurst United White') +
            gline('Jun 6','L','2&ndash;6','Surf') + gline('Jun 7','W','7&ndash;6','Joga Labs Red',True) +
            gline('Jun 13','L','9&ndash;10','Sting') + gline('Jun 14','L','3&ndash;9','Atletico Dallas Black'))

# ---------------- Winter 2 ----------------
w14_stand = table([
 srow(1,'Fever Red',6,6,0,0,18), srow(2,'Fever Black',6,4,2,0,12),
 srow(3,'Sting Royal',6,2,4,0,6), srow(4,'Sting White',6,2,4,0,6),
 srow(5,'Joga Labs (14B)',6,1,5,0,3,True)])
w13_stand = table([
 srow(1,'Sting Royal (Williams)',6,5,0,1,16), srow(2,'Sting White',6,4,1,1,13),
 srow(3,'Sting Royal (Robles)',6,3,3,0,9), srow(4,'Stronger FC',6,2,4,0,6),
 srow(5,'Joga Labs (13B)',6,0,6,0,0,True)])
w14_games = (gline('Jan 3','L','9&ndash;10','Sting White') + gline('Jan 11','L','4&ndash;12','Fever Black') +
             gline('Jan 18','L','2&ndash;8','Fever Red') + gline('Jan 30','L','3&ndash;12','Sting Royal') +
             gline('Jan 31','L','5&ndash;14','Fever Red') + gline('Feb 8','W','5&ndash;3','Sting White'))
w13_games = (gline('Jan 3','L','2&ndash;18','Sting Royal (W)') + gline('Jan 10','L','5&ndash;9','Sting White') +
             gline('Jan 18','L','8&ndash;20','Sting Royal (R)') + gline('Jan 31','L','7&ndash;11','Stronger FC') +
             gline('Feb 7','L','4&ndash;8','Sting White') + gline('Feb 8','L','1&ndash;13','Sting Royal (R)'))

LL = 'https://scheduler.leaguelobster.com/'

body = f'''
<section class="phero">
  <div class="phero-bg" style="background-image:url('assets/img_1434.jpg');"></div><div class="phero-fade"></div>
  <div class="phero-in">
    <div class="crumbs"><a href="jogalabs-website.html">Home</a> / <b>Past Results</b></div><span class="lbl on-dark">Club Record</span>
    <h1 class="d1">Past <span class="sky">Results.</span></h1>
    <p class="sub">Every Joga Labs FC scoreline and standing from the Chaos Indoor Futsal League in Keller, TX &mdash; season by season, from our first whistle in January to today.</p>
    <div class="hero-actions"><a href="jogalabs-website.html#schedule" class="btn btn--sky">Upcoming Games</a></div>
  </div>
</section>
{CSS}
<section class="sec">
  <div class="wrap">
    <div class="shead center rv">
      <span class="lbl">The Climb</span>
      <h2 class="d2">Built in six months.</h2>
      <p>Joga Labs entered its first Chaos league in January 2026. Two seasons later, Joga Labs Red is fighting for a playoff spot and both squads won their last outing. That&rsquo;s what game-based development looks like.</p>
    </div>
    <div class="climb rv">
      <div class="cstat"><b>1</b><span>Win &mdash; Winter (first season)</span></div>
      <div class="cstat"><b>5</b><span>Wins &mdash; Summer 1 &middot; Red finished 3rd</span></div>
      <div class="cstat"><b>3&ndash;0</b><span>Both squads won Jul 18</span></div>
    </div>
  </div>
</section>

<section class="sec sec--cream">
  <div class="wrap">
    <div class="shead center rv">
      <span class="lbl">Season by Season</span>
      <h2 class="d2">Results &amp; standings.</h2>
      <p>League tables and every Joga Labs game. Joga rows highlighted. All games played at Chaos Sports Performance, 5701 Egg Farm Rd, Fort Worth (Keller), TX.</p>
    </div>

    <div class="res-season rv">
      <div class="res-head"><h3>2026 Summer 2 <span class="res-live">In Progress</span></h3><span class="res-dates">Jun 27 &ndash; Aug 9 &middot; U13 13/14 Division</span></div>
      <div class="res-body">
        <div class="res-cell"><h4>Standings &mdash; Week 3 of 6</h4>{s2_stand}</div>
        <div class="res-cell">
          <div class="squad-split">
            <div><h4>Joga Labs Red</h4>{s2_red}</div>
            <div><h4>Joga Labs Black</h4>{s2_black}</div>
          </div>
        </div>
      </div>
      <div class="res-note">Updated Jul 19, 2026 &middot; <a href="{LL}2727211/" target="_blank" rel="noopener">Live standings on LeagueLobster &rarr;</a></div>
    </div>

    <div class="res-season rv">
      <div class="res-head"><h3>2026 Summer 1</h3><span class="res-dates">May 8 &ndash; Jun 14 &middot; U13 13/14 Division</span></div>
      <div class="res-body">
        <div class="res-cell"><h4>Final Standings &mdash; Red 3rd of 9</h4>{s1_stand}</div>
        <div class="res-cell">
          <div class="squad-split">
            <div><h4>Joga Labs Red &mdash; 4W 2L</h4>{s1_red}</div>
            <div><h4>Joga Labs Black &mdash; 1W 5L</h4>{s1_black}</div>
          </div>
          <p style="font-size:12.5px;color:#66707f;margin-top:12px;">June 7 was the club&rsquo;s first-ever derby &mdash; Black edged Red 7&ndash;6.</p>
        </div>
      </div>
      <div class="res-note">Season archive &middot; <a href="{LL}2675393/" target="_blank" rel="noopener">Full season on LeagueLobster &rarr;</a></div>
    </div>

    <div class="res-season rv">
      <div class="res-head"><h3>2026 Winter 2</h3><span class="res-dates">Jan 3 &ndash; Feb 8 &middot; Two Divisions</span></div>
      <div class="res-body">
        <div class="res-cell">
          <h4>U13 13/14 Division &mdash; Final</h4>{w14_stand}
          <h4 style="margin-top:20px;">13&rsquo;s Division &mdash; Final</h4>{w13_stand}
        </div>
        <div class="res-cell">
          <div class="squad-split">
            <div><h4>Joga Labs 14B &mdash; 1W 5L</h4>{w14_games}</div>
            <div><h4>Joga Labs 13B &mdash; 0W 6L</h4>{w13_games}</div>
          </div>
          <p style="font-size:12.5px;color:#66707f;margin-top:12px;">Our first league season. Every team on this page had years of a head start &mdash; we closed it out with a 5&ndash;3 win on the final day and haven&rsquo;t looked back. (The club sat out Spring 1 to rebuild and train.)</p>
        </div>
      </div>
      <div class="res-note">Season archive &middot; <a href="{LL}2507847/" target="_blank" rel="noopener">Full season on LeagueLobster &rarr;</a></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="shead center rv">
      <span class="lbl">Be Part of the Next Chapter</span>
      <h2 class="d2">The table doesn&rsquo;t lie. The work shows.</h2>
      <p>Joga Labs is a competitive youth futsal club &mdash; players earn these results through weekly practice at 4200 Keller Haslet Rd and league nights at Chaos. Ready to compete? <a href="team-labs.html" style="color:var(--sky-d);font-weight:700;">Join a squad &rarr;</a></p>
    </div>
  </div>
</section>
'''

doc = shell_top + body + shell_bottom
io.open('results.html', 'w', encoding='utf-8').write(doc)
print('wrote results.html', len(doc))

# ---- Footer link sweep: add Past Results after Game Schedule on all pages ----
import glob
FOOT_OLD = '<a href="jogalabs-website.html#schedule">Game Schedule</a>'
FOOT_NEW = FOOT_OLD + '\n      <a href="results.html">Past Results</a>'
count = 0
for f in glob.glob('*.html'):
    if '-old' in f or f in ('signup.html',) or f.startswith('email-'): continue
    s = io.open(f, encoding='utf-8').read()
    if 'results.html">Past Results' in s: continue
    if FOOT_OLD in s:
        io.open(f, 'w', encoding='utf-8').write(s.replace(FOOT_OLD, FOOT_NEW)); count += 1
print('footer link added to', count, 'files')

# ---- Home schedule area link ----
SCHED_OLD = '<div class="stand-note">Updated Jul 19 &middot; <a href="https://scheduler.leaguelobster.com/2727211/" target="_blank" rel="noopener">Full standings &rarr;</a></div>'
SCHED_NEW = '<div class="stand-note">Updated Jul 19 &middot; <a href="https://scheduler.leaguelobster.com/2727211/" target="_blank" rel="noopener">Full standings &rarr;</a> &middot; <a href="results.html">Past Results &rarr;</a></div>'
for f in ('jogalabs-website.html', 'index.html'):
    s = io.open(f, encoding='utf-8').read()
    assert SCHED_OLD in s, f
    io.open(f, 'w', encoding='utf-8').write(s.replace(SCHED_OLD, SCHED_NEW))
print('home schedule link added')
