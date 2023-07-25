"""
It's my first application with Beeware!
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial

class SimpleCalculator(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN))
         
        self.number_one = toga.TextInput(placeholder="Enter Number 1")
        self.number_Two = toga.TextInput(placeholder="Enter Number 2")

        btn_box = toga.Box(style=Pack(direction=ROW))

        btn_jam = toga.Button("+" , on_press=partial(self.calc , Data = "+"))
        btn_menha = toga.Button("-" , on_press=partial(self.calc , Data = "-"))
        btn_zarb = toga.Button("x" , on_press=partial(self.calc , Data = "x"))
        btn_taghsim = toga.Button("/" , on_press=partial(self.calc , Data = "/"))

        self.lbl_hesab = toga.Label("")
        btn_box.add(btn_zarb , btn_jam , btn_menha , btn_taghsim)
        main_box.add(self.number_one)
        main_box.add(self.number_Two)
        main_box.add(btn_box)
        main_box.add(self.lbl_hesab)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def calc(self , widget , data):
        if data=="+":
            ans = int(self.number_one.value) + int(self.number_Two.value)
            self.lbl_hesab.text = ans
            yield 0.1
        elif data=="-":
            ans = int(self.number_one.value) - int(self.number_Two.value)
            self.lbl_hesab.text = ans
            yield 0.1    
        elif data=="x":
            ans = int(self.number_one.value) * int(self.number_Two.value)
            self.lbl_hesab.text = ans
            yield 0.1
        elif data=="/":
            ans = int(self.number_one.value) / int(self.number_Two.value)
            self.lbl_hesab.text = ans
            yield 0.1
        else:
            self.main_window.info_dialog("Error" ,"Not Supported")
def main():
    return SimpleCalculator()
