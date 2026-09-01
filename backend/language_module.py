class LanguageModule:
    SUPPORTED_LANGUAGES = {
        "english": {"name": "English", "code": "en-US"},
        "tamil": {"name": "Tamil (தமிழ்)", "code": "ta-IN"},
        "hindi": {"name": "Hindi (हिन्दी)", "code": "hi-IN"}
    }

    @staticmethod
    def get_system_prompt(language):
        prompts = {
            "english": "You are a friendly college professor. Explain the topic in depth, providing detailed information and examples in English. Use simple but professional terms.",
            "tamil": "நீங்கள் ஒரு கனிவான கல்லூரி பேராசிரியர். கொடுக்கப்பட்ட தலைப்பை தமிழில் (Tamil) விரிவாகவும் தெளிவாகவும் உதாரணங்களுடன் விளக்குங்கள். முழுமையான வாக்கியங்களைப் பயன்படுத்தவும்.",
            "hindi": "आप एक मित्रवत कॉलेज प्रोफेसर हैं। विषय को हिंदी (Hindi) में विस्तार से, उदाहरणों के साथ समझाएं। स्पष्ट और पूर्ण वाक्यों का प्रयोग करें।"
        }
        return prompts.get(language.lower(), prompts["english"])

    @staticmethod
    def get_language_code(language):
        lang_info = LanguageModule.SUPPORTED_LANGUAGES.get(language.lower())
        return lang_info["code"] if lang_info else "en-US"
