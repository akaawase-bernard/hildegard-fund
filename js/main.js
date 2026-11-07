// The Hildegard Fund

// Header turns frosted once you scroll
const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 10);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Gentle fade-up as sections come into view
const reveals = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
  reveals.forEach((el) => io.observe(el));
} else {
  reveals.forEach((el) => el.classList.add("in"));
}

// Mobile menu
const menuBtn = document.querySelector(".menu-btn");
const mobileNav = document.getElementById("mobile-nav");
menuBtn.addEventListener("click", () => {
  const open = mobileNav.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", open);
});

// Testimony video: put a YouTube embed link in the button's data-video attribute
const video = document.querySelector(".video");
if (video) {
  video.addEventListener("click", () => {
    const src = video.dataset.video;
    if (!src) return;
    video.innerHTML = `<iframe src="${src}?autoplay=1" title="Testimony" allow="autoplay; encrypted-media" allowfullscreen></iframe>`;
  });
}

// Donate form
const donate = document.querySelector(".donate-form");
if (donate) {
  const msg = donate.querySelector(".form-msg");
  const other = donate.querySelector('[name="other"]');
  const preset = new URLSearchParams(location.search).get("amount");
  if (preset) {
    const r = donate.querySelector(`[name="amount"][value="${preset}"]`);
    if (r) r.checked = true;
  }
  other.addEventListener("input", () => {
    donate.querySelectorAll('[name="amount"]').forEach((r) => (r.checked = false));
  });
  donate.addEventListener("change", (e) => {
    if (e.target.name === "amount") other.value = "";
  });
  donate.addEventListener("submit", (e) => {
    e.preventDefault();
    const picked = donate.querySelector('[name="amount"]:checked');
    const amount = Number(other.value) || (picked && Number(picked.value));
    if (!amount) {
      msg.textContent = "Please choose an amount.";
      return;
    }
    // Connect your payment provider here (Stripe, Givebutter, Donorbox...).
    msg.textContent = "Online payments aren't set up yet. Thank you for your patience.";
  });
}

// Newsletter
const news = document.querySelector(".news-form");
// The form posts to the Mailchimp audience "The Hildegard Fund", which opens its confirmation in a new tab.
news.addEventListener("submit", (e) => {
  const email = news.querySelector('[name="EMAIL"]').value.trim();
  const out = document.querySelector(".news-msg");
  if (!/^\S+@\S+\.\S+$/.test(email)) {
    e.preventDefault();
    out.textContent = "That email address doesn't look right.";
    return;
  }
  out.textContent = "Thank you! Your sign-up is finishing in a new tab.";
  setTimeout(() => news.reset(), 500);
});
