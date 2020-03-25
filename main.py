import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.core.text.markup import MarkupLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.banner import MDBanner
from kivymd.uix.toolbar import MDToolbar
from plyer import vibrator
from android.runnable import run_on_ui_thread
from jnius import autoclass

Color = autoclass("android.graphics.Color")
WindowManager = autoclass('android.view.WindowManager$LayoutParams')
activity = autoclass('org.kivy.android.PythonActivity').mActivity


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Main_Screen(FloatLayout):
    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)


class Custom(FloatLayout):
    def __init__(self, **kwargs):
        super(Custom, self).__init__(**kwargs)
        self._height = "[b][color=b39ddb]185[/color][/b]" if main_app.theme == "purple" else f"[b][color=CFD8DC]185[/b][/color]"
        self._age = "[b][color=b39ddb]21[/color][/b]" if main_app.theme == "purple" else f"[b][color=CFD8DC]21[/b][/color]"
        self.bmi = 0

    def ban_show(self):
        if self.bmi < 16:
            self.advice = "[color=b71c1c]You are [b]severely thin[/b].[/color]"
        elif self.bmi >= 16 and self.bmi < 17:
            self.advice = "[color=f44336]You are [b]moderately thin[/b].[/color]"
        elif self.bmi >= 17 and self.bmi < 18.5:
            self.advice = "[color=F57F17]You are [b]mildly thin[/b].[/color]"
        elif self.bmi >= 18.5 and self.bmi < 25:
            self.advice = "[color=4CAF50]You are [b]normal[/b].[/color]"
        elif self.bmi >= 25 and self.bmi < 30:
            self.advice = "[color=F57F17]You are [b]overweight[/b].[/color]"
        elif self.bmi >= 30 and self.bmi < 35:
            self.advice = "[color=f44336]You are [b]mildly obese[/b].[/color]"
        elif self.bmi >= 35 and self.bmi < 40:
            self.advice = "[color=d32f2f]You are [b]moderately obese[/b].[/color]"
        elif self.bmi >= 40:
            self.advice = "[color=b71c1c]You are [b]severely obese[/b].[/color]"
        self.bmi_text = f"[color=311B92]Your BMI is [b]{self.bmi}[/b][/color]" if main_app.theme == "purple" else f"[color=263238]Your BMI is [b]{self.bmi}[/b][/color]"
        self.ban = MDBanner(opening_transition="in_elastic", type="two-line", id="banner", text=[
                            self.bmi_text, self.advice], vertical_pad=Window.size[0]/8, over_widget=self.parent.parent.parent.parent,)
        self.tool = MDToolbar(id="toolbar", pos_hint={"top": 1}, elevation=0)
        self.parent.parent.parent.parent.parent.add_widget(self.ban)
        self.ban.show()

    def height_increment(self):
        vibrator.vibrate(0.017)
        self._height = MarkupLabel(self._height).markup
        self._height = int(self._height[2])
        self._height += 1
        self._height = f'[b][color=b39ddb]{self._height}[/color][/b]' if main_app.theme == "purple" else f"[b][color=CFD8DC]{self._height}[/b][/color]"
        self.ids.height.text = self._height

    def height_decrement(self):
        vibrator.vibrate(0.017)
        self._height = MarkupLabel(self._height).markup
        self._height = int(self._height[2])
        if self._height > 0:
            self._height -= 1
        self._height = f'[b][color=b39ddb]{self._height}[/color][/b]' if main_app.theme == "purple" else f"[b][color=CFD8DC]{self._height}[/b][/color]"
        self.ids.height.text = self._height

    def age_increment(self):
        vibrator.vibrate(0.017)
        self._age = MarkupLabel(self._age).markup
        self._age = int(self._age[2])
        self._age += 1
        self._age = f'[b][color=b39ddb]{self._age}[/color][/b]' if main_app.theme == "purple" else f"[b][color=CFD8DC]{self._age}[/b][/color]"
        self.ids.age.text = self._age

    def age_decrement(self):
        vibrator.vibrate(0.017)
        self._age = MarkupLabel(self._age).markup
        self._age = int(self._age[2])
        if self._age > 0:
            self._age -= 1
        self._age = f'[b][color=b39ddb]{self._age}[/color][/b]' if main_app.theme == "purple" else f"[b][color=CFD8DC]{self._age}[/b][/color]"
        self.ids.age.text = self._age

    def bmi_calc(self):
        vibrator.vibrate(0.035)
        self._height = MarkupLabel(self.ids.height.text).markup
        self._height = int(self._height[2])
        self.bmi = round(((self.ids.weight.value*10000)/(self._height**2)), 1)
        self._height = f'[b][color=b39ddb]{self._height}[/color][/b]' if main_app.theme == "purple" else f"[b][color=CFD8DC]{self._height}[/b][/color]"
        self.ids.height.text = self._height


class MainApp(MDApp):
    theme = StringProperty('purple')

    def build(self):
        app = MDApp.get_running_app()
        if self.theme == 'purple':
            app.theme_cls.primary_palette = "DeepPurple"
            app.theme_cls.accent_palette = "DeepPurple"
            app.theme_cls.primary_hue = "600"
            app.statusbar("#5E35B1")
        else:
            app.statusbar("#424242")
            app.theme_cls.primary_palette = "Gray"
            app.theme_cls.accent_palette = "Gray"
            app.theme_cls.primary_hue = "800"

        Window.borderless = False
        self.title = "BMI Calc"
        Config.set('kivy', 'window_title', 'BMI Calc')
        Builder.load_file(os.path.join(os.path.dirname(__file__), 'main.kv'))
        return Factory.Main_Screen()

    def themer(self):
        app = MDApp.get_running_app()
        if self.theme == "purple":
            self.theme = "dark"
            app.statusbar("#424242")
            app.theme_cls.primary_palette = "Gray"
            app.theme_cls.accent_palette = "Gray"
            app.theme_cls.primary_hue = "800"
            print(self.theme)
        else:
            self.theme = "purple"
            app.statusbar("#5E35B1")
            app.theme_cls.primary_palette = "DeepPurple"
            app.theme_cls.accent_palette = "DeepPurple"
            app.theme_cls.primary_hue = "600"
            print(self.theme)

    def show_example_bottom_sheet(self):
        bs_menu = MDListBottomSheet()
        bs_menu.add_item("[b][color=311B92]Change Theme[/color][/b]" if main_app.theme ==
                         "purple" else f"[b][color=263238]Change Theme[/b][/color]", lambda x: self.themer(), icon="theme-light-dark")
        bs_menu.add_item("[b][color=311B92]BMI Calculator[/color][/b]" if main_app.theme ==
                         "purple" else f"[b][color=263238]BMI Calculator[/b][/color]", lambda x: None, icon="google-fit")
        bs_menu.add_item("Made by Abhay Maurya",
                         lambda x: None, icon="dev-to",)
        bs_menu.add_item("using Python!", lambda x: None,
                         icon="language-python",)
        bs_menu.open()

    @run_on_ui_thread
    def statusbar(self, color):
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color))
        window.setNavigationBarColor(Color.parseColor(color))


if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()
