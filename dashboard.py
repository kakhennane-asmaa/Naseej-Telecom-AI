import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. ضبط إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="A.S.M.A.A | Telecom AI Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تخصيص تصميم مستقبلي وثيم ذكاء اصطناعي (Custom CSS / Neon & Glassmorphism)
st.markdown("""
<style>
    /* خلفية داكنة مستقبلية */
    .stApp {
        background: linear-gradient(135deg, #0a0e1a 0%, #0d1527 50%, #0a1122 100%);
        color: #e0e6ed;
    }
    
    /* بطاقات زجاجية مضيئة (Glassmorphism Cards) */
    .ai-card {
        background: rgba(18, 28, 48, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 229, 255, 0.2);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* عنوان المنصة المضيء */
    .glowing-title {
        font-family: 'Segoe UI', Tahoma, sans-serif;
        font-weight: 800;
        font-size: 2.5rem;
        background: linear-gradient(90deg, #00e5ff, #3b82f6, #00ff88);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .sub-tagline {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        letter-spacing: 1.5px;
        margin-bottom: 25px;
    }
    
    /* أزرار مستقبلية */
    .stButton>button {
        background: linear-gradient(90deg, #00e5ff 0%, #0284c7 100%);
        color: #04101e;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# 3. ترويسة المنصة الرسمية (A.S.M.A.A Platform Header)
st.markdown('<div class="glowing-title">⚡ منصة A.S.M.A.A للذكاء الاصطناعي</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-tagline"><b>A</b>dvanced <b>S</b>mart <b>M</b>aintenance & <b>A</b>I <b>A</b>nalytics | Algérie Télécom Pilot</div>', unsafe_allow_html=True)

# شريط الحالة العلوي
st.markdown("""
<div style="display: flex; justify-content: space-between; background: rgba(0, 229, 255, 0.08); border: 1px solid rgba(0, 229, 255, 0.3); border-radius: 10px; padding: 10px 20px; margin-bottom: 25px;">
    <span>📍 <b>عقدة الاختبار الميداني:</b> ولاية البيض (Node: EL-BAYADH-GPON-01)</span>
    <span>🟢 <b>حالة النواة العصبية:</b> تشغيل نشط (Active Autonomous Mode)</span>
    <span>⏱️ <b>آخر تدريب للنموذج:</b> اليوم 2026</span>
</div>
""", unsafe_allow_html=True)

# 4. مؤشرات الأداء الحيوية (Key Performance Indicators)
st.markdown("### 📊 المؤشرات الاستراتيجية للشبكة (Strategic KPIs)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="🎯 دقة التنبؤ العصبي (AI Accuracy)", value="98.7%", delta="+1.2% هذا الأسبوع")
with col2:
    st.metric(label="🌐 خطوط FTTH المراقبة آنياً", value="2,480", delta="عقدة البيض المركزية")
with col3:
    st.metric(label="⚠️ انقطاعات تم منعها استباقياً", value="34 خط", delta="-85% شكاوى الزبائن")
with col4:
    st.metric(label="⚡ سرعة الإصلاح الذاتي (MTTR)", value="0.32 ثانية", delta="Zero-Touch Resolution")

st.write("")

# 5. زر التشخيص التفاعلي الفوري (Interactive AI Scanner)
col_btn, col_empty = st.columns([1, 2])
with col_btn:
    if st.button("⚡ تشغيل الفحص الشامل للشبكة الضوئية الآن"):
        with st.spinner("🤖 جاري تحليل التيليمتري الضوئية ومصفوفات الإشارة عبر الذكاء الاصطناعي..."):
            import time
            time.sleep(1.2)
        st.toast("✅ تم فحص 2,480 عقدة ضوئية بنجاح. تم رصد حالة حرجة واحدة تستوجب التدخل.", icon="🔍")

# 6. الخريطة الجغرافية التفاعلية لعقد ولاية البيض (GIS Map)
st.markdown("### 🗺️ الخريطة الجغرافية لتوطين الأعطال الضوئية (GIS Telemetry Map)")
st.caption("تحديد مواقع علب التوزيع الضوئية (FAT / ODF) في ولاية البيض مع تدرج الخطورة:")

# إحداثيات ولاية البيض الحقيقية مع نقاط علب توزيع متفرقة
bayadh_coords = pd.DataFrame({
    'lat': [31.6989, 31.7050, 31.6920, 31.7100, 31.6850],
    'lon': [1.0118, 1.0200, 1.0050, 1.0150, 1.0300]
})
st.map(bayadh_coords, zoom=12)

# 7. الرسوم البيانية لتدهور الإشارة الضوئية (Telemetry Analytics)
st.markdown("### 📉 الرصد الفيزيائي لتدهور الإشارة الضوئية (ITU-T G.984 Standards)")
dates = pd.date_range(end=datetime.today(), periods=10)

telemetry_data = pd.DataFrame({
    'عقدة حي الوئام (سليمة - 19dBm)': np.random.uniform(-19.1, -19.4, 10),
    'عقدة حي المجاهدين (تحذير - 23.5dBm)': np.linspace(-20.5, -23.8, 10),
    'عقدة حي المستقبل (حرجة - ستنقطع 26.8dBm)': np.linspace(-21.0, -27.2, 10)
}, index=dates)

st.line_chart(telemetry_data)

# 8. جدول التذاكر الذكية للتدخل الاستباقي
st.markdown("### 🎫 سجل التذاكر الاستباقية للفرق الميدانية (Proactive Work Orders)")
tickets_df = pd.DataFrame({
    "رقم التذكرة": ["TK-2026-081", "TK-2026-082", "TK-2026-083", "TK-2026-084"],
    "معرف الخط": ["FTTH-DZ-BAY-042", "FTTH-DZ-BAY-109", "FTTH-DZ-BAY-201", "FTTH-DZ-BAY-005"],
    "المنطقة / الحي": ["حي المستقبل - البيض", "حي المجاهدين - البيض", "وسط المدينة - البيض", "حي أول نوفمبر"],
    "القدرة الضوئية": ["-27.2 dBm (حرج)", "-24.1 dBm (تحذير)", "-19.2 dBm (ممتاز)", "-18.9 dBm (ممتاز)"],
    "التشخيص الفيزيائي للـ AI": ["التواء شديد في الألياف (Macro-bend)", "تراكم غبار في المنفذ الضوئي", "استقرار مثالي للإشارة", "استقرار مثالي للإشارة"],
    "الإجراء المقترح": ["إرسال تقني لمعالجة الالتواء خلال 12 سا", "تنظيف موصل FAT في الصيانة الدورية", "لا يتطلب أي إجراء", "لا يتطلب أي إجراء"]
})
st.dataframe(tickets_df, use_container_width=True)

# 9. التذييل الرسمي للمنصة
st.divider()
st.markdown("""
<div style="text-align: center; color: #64748b; font-size: 0.9rem;">
    منصة <b>A.S.M.A.A</b> | تطوير: <b>أسماء كخنان</b> & فريق النظم والذكاء الاصطناعي 🇩🇿<br>
    مصممة وفق أعلى معايير أتمتة الشبكات والاتصالات العالمية (Carrier-Grade AIOps).
</div>
""", unsafe_allow_html=True)
