import streamlit as st
import zipfile
import io
import json
import datetime
import re

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="StopWebRent Builder | Titan Engine v30.5", 
    layout="wide", 
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (CSS FOR BUILDER) ---
st.markdown("""
    <style>
    /* UI Reset & Variables */
    :root { --primary: #0f172a; --accent: #ef4444; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    [data-testid="stSidebar"] h1 { 
        background: linear-gradient(90deg, #0f172a, #ef4444);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        font-size: 1.8rem !important;
    }
    
    /* Modern Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        color: #0f172a !important;
    }
    
    /* Action Buttons */
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%);
        color: white; font-weight: 800; border: none;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3);
        text-transform: uppercase; letter-spacing: 1px;
        transition: transform 0.2s;
    }
    .stButton>button:hover { transform: translateY(-2px); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE CONTROL CENTER ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v30.5 | StopWebRent Edition")
    st.divider()
    
    # 3.1 VISUAL DNA
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", [
            "Clean Corporate (Light)", 
            "Midnight SaaS (Dark)", 
            "Stark Minimalist"
        ])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#0F172A") # Navy Blue
        s_color = c2.color_picker("Action (CTA)", "#EF4444")  # Urgent Red/Orange
        
        st.markdown("**Typography**")
        h_font = st.selectbox("Headings", ["Montserrat", "Space Grotesk", "Oswald", "Clash Display"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto"])
        
        st.markdown("**UI Physics**")
        border_rad = st.select_slider("Corner Roundness", ["0px", "4px", "12px", "24px"], value="8px")
        anim_type = st.selectbox("Animation Style", ["Fade Up", "Zoom In", "None"])

    # 3.2 MODULE MANAGER
    with st.expander("🧩 Section Manager", expanded=False):
        st.caption("Toggle sections to include:")
        show_hero = st.checkbox("Hero Section", value=True)
        show_problem = st.checkbox("The 'Rent' Problem", value=True) # NEW
        show_features = st.checkbox("The 4 Pillars", value=True)
        show_pricing = st.checkbox("Pricing Comparison Table", value=True) # NEW
        show_stats = st.checkbox("Trust Stats", value=True)
        show_inventory = st.checkbox("Portfolio / Templates", value=True) # Repurposed Inventory
        show_gallery = st.checkbox("About Section", value=True)
        show_testimonials = st.checkbox("Testimonials", value=False)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_cta = st.checkbox("Final Call to Action", value=True)

    # 3.3 TECHNICAL
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global / Remote")
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID")
        og_image = st.text_input("Social Share Image URL")

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ StopWebRent Site Builder")

tabs = st.tabs(["1. Identity", "2. Sales Copy", "3. Pricing Table", "4. Portfolio", "5. Legal"])

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
        logo_url = st.text_input("Logo URL (PNG/SVG)")
        
    st.subheader("Social Links")
    sc1, sc2 = st.columns(2)
    fb_link = sc1.text_input("Facebook URL")
    x_link = sc2.text_input("X (Twitter) URL")
    wa_num = biz_phone # Sync

with tabs[1]:
    st.subheader("Hero Section")
    hero_h = st.text_input("Hero Headline", "Stop Renting Your Website. Start Owning Your Digital Future.")
    hero_sub = st.text_input("Hero Subtext", "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
    
    hc1, hc2 = st.columns(2)
    # Using a tech/architecture abstract image
    hero_img_1 = hc1.text_input("Hero Image", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    
    st.divider()
    st.subheader("The 'Rent' Problem")
    prob_h = st.text_input("Problem Headline", "Why pay a mortgage on a digital brochure?")
    prob_txt = st.text_area("Problem Text", "Traditional agencies and builders like Wix/Shopify charge you 'rent' every month. If you stop paying, they delete your business. Over 5 years, you lose **$1,700+**. We changed the rules.")

    st.divider()
    st.subheader("The 4 Pillars (Features)")
    f_title = st.text_input("Features Title", "The Titan Value Pillars")
    st.info("Keywords for icons: bolt (speed), wallet (cost), table (sheets), shield (security)")
    feat_data = st.text_area("Features List", 
                             "bolt | The Performance Pillar | **0.1s High-Velocity Loading**. While traditional sites take 3–5s, Titan loads instantly. This satisfies Google’s Core Web Vitals perfectly.\nwallet | The Economic Pillar | **$0 Monthly Fees**. We eliminated hosting subscriptions. You pay once and own the raw source code forever. No 'rent'.\ntable | The Functional Pillar | **Google Sheets CMS**. Update prices and photos directly from a simple spreadsheet. If you can use Excel, you can manage your site.\nshield | The Authority Pillar | **Unhackable Security**. By removing the database (Zero-DB Architecture), we removed the hacker's entry point.",
                             height=200)

    st.subheader("Trust Stats")
    s1, s2, s3 = st.columns(3)
    stat_1 = s1.text_input("Stat 1", "0.1s")
    label_1 = s1.text_input("Label 1", "Load Speed")
    stat_2 = s2.text_input("Stat 2", "$0")
    label_2 = s2.text_input("Label 2", "Monthly Fees")
    stat_3 = s3.text_input("Stat 3", "100%")
    label_3 = s3.text_input("Label 3", "Ownership")

    st.subheader("About / Gallery")
    about_h = st.text_input("About Title", "Control Your Empire from a Spreadsheet")
    about_short = st.text_area("About Summary", "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.", height=150)
    about_img = st.text_input("About Image (Google Sheet Visual)", "https://images.unsplash.com/photo-1543286386-713df548e9cc?q=80&w=1600")

with tabs[2]:
    st.header("💰 The Pricing Engine")
    st.info("This generates the comparison table on the Home Page.")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    titan_price = col_p1.text_input("Titan Setup Fee", "$199")
    titan_mo = col_p1.text_input("Titan Monthly", "$0")
    
    wix_name = col_p2.text_input("Competitor Name", "Wix (Core Plan)")
    wix_mo = col_p2.text_input("Competitor Monthly", "$29/mo")
    
    save_val = col_p3.text_input("5-Year Savings Calculation", "$1,466")
    
    st.caption("The table calculates: Titan (One time) vs Competitor (Monthly x 60 months).")

with tabs[3]:
    st.header("📂 Portfolio & Demos")
    st.info("Re-purposing the Inventory System to show Templates.")
    sheet_url = st.text_input("Google Sheet CSV Link", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Template Image", "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=800")
    st.caption("CSV Columns: TemplateName, Category, Description, ImageURL")

with tabs[4]:
    st.subheader("Trust & Legal")
    faq_data = st.text_area("FAQ Data (Q? ? A)", "Do I really pay $0 for hosting? ? Yes. We use static architecture that fits within the free tiers of enterprise CDNs (Netlify/Vercel).\nWhat about my Domain Name? ? You pay ~$15/year directly to the registrar (Namecheap). We don't mark this up.\nCan I add a blog later? ? Yes, the Titan Engine is scalable.", height=150)
    
    l1, l2 = st.columns(2)
    priv_txt = l1.text_area("Privacy Policy", "**1. Digital Sovereignty**\nAt StopWebRent, we treat data privacy as a fundamental requirement.", height=150)
    term_txt = l2.text_area("Terms of Service", "**1. Service Agreement**\nUpon final payment, full IP rights and source code ownership are transferred to the client.", height=150)

# --- 5. COMPILER ENGINE ---

def format_text(text):
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    return processed_text.replace('\n', '<br>')

def gen_schema():
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": biz_name,
        "image": logo_url or hero_img_1,
        "telephone": biz_phone,
        "url": prod_url,
        "description": seo_d
    }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

def get_theme_css():
    # Base Defaults
    bg_color = "#ffffff"
    text_color = "#0f172a"
    card_bg = "#f8fafc"
    glass_nav = "rgba(255, 255, 255, 0.95)"
    
    if "Midnight" in theme_mode:
        bg_color, text_color, card_bg, glass_nav = "#0f172a", "#f8fafc", "#1e293b", "rgba(15, 23, 42, 0.95)"
    elif "Stark" in theme_mode:
        bg_color, text_color, card_bg, glass_nav = "#ffffff", "#000000", "#ffffff", "rgba(255,255,255,1)"

    anim_css = ""
    if anim_type == "Fade Up":
        anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; } .reveal.active { opacity: 1; transform: translateY(0); }"
    elif anim_type == "Zoom In":
        anim_css = ".reveal { opacity: 0; transform: scale(0.95); transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); } .reveal.active { opacity: 1; transform: scale(1); }"
    
    return f"""
    :root {{
        --p: {p_color}; --s: {s_color}; --bg: {bg_color}; --txt: {text_color}; --card: {card_bg};
        --radius: {border_rad}; --nav: {glass_nav};
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    
    p, h1, h2, h3, h4, h5, h6 {{ color: inherit; }}
    h1, h2, h3 {{ font-family: var(--h-font); color: var(--p); line-height: 1.1; margin-bottom: 1rem; }}
    strong {{ color: var(--p); font-weight: 800; }}
    
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 20px; }}
    .btn {{ display: inline-block; padding: 1rem 2.5rem; border-radius: var(--radius); font-weight: 700; text-decoration: none; transition: 0.3s; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; border: none; text-align: center; }}
    .btn-primary {{ background: var(--p); color: white !important; }}
    .btn-accent {{ background: var(--s); color: white !important; box-shadow: 0 10px 25px -5px var(--s); }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.15); }}
    
    /* Nav */
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(100,100,100,0.1); padding: 1rem 0; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links a {{ margin-left: 2rem; text-decoration: none; font-weight: 600; color: var(--txt); opacity: 0.8; transition:0.2s; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    
    /* Hero */
    .hero {{ position: relative; padding: 8rem 0 5rem; text-align: center; background: linear-gradient(to bottom, var(--bg), var(--card)); }}
    .hero h1 {{ font-size: clamp(2.5rem, 6vw, 4.5rem); margin-bottom: 1.5rem; max-width: 900px; margin-left: auto; margin-right: auto; }}
    .hero p {{ font-size: clamp(1.1rem, 2vw, 1.4rem); max-width: 700px; margin: 0 auto 2.5rem auto; opacity: 0.9; }}
    
    section {{ padding: 5rem 0; }}
    .section-head {{ text-align: center; margin-bottom: 4rem; }}
    .section-head h2 {{ font-size: 2.5rem; }}
    
    /* Grid & Cards */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .card {{ background: var(--card); padding: 2rem; border-radius: var(--radius); border: 1px solid rgba(100,100,100,0.1); transition: 0.3s; height: 100%; }}
    .card:hover {{ transform: translateY(-5px); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.05); border-color: var(--s); }}
    
    /* PRICING TABLE CSS (NEW) */
    .pricing-wrapper {{ overflow-x: auto; margin: 2rem 0; }}
    .pricing-table {{ width: 100%; border-collapse: collapse; min-width: 600px; }}
    .pricing-table th {{ background: var(--p); color: white; padding: 1.5rem; text-align: left; font-size: 1.1rem; }}
    .pricing-table td {{ padding: 1.5rem; border-bottom: 1px solid rgba(100,100,100,0.1); background: var(--card); color: var(--txt); }}
    .pricing-table tr:last-child td {{ font-weight: bold; font-size: 1.2rem; background: rgba(var(--s), 0.1); border-bottom: none; }}
    
    /* FAQ Styling */
    details {{ background: var(--card); border: 1px solid rgba(100,100,100,0.1); border-radius: 8px; margin-bottom: 1rem; padding: 1rem; cursor: pointer; }}
    details summary {{ font-weight: bold; font-size: 1.1rem; }}
    
    /* Footer */
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    
    /* Social Icons */
    .social-icon {{ width: 24px; height: 24px; fill: rgba(255,255,255,0.7); transition: 0.3s; }}
    .social-icon:hover {{ fill: #ffffff; transform: scale(1.1); }}

    /* Share Buttons */
    .share-btn {{ width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: none; cursor: pointer; color: white; margin-right: 0.5rem; }}
    .share-wa {{ background: #25D366; }} .share-fb {{ background: #1877F2; }} .share-x {{ background: #000000; }}
    
    .prod-img {{ width: 100%; height: 220px; object-fit: cover; border-radius: var(--radius); margin-bottom: 1rem; }}
    
    @media (max-width: 768px) {{
        .nav-links {{ display: none; position: absolute; top: 100%; left: 0; width: 100%; background: var(--bg); padding: 1rem; flex-direction: column; }}
        .nav-links.active {{ display: flex; }}
        .nav-links a {{ margin: 0.5rem 0; }}
        .mobile-menu {{ display: block; }}
        .about-grid {{ grid-template-columns: 1fr !important; }}
    }}
    {anim_css}
    """

def gen_nav():
    logo_display = f'<img src="{logo_url}" height="40" alt="{biz_name} Logo">' if logo_url else f'<span style="font-weight:900; font-size:1.5rem; color:var(--p)">{biz_name}</span>'
    return f"""
    <nav><div class="container nav-flex">
        <a href="index.html" style="text-decoration:none">{logo_display}</a>
        <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="index.html#features">Why Us</a>
            <a href="index.html#pricing">Savings</a>
            <a href="index.html#portfolio">Portfolio</a>
            <a href="contact.html">Contact</a>
            <a href="https://wa.me/{wa_num}" class="btn-accent" style="padding:0.6rem 1.5rem; margin-left:1.5rem; color:white !important; border-radius:50px;">WhatsApp</a>
        </div>
    </div></nav>
    """

def get_simple_icon(name):
    name = name.lower().strip()
    # STOPWEBRENT ICONS
    if "bolt" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"/></svg>'
    if "wallet" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>'
    if "table" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM5 19V5h14v14H5zm2-2h10v-2H7v2zm0-4h10v-2H7v2zm0-4h10V7H7v2z"/></svg>'
    if "shield" in name: return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>'
    
    # FALLBACK
    return '<svg viewBox="0 0 24 24" width="40" height="40" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'

def gen_hero():
    return f"""
    <section class="hero">
        <div class="container hero-content">
            <h1 class="reveal">{hero_h}</h1>
            <p class="reveal">{hero_sub}</p>
            <div class="reveal" style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
                <a href="#pricing" class="btn btn-accent">Calculate Savings</a>
                <a href="contact.html" class="btn" style="background:transparent; color:var(--p); border:2px solid var(--p);">Get Free Audit</a>
            </div>
            <img src="{hero_img_1}" class="reveal" style="width:100%; max-width:1000px; margin-top:4rem; border-radius:var(--radius); box-shadow:0 20px 50px -10px rgba(0,0,0,0.15);">
        </div>
    </section>
    """

def gen_features():
    cards = ""
    lines = [x for x in feat_data.split('\n') if x.strip()]
    for line in lines:
        if "|" in line:
            parts = line.split('|')
            icon_code = get_simple_icon(parts[0])
            cards += f"""<div class="card reveal"><div style="color:var(--s); margin-bottom:1rem;">{icon_code}</div><h3 style="font-size:1.2rem;">{parts[1].strip()}</h3><div style="opacity:0.9; font-size:0.95rem;">{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2>{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_pricing_table():
    if not show_pricing: return ""
    return f"""
    <section id="pricing"><div class="container">
        <div class="section-head reveal"><h2>The Cost of Ownership</h2><p>See how the "Monthly Trap" adds up over 5 years.</p></div>
        <div class="pricing-wrapper reveal">
            <table class="pricing-table">
                <thead>
                    <tr><th style="width:40%">Expense Category</th><th style="background:var(--s); font-size:1.2rem;">Titan Engine (Us)</th><th>{wix_name}</th><th>Standard Agency</th></tr>
                </thead>
                <tbody>
                    <tr><td>Initial Setup Fee</td><td><strong>{titan_price}</strong> (One-time)</td><td>$0 (DIY)</td><td>$2,000+</td></tr>
                    <tr><td>Annual Hosting Costs</td><td><strong>{titan_mo}</strong></td><td>{wix_mo} ($348/yr)</td><td>$600/yr</td></tr>
                    <tr><td>SSL & Security</td><td>$0 (Included)</td><td>$0 (Included)</td><td>$100/yr</td></tr>
                    <tr><td><strong>Your 5-Year Savings</strong></td><td style="color:var(--s); font-size:1.3rem;">You Save {save_val}</td><td>$0</td><td>$0</td></tr>
                </tbody>
            </table>
        </div>
        <p style="text-align:center; font-size:0.8rem; opacity:0.6; margin-top:1rem;">*Comparison pricing based on standard public rates. Titan Engine is not affiliated with competitor trademarks.</p>
    </div></section>
    """

def gen_about_section():
    return f"""
    <section id="about"><div class="container">
        <div style="display:grid; grid-template-columns:1fr 1fr; gap:4rem; align-items:center;" class="about-grid">
            <div class="reveal">
                <h2>{about_h}</h2>
                <div style="font-size:1.1rem; opacity:0.9; margin-bottom:2rem;">{format_text(about_short)}</div>
                <a href="about.html" class="btn btn-primary">How It Works</a>
            </div>
            <img src="{about_img}" class="reveal" loading="lazy" style="width:100%; border-radius:var(--radius); box-shadow:0 20px 50px -20px rgba(0,0,0,0.2);">
        </div>
    </div></section>
    """

def gen_csv_parser():
    return """<script>function parseCSVLine(str){const res=[];let cur='';let inQuote=false;for(let i=0;i<str.length;i++){const c=str[i];if(c==='"'){if(inQuote&&str[i+1]==='"'){cur+='"';i++;}else{inQuote=!inQuote;}}else if(c===','&&!inQuote){res.push(cur.trim());cur='';}else{cur+=c;}}res.push(cur.trim());return res;}</script>"""

def gen_portfolio_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    {gen_csv_parser()}
    <script>
    {demo_flag}
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}');
            const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/);
            const box = document.getElementById('inv-grid');
            if(!box) return;
            box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                if(!lines[i].trim()) continue;
                const clean = parseCSVLine(lines[i]);
                let img = clean[3] && clean[3].length > 5 ? clean[3] : '{custom_feat}'; 
                if(clean.length > 1) {{
                    const prodName = encodeURIComponent(clean[0]);
                    box.innerHTML += `
                    <div class="card reveal">
                        <img src="${{img}}" class="prod-img" loading="lazy" onerror="this.onerror=null;this.src='{custom_feat}';">
                        <h3 style="font-size:1.2rem; margin-bottom:0.5rem;">${{clean[0]}}</h3>
                        <p style="font-size:0.9rem; opacity:0.8; margin-bottom:1rem;">${{clean[1]}}</p>
                        <div style="display:flex; gap:0.5rem;">
                            <a href="product.html?item=${{prodName}}" class="btn" style="background:#e2e8f0; color:#0f172a !important; padding:0.6rem; font-size:0.8rem; flex-grow:1; text-align:center;">View Demo</a>
                        </div>
                    </div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>
    """

def gen_portfolio():
    if not show_inventory: return ""
    return f"""<section id="portfolio" style="background:var(--card)"><div class="container"><div class="section-head reveal"><h2>Our Template Portfolio</h2><p>Choose a foundation. We customize it for you.</p></div><div id="inv-grid" class="grid-3"><div style="grid-column:1/-1; text-align:center; padding:4rem; color:var(--s);">Loading Designs...</div></div></div></section>{gen_portfolio_js(False)}"""

def gen_stats():
    if not show_stats: return ""
    return f"""<div style="background:var(--p); color:white; padding:4rem 0; text-align:center;"><div class="container grid-3"><div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3.5rem;">{stat_1}</h3><p>{label_1}</p></div><div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3.5rem;">{stat_2}</h3><p>{label_2}</p></div><div class="reveal"><h3 style="color:#ffffff; margin:0; font-size:3.5rem;">{stat_3}</h3><p>{label_3}</p></div></div></div>"""

def gen_problem():
    if not show_problem: return ""
    return f"""<section style="background:var(--card); text-align:center;"><div class="container" style="max-width:800px;"><h2 class="reveal" style="font-size:2.5rem; margin-bottom:1.5rem;">{prob_h}</h2><div class="reveal" style="font-size:1.2rem; opacity:0.9;">{format_text(prob_txt)}</div></div></section>"""

def gen_faq():
    items = ""
    for line in faq_data.split('\n'):
        if "?" in line:
            parts = line.split('?', 1)
            items += f"<details class='reveal'><summary>{parts[0]}?</summary><p>{parts[1]}</p></details>"
    return f"""<section id="faq"><div class="container" style="max-width:800px;"><div class="section-head reveal"><h2>Common Questions</h2></div>{items}</div></section>"""

def gen_footer():
    return f"""<footer><div class="container"><div class="footer-grid"><div><h3>{biz_name}</h3><p>{biz_addr}</p><p>{biz_email}</p></div><div><h4>Links</h4><a href="index.html">Home</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy</a></div></div><div style="margin-top:3rem; padding-top:2rem; border-top:1px solid rgba(255,255,255,0.1); opacity:0.6; font-size:0.8rem;">&copy; {biz_name}. Powered by Titan Engine.</div></div></footer>"""

def gen_wa_widget():
    if not wa_num: return ""
    return f"""<a href="https://wa.me/{wa_num}" target="_blank" style="position:fixed; bottom:30px; right:30px; background:#25d366; color:white; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(37,211,102,0.4); z-index:9999;"><svg style="width:32px;height:32px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></a>"""

def gen_scripts():
    return """<script>window.addEventListener('scroll',()=>{var r=document.querySelectorAll('.reveal');for(var i=0;i<r.length;i++){if(r[i].getBoundingClientRect().top<window.innerHeight-150){r[i].classList.add('active');}}});window.dispatchEvent(new Event('scroll'));</script>"""

# --- PAGE BUILDERS ---

def build_page(title, content, extra_js=""):
    css = get_theme_css()
    meta = f'<meta name="description" content="{seo_d}">'
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title>{meta}{gen_schema()}<link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ','+')}:wght@400;700;900&family={b_font.replace(' ','+')}:wght@300;400;600&display=swap" rel="stylesheet"><style>{css}</style></head><body>{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}{gen_scripts()}{extra_js}</body></html>"""

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""
    <section style="padding-top:150px;"><div class="container"><div id="product-detail" style="display:grid; grid-template-columns:1fr 1fr; gap:3rem;">
        <div style="background:#eee; height:400px; border-radius:12px;"></div><div>Loading...</div>
    </div></div></section>
    {gen_csv_parser()}
    <script>
    {demo_flag}
    // Simple Share Script
    function shareWA(url, title) {{ window.open('https://wa.me/?text=' + encodeURIComponent(title + ' ' + url), '_blank'); }}
    async function loadProduct() {{
        const params = new URLSearchParams(window.location.search);
        let targetName = params.get('item');
        if(isDemo && !targetName) targetName = "Demo Item"; // Fallback for preview
        
        try {{
            const res = await fetch('{sheet_url}');
            const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/);
            for(let i=1; i<lines.length; i++) {{
                const clean = parseCSVLine(lines[i]);
                if (isDemo) {{ targetName = clean[0]; }} // Force first item
                if(clean[0] === targetName) {{
                    let img = clean[3] || '{custom_feat}';
                    document.getElementById('product-detail').innerHTML = `
                        <img src="${{img}}" style="width:100%; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1);">
                        <div>
                            <h1 style="font-size:3rem; line-height:1.1;">${{clean[0]}}</h1>
                            <p style="font-size:1.5rem; color:var(--s); font-weight:bold; margin-bottom:1.5rem;">${{clean[1]}}</p>
                            <div style="opacity:0.8; margin-bottom:2rem;">${{clean[2]}}</div>
                            <button onclick="shareWA(window.location.href, '${{clean[0]}}')" class="btn btn-primary" style="width:100%">Get This Template</button>
                        </div>
                    `;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadProduct();
    </script>
    """

# --- 6. PAGE CONTENT ASSEMBLY ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_problem: home_content += gen_problem()
if show_features: home_content += gen_features()
if show_pricing: home_content += gen_pricing_table() # THE NEW FEATURE
if show_gallery: home_content += gen_about_section()
if show_inventory: home_content += gen_portfolio()
if show_faq: home_content += gen_faq()
if show_cta: home_content += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2>Start Owning Your Future</h2><p style="margin-bottom:2rem;">Stop paying rent. Start building equity.</p><a href="contact.html" class="btn" style="background:white; color:var(--s);">Get Started</a></div></section>'

# Inner Pages
about_content = f"""<section class="hero" style="min-height:40vh;"><div class="container"><h1>About Us</h1></div></section><section><div class="container">{format_text(about_short)}</div></section>"""
contact_content = f"""<section class="hero" style="min-height:40vh;"><div class="container"><h1>Contact</h1></div></section><section><div class="container"><div class="card"><h3>Send Message</h3><p>{biz_email}</p><br><a href="https://wa.me/{wa_num}" class="btn btn-accent">WhatsApp Us</a></div></div></section>"""
priv_content = f"""<section class="hero" style="min-height:40vh;"><div class="container"><h1>Privacy Policy</h1></div></section><section><div class="container">{format_text(priv_txt)}</div></section>"""

# --- 7. RENDER & DEPLOY ---
st.divider()
c1, c2 = st.columns([3, 1])

with c1:
    st.subheader("Live Preview")
    st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)

with c2:
    st.success("StopWebRent Engine Ready")
    if st.button("DOWNLOAD WEBSITE ZIP", type="primary"):
        z_b = io.BytesIO()
        with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", build_page("Home", home_content))
            zf.writestr("about.html", build_page("About", about_content))
            zf.writestr("contact.html", build_page("Contact", contact_content))
            zf.writestr("privacy.html", build_page("Privacy", priv_content))
            zf.writestr("product.html", build_page("Template Details", gen_product_page_content(False)))
            zf.writestr("robots.txt", "User-agent: *\nAllow: /")
        st.download_button("📥 Click to Save", z_b.getvalue(), "stopwebrent_site.zip", "application/zip")
