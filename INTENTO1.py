from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from random import randint

class Juego(Widget):
    def __init__(self, **kwargs):
        super(Juego, self).__init__(**kwargs)
        self.objeto = Button(text='¡Tócame!', size_hint=(None, None), pos=(100, 100))
        self.objeto.bind(on_press=self.tocar_objeto)
        self.add_widget(self.objeto)
        self.puntuacion = 0
        self.puntuacion_label = Label(text=f'Puntuación: {self.puntuacion}', pos=(0, 0))
        self.add_widget(self.puntuacion_label)

    def tocar_objeto(self, instance):
        self.puntuacion += 1
        self.puntuacion_label.text = f'Puntuación: {self.puntuacion}'
        self.objeto.pos = (randint(0, self.width - self.objeto.width), randint(0, self.height - self.objeto.height))

class JuegoApp(App):
    def build(self):
        juego = Juego()
        Clock.schedule_interval(juego.update, 1.0 / 60.0)
        return juego

if __name__ == '__main__':
    JuegoApp().run()
