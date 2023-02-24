from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup


Builder.load_file('re_inv_calc.kv')
Window.size = (400,600)

class re_inv:
    def __init__(self, percent_month, num_months, fixed_per_month):
        self.percent_month = percent_month
        self.num_months = num_months
        self.fixed_per_month = fixed_per_month

    
    def final_amount(self, initial_val):
        i = 0
        while i < float(self.num_months):
            passive_rev = percentage(float(self.percent_month), float(initial_val))
            initial_val = float(initial_val) + float(passive_rev) + float(self.fixed_per_month)
            
            i += 1
        final_amount = initial_val
        return final_amount      
    
    def profits_based_entry(self, initial_val):
        return self.final_amount(initial_val) - float(initial_val)
    
    def profits_not_based_entry(self, initial_val):
        return self.final_amount(initial_val) - float(initial_val) - (float(self.fixed_per_month)*float(self.num_months))
    
    def time_passive_income(self, initial_val, targeted_passive):
        passive_rev = 0
        months_for_passive = 0
        while float(targeted_passive) > passive_rev:
            passive_rev = percentage(self.percent_month, float(initial_val))
            initial_val = float(initial_val) + float(passive_rev) + float(self.fixed_per_month)
            months_for_passive += 1
        return months_for_passive

class no_re_inv:
    def __init__(self, percent_month, num_months, fixed_per_month):
        self.percent_month = percent_month
        self.num_months = num_months
        self.fixed_per_month = fixed_per_month

    def final_amount(self, initial_val):
        i = 0
        accumulation = 0
        while i < float(self.num_months):
            passive_rev = percentage(self.percent_month, initial_val)
            initial_val = float(initial_val) + float(self.fixed_per_month)
            accumulation = accumulation + passive_rev
            i += 1
        final_amount = initial_val + accumulation
        return final_amount 
          
    def profits_based_entry(self, initial_val):
        return self.final_amount(initial_val) - float(initial_val)
    
    def profits_not_based_entry(self, initial_val):
        return self.final_amount(initial_val) - float(initial_val) - (float(self.fixed_per_month)*float(self.num_months))
    
    def time_passive_income(self, initial_val, targeted_passive):
        passive_rev = 0
        months_for_passive = 0
        while float(targeted_passive) > passive_rev:
            passive_rev = percentage(self.percent_month, float(initial_val))
            initial_val = float(initial_val) + float(self.fixed_per_month)
            months_for_passive += 1
        return months_for_passive
    
def diff_in_profits(x, y):
    if x > y:
        difference = x - y
        percent = (difference / y) * 100
        return percent
    else:
        return print('Error')
    
def percentage(percent, whole):
    return (float(percent) * float(whole)) / 100


class MyLayout(Widget):

    #functions to get stuff
    def get_entry(self):
        return float(self.ids.entry_input.text)
    def get_return_month(self):
        return float(self.ids.return_per_month_input.text)
    def get_num_months(self):
        return float(self.ids.n_months_input.text)
    def get_fixed_per_month(self):
        return float(self.ids.reccurence_inv_input.text)
    def get_target_passive_inc(self):
        return float(self.ids.target_passive_income_input.text)
    
    
    #functions to calculate stuff re_inv
    def re_inv_calc_final_amount(self):
        entry = self.get_entry()
        p1 = re_inv(self.get_return_month(), self.get_num_months(),self.get_fixed_per_month()).final_amount(entry)
        return p1
    def re_inv_calc_profits_not_based_entry(self):
        entry = self.get_entry()
        p2 = re_inv(self.get_return_month(), self.get_num_months(),self.get_fixed_per_month()).profits_not_based_entry(entry)
        return p2
    def re_inv_calc_time_passive_income(self):
        entry = self.get_entry()
        target_passive = self.get_target_passive_inc()
        p3 = re_inv(self.get_return_month(), self.get_num_months(),self.get_fixed_per_month()).time_passive_income(entry, target_passive)
        return p3
    

    #functions to calculate stuff no_re_inv
    def no_re_inv_calc_final_amount(self):
        entry = self.get_entry()
        p4 = no_re_inv(self.get_return_month(), self.get_num_months(),self.get_fixed_per_month()).final_amount(entry)
        return p4
    def no_re_inv_calc_profits_not_based_entry(self):
        entry = self.get_entry()
        p5 = no_re_inv(self.get_return_month(), self.get_num_months(),self.get_fixed_per_month()).profits_not_based_entry(entry)
        return p5
    def no_re_inv_calc_time_passive_income(self):
        entry = self.get_entry()
        target_passive = self.get_target_passive_inc()
        p6 = no_re_inv(self.get_return_month(), self.get_num_months(),self.get_fixed_per_month()).time_passive_income(entry, target_passive)
        return p6
    

    #function to open popup
    def pls_open(self):
        try:
            re_inv_f_amount = str(round(self.re_inv_calc_final_amount(), 2))
            re_inv_profits = str(round(self.re_inv_calc_profits_not_based_entry(), 2))
            re_inv_time_passiv = str(self.re_inv_calc_time_passive_income())

            no_re_inv_f_amount = str(round(self.no_re_inv_calc_final_amount(), 2))
            no_re_inv_profits = str(round(self.no_re_inv_calc_profits_not_based_entry(), 2))
            no_re_inv_time_passiv = str(self.no_re_inv_calc_time_passive_income())

            targeted = self.ids.target_passive_income_input.text
            n_months = self.ids.n_months_input.text

            difference_in_profits_percentage = diff_in_profits(self.re_inv_calc_profits_not_based_entry(), self.no_re_inv_calc_profits_not_based_entry())

            diff_in_months = (float(no_re_inv_time_passiv) - float(re_inv_time_passiv))

            # create an instance of the popup
            popup = MyPopup(re_inv_f_amount, re_inv_profits, re_inv_time_passiv, no_re_inv_f_amount, no_re_inv_profits, no_re_inv_time_passiv, n_months, targeted, difference_in_profits_percentage, diff_in_months)
            # open the popup
            popup.open()
        except ValueError:
            # If the user input is not a valid float, show an error message in a popup
            error_popup = Popup(title='Error', content=Label(text='Please enter a valid number'), size_hint=(None, None), size=(400, 400))
            error_popup.open()


class MyPopup(Popup):
    def __init__(self, re_inv_f_amount, re_inv_profits, re_inv_time_passiv, no_re_inv_f_amount, no_re_inv_profits, no_re_inv_time_passiv, n_months, targeted, difference_in_profits_percentage, diff_in_months, **kwargs):
        super().__init__(**kwargs)
        self.ids.popup_label_re_inv.text = f'The final amount is: [b]R$ {re_inv_f_amount}[/b] \nand your profits after {n_months} months are: [b]R$ {re_inv_profits}[/b] \nit will take [b]{re_inv_time_passiv}[/b] months to reach at least [b]R$ {targeted}[/b]'
  
        self.ids.popup_label_no_re_inv.text = f'The final amount is [b]R$ {no_re_inv_f_amount}[/b] \nand your profits after {n_months} months are: [b]R$ {no_re_inv_profits}[/b] \nit will take [b]{no_re_inv_time_passiv}[/b] months to reach at least [b]R$ {targeted}[/b]'

        self.ids.diff.text = f'The percent difference in profits is [color=00ff00]{round(difference_in_profits_percentage, 2)}%[/color] \nAnd without re-investing it will take [color=FF0000]{round(diff_in_months)} more months[/color] \nto achieve [b]R$ {targeted}[/b] passive income per month'

      
  

class ReInvCalcApp(App):
    def build(self):
        return MyLayout()
    

if __name__ == '__main__':
    ReInvCalcApp().run()