from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior

KV1 = '''
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

KV = '''
#:set color_deep_purple [0.36862745098,0.20784313725 ,0.69411764705,1]
#:set color_deep_purple_dark [0.270588235,0.152941176 ,0.62745098,1]
<ContentNavigationDrawer>:
	orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
	AnchorLayout:
        anchor_x: "center"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "200dp", "200dp"
            source: "icon.png"
	ScrollView:
		MDList:
		    OneLineAvatarListItem:
		        text: "1"

		        on_press:
		            root.nav_drawer.set_state("close")
		            root.screen_manager.current = "1"

		        IconLeftWidget:
            		icon: "plus"
            		pos_hint: {'center_x': .25, 'center_y': .5}
            		on_press:
				        root.nav_drawer.set_state("close")
				        root.screen_manager.current = "1"
		    OneLineAvatarListItem:
		        text: "2"
		        on_press:
		            root.nav_drawer.set_state("close")
		            root.screen_manager.current = "2"

		        IconLeftWidget:
            		icon: "plus"
            		on_press:
				        root.nav_drawer.set_state("close")
				        root.screen_manager.current = "2"
            		pos_hint: {'center_x': .25, 'center_y': .5}
		    TwoLineAvatarListItem:
		        text: "3"
		        secondary_text: "3.1"
		        on_press:
		            root.nav_drawer.set_state("close")
		            root.screen_manager.current = "3"
		        IconLeftWidget:
            		icon: "plus"
            		pos_hint: {'center_x': .25, 'center_y': .5}
            		on_press:
				        root.nav_drawer.set_state("close")
				        root.screen_manager.current = "Settings"
		        MDSwitch:
					pos_hint: {'center_x': .75, 'center_y': .5}
					active: False
					on_active: root.nav_drawer.set_state("close")
Screen:
	NavigationLayout:
		ScreenManager:
			Screen:
				ScreenManager:
					id: screen_manager
					Screen:
						name: "1"
						GridLayout:
							cols: 1
							canvas:
								Color:
									rgba: color_deep_purple
								Rectangle:
									pos: 0, 0
									size: self.size[0], self.size[1]
							Label:
								size_hint_y: '0.10'
							GridLayout:
								cols: 2
								padding: 10
								canvas:
									Color:
										rgba: color_deep_purple
									Rectangle:
										pos: 0, 0
										size: self.size[0], self.size[1]
									Color:
										rgba: color_deep_purple_dark
									RoundedRectangle:
										pos: self.size[1]/60, self.size[1]*0.75 + self.size[1]/60
										size: self.size[0]/2 - self.size[1]/60 - self.size[1]/120, self.size[1]/4 - self.size[1]/60
										radius: [20]
									Color:
										rgba: color_deep_purple_dark
									RoundedRectangle:
										pos: self.size[0]/2 + self.size[1]/120, self.size[1]*0.75 + self.size[1]/60
										size: self.size[0]/2 - self.size[1]/30 + self.size[1]/120, self.size[1]/4 - self.size[1]/60
										radius: [20]
									Color:
										rgba: color_deep_purple_dark
									RoundedRectangle:
										pos: self.size[1]/60, self.size[1]*0.50 + self.size[1]/60
										size: self.size[0] - self.size[1]/15 + self.size[1]/30, self.size[1]/4 - self.size[1]/60
										radius: [20]
									Color:
										rgba: color_deep_purple_dark
									RoundedRectangle:
										pos: self.size[1]/60, self.size[1]*0.25 + self.size[1]/60
										size: self.size[0] - self.size[1]/15 + self.size[1]/30, self.size[1]/4 - self.size[1]/60
										radius: [20]
									Color:
										rgba: color_deep_purple_dark
									RoundedRectangle:
										pos: self.size[1]/60, 0 + self.size[1]/60
										size: self.size[0] - self.size[1]/15 + self.size[1]/30, self.size[1]/4 - self.size[1]/60
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

					Screen:
						name: "2"
					Screen:
						name: "3"
				MDToolbar:
					id: toolbar
					pos_hint: {"top": 1}
					elevation: 0
					title: ""
					left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
		MDNavigationDrawer:
			id: nav_drawer
			elevation: 0

			ContentNavigationDrawer:
				screen_manager: screen_manager
				nav_drawer: nav_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainApp(MDApp):
	def build(self):
		app = MDApp.get_running_app()
		app.theme_cls.primary_palette = "DeepPurple"
		app.theme_cls.accent_palette = "DeepPurple"
		app.theme_cls.primary_hue = "600"
		app.theme_cls.theme_style = "Dark"
		Window.borderless = False
		self.title = "BMI Calc"
		Config.set('kivy', 'window_title', 'BMI Calc')
		return Builder.load_string(KV)


if __name__ == '__main__':
    MainApp().run()
