import streamlit as st
import zipfile
import io
import json
import re

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="StopWebRent Builder | Titan Engine", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (CSS FOR BUILDER) ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white; font-weight: 800; border: none;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3);
        text-transform: uppercase; letter-spacing: 1px;
    }
    .stButton>button:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE CONTROL CENTER ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("Configuration: StopWebRent.com")
    st.divider()
    
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Clean Corporate (Light)", "Midnight SaaS (Dark)"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary (Trust)", "#0F172A") 
        s_color = c2.color_picker("Action (Urgency)", "#2563EB")  
        
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Oswald"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto"])
        border_rad = st.select_slider("Corner Roundness", ["0px", "4px", "12px", "24px"], value="12px")

    with st.expander("🧩 Section Manager", expanded=False):
        show_hero = st.checkbox("Hero Section", value=True)
        show_problem = st.checkbox("The 'Rent' Problem", value=True) # New
        show_stats = st.checkbox("Trust Stats", value=True)
        show_features = st.checkbox("The 4 Pillars", value=True)
        show_pricing = st.checkbox("Pricing Comparison Table", value=True) # New
        show_demo = st.checkbox("Template Portfolio", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_cta = st.checkbox("Final Call to Action", value=True)

    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global / Remote")
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID")

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ StopWebRent Site Builder")

tabs = st.tabs(["1. Identity", "2. Sales Copy", "3. Pricing & Data", "4. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent.com")
        biz_tagline = st.text_input("Tagline", "Stop Renting. Start Owning.")
        biz_phone = st.text_input("WhatsApp (No +)", "966572562151")
        biz_email = st.text_input("Email", "hello@stopwebrent.com")
    with c2:
        prod_url = st.text_input("Website URL", "https://stopwebrent.com")
        biz_addr = st.text_area("Address", "Titan HQ, Kolkata, West Bengal, India", height=100)
        seo_d = st.text_area("Meta Description", "The Titan Engine is 10x faster and $0 monthly fees. Stop renting your website from Wix or Shopify. Pay once, own it forever.", height=100)
        logo_url = st.text_input("Logo URL (Optional)")

with tabs[1]:
    st.subheader("Hero Section")
    hero_h = st.text_input("Hero Headline", "Stop Renting Your Website. Start Owning Your Digital Future.")
    hero_sub = st.text_input("Hero Subtext", "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
    
    hc1, hc2 = st.columns(2)
    hero_img_1 = hc1.text_input("Hero Image", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    
    st.divider()
    st.subheader("The 'Problem' Section")
    prob_h = st.text_input("Problem Headline", "Why pay a mortgage on a digital brochure?")
    prob_txt = st.text_area("Problem Text", "Traditional agencies and builders like Wix/Shopify charge you 'rent' every month. If you stop paying, they delete your business. Over 5 years, you lose $1,700+. We changed the rules.")

    st.divider()
    st.subheader("The 4 Pillars (Features)")
    f_title = st.text_input("Features Title", "The Titan Value Pillars")
    # Pre-filled with the exact copy from your prompt
    feat_data = st.text_area("Features List (icon | title | desc)", 
                             "bolt | The Performance Pillar | 0.1s High-Velocity Loading. While traditional sites take 3–5s, Titan loads instantly. This satisfies Google’s Core Web Vitals perfectly.\nwallet | The Economic Pillar | $0 Monthly Fees. We eliminated hosting subscriptions. You pay once and own the raw source code forever. No 'rent'.\ntable | The Functional Pillar | Google Sheets CMS. Update prices and photos directly from a simple spreadsheet. If you can use Excel, you can manage your site.\nshield | The Authority Pillar | Unhackable Security. By removing the database (Zero-DB Architecture), we removed the hacker's entry point.",
                             height=200)

    st.subheader("Trust Stats")
    s1, s2, s3 = st.columns(3)
    stat_1 = s1.text_input("Stat 1", "0.1s")
    label_1 = s1.text_input("Label 1", "Load Speed")
    stat_2 = s2.text_input("Stat 2", "$0")
    label_2 = s2.text_input("Label 2", "Monthly Fees")
    stat_3 = s3.text_input("Stat 3", "100%")
    label_3 = s3.text_input("Label 3", "Ownership")

with tabs[2]:
    st.subheader("Pricing Table Configuration")
    st.info("Edit the specific values for the comparison table.")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    titan_price = col_p1.text_input("Titan Price", "$199")
    titan_mo = col_p1.text_input("Titan Monthly", "$0")
    
    wix_price = col_p2.text_input("Competitor Name", "Wix / Shopify")
    wix_mo = col_p2.text_input("Competitor Monthly", "$29/mo")
    
    save_val = col_p3.text_input("5-Year Savings", "$1,466")
    
    st.divider()
    st.subheader("Portfolio / Demo Data")
    st.caption("Use this to show 'The Tradesman', 'The Lawyer' etc.")
    sheet_url = st.text_input("Google Sheet CSV (for Demos)", "")
    st.info("If left blank, a placeholder portfolio will be generated.")

with tabs[3]:
    st.subheader("Legal & FAQ")
    faq_data = st.text_area("FAQ (Q? ? A)", "Do I really pay $0 hosting? ? Yes. We use static architecture that fits within free tiers of enterprise CDNs.\nWhat about my Domain? ? You pay ~$15/year directly to the registrar. We don't mark this up.\nCan I add a blog? ? Yes, the Titan Engine is scalable.", height=150)
    term_txt = st.text_area("Terms", "Titan Engine grants you a perpetual, non-exclusive license to the code upon payment.", height=100)

# --- 5. COMPILER ENGINE ---

def format_text(text):
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return processed_text.replace('\n', '<br>')

def get_theme_css():
    bg_color = "#ffffff" if "Light" in theme_mode else "#0f172a"
    text_color = "#0f172a" if "Light" in theme_mode else "#f8fafc"
    card_bg = "#f8fafc" if "Light" in theme_mode else "#1e293b"
    
    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg_color}; --txt: {text_color}; --card: {card_bg}; --radius: {border_rad}; }}
    * {{ box-sizing: border-box; }}
    body {{ background: var(--bg); color: var(--txt); font-family: '{b_font}', sans-serif; margin: 0; line-height: 1.6; }}
    h1, h2, h3 {{ font-family: '{h_font}', sans-serif; color: var(--p); line-height: 1.1; }}
    .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
    .btn {{ display: inline-block; padding: 1rem 2rem; border-radius: var(--radius); font-weight: 700; text-decoration: none; background: var(--s); color: white; transition: 0.3s; }}
    .btn:hover {{ transform: translateY(-2px); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }}
    
    /* Hero */
    .hero {{ padding: 8rem 0 4rem; text-align: center; background: linear-gradient(to bottom, var(--bg), var(--card)); }}
    .hero h1 {{ font-size: clamp(2.5rem, 5vw, 4rem); max-width: 900px; margin: 0 auto 1.5rem; }}
    .hero p {{ font-size: 1.25rem; opacity: 0.9; max-width: 700px; margin: 0 auto 2.5rem; }}
    
    /* Cards */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .card {{ background: var(--card); padding: 2rem; border-radius: var(--radius); border: 1px solid rgba(128,128,128,0.1); }}
    
    /* Pricing Table */
    .pricing-wrapper {{ overflow-x: auto; margin: 3rem 0; }}
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; text-align: left; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(128,128,128,0.1); background: var(--card); color: var(--txt); }}
    .pricing-table tr:last-child td {{ font-weight: bold; font-size: 1.1rem; background: rgba(37, 99, 235, 0.1); border-bottom: none; }}
    
    /* Nav */
    nav {{ padding: 1.5rem 0; background: var(--bg); position: sticky; top: 0; z-index: 100; border-bottom: 1px solid rgba(128,128,128,0.1); }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    
    /* Footer */
    footer {{ background: var(--p); color: white; padding: 4rem 0; text-align: center; margin-top: 4rem; }}
    footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; }}
    """

def gen_icon(name):
    name = name.lower().strip()
    if "bolt" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"/></svg>'
    if "wallet" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>'
    if "table" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM5 19V5h14v14H5zm2-2h10v-2H7v2zm0-4h10v-2H7v2zm0-4h10V7H7v2z"/></svg>'
    return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'

def gen_pricing_table():
    if not show_pricing: return ""
    return f"""
    <section id="pricing"><div class="container">
        <div style="text-align:center; margin-bottom:3rem;">
            <h2>The Cost of Ownership</h2>
            <p>See how the "Monthly Trap" adds up over 5 years.</p>
        </div>
        <div class="pricing-wrapper">
            <table class="pricing-table">
                <thead>
                    <tr>
                        <th style="width:40%">Expense Category</th>
                        <th style="background:var(--s); font-size:1.1rem;">Titan Engine</th>
                        <th>{wix_price}</th>
                        <th>Standard Agency</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Initial Setup Fee</td>
                        <td><strong>{titan_price}</strong> (One-time)</td>
                        <td>$0 (DIY)</td>
                        <td>$2,000+</td>
                    </tr>
                    <tr>
                        <td>Annual Hosting Costs</td>
                        <td><strong>{titan_mo}</strong></td>
                        <td>{wix_mo} ($348/yr)</td>
                        <td>$600/yr</td>
                    </tr>
                    <tr>
                        <td>SSL & Security</td>
                        <td>$0 (Included)</td>
                        <td>$0 (Included)</td>
                        <td>$100/yr</td>
                    </tr>
                    <tr>
                        <td><strong>Your 5-Year Savings</strong></td>
                        <td style="color:var(--s); font-size:1.2rem;">You Save {save_val}</td>
                        <td>$0</td>
                        <td>$0</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p style="text-align:center; font-size:0.8rem; opacity:0.6; margin-top:1rem;">
            *Comparison pricing based on standard public rates. Titan Engine is not affiliated with Wix or Shopify trademarks.
        </p>
    </div></section>
    """

def gen_content():
    # HERO
    hero = f"""
    <section class="hero"><div class="container">
        <h1>{hero_h}</h1>
        <p>{hero_sub}</p>
        <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
            <a href="#pricing" class="btn">Calculate Savings</a>
            <a href="https://wa.me/{biz_phone}" class="btn" style="background:transparent; color:var(--p); border:2px solid var(--p);">WhatsApp Audit</a>
        </div>
        <img src="{hero_img_1}" style="width:100%; max-width:1000px; margin-top:3rem; border-radius:12px; box-shadow:0 20px 50px -10px rgba(0,0,0,0.2);">
    </div></section>
    """ if show_hero else ""

    # PROBLEM
    problem = f"""
    <section style="padding:5rem 0; background:var(--card);"><div class="container" style="text-align:center; max-width:800px;">
        <h2 style="font-size:2.5rem; margin-bottom:1.5rem;">{prob_h}</h2>
        <p style="font-size:1.1rem; opacity:0.9;">{prob_txt}</p>
    </div></section>
    """ if show_problem else ""

    # PILLARS (FEATURES)
    feats = ""
    lines = [x for x in feat_data.split('\n') if x.strip()]
    for line in lines:
        parts = line.split('|')
        if len(parts) >= 3:
            icon = gen_icon(parts[0])
            feats += f"""<div class="card"><div style="color:var(--s); margin-bottom:1rem;">{icon}</div><h3>{parts[1].strip()}</h3><p>{parts[2].strip()}</p></div>"""
    feature_sec = f"""<section style="padding:5rem 0;"><div class="container"><h2 style="text-align:center; margin-bottom:3rem;">{f_title}</h2><div class="grid-3">{feats}</div></div></section>""" if show_features else ""

    # STATS
    stats = f"""
    <div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3">
        <div><h3 style="color:white; font-size:3rem; margin:0;">{stat_1}</h3><p>{label_1}</p></div>
        <div><h3 style="color:white; font-size:3rem; margin:0;">{stat_2}</h3><p>{label_2}</p></div>
        <div><h3 style="color:white; font-size:3rem; margin:0;">{stat_3}</h3><p>{label_3}</p></div>
    </div></div>
    """ if show_stats else ""

    # PRICING
    pricing = gen_pricing_table()

    # FAQ
    faq_items = ""
    for line in faq_data.split('\n'):
        if "?" in line:
            q, a = line.split('?', 1)
            faq_items += f"<details style='background:var(--card); padding:1rem; margin-bottom:1rem; border-radius:8px;'><summary style='font-weight:bold; cursor:pointer;'>{q}?</summary><p style='margin-top:1rem;'>{a.strip()}</p></details>"
    faq = f"""<section style="padding:5rem 0;"><div class="container" style="max-width:800px;"><h2 style="text-align:center; margin-bottom:3rem;">Common Questions</h2>{faq_items}</div></section>""" if show_faq else ""

    return hero + stats + problem + feature_sec + pricing + faq

def build_html():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{biz_name}</title>
        <meta name="description" content="{seo_d}">
        <link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ','+')}:wght@700&family={b_font.replace(' ','+')}:wght@400;600&display=swap" rel="stylesheet">
        <style>{get_theme_css()}</style>
    </head>
    <body>
        <nav><div class="container nav-flex">
            <div style="font-weight:900; font-size:1.5rem; color:var(--p)">{biz_name}</div>
            <div>
                <a href="#pricing" style="margin-right:1.5rem; color:var(--txt); text-decoration:none;">Pricing</a>
                <a href="https://wa.me/{biz_phone}" class="btn">Chat Now</a>
            </div>
        </div></nav>
        
        {gen_content()}
        
        <footer><div class="container">
            <h3>{biz_name}</h3>
            <p>{biz_addr}</p>
            <p style="opacity:0.6; font-size:0.9rem;">&copy; {biz_name}. All rights reserved. <br>{term_txt}</p>
        </div></footer>
    </body>
    </html>
    """

# --- 6. PREVIEW & DOWNLOAD ---
c_prev, c_down = st.columns([3, 1])

with c_prev:
    st.subheader("Live Preview")
    html_code = build_html()
    st.components.v1.html(html_code, height=600, scrolling=True)

with c_down:
    st.success("Configuration Ready")
    if st.button("DOWNLOAD WEBSITE ZIP", type="primary"):
        z_b = io.BytesIO()
        with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", html_code)
            zf.writestr("robots.txt", "User-agent: *\nAllow: /")
        st.download_button("📥 Click to Save", z_b.getvalue(), "stopwebrent_site.zip", "application/zip")
