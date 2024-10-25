from pytube import YouTube
from pydantic import BaseModel, Field
from typing import List, Optional

class Error(BaseModel):
    error_name: str = Field(..., description='Название ошибки')


class Result(BaseModel):
    errors: List[Error] = Field(default_factory=list, description="Список ошибок")
    result: Optional[str] = Field(None, description="Поле с результатом")


class YouTubeSummarizer:
    def __init__(self):
        pass

    def get_subtitles_from_youtube(self, link: str, language_code: str = 'en') -> Result:
        """
        Fetches subtitles from a YouTube video.

        Parameters:
            link (str): URL of the YouTube video.
            language_code (str): Language code for the subtitles (default is 'en').

        Returns:
            Result: An instance of Result containing subtitles or errors.
        """
        try:
            # Initialize YouTube object
            yt = YouTube(url=link)
            
            # Get available captions
            captions = yt.captions

            # Output available captions for debugging
            print("Available captions:")
            for caption in captions:
                print(caption)

            # Use dictionary-style access instead of deprecated method
            if language_code in captions:
                caption = captions[language_code]
                subtitle_text = caption.generate_srt_captions()
                return Result(result=subtitle_text)
            else:
                return Result(errors=[Error(error_name="No subtitles available for the selected language.")])
        
        except Exception as e:
            # Handle other potential errors (e.g., network errors, invalid URL)
            return Result(errors=[Error(error_name=str(e))])


if __name__ == "__main__":
    yt_summarizer = YouTubeSummarizer()
    link = "https://www.youtube.com/watch?v=your_video_id"  # Replace with your video link
    result = yt_summarizer.get_subtitles_from_youtube(link, language_code='en')

    if result.result:
        print("Subtitles:", result.result)
    else:
        print("Errors:")
        for error in result.errors:
            print(error.error_name)
