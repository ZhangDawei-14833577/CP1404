from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window


class DynamicLabelsApp(App):
    """Create labels dynamically from a list of names."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ----- model (data) -----
        self.names = [
            "Ada Lovelace",
            "Alan Turing",
            "Grace Hopper",
            "Donald Knuth",
            "Linus Torvalds"
        ]

    def build(self):
        Window.size = (400, 300)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")

        # ----- controller logic: build the view from the model -----
        for name in self.names:
            lbl = Label(text=name, font_size=18)
            self.root.ids.main.add_widget(lbl)

        return self.root


if __name__ == "__main__":
    DynamicLabelsApp().run()
