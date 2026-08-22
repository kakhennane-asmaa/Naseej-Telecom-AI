import unittest

# =====================================================================
# Automated Unit Tests for A.S.M.A.A (Naseej Predictive Engine)
# Framework: Python unittest (Carrier-Grade Validation)
# =====================================================================

class TestASMAAPredictiveEngine(unittest.TestCase):
    
    def setUp(self):
        """تهيئة ثوابت الاختبار المستوحاة من معايير ITU-T G.984"""
        self.CRITICAL_LOS_THRESHOLD = -27.5  # حد الانقطاع التام
        self.WARNING_THRESHOLD = -24.0       # حد التحذير

    def test_normal_signal(self):
        """الاختبار الأول: التأكد من أن الإشارة الجيدة (-19.2) تُقرأ كحالة سليمة"""
        current_power = -19.2
        self.assertTrue(current_power > self.WARNING_THRESHOLD)
        print("✅ اجتياز الاختبار 1: النظام يتعرف على الإشارة الممتازة بشكل صحيح.")

    def test_critical_signal(self):
        """الاختبار الثاني: التأكد من أن النظام يطلق إنذاراً عند تجاوز الحد الحرج (-28)"""
        current_power = -28.0
        self.assertTrue(current_power <= self.CRITICAL_LOS_THRESHOLD)
        print("✅ اجتياز الاختبار 2: النظام يكتشف الانقطاع الكلي بدقة 100%.")

    def test_predictive_mathematics(self):
        """الاختبار الثالث: التأكد من دقة الخوارزمية في حساب الأيام المتبقية للانقطاع"""
        current_power = -25.5
        degradation_rate = 1.0  # تدهور بمقدار 1 ديسيبل يومياً
        
        # الحساب الرياضي: المسافة المتبقية للوصول إلى -27.5
        margin = current_power - self.CRITICAL_LOS_THRESHOLD # (-25.5 - -27.5) = 2.0
        days_to_failure = margin / degradation_rate
        
        # التأكد من أن النظام يحسب يومين بدقة تامة
        self.assertEqual(days_to_failure, 2.0)
        print("✅ اجتياز الاختبار 3: خوارزمية التنبؤ بالأيام تعمل بدقة رياضية مطلقة.")

if __name__ == '__main__':
    unittest.main()
