from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder

KV='''
GridLayout:
	cols: 1
	Label:
		text: "Hello1"
		font_size: self.size[0]/6
		size_hint_y: None
		height: self.size[0]/7
	GridLayout:
		cols: 2
		padding: 10
		canvas:
			Color:
				rgba: 0.2,0.2,0.2,1
			Rectangle:
				pos: 0, 0
				size: self.size[0], self.size[1]
			Color:
				rgba: 0.4,0.4,0.4,1
			RoundedRectangle:
				pos: self.size[1]/60, self.size[1]*0.75
				size: self.size[0]/2 - self.size[1]/60 - self.size[1]/120, self.size[1]/4 - self.size[1]/60
				radius: [20]
			Color:
				rgba: 0.4,0.4,0.4,1
			RoundedRectangle:
				pos: self.size[0]/2 + self.size[1]/120, self.size[1]*0.75
				size: self.size[0]/2 - self.size[1]/30 + self.size[1]/120, self.size[1]/4 - self.size[1]/60
				radius: [20]
		FloatLayout:
			Label:
				text: "Hello"
				font_size: self.size[0]/8
				pos_hint: {'center_x':0.25, 'center_y': 0.95}
			Label:
				text: "Hello"
				font_size: self.size[0]/8
				pos_hint: {'center_x':0.75, 'center_y': 0.95}
'''

class MainApp(MDApp):
	def build(self):
		return Builder.load_string(KV)
		
		
if __name__ == '__main__':
	MainApp().run()
