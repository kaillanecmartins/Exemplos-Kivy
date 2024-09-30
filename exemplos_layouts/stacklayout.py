from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class StackLayoutExample(App):
    def build(self):
        layout = StackLayout()
        for i in range(5):
            layout.add_widget(Button(text=f"Botão {i+1}", size_hint=(.2, .2)))
        return layout

StackLayoutExample().run()