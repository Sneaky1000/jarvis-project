# jarvis/audio/listener.py
import speech_recognition as sr

class AudioListener:
    def __init__(self, device_index = None):
        """
        device_index: If specified, tells SpeechRecognition which microphone device to use.
        """
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 1.0

        # If device_index is None, the default system mic is used.
        # Otherwise, we explicitly set which mic to open.
        self.microphone = sr.Microphone(device_index = device_index)

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio_data = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Error connecting to the speech recognition service.")
            return None
