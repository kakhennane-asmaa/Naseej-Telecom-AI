import time

# =====================================================================
# Project: Naseej-Telecom-AI
# Description: Automated Diagnostics & Self-Healing Network for Algérie Télécom
# Author: Asmaa Kakhennane & Engineering Team
# Wilaya Target: El Bayadh (Pilot Node)
# =====================================================================

class NaseejRouter:
    """
    Virtual representation of Algérie Télécom's Customer Premises Equipment (CPE).
    Simulates real-time telemetry: Ping, Bandwidth, Optical Power, and Connection State.
    """
    def __init__(self, client_name, wilaya):
        self.client_name = client_name
        self.wilaya = wilaya
        self.is_connected = True
        self.ping = 20          # ms (Normal baseline)
        self.speed = 100        # Mbps (FTTH standard tier)

    def check_status(self):
        time.sleep(1.5)
        if self.ping > 100 or self.speed < 10:
            return "⚠️ يوجد مشكل: بطء شديد في تدفق الإنترنت (High Latency / Bottleneck)."
        elif not self.is_connected:
            return "❌ المشكل: الخط مقطوع من السنترال الرئيسي (Fiber Link Down)."
        else:
            return "✅ الخط متصل وبسرعة ممتازة (100Mbps FTTH Active)."

    def auto_fix(self):
        time.sleep(1.5)
        self.ping = 20
        self.speed = 100
        self.is_connected = True
        return "✅ تم تحديث المنفذ (Port Refresh) وإعادة توجيه المسار وضبط الإشارة بنجاح!"


class NaseejAI_Agent:
    """
    Intelligent NLP-driven Customer Support & Automated Network Diagnostic Agent.
    Trained for Algerian localized vocabulary & network troubleshooting.
    """
    def __init__(self, router):
        self.router = router

    def chat(self):
        print("\n" + "="*50)
        print("🤖 نَسِيج: أهلا بكِ في خدمة زبائن اتصالات الجزائر المعتمدة على الذكاء الاصطناعي.")
        print(f"🤖 نَسِيج: مرحباً بالسيدة/الآنسة ({self.router.client_name}) من ولاية ({self.router.wilaya}).")
        print("🤖 نَسِيج: أنا في الخدمة، اسأليني أي شيء! (اكتبي 'خروج' للإغلاق)")
        print("="*50)
        
        while True:
            user_input = input("\nأنتِ (الزبونة): ").strip()
            
            if user_input == 'خروج':
                print(f"🤖 نَسِيج: شكراً لتواصلكِ معنا يا {self.router.client_name}. يومكِ سعيد في ولاية {self.router.wilaya}!")
                break
                
            # 1. القواميس المعرفية والهوية
            name_q = ["اسمك", "شكون انت", "من انت", "عرف بنفسك", "ما هو اسمك"]
            origin_q = ["من اين انت", "وين تسكن", "منين انت", "مكانك", "وين راك"]
            job_q = ["واش تخدم", "واش دير", "ما هي وظيفتك", "كيفاش تعاوني", "واش تقدر دير"]
            joke_q = ["نكتة", "ضحكني", "احكيلي نكتة", "قصة"]
            
            # 2. قواميس المحادثة والتحية
            greetings = ["سلام", "السلام عليكم", "مرحبا", "صباح الخير", "مساء الخير", "اهلا", "صحا"]
            chitchat = ["واش راك", "لاباس", "هل انت بخير", "كيف الحال", "راك مليح", "احوالك"]
            gratitude = ["شكرا", "يعطيك الصحة", "بارك الله فيك", "يرحم والديك", "صحيت", "شكرا جزيلا"]
            
            # 3. قواميس المشاكل التقنية لشبكة الاتصالات
            keywords_slow = ["ثقيلة", "ناقصة", "ضعيفة", "بطيئة", "عيانة", "تقطع"]
            keywords_cut = ["مقطوعة", "راحت", "ماكانش", "كوباولي", "البواطة الحمرا", "حمرة"]
            keywords_fiber = ["الياف", "فيبر", "مودام", "روتر", "4g", "idom", "ايدوم"]
            
            # ---------------- منطق التحليل والاستجابة الذكية ----------------
            
            if any(word in user_input for word in name_q):
                print("🤖 نَسِيج: أنا 'نَسِيج' (Naseej AI)، المساعد الذكي المطور لاتصالات الجزائر لحل المشاكل آلياً.")
                
            elif any(word in user_input for word in origin_q):
                print("🤖 نَسِيج: أنا نظام سحابي جزائري متواجد في كافة الولايات لخدمتكم من البيض حتى العاصمة!")
                
            elif any(word in user_input for word in job_q):
                print("🤖 نَسِيج: وظيفتي فحص خط الإنترنت عن بُعد، وإصلاح الأعطال تلقائياً على مدار الساعة 24/7.")
                
            elif any(word in user_input for word in joke_q):
                print("🤖 نَسِيج: ههه اسمعي هذي: واحد قال للمودم ديالو علاش راك طافي؟ قالو: راني فاقد الإشارة وعايش بلا كونيكسيون! 😂")

            elif any(word in user_input for word in greetings):
                print(f"🤖 نَسِيج: وعليكم السلام ورحمة الله! أهلاً بكِ وبكل ناس ولاية {self.router.wilaya}. تفضلي كيف أساعدك؟")
            
            elif any(word in user_input for word in chitchat):
                print("🤖 نَسِيج: أنا بأفضل حال والحمد لله! أنظمتي تعمل بكفاءة 100%. كيف هي حالة الإنترنت لديكِ اليوم؟")
                
            elif any(word in user_input for word in gratitude):
                print(f"🤖 نَسِيج: العفو يا {self.router.client_name}! هذا واجبي. اتصالات الجزائر دائماً في خدمتكم.")
                
            elif any(word in user_input for word in keywords_slow):
                print("🤖 نَسِيج: تم استلام البلاغ عن بطء السرعة. سأقوم بفحص واختبار الروتر فوراً.")
                self.troubleshoot(issue_type="slow")
                
            elif any(word in user_input for word in keywords_cut):
                print("🤖 نَسِيج: تم رصد انقطاع الاتصال. سأقوم بتشخيص الإشارة وإعادة التوصيل آلياً.")
                self.troubleshoot(issue_type="cut")
                
            elif any(word in user_input for word in keywords_fiber):
                print("🤖 نَسِيج: خدمة الألياف البصرية (FTTH Idoom Fibre) توفر استقراراً فائقاً وسرعات تصل لـ 300Mbps.")
                
            else:
                print("🤖 نَسِيج: عذراً، لم أفهم طلبكِ بدقة. يمكنكِ سؤالي عن: (حالة الخط، سرعة الإنترنت، الأعطال التقنية).")

    def troubleshoot(self, issue_type):
        if issue_type == "slow":
            self.router.speed = 5
            self.router.ping = 200
        elif issue_type == "cut":
            self.router.is_connected = False
            
        print(f"🤖 نَسِيج: ⏳ جاري الاتصال بروتر الزبونة {self.router.client_name} في ولاية {self.router.wilaya}...")
        
        status = self.router.check_status()
        print(f"📊 التقرير التقني: {status}")
        
        if "مشكل" in status or "مقطوع" in status:
            print("🤖 نَسِيج: ⚙️ الذكاء الاصطناعي يتدخل لمعالجة الخلل ذاتياً...")
            fix_result = self.router.auto_fix()
            print(f"🤖 نَسِيج: {fix_result}")
            print(f"🤖 نَسِيج: تم استرجاع الخدمة بنجاح وبأقصى سرعة!")

# ----------- Main Execution Block -----------
if __name__ == "__main__":
    pilot_router = NaseejRouter(client_name="أسماء", wilaya="البيض")
    ai_system = NaseejAI_Agent(router=pilot_router)
    ai_system.chat()
