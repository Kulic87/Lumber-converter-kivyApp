from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.tab import MDTabsBase

def first_tab(h, w, l, n, p):
    '''Count lumber in cubic meters and count value of lumber in ruble'''
    lumber_in_cubic_meters = float(round((h / 1000) * (w / 1000) * l * n, 2))
    value_in_rubles = float(round(lumber_in_cubic_meters * p, 2))

    return {'lumber_in_cubic_meters': str(lumber_in_cubic_meters),
            'value_in_rubles': str(value_in_rubles)}


def second_tab(h, w, l, cub_m, p):
    '''Count number lumber from volume lumber and count value of lumber in ruble'''
    try:
        number_second = float(round(cub_m / ((h / 1000) * (w / 1000) * l), 2))
        value_in_rubles_second = float(round(cub_m * p, 2))
    except ZeroDivisionError:
        number_second = 0
        value_in_rubles_second = 0

    return {'number_second': str(number_second),
            'value_in_rubles_second': str(value_in_rubles_second)}

class Container(GridLayout):
    def calculate(self):
        '''Return values:
        - lumber_in_cubic_meters
        - value_in_rubles
         in text field of app '''
        try:
            text_field_height = float(self.text_field_height.text)
            text_field_width = float(self.text_field_width.text)
            text_field_length = float(self.text_field_length.text)
            text_field_number = float(self.text_field_number.text)
            text_field_price = float(self.text_field_price.text)
        except:
            text_field_height = 0
            text_field_width = 0
            text_field_length = 0
            text_field_number = 0
            text_field_price = 0
        var_tab = first_tab(text_field_height, text_field_width, text_field_length,
                            text_field_number, text_field_price)

        self.lumber_in_cubic_meters.text = var_tab.get('lumber_in_cubic_meters')
        self.value_in_rubles.text = var_tab.get('value_in_rubles')

    def calculate_2(self):
        '''Return values:
        - number_second
        - value_in_rubles_second
         in text field of app '''
        try:
            text_field_height_2 = int(self.text_field_height_2.text)
            text_field_width_2 = int(self.text_field_width_2.text)
            text_field_length_2 = int(self.text_field_length_2.text)
            number_cubic_meters = float(self.number_cubic_meters.text)
            text_field_price_2 = float(self.text_field_price_2.text)
        except:
            text_field_height_2 = 0
            text_field_width_2 = 0
            text_field_length_2 = 0
            text_field_price_2 = 0
            number_cubic_meters = 0

        var_tab_2 = second_tab(text_field_height_2, text_field_width_2,
                               text_field_length_2, number_cubic_meters,
                               text_field_price_2)

        self.number_second.text = var_tab_2.get('number_second')
        self.value_in_rubles_second.text = var_tab_2.get('value_in_rubles_second')


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


class MainApp(MDApp):
    title = 'Считаем пиломатериал'
    def build(self):
        return Container()

    def on_start(self):
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.prymary_hue = '900'

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.
        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        pass


MainApp().run()
