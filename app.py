from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.navigationrail import MDNavigationRail
# from  kivymd.uix.button.button import MDButton
from kivymd.toast import toast
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
# date-picker
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.filemanager import MDFileManager


# Check if directory exists | if not create it
import os
def check_dir(dir_path:str):
    '''Check if directory exists | if not create it'''
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:    return dir_path

save_path = os.path.join(os.getcwd(),"save")
'''file to save the generated excel file'''
check_dir(save_path)

manpower = []
'''list of manpower to be added to the excel file'''
designation = []
'''list of designation to be added to the excel file'''
date_selected = []
''' selected date from the date picker'''
downld_dir_ = ''
'''directory to download the file'''

# date
from datetime import datetime
def format_date(date_str:str='2024-09-21') -> list[str, str]:
    '''
    formats the date string to year and month {2024-09-21} -> {2024, September}
    - ``` MDDatePicker ``` to ``` formated yy-mm```
    '''
    # assuming date_str is the date you got from mddatepicker
    # date_str = "2024-Mar-09"

    # convert the string to a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")

    # get the year and month
    year = str(date_obj.year)
    month = date_obj.strftime("%B")
    # 
    return [year, month]

# 
import extract_weekdays as ew
import format as f
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton
# from kivy.uix.boxlayout import BoxLayout

# Define the screens
class ScreenOne(MDScreen):
    pass

class ScreenTwo(MDScreen):
    pass

class ClickableLabel(ButtonBehavior, MDLabel):
    pass

# Define the app
class MainApp(MDApp):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.manager_open = False
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=self.select_path,
    #     )

    file_manager = None
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

    def download_file(self, *args):
        # self.root.current = 'screen_two'
        toast('Downloading file {}'.format(*args))
        #
        global downld_dir_
        print('dirD',downld_dir_)
        def copy_file(*args):
            import shutil
            shutil.copy2(*args, downld_dir_)
        if not downld_dir_:
            toast('Select directory to download file')
            self.file_manager_open()
        else: copy_file(*args)
        # from plyer import filechooser

        # def pick_directory():
        #     path = filechooser.choose_dir(title="Choose Directory")
        #     if path:
        #         print(path[0])  # path is a list containing the chosen directory path

    ''' file manager '''
    def file_manager_open(self):
        if not self.file_manager:
            self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )
        self.file_manager.show(
            os.path.expanduser("~"))  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        # copy to selected directory
        global downld_dir_
        downld_dir_ = path
        #
        self.exit_manager()
        # 
        toast('Folder selected try again to download file')
        # shutil.copy2(path, self.selected_file)


    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    ''' file manager-end '''

    def show_date_picker(self, *args):
        def test(instance, value, *args, **kwargs):
            # toast('Date selected: {}'.format(value))
            print('Date selected: {}'.format(value))
            # set the selected date to the text field
            global date_selected
            date_selected=format_date(str(value))
            self.root.get_screen('screen_one').ids.text_field_date.text = f"{date_selected[0]}-{date_selected[1]}"
            # set hint text to "Date selected"
            self.root.get_screen('screen_one').ids.text_field_date.hint_text = 'Month selected'
            # print('Date selected: {}'.format(kwargs))
            # 
            # self.generate_exel()
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=test)
        # date_dialog.bind(on_save=print('lll'), on_cancel=self.download_file('p'))
        date_dialog.open()

    def generate_exel(self):
        # self.root.current = 'screen_two'
        #
        weekdays_ = ew.get_month_weekdays(date_selected[0], date_selected[1])
        global manpower , designation
        manpower = [self.root.get_screen('screen_one').ids.text_field_name.text+'\n'+self.root.get_screen('screen_one').ids.text_field_contact.text]
        designation = [self.root.get_screen('screen_one').ids.text_field_designation.text]
        #
        f.generate_format(month_days=weekdays_,year=date_selected[0],month=date_selected[1])
        f.add_data(manpower=manpower,designation=designation)
        
        f.save_workbook(file:=os.path.join(save_path,'Weekly roaster for '+date_selected[1]+' '+date_selected[0]+".xlsx"))
        #
        toast('Generating excel file')
        # 
        self.add_to_display(file)

    def add_to_display(self, *args):
        # self.root.current = 'screen_two'
        root = self.root.get_screen('screen_two').ids.box_display
        card = MDCard(size_hint={0.87, None}, height="60dp", pos_hint={"center_x": .5}, border_radius=10, elevation=1)
        box = BoxLayout(padding=dp(10))
        box.add_widget(ClickableLabel(text=os.path.basename(*args), halign='center', on_release=lambda instance: self.toast_t(*args)))
        box.add_widget(MDRaisedButton(text='Download', on_release=lambda instance: self.download_file(*args)))
        card.add_widget(box)
        root.add_widget(card)
        print(root.children)

    def toast_t(self, *args):
        toast(*args)
    
        # toast('Adding to display')
    def share(self, *args): ...
        # from plyer import share

        # share.file(path='/path/to/your/file', reason='Share file')
        # toast('Sharing file')


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
        left_action_items: [["arrow", lambda x: app.change_screen_two()]]
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
                    
                    MDTextField:
                        id: text_field_date
                        hint_text: "Example: 2024-03-01"
                        readonly: True
                        on_focus: if self.focus: app.show_date_picker()

                    MDRaisedButton:
                        text: 'Generate Excel file'
                        md_bg_color: app.theme_cls.primary_color
                        pos_hint: {'right': .9, 'y': .1}
                        on_release: app.generate_exel()
                        
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
        
        MDCard:
            size_hint: None, None
            size_hint: .9, 1
            pos_hint: {'center_x': .5, 'center_y': .2}
            elevation: 2
            ScrollView:
                do_scroll_x: False
                
                MDBoxLayout:
                    id: box_display
                    orientation: 'vertical'
                    size_hint: None, None
                    size_hint: 1, None
                    height: self.minimum_height
                    padding: [dp(5), dp(20), dp(5), dp(5)]
                    spacing: dp(4)

                    MDCard:
                        size_hint: 0.87, None
                        height: "60dp"
                        pos_hint: {"center_x": .5}
                        border_radius: 10
                        elevation: 1
                        BoxLayout:
                            padding: dp(10)
                            ClickableLabel:  
                                text: '2023-3-W'
                                halign: 'center'
                                on_release: app.download_file('2023-3-W') 
                            MDRaisedButton:
                                text: 'Download'
                                on_release: app.download_file()
                            
                    MDLabel:
                        text: ''
                    
                    MDLabel:
                        text: ''

        MDFloatingActionButton:
            icon: 'plus'
            md_bg_color: app.theme_cls.primary_color
            pos_hint: {'right': .9, 'y': .1}
            on_release: app.change_screen_one()

"""

# Run the app
if __name__ == '__main__':
    MainApp().run()