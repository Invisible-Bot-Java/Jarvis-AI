from Features.Extra_Features import Tired
from Brain.AIBrain import ReplyBrain
from Features.Extra_Features.Screenshot import Screenshot
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Started The Jarvis : Wait For Few Seconds More")
from Main import MainTaskExecution

for i in range(3):
    Speak("Please Enter your Password Sir")
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("DataBase\\password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        Speak("Incorrect Password")
        print("Try Again")

def MainExecution():
    from Features.Intro import intro
    intro()
    import datetime
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        Speak("Good Morning  sir")
        Speak("I'm Jarvis, I'm Ready To Assist You Sir.")         
    elif hour >=12 and hour<=18:
        Speak("Good Afternoon  sir")
        Speak("I'm Jarvis, I'm Ready To Assist You Sir.") 
    else:
        Speak("Good Evening  sir")
        Speak("I am Jarvis, I'm Ready To Assist You Sir.") 
    
    
    
    
    

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "whatsapp message" in Data:
            pass

        elif "turn on the tv" in Data:# Specific COmmand
            Speak("Ok..Turning On The Android TV")

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)
            Speak(Reply)
        elif "screenshot" in Data:
           
            Screenshot()
            Speak("Screenshot Saved Sir")
        elif "change password" in Data:
            Speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("DataBase\\password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            Speak("Done sir")
            Speak(f"Your new password is {new_pw}")    
        elif "what is my internet speed." in Data or "net speed" in Data or "net " in Data or "internet speed" in Data: 
            Speak("Testing Internet Speed Sir")
            from Features.Internet_Speed import Int_Speed
            Int_Speed()
        elif "tired" in Data or "sad" in Data or "depressed" in Data:
            Speak("This Might Make You Feel Happy")
            Speak("Playing your favourite songs sir")
            from Features.Extra_Features.Tired import Tired_Exe
            Tired_Exe()
        elif "temp" in Data:
            from Features.temprature import get_Temp
            get_Temp()   
        elif "news" in Data or "News" in Data or "latest news" in Data:
            from Features.News import latestnews
            latestnews()  
        elif "wikipedia" in Data:
            from Features.Wiki_Search import Search_Wikipedia
            Search_Wikipedia(Data)   
        elif "google" in Data:
            from Features.Google_Search import Search_Google
            Search_Google(Data)                    
        elif "youtube" in Data:
            from Features.Yt_Search import Search_Youtube
            Search_Youtube(Data)   
        elif "stop video" in Data:
            from Features.Yt_Controls import Play_Video
            Play_Video()
        elif "volume up" in Data:
            from Features.Volume_Controls import volumeup
            Speak("Turning volume up,sir")
            volumeup()
                    
        elif "volume down" in Data:
            from Features.Volume_Controls import volumedown
            Speak("Turning volume down, sir")
            volumedown()                         
        elif "pause video" in Data:
            from Features.Yt_Controls import Pause_Video
            Pause_Video()  
        elif "the time" in Data:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            Speak(f"Sir, the time is {strTime}")      
        elif "Joke" in Data or "joke" in Data or "tell me a joke" in Data:
            from Features.Joke import Joke
            Joke()
        # elif "nasa" in Data or "NASA" in Data:
        
              
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

# def ClapDetect():

#     query = Tester()
#     if "True-Mic" in query:
#         print("")
        
#     else:
#         pass
 
MainExecution()
# I'd:              :itz_brar_.x
# Password: brarxx002