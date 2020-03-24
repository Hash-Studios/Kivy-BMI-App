from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.bottomsheet import MDListBottomSheet

#from android.runnable import run_on_ui_thread
#from jnius import autoclass

# Color = autoclass("android.graphics.Color")
# WindowManager = autoclass('android.view.WindowManager$LayoutParams')
# activity = autoclass('org.kivy.android.PythonActivity').mActivity

KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:set color_deep_purple [0.36862745098,0.20784313725 ,0.69411764705,1]
#:set color_deep_purple_dark [0.270588235,0.152941176 ,0.62745098,1]
<BoxContentForBottomSheetCustomScreenList>
    orientation: "vertical"
    padding: dp(10)
    spacing: dp(10)
    size_hint_y: None
    height: self.minimum_height
    pos_hint: {"top": 1}

    ScrollView:

        GridLayout:
            id: box
            size_hint_y: None
            height: self.minimum_height
            cols: 1
Screen:
	NavigationLayout:
		ScreenManager:
			Screen:
				ScreenManager:
					id: screen_manager
					transition: FadeTransition(duration=.2, clearcolor=app.theme_cls.bg_dark)
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
										text: "[b][color=b39ddb]Age[/color][/b]"
										markup: True
										font_size: self.size[0]/19
										pos_hint: {'center_x':0.25, 'center_y': 0.97}
									Label:
										text: "[b][color=b39ddb]Height(cms)[/color][/b]"
										markup: True
										font_size: self.size[0]/19
										pos_hint: {'center_x':0.75, 'center_y': 0.97}

					Screen:
						name: "2"
					Screen:
						name: "3"
				MDToolbar:
					id: toolbar
					pos_hint: {"top": 1}
					elevation: 0
					title: ""
					left_action_items: [["menu", lambda x: app.show_example_bottom_sheet()]]
					BoxLayout:
						Label:
							text: "[b][color=b39ddb]BMI Calculator[/color][/b]"
							markup: True
							font_size: self.size[0]/8
							pos_hint: {'center_x':0, 'center_y': 0.5}

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
		app.theme_cls.theme_style = "Light"
		Window.borderless = False
		self.title = "BMI Calc"
		Config.set('kivy', 'window_title', 'BMI Calc')
		return Builder.load_string(KV)
	def show_example_bottom_sheet(self):
		bs_menu = MDListBottomSheet()
		bs_menu.add_item("[b][color=311B92]BMI Calculator[/color][/b]", lambda x: None, icon="google-fit")
		bs_menu.add_item("Made by Abhay Maurya", lambda x: None, icon="dev-to",)
		bs_menu.add_item("using Python!", lambda x: None, icon="language-python",)
		bs_menu.open()
	# @run_on_ui_thread
	# def statusbar(self,color):
	# 	window = activity.getWindow()
	# 	window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
	# 	window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
	# 	window.setStatusBarColor(Color.parseColor(color)) 
	# 	window.setNavigationBarColor(Color.parseColor(color))


if __name__ == '__main__':
	main_app = MainApp()
	#main_app.statusbar("#5E35B1")
	main_app.run()
