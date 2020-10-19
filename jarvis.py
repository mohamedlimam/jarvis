import time
from utils import text_to_speech, speech_to_text, is_keywords


class Jarvis:
    
    def __init__(self):
        self.user_name = ''
    
    def respond(self, voice_text):
        print(voice_text)
        if voice_text:
            if is_keywords(  # check stop words
                text=voice_text.lower(), 
                key_words=['comment', 'quel', 'ton', 'tu', 'vous']
                ) and is_keywords(  # check important words
                    text=voice_text.lower(),
                    key_words=['appelle', 'prenom', 'prénom', 'nom']
                ):
                self.ask_my_name()
    
    def get_user_name(self):
        question = 'Comment vous appelez vous ?'
        voice_text = speech_to_text(question=question)
        if voice_text is not None:
            self.user_name =  [x for x in voice_text.split() 
                            if x.lower() not in [
                                'je', 
                                'm\'appelle', 
                                'm\'',
                                'm', 
                                'appelle',
                                'mon',
                                'prenom',
                                'nom',
                                'est'
                                ]
                            ]
            self.user_name = ' '.join(self.user_name).strip()
        print(self.user_name)
        text_to_speech(text="Enchanté " + self.user_name + " Moi je m'appelle Jarviset", filename='vocal_assistant_name')
    
    def ask_my_name(self):
        text_to_speech(text="Alors, je m'appelle Jarviset", filename='vocal_assistant_name')
        
    def vocal_assistant(self):
        while True:
            voice_text = speech_to_text(question='Comment puis-je vous aider ?')
            self.respond(voice_text=voice_text)
            time.sleep(1)