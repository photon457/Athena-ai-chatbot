from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.core.window import Window

from time_ import get_response  # Backend

Window.size = (1000, 600)

class HomeScreen(Screen):
    
    def on_send(self):
        user_input = self.ids.user_input.text.strip()
        if user_input:
            self.ids.user_input.text = ""

            # Add user's message
            self.add_message(user_input, from_user=True)

            # Get assistant response
            response = get_response(user_input)
            self.add_message(response, from_user=False)
            

    def add_message(self, text, from_user):
        color = (0.6, 0.8, 1, 1) if from_user else (1.0, 0.819, 0.0, 1)#best piece of code ever came across.goated af

        align = "right" if from_user else "right"

        label = Label(
            text=text,
            color=color,
            size_hint_y=None,
            text_size=(self.width * 0.7, None),
            halign=align,
            valign="top",
            font_size=16,
        )
        label.bind(texture_size=lambda instance, value: setattr(label, 'height', value[1] + 20))

        self.ids.output_box.add_widget(label)

        # Scroll to bottom
        self.ids.scrollview.scroll_y = 0

class AssistantApp(App):
    def build(self):
        self.title = 'ATHENA'
        Builder.load_file("assistant.kv")
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    AssistantApp().run()
