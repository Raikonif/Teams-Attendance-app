# from src.menu.menu_handler import handle_questions_menu, handle_question_input_data
from menu.menu_handler import handle_questions_menu, handle_question_input_data
def main():
    pass
    ## show `Questions menu + Quit option` while not Quit
    # selected_question is string or number or tuple or list or dictionary
    selected_question = handle_questions_menu()
    ## show `request Question input data + Quit option` while not Quit
    # selected_question is string or number or tuple or list or dictionary
    options = handle_question_input_data(selected_question)

    ## TODO: bussiness logic to read data + generate response + dislay and save 

main()