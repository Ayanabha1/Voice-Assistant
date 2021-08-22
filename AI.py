import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from datetime import date
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
import random
from selenium.webdriver import ActionChains
import psutil
from pynput.keyboard import Key,Controller

keyboard = Controller()
email_id = "abc@gmail.com" #Enter your mail id
password = "12345678" #Enter your password
who_are_you = ['who are you','what is you','are you alive']

made = ['who made you' , 'who developed you' , 'who created you']

sleep = ['sleep', 'good night', 'quit', 'sign off', 'sign out','goodbye']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
emails = {"abc": "abc@gmail.com",
          "def": "def@gmail.com",
          "ghi": "ghi@gmail.com",
          "jkl": "jkl@gmail.com",
          "mno": "mno@gmail.com"
        }

user_main = "Ayanabha"

west_bengal = ['west bengal', 'my state']

how_are_you = ['how are you', 'how do you do', 'how you doing']

how_i_am = ['i am good', 'i am fine', 'all is good', 'never felt better',
            "can't be better", 'never felt like this before', 'good', 'fine','i am good too','doing well']

yes = ['yes','yeah','hell yeah','ha','hmm','sure']

thanks = ['thank you', 'thanks']

hi = ['hello', 'hi', 'hell yeah','yo','hai','hey']

greet_back = {'french':'bonjour','spanish':'hola','russian':'Zdravstvuyte', 'chinese':'Nǐn hǎo','italian':'salve','japanese':'Konnichiwa','german':'Guten Tag', 'portugese':'Olá','korean':'Anyoung haseyo','hindi':'namaste','bengali':'namaskar'}

add = ['addition', 'add', 'sum']

math = ['+', '-', '*', '/', 'log', 'ln']

sleep = ['sleep', 'goodbye','ok go to sleep','sign off', 'quit', 'take rest', 'take break', 'break','take a break', 'ok quit','go to sleep']

sleep_movie = [ 'i will do ', ' i will do that myself ' , " you don't have to bother" , "don't bother" , 'sleep' , 'quit ' , 'i will search myself']

covid = ['covid-19','covid 19','covid','corona','coronavirus','pandemic','epidemic','covid cases','coronavirus cases','covid-19 cases']

wow = ['wow','wonderful','excelent','fabulous','mindblowing','good job','good','bravo','bah','ok']

shut_down = ['shut down','turn off','turn of','shut down my pc','shut down my laptop','shut down my system','turn off my pc','turn off my system','turn off my laptop''turn off my computer','turn off pc','turn off laptop','turn off computer','turn off system']

close = ['close','turn off','shut down']

browser = ['chrome','internet explorer','firefox','browser']

open_now = ['open','start','initiate']

games = ['Watch dogs 2' , 'Detroit Becoming Human','Gta 5']

query_history = ['query','history','queries','query history']

leave = ['nevermind','leave it','leave','sorry']

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.operation_timeout = 5
        r.energy_threshold = 5000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Something went wrong ... try saying it again")
        return "None"
    return query

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good morning {user_main}")
    elif hour >= 12 and hour < 16:
        speak(f"Good afternoon {user_main}.")
    else:
        speak(f"Good evening {user_main}.")
    speak("I am your virtual voice assistant.")
    speak("What can I do for you?")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', '123') // enter your email id here
    server.sendmail('abc@gmail.com', to, content)
    server.close()

def Netflix():

    try:
        driver = webdriver.Chrome('F:\chromedriver.exe')


        driver.get('https://www.netflix.com/')

        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()

        driver.find_element_by_xpath('//*[@id="id_userLoginId"]').send_keys(email_id)

        driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)


        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button').click()

        driver.maximize_window()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div').click()
        time.sleep(5)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[1]/button').click()

        except Exception as e:
            print(e)

        


        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/button').click()

        
        speak("What do you want to watch?")
        movie_netflix = takecommand()


        keyboard.type(f"{movie_netflix}")

        time.sleep(2)

        image_netflix = driver.find_element_by_xpath('//*[@id="title-card-0-0"]/div[1]/a/div[1]/img')

        actions = ActionChains(driver)

        time.sleep(1)
        actions.move_to_element(image_netflix).click().perform()
        speak("Do you want to watch now or add to your list? ")
        driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[2]/div/button').click()
        
        decision = takecommand()

        if 'watch' in decision:
            try:
                play = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[2]/a/button')
                actions.move_to_element(play).click().perform()
                speak(f"Enjoy watching {movie_netflix}")
            except Exception as e:
                driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/div/div[1]/div[2]/a[2]/button').click()

            keyboard.press(Key.space)
            keyboard.release(Key.space)
            speak("Do you want to set a timer?")
            timer_netflix_watch = takecommand() 
            
            if timer_netflix_watch in yes:

                speak("please say it in minutes...")
                time_to_remain_slept = int(takecommand())
                speak("ok")
                keyboard.press(Key.space)
                keyboard.release(Key.space)
                time.sleep(60*time_to_remain_slept)
                speak(f"{time_to_remain_slept} minutes elasped ")

            elif "no" in timer_netflix_watch:
                speak("Ok")
                keyboard.press(Key.space)
                keyboard.release(Key.space) 

            
        elif 'add' in decision:

            addtolist = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/div/div[1]/div[1]/div/button')
            actions.move_to_element(addtolist).click().perform()
            speak(f'{movie_netflix} added to list successfully')
            driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div[2]/div[2]/svg').click()
            driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[1]/div/div[1]/ul/li[6]/a').click()

        elif 'exit' in decision:

            driver.close()
    
    except Exception as e :

        print(e)
        speak("Looks like internet connection is low.")







def log_query():
    if log_subject != "None":
        with open("log_query.txt", "a") as f:
            f.write(
                f"User searched : {log_subject} ,at {datetime.datetime.now().strftime('%H:%M:%S')} \n")


def get_data():
    myHtmldata = requests.get(f"https://www.worldometers.info/coronavirus/country/{place}/").text
    soup = BeautifulSoup(myHtmldata,'html.parser')
    mystr = ""
    for div in soup.find_all('div', {'class':'maincounter-number'}):
        mystr += div.get_text()
    cases = mystr.split("\n")[1]
    deaths = mystr.split("\n")[3]
    recoveries = mystr.split("\n")[5]
    print(f"Total covid cases in {place} are {cases}")
    print(f"Total deaths in {place} are {deaths}")
    print(f"Total recoveries in {place} are {recoveries}")
    speak(f"Total covid cases in {place} are {cases}")
    speak(f"Total deaths in {place} are {deaths}")
    speak(f"Total recoveries in {place} are {recoveries}")





def del_query():
    with open('log_query.txt','w') as f:
        f.write("")



def battery():
    
    battery = psutil.sensors_battery()
    
    plugged = battery.power_plugged

    percent = int(battery.percent)

    plugged = "plugged in" if plugged else "not plugged in"

    if percent <= 20 :
        speak(f"Battery percentage is {percent}%")
        speak(f"and your system is {plugged}")
        speak("You should use the power adapter")
    
    else:
        speak(f"Battery percentage is {percent}% and your system in {plugged}")

runs = 0
choice = 0
wicks = 0
overs = 0

class game_info:
    chances = wicks
    run = runs
    ch = choice
    ov = overs*6

    def __init__(self, name):
        self.name = name

    def speakdetails(self):
        print(
            f"********{self.name}********\n    Runs scored = {self.run}\n    Wickets remaining = {self.chances}")


p1 = game_info("player1")
p2 = game_info("computer")

target = 0

def game(t1, t2):

    if (t1.chances == 0):
        speak(f"*************{t2.name}'s turn*************")
        speak(F"Target run = {t1.run + 1}")

    if t1.ov == overs:
        speak(f"*************{t1.name}'s turn*************")

    t1.ch = 0
    t2.ch = 0
    if (t1.chances > 0) and (t1.ov > 0):

        if (t1.name == "player1"):

            speak(f"{t1.name}: Swing your bat :\t")
            t1.ch = int(takecommand())
            t2.ch = random.randint(0, 6)

        else:

            speak(f"{t2.name}: Throw the ball :\t")
            t2.ch = int(takecommand())

            t1.ch = random.randint(0, 6)

        if (t1.ch == t2.ch):

            speak(
                f"{t1.name} chose {t1.ch} and {t2.name} chose {t2.ch}\nIt is an out")
            t1.chances = t1.chances - 1
            speak(t1.chances)

        elif t1.ch <= 6 and t1.ch >= 0:

            t1.run = t1.run + t1.ch
            speak(f"{t1.name} chose {t1.ch} and {t2.name} chose {t2.ch}\n")
            speak(f"{t1.name}'s Run = {t1.run}")
            speak(f"{t2.name}'s Run = {t2.run}")

        t1.ov = t1.ov - 1

        if ((t1.chances == 0) and ((t2.chances != 0)) and (t1.ov == 0)):
            speak(f"***********{t2.name}***********")
            speak(f"Target score = {t1.run + 1}")

        

        game(t1, t2)

    if (t2.chances > 0) and (t2.ov > 0):
        game(t2, t1)

    


def toss():
    toss_dec = random.randint(1, 2)
    if toss_dec == 2:
        speak(f"{p2.name} has won the toss")
        time.sleep(1)
        game(p2, p1)
    else:
        speak(f"{p1.name} has won the toss")
        time.sleep(1)
        game(p1, p2)


if __name__ == "__main__":

    wishme()

    while True:
        query = takecommand().lower()
        log_subject = query.capitalize()
        log_query()
        



        


        # Logic for excecuting tasks based on query

        if 'wikipedia' in query:
            try:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Something went wrong......Try again")
        
        
        elif "exit" in query:
            driver = webdriver.Chrome('F:\chromedriver.exe')
            driver.close()
        elif "fun" in query:
            spam()
        elif query in wow:
            speak("Okay")

        elif "mark" in query:
            speak("Present sir...")
        elif 'close' in query and 'browser' in query:
            try:
                os.system("taskkill /im chrome.exe /f")
                speak("Done")

            except Exception as e:
                print(e)
                speak("No browser is open")

        elif 'close' in query and 'netflix' in query:
            try:
                os.system("taskkill /im chrome.exe /f")
                speak("Done")
            except Exception as e:
                speak("Netflix is not opened")    
                
        elif 'class' in query:
            query = query.replace("initialize")

        elif ("hand" in query) or ("cricket" in query):
            speak("Let's begin")
            speak("Enter the number of overs:\t")
            overs = int(takecommand())
            speak("Enter the number of wickets:\t")
            wicks = int(takecommand())
            toss()
            speak("\n\n\n**************Results on your screen**************")

            p1.speakdetails()
            print("\n")
            p2.speakdetails()

            if (p1.run)>(p2.run):
                speak(f"{p1.name} won the game")
            else:
                speak(f"{p2.name} won the game")
            
            
        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com/")
            speak("Opening Youtube")
            speak("What do you want to search ?")
            search_y = takecommand()
            if 'channel' in search_y:
                search_y = search_y.replace("channel", "")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={search_y}&sp=EgIQAg%253D%253D")
                speak(f"searching {search_y} in Youtube Channels")
            else:
                webbrowser.open(
                    f'https://www.youtube.com/results?search_query={search_y}')
                speak(f"searching {search_y} in Youtube")
    
        
        elif 'stackoverflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")
            speak("Opening Stackoverflow.com")


        elif 'prime music' in query:
            webbrowser.open_new_tab('https://music.amazon.in/my/songs')
            speak("opening amazon prime music.")

        elif 'physics wala' in query:
            webbrowser.open_new_tab("physicswallahalakhpandey.com")
            speak("Opening")

        elif query in thanks:
            speak("Your welcome")

        elif query in hi:
            x = random.choice(list(greet_back.items()))
            y = list(x)
            speak(f"{y[1]}")
            speak(f"That's hello in {y[0]}")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ADMIN\\Downloads\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Here you go")
            speak("Let's enjoy the song togather")

        elif query in how_are_you:
            speak('I am good . What about you')

        elif 'battery' in query:
            battery()

        elif "open" and "queries" in query:
            speak("ok")
            os.open('log_query.txt')

        elif "delete" and "queries" in query:
            speak("Are you sure?")
            sure_del = takecommand()
            if sure_del in yes:
                speak("Ok")
                speak("Delete all queries.")
                del_query()
            else:
                speak("Ok. Nevermind.")

        elif query in how_i_am:
            speak('glad to hear it.')

        elif 'whatsapp' in query:
            try:
                driver = webdriver.Chrome('F:\chromedriver.exe')
                driver.get('https://web.whatsapp.com/')
                driver.maximize_window()
                speak("Scan the QR code shown in the screen.")
                speak("I'll wait for 5 seconds")
                time.sleep(5)
                speak("Do you want to send any message?")
                what_ques = takecommand()
                if 'yes' in what_ques:
                    try:
                        speak("Whom do you want to send the messege?")
                        name_w = takecommand()
                        speak("What is the messege?")
                        mess_w = takecommand()
                        count = 1

                        user_w = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[1]/span/span')
                        user_w.click()

                        msg_box = driver.find_element_by_xpath(
                            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

                        for i in range(count):
                            msg_box.send_keys(mess_w)
                            button = driver.find_element_by_xpath(
                                "//*[@id='main']/footer/div[1]/div[3]/button")
                            button.click()
                            speak("Messege sent")
                    except Exception as e:
                        print(e)
                        speak("Couldn't sent the messege.Try again later.")
                else:
                    speak("Ok,nevermind")
            except Exception as e:
                print(e)
                speak("Looks like internet connection is down . Please try again later")

        elif 'game' in query:
            speak(f"You currently have {len(games)} games.")
            speak(f"{games[0]} and {games[1]}")
            speak("which one do you wanna play?")
            gamesquery = takecommand().lower()

            if 'detroit' in gamesquery:
                speak("ok")
                os.startfile(r'E:\Detroit.Become.Human\Detroit Become Human\DetroitBecomeHuman.exe')
                speak("Enjoy your game.")
                exit()
            elif 'watch dogs 2' in gamesquery:
                speak("ok")
                os.startfile(r'E:\Watch Dogs 2\bin\WatchDogs2.exe')
                speak("Enjoy your game.")
                exit()
        
        elif 'watch dogs 2' in query:
            speak("ok")
            os.startfile(r'E:\Watch Dogs 2\bin\WatchDogs2.exe')
            speak("Enjoy your game.")
            exit()
        
        elif 'detroit' in query:
            speak("ok")
            os.startfile(r'E:\Detroit.Become.Human\Detroit Become Human\DetroitBecomeHuman.exe')
            speak("Enjoy your game.")
            exit()

        elif 'search' in query:
            driver = webdriver.Chrome('F:\chromedriver.exe')
            query = query.replace("google", "")
            query = query.replace("search", "")
            driver.get("https://www.google.com/")
            msg_g = driver.find_element_by_xpath(
                "//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
            try:
                msg_g.send_keys(query)
                button_g = driver.find_element_by_xpath(
                    "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
                button_g.click()
            except:
                speak("Something went wrong.Please try again")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Rimbo...The time is {strTime}")

        elif 'open visual studio code' in query:
            code_path = 'C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak("Opening Visual Studio Code")
            os.startfile(code_path)
            speak("Please finish with your studies first and then start coding")

            speak("Do you want me to sign off, so that you can code uninterruptedly?")
            respond = takecommand()
            if 'yes' in respond:
                speak("As you wish...")
                speak("Signing off...Have fun")
                quit(query)
            if 'no' in respond:
                speak("As you wish")


        elif 'open' and 'chrome' in query:
            
            webbrowser.open_new_tab('https://www.google.co.in/')
            speak("Opening Google Chrome")
       

        elif 'email' in query:
            speak("Whom do you want to send the email?")
            receiver = takecommand()

            if receiver in leave:
                speak("Nevermind")
            else:
                try:
                    speak("What will be the content?")
                    content = takecommand()
                    content = content.capitalize()
                    to = emails[receiver]
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry Rimbo I am not able to send the email.")
                    speak("Please check your internet connection.")

        elif query in query_history:
            open('log_query.txt')

        elif 'prime music' in query:
            driver = webdriver.Chrome('F:\chromedriver.exe')

            speak("Opening Amazon Prime Music")
            webbrowser.open_new_tab(
                'https://music.amazon.in/my/songs#play/each')
            speak("What do you want to search?")
            music_command = takecommand()
            if 'leave it ' in music_command:
                speak("Ok...Fine")
                break

        elif 'netflix' in query:
            speak("Opening Netflix")
            Netflix()

        elif 'prime video' in query:

            webbrowser.open_new_tab(
                'https://www.primevideo.com/ref=av_auth_return_redir?_encoding=UTF8&ext_vrnc=hi%7Cc_386559716823_m_4mEHKPKZ-dc_s_&ie=UTF8')
            speak("What do you want to watch")
            question2 = takecommand()
            try:
                webbrowser.open(
                    f'https://www.primevideo.com/search/ref=atv_sr_sug_8?phrase={question2}&ie=UTF8')
                speak(f"Searching {question2} in Amzon prime video")
            except Exception as e:
                print(e)
                speak("Sorry...")
                speak("I could'nt search that.")
                speak("Try again.")
            while True:
                speak("Did you get that?")
                ques = takecommand()

                if 'no' in ques:
                    speak("ok")
                    speak("Let's try again")
                    speak("What do you want to watch")
                    question3 = takecommand()
                    webbrowser.open(
                        f'https://www.primevideo.com/search/ref=atv_sr_sug_8?phrase={question3}&ie=UTF8')
                    speak(f"Searching {question3} in Amazon prime video")

                else:
                    speak("Good")
                    speak(
                        "Signing off , so that you can enjoy the movie uninterruptadely.")

        elif 'date' in query:
            date = date.today()
            speak(date)

        elif query in made :
            speak('I was developed by Rimbo')
            speak("In the month of April,2020")

        elif query in who_are_you:
            speak(
                "I am a virtual voice assistant and I am not fully ready yet. I am still getting developed.")

        elif 'your name' in query:
            name_u = 'Mark'
            speak(f"My name is {name_u}")
            speak("I was developed by Rimbo")

        elif 'lyrics' in query:
            query = query.replace('lyrics', "")
            query = query.replace('of', "")
            query = query.replace('show', "")
            query = query.replace('search for', "")
            query = query.replace('lyrics', "")
            speak("Searching...")
            webbrowser.open(
                f"https://www.google.com/search?q={query}+lyrics&oq={query}&aqs=chrome.0.69i59j46j35i39j46j0j69i60l3.9304j0j9&sourceid=chrome&ie=UTF-8")

            

        elif query in covid:
            speak("In which country?")
            place = takecommand()
            get_data()

        elif 'covid' in query:
            speak("In which country?")
            place = takecommand()
            get_data()
        elif 'covid-19' in query:
            speak("In which country?")
            place = takecommand()
            get_data()
        elif 'coronavirus' in query:
            speak("In which country?")
            place = takecommand()
            get_data()
            
            

        elif 'control panel' in query:
            os.system("open /Applications/Control panel.app")

        elif 'day' in query:
            day = date.today().strftime("%A")
            speak(day)

        elif 'year' in query:
            speak(f"The month is {date.today().year}")

        elif 'month' in query:
            speak(f"The month is {date.today().month}")

        elif query in add:
            query = query.replace("addition", "")
            query = query.replace("add", "")
            query = query.replace("sum", "")
            query = query.replace("to", "")
            query = query.replace("of", "")
            query = query.replace("and", "")
            query = query.split(" ")
            num1 = int(query[0])
            num2 = int(query[1])

            speak(f"The answer is {num1+num2}")

        elif query in sleep:

            hour = int(datetime.datetime.now().hour)

            speak("Signing off...")

            speak("Thanks for your time Rimbo...")

            if hour >= 12 and hour < 16:

                speak("May you have a Good day.")

            elif hour >= 16 and hour < 20:

                speak("May you have a Good evening")

            elif hour >= 20:

                speak("Good Night")

            exit()

        elif query in shut_down:
            speak("Turning off your system")
            os.system('shutdown /p /f')