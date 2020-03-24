from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.core.text.markup import MarkupLabel
from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.bottomsheet import MDListBottomSheet

#from android.runnable import run_on_ui_thread
#from jnius import autoclass

# Color = autoclass("android.graphics.Color")
# WindowManager = autoclass('android.view.WindowManager$LayoutParams')
# activity = autoclass('org.kivy.android.PythonActivity').mActivity

KV = '''
#:import Window kivy.core.window.Window
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:set color_deep_purple [0.36862745098,0.20784313725 ,0.69411764705,1]
#:set color_deep_purple_dark [0.270588235,0.152941176 ,0.62745098,1]
#:set color_deep_purple_light [0.701960784,0.615686275 ,0.858823529,1]
<Custom@FloatLayout>:
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
	Label:
		id: age
		text: "[b][color=b39ddb]21[/color][/b]"
		markup: True
		font_size: self.size[0]/10
		pos_hint: {'center_x':0.25, 'center_y': 0.9}
	Label:
		id: height
		text: "[b][color=b39ddb]185[/color][/b]"
		markup: True
		font_size: self.size[0]/10
		pos_hint: {'center_x':0.75, 'center_y': 0.9}
	MDIconButton:
		icon: "minus"
		pos_hint: {'center_x':0.15, 'center_y': 0.83}
		theme_text_color: "Custom"
		text_color: color_deep_purple_light
		on_press: root.age_decrement()
	MDIconButton:
		icon: "plus"
		pos_hint: {'center_x':0.35, 'center_y': 0.83}
		theme_text_color: "Custom"
		text_color: color_deep_purple_light
		on_press: root.age_increment()
	MDIconButton:
		icon: "minus"
		pos_hint: {'center_x':0.65, 'center_y': 0.83}
		theme_text_color: "Custom"
		text_color: color_deep_purple_light
		on_press: root.height_decrement()
	MDIconButton:
		icon: "plus"
		pos_hint: {'center_x':0.85, 'center_y': 0.83}
		theme_text_color: "Custom"
		text_color: color_deep_purple_light
		on_press: root.height_increment()
	Label:
		text: "[b][color=b39ddb]Weight(kg)[/color][/b]"
		markup: True
		font_size: self.size[0]/19
		pos_hint: {'center_x':0.5, 'center_y': 0.71}
	Label:
		id: weightn
		text: '[b][color=b39ddb]' + str(round(root.ids.weight.value)) + '[/color][/b]'
		markup: True
		font_size: self.size[0]/10
		pos_hint: {'center_x':0.5, 'center_y': 0.64}
	BoxLayout:
		padding: 10
		orientation:"vertical"
		pos_hint: {'center_x':0.5, 'center_y': 0.57}
		MDLabel:
            text: ""
            halign: "center"
		MDLabel:
            text: ""
            halign: "center"	
		MDSlider:
			id: weight
			min: 10
			max: 150
			value: 70
			size_hint_x: None
			size_hint_y: 1
			width: Window.size[0]*0.75
			hint: False
			pos_hint: {'center_x':0.5, 'center_y': 0.57}
		MDLabel:
            text: ""
            halign: "center"
		MDLabel:
            text: ""
            halign: "center"
	MDSwitch:
		pos_hint: {'center_x':0.5, 'center_y': 0.38}
		active: True
	Label:
		text: "[b][color=b39ddb]Male[/color][/b]"
		markup: True
		font_size: self.size[0]/19
		pos_hint: {'center_x':0.25, 'center_y': 0.38}
	Label:
		text: "[b][color=b39ddb]Female[/color][/b]"
		markup: True
		font_size: self.size[0]/19
		pos_hint: {'center_x':0.78, 'center_y': 0.38}
	MDFloatingActionButton:
		elevation: 0
		icon: "google-fit"
		user_font_size: "58sp"
		pos_hint: {'center_x':0.5, 'center_y': 0.115}
		theme_text_color: "Custom"
        text_color: color_deep_purple_light

<Main_Screen@ScreenManager>:
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
				Custom:

	Screen:
		name: "2"
	Screen:
		name: "3"

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
				Main_Screen:
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

class Main_screen(ScreenManager):
	def __init__(self, **kwargs):
		super(Main_screen, self).__init__(**kwargs)
	def screen_change(self, page):
		self.current = page

class Custom(FloatLayout):
	def __init__(self, **kwargs):
		super(Custom, self).__init__(**kwargs)
		self._height = "[b][color=b39ddb]185[/color][/b]"
		self._age = "[b][color=b39ddb]21[/color][/b]"

	def height_increment(self):
		self._height = MarkupLabel(self._height).markup
		self._height = int(self._height[2])
		self._height += 1
		self._height = f'[b][color=b39ddb]{self._height}[/color][/b]'
		self.ids.height.text = self._height

	def height_decrement(self):
		self._height = MarkupLabel(self._height).markup
		self._height = int(self._height[2])
		if self._height>0:
			self._height -= 1
		self._height = f'[b][color=b39ddb]{self._height}[/color][/b]'
		self.ids.height.text = self._height

	def age_increment(self):
		self._age = MarkupLabel(self._age).markup
		self._age = int(self._age[2])
		self._age += 1
		self._age = f'[b][color=b39ddb]{self._age}[/color][/b]'
		self.ids.age.text = self._age

	def age_decrement(self):
		self._age = MarkupLabel(self._age).markup
		self._age = int(self._age[2])
		if self._age>0:
			self._age -= 1
		self._age = f'[b][color=b39ddb]{self._age}[/color][/b]'
		self.ids.age.text = self._age

	
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
