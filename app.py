import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import time

# Sayfa Yapılandırması (Geniş ekran ve koyu tema hissi)
st.set_page_config(
    page_title="Echoes of Orbit - NASA Space Apps",
    page_icon="🛰️",
    layout="wide"
)

# Özel CSS ile Sci-Fi / Terminal Atmosferi Oluşturma
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #00ffcc;
    }
    .stButton>button {
        background-color: #1f293d;
        color: #00ffcc;
        border: 1px solid #00ffcc;
        border-radius: 5px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ffcc;
        color: #0b0f19;
    }
    .metric-card {
        background-color: #111827;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #1f293d;
    }
    </style>
""", unsafe_allow_html=True)

# Oturum Durumu (Oyun İlerlemesi ve Hikaye Aşamaları)
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "score" not in st.session_state:
    st.session_state.score = 100

# --- BAŞLIK VE DURUM ÇUBUĞU ---
st.title("🛰️ ECHOES OF ORBIT: Artemis-V İstasyonu")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Görev Durumu", value="KRİTİK AKTİF", delta="Güneş Fırtınası Yaklaşıyor")
with col2:
    st.metric(label="İstasyon Güvenliği", value=f"%{st.session_state.score}", delta="-5%")
with col3:
    st.metric(label="Aktif Modül", value=f"Bölüm {st.session_state.stage} / 3")

# --- HİKAYE VE OYUN AKIŞI ---

if st.session_state.stage == 1:
    st.subheader("Bölüm 1: Kessler Sendromu (Yörünge Temizliği)")
    st.write("""
    **Artemis-V AI Günlüğü:** *Komutan, yörüngedeki başıboş uzay çöpleri ana haberleşme uydumuzu tehdit ediyor. 
    Gerçek NASA TLE (Two-Line Element) verilerine dayanarak tehlikeli enkaz rotalarını tespit etmeli ve güvenli sönümleme yörüngesine yönlendirmeliyiz.*
    """)

    # 3D Dünya ve Enkaz Simülasyonu (Plotly ile interaktif 3D Küre)
    np.random.seed(42)
    n_debris = 30
    df_debris = pd.DataFrame({
        'x': np.random.randn(n_debris) * 5,
        'y': np.random.randn(n_debris) * 5,
        'z': np.random.randn(n_debris) * 5,
        'Risk': np.random.choice(['Yüksek Risk', 'Güvenli'], n_debris, p=[0.3, 0.7])
    })

    fig = px.scatter_3d(
        df_debris, x='x', y='y', z='z', color='Risk',
        color_discrete_map={'Yüksek Risk': '#ff4b4b', 'Güvenli': '#00ffcc'},
        title="Yörünge Enkaz Haritası (3D Canlı Telemetri)"
    )
    fig.update_layout(
        scene=dict(xaxis_backgroundcolor="rgba(0,0,0,0)",
                   yaxis_backgroundcolor="rgba(0,0,0,0)",
                   zaxis_backgroundcolor="rgba(0,0,0,0)"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )
    st.plotly_chart(fig, use_container_width=True)

    # Karar / Etkileşim Butonları
    st.write("### Karar Noktası:")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🚀 Yüksek Riskli Çöpleri İtme Manevrası Yap"):
            st.success("Manevra başarılı! Çöpler kontrollü yanma için atmosfere yönlendirildi.")
            st.session_state.stage = 2
            st.rerun()
    with col_b:
        if st.button("⚠️ Hiçbir Şey Yapma (Bekle)"):
            st.error("Çarpışma gerçekleşti! İstasyon hasar aldı.")
            st.session_state.score -= 25
            st.rerun()

elif st.session_state.stage == 2:
    st.subheader("Bölüm 2: İklim Anomalisi ve Dünya Gözlem Verileri")
    st.write("""
    **Artemis-V AI Günlüğü:** *Tehdit uzaklaştırıldı ancak Dünya'nın atmosferinde gizemli bir sıcaklık dalgalanması tespit edildi. 
    NASA Earth Observatory verilerini inceleyerek anomalinin kaynağını bulmalıyız.*
    """)

    # Basit bir mini veri bulmacası
    carbon_level = st.slider("Atmosferik Karbon Salınım Simülasyonu (ppm)", 300, 450, 415)
    
    if carbon_level > 420:
        st.warning("⚠️ Dikkat! Bu seviye kutuplardaki erimeyi hızlandırıyor, sinyalin kaynağı bu bölge olamaz.")
    else:
        st.success("✨ Optimum karbon dengesi aralığı yakalandı! Sinyalin kaynağı Amazon Ormanları üzerindeki bir uydu anomalisi.")

    if st.button("🔍 Bölüm 3'e Geç (Ötegezegen Sinyali Çözümleme)"):
        st.session_state.stage = 3
        st.rerun()

elif st.session_state.stage == 3:
    st.subheader("Bölüm 3: Ötegezegen Sinyali ve Spektroskopi")
    st.write("""
    **Artemis-V AI Günlüğü:** *Tebrikler Komutan! Derin uzaydan gelen gizemli 'Echo' sinyalinin James Webb Uzay Teleskobu (JWST) verileriyle eşleştiği doğrulandı. 
    Gezegenin atmosferinde su buharı ve yaşam izleri aranıyor.*
    """)

    # Başarı Kutlaması
    st.balloons()
    st.success("🎉 TEBRİKLER! 'Echoes of Orbit' görevini başarıyla tamamladın ve insanlığı kurtardın.")
    
    if st.button("🔄 Oyunu Yeniden Başlat"):
        st.session_state.stage = 1
        st.session_state.score = 100
        st.rerun()
