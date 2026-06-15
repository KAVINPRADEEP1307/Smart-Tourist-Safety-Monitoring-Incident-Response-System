import streamlit as st

st.set_page_config(
    page_title="SafeTrail – Tourist Safety System",
    page_icon="🛡️",
    layout="wide"
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1e;
    color: #e2e8f0;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem; max-width: 1200px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b3e 0%, #0a0f1e 100%);
    border-right: 1px solid #1e2d50;
}
[data-testid="stSidebar"] * { color: #94a3b8 !important; }
[data-testid="stSidebar"] .stSelectbox label { color: #64748b !important; font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; }

/* Sidebar brand */
.sidebar-brand {
    text-align: center;
    padding: 2rem 1rem 1.5rem;
    border-bottom: 1px solid #1e2d50;
    margin-bottom: 1.5rem;
}
.sidebar-brand h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 700;
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0.5rem 0 0.2rem;
}
.sidebar-brand p { font-size: 11px; color: #475569 !important; margin: 0; }

/* ── Cards ── */
.card {
    background: linear-gradient(135deg, #111827 0%, #0f172a 100%);
    border: 1px solid #1e2d50;
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: border-color .2s;
}
.card:hover { border-color: #38bdf8; }

/* ── Page title ── */
.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 32px;
    font-weight: 700;
    background: linear-gradient(135deg, #f0f9ff 0%, #bae6fd 60%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.25rem;
}
.page-subtitle { font-size: 14px; color: #475569; margin-bottom: 2rem; }

/* ── Metric tiles ── */
.metric-tile {
    background: linear-gradient(135deg, #111827, #0f172a);
    border: 1px solid #1e2d50;
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    position: relative;
    overflow: hidden;
}
.metric-tile::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
}
.metric-tile.blue::before  { background: linear-gradient(90deg, #38bdf8, #818cf8); }
.metric-tile.green::before { background: linear-gradient(90deg, #34d399, #059669); }
.metric-tile.amber::before { background: linear-gradient(90deg, #fbbf24, #f59e0b); }
.metric-tile.red::before   { background: linear-gradient(90deg, #f87171, #ef4444); }
.metric-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: #475569; margin-bottom: 0.4rem; }
.metric-value { font-family: 'Space Grotesk', sans-serif; font-size: 36px; font-weight: 700; color: #f1f5f9; }
.metric-sub   { font-size: 12px; color: #64748b; margin-top: 0.25rem; }

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #0ea5e9, #6366f1) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.8rem !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    letter-spacing: 0.3px !important;
    transition: opacity .2s, transform .1s !important;
    box-shadow: 0 4px 15px rgba(14,165,233,.25) !important;
}
.stButton > button:hover { opacity: .85 !important; transform: translateY(-1px) !important; }

/* SOS button override */
.sos-btn .stButton > button {
    background: linear-gradient(135deg, #ef4444, #b91c1c) !important;
    font-size: 20px !important;
    padding: 1rem 3rem !important;
    border-radius: 50px !important;
    box-shadow: 0 0 30px rgba(239,68,68,.4) !important;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%,100% { box-shadow: 0 0 30px rgba(239,68,68,.4); }
    50%      { box-shadow: 0 0 50px rgba(239,68,68,.7); }
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #0f172a !important;
    border: 1px solid #1e2d50 !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    padding: 0.7rem 1rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 0 3px rgba(56,189,248,.15) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label, .stSlider label {
    color: #94a3b8 !important; font-size: 13px !important; font-weight: 500 !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: #0f172a !important;
    border: 1px solid #1e2d50 !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
}

/* ── Slider ── */
.stSlider > div { padding: 0 !important; }

/* ── Alerts ── */
.stAlert { border-radius: 12px !important; border-left-width: 4px !important; }

/* ── Table ── */
.stDataFrame, .stTable { background: #0f172a !important; border-radius: 12px !important; }

/* ── Login hero ── */
.login-hero {
    text-align: center;
    padding: 3rem 1rem 2rem;
}
.login-hero .shield { font-size: 64px; margin-bottom: 1rem; }
.login-hero h2 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px; font-weight: 700;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.login-hero p { color: #475569; font-size: 14px; }

/* Status badge */
.badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.badge-safe   { background: rgba(52,211,153,.15); color: #34d399; border: 1px solid rgba(52,211,153,.3); }
.badge-alert  { background: rgba(251,191,36,.15);  color: #fbbf24; border: 1px solid rgba(251,191,36,.3); }
.badge-danger { background: rgba(248,113,113,.15); color: #f87171; border: 1px solid rgba(248,113,113,.3); }

/* Risk bar */
.risk-bar-wrap { background: #1e2d50; border-radius: 8px; height: 12px; margin: 1rem 0; overflow: hidden; }
.risk-bar { height: 12px; border-radius: 8px; transition: width .5s; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div style="font-size:36px">🛡️</div>
        <h1>SafeTrail</h1>
        <p>Tourist Safety System</p>
    </div>
    """, unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "NAVIGATE",
    ["🔐 Login", "📊 Tourist Dashboard", "📍 Geo-Fencing",
     "🚨 SOS Emergency", "🤖 AI Risk Prediction", "📝 Incident Report", "⚙️ Admin Dashboard"]
)

# ════════════════════════════════════════════════════════════════
# LOGIN
# ════════════════════════════════════════════════════════════════
if menu == "🔐 Login":
    col_l, col_c, col_r = st.columns([1, 1.2, 1])
    with col_c:
        st.markdown("""
        <div class="login-hero">
            <div class="shield">🛡️</div>
            <h2>Welcome Back</h2>
            <p>Sign in to access the SafeTrail dashboard</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="••••••••")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sign In →", use_container_width=True):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful — Welcome, Admin!")
                st.balloons()
            else:
                st.error("❌ Invalid credentials. Try admin / 1234")

        st.markdown("""
        <div style="text-align:center; margin-top:1rem; font-size:12px; color:#334155;">
            Demo credentials: <code style="color:#38bdf8">admin</code> / <code style="color:#38bdf8">1234</code>
        </div>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# TOURIST DASHBOARD
# ════════════════════════════════════════════════════════════════
elif menu == "📊 Tourist Dashboard":
    st.markdown('<div class="page-title">Tourist Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Live overview of all registered tourists and current safety status</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    tiles = [
        (c1, "blue",  "TOTAL TOURISTS", "125", "↑ 3 today"),
        (c2, "green", "RISK LEVEL",      "Low", "All zones clear"),
        (c3, "amber", "ACTIVE ALERTS",   "2",   "Requires attention"),
        (c4, "green", "SAFE ZONES ONLINE","7",  "All operational"),
    ]
    for col, color, label, value, sub in tiles:
        with col:
            st.markdown(f"""
            <div class="metric-tile {color}">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📡 Live Status Feed")
    st.info("🟢 All tourist groups are currently within designated safe zones. No immediate threats detected.")

    data = {
        "Tourist":  ["Alice",  "Bob",    "Charlie", "Diana",  "Ethan"],
        "Zone":     ["Zone A", "Zone B", "Zone A",  "Zone C", "Zone B"],
        "Status":   ["✅ Safe","⚠️ Alert","✅ Safe", "✅ Safe","✅ Safe"],
        "Last Seen":["2 min",  "5 min",  "1 min",   "8 min",  "3 min"],
    }
    st.table(data)
    st.markdown('</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# GEO-FENCING
# ════════════════════════════════════════════════════════════════
elif menu == "📍 Geo-Fencing":
    st.markdown('<div class="page-title">Geo-Fencing Monitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Real-time boundary tracking for all active tourist zones</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        status = st.selectbox("Select Tourist Status", ["Inside Safe Zone", "Outside Safe Zone"])
        tourist = st.selectbox("Select Tourist", ["Alice", "Bob", "Charlie", "Diana", "Ethan"])
        zone    = st.selectbox("Zone", ["Zone A – City Centre", "Zone B – Waterfront", "Zone C – Heritage Site"])
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        if status == "Inside Safe Zone":
            st.markdown(f"""
            <div style="text-align:center; padding:2rem 0;">
                <div style="font-size:56px">✅</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:22px; color:#34d399; font-weight:700; margin:.5rem 0;">{tourist} is SAFE</div>
                <div style="color:#475569; font-size:14px;">Currently inside {zone}</div>
            </div>
            """, unsafe_allow_html=True)
            st.success("Boundary check passed. No action required.")
        else:
            st.markdown(f"""
            <div style="text-align:center; padding:2rem 0;">
                <div style="font-size:56px; animation:pulse 1s infinite;">⚠️</div>
                <div style="font-family:'Space Grotesk',sans-serif; font-size:22px; color:#fbbf24; font-weight:700; margin:.5rem 0;">{tourist} LEFT THE ZONE</div>
                <div style="color:#475569; font-size:14px;">Last known: {zone}</div>
            </div>
            """, unsafe_allow_html=True)
            st.warning("⚠️ Tourist has breached the geo-fence boundary. Alerting nearest response unit.")
        st.markdown('</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# SOS EMERGENCY
# ════════════════════════════════════════════════════════════════
elif menu == "🚨 SOS Emergency":
    st.markdown('<div class="page-title">SOS Emergency</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Instantly alert emergency responders with your location</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Tourist Details")
        name     = st.text_input("Your Name", placeholder="e.g. Alice Johnson")
        location = st.text_input("Last Known Location", placeholder="e.g. Zone B – Waterfront")
        etype    = st.selectbox("Emergency Type", ["Medical", "Theft / Robbery", "Lost", "Natural Disaster", "Other"])
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card" style="text-align:center; padding:3rem 1rem;">
            <div style="font-size:64px; margin-bottom:1rem;">🚨</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:20px; color:#f87171; font-weight:700; margin-bottom:.5rem;">PRESS IN AN EMERGENCY</div>
            <div style="font-size:13px; color:#475569; margin-bottom:1.5rem;">Alert is sent instantly to all nearby responders</div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="sos-btn">', unsafe_allow_html=True)
        if st.button("🆘 SEND SOS NOW", use_container_width=True):
            st.error(f"🚨 EMERGENCY ALERT DISPATCHED for {name or 'Unknown'} — {etype} — {location or 'Location unknown'}")
            st.snow()
        st.markdown('</div></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# AI RISK PREDICTION
# ════════════════════════════════════════════════════════════════
elif menu == "🤖 AI Risk Prediction":
    st.markdown('<div class="page-title">AI Risk Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Machine-learning powered safety scoring for zones and tourists</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        score = st.slider("Adjust Risk Score", 0, 100, 25)

        if score < 30:
            color, label, icon, tip = "#34d399", "LOW RISK", "🟢", "Conditions are safe. Continue normal operations."
            bar_color = "linear-gradient(90deg,#34d399,#059669)"
        elif score < 70:
            color, label, icon, tip = "#fbbf24", "MEDIUM RISK", "🟡", "Exercise caution. Increase patrol frequency."
            bar_color = "linear-gradient(90deg,#fbbf24,#f59e0b)"
        else:
            color, label, icon, tip = "#f87171", "HIGH RISK", "🔴", "Immediate action required. Evacuate if necessary."
            bar_color = "linear-gradient(90deg,#f87171,#ef4444)"

        st.markdown(f"""
        <div style="margin:1.5rem 0; text-align:center;">
            <div style="font-size:48px">{icon}</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:28px; font-weight:700; color:{color}; margin:.5rem 0;">{label}</div>
            <div class="risk-bar-wrap">
                <div class="risk-bar" style="width:{score}%; background:{bar_color};"></div>
            </div>
            <div style="font-size:13px; color:#64748b;">{tip}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Zone Risk Summary")
        zones_data = {
            "Zone":  ["Zone A", "Zone B", "Zone C", "Zone D"],
            "Score": [12,       58,        81,        24],
            "Level": ["🟢 Low", "🟡 Med",  "🔴 High", "🟢 Low"],
        }
        st.table(zones_data)
        st.markdown('</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# INCIDENT REPORT
# ════════════════════════════════════════════════════════════════
elif menu == "📝 Incident Report":
    st.markdown('<div class="page-title">Incident Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Submit and track safety incidents on the blockchain ledger</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### New Report")
        reporter = st.text_input("Your Name", placeholder="Full name")
        zone     = st.selectbox("Zone", ["Zone A – City Centre", "Zone B – Waterfront", "Zone C – Heritage Site"])
        severity = st.selectbox("Severity", ["🟢 Minor", "🟡 Moderate", "🔴 Critical"])
        incident = st.text_area("Incident Description", placeholder="Describe what happened in detail...", height=130)

        if st.button("Submit Report →", use_container_width=True):
            if incident.strip():
                st.success("✅ Report submitted and recorded on blockchain ledger.")
                st.code(f"TX HASH: 0x4f3a{hash(incident) % 10**12:012x}  |  Block: #{abs(hash(reporter)) % 99999}", language="text")
            else:
                st.warning("Please describe the incident before submitting.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Recent Reports")
        recent = {
            "ID":       ["#021", "#020", "#019"],
            "Zone":     ["Zone B", "Zone A", "Zone C"],
            "Type":     ["Theft", "Medical", "Lost"],
            "Severity": ["🟡 Mod", "🔴 Crit", "🟢 Minor"],
            "Status":   ["Open", "Resolved", "Open"],
        }
        st.table(recent)
        st.markdown('</div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════
# ADMIN DASHBOARD
# ════════════════════════════════════════════════════════════════
elif menu == "⚙️ Admin Dashboard":
    st.markdown('<div class="page-title">Admin Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">System-wide control panel and analytics overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, color, label, val, sub in [
        (c1, "blue",  "TOTAL TOURISTS",  "125", "Active today"),
        (c2, "amber", "ACTIVE ALERTS",   "2",   "Needs review"),
        (c3, "red",   "INCIDENTS",        "18",  "This month"),
        (c4, "green", "SYSTEM HEALTH",   "99%", "All services up"),
    ]:
        with col:
            st.markdown(f"""
            <div class="metric-tile {color}">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{val}</div>
                <div class="metric-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 👥 Tourist Registry")
        st.table({
            "Tourist":    ["Alice", "Bob",     "Charlie", "Diana",  "Ethan"],
            "Zone":       ["A",     "B",        "A",       "C",      "B"],
            "Status":     ["✅ Safe","⚠️ Alert","✅ Safe", "✅ Safe","✅ Safe"],
            "Risk Score": [12,       65,         18,        22,       30],
        })
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### ⚙️ System Controls")
        st.toggle("Geo-fence Alerts",    value=True)
        st.toggle("AI Risk Monitoring",  value=True)
        st.toggle("Blockchain Logging",  value=True)
        st.toggle("SMS Notifications",   value=False)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Refresh All Data", use_container_width=True):
            st.success("Data refreshed successfully!")
        st.markdown('</div>', unsafe_allow_html=True)
