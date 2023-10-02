from Body.Speak import Speak
import pyjokes
def Joke():
    Joke = pyjokes.get_joke()
    Speak(Joke)