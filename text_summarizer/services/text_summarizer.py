from services.base_summarizator.summarizator import Summarizer

class TextSummarizer(Summarizer):
    
    def __init__(self):
        super().__init__()
        
    def text_summarize(self, text_to_summarize: str) -> dict[str, str]:
        summarize_data: dict[str, str] = self.summarize(text_query=str(text_to_summarize))
    
        return summarize_data
