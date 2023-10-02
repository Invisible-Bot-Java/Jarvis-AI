def Search_Youtube(query):
    from Body.Speak import Speak
    import webbrowser
    import pywhatkit

    Speak("This is what I found for your search!") 
    query = query.replace("youtube search","")
    query = query.replace("youtube","")
    query = query.replace("jarvis","")
    web  = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    Speak("Done, Sir")
              