# Joga Labs Website — Next Steps Guide

Your working files: 21 HTML pages + the `assets/` folder (photos, video, waves.svg). Keep them together.

---

## 1. Adding This to WordPress

Your live site (jogalab.com) runs WordPress with Divi-style builders. You have three options, easiest to hardest:

### Option A — Page-by-page with a "blank canvas" template (recommended to start)
1. In WP Admin, create a new Page (e.g. "Locations").
2. Set the page template to **Blank** / **Canvas** (Divi: "Blank Page"; most themes have one). This removes the theme's own header/footer so they don't double up.
3. Add a **Code block** (Divi: "Code" module; Gutenberg: "Custom HTML" block).
4. Open my HTML file in a text editor. Copy everything **between `<body>` and `</body>`** and paste it into the code block.
5. Copy everything between `<style>` and `</style>` and paste it at the top of the same code block wrapped in `<style>...</style>` tags. Same for the `<script>` blocks at the bottom.
6. Upload the `assets/` images via **Media Library**, then find-and-replace `assets/img_1282.jpg` etc. with the WordPress media URLs (they'll look like `/wp-content/uploads/2026/07/img_1282.jpg`).
7. Set the page's **slug** to match: `locations`, `keller-tx-futsal`, etc. (Settings → Permalinks must be set to "Post name".)
8. In your SEO plugin (Yoast/RankMath), paste in the title tag and meta description from the top of each HTML file.

### Option B — Keep your theme's header/footer
Same as A, but paste only the content sections (skip my `<header>`/`<footer>`) into a normal page. Less consistent, but faster and keeps your existing menus.

### Option C — Custom child theme (best long-term, needs a developer)
Turn the design into a proper WordPress theme: header.php / footer.php from my shared header/footer, page templates for labs and city pages, and WP menus. This makes every future page automatic. Any WordPress freelancer can do this in a few hours with my files as the spec — the CSS is one self-contained block per page.

**Important WordPress notes**
- The city-page slugs must be exactly: `keller-tx-futsal`, `north-fort-worth-tx-futsal`, `haslet-tx-futsal`, `watauga-tx-futsal`, `roanoke-tx-futsal`, `justin-tx-futsal`, `saginaw-tx-futsal`, `northlake-tx-futsal`, `westlake-tx-futsal`, `trophy-club-tx-futsal`, `argyle-tx-futsal`, `colleyville-tx-futsal`, `arlington-tx-futsal` — plus `locations`.
- Each file's `<script type="application/ld+json">` block is the structured data — paste it via your SEO plugin's "schema" box or keep it in the Code block.
- Internal links in my files point to `.html` files (for local preview). On WordPress, find-and-replace them to clean URLs: `team-labs.html` → `/team-labs/`, `keller-tx-futsal.html` → `/keller-tx-futsal/`, `jogalabs-website.html` → `/`.

---

## 2. Connecting MailerLite

Right now the forms open the visitor's email app addressed to info@jogalabs.com (works everywhere, no backend). To capture leads in MailerLite instead:

### Step 1 — Create the form in MailerLite
1. MailerLite dashboard → **Forms → Embedded forms → Create**.
2. Add fields to match the site's form: name, email, phone, plus custom fields (**Subscribers → Fields**) for `player_name`, `player_age`, `player_birthdate`, `experience`, `program`, `preferred_contact`.
3. Create one **Group** per program: "Team Labs Leads", "Classes Leads", "Inspire Labs Leads", "General Contact" — so each form feeds the right group.

### Step 2 — Embed it
MailerLite gives you an embed snippet like:
```html
<div class="ml-embedded" data-form="XXXXXX"></div>
<script src="https://assets.mailerlite.com/js/universal.js" async></script>
```
Replace the `<form class="join-form">...</form>` block in each page with that snippet (keep the surrounding `<section id="join-form">` so the Join buttons still scroll there). You can style MailerLite forms in their editor to match: navy `#0d1155`, sky `#38b6ff`, square corners, Inter font.

### Step 3 — Automate
- **Automations → New**: when someone joins "Team Labs Leads" → send a welcome email with tryout details + Chaos address → notify yourself.
- Turn on **double opt-in** only for the newsletter, not tryout forms (you don't want to lose a lead over an unconfirmed email).

If you send me your MailerLite embed codes, I'll wire them into the pages for you.

---

## 3. Using GitHub for This Project

GitHub gives you version history (every change saved forever), safe experimentation, and free hosting for previews.

### One-time setup (15 minutes)
1. Create an account at github.com → **New repository** → name it `jogalabs-website`, keep it **Private**.
2. Install **GitHub Desktop** (desktop.github.com) — no command line needed.
3. In GitHub Desktop: **Clone** your repository to a folder on your computer.
4. Copy all the HTML files + `assets/` folder into that folder.
5. GitHub Desktop will show all files as changes → write a summary like "Initial site v2" → **Commit to main** → **Push origin**.

### Daily workflow
- Edit files (or drop in new versions I make) → open GitHub Desktop → review what changed → Commit with a short note ("Updated summer schedule") → Push.
- Made a mistake? Right-click any commit → revert. Nothing is ever lost.

### Free live preview with GitHub Pages
1. Repo → **Settings → Pages** → Source: "Deploy from a branch" → `main`.
2. Rename `jogalabs-website.html` to `index.html` first (GitHub Pages treats index.html as the homepage).
3. Your site appears at `https://YOURNAME.github.io/jogalabs-website/` in ~1 minute — perfect for previewing changes and sharing with parents/partners before touching WordPress. (Keep the repo public, or upgrade for private Pages.)

### Suggested repo structure
```
jogalabs-website/
├── index.html            (renamed from jogalabs-website.html)
├── team-labs.html, soccer-classes.html, inspire-labs.html
├── about.html, faq.html, contact.html
├── locations.html + 13 city pages
├── assets/               (images, video, waves.svg)
└── README.md             (notes to yourself)
```

---

## 4. SEO Recommendations (what's done + what's next)

### Already built into the site
- Unique keyword-targeted title tags & meta descriptions on all 21 pages
- Canonical URLs matching your desired structure (`/keller-tx-futsal` etc.)
- Structured data: SportsOrganization (home), FAQPage (FAQ), SportsActivityLocation with `areaServed` (each city page)
- Unique, non-duplicated copy per city page (Google penalizes copy-paste city pages)
- Internal linking: footer "Areas We Serve" on every page + locations hub + breadcrumbs
- Descriptive alt text on images, lazy loading, one H1 per page

### Do next (highest impact first)
1. **Google Business Profile** — the #1 local SEO lever. Create/claim "Joga Labs" with the Southlake address, add photos, your schedule, and get parents to leave reviews. Reviews mentioning "futsal" and city names are gold.
2. **Google Search Console** — verify jogalab.com, submit your sitemap (`jogalab.com/sitemap.xml` — your SEO plugin generates it). You'll see exactly which searches you appear for.
3. **Consistent NAP** — your Name/Address/Phone must be identical everywhere: site footer, Google, Facebook, league pages. Right now use: Joga Labs, 250 Players Cir, Southlake, TX 76092, (214) 206-6151.
4. **Local citations** — list the club on Bing Places, Apple Maps, Yelp, and youth-sports directories (SincSports, local chamber, Keller/Southlake community sites).
5. **Backlinks from the league** — ask Chaos Sports Performance and LeagueLobster to link "Joga Labs" to jogalab.com on their pages. Local, relevant links beat everything.
6. **Post match recaps** — a short weekly "Club News" post ("Joga Labs Red 5–3 Hurst United...") keeps the site fresh, targets long-tail searches, and gives parents something to share.
7. **YouTube optimization** — your videos rank too. Retitle them with keywords ("Youth Futsal Training in Keller, TX — Joga Labs") and put jogalab.com in the descriptions.
8. **Page speed** — compress the gallery JPGs to WebP when uploading to WordPress (plugins like ShortPixel do it automatically).
9. **Expand city pages over time** — add a real photo or testimonial from a family in that city to each page as you get them. Unique local content compounds.
