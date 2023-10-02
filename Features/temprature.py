def get_Temp():
    import requests
    from bs4 import BeautifulSoup
    from Body.Speak import Speak
    search = "temperature in bareta"
    url = f"https://www.google.com/search?q={search}"
    r  = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    Speak(f"current {search} is {temp}")
  
