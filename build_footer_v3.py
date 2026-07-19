#!/usr/bin/env python3
# Footer v3: Programs (trimmed) / Club / Futsal Resources + newsletter signup. Local sweep + WP payload strings.
import io, os, json, glob, gzip, struct, zlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))

OLD = '''      <h5>Programs</h5>
      <a href="team-labs.html">Futsal Teams</a>
      <a href="soccer-classes.html">Soccer Classes</a>
      <a href="inspire-labs.html">Autism Soccer</a>
      <a href="jogalabs-website.html#schedule">Game Schedule</a>
      <a href="results.html">Past Results</a>
      <a href="video-blog.html">Futsal Blog</a>
      <a href="futsal-directory.html">Futsal Directory</a>
      <a href="jogalabs-website.html#gallery">Gallery</a>
    </div>
    <div class="foot-col">
      <h5>Club</h5>
      <a href="about.html">About Us</a>
      <a href="faq.html">FAQs</a>
      <a href="contact.html">Contact Us</a>
      <a href="locations.html">Locations</a>
      <a href="https://jogalab.com/terms/">Terms &amp; Privacy</a>
    </div>
    <div class="foot-col">
      <h5>Areas We Serve</h5>
      <div class="foot-cities">
      <a href="keller-tx-futsal.html">Keller, TX</a>
      <a href="north-fort-worth-tx-futsal.html">North Fort Worth, TX</a>
      <a href="haslet-tx-futsal.html">Haslet, TX</a>
      <a href="watauga-tx-futsal.html">Watauga, TX</a>
      <a href="roanoke-tx-futsal.html">Roanoke, TX</a>
      <a href="justin-tx-futsal.html">Justin, TX</a>
      <a href="saginaw-tx-futsal.html">Saginaw, TX</a>
      <a href="northlake-tx-futsal.html">Northlake, TX</a>
      <a href="westlake-tx-futsal.html">Westlake, TX</a>
      <a href="trophy-club-tx-futsal.html">Trophy Club, TX</a>
      <a href="argyle-tx-futsal.html">Argyle, TX</a>
      <a href="colleyville-tx-futsal.html">Colleyville, TX</a>
      <a href="arlington-tx-futsal.html">Arlington, TX</a>
      </div>
    </div>'''

NEW = '''      <h5>Programs</h5>
      <a href="team-labs.html">Futsal Teams</a>
      <a href="soccer-classes.html">Soccer Classes</a>
      <a href="inspire-labs.html">Autism Soccer</a>
      <a href="jogalabs-website.html#schedule">Game Schedule</a>
      <a href="results.html">Past Results</a>
      <a href="jogalabs-website.html#gallery">Gallery</a>
    </div>
    <div class="foot-col">
      <h5>Club</h5>
      <a href="about.html">About Us</a>
      <a href="faq.html">FAQs</a>
      <a href="contact.html">Contact Us</a>
      <a href="locations.html">Locations</a>
      <a href="https://jogalab.com/terms/">Terms &amp; Privacy</a>
    </div>
    <div class="foot-col">
      <h5>Futsal Resources</h5>
      <a href="video-blog.html">Futsal Blog</a>
      <a href="futsal-directory.html">Futsal Directory</a>
      <style>
      .nlbox{margin-top:16px;}
      .nl-head{font-size:13.5px;font-weight:700;color:#fff;margin:0 0 10px;line-height:1.5;}
      .nl-form{display:flex;flex-direction:column;gap:8px;}
      .nl-form input,.nl-form select{font-family:var(--bfont);font-size:13.5px;padding:10px 12px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.07);color:#fff;width:100%;}
      .nl-form input::placeholder{color:#9aa3c0;}
      .nl-form select{color:#9aa3c0;}
      .nl-form select.filled{color:#fff;}
      .nl-form select option{color:var(--ink);}
      .nl-form input:focus,.nl-form select:focus{outline:2px solid var(--sky);}
      .nl-form button{font-family:var(--dfont);font-weight:700;letter-spacing:1.6px;text-transform:uppercase;font-size:14px;background:var(--sky);color:var(--navy);border:0;padding:11px 14px;cursor:pointer;}
      .nl-form button:hover{background:#5cc3ff;}
      </style>
      <div class="nlbox">
        <p class="nl-head">Get the most recent news about Joga Labs!</p>
        <form class="nl-form" onsubmit="return jlNews(this)">
          <input name="fname" placeholder="First Name" required aria-label="First Name">
          <input name="lname" placeholder="Last Name" required aria-label="Last Name">
          <input type="email" name="email" placeholder="Email" required aria-label="Email">
          <select name="interest" required aria-label="Interest" onchange="this.classList.add('filled')">
            <option value="" disabled selected>I&rsquo;m interested in&hellip;</option>
            <option>Futsal Team</option>
            <option>Classes</option>
            <option>Autism Soccer</option>
          </select>
          <button type="submit">Sign Up</button>
        </form>
        <!-- MAILERLITE-NEWSLETTER-EMBED-SLOT -->
      </div>
      <script>
      function jlNews(f){var d=new FormData(f);
        window.location.href='mailto:info@jogalab.com?subject='+encodeURIComponent('Newsletter Signup - '+d.get('interest'))
        +'&body='+encodeURIComponent('Please add me to the Joga Labs newsletter.\\n\\nFirst Name: '+d.get('fname')+'\\nLast Name: '+d.get('lname')+'\\nEmail: '+d.get('email')+'\\nInterested in: '+d.get('interest'));
        return false;}
      </script>
    </div>'''

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

n = 0
for f in glob.glob('*.html'):
    if '-old' in f or f.startswith('email-'): continue
    s = io.open(f, encoding='utf-8').read()
    if OLD in s:
        io.open(f, 'w', encoding='utf-8').write(s.replace(OLD, NEW)); n += 1
print('local files updated:', n)

payload = {'old': to_wp(OLD), 'new': to_wp(NEW)}
raw = gzip.compress(json.dumps(payload, ensure_ascii=False).encode('utf-8'))
def chunk(typ, data):
    return struct.pack('>I', len(data)) + typ + data + struct.pack('>I', zlib.crc32(typ + data) & 0xffffffff)
png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0))
       + chunk(b'IDAT', zlib.compress(b'\x00\x00\x00\x00')) + chunk(b'IEND', b''))
io.open('jl-footer3-data.png', 'wb').write(png + b'JLDATA' + raw)
print('payload gz:', len(raw))
