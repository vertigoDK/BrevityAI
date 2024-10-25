import logging
from dotenv import load_dotenv
from django.conf import settings

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
class BaseSummarizer:
    def __init__(self):
        try:
            if not settings.configured:
                settings.configure(MODEL_NAME='gemini-1.5-flash') 
            self.model = GoogleGenerativeAI(model=settings.MODEL_NAME)
        except Exception as e:
            logging.error(f"Ошибка инициализации модели: {str(e)}")
            raise RuntimeError("Не удалось инициализировать модель.") from e


class Summarizer(BaseSummarizer):
    """
    Класс для генерации и анализа суммаризованного текста.
    """
    
    def __init__(self):
        super().__init__()
    
    def generate_summary(self, text_to_summarize: str) -> str:
        """
        Создаёт запрос для генерации суммаризированного текста.
        """
        if not text_to_summarize.strip():
            raise ValueError("Входной текст не может быть пустым.")
        
        try:
            prompt = ChatPromptTemplate.from_messages([
                ('system', 'You need to summarize this text. Суммаризируй на том же языке что тебе отдают текст'),
                ('human', '{text_to_summarize}')
            ])
            
            chain = prompt | self.model
            return chain.invoke({
                "text_to_summarize": text_to_summarize
            })
        
        except Exception as e:
            logging.error(f"Ошибка при запросе к модели: {str(e)}")
            raise RuntimeError("Не удалось сгенерировать суммаризацию.") from e
    
    def summarize(self, text_query: str) -> dict[str, str]:
        """
        Возвращает длину текста до и после суммаризации и сам суммаризованный текст.
        """
        try:
            summarized_text = self.generate_summary(text_to_summarize=text_query)
            without_summarize_len = len(text_query)
            
            return {
                'len_before_summarize': without_summarize_len,
                'len_after_summarize': len(summarized_text),
                'text_before_summarize': text_query,
                'summarized_text': summarized_text
            }
        
        except ValueError as ve:
            logging.warning(f"Предупреждение: {str(ve)}")
            return {
                'error': str(ve),
                'len_before_summarize': 0,
                'len_after_summarize': 0,
                'summarized_text': ''
            }
        
        except Exception as e:
            logging.error(f"Ошибка суммаризации: {str(e)}")
            return {
                'error': "Ошибка во время выполнения суммаризации.",
                'len_before_summarize': 0,
                'len_after_summarize': 0,
                'summarized_text': ''
            }


if __name__ == '__main__':
    summarizer = Summarizer()
    
    result = summarizer.summarize("""Искусственный интеллект (ИИ) — это область компьютерных наук, которая занимается созданием машин и программ, способных выполнять задачи, требующие человеческого интеллекта. Такие задачи включают распознавание речи, понимание естественного языка, принятие решений, обучение и планирование. За последние десятилетия ИИ продвинулся далеко за пределы первоначальных теоретических исследований и стал частью повседневной жизни: от виртуальных помощников, таких как Siri и Alexa, до самоуправляемых автомобилей и умных городов. Несмотря на огромный прогресс, ИИ сталкивается с вызовами в таких областях, как этика, приватность данных и зависимость от машин. В будущем развитие ИИ будет определяться тем, как хорошо человечество сможет сбалансировать его возможности и риски.""")
    
    print(result)