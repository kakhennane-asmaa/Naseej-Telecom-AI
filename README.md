# 🌐 منصة A.S.M.A.A | Algérie Télécom AIOps
> **Advanced Smart Maintenance & AI Analytics - Autonomous Network Ecosystem.**

![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)
![Tests: 100% Passing](https://img.shields.io/badge/Tests-100%25%20Passing-success?style=for-the-badge)
![Compliance: ITU-T G.984](https://img.shields.io/badge/Compliance-ITU--T%20G.984-blue?style=for-the-badge)

---

## 🚀 1. التجربة الحية (Live Dashboard)
يمكنك معاينة لوحة التحكم التفاعلية لمركز العمليات (NOC) والخاصة بمحاكاة شبكة ولاية البيض عبر الرابط التالي:
🔗 **[👉 اضغط هنا للدخول إلى منصة A.S.M.A.A الحية](https://share.streamlit.io/)** 
*(ملاحظة: تعمل المنصة ببيانات محاكاة مشفرة لضمان سرية شبكة اتصالات الجزائر).*

---

## 📌 2. الرؤية العامة للمشروع (Executive Summary)
مشروع **"A.S.M.A.A"** هو نظام بيئي ذكي (AIOps) مصمم خصيصاً لتطوير البنية التحتية لشركة **اتصالات الجزائر (Algérie Télécom)**. 
يحول النظام شبكة الألياف البصرية من "نظام تفاعلي ينتظر شكاوى الزبائن" إلى **"شبكة استباقية ذاتية الشفاء" (Proactive Self-Healing Network)**، مما يوفر على الشركة ملايير الدنانير من تكاليف التدخلات الميدانية المتأخرة، ويرفع نسبة رضا الزبائن (QoS) إلى أقصى حد.

---

## ⚡ 3. المعمارية التقنية والوحدات (Core Architecture)
تم بناء المنصة وفق معايير الاتصالات الدولية مقسمة إلى 4 وحدات برمجية:

1. **`dashboard.py` (منصة العمليات الجغرافية):** واجهة ويب تفاعلية تدعم الخرائط الحقيقية (GIS) وأنظمة التنبيه اللحظي.
2. **`predictive_engine.py` (محرك الفيزياء الضوئية):** يحلل بيانات التيليمتري اللحظية (Rx Power dBm) ويتنبأ بانقطاع الألياف البصرية قبل حدوثه بـ 48 ساعة.
3. **`naseej_core.py` (معالج اللغة والإصلاح الآلي):** روبوت ذكاء اصطناعي يفهم اللهجة الجزائرية لإصلاح أعطال أجهزة المودم (Port Refresh) دون تدخل بشري (Zero-Touch).
4. **`test_engine.py` (نظام الفحص والموثوقية):** وحدة اختبارات آلية (Automated Unit Testing) لضمان دقة الخوارزميات الرياضية ومطابقتها لمعايير ITU-T.

---

## 🛡️ 4. الموثوقية ومعايير الاتصالات (Carrier Compliance)
* **المعايير الفيزيائية:** مطابقة تامة لبروتوكول **ITU-T G.984** الخاص بشبكات GPON.
* **بروتوكولات التحكم:** تدعم الهيكلة التكامل مع بروتوكولات (TR-069) و (SNMP v3).
* **الاختبارات الآلية:** اجتازت الخوارزمية 100% من اختبارات الإجهاد والدقة الرياضية.

### ⚙️ لتشغيل الاختبارات الآلية (Run Tests):
```bash
python -m unittest test_engine.py
