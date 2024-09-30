from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(orientation = 'horizontal', spacing = 10, padding = 20)
        layout.add_widget(Button(text = "Botão 1"))
        layout.add_widget(Button(text = "Botão 2"))
        layout.add_widget(Button(text = "Botão 3"))
        return layout
    

BoxLayoutExample().run()