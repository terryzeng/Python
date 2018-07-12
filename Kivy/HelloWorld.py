from kivy.app import App
from kivy.uix.button import Button

class HelloWorld(App):
	def build(self):
		btn=Button(text='Hello World!')
		return btn

if __name__=='__main__':
	HolloWorld().run()
