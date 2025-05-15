import random

class ChatbotService:
    def __init__(self):
        self.responses = [
            "I understand you're asking about {}, but I'm a basic medical chatbot and can't provide specific medical advice. Please consult with a healthcare professional for accurate information.",
            "While I can't give medical advice, it's generally good to maintain a healthy lifestyle with a balanced diet and regular exercise. If you're concerned about {}, please speak to a doctor.",
            "I'm sorry, but I can't diagnose or treat medical conditions. If you're experiencing symptoms related to {}, it's best to consult with a healthcare provider.",
            "Health concerns about {} are common. However, for personalized medical advice, it's crucial to consult with a qualified healthcare professional.",
            "I'm not able to provide specific information about {}. For the most accurate and up-to-date medical information, please refer to reputable health organizations or consult your doctor."
        ]

    async def generate_response(self, message: str) -> str:
        # This is a simple mock-up. In a real scenario, you'd integrate with a proper LLM or medical knowledge base.
        topic = message.lower().split()[-1]  # Simplistic way to extract the topic
        response = random.choice(self.responses).format(topic)
        return response