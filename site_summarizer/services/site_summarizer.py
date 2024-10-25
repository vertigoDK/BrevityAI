import requests
from bs4 import BeautifulSoup
from services.base_summarizator.summarizator import Summarizer

class SiteSummarizerTools:
    @staticmethod
    def check_url_exists(url: str) -> bool:
        """
        Проверяет, существует ли ссылка (возвращает статус 200).
        """
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False


class SiteSummarizer(Summarizer):
    
    def __init__(self):
        super().__init__()
    
    def _get_content_from_link(self, link: str) -> str:
        """
        Получает контент по ссылке, если она существует.
        Возвращает контент страницы, ограниченный 100 000 символами.
        """
        # Проверяем, существует ли ссылка
        if not SiteSummarizerTools.check_url_exists(url=link):
            return "Error: URL does not exist or cannot be reached."
        
        try:
            # Отправляем запрос и получаем HTML-контент
            response = requests.get(link)
            if response.status_code != 200:
                return "Error: Unable to retrieve content."
            
            # Парсим HTML-контент с помощью BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Извлекаем весь текст с веб-страницы
            page_content = soup.get_text(separator=' ', strip=True)
            
            # Ограничиваем контент 100 000 символами
            if len(page_content) > 100000:
                return page_content[:100000] + "..."
            
            return page_content
        except Exception as e:
            return f"Error while processing the URL: {str(e)}"

    def summarize_site(self, link) -> dict[str, str]:
        try:
            text_content: str = self._get_content_from_link(link=link)
            
            result: dict[str,str] = self.summarize(text_query=text_content)
            
            return result
        except Exception as e:
            return f"Error whiile processing {e}"