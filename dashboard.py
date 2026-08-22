import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="A.S.M.A.A | Algérie Télécom", page_icon="📡", layout="wide")

# 2. تصميم أبيض نقي مع تصميم الزر الأزرق
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; color: #0f172a; font-family: 'Segoe UI', Tahoma, sans-serif; }
    .main-header {
        background: linear-gradient(135deg, #004b87 0%, #0284c7 100%);
        color: white; padding: 20px; border-radius: 12px; text-align: center; margin-bottom: 20px;
    }
    div[data-testid="stMetric"] {
        background-color: white; border: 1px solid #cbd5e1; padding: 15px; border-radius: 10px;
    }
    /* تصميم زر الفحص الشامل */
    div.stButton > button:first-child {
        background-color: #004b87; color: white; font-weight: bold; padding: 10px 25px; border-radius: 8px; border: none; width: 100%;
    }
    div.stButton > button:first-child:hover { background-color: #0284c7; color: white; }
</style>
""", unsafe_allow_html=True)

# 3. عنوان المنصة
st.markdown("""
<div class="main-header">
    <h1 style='margin:0; font-size: 2rem;'>📡 منصة A.S.M.A.A للتشخيص والصيانة التنبؤية</h1>
    <p style='margin:5px 0 0 0; font-size: 1.05rem; opacity: 0.95;'>
        <b>A</b>dvanced <b>S</b>mart <b>M</b>aintenance & <b>A</b>I <b>A</b>nalytics — اتصالات الجزائر (ولاية البيض)
    </p>
</div>
""", unsafe_allow_html=True)

# 4. المؤشرات
st.subheader("📊 مؤشرات أداء الشبكة اللحظية (KPIs)")
c1, c2, c3, c4 = st.columns(4)
c1.metric("🎯 دقة التنبؤ بالأعطال", "98.7%", "استقرار ممتاز")
c2.metric("🌐 إجمالي خطوط FTTH", "2,480 خط", "نشطة بالبيض")
c3.metric("🚨 أعطال تم منعها", "18 عطل", "قبل حدوث الانقطاع")
c4.metric("⚡ سرعة التشخيص الآلي", "0.32 ثانية", "بدون تدخل بشري")

st.divider()

# ==========================================
# ⚡ 5. زر الفحص الشامل التفاعلي (الذي طلبته)
# ==========================================
st.subheader("⚙️ لوحة التحكم العصبية (AI Control Panel)")
col_btn, col_empty = st.columns([1, 2])
with col_btn:
    if st.button("⚡ بدء الفحص الشامل للشبكة (Run AI Scan)"):
        with st.spinner("🤖 جاري فحص 2,480 روتر وتحليل مصفوفات الإشارة..."):
            time.sleep(2) # محاكاة وقت الفحص
        st.success("✅ اكتمل الفحص: تم رصد حالة حرجة واحدة تستوجب التدخل الفوري في (حي المستقبل).")
        
st.divider()

# 6. الخريطة الجغرافية
st.subheader("🗺️ خريطة الرصد الجغرافي الحي لعقد الألياف البصرية (مدينة البيض)")
map_html = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>#map {height: 420px; width: 100%; border-radius: 12px; border: 2px solid #94a3b8;}</style>
</head>
<body>
    <div id="map"></div>
    <script>
        var map = L.map('map').setView([33.6803, 1.0203], 15);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);

        L.circleMarker([33.6850, 1.0250], {color: '#dc2626', fillColor: '#ef4444', fillOpacity: 0.85, radius: 11})
            .bindPopup("<b>🚨 علبة FAT-042 (حي المستقبل)</b><br>الإشارة: -27.2 dBm<br>السبب: التواء حاد").addTo(map);

        L.circleMarker([33.6760, 1.0140], {color: '#ea580c', fillColor: '#f97316', fillOpacity: 0.85, radius: 10})
            .bindPopup("<b>⚠️ علبة FAT-109 (طريق الرقاصة)</b><br>الإشارة: -24.1 dBm<br>السبب: تراكم غبار").addTo(map);

        L.circleMarker([33.6803, 1.0203], {color: '#16a34a', fillColor: '#22c55e', fillOpacity: 0.9, radius: 10})
            .bindPopup("<b>✅ مركز الاتصالات (وسط المدينة)</b><br>الإشارة: -19.2 dBm<br>الحالة: ممتازة").addTo(map);
    </script>
</body>
</html>
"""
components.html(map_html, height=440)

st.divider()

# 7. المنحنى البياني (تم إصلاحه ليظهر بوضوح)
st.subheader("📉 المنحنى الزمني للقدرة الضوئية (Rx Optical Power - dBm)")
dates = pd.date_range(end=datetime.today(), periods=10)

# استخدام أسماء إنجليزية برمجياً لتفادي أخطاء العرض، وسيتم عرضها بالألوان
telemetry_df = pd.DataFrame({
    'حي المستقبل (خطر)': np.linspace(-21.0, -27.2, 10),
    'طريق الرقاصة (تحذير)': np.linspace(-20.5, -23.8, 10),
    'وسط المدينة (سليم)': np.random.uniform(-19.0, -19.3, 10)
}, index=dates)

st.line_chart(telemetry_df)

# 8. جدول التذاكر
st.subheader("🎫 سجل أوامر العمل الاستباقية للفرق التقنية")
work_orders = pd.DataFrame({
    "رقم التذكرة": ["TK-2026-081", "TK-2026-082", "TK-2026-083"],
    "الموقع": ["حي المستقبل - البيض", "طريق الرقاصة - البيض", "وسط المدينة (Actel)"],
    "القدرة (dBm)": ["-27.2 (حرج جداً)", "-24.1 (تحذير)", "-19.2 (ممتاز)"],
    "التشخيص الذكي": ["التواء شديد في الكابل", "تراكم غبار وأتربة", "استقرار مثالي"],
    "الإجراء المطلوب": ["🚨 تدخل فوري خلال 12 سا", "⚠️ تنظيف في الجولة القادمة", "✅ لا يتطلب أي تدخل"]
})
st.dataframe(work_orders, use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>منصة A.S.M.A.A — هندسة وتطوير: <b>أسماء كخنان</b> | اتصالات الجزائر 🇩🇿</p>", unsafe_allow_html=True)
