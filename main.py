import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
import random
import send_msg

class MyGrid(RelativeLayout):
    my_text = StringProperty("")

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.send_text()

    def shuffle(self):
        self.add_widget(Button(text = 'New'))

    def get_text(self):
        file = open("PhoneAppText.txt", "r")
        f = file.readlines()  # list of size n
        n = random.randint(0, len(f)-1) # make sure to subtract one to not get out of index
        self.my_text = f[n]
        #self.add_widget(Label(text=f[n])
        return self.my_text

    def send_text(self):
        return send_msg.send_sms("XXXXXXXXXX", self.get_text(), "Cricket Wireless", ("XXXXXX@gmail.com", "XXXXXX"))


class PhoneApp(App): #takes all properties from kivy's App class to be used
    def build(self):
        return MyGrid()


PhoneApp().run()
