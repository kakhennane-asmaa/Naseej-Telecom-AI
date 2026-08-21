import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. إعدادات الصفحة
st.set_page_config(page_title="Naseej - NOC Dashboard", page_icon="🌐", layout="wide")

# 2. تصميم رأس الصفحة
st.markdown("<h1 style='text-align: center; color: #004b87;'>🌐 مشروع نَسِيج | لوحة تحكم مركز العمليات</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #e3000f;'>AI-Powered Automated Diagnostics - Algérie Télécom</h4>", unsafe_allow_html=True)
st.divider()

# 3. الإحصائيات العلوية
st.subheader("📊 مؤشرات الأداء الحية (KPIs) - منطقة البيض")
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="دقة التنبؤ (AI Accuracy)", value="98.5%", delta="مستقر")
col2.metric(label="إجمالي المشتركين النشطين", value="1,240", delta="FTTH GPON")
col3.metric(label="الخطوط المهددة بالانقطاع", value="12", delta="-3 تم إصلاحها آلياً", delta_color="inverse")
col4.metric(label="زمن الاستجابة للذكاء الاصطناعي", value="0.4 ثانية", delta="ممتاز")

st.divider()

# 4. الرسوم البيانية (محاكاة البيانات)
st.subheader("📉 منحنى تدهور الإشارة الضوئية (Rx Power Degradation)")
days = pd.date_range(start=datetime.now(), periods=10)
data = pd.DataFrame({
    'FTTH-001 (مستقر)': np.random.uniform(-19, -20, 10),
    'FTTH-002 (خطر)': np.linspace(-21, -26, 10) + np.random.uniform(-0.5, 0.5, 10),
    'FTTH-003 (حرج-سيعطل)': np.linspace(-24, -28, 10) + np.random.uniform(-0.2, 0.2, 10)
}, index=days)
st.line_chart(data)

# 5. جدول التدخل الميداني
st.subheader("📋 قائمة التدخل الاستباقي (Proactive Dispatch List)")
df = pd.DataFrame({
    "المعرف (ID)": ["FTTH-003", "FTTH-002", "FTTH-099", "FTTH-001"],
    "الولاية / العقدة": ["البيض / OLT-04", "البيض / OLT-04", "البيض / OLT-02", "البيض / OLT-01"],
    "قوة الإشارة (dBm)": ["-27.5", "-26.1", "-24.0", "-19.2"],
    "السبب التقني المحتمل": ["التواء حاد (Macro-bend)", "تلوث الموصل (Dust)", "تقادم اللحام", "سليم (Normal)"],
    "قرار الذكاء الاصطناعي": ["🚨 إصلاح فوري (خلال 24 سا)", "⚠️ إرسال تقني (خلال 5 أيام)", "👀 مراقبة آلية", "✅ لا تدخل مطلوب"]
})
st.dataframe(df, use_container_width=True)

st.success("✅ البيانات مشفرة وآمنة. تعمل الواجهة بنظام المحاكاة (Simulation Mode).")
