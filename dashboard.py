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

# 2. تصميم احترافي نظيف وفاتح (Corporate Clean Light Theme)
st.markdown("""
<style>
    /* خلفية بيضاء نقية */
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* ترويسة أنيقة */
    .main-header {
        background: linear-gradient(135deg, #004b87 0%, #0284c7 100%);
        color: white;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 75, 135, 0.15);
    }
    
    /* بطاقات بيضاء للإحصائيات */
    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e2e8f0;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
</style>
""", unsafe_allow_html=True)

# 3. عنوان المنصة
st.markdown("""
<div class="main-header">
    <h1 style='margin:0; font-size: 2.2rem;'>📡 منصة A.S.M.A.A للتشخيص والصيانة التنبؤية</h1>
    <p style='margin:5px 0 0 0; font-size: 1.1rem; opacity: 0.9;'>
        <b>A</b>dvanced <b>S</b>mart <b>M</b>aintenance & <b>A</b>I <b>A</b>nalytics — اتصالات الجزائر (ولاية البيض)
    </p>
</div>
""", unsafe_allow_html=True)

# 4. شريط معلومات التشغيل
st.info("📍 **عقدة الرصد الحالية:** قطاع الألياف البصرية بولاية البيض (FTTH Central Node) — النظام يعمل بوضع المحاكاة المطابقة لمعايير ITU-T G.984 الدولية.")

# 5. المؤشرات الاستراتيجية
st.subheader("📊 مؤشرات أداء الشبكة اللحظية (KPIs)")
c1, c2, c3, c4 = st.columns(4)
c1.metric("🎯 دقة التنبؤ بالأعطال", "98.7%", "استقرار ممتاز")
c2.metric("🌐 إجمالي خطوط FTTH", "2,480 خط", "نشطة")
c3.metric("🚨 أعطال تم منعها استباقياً", "18 عطل", "قبل حدوث الانقطاع")
c4.metric("⚡ سرعة التشخيص الآلي", "0.32 ثانية", "بدون تدخل بشري")

st.divider()

# 6. خريطة الشوارع التفاعلية الحقيقية لولاية البيض (Leaflet Real Map)
st.subheader("🗺️ خريطة الرصد الجغرافي الحي لعقد الألياف البصرية (ولاية البيض)")
st.caption("الخريطة تعرض الشوارع الحقيقية ومواقع علب التوزيع الضوئية (FAT) مع بيان مستوى الخطورة:")

# تضمين خريطة OpenStreetMap حقيقية لشوارع ولاية البيض
map_html = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>#map {height: 380px; width: 100%; border-radius: 10px; border: 1px solid #cbd5e1;}</style>
</head>
<body>
    <div id="map"></div>
    <script>
        // إحداثيات ولاية البيض
        var map = L.map('map').setView([31.6989, 1.0118], 14);
        
        // خريطة الشوارع الحقيقية OpenStreetMap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        // إضافة نقاط المراقبة بعلب التوزيع الحقيقية
        // 1. نقطة حمراء: خطر وانقطاع وشيك
        L.circleMarker([31.7050, 1.0150], {color: 'red', radius: 10, fillOpacity: 0.8})
            .bindPopup("<b>🚨 علبة FAT-042 (حي المستقبل)</b><br>الإشارة: -27.2 dBm<br>الحالة: التواء حاد وشيك الانقطاع!")
            .addTo(map);

        // 2. نقطة برتقالية: تحذير وتدهور تدريجي
        L.circleMarker([31.6920, 1.0080], {color: 'orange', radius: 9, fillOpacity: 0.8})
            .bindPopup("<b>⚠️ علبة FAT-109 (حي المجاهدين)</b><br>الإشارة: -24.1 dBm<br>الحالة: غبار وتدهور تدريجي")
            .addTo(map);

        // 3. نقطة خضراء: خطوط سليمة ومستقرة
        L.circleMarker([31.6989, 1.0118], {color: 'green', radius: 8, fillOpacity: 0.8})
            .bindPopup("<b>✅ السنترال الرئيسي (وسط مدينة البيض)</b><br>الإشارة: -19.2 dBm<br>الحالة: ممتازة")
            .addTo(map);
    </script>
</body>
</html>
"""
components.html(map_html, height=400)

st.divider()

# 7. منحنى تدهور الإشارة الضوئية
st.subheader("📉 المنحنى الزمني للقدرة الضوئية للمشتركين (Rx Optical Power - dBm)")
dates = pd.date_range(end=datetime.today(), periods=10)
telemetry_df = pd.DataFrame({
    'حي المستقبل (🚨 خطر - سينقطع)': np.linspace(-21.0, -27.2, 10),
    'حي المجاهدين (⚠️ تحذير)': np.linspace(-20.5, -23.8, 10),
    'وسط المدينة (✅ سليم)': np.random.uniform(-19.0, -19.3, 10)
}, index=dates)

st.line_chart(telemetry_df)

# 8. جدول التذاكر الاستباقية
st.subheader("🎫 سجل أوامر العمل الاستباقية للفرق التقنية الميدانية")
work_orders = pd.DataFrame({
    "رقم التذكرة": ["TK-2026-081", "TK-2026-082", "TK-2026-083"],
    "الحي / الموقع": ["حي المستقبل - البيض", "حي المجاهدين - البيض", "وسط المدينة - البيض"],
    "القدرة الضوئية (dBm)": ["-27.2 (حرج جداً)", "-24.1 (تحذير)", "-19.2 (ممتاز)"],
    "التشخيص الفيزيائي للذكاء الاصطناعي": ["التواء شديد في شعيرة الألياف (Macro-bend)", "تراكم غبار وأتربة في الموصل", "استقرار مثالي في التردد"],
    "الإجراء الميداني المطلوب": ["🚨 تدخل فوري لتقويم الانحناء خلال 12 سا", "⚠️ تنظيف المنفذ أثناء الجولة الدورية", "✅ لا يتطلب أي تدخل"]
})
st.dataframe(work_orders, use_container_width=True)

# 9. التذييل
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>منصة A.S.M.A.A — هندسة وتطوير: <b>أسماء خنان</b> | اتصالات الجزائر 🇩🇿</p>", unsafe_allow_html=True)
