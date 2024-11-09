import speech_recognition as sr

def transcribe_audio(file_path, language):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_vosk(audio_data=audio_data, language=language)
            return text
    except sr.UnknownValueError:
        return ''
    except sr.RequestError as e:
        return ''
