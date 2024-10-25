from site_summarizer.services.site_summarizer import SiteSummarizer


if __name__ == '__main__':
    sSummarizer = SiteSummarizer()
    
    response = sSummarizer.summarize_site('https://pushkinlibrary.kz/ru/allnewsru/498-legendy-i-skazaniya-vostochnogo-kazakhstana-prezentatsiya-sbornika.html')
    
    print(response)