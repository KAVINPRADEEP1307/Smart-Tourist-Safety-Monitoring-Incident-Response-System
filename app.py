import streamlit as st

st.set_page_config(
    page_title="SafeTrail – Tourist Safety System",
    page_icon="🛡️",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "Login"

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1e;
    color: #e2e8f0;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.5rem 2.5rem; max-width: 1200px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b3e 0%, #070d1f 100%);
    border-right: 1px solid #1a2744;
}

.sidebar-brand {
    text-align: center;
    padding: 2rem 1rem 1.5rem;
    border-bottom: 1px solid #1a2744;
    margin-bottom: 1rem;
}
.sidebar-brand .logo { font-size: 44px; margin-bottom: .4rem; }
.sidebar-brand h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px; font-weight: 700;
    background: linear-gradient(135deg, #38bdf8, #818cf8);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin: 0 0 .2rem;
}
.sidebar-brand p { font-size: 11px; color: #334155 !important; margin: 0; }

/* Nav buttons */
.stButton > button {
    background: transparent !important;
    color: #64748b !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.65rem 1rem !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    text-align: left !important;
    width: 100% !important;
    transition: all .18s !important;
    margin-bottom: 2px !important;
}
.stButton > button:hover {
    background: rgba(56,189,248,.08) !important;
    color: #38bdf8 !important;
}

/* Active nav button override via data attr trick — we highlight with markdown instead */
.nav-active > .stButton > button {
    background: linear-gradient(90deg, rgba(56,189,248,.15), rgba(129,140,248,.1)) !important;
    color: #38bdf8 !important;
    border-left: 3px solid #38bdf8 !important;
    font-weight: 600 !important;
}

/* ── Page title ── */
.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 30px; font-weight: 700;
    background: linear-gradient(135deg, #f0f9ff 0%, #bae6fd 60%, #818cf8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: .2rem;
}
.page-subtitle { font-size: 13px; color: #475569; margin-bottom: 1.8rem; }

/* ── Cards ── */
.card {
    background: linear-gradient(135deg, #111827 0%, #0f172a 100%);
    border: 1px solid #1e2d50;
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.card:hover { border-color: #334155; }

/* ── Metric tiles ── */
.metric-tile {
    background: linear-gradient(135deg, #111827, #0f172a);
    border: 1px solid #1e2d50;
    border-radius: 16px;
    padding: 1.3rem 1.5rem;
    position: relative; overflow: hidden;
}
.metric-tile::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; }
.metric-tile.blue::before  { background: linear-gradient(90deg,#38bdf8,#818cf8); }
.metric-tile.green::before { background: linear-gradient(90deg,#34d399,#059669); }
.metric-tile.amber::before { background: linear-gradient(90deg,#fbbf24,#f59e0b); }
.metric-tile.red::before   { background: linear-gradient(90deg,#f87171,#ef4444); }
.metric-label { font-size:11px; text-transform:uppercase; letter-spacing:1.5px; color:#475569; margin-bottom:.4rem; }
.metric-value { font-family:'Space Grotesk',sans-serif; font-size:34px; font-weight:700; color:#f1f5f9; }
.metric-sub   { font-size:12px; color:#64748b; margin-top:.2rem; }

/* ── Inputs ── */
.stTextInput > div > div > input,
.stTextArea  > div > div > textarea {
    background:#0f172a !important; border:1px solid #1e2d50 !important;
    border-radius:10px !important; color:#e2e8f0 !important; padding:.7rem 1rem !important;
}
.stTextInput > div > div > input:focus,
.stTextArea  > div > div > textarea:focus {
    border-color:#38bdf8 !important; box-shadow:0 0 0 3px rgba(56,189,248,.12) !important;
}
.stTextInput label,.stTextArea label,.stSelectbox label,.stSlider label {
    color:#94a3b8 !important; font-size:13px !important; font-weight:500 !important;
}
.stSelectbox > div > div {
    background:#0f172a !important; border:1px solid #1e2d50 !important;
    border-radius:10px !important; color:#e2e8f0 !important;
}

/* Action buttons (non-nav) */
.action-btn .stButton > button {
    background: linear-gradient(135deg,#0ea5e9,#6366f1) !important;
    color:#fff !important; border-radius:10px !important;
    padding:.6rem 1.8rem !important; font-weight:600 !important;
    box-shadow:0 4px 15px rgba(14,165,233,.25) !important;
    text-align:center !important;
}
.action-btn .stButton > button:hover { opacity:.85 !important; }

/* SOS */
.sos-btn .stButton > button {
    background:linear-gradient(135deg,#ef4444,#b91c1c) !important;
    font-size:18px !important; padding:1rem 2rem !important;
    border-radius:50px !important;
    box-shadow:0 0 30px rgba(239,68,68,.45) !important;
    text-align:center !important;
    animation: sosPulse 2s infinite;
}
@keyframes sosPulse {
    0%,100% { box-shadow:0 0 30px rgba(239,68,68,.45); }
    50%      { box-shadow:0 0 55px rgba(239,68,68,.8); }
}

/* risk bar */
.risk-bar-wrap { background:#1e2d50; border-radius:8px; height:12px; margin:1rem 0; overflow:hidden; }
.risk-bar { height:12px; border-radius:8px; }

/* login hero */
.login-hero { text-align:center; padding:2.5rem 1rem 1.5rem; }
.login-hero .shield { font-size:60px; margin-bottom:.8rem; }
.login-hero h2 {
    font-family:'Space Grotesk',sans-serif; font-size:26px; font-weight:700;
    background:linear-gradient(135deg,#38bdf8,#818cf8);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.login-hero p { color:#475569; font-size:13px; }

.divider { border:none; border-top:1px solid #1a2744; margin:1rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Nav items ──────────────────────────────────────────────────────────────
nav_items = [
    ("🔐", "Login"),
    ("📊", "Tourist Dashboard"),
    ("📍", "Geo-Fencing"),
    ("🚨", "SOS Emergency"),
    ("🤖", "AI Risk Prediction"),
    ("📝", "Incident Report"),
    ("⚙️",  "Admin Dashboard"),
]

# ── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="logo">🛡️</div>
        <h1>SafeTrail</h1>
        <p>Tourist Safety System v2.0</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="font-size:10px;color:#334155;text-transform:uppercase;letter-spacing:1.5px;padding:0 .5rem .4rem;margin:0;">MAIN MENU</p>', unsafe_allow_html=True)

    for icon, label in nav_items:
        active = st.session_state.page == label
        if active:
            st.markdown('<div class="nav-active">', unsafe_allow_html=True)
        if st.button(f"{icon}  {label}", key=f"nav_{label}", use_container_width=True):
            st.session_state.page = label
            st.rerun()
        if active:
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.markdown('<p style="font-size:11px;color:#1e2d50;text-align:center;padding:.5rem;">© 2025 SafeTrail Inc.</p>', unsafe_allow_html=True)

page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: LOGIN
# ══════════════════════════════════════════════════════════════════════════════
if page == "Login":
    _, col, _ = st.columns([1, 1.1, 1])
    with col:
        st.markdown("""
        <div class="login-hero">
            <div class="shield">🛡️</div>
            <h2>Welcome to SafeTrail</h2>
            <p>Sign in to access your safety dashboard</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="action-btn">', unsafe_allow_html=True)
        if st.button("Sign In →", use_container_width=True):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful — Welcome, Admin!")
                st.balloons()
            else:
                st.error("❌ Invalid credentials. Try  admin / 1234")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align:center;margin-top:1rem;font-size:12px;color:#334155;">
            Demo: <code style="color:#38bdf8">admin</code> / <code style="color:#38bdf8">1234</code>
        </div></div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: TOURIST DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Tourist Dashboard":
    st.markdown('<div class="page-title">📊 Tourist Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Live overview of all registered tourists and safety status</div>', unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col,color,label,val,sub in [
        (c1,"blue","Total Tourists","125","↑ 3 joined today"),
        (c2,"green","Risk Level","Low","All zones clear"),
        (c3,"amber","Active Alerts","2","Needs attention"),
        (c4,"green","Safe Zones","7 / 7","All operational"),
    ]:
        with col:
            st.markdown(f'<div class="metric-tile {color}"><div class="metric-label">{label}</div><div class="metric-value">{val}</div><div class="metric-sub">{sub}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 📡 Live Tourist Feed")
    st.info("🟢 All tourist groups are within designated safe zones.")
    st.table({"Tourist":["Alice","Bob","Charlie","Diana","Ethan"],"Zone":["Zone A","Zone B","Zone A","Zone C","Zone B"],"Status":["✅ Safe","⚠️ Alert","✅ Safe","✅ Safe","✅ Safe"],"Last Seen":["2 min","5 min","1 min","8 min","3 min"]})
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GEO-FENCING
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Geo-Fencing":
    st.markdown('<div class="page-title">📍 Geo-Fencing Monitor</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Real-time boundary tracking for all active zones</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        tourist = st.selectbox("Select Tourist", ["Alice","Bob","Charlie","Diana","Ethan"])
        zone    = st.selectbox("Zone", ["Zone A – City Centre","Zone B – Waterfront","Zone C – Heritage Site"])
        status  = st.selectbox("Current Status", ["Inside Safe Zone","Outside Safe Zone"])
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card" style="text-align:center;padding:2.5rem 1rem;">', unsafe_allow_html=True)
        if status == "Inside Safe Zone":
            st.markdown(f'<div style="font-size:56px">✅</div><div style="font-family:Space Grotesk,sans-serif;font-size:22px;color:#34d399;font-weight:700;margin:.5rem 0">{tourist} is SAFE</div><div style="color:#475569;font-size:13px;">Currently inside {zone}</div>', unsafe_allow_html=True)
            st.success("Boundary check passed. No action required.")
        else:
            st.markdown(f'<div style="font-size:56px">⚠️</div><div style="font-family:Space Grotesk,sans-serif;font-size:22px;color:#fbbf24;font-weight:700;margin:.5rem 0">{tourist} LEFT THE ZONE</div><div style="color:#475569;font-size:13px;">Last known: {zone}</div>', unsafe_allow_html=True)
            st.warning("Tourist breached geo-fence! Alerting nearest response unit.")
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SOS EMERGENCY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "SOS Emergency":
    st.markdown('<div class="page-title">🚨 SOS Emergency</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Instantly alert emergency responders with your location</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        name     = st.text_input("Your Name", placeholder="Full name")
        location = st.text_input("Last Known Location", placeholder="e.g. Zone B – Waterfront")
        etype    = st.selectbox("Emergency Type", ["Medical","Theft / Robbery","Lost","Natural Disaster","Other"])
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card" style="text-align:center;padding:3rem 1rem;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:60px;margin-bottom:.8rem;">🚨</div><div style="font-family:Space Grotesk,sans-serif;font-size:18px;color:#f87171;font-weight:700;margin-bottom:.4rem;">PRESS IN AN EMERGENCY</div><div style="font-size:12px;color:#475569;margin-bottom:1.5rem;">Instantly alerts all nearby responders</div>', unsafe_allow_html=True)
        st.markdown('<div class="sos-btn">', unsafe_allow_html=True)
        if st.button("🆘 SEND SOS NOW", use_container_width=True):
            st.error(f"🚨 ALERT SENT — {name or 'Unknown'} | {etype} | {location or 'Location unknown'}")
            st.snow()
        st.markdown('</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: AI RISK PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "AI Risk Prediction":
    st.markdown('<div class="page-title">🤖 AI Risk Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Machine-learning powered safety scoring for zones and tourists</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.2,1])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        score = st.slider("Adjust Risk Score", 0, 100, 25)
        if score < 30:
            color,label,icon,tip = "#34d399","LOW RISK","🟢","Conditions are safe. Continue normal operations."
            bar = "linear-gradient(90deg,#34d399,#059669)"
        elif score < 70:
            color,label,icon,tip = "#fbbf24","MEDIUM RISK","🟡","Exercise caution. Increase patrol frequency."
            bar = "linear-gradient(90deg,#fbbf24,#f59e0b)"
        else:
            color,label,icon,tip = "#f87171","HIGH RISK","🔴","Immediate action required. Evacuate if necessary."
            bar = "linear-gradient(90deg,#f87171,#ef4444)"
        st.markdown(f'<div style="text-align:center;margin:1.5rem 0"><div style="font-size:48px">{icon}</div><div style="font-family:Space Grotesk,sans-serif;font-size:26px;font-weight:700;color:{color};margin:.5rem 0">{label}</div><div class="risk-bar-wrap"><div class="risk-bar" style="width:{score}%;background:{bar}"></div></div><div style="font-size:13px;color:#64748b">{tip}</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Zone Risk Summary")
        st.table({"Zone":["Zone A","Zone B","Zone C","Zone D"],"Score":[12,58,81,24],"Level":["🟢 Low","🟡 Med","🔴 High","🟢 Low"]})
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: INCIDENT REPORT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Incident Report":
    st.markdown('<div class="page-title">📝 Incident Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Submit and track safety incidents on the blockchain ledger</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        reporter = st.text_input("Your Name", placeholder="Full name")
        zone     = st.selectbox("Zone", ["Zone A – City Centre","Zone B – Waterfront","Zone C – Heritage Site"])
        severity = st.selectbox("Severity", ["🟢 Minor","🟡 Moderate","🔴 Critical"])
        incident = st.text_area("Incident Description", placeholder="Describe what happened...", height=120)
        st.markdown('<div class="action-btn">', unsafe_allow_html=True)
        if st.button("Submit Report →", use_container_width=True):
            if incident.strip():
                st.success("✅ Report submitted and recorded on blockchain.")
                st.code(f"TX HASH: 0x4f3a{hash(incident)%10**12:012x}  |  Block: #{abs(hash(reporter))%99999}", language="text")
            else:
                st.warning("Please describe the incident before submitting.")
        st.markdown('</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### Recent Reports")
        st.table({"ID":["#021","#020","#019"],"Zone":["Zone B","Zone A","Zone C"],"Type":["Theft","Medical","Lost"],"Severity":["🟡 Mod","🔴 Crit","🟢 Minor"],"Status":["Open","Resolved","Open"]})
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ADMIN DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Admin Dashboard":
    st.markdown('<div class="page-title">⚙️ Admin Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">System-wide control panel and analytics overview</div>', unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col,color,label,val,sub in [
        (c1,"blue","Total Tourists","125","Active today"),
        (c2,"amber","Active Alerts","2","Needs review"),
        (c3,"red","Incidents","18","This month"),
        (c4,"green","System Health","99%","All services up"),
    ]:
        with col:
            st.markdown(f'<div class="metric-tile {color}"><div class="metric-label">{label}</div><div class="metric-value">{val}</div><div class="metric-sub">{sub}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.4,1])
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### 👥 Tourist Registry")
        st.table({"Tourist":["Alice","Bob","Charlie","Diana","Ethan"],"Zone":["A","B","A","C","B"],"Status":["✅ Safe","⚠️ Alert","✅ Safe","✅ Safe","✅ Safe"],"Risk Score":[12,65,18,22,30]})
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("#### ⚙️ System Controls")
        st.toggle("Geo-fence Alerts", value=True)
        st.toggle("AI Risk Monitoring", value=True)
        st.toggle("Blockchain Logging", value=True)
        st.toggle("SMS Notifications", value=False)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="action-btn">', unsafe_allow_html=True)
        if st.button("🔄 Refresh All Data", use_container_width=True):
            st.success("Data refreshed!")
        st.markdown('</div></div>', unsafe_allow_html=True)
