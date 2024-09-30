from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatLayoutExample(App):
    def build(self):
        layout = FloatLayout()
        btn1 = Button(text="Botão 1", size_hint=(.2, .1), pos_hint={'x': .4, 'y': .7})
        btn2 = Button(text="Botão 2", size_hint=(.2, .1), pos_hint={'x': .4, 'y': .4})
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout

FloatLayoutExample().run()