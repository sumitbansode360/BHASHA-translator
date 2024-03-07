# google translate using python
import speech_recognition as sr
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES
from PIL import Image, ImageTk
import pyttsx3
from gtts import gTTS   
import os  
from playsound import playsound as PS  

# Define the list of languages with their corresponding codes
languages = [
    ('afrikaans', 'af'), ('albanian', 'sq'), ('amharic', 'am'), ('arabic', 'ar'), ('armenian', 'hy'),
    ('azerbaijani', 'az'), ('basque', 'eu'), ('belarusian', 'be'), ('bengali', 'bn'), ('bosnian', 'bs'),
    ('bulgarian', 'bg'), ('catalan', 'ca'), ('cebuano', 'ceb'), ('chichewa', 'ny'), ('chinese (simplified)', 'zh-cn'),
    ('chinese (traditional)', 'zh-tw'), ('corsican', 'co'), ('croatian', 'hr'), ('czech', 'cs'), ('danish', 'da'),
    ('dutch', 'nl'), ('english', 'en'), ('esperanto', 'eo'), ('estonian', 'et'), ('filipino', 'tl'), ('finnish', 'fi'),
    ('french', 'fr'), ('frisian', 'fy'), ('galician', 'gl'), ('georgian', 'ka'), ('german', 'de'), ('greek', 'el'),
    ('gujarati', 'gu'), ('haitian creole', 'ht'), ('hausa', 'ha'), ('hawaiian', 'haw'), ('hebrew', 'he'), ('hindi', 'hi'),
    ('hmong', 'hmn'), ('hungarian', 'hu'), ('icelandic', 'is'), ('igbo', 'ig'), ('indonesian', 'id'), ('irish', 'ga'),
    ('italian', 'it'), ('japanese', 'ja'), ('javanese', 'jw'), ('kannada', 'kn'), ('kazakh', 'kk'), ('khmer', 'km'),
    ('korean', 'ko'), ('kurdish (kurmanji)', 'ku'), ('kyrgyz', 'ky'), ('lao', 'lo'), ('latin', 'la'), ('latvian', 'lv'),
    ('lithuanian', 'lt'), ('luxembourgish', 'lb'), ('macedonian', 'mk'), ('malagasy', 'mg'), ('malay', 'ms'),
    ('malayalam', 'ml'), ('maltese', 'mt'), ('maori', 'mi'), ('marathi', 'mr'), ('mongolian', 'mn'),
    ('myanmar (burmese)', 'my'), ('nepali', 'ne'), ('norwegian', 'no'), ('odia', 'or'), ('pashto', 'ps'),
    ('persian', 'fa'), ('polish', 'pl'), ('portuguese', 'pt'), ('punjabi', 'pa'), ('romanian', 'ro'), ('russian', 'ru'),
    ('samoan', 'sm'), ('scots gaelic', 'gd'), ('serbian', 'sr'), ('sesotho', 'st'), ('shona', 'sn'), ('sindhi', 'sd'),
    ('sinhala', 'si'), ('slovak', 'sk'), ('slovenian', 'sl'), ('somali', 'so'), ('spanish', 'es'), ('sundanese', 'su'),
    ('swahili', 'sw'), ('swedish', 'sv'), ('tajik', 'tg'), ('tamil', 'ta'), ('telugu', 'te'), ('thai', 'th'),
    ('turkish', 'tr'), ('ukrainian', 'uk'), ('urdu', 'ur'), ('uyghur', 'ug'), ('uzbek', 'uz'), ('vietnamese', 'vi'),
    ('welsh', 'cy'), ('xhosa', 'xh'), ('yiddish', 'yi'), ('yoruba', 'yo'), ('zulu', 'zu')
]
languages_dict = dict(languages)


def change(text="type",src="English",dest="Hindi"):
    text1 = text  #stroing funcion defualt paramters 
    src1 = src
    dest1 = dest 
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = s_list.get()
    d = d_list.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    des_txt.delete(1.0,END)
    des_txt.insert(END,textget)

def change_theme():
   """Toggles between normal and color blind modes."""
   global current_theme
   if current_theme == "normal":
      current_theme = "color_blind"
      set_color_blind_theme()
   else:
      current_theme = "normal"
      set_normal_theme()

def set_normal_theme():
    """Sets the UI colors for the normal theme."""
    root.config(bg="orange")
    lab_tex.config(fg="red", bg="orange")
    # ... (update colors for other UI elements)

def set_color_blind_theme():
    """Sets the UI colors for color blindness accessibility."""
    root.config(bg="#333333")  # Dark background for better contrast
    lab_tex.config(fg="#FFFFFF", bg="#333333")  # White text on dark background
    # ... (update colors for other UI elements using color blind friendly combinations)

def speechtx_source():
    msg = Sor_txt.get(1.0,END)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(msg)
    engine.runAndWait()


def speechtx_dest():
   masg = des_txt.get(1.0, END)
   s = s_list.get()
   d = d_list.get()
   to_langeuage=NONE
   for code, lang in LANGUAGES.items():
      if lang == d: 
            to_language = code
            break
#    textget = change(text=masg, src=s, dest=d)
   speak = gTTS(text=masg, lang=to_language, slow=False)
   
   speak.save("captured_JTP_voice.mp3")
   PS('captured_JTP_voice.mp3')
   os.remove('captured_JTP_voice.mp3')

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            Sor_txt.insert(END, data)            
        except sr.UnknownValueError:
            print("Not understanding")

def clc():
    des_txt.delete("1.0",END)
    Sor_txt.delete("1.0",END)


root = Tk()
root.title('BHASHA')
root.geometry("480x700")
root.maxsize(500,680)
root.minsize(500,680)
root.config(bg="orange")




lab_tex = Label(root,text="Translator",font=("Time New Roman",40,"bold"),fg="red",bg="orange")
lab_tex.place(x=100,y=40,height=50,width=300)

frame1 = Frame(root).pack(side=BOTTOM)

sor_label = Label(root,text="Input Text",font=("Time New Roman",20,"bold"),bg="orange",fg="blue4")
sor_label.place(x=150,y=110,height=50,width=200)

Sor_txt = Text(frame1,font=("Time New Roman",20,"bold"),wrap=WORD,bg="aliceblue",relief="sunken")
Sor_txt.place(x=10,y=180,height=100,width=480)


list_txt = list(LANGUAGES.values())
s_list = ttk.Combobox(frame1,values=list_txt)
s_list.set("english")
s_list.place(x=10,y=300,height=40,width=150)

Btn = Button(text="Translate",relief="raised",cursor='hand2',command=data,bg="pink1",font=("Time New Roman",18,"bold"))
Btn.place(x=175,y=300,height=40,width=150)

d_list = ttk.Combobox(frame1,values=list_txt)
d_list.set("english")
d_list.place(x=340,y=300,height=40,width=150)

sor_label1 = Label(root,text="Output Text",font=("Time New Roman",20,"bold"),bg="orange",fg="blue4")
sor_label1.place(x=150,y=360,height=50,width=200)

des_txt = Text(frame1,font=("Time New Roman",20,"bold"),wrap=WORD,bg="aliceblue",relief="sunken")
des_txt.place(x=10,y=430,height=100,width=480)

clcs = Button(text="Clear",relief="raised",cursor="hand2",bg="pink1",font=("Time New Roman",18,"bold"),command=clc)#command=clear_area
clcs.place(x=10,y=550,height=80,width=160)

icon_path = "acces.png"
icon_img = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_img)

cb = Button(image=icon_photo,relief="raised",cursor="hand2",bg="pink1",command=change_theme)
cb.place(x=325,y=550,height=80,width=160)

icon_path1 = "speak.png"
icon_img1 = Image.open(icon_path1)
icon_photo1 = ImageTk.PhotoImage(icon_img1)

sp1 = Button(image=icon_photo1,relief="raised",cursor="hand2",bg="pink1",command=speechtx_source)
sp1.place(x=420,y=140,height=30,width=40)

sp2 = Button(image=icon_photo1,relief="raised",cursor="hand2",bg="pink1",command=speechtx_dest)
sp2.place(x=420,y=390,height=30,width=40)

icon_path2 = "mic.png"
icon_img2 = Image.open(icon_path2)
icon_photo2 = ImageTk.PhotoImage(icon_img2)

lis = Button(image=icon_photo2,relief="raise",cursor="hand2",bg="pink1",command=sptext)
lis.place(x=370,y=140,height=30,width=40)


# Initialize theme
current_theme = "normal"

# Bind the theme toggle button to the change_theme function
cb.config(command=change_theme)

root.mainloop()