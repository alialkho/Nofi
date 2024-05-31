import os
import customtkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
from CTkListbox import *

class Nofi:

    def __init__(self, rootVar):
        self.root = rootVar
        self.filePath = ''
        self.artist = ''
        self.songName = ''
        self.isPaused = False
        self.history = ['NA']
        self.filePaths = []
        self.indices = [0]
        self.curIndex = 0
        self.playLabel = ''
        self.forwardLabel = ''
        self.backLabel = ''
        self.plusLabel = ''
        self.addFileLabel = ''
        self.addFileBtn = ''
        self.playBtn = ''
        self.forwardBtn = ''
        self.backBtn = ''
        self.plusBtn = ''
        self.allAudios = []
        

    def startApp(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("blue")
        
        pygame.mixer.init()

        frame3 = Frame(self.root, width=450, height=640, background="gray10", pady = 20)
        self.listbox = CTkListbox(frame3, width=450, height=622, justify="center", font=('Helvetica', 18))
        self.addSongOnStartUp()

        frame1 = Frame(self.root, width=450, height=80, relief=GROOVE, borderwidth=0)
        frame1.pack(side=BOTTOM)
        frame1.pack_propagate(False)


        logoImage1 = Image.open("visuals/logo.png")
        logoImage2 = customtkinter.CTkImage(
            light_image=logoImage1,
            dark_image=logoImage1,
            size=(32,32)
        )


        frame2 = Frame(self.root, width=450, height=50, relief=GROOVE, borderwidth=0, background="gray14")
        frame2.pack()
        frame2.pack_propagate(False)

        playBtn01 = Image.open("visuals/playbutton.png")
        playBtn02 = customtkinter.CTkImage(
            light_image=playBtn01,
            dark_image=playBtn01,
            size=(64,64)
        )

        forwardBtn01 = Image.open("visuals/nextbutton01.png")
        forwardBtn02 = customtkinter.CTkImage(
            light_image=forwardBtn01,
            dark_image=forwardBtn01,
            size=(52,52)
        )

        backBtn01 = Image.open("visuals/backbutton01.png")
        backBtn02 = customtkinter.CTkImage(
            light_image=backBtn01,
            dark_image=backBtn01,
            size=(52,52)
        )

        plusBtn01 = Image.open("visuals/plus.png")
        plusBtn02 = customtkinter.CTkImage(
            light_image=plusBtn01,
            dark_image=plusBtn01,
            size=(42,42)
        )

        self.playLabel = customtkinter.CTkLabel(self.root, image=playBtn02, text="")
        self.forwardLabel = customtkinter.CTkLabel(self.root, image=forwardBtn02, text="")
        self.backLabel = customtkinter.CTkLabel(self.root, image=backBtn02, text="")
        self.plusLabel = customtkinter.CTkLabel(self.root, image=plusBtn02, text="")

        self.playBtn = customtkinter.CTkButton(frame1, image=playBtn02, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.play)
        self.forwardBtn = customtkinter.CTkButton(frame1, image=forwardBtn02, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.nextSong)
        self.backBtn = customtkinter.CTkButton(frame1, image=backBtn02, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.prevSong)
        self.plusBtn = customtkinter.CTkButton(frame2, image=plusBtn02, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.addSong)
        logo = customtkinter.CTkLabel(frame2, text = "", image = logoImage2)

        self.backBtn.pack(side=LEFT, ipadx=10)
        self.playBtn.pack(side=LEFT, padx=103)
        self.forwardBtn.pack(side=RIGHT, ipadx=10)
        self.plusBtn.pack(side=RIGHT, padx= 10)
        logo.pack(pady=10, side=LEFT, padx=13)

        self.playBtn.bind('<Enter>', self.onHover)
        self.playBtn.bind('<Leave>', self.hoverOff)
        self.backBtn.bind('<Enter>', self.onHover2)
        self.backBtn.bind('<Leave>', self.hoverOff2)
        self.forwardBtn.bind('<Enter>', self.onHover3)
        self.forwardBtn.bind('<Leave>', self.hoverOff3)
        self.plusBtn.bind('<Enter>', self.onHover4)
        self.plusBtn.bind('<Leave>', self.hoverOff4)

        frame3.pack()

        self.listbox.pack(fill=BOTH)

        scrollbar = Scrollbar(frame3)
        scrollbar.pack()


    def loadData(self):
        
        self.filePath = filedialog.askopenfilename(filetypes=(("mp3 file", "*.mp3"),))
        
        if self.filePath:
            label1 = customtkinter.CTkLabel(self.top, text="File uploaded successfully", text_color="lightgreen")
            label1.place(x=120, y = 265)
            self.filePaths.append(self.filePath)
        elif not self.filePath:
            label1 = customtkinter.CTkLabel(self.top, text="Error uploading file", text_color="red")
            label1.place(x=140, y = 265)

    def addSong(self):
        self.top = Toplevel()
        self.top.title("Add Song")
        self.top.geometry("400x400")
        self.top.resizable(False,False)
    

        self.songNameEntry = customtkinter.CTkEntry(self.top, placeholder_text="Song Name", width=350, justify="center")
        self.artistNameEntry = customtkinter.CTkEntry(self.top, placeholder_text="Artist Name", width=350, justify="center")
        coverUrlLabel = customtkinter.CTkLabel(self.top, text="Upload Cover Art Photo: ")
        audioLabel = customtkinter.CTkLabel(self.top, text="Upload Audio: ")

        loadFileBtn1 = Image.open("visuals/loadfile.png")
        loadFileBtn2 = customtkinter.CTkImage(
        light_image=loadFileBtn1,
        dark_image=loadFileBtn1,
        size=(48,48)
    )

        addFileBtn1 = Image.open("visuals/plus.png")
        addFileBtn2 = customtkinter.CTkImage(
            light_image=addFileBtn1,
            dark_image=addFileBtn1,
            size=(48,48)
        )

        loadFileBtn3 = Image.open("visuals/loadfile.png")
        loadFileBtn4 = customtkinter.CTkImage(
        light_image=loadFileBtn3,
        dark_image=loadFileBtn3,
        size=(48,48)
    )

        
        
        loadFileLabel = customtkinter.CTkLabel(self.top, image=loadFileBtn2, text="")
        loadFileBtn = customtkinter.CTkButton(self.top, image=loadFileBtn2, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.loadData)
        self.addFileLabel = customtkinter.CTkLabel(self.top, image=addFileBtn2, text="")
        self.addFileBtn = customtkinter.CTkButton(self.top, image=addFileBtn2, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.submitSong)
        audioLabel1 = customtkinter.CTkLabel(self.top, image=loadFileBtn4, text="")
        addAudioBtn = customtkinter.CTkButton(self.top, image=loadFileBtn4, cursor="pointinghand", text="", fg_color="transparent", hover="none", width=10, height=10, command=self.loadData)

        self.addFileBtn.bind('<Enter>', self.onHover5)
        self.addFileBtn.bind('<Leave>', self.hoverOff5)

        self.songNameEntry.place(x=25,y=45)
        self.artistNameEntry.place(x=25, y=100)
        audioLabel.place(x=153,y=160)
        addAudioBtn.place(x=167, y = 200)
        self.addFileBtn.place(x=167,y=300)

    def addSongOnStartUp(self):
        with open('music/musicNamesAndFiles.txt', 'r') as f:
            for line in f:
                line = line.split(',')
                for i in range(len(line)):
                    line[i].strip()
                
                song = line[0]
                artist = line[1]
                filePath = line[2]
                filePath = filePath.strip()
    
                self.listbox.insert(END, song + " - " + artist)
                self.allAudios.append(f"{song} - {artist}")
                self.filePaths.append(filePath)

    def submitSong(self):
        song = self.songNameEntry.get()
        artist = self.artistNameEntry.get()
        
        # write song to file
        with open('music/musicNamesAndFiles.txt', 'a') as f:
            f.write(f'{song}, {artist}, {self.filePath}\n')
            f.close()
        
        if (song or artist) and self.filePath:
            lab = Frame(self.root, width=50, height=10, background="blue")
            self.listbox.insert(END, song + " - " + artist)
            self.allAudios.append(f"{song} - {artist}")
            self.top.destroy()

    def play(self):
        self.curIndex = self.listbox.curselection()
        l = self.listbox.get(self.curIndex)
        self.indices.append(self.curIndex)
        if self.listbox.get(self.curIndex):
            song = self.filePaths[self.curIndex]

            if self.isPaused:
                if self.indices[-1] != self.indices[-2]:
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play() 
                else:
                    pygame.mixer.music.unpause()
                    self.isPaused = False
            elif pygame.mixer.music.get_busy() and self.isPaused == False:
                    if self.indices[-1] != self.indices[-2]:
                        pygame.mixer.music.load(song)
                        pygame.mixer.music.play() 
                    else:
                        pygame.mixer.music.pause()
                        self.isPaused = True
            elif not pygame.mixer.music.get_busy() and self.isPaused == False:
                pygame.mixer.music.load(song)
                pygame.mixer.music.play() 
    
    def nextSong(self):
        self.curIndex = self.listbox.curselection()
        if self.listbox.get(self.curIndex):
            nextOne = self.listbox.curselection()
            if self.listbox.size() > 1:
                nextOne = self.curIndex + 1
                if self.curIndex < self.listbox.size():
                    song = self.listbox.get(nextOne)
                    self.listbox.deselect(self.curIndex)
                    self.listbox.select(nextOne)
                    self.play()

    def prevSong(self):
        self.curIndex = self.listbox.curselection()
        if self.listbox.get(self.curIndex):
            prevOne = self.listbox.curselection()
            if self.listbox.size() > 1:
                prevOne = self.curIndex - 1
                if self.curIndex >= 0:
                    song = self.listbox.get(prevOne)
                    self.listbox.deselect(self.curIndex)
                    self.listbox.select(prevOne)
                    self.play()

    def onHover(self, e):
        newImage = Image.open("visuals/plusbuttoneffect.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(64,64)
        )

        self.playLabel.configure(image=playBtn03)
        self.playBtn.configure(image=playBtn03)

    def hoverOff(self, e):
        newImage = Image.open("visuals/playbutton.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(64,64)
        )

        self.playLabel.configure(image=playBtn03)
        self.playBtn.configure(image=playBtn03)

    def onHover2(self, e):
        newImage = Image.open("visuals/backbuttoneffect.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(52,52)
        )

        self.backLabel.configure(image=playBtn03)
        self.backBtn.configure(image=playBtn03)

    def hoverOff2(self, e):
        newImage = Image.open("visuals/backbutton01.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(52,52)
        )

        self.backLabel.configure(image=playBtn03)
        self.backBtn.configure(image=playBtn03)
    
    def onHover3(self, e):
        newImage = Image.open("visuals/nextbuttoneffect.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(52,52)
        )

        self.forwardLabel.configure(image=playBtn03)
        self.forwardBtn.configure(image=playBtn03)

    def hoverOff3(self, e):
        newImage = Image.open("visuals/nextbutton01.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(52,52)
        )

        self.forwardLabel.configure(image=playBtn03)
        self.forwardBtn.configure(image=playBtn03)
    
    def onHover4(self, e):
        newImage = Image.open("visuals/plusbuttoneffect1.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(42,42)
        )

        self.plusLabel.configure(image=playBtn03)
        self.plusBtn.configure(image=playBtn03)

    def hoverOff4(self, e):
        newImage = Image.open("visuals/plus.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(42,42)
        )

        self.plusLabel.configure(image=playBtn03)
        self.plusBtn.configure(image=playBtn03)

    def onHover5(self, e):
        newImage = Image.open("visuals/plusbuttoneffect1.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(48,48)
        )

        self.addFileLabel.configure(image=playBtn03)
        self.addFileBtn.configure(image=playBtn03)

    def hoverOff5(self, e):
        newImage = Image.open("visuals/plus.png")
        playBtn03 = customtkinter.CTkImage(
            light_image=newImage,
            dark_image=newImage,
            size=(48,48)
        )

        self.addFileLabel.configure(image=playBtn03)
        self.addFileBtn.configure(image=playBtn03)
    

if __name__ == "__main__":
    root = customtkinter.CTk()
    root.geometry("450x800")
    root.resizable(False,False)
    root.title("Nofi")  
    root.wm_attributes('-transparent', True)

    app = Nofi(root)
    app.startApp()

    root.mainloop()