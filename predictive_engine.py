import time
import math

# =====================================================================
# Module: Optical Telemetry & Predictive Maintenance Engine
# Standard: ITU-T G.984 (GPON Physical Layer Compliance)
# Target Node: El Bayadh FTTH OLT-01 (Sector 04)
# =====================================================================

class OpticalLinkDiagnostics:
    """
    Analyzes physical layer optical power (dBm) and predicts link failures
    based on ITU-T G.984 GPON optical budget thresholds.
    """
    CRITICAL_LOS_THRESHOLD = -27.5  # dBm: حد انقطاع الإشارة التام
    WARNING_THRESHOLD = -24.0       # dBm: بداية مرحلة الخطر

    def __init__(self, subscriber_id, initial_rx_power=-18.5):
        self.subscriber_id = subscriber_id
        self.rx_power_history = [initial_rx_power] # سجل قراءات الإشارة

    def simulate_telemetry_stream(self, days=7, degradation_rate=1.2):
        """
        محاكاة قراءات القدرة الضوئية (Rx Power) القادمة من روتر الزبون على مدار أسبوع
        degradation_rate: معدل تدهور الإشارة يومياً بوحدة dBm نتيجة خلل فيزيائي في الكابل.
        """
        print(f"📡 بدء جمع وتحليل بيانات التيليمتري الضوئية للمشتركة: {self.subscriber_id}...")
        current_power = self.rx_power_history[0]
        
        for day in range(1, days + 1):
            # محاكاة انخفاض الإشارة تدريجياً
            current_power -= degradation_rate
            self.rx_power_history.append(round(current_power, 2))
            time.sleep(0.4)
            print(f"  📅 اليوم {day:02d}: القدرة الضوئية المستقبلة (Rx Power) = {current_power:.2f} dBm")

    def run_predictive_ai(self):
        """
        خوارزمية التنبؤ الرياضي: حساب ميل الانحدار وتحديد موعد الانهيار قبل وقوعه
        """
        print("\n" + "="*55)
        print("🧠 [Naseej Predictive AI] جاري تحليل معدل التدهور الضوئي...")
        print("="*55)
        time.sleep(1)

        # حساب معدل التغير اليومي (Delta dBm / Day)
        recent_readings = self.rx_power_history[-4:]
        daily_drop = (recent_readings[0] - recent_readings[-1]) / (len(recent_readings) - 1)
        current_power = self.rx_power_history[-1]

        print(f"📊 القراءة الحالية: {current_power} dBm")
        print(f"📉 معدل التدهور اليومي: {daily_drop:.2f} dBm/يوم")

        if current_power <= self.CRITICAL_LOS_THRESHOLD:
            print("🚨 حالة حرجة: الخط منقطع فعلياً (Total Signal Loss).")
            return

        if current_power <= self.WARNING_THRESHOLD:
            # حساب الأيام المتبقية قبل الانقطاع التام
            power_margin = current_power - self.CRITICAL_LOS_THRESHOLD
            days_to_failure = math.floor(power_margin / daily_drop)

            print(f"\n⚠️ [تنبيه استباقي]: رصد تدهور فيزيائي سريع في الألياف البصرية!")
            print(f"⏳ التنبؤ: سينقطع الاتصال كلياً خلال ({days_to_failure} أيام) إذا لم يتم التدخل.")
            
            # توليد تذكرة صيانة موجهة لفرق اتصالات الجزائر الميدانية
            self.generate_dispatch_ticket(days_to_failure, current_power)
        else:
            print("✅ حالة الألياف البصرية مستقرة وضمن المعايير القياسية.")

    def generate_dispatch_ticket(self, days_left, power_level):
        print("\n" + "-"*50)
        print("🎫 [نظام أتمتة الصيانة - اتصالات الجزائر]")
        print(f"📍 الوحدة الميدانية: ولاية البيض (Node: EL-BAYADH-OLT-04)")
        print(f"👤 المشتركة: {self.subscriber_id}")
        print(f"🔍 التشخيص التقني: احتمال وجود التواء حاد (Macro-bend) أو غبار في علبة التوزيع (FAT Box).")
        print(f"⚡ الإجراء المطلوب: فحص وتنظيف نقطة التوصيل قبل انقضاء مهلة ({days_left}) أيام.")
        print(f"📌 مستوى الأولوية: قصوى (High Priority - Proactive Dispatch)")
        print("-"*50)


# ----------- تنفيذ الاختبار الميداني -----------
if __name__ == "__main__":
    # محاكاة خط مشترك للألياف البصرية في ولاية البيض
    asmaa_line = OpticalLinkDiagnostics(subscriber_id="FTTH-DZ-BAYADH-0042", initial_rx_power=-19.0)
    
    # 1. محاكاة وصول بيانات الشبكة لمدة 5 أيام مع وجود تآكل فيزيائي
    asmaa_line.simulate_telemetry_stream(days=5, degradation_rate=1.4)
    
    # 2. تشغيل محرك التنبؤ الذكي
    asmaa_line.run_predictive_ai()
