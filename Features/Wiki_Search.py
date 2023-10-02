def Search_Wikipedia(query):
    import wikipedia
    from Body.Speak import Speak
    Speak("Searching from wikipedia....")
    query = query.replace("wikipedia","")
    query = query.replace("search wikipedia","")
    query = query.replace("jarvis","")
    results = wikipedia.summary(query,sentences = 2)
    Speak("According to wikipedia.." + results)
        
        
        

# elif "youtube" in query:
#                     from Features.SearchNow import searchYoutube
#                     searchYoutube(query)
                    
#                 elif "wikipedia" in query:
#                     from Features.SearchNow import searchWikipedia
#                     searchWikipedia(query)        