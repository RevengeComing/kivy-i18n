from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy_i18n.uix import Label, Button, TextInput

class TestApp(App):
    def build(self):
        button = Button(text='سلام hello دنیا world!')
        label = Label(text='سلام hello دنیا world!')
        text_input = TextInput(text="سلام hello دنیا world!")

        bl = BoxLayout(orientation='vertical')
        bl.add_widget(label)
        bl.add_widget(button)
        bl.add_widget(text_input)
        
        return bl


if __name__ == '__main__':
    TestApp().run()