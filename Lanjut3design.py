from kivymd.app import MDApp
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader,Sound
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from random import randint
from kivy.core.window import Window
from kivy.utils import platform
# # Window.softinput_mode = "pan"


# if platform != "android":
#     Window.size = (350*1.2, 650*1.2)

class MenuScreen(Screen):
	#pass
	M = SoundLoader.load('Fluffing-a-Duck.mp3')
	M.play()
	def plays(self):
		if MenuScreen.M.state == 'play':
			self.ids.mmm.text="Music off"
			self.ids.mmm.icon="music-off"
			self.M.stop()
		else:
			self.ids.mmm.text="Music On"
			self.ids.mmm.icon="music"
			self.M.play()

class MainGameplay(Screen):
    level =0
    soal=[
    "1, 2, 3, 4, 5, ...",
    "2, 3, 5, 8, 13, ...",
    "2, 3, 5, 7, 11, ...",
    "8723, 3872, 2387, ...",
    "3, 8, 15, 24, 35, ...",
    "0, 4, 2, 6, 4, 8, ...",
    "1, 2, 6, 24, 120, ...",
    "99, 92, 86, 81, 77, ...",
    "1, 4, 9 ,18, 35, ....",
    "1, 2, 3, 6, 11, 20, 37, ...",
    "Tamat"
    ]
    jawaban = [
        "6",
        "21",
        "13",
        "7238",
        "48",
        "6",
        "720",
        "74",
        "68",
        "68",
        "Tamat"
        ]
    ssoal = StringProperty(soal[level])
    labelscor = StringProperty(f"level {level+1}")
    def hafus(self):
        self.ids.inijawabanuser.text = self.ids.inijawabanuser.text[:-1]
    def tekan(self,button):
        if self.ids.inijawabanuser.text=="0":
            self.ids.inijawabanuser.text=""
        self.ids.inijawabanuser.text+=f'{button}'    
    def gantilevel(self):
        self.ssoal = self.soal[self.level]
        self.labelscor = f"level {self.level+1}"
    def ngecek(self):
        kunci = self.jawaban[self.level]
        jawab = self.ids.inijawabanuser.text
        layout = GridLayout(cols = 1, padding = 10)
        if str(jawab)==str(kunci):
            # popp=Popup(title="Betul dong!!!!",content=Label(text='Pinter nih ye...'))
            popupLabel = Label(text = "Pinter nih ye...") 
            closeButton = Button(text = "Close the pop-up") 
    
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)     
            popp = Popup(title ='Betul dong!!!!', 
                          content = layout)  
            self.level += 1
            self.gantilevel()
        elif self.jawaban[self.level]=="Tamat":
            # popp=Popup(title="Udah Tamat Tong..!!!!",content=Label(text='Ditunggu ya kelanjutannya!!'))
            popupLabel = Label(text = "Ditunggu ya kelanjutannya!!") 
            closeButton = Button(text = "Close the pop-up") 
    
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)     
            popp = Popup(title ='Udah Tamat Tong..!!!!', 
                          content = layout)  
        else:
            # popp=Popup(title="Duuuh...Salah!!!!",content=Label(text='Bodoh nih ye...'))
            popupLabel = Label(text = "Bodoh nih ye...") 
            closeButton = Button(text = "Close the pop-up") 
    
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)     
            popp = Popup(title ='Duuuh...Salah!!!!', 
                          content = layout)   
        popp.open()
        closeButton.bind(on_press = popp.dismiss)
        self.ids.inijawabanuser.text = ""

 
class Lanjut3design(MDApp):
    def build(self):
        sm = ScreenManager(transition=WipeTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MainGameplay(name='maingameplay'))
        return sm

Lanjut3design().run()