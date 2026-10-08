from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class StudyAssistantApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="AI Study Assistant",
            font_size="28sp"
        )

        study_button = Button(
            text="AI Study",
            font_size="20sp"
        )

        assistant_button = Button(
            text="AI Assistant",
            font_size="20sp"
        )

        layout.add_widget(title)
        layout.add_widget(study_button)
        layout.add_widget(assistant_button)

        return layout


if __name__ == "__main__":
    StudyAssistantApp().run()
