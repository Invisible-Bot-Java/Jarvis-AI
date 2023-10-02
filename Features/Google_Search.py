def Search_Google(query):
    from Body.Speak import Speak
    import webbrowser
    import pywhatkit        
    import wikipedia as googleScrap
    query = query.replace("jarvis","")
    query = query.replace("google search","")
    query = query.replace("google","")
    Speak("This is what I found on google")

    try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            Speak(result)

    except:
            Speak("No speakable output available")
         