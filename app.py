import streamlit as st
from PIL import Image
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Beeai Morrison | Strategic Architect", page_icon="🛡️", layout="wide")

# --- 2. CUSTOM THEMING & GLASSMORPHISM CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #FFFFFF;
    }
    [data-testid="stVerticalBlock"] > div:has(div.glass-card) {
        padding: 0;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 35px;
        transition: 0.4s ease;
    }
    .glass-card:hover {
        border: 1px solid #00ccff;
        box-shadow: 0px 0px 20px rgba(0, 204, 255, 0.2);
    }
    .hero-text {
        font-weight: 800;
        background: linear-gradient(90deg, #FFFFFF, #888888);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .process-step {
        color: #00ccff;
        font-weight: bold;
        font-size: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR / PROFILE SECTION ---
with st.sidebar:
    st.markdown("### Digital Identity")
    # This checks if you've uploaded a 'profile.jpg' to your GitHub repo
    if os.path.exists("profile.jpg"):
        st.image("profile.jpg", use_container_width=True, caption="Beeai Morrison")
    else:
        st.info("To show your profile picture, upload a file named 'profile.jpg' to your GitHub repository.")
    
    st.divider()
    st.markdown("**Role:** Strategic Architect")
    st.markdown("**Location:** Lekki, Lagos")
    st.link_button("Email Me", "mailto:your-email@example.com")

# --- 4. HERO SECTION ---
col_h1, col_h2 = st.columns([2, 1])

with col_h1:
    st.markdown('<h1 class="hero-text" style="font-size: 4.5rem; margin-bottom:0;">BEEAI MORRISON</h1>', unsafe_allow_width=True)
    st.markdown('<h3 style="color: #00ccff; margin-top:0;">Technical Rigor & Creative Conversion</h3>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"""
        <p style="font-size: 1.3rem; line-height: 1.6; font-style: italic; color: #bbb;">
            "My approach aligns the rigors of standard academic research with the unique requirements 
            of specific projects. I provide strategic support for M.Sc. and B.Sc. candidates, 
            ensuring that theses, dissertations, and high-level technical assignments meet 
            institutional demands while maintaining the creative edge of the project's vision."
        </p>
    """, unsafe_allow_html=True)

# --- 5. THE THREE CORE PILLARS ---
st.write("##")
p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""<div class="glass-card">
        <h3 style="color: #00ccff;">🎓 Academic Rigor</h3>
        <p>Strategic guidance for high-stakes research. Aligning unique project visions with the strict demands of institutional boards.</p>
    </div>""", unsafe_allow_html=True)

with p2:
    st.markdown("""<div class="glass-card">
        <h3 style="color: #00ccff;">✍️ Direct-Response</h3>
        <p>Engineering communication frameworks and video scripts for health, tech, and lifestyle brands that trigger action.</p>
    </div>""", unsafe_allow_html=True)

with p3:
    st.markdown("""<div class="glass-card">
        <h3 style="color: #00ccff;">📈 Systematic SEO</h3>
        <p>Data-driven visibility. Crafting metadata architecture that ensures visionary content is discovered, ranked, and valued.</p>
    </div>""", unsafe_allow_html=True)

# --- 6. THE METHODOLOGY (CONVENTIONAL STANDARD ADDITION) ---
st.write("##")
st.write("---")
st.header("The Methodology")
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown('<p class="process-step">01. Discovery</p>', unsafe_allow_html=True)
    st.write("Mapping the rigors of your specific academic or brand requirements to establish a solid foundation.")

with m2:
    st.markdown('<p class="process-step">02. Engineering</p>', unsafe_allow_html=True)
    st.write("Building the system—whether a 10,000-word thesis or a Python dashboard—with technical precision.")

with m3:
    st.markdown('<p class="process-step">03. Calibration</p>', unsafe_allow_html=True)
    st.write("Final optimization for institutional defense or global search engine visibility.")

# --- 7. CALL TO ACTION ---
st.write("##")
st.markdown("""
    <div style="text-align: center; padding: 50px; background: rgba(0, 204, 255, 0.1); border-radius: 20px;">
        <h2>Ready to deploy your vision?</h2>
        <p>Let's align your project with global standards of excellence.</p>
    </div>
""", unsafe_allow_html=True)

st.write("##")
c_col1, c_col2, c_col3 = st.columns([1, 2, 1])
with c_col2:
    st.button("SCHEDULE A CONSULTATION", use_container_width=True)

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #444; margin-top: 50px;'>© 2026 Beeai Morrison | Strategic Execution</p>", unsafe_allow_html=True)
