from utils import text_to_speech, speech_to_text


class Jarvis:
    
    def __init__(self):
        self.user_name = None
    
    def respond(self):
        pass
    
    def get_user_name(self):
        question = 'Comment vous appelez vous ?'
        text_to_speech(text=question, filename='user_name')
        voice_text = speech_to_text(question=question)
        self.user_name =  [x for x in voice_text.split() 
                           if all(y not in x.lower() for y in [
                               'je', 
                               'm\'appelle', 
                               'm\'',
                               'm', 
                               'appelle',
                               'mon',
                               'prenom',
                               'nom',
                               'est'
                               ])]
        self.user_name = ' '.join(self.user_name).strip()
        print(self.user_name)
        text_to_speech(text="Enchanté " + self.user_name + " Moi je m'appelle Jarviset", filename='user_name')
