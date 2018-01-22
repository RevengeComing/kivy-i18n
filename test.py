from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy_i18n.uix import Label, Button

class TestApp(App):
    def build(self):
        button = Button(text='سلام hello دنیا world!')
        label = Label(text='سلام hello دنیا world!')

        bl = BoxLayout()
        bl.add_widget(label)
        bl.add_widget(button)
        
        return bl


if __name__ == '__main__':
    TestApp().run()