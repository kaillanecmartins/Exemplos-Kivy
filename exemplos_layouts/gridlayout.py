from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayoutExample(App):
    def build(self):
        layout = GridLayout(cols = 2, spacing = 20, padding = 10)
        layout.add_widget(Button(text =  "LOONA"))
        layout.add_widget(Button(text =  "ODC"))
        layout.add_widget(Button(text =  "YYXY"))
        layout.add_widget(Button(text =  "1/3"))
        layout.add_widget(Button(text =  "Artms"))
        layout.add_widget(Button(text =  "Loosemble"))
        return layout
    
GridLayoutExample().run()