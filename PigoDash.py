from customtkinter import *
import webbrowser

Gołąb= CTk()
Gołąb.title("PigeoDash")
Gołąb.geometry("1000x1000")
Gołąb.config(bg="#656d4a")
PigeoDash=CTkLabel(master=Gołąb ,text="PigeoDash",bg_color="#656d4a", font=("Serif", 65),text_color="#dad7cd")
PigeoDash.pack()
def Youtube():
    WSI.pack_forget()
    Gugel.pack_forget()
    yt.pack_forget()
    zapytaj = CTkEntry(master=Gołąb, corner_radius=500, fg_color="#588157", bg_color="#656d4a",
                   border_color="#a3b18a", border_width=3, width=500, height=100, font=("Serif", 65),
                   text_color="#dad7cd")
    zapytaj.pack()
    def Pobierz():
        YT = zapytaj.get()
        webbrowser.open("https://www.youtube.com/results?search_query=" + YT)
    Zatwierdź = CTkButton(master=Gołąb, text="Zatwierdź", corner_radius=500, fg_color="#588157",
                      bg_color="#656d4a", hover_color="#3a5a40", border_color="#a3b18a",
                      border_width=3, command=Pobierz, width=500, height=100, font=("Serif", 65),
                      text_color="#dad7cd")
    def Wróć():
        Zatwierdź.pack_forget()
        zapytaj.pack_forget()
        yt.pack()
        WSI.pack()
        Gugel.pack()
        Arizona.pack_forget()
    Arizona = CTkButton(master=Gołąb, text="Wróć", corner_radius=500, fg_color="#588157",
                 bg_color="#656d4a", hover_color="#3a5a40", border_color="#a3b18a",
                 border_width=3, command=Wróć, width=500, height=100, font=("Serif", 65),
                 text_color="#dad7cd")
    Zatwierdź.pack()
    Arizona.pack()
yt=CTkButton(master=Gołąb,text="Youtube",corner_radius=500, fg_color="#588157",
             bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" , border_width=3,
             command=Youtube, width=500 ,height=100,font=("Serif", 65),text_color="#dad7cd")
yt.pack()

def Tiktok():
    webbrowser.open("https://www.tiktok.com/explore")
tt=CTkButton(master=Gołąb,text="Tiktok",corner_radius=500, fg_color="#588157",
             bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
             border_width=3, command=Tiktok, width=500 ,height=100,font=("Serif", 65),
             text_color="#dad7cd")
tt.pack()

def Instagram():
    webbrowser.open("https://www.instagram.com")
insta=CTkButton(master=Gołąb,text="Instagram",corner_radius=500, fg_color="#588157",
                bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" , border_width=3,
                command=Instagram, width=500 ,height=100,font=("Serif", 65),text_color="#dad7cd")
insta.pack()

def gmail():
    webbrowser.open("https://mail.google.com/")
gm=CTkButton(master=Gołąb,text="Gmail",corner_radius=500, fg_color="#588157",
             bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" , border_width=3,
             command=gmail, width=500 ,height=100,font=("Serif", 65),text_color="#dad7cd")
gm.pack()

def Wiki():
    webbrowser.open("https://pl.wikipedia.org")
Wiki=CTkButton(master=Gołąb,text="Wikipedia",corner_radius=500, fg_color="#588157",
                 bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
                 border_width=3, command=Wiki, width=500 ,height=100,font=("Serif", 65),
                 text_color="#dad7cd")
Wiki.pack()

def AI():
    Gugel.pack_forget()
    WSI.pack_forget()
    ai.pack_forget()
    zapytaj=CTkEntry(master=Gołąb, corner_radius=500, fg_color="#588157", bg_color="#656d4a",
                   border_color="#a3b18a",border_width=3, width=500, height=100, font=("Serif", 65),
                   text_color="#dad7cd")
    zapytaj.pack()
    def Pobierz():
         AI=zapytaj.get()
         webbrowser.open("https://www.google.com/search?udm=50&q="+AI)
    Zatwierdź=CTkButton(master=Gołąb,text="Zatwierdź",corner_radius=500, fg_color="#588157",
              bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
              border_width=3, command=Pobierz, width=500 ,height=100,font=("Serif", 65),
              text_color="#dad7cd")
    def Wróć():
            Zatwierdź.pack_forget()
            zapytaj.pack_forget()
            Gugel.pack()
            WSI.pack()
            Wróć.pack_forget()
            ai.pack()
    Wróć=CTkButton(master=Gołąb,text="Wróć",corner_radius=500, fg_color="#588157",
              bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
              border_width=3, command=Wróć, width=500 ,height=100,font=("Serif", 65),
              text_color="#dad7cd")
    Zatwierdź.pack()
    Wróć.pack()
ai=CTkButton(master=Gołąb,text="AI",corner_radius=500, fg_color="#588157",
              bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
              border_width=3, command=AI, width=500 ,height=100,font=("Serif", 65),
              text_color="#dad7cd")
ai.pack()

def URL():
    WSI.pack_forget()
    Gugel.pack_forget()
    URL = CTkEntry(master=Gołąb, corner_radius=500, fg_color="#588157", bg_color="#656d4a",
                   border_color="#a3b18a",border_width=3, width=500, height=100, font=("Serif", 65),
                   text_color="#dad7cd")
    URL.pack()
    def Pobierz():
         WURL=URL.get()                        
         webbrowser.open("https://"+WURL)
    Zatwierdź=CTkButton(master=Gołąb,text="Zatwierdź",corner_radius=500, fg_color="#588157",
              bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
              border_width=3, command=Pobierz, width=500 ,height=100,font=("Serif", 65),
              text_color="#dad7cd")
    def Wróć():
            Zatwierdź.pack_forget()
            URL.pack_forget()
            Gugel.pack()
            WSI.pack()
            Wróć.pack_forget()
    Wróć=CTkButton(master=Gołąb,text="Wróć",corner_radius=500, fg_color="#588157",
              bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
              border_width=3, command=Wróć, width=500 ,height=100,font=("Serif", 65),
              text_color="#dad7cd")
    Zatwierdź.pack()
    Wróć.pack()
WSI=CTkButton(master=Gołąb,text="Własne URL",corner_radius=500, fg_color="#588157",
               bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
               border_width=3, command=URL, width=500 ,height=100,font=("Serif", 65),
               text_color="#dad7cd")                                                                                                   
WSI.pack()

def wwg():
    WSI.pack_forget()
    Gugel.pack_forget()
    wwg=CTkEntry(master=Gołąb, corner_radius=500, fg_color="#588157", bg_color="#656d4a",
                 border_color="#a3b18a",border_width=3, width=500, height=100, font=("Serif", 65),
                 text_color="#dad7cd")
    wwg.pack()
    def Google():
               Google=wwg.get()
               webbrowser.open("https://google.com/search?q="+Google)
    Zatwierdź=CTkButton(master=Gołąb,text="Zatwierdź",corner_radius=500, fg_color="#588157",
                  bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
                  border_width=3, command=Google, width=500 ,height=100,font=("Serif", 65),
               text_color="#dad7cd")
    Zatwierdź.pack()
    def Powrót():
            Zatwierdź.pack_forget()
            wwg.pack_forget()
            Gugel.pack()
            WSI.pack()
            Wróć.pack_forget()
    Wróć = CTkButton(master=Gołąb, text="Wróć", corner_radius=500, fg_color="#588157",
                     bg_color="#656d4a", hover_color="#3a5a40", border_color="#a3b18a",
                     border_width=3, command=Powrót, width=500, height=100, font=("Serif", 65),
                     text_color="#dad7cd")
    Wróć.pack()
Gugel=CTkButton(master=Gołąb,text="Wyszukaj",corner_radius=500, fg_color="#588157",
                   bg_color="#656d4a",hover_color="#3a5a40",border_color="#a3b18a" ,
                   border_width=3, command=wwg, width=500 ,height=100,font=("Serif", 65),
                   text_color="#dad7cd")
Gugel.pack()

Gołąb.mainloop()