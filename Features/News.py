def latestnews():
    from Body.Speak import Speak
    from Body.Listen import MicExecution
    fileopen = open("Data\\News_API.txt","r")
    API = fileopen.read()
    fileopen.close()
    
    
    
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=" + API,
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=" + API,
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=" +API,
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=" + API,
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=" + API,
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=" + API
}

    import time

    import requests
    import json
    content = None
    url = None
    Speak("Which field news do you want to Listen Sir :")  
    print("[business] , [health] , [technology], [sports] , [entertainment] , [science]")
   
    z = MicExecution()
    field = z.lower()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            break
        else:
            
            
            url = True
            
    if url is True:
        Speak("Please Choose a valid News Field Sir")
        time.sleep(1)
        
        
    
    news = requests.get(url).text
    news = json.loads(news)
    Speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
       
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")
        time.sleep(5)
        Speak("Do you want to listen more news sir")
        a = MicExecution()
        if "yes" in a or "sure" in a:
            pass
        elif "no" in a:
            break
        else:
            break
    Speak("thats all")