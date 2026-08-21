import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="A.S.M.A.A | Algérie Télécom",
    page_icon="📡",
    layout="wide"
)

# 2. تصميم أبيض نقي وواضح جداً (Corporate Clean Theme)
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #004b87 0%, #0284c7 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0, 75, 135, 0.15);
    }
    
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #cbd5e1;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
</style>
""", unsafe_allow_html=True)

# 3. عنوان المنصة الرسمي
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
c3.metric("🚨 أعطال تم منعها استباقياً", "18 عطل", "قبل حدوث الانقطاع")
c4.metric("⚡ سرعة التشخيص الآلي", "0.32 ثانية", "بدون تدخل بشري")

st.divider()

# 5. خريطة شوارع ولاية البيض الحقيقية والمفصلة (True City Center Map)
st.subheader("🗺️ خريطة الرصد الجغرافي الحي لعقد الألياف البصرية (مدينة البيض)")
st.caption("الخريطة تعرض شوارع وأحياء مدينة البيض الحقيقية ومواقع علب التوزيع (FAT) مع مستوى الخطورة:")

# تضمين خريطة OpenStreetMap الحقيقية لوسط مدينة البيض
map_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        #map {height: 420px; width: 100%; border-radius: 12px; border: 2px solid #94a3b8;}
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        // الإحداثيات الحقيقية لقلب مدينة البيض (El Bayadh City Center)
        var map = L.map('map').setView([33.6803, 1.0203], 15);
        
        // خريطة الشوارع والتفاصيل الحضرية
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap contributors | Algérie Télécom GIS'
        }).addTo(map);

        // 1. نقطة حمراء: حي المستقبل (عطل وشيك - التواء كابل)
        L.circleMarker([33.6850, 1.0250], {
            color: '#dc2626', fillColor: '#ef4444', fillOpacity: 0.85, radius: 11
        }).bindPopup("<b>🚨 علبة FAT-042 (شمال شرق البيض)</b><br><b>الإشارة:</b> -27.2 dBm<br><b>التشخيص:</b> التواء حاد وشيك الانقطاع!").addTo(map);

        // 2. نقطة برتقالية: طريق الرقاصة / حي المجاهدين (تحذير وتدهور)
        L.circleMarker([33.6760, 1.0140], {
            color: '#ea580c', fillColor: '#f97316', fillOpacity: 0.85, radius: 10
        }).bindPopup("<b>⚠️ علبة FAT-109 (طريق الرقاصة)</b><br><b>الإشارة:</b> -24.1 dBm<br><b>التشخيص:</b> غبار في الموصل الضوئي").addTo(map);

        // 3. نقطة خضراء: مقر اتصالات الجزائر / وسط المدينة (سليم)
        L.circleMarker([33.6803, 1.0203], {
            color: '#16a34a', fillColor: '#22c55e', fillOpacity: 0.9, radius: 10
        }).bindPopup("<b>✅ مركز الاتصالات الرئيسي (وسط المدينة)</b><br><b>الإشارة:</b> -19.2 dBm<br><b>الحالة:</b> كفاءة تامة").addTo(map);
    </script>
</body>
</html>
"""
components.html(map_html, height=440)

st.divider()

# 6. منحنى تدهور الإشارة
st.subheader("📉 المنحنى الزمني للقدرة الضوئية للمشتركين (Rx Optical Power - dBm)")
dates = pd.date_range(end=datetime.today(), periods=10)
telemetry_df = pd.DataFrame({
    'حي المستقبل (🚨 خطر - سينقطع)': np.linspace(-21.0, -27.2, 10),
    'حي المجاهدين (⚠️ تحذير)': np.linspace(-20.5, -23.8, 10),
    'وسط المدينة (✅ سليم)': np.random.uniform(-19.0, -19.3, 10)
}, index=dates)

st.line_chart(telemetry_df)

# 7. جدول التذاكر
st.subheader("🎫 سجل أوامر العمل الاستباقية للفرق التقنية الميدانية")
work_orders = pd.DataFrame({
    "رقم التذكرة": ["TK-2026-081", "TK-2026-082", "TK-2026-083"],
    "الحي / الموقع": ["حي المستقبل - البيض", "طريق الرقاصة - البيض", "وسط المدينة (Actel)"],
    "القدرة الضوئية (dBm)": ["-27.2 (حرج جداً)", "-24.1 (تحذير)", "-19.2 (ممتاز)"],
    "التشخيص الفيزيائي للذكاء الاصطناعي": ["التواء شديد في شعيرة الألياف (Macro-bend)", "تراكم غبار وأتربة في الموصل", "استقرار مثالي في التردد"],
    "الإجراء الميداني المطلوب": ["🚨 تدخل فوري لتقويم الانحناء خلال 12 سا", "⚠️ تنظيف المنفذ أثناء الجولة الدورية", "✅ لا يتطلب أي تدخل"]
})
st.dataframe(work_orders, use_container_width=True)

# 8. التذييل
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>منصة A.S.M.A.A — هندسة وتطوير: <b>أسماء خنان</b> | اتصالات الجزائر 🇩🇿</p>", unsafe_allow_html=True)
