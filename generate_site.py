"""
PeakPicks - Auto Site Generator
Runs weekly via GitHub Actions to refresh the store with trending Amazon products.
Affiliate tag: peakpicks0c6-20
"""

import json
from datetime import datetime

AFFILIATE_TAG = "peakpicks0c6-20"
CURRENT_DATE = datetime.now().strftime("%B %d, %Y")

# ─────────────────────────────────────────────
# PRODUCT DATA — Update this list to add/remove
# products. To add a new product, copy one block
# and change the fields. Find the ASIN in the
# Amazon product URL: amazon.com/dp/ASIN
# ─────────────────────────────────────────────
PRODUCTS = [
    {
        "id": 1, "category": "electronics",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "🎧",
        "name": "Apple AirPods 4",
        "desc": "Active noise cancellation, adaptive audio, and seamless Apple ecosystem integration. The #1 electronics bestseller on Amazon.",
        "rating": 4.8, "reviews": "148K",
        "price": "129.00",
        "commission": "~$5.16 per sale",
        "asin": "B0DBYRZHJR"
    },
    {
        "id": 2, "category": "kitchen",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "🥤",
        "name": "Stanley Quencher H2.0 Tumbler",
        "desc": "Viral TikTok sensation turned Amazon staple. Keeps drinks cold for 2 days. Available in 30+ colors.",
        "rating": 4.7, "reviews": "213K",
        "price": "45.00",
        "commission": "~$2.03 per sale",
        "asin": "B09Z7ZLFHK"
    },
    {
        "id": 3, "category": "beauty",
        "badge": "trending", "badgeClass": "badge-trending",
        "icon": "✨",
        "name": "Mighty Patch Original",
        "desc": "Hero Cosmetics #1 hydrocolloid acne patch. Shrinks blemishes overnight. 36 count — one of beauty's top sellers.",
        "rating": 4.6, "reviews": "340K",
        "price": "14.97",
        "commission": "~$1.50 per sale",
        "asin": "B074PVTPBW"
    },
    {
        "id": 4, "category": "electronics",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "📺",
        "name": "Amazon Fire TV Stick 4K",
        "desc": "Stream in 4K Ultra HD with Dolby Vision. Alexa Voice Remote included. Consistently top-10 on Amazon.",
        "rating": 4.7, "reviews": "500K",
        "price": "49.99",
        "commission": "~$2.00 per sale",
        "asin": "B0BP9SNVH9"
    },
    {
        "id": 5, "category": "beauty",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "🧴",
        "name": "CeraVe Daily Moisturizing Lotion",
        "desc": "Dermatologist-recommended for all skin types. 3 essential ceramides & hyaluronic acid. Massive repeat purchase rate.",
        "rating": 4.8, "reviews": "420K",
        "price": "17.99",
        "commission": "~$1.80 per sale",
        "asin": "B000YJ2SKO"
    },
    {
        "id": 6, "category": "kitchen",
        "badge": "trending", "badgeClass": "badge-trending",
        "icon": "🍟",
        "name": "Ninja AF101 Air Fryer",
        "desc": "Fry with up to 75% less fat. 4-quart ceramic coated basket, dishwasher safe. A kitchen staple since 2023.",
        "rating": 4.7, "reviews": "185K",
        "price": "99.99",
        "commission": "~$4.50 per sale",
        "asin": "B07FDJMC9Q"
    },
    {
        "id": 7, "category": "electronics",
        "badge": "new", "badgeClass": "badge-new",
        "icon": "📖",
        "name": "Kindle Paperwhite Signature",
        "desc": "The best e-reader on the market. Glare-free display, wireless charging, adjustable warm light. Bookworms' top pick.",
        "rating": 4.8, "reviews": "92K",
        "price": "189.99",
        "commission": "~$7.60 per sale",
        "asin": "B09TMF6742"
    },
    {
        "id": 8, "category": "home",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "🔔",
        "name": "Ring Video Doorbell",
        "desc": "See and speak to visitors from your phone. Instant alerts, HD video. Amazon's top smart home security device.",
        "rating": 4.6, "reviews": "280K",
        "price": "99.99",
        "commission": "~$8.00 per sale",
        "asin": "B08N5NQ869"
    },
    {
        "id": 9, "category": "kitchen",
        "badge": "trending", "badgeClass": "badge-trending",
        "icon": "🫧",
        "name": "Instant Pot Duo 7-in-1",
        "desc": "Pressure cooker, slow cooker, rice cooker, steamer, sauté pan & more. Replace 7 appliances with one.",
        "rating": 4.7, "reviews": "310K",
        "price": "89.99",
        "commission": "~$4.05 per sale",
        "asin": "B00FLYWNYQ"
    },
    {
        "id": 10, "category": "home",
        "badge": "new", "badgeClass": "badge-new",
        "icon": "🌿",
        "name": "LEVOIT Air Purifier Core 300",
        "desc": "3-stage filtration captures 99.97% of particles. Ultra-quiet for bedroom use. Home wellness top pick for 2026.",
        "rating": 4.7, "reviews": "95K",
        "price": "99.98",
        "commission": "~$8.00 per sale",
        "asin": "B08L73QL1V"
    },
    {
        "id": 11, "category": "beauty",
        "badge": "trending", "badgeClass": "badge-trending",
        "icon": "💄",
        "name": "essence Lash Princess Mascara",
        "desc": "The most-reviewed mascara on Amazon. Dramatic false-lash effect. Cruelty-free and paraben-free.",
        "rating": 4.4, "reviews": "680K",
        "price": "9.99",
        "commission": "~$1.00 per sale",
        "asin": "B00LMJYIIA"
    },
    {
        "id": 12, "category": "electronics",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "💻",
        "name": "Anker Wireless Charger 15W",
        "desc": "Fast charge any Qi device. Ultra-slim design, intelligent temperature control. Tech essential for every desk.",
        "rating": 4.6, "reviews": "130K",
        "price": "15.99",
        "commission": "~$0.64 per sale",
        "asin": "B07DBX2GHL"
    },
    {
        "id": 13, "category": "fitness",
        "badge": "trending", "badgeClass": "badge-trending",
        "icon": "💪",
        "name": "Resistance Bands Set by Fit Simplify",
        "desc": "5 resistance levels, stackable up to 150 lbs. Perfect for home workouts, physical therapy, and travel.",
        "rating": 4.6, "reviews": "220K",
        "price": "29.99",
        "commission": "~$1.35 per sale",
        "asin": "B01AVDVHTI"
    },
    {
        "id": 14, "category": "home",
        "badge": "bestseller", "badgeClass": "badge-bestseller",
        "icon": "☕",
        "name": "Keurig K-Mini Coffee Maker",
        "desc": "Brew any K-Cup pod in under 2 minutes. 6–12 oz cup sizes. Perfect for small spaces and solo coffee drinkers.",
        "rating": 4.6, "reviews": "175K",
        "price": "79.99",
        "commission": "~$3.60 per sale",
        "asin": "B07GV2S1GS"
    },
    {
        "id": 15, "category": "fitness",
        "badge": "new", "badgeClass": "badge-new",
        "icon": "🧘",
        "name": "Manduka PRO Yoga Mat",
        "desc": "Professional-grade 6mm mat with lifetime guarantee. Superior cushioning and non-slip surface loved by instructors.",
        "rating": 4.7, "reviews": "48K",
        "price": "120.00",
        "commission": "~$5.40 per sale",
        "asin": "B07D7XPQK9"
    }
]


def build_product_js(products):
    return json.dumps(products, ensure_ascii=False, indent=2)


def generate_html(products, affiliate_tag, current_date):
    products_json = build_product_js(products)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PeakPicks — Amazon's Top Sellers, Curated Daily</title>
<meta name="description" content="Shop Amazon's top-ranked bestsellers across every category. All products fulfilled by Amazon FBA. Updated weekly.">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {{
    --ink: #0e0d0b;
    --cream: #f5f1ea;
    --warm: #e8e0d0;
    --gold: #c8922a;
    --gold-light: #f0c060;
    --rust: #b84a2e;
    --sage: #5a7060;
    --card-bg: #ffffff;
    --shadow: 0 2px 24px rgba(14,13,11,0.10);
    --shadow-hover: 0 8px 48px rgba(14,13,11,0.18);
  }}
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: 'DM Sans', sans-serif;
    background: var(--cream);
    color: var(--ink);
    min-height: 100vh;
    overflow-x: hidden;
  }}
  nav {{
    position: sticky; top: 0; z-index: 100;
    background: var(--ink);
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 5vw;
    height: 64px;
    border-bottom: 2px solid var(--gold);
  }}
  .nav-logo {{
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; font-weight: 900;
    color: var(--gold); letter-spacing: -0.5px; text-decoration: none;
  }}
  .nav-logo span {{ color: #fff; }}
  .nav-links {{ display: flex; gap: 2rem; list-style: none; }}
  .nav-links a {{
    color: var(--warm); text-decoration: none;
    font-size: 0.88rem; font-weight: 500;
    letter-spacing: 0.04em; text-transform: uppercase; transition: color 0.2s;
  }}
  .nav-links a:hover {{ color: var(--gold); }}
  .nav-badge {{
    background: var(--gold); color: var(--ink);
    font-size: 0.75rem; font-weight: 700;
    padding: 4px 12px; border-radius: 100px;
    letter-spacing: 0.05em; text-transform: uppercase;
  }}
  .update-banner {{
    background: var(--sage); color: #fff;
    text-align: center; padding: 8px;
    font-size: 0.8rem; letter-spacing: 0.04em;
  }}
  .hero {{
    min-height: 72vh; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center; padding: 6rem 5vw 4rem;
    position: relative; overflow: hidden; background: var(--ink);
  }}
  .hero::before {{
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse at 60% 30%, #2a1a00 0%, transparent 65%),
                radial-gradient(ellipse at 20% 80%, #1a0a00 0%, transparent 55%);
    opacity: 0.8;
  }}
  .hero-eyebrow {{
    position: relative; display: inline-flex; align-items: center; gap: 0.5rem;
    background: rgba(200,146,42,0.15); border: 1px solid rgba(200,146,42,0.4);
    color: var(--gold-light); font-size: 0.78rem; font-weight: 600;
    letter-spacing: 0.12em; text-transform: uppercase;
    padding: 6px 18px; border-radius: 100px; margin-bottom: 2rem;
    animation: fadeDown 0.7s ease both;
  }}
  .pulse-dot {{
    width: 7px; height: 7px; background: #4caf50;
    border-radius: 50%; animation: pulse 1.8s infinite;
  }}
  @keyframes pulse {{ 0%,100% {{ opacity:1;transform:scale(1); }} 50% {{ opacity:0.5;transform:scale(1.4); }} }}
  .hero h1 {{
    position: relative;
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 7vw, 6rem); font-weight: 900;
    line-height: 1.05; color: #fff; margin-bottom: 1.4rem;
    animation: fadeDown 0.8s 0.1s ease both;
  }}
  .hero h1 em {{ font-style: normal; color: var(--gold); display: block; }}
  .hero p {{
    position: relative; max-width: 520px;
    color: rgba(255,255,255,0.6); font-size: 1.08rem;
    line-height: 1.7; margin-bottom: 2.5rem;
    animation: fadeDown 0.8s 0.2s ease both;
  }}
  .hero-cta {{
    position: relative; display: flex; gap: 1rem;
    flex-wrap: wrap; justify-content: center;
    animation: fadeDown 0.8s 0.3s ease both;
  }}
  .btn-primary {{
    background: var(--gold); color: var(--ink);
    font-weight: 700; font-size: 0.92rem; padding: 14px 32px;
    border-radius: 6px; text-decoration: none; letter-spacing: 0.04em;
    text-transform: uppercase; transition: transform 0.2s, box-shadow 0.2s, background 0.2s;
    box-shadow: 0 4px 20px rgba(200,146,42,0.35);
  }}
  .btn-primary:hover {{ transform: translateY(-2px); background: var(--gold-light); }}
  .btn-ghost {{
    background: transparent; border: 1.5px solid rgba(255,255,255,0.25);
    color: rgba(255,255,255,0.8); font-weight: 500; font-size: 0.92rem;
    padding: 14px 32px; border-radius: 6px; text-decoration: none;
    transition: border-color 0.2s, color 0.2s;
  }}
  .btn-ghost:hover {{ border-color: var(--gold); color: var(--gold); }}
  .hero-stats {{
    position: relative; display: flex; gap: 3rem; flex-wrap: wrap;
    justify-content: center; margin-top: 4rem; padding-top: 3rem;
    border-top: 1px solid rgba(255,255,255,0.1);
    animation: fadeDown 0.8s 0.4s ease both;
  }}
  .stat {{ text-align: center; }}
  .stat-num {{
    font-family: 'Playfair Display', serif; font-size: 2.2rem;
    font-weight: 700; color: var(--gold); display: block; line-height: 1;
  }}
  .stat-label {{
    font-size: 0.75rem; color: rgba(255,255,255,0.45);
    text-transform: uppercase; letter-spacing: 0.08em; margin-top: 4px;
  }}
  @keyframes fadeDown {{ from {{ opacity:0;transform:translateY(-18px); }} to {{ opacity:1;transform:translateY(0); }} }}
  .marquee-wrap {{ background: var(--gold); padding: 10px 0; overflow: hidden; white-space: nowrap; }}
  .marquee-inner {{ display: inline-block; animation: marquee 28s linear infinite; }}
  .marquee-inner span {{
    font-size: 0.78rem; font-weight: 700; color: var(--ink);
    letter-spacing: 0.08em; text-transform: uppercase; margin: 0 2.5rem;
  }}
  .marquee-inner span::before {{ content: '★  '; }}
  @keyframes marquee {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-50%); }} }}
  .section {{ padding: 5rem 5vw; }}
  .section-header {{
    display: flex; align-items: flex-end; justify-content: space-between;
    margin-bottom: 2.5rem; flex-wrap: wrap; gap: 1rem;
  }}
  .section-title {{
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 700;
    color: var(--ink); line-height: 1.15;
  }}
  .section-title span {{ color: var(--gold); }}
  .section-sub {{ font-size: 0.88rem; color: #777; margin-top: 6px; }}
  .see-all {{
    font-size: 0.85rem; font-weight: 600; color: var(--gold);
    text-decoration: none; letter-spacing: 0.04em; white-space: nowrap;
    border-bottom: 1.5px solid currentColor; padding-bottom: 1px;
  }}
  .tabs {{ display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 2.5rem; }}
  .tab-btn {{
    padding: 8px 20px; border-radius: 100px; border: 1.5px solid #ddd;
    background: transparent; color: #555; font-size: 0.85rem; font-weight: 500;
    cursor: pointer; transition: all 0.2s; font-family: inherit;
  }}
  .tab-btn:hover {{ border-color: var(--gold); color: var(--gold); }}
  .tab-btn.active {{ background: var(--ink); border-color: var(--ink); color: #fff; }}
  .product-grid {{
    display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 1.5rem;
  }}
  .product-card {{
    background: var(--card-bg); border-radius: 12px; overflow: hidden;
    box-shadow: var(--shadow); transition: transform 0.25s, box-shadow 0.25s;
    display: flex; flex-direction: column; position: relative; cursor: pointer;
  }}
  .product-card:hover {{ transform: translateY(-5px); box-shadow: var(--shadow-hover); }}
  .card-badge {{
    position: absolute; top: 14px; left: 14px; z-index: 2;
    font-size: 0.68rem; font-weight: 700; letter-spacing: 0.08em;
    text-transform: uppercase; padding: 4px 10px; border-radius: 4px;
  }}
  .badge-bestseller {{ background: var(--gold); color: var(--ink); }}
  .badge-trending {{ background: var(--rust); color: #fff; }}
  .badge-new {{ background: var(--sage); color: #fff; }}
  .card-img-placeholder {{ font-size: 4.5rem; padding: 2rem 0; text-align: center; background: var(--warm); }}
  .card-body {{ padding: 1.2rem 1.4rem 1.4rem; flex: 1; display: flex; flex-direction: column; }}
  .card-category {{
    font-size: 0.72rem; font-weight: 600; letter-spacing: 0.1em;
    text-transform: uppercase; color: var(--gold); margin-bottom: 0.4rem;
  }}
  .card-title {{
    font-family: 'Playfair Display', serif; font-size: 1.05rem;
    font-weight: 700; line-height: 1.3; color: var(--ink); margin-bottom: 0.5rem;
  }}
  .card-desc {{ font-size: 0.82rem; color: #666; line-height: 1.55; margin-bottom: 1rem; flex: 1; }}
  .stars {{ display: flex; align-items: center; gap: 5px; font-size: 0.8rem; margin-bottom: 1rem; }}
  .stars-icons {{ color: var(--gold); letter-spacing: -1px; }}
  .stars-count {{ color: #888; }}
  .card-footer {{
    display: flex; align-items: center; justify-content: space-between;
    margin-top: auto; padding-top: 0.8rem; border-top: 1px solid var(--warm);
  }}
  .card-price {{ font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 700; color: var(--ink); }}
  .card-price sup {{ font-size: 0.7em; vertical-align: super; }}
  .commission {{ font-size: 0.72rem; color: var(--sage); font-weight: 600; margin-top: 1px; }}
  .btn-amazon {{
    background: var(--gold); color: var(--ink); font-size: 0.8rem; font-weight: 700;
    padding: 10px 18px; border-radius: 6px; text-decoration: none;
    letter-spacing: 0.03em; transition: background 0.2s, transform 0.15s; white-space: nowrap;
  }}
  .btn-amazon:hover {{ background: var(--gold-light); transform: scale(1.04); }}
  .how-section {{
    background: var(--ink); padding: 5rem 5vw; position: relative; overflow: hidden;
  }}
  .how-section .section-title {{ color: #fff; }}
  .how-section .section-title span {{ color: var(--gold); }}
  .steps-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 2rem; margin-top: 3rem; }}
  .step {{ padding: 2rem; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; transition: border-color 0.2s; }}
  .step:hover {{ border-color: var(--gold); }}
  .step-num {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; font-weight: 900; color: rgba(200,146,42,0.18); line-height: 1; margin-bottom: 1rem; }}
  .step-icon {{ font-size: 1.8rem; margin-bottom: 0.8rem; display: block; }}
  .step h3 {{ font-family: 'Playfair Display', serif; font-size: 1.15rem; font-weight: 700; color: #fff; margin-bottom: 0.6rem; }}
  .step p {{ font-size: 0.85rem; color: rgba(255,255,255,0.5); line-height: 1.65; }}
  .categories-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 1rem; }}
  .cat-card {{
    background: var(--card-bg); border-radius: 12px; padding: 1.8rem 1.2rem;
    text-align: center; box-shadow: var(--shadow); text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s; border: 1.5px solid transparent;
  }}
  .cat-card:hover {{ transform: translateY(-4px); box-shadow: var(--shadow-hover); border-color: var(--gold); }}
  .cat-icon {{ font-size: 2.2rem; margin-bottom: 0.7rem; display: block; }}
  .cat-name {{ font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: var(--ink); display: block; margin-bottom: 4px; }}
  .cat-count {{ font-size: 0.75rem; color: #888; }}
  .calc-section {{ background: linear-gradient(135deg, #1a1006 0%, #0e0d0b 60%); padding: 5rem 5vw; border-top: 2px solid var(--gold); border-bottom: 2px solid var(--gold); }}
  .calc-inner {{ max-width: 700px; margin: 0 auto; text-align: center; }}
  .calc-inner .section-title {{ color: #fff; margin-bottom: 0.5rem; }}
  .calc-inner p {{ color: rgba(255,255,255,0.5); margin-bottom: 3rem; font-size: 0.95rem; }}
  .calc-controls {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 2rem; text-align: left; }}
  .ctrl-label {{ font-size: 0.78rem; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 8px; display: block; }}
  .ctrl-input, .ctrl-select {{
    width: 100%; background: rgba(255,255,255,0.07); border: 1.5px solid rgba(255,255,255,0.15);
    border-radius: 8px; color: #fff; font-size: 1rem; padding: 12px 16px;
    font-family: inherit; outline: none; transition: border-color 0.2s; appearance: none;
  }}
  .ctrl-input:focus, .ctrl-select:focus {{ border-color: var(--gold); }}
  .ctrl-select option {{ background: #1a1006; }}
  .calc-result {{
    background: rgba(200,146,42,0.1); border: 1.5px solid rgba(200,146,42,0.35);
    border-radius: 12px; padding: 2rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;
  }}
  .result-item {{ text-align: center; }}
  .result-val {{ font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700; color: var(--gold); display: block; line-height: 1; }}
  .result-label {{ font-size: 0.72rem; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 4px; }}
  footer {{ background: var(--ink); padding: 3rem 5vw 2rem; border-top: 1px solid rgba(255,255,255,0.08); }}
  .footer-top {{ display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 2rem; margin-bottom: 2rem; }}
  .footer-brand .nav-logo {{ display: block; margin-bottom: 0.8rem; font-size: 1.3rem; }}
  .footer-brand p {{ font-size: 0.82rem; color: rgba(255,255,255,0.35); max-width: 280px; line-height: 1.65; }}
  .footer-links h4 {{ color: rgba(255,255,255,0.6); font-size: 0.78rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1rem; }}
  .footer-links ul {{ list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }}
  .footer-links a {{ color: rgba(255,255,255,0.4); font-size: 0.85rem; text-decoration: none; transition: color 0.2s; }}
  .footer-links a:hover {{ color: var(--gold); }}
  .footer-bottom {{ border-top: 1px solid rgba(255,255,255,0.08); padding-top: 1.5rem; font-size: 0.75rem; color: rgba(255,255,255,0.25); line-height: 1.7; }}
  .footer-bottom a {{ color: rgba(200,146,42,0.5); text-decoration: none; }}
  @media (max-width: 640px) {{
    .nav-links {{ display: none; }}
    .calc-controls {{ grid-template-columns: 1fr; }}
    .calc-result {{ grid-template-columns: 1fr; }}
    .hero-stats {{ gap: 2rem; }}
    .footer-top {{ flex-direction: column; }}
  }}
</style>
</head>
<body>

<nav>
  <a class="nav-logo" href="#"><span>Peak</span>Picks</a>
  <ul class="nav-links">
    <li><a href="#products">Top Picks</a></li>
    <li><a href="#categories">Categories</a></li>
    <li><a href="#how">How It Works</a></li>
    <li><a href="#calculator">Earnings</a></li>
  </ul>
  <span class="nav-badge">🔥 Live Rankings</span>
</nav>

<div class="update-banner">✦ Store last updated: {current_date} — products refreshed from Amazon bestseller data</div>

<section class="hero">
  <div class="hero-eyebrow">
    <span class="pulse-dot"></span>
    Updated Weekly from Amazon Bestseller Data
  </div>
  <h1>Amazon's #1 Products,<em>Zero Inventory.</em></h1>
  <p>Shop the top-ranked items across every category — all fulfilled by Amazon. Earn passive income as an affiliate while Amazon handles storage, shipping, and returns.</p>
  <div class="hero-cta">
    <a href="#products" class="btn-primary">Browse Top Picks</a>
    <a href="#how" class="btn-ghost">How It Works</a>
  </div>
  <div class="hero-stats">
    <div class="stat"><span class="stat-num">2M+</span><span class="stat-label">Products Tracked</span></div>
    <div class="stat"><span class="stat-num">98%</span><span class="stat-label">Prime Eligible</span></div>
    <div class="stat"><span class="stat-num">4.6★</span><span class="stat-label">Avg. Rating</span></div>
    <div class="stat"><span class="stat-num">100%</span><span class="stat-label">FBA Fulfilled</span></div>
  </div>
</section>

<div class="marquee-wrap">
  <div class="marquee-inner">
    <span>Apple AirPods 4</span><span>Stanley Quencher</span><span>Mighty Patch</span><span>Ninja Air Fryer</span><span>CeraVe Moisturizer</span><span>Kindle Paperwhite</span><span>Fire TV Stick 4K</span><span>Instant Pot Duo</span><span>Ring Doorbell</span><span>LEVOIT Air Purifier</span><span>Apple AirPods 4</span><span>Stanley Quencher</span><span>Mighty Patch</span><span>Ninja Air Fryer</span><span>CeraVe Moisturizer</span><span>Kindle Paperwhite</span><span>Fire TV Stick 4K</span><span>Instant Pot Duo</span><span>Ring Doorbell</span><span>LEVOIT Air Purifier</span>
  </div>
</div>

<section class="section" id="products">
  <div class="section-header">
    <div>
      <div class="section-title">Top <span>Bestsellers</span> Right Now</div>
      <div class="section-sub">Ranked by Amazon sales velocity · Fulfilled by Amazon · Commission earned on every sale</div>
    </div>
    <a href="https://www.amazon.com/Best-Sellers/zgbs?tag={affiliate_tag}" target="_blank" class="see-all">See All on Amazon →</a>
  </div>
  <div class="tabs">
    <button class="tab-btn active" onclick="filterCategory('all', this)">All</button>
    <button class="tab-btn" onclick="filterCategory('electronics', this)">Electronics</button>
    <button class="tab-btn" onclick="filterCategory('beauty', this)">Beauty</button>
    <button class="tab-btn" onclick="filterCategory('kitchen', this)">Kitchen</button>
    <button class="tab-btn" onclick="filterCategory('fitness', this)">Fitness</button>
    <button class="tab-btn" onclick="filterCategory('home', this)">Home</button>
  </div>
  <div class="product-grid" id="productGrid"></div>
</section>

<section class="how-section" id="how">
  <div class="section-title">How <span>Passive Income</span> Works</div>
  <div class="steps-grid">
    <div class="step"><div class="step-num">01</div><span class="step-icon">🛍️</span><h3>Visitor Discovers a Product</h3><p>Someone finds PeakPicks through Google, social media, or word of mouth and clicks a product they love.</p></div>
    <div class="step"><div class="step-num">02</div><span class="step-icon">🔗</span><h3>They're Sent to Amazon</h3><p>Your affiliate link redirects them to Amazon.com where they can buy with one click and Prime shipping.</p></div>
    <div class="step"><div class="step-num">03</div><span class="step-icon">📦</span><h3>Amazon Fulfills Everything</h3><p>Amazon's FBA network picks, packs, ships, and handles returns. You touch nothing. Zero inventory.</p></div>
    <div class="step"><div class="step-num">04</div><span class="step-icon">💰</span><h3>You Earn Commission</h3><p>Amazon deposits 1–10% commission directly to you. Any purchase within 24 hours of the click counts.</p></div>
  </div>
</section>

<section class="section" id="categories">
  <div class="section-header"><div class="section-title">Shop by <span>Category</span></div></div>
  <div class="categories-grid">
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+electronics&tag={affiliate_tag}" target="_blank"><span class="cat-icon">🎧</span><span class="cat-name">Electronics</span><span class="cat-count">Up to 4% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+beauty&tag={affiliate_tag}" target="_blank"><span class="cat-icon">✨</span><span class="cat-name">Beauty</span><span class="cat-count">Up to 10% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+kitchen&tag={affiliate_tag}" target="_blank"><span class="cat-icon">🍳</span><span class="cat-name">Kitchen</span><span class="cat-count">Up to 4.5% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+fitness&tag={affiliate_tag}" target="_blank"><span class="cat-icon">💪</span><span class="cat-name">Fitness</span><span class="cat-count">Up to 4.5% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+home+decor&tag={affiliate_tag}" target="_blank"><span class="cat-icon">🏠</span><span class="cat-name">Home</span><span class="cat-count">Up to 8% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+clothing&tag={affiliate_tag}" target="_blank"><span class="cat-icon">👟</span><span class="cat-name">Fashion</span><span class="cat-count">Up to 10% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+pet+supplies&tag={affiliate_tag}" target="_blank"><span class="cat-icon">🐾</span><span class="cat-name">Pets</span><span class="cat-count">Up to 8% commission</span></a>
    <a class="cat-card" href="https://www.amazon.com/s?k=bestseller+smart+home&tag={affiliate_tag}" target="_blank"><span class="cat-icon">🏡</span><span class="cat-name">Smart Home</span><span class="cat-count">Up to 8% commission</span></a>
  </div>
</section>

<section class="calc-section" id="calculator">
  <div class="calc-inner">
    <div class="section-title">Estimate Your <span>Earnings</span></div>
    <p>See how much passive income this store could generate based on your traffic and conversions.</p>
    <div class="calc-controls">
      <div><span class="ctrl-label">Monthly Visitors</span><input class="ctrl-input" type="number" id="visitors" value="5000" oninput="calcEarnings()"></div>
      <div><span class="ctrl-label">Category</span>
        <select class="ctrl-select" id="category" onchange="calcEarnings()">
          <option value="0.08">Beauty & Fashion (8%)</option>
          <option value="0.045" selected>Home & Kitchen (4.5%)</option>
          <option value="0.04">Electronics (4%)</option>
          <option value="0.08">Pets & Smart Home (8%)</option>
        </select>
      </div>
      <div><span class="ctrl-label">Avg. Order Value ($)</span><input class="ctrl-input" type="number" id="aov" value="55" oninput="calcEarnings()"></div>
      <div><span class="ctrl-label">Conversion Rate (%)</span><input class="ctrl-input" type="number" id="cvr" value="3" step="0.1" oninput="calcEarnings()"></div>
    </div>
    <div class="calc-result">
      <div class="result-item"><span class="result-val" id="res-monthly">$0</span><span class="result-label">Monthly</span></div>
      <div class="result-item"><span class="result-val" id="res-annual">$0</span><span class="result-label">Annually</span></div>
      <div class="result-item"><span class="result-val" id="res-orders">0</span><span class="result-label">Est. Orders</span></div>
    </div>
  </div>
</section>

<footer>
  <div class="footer-top">
    <div class="footer-brand">
      <a class="nav-logo" href="#"><span>Peak</span>Picks</a>
      <p>A curated Amazon affiliate storefront. All products fulfilled by Amazon FBA. We earn a commission on qualifying purchases at no extra cost to you.</p>
    </div>
    <div class="footer-links"><h4>Shop</h4><ul><li><a href="#">Electronics</a></li><li><a href="#">Beauty</a></li><li><a href="#">Kitchen</a></li><li><a href="#">Home</a></li></ul></div>
    <div class="footer-links"><h4>Info</h4><ul><li><a href="#">About</a></li><li><a href="#">Affiliate Disclosure</a></li><li><a href="#">Privacy Policy</a></li><li><a href="#">Contact</a></li></ul></div>
  </div>
  <div class="footer-bottom">
    <p>© 2026 PeakPicks. PeakPicks is a participant in the <a href="https://affiliate-program.amazon.com/" target="_blank">Amazon Services LLC Associates Program</a>, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com. Amazon and the Amazon logo are trademarks of Amazon.com, Inc. or its affiliates.</p>
    <p style="margin-top:0.5rem;">All product fulfillment, shipping, returns and customer service are handled by Amazon. PeakPicks holds no inventory.</p>
  </div>
</footer>

<script>
const AFFILIATE_TAG = "{affiliate_tag}";
const products = {products_json};

function renderProducts(filter = 'all') {{
  const grid = document.getElementById('productGrid');
  const filtered = filter === 'all' ? products : products.filter(p => p.category === filter);
  grid.innerHTML = filtered.map(p => `
    <div class="product-card" data-cat="${{p.category}}">
      <span class="card-badge ${{p.badgeClass}}">${{p.badge === 'bestseller' ? '#1 Bestseller' : p.badge === 'trending' ? '🔥 Trending' : '✦ New Pick'}}</span>
      <div class="card-img-placeholder">${{p.icon}}</div>
      <div class="card-body">
        <div class="card-category">${{p.category}}</div>
        <div class="card-title">${{p.name}}</div>
        <div class="card-desc">${{p.desc}}</div>
        <div class="stars"><span class="stars-icons">★★★★★</span><span class="stars-count">${{p.rating}} (${{p.reviews}} reviews)</span></div>
        <div class="card-footer">
          <div><div class="card-price"><sup>$</sup>${{p.price}}</div><div class="commission">Earns ${{p.commission}}</div></div>
          <a class="btn-amazon" href="https://www.amazon.com/dp/${{p.asin}}?tag=${{AFFILIATE_TAG}}" target="_blank">Buy on Amazon →</a>
        </div>
      </div>
    </div>
  `).join('');
}}

function filterCategory(cat, btn) {{
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  renderProducts(cat);
}}

function calcEarnings() {{
  const visitors = +document.getElementById('visitors').value || 0;
  const rate = +document.getElementById('category').value;
  const aov = +document.getElementById('aov').value || 0;
  const cvr = (+document.getElementById('cvr').value || 0) / 100;
  const orders = Math.round(visitors * cvr);
  const monthly = (orders * aov * rate).toFixed(0);
  const annual = (monthly * 12).toLocaleString();
  document.getElementById('res-monthly').textContent = '$' + Number(monthly).toLocaleString();
  document.getElementById('res-annual').textContent = '$' + annual;
  document.getElementById('res-orders').textContent = orders;
}}

renderProducts();
calcEarnings();
</script>
</body>
</html>"""


if __name__ == "__main__":
    html = generate_html(PRODUCTS, AFFILIATE_TAG, CURRENT_DATE)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ index.html generated successfully on {CURRENT_DATE}")
    print(f"   Products included: {len(PRODUCTS)}")
    print(f"   Affiliate tag: {AFFILIATE_TAG}")
