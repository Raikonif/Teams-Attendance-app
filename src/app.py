# from src.menu.menu_handler import handle_questions_menu, handle_question_input_data
from menu.menu_handler import *
from datetime import date
initial_date = '9/12/2022'
final_date = '9/16/2022'

def main():
    options = True
    ## show `Questions menu + Quit option` while not Quit
    # selected_question is string or number or tuple or list or dictionary
    while options:
        selected_question = handle_questions_menu()
    ## show `request Question input data + Quit option` while not Quit
    # selected_question is string or number or tuple or list or dictionary
        date_list_selected = filter_dates(initial_date, final_date)
        options = handle_question_input_data(selected_question)
    

    ## TODO: bussiness logic to read data + generate response + dislay and save 

main()