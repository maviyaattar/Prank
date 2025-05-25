from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.utils import platform
from kivy.core.window import Window

if platform == 'android':
    from jnius import autoclass

class PrankApp(App):
    def build(self):
        self.label = Label(text="Welcome! Enjoy earning money!", font_size='20sp')
        
        # Disable escape key / back key
        Window.bind(on_keyboard=self.on_back_button)
        
        Clock.schedule_once(self.start_audio, 1)
        return self.label

    def start_audio(self, dt):
        if platform == 'android':
            AudioManager = autoclass('android.media.AudioManager')
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            self.context = PythonActivity.mActivity.getSystemService(PythonActivity.AUDIO_SERVICE)
            self.stream_type = AudioManager.STREAM_MUSIC
            self.max_volume = self.context.getStreamMaxVolume(self.stream_type)

            self.sound = SoundLoader.load("song.mp3")
            if self.sound:
                self.sound.play()

            # Force max volume every 0.2 sec
            Clock.schedule_interval(self.force_max_volume, 0.2)
        else:
            self.label.text = "Run on Android only."

    def force_max_volume(self, dt):
        self.context.setStreamVolume(self.stream_type, self.max_volume, 0)

    def on_back_button(self, window, key, *args):
        if key in (27, 1001):
            return True
        return False

    def on_pause(self):
        return True

    def on_stop(self):
        if self.sound:
            self.sound.stop()

if __name__ == '__main__':
    PrankApp().run()
