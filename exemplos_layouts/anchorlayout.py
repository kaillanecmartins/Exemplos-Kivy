from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class AnchorLayoutExample(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='top')
        btn = Button(text="IVE")
        layout.add_widget(btn)
        return layout

AnchorLayoutExample().run()