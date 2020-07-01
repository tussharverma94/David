import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
from whatsapp import auto_send
import winsound
import socket
from call_script import callpy
from search_file import search_f

engine = pyttsx3.init('sapi5')
current_voice = 0
world_for_ip = ["get ip address", "what is my ip address", "whats my ip address", "can you tell my ip address"]
world_for_game = ["play a game", "play game", "can you play me a game"]
mail_di = {}
world_for_acknowledge = ["how are you", "hi how are you", "are you fine"]
world_for_stopping = ["stop yourself", "shutdown", "shut down", "can you please just shut up", "kill yourself"]
world_for_search_google = ["search google", "google search", "what google say about"]
world_for_search_file = ["search for", "play"]

def speak(speech):
    engine.say(speech)
    engine.runAndWait()


def change_speed(speed):
    engine.setProperty('rate', speed)
    speech = "Sir my speaking rate has been changed to {}".format(speed)
    speak(speech)


def get_speed_rate():
    rate = engine.getProperty('rate')
    speech = "My rate of speech is set to {}".format(rate)
    speak(speech)


def change_volume(volume_rate):
    engine.setProperty('volume', volume_rate)
    speech = "Sir my volume has been set to {}".format(str(volume_rate))
    speak(speech)


def get_volume():
    volume = engine.getProperty('volume')
    speech = "My Volume of speech is set to {}".format(str(volume))
    speak(speech)


def change_voice():
    voices = engine.getProperty('voices')
    global current_voice
    if current_voice == 0:
        engine.setProperty('voices', voices[1].id)
        current_voice = 1
        speech = "Hello I am Kiara"
        speak(speech)
    elif current_voice == 1:
        engine.setProperty('voices', voices[0].id)
        current_voice = 0
        speech = "Hello I am David"
        speak(speech)


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning, Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")

    else:
        speak("Good Evening")

    speak("I am David Sir. Please tell me how may i help you")


def take_command(phrase_time_l=5):
    """takes voice input and return str of that voice input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning..")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=phrase_time_l)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"Sir you said: {query}\n")
        return query

    except Exception as e:
        print("Say that again\n")
        return "None"


def send_mail(name):
    pass
    # speak("What should i say")
    # content = take_command()


def open_website(user_site):
    try:
        speak("Opening")
        webbrowser.open(user_site)
    except Exception as e:
        speak("Not able  to process the qurey do to some unavoidable poblem")


def send_whatsapp():
    count = 0
    speak("Enter the name to whom you want to send the message")
    name = take_command()
    if name == "None":
        if count < 4:
            speak("Sorry Not able to hear you,please speak again")
            send_whatsapp()
            count = count + 1
        else:
            speak("There is some problem")
    else:
        speak("You want to send message to {}. Do you want to send it".format(name))
        confirmation_ = take_command()
        if confirmation_ == "yes":
            speak("Speak the message")
            message_ = take_command()
            k = auto_send(name, message_, "https://web.whatsapp.com", 1)
            result_ = k.send_mssg()
            if result_ == "successful":
                speak("Your message was sent succesfully")
            elif result_ == "failed":
                speak("failed to send the message, Try again")
        elif confirmation_ == "no":
            speak("Your message was cancelled")


def make_sound(frequency=2500, duration=1000):
    try:
        winsound.Beep(frequency, duration)
    except Exception as e:
        pass


def find_spelling(user_string, base_s):
    """gives the correct spelling of the world spoken"""
    len_ = len(base_s)
    wrong_or_correct_world = user_string[len_ + 1:]
    return wrong_or_correct_world


def is_game(query):
    for i in world_for_game:
        if i in query:
            return True
    return False


def run_game():
    call_object = callpy()
    call_object.call_python_file()


def is_ip_world(user_text):
    for i in world_for_ip:
        if i in user_text:
            return True
    return False


def is_acknowledge(query):
    for i in world_for_acknowledge:
        if i in query:
            return True
    return False

def is_stopping(query):
    for i in world_for_stopping:
        if i in query:
            return True
    return False

def is_search_google(query):
    for i in world_for_search_google:
        if i in query:
            return True
    return False

def is_search_file(query):
    """search for "name of movie" only"""
    for world in world_for_search_file:
        if world in query:
            return True
    return False


if __name__ == "__main__":
    greet()
    run = True
    while run:
        query = take_command().lower()
        if query == "None":
            speak("Sorry Not able to hear you,please speak again")
            continue

        # logic for executing task
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open gaurav taneja' in query or 'flying beast' in query:
            try:
                open_website("https://www.youtube.com/channel/UCNSdjX4ry9fICqeObdZPAZQ")
            except Exception as e:
                speak("Channel not found")

        elif 'open youtube' in query:
            try:
                open_website("https://www.youtube.com")
            except Exception as e:
                speak("There is some problem in opening youtube")


        elif 'open google' in query:
            open_website("https://www.google.com")

        elif 'open keep' in query:
            open_website("https://keep.google.com")

        elif 'play music' in query:
            music_dir = ""
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query or "what's the time" in query:
            srtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {srtTime}")

        elif "send email" in query:
            name = take_command()
            speak("Are you sure you want to send email to {}".format(name))
            confirmation = take_command()
            if confirmation == "yes":
                send_mail(name)
            else:
                speak("Email send cancelled")
                continue
        elif "send whatsapp" in query:
            send_whatsapp()

        elif "convert to text" in query:
            base_path = "C:\\Users\\tussh\\OneDrive\\Desktop\\"
            speak("Sir, provide the name of the file in which the text is to be saved")
            file_name = take_command(3)
            if file_name == "None":
                speak("Giving the default name as speech_to_text")
                file_name = "speech_to_text"
                base_path = base_path + file_name + ".txt"
            else:
                base_path = base_path + file_name + ".txt"
            speak("Sir you could speak the speech after a beep for 40 seconds")
            make_sound()
            text = take_command(20)
            speak("Converting ,Sir")
            if text == "None":
                speak("Something Went Wrong Please Try Again")
            else:
                try:
                    speak("Saving the text")
                    file = open(base_path, 'w')
                    file.write(text)
                    file.close()
                    speak("your text was successfully saved at {} with file name as {}".format(base_path, file_name))

                except Exception as e:
                    print(e)
                    speak("Something went wrong, Please try again")
        elif "what is the spelling" in query or "what's the spelling of" in query:
            speak("The spelling of")
            if "what is the spelling" in query:
                base_s = "what is the spelling of"
                correct_world = find_spelling(query, base_s)
                speak("{} is".format(correct_world))
                for i in correct_world:
                    speak(i)
            else:
                base_s = "what's is the spelling of"
                correct_world = find_spelling(query, base_s)
                speak("{} is".format(correct_world))
                for i in correct_world:
                    speak(i)

        elif is_ip_world(query):
            shell_object = callpy()
            local_ip = shell_object.return_ip()
            print(local_ip)
            speak("your ip address is {}".format(local_ip))

        elif is_game(query):
            speak("running a game")
            run_game()
            run = True

        elif is_acknowledge(query):
            speak("i am fine sir, how can i help you")

        elif is_stopping(query):
            speak("shutting down")
            run = False

        elif is_search_google(query):
            speak("presenting on your default browser")
            for i in world_for_search_google:
                if i in query:
                    output = query[len(i):]
                    user_site = "https://google.com/search?q={}".format(output)
                    open_website(user_site)
                    break

        elif is_search_file(query):
            for world in world_for_search_file:
                if world in query:
                    output = query[len(world)+1:]
                    output = output.strip()
                    print(len(output))
                    speak("Searching")
                    directory_name = "time"
                    search_obj = search_f(output,directory_name)
                    #answer = search_obj.find_file() #search using os
                    answer = search_obj.find_file_glob()
                    if answer == "found":
                        speak("playing")
                    else:
                        speak("Not able to find the file, try again")
                    break
