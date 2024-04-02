from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationrail import MDNavigationRail
# from  kivymd.uix.button.button import MDButton
from kivymd.toast import toast

# Define the screens
class ScreenOne(MDScreen):
    pass

class ScreenTwo(MDScreen):
    pass

# Define the app
class MainApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

    def switch_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

    def change_screen_one(self, *args):
        self.root.current = 'screen_one'

    def change_screen_two(self, *args):
        self.root.current = 'screen_two'
    def change_screen_settings(self, *args):
        # self.root.current = 'screen_two'
        toast('Settings')



# Define the kv design file
kv = """
ScreenManager:
    ScreenTwo:
    ScreenOne:

<ScreenOne>:
    name: 'screen_one'
    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 2
        title: 'Screen One'
        left_action_items: [["menu", lambda x: x]]
        right_action_items: [["cog", lambda x: app.change_screen_settings()], ["lightbulb-outline", lambda x: app.switch_theme()]]
    MDFloatLayout:
        MDCard:
            size_hint: None, None
            size_hint: .9, 1
            pos_hint: {'center_x': .5, 'center_y': .3}
            elevation: 2
            ScrollView:
                do_scroll_x: False
                
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size_hint: 1, None
                    height: self.minimum_height
                    padding: [dp(10), dp(20), dp(10), dp(10)]
                    spacing: dp(10)
                    
                    MDTextField:
                        id: text_field_name
                        hint_text: "Enter name"
                        max_text_length: 25
                    MDTextField:
                        id: text_field_contact
                        hint_text: "Contact number"
                        input_filter: "int"
                        max_text_length: 10
                        hint_text: "Contact number"
                    MDTextField:
                        id: text_field_designation
                        hint_text: "Enter designation"
                    
                    
                    
                    MDFloatingActionButton:
                        icon: 'plus'
                        md_bg_color: app.theme_cls.primary_color
                        pos_hint: {'right': .9, 'y': .1}
                        on_release: app.change_screen_two()
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''
                    
                    
<ScreenTwo>:
    name: 'screen_two'
    MDTopAppBar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 2
        title: 'Screen Two'
        left_action_items: [["menu", lambda x: x]]
        right_action_items: [["cog", lambda x: app.change_screen_settings()], ["lightbulb-outline", lambda x: app.switch_theme()]]
    MDFloatLayout:
        MDLabel:
            text: 'Screen Two'
            halign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDCard:
            size_hint: None, None
            size_hint: .9, 1
            pos_hint: {'center_x': .5, 'center_y': .2}
            elevation: 2
            ScrollView:
                do_scroll_x: False
                
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint: None, None
                    size_hint: 1, None
                    height: self.minimum_height
                    padding: [dp(10), dp(20), dp(10), dp(10)]
                    spacing: dp(10)

                    MDCard:
                        size_hint: 0.87, None
                        height: "40dp"
                        pos_hint: {"center_x": .5}
                        border_radius: 10
                        elevation: 1
                        BoxLayout:
                            padding: dp(10)

                            MDLabel:
                                text: '2023-3-W'
                                halign: 'center'

        MDFloatingActionButton:
            icon: 'plus'
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {'right': .9, 'y': .1}
            on_release: app.change_screen_one()

"""

# Run the app
if __name__ == '__main__':
    MainApp().run()