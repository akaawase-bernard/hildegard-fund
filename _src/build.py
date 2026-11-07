"""Assemble the Hildegard Fund pages with a shared header and footer."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
SRC = pathlib.Path(__file__).parent / "pages"

NAV = [("about.html", "About Us"), ("approach.html", "Our Approach"),
       ("get-involved.html", "Work With Us"), ("about.html#faq", "FAQ")]

def header(current):
    links = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>'
        for h, t in NAV)
    mlinks = "\n".join(f'      <a href="{h}">{t}</a>' for h, t in NAV)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="index.html"><i>The</i> Hildegard Fund</a>
    <div class="header-right">
      <nav class="nav" aria-label="Main">
{links}
      </nav>
      <a class="donate-btn" href="https://www.paypal.com/pool/9ub8hglGhU?sr=wccr" target="_blank" rel="noopener">Donate</a>
      <button class="menu-btn" aria-expanded="false" aria-controls="mobile-nav" aria-label="Menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
      </button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Main">
    <div>
{mlinks}
      <a href="get-involved.html#contact">Contact Us</a>
    </div>
  </nav>
</header>"""

FOOTER = """<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <p class="footer-name"><i>The</i><br>Hildegard Fund</p>
        <p>Helping families welcome their babies at home, with a midwife by their side.</p>
      </div>
      <div>
        <h4>About Us</h4>
        <ul>
          <li><a href="about.html#vision">Our vision &amp; values</a></li>
          <li><a href="about.html#history">History of homebirth</a></li>
          <li><a href="about.html#team">Meet the team</a></li>
          <li><a href="about.html#partners">Partners</a></li>
          <li><a href="about.html#accountability">Accountability</a></li>
          <li><a href="about.html#faq">FAQ</a></li>
        </ul>
      </div>
      <div>
        <h4>Our Approach</h4>
        <ul>
          <li><a href="approach.html#sponsorship">Sponsorship</a></li>
          <li><a href="approach.html#legal">Legal campaign</a></li>
          <li><a href="approach.html#goals">Long-term goals</a></li>
        </ul>
        <h4>Work With Us</h4>
        <ul>
          <li><a href="get-involved.html#volunteer">Volunteer roles</a></li>
        </ul>
      </div>
      <div>
        <h4>Connect With Us</h4>
        <div class="socials">
          <a href="https://www.facebook.com/profile.php?id=61595986334964&amp;sk=directory_communities" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8z"/></svg></a>
        </div>
        <h4>Contact Us</h4>
        <ul>
          <li><a href="get-involved.html#contact">Write to us</a></li>
        </ul>
      </div>
    </div>

    <div class="newsletter">
      <h3>Get our <em>newsletter</em></h3>
      <form class="news-form" novalidate method="post" target="_blank" rel="noopener" action="https://hildegardfund.us11.list-manage.com/subscribe/post?u=039ddeb687fab4f3319a299d8&amp;id=04e54910ec">
        <label class="sr-only" for="news-email">Email address</label>
        <input type="email" name="EMAIL" id="news-email" placeholder="Email address" autocomplete="email">
        <div aria-hidden="true" style="position:absolute;left:-5000px"><input type="text" name="b_039ddeb687fab4f3319a299d8_04e54910ec" tabindex="-1" value=""></div>
        <button type="submit" aria-label="Sign up">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
        </button>
      </form>
      <p class="news-msg" aria-live="polite"></p>
    </div>

    <p class="copyright">&copy; The Hildegard Fund 2026</p>
  </div>
</footer>"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600'
         '&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">')

for src in sorted(SRC.glob("*.html")):
    raw = src.read_text()
    title, desc, body = raw.split("\n---\n", 2)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title.strip()}</title>
  <meta name="description" content="{desc.strip()}">
  {FONTS}
  <link rel="stylesheet" href="css/style.css?v=10">
  <script>document.documentElement.classList.add("js")</script>
</head>
<body>

{header(src.name)}

<main>
{body.strip()}
</main>

{FOOTER}

<script src="js/main.js?v=12"></script>
</body>
</html>
"""
    (OUT / src.name).write_text(page)
    print("wrote", src.name)
