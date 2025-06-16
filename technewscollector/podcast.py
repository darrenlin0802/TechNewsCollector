from gtts import gTTS


def text_to_speech(text: str, output_path: str, lang: str = 'en') -> None:
    """Convert text to speech and save as an MP3 file."""
    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)
