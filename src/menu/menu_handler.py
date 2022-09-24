from datetime import datetime,date





def filter_dates(first_date, last_date):
    first_date_split = first_date.split('/')
    last_date_split = last_date.split('/')
    date_list = []
    sum_days = abs(int(first_date_split[1]) - int(last_date_split[1]))
    sum_months = abs(int(first_date_split[0]) - int(last_date_split[0]))
    sum_years = abs(int(first_date_split[2]) - int(last_date_split[2]))
    if(sum_days > 0 and sum_months == 0 and sum_years == 0):
        for current_date in range(int(first_date_split[1]), int(last_date_split[1])+1):
            date_list.append('{}/{}/{}'.format(current_date, first_date_split[0], first_date_split[2]))
            print("{}/{}/{}".format(current_date,first_date_split[0],first_date_split[2]))
    return date_list


def question_menu(questions_list):
    for q in questions_list:
        print(questions_list.index(q)+1, q, sep=". ")


def handle_questions_menu():
    run = True
    question_selected = ''
    meeting_title = ''
    questions_list = [
        "What is the number of Partipants attending General Meeting per date, " 
    "date filter between 9/12/2022 and 9/16/2022?",
    "What is the Meeting duration of General Meeting per date, " 
    "date filter between between 9/12/2022 and 9/16/2022?"
    ]

    question_menu(questions_list)
    
    while run:
        selected_question = input("Select a question or Q to quit: ")

        if (selected_question == "Q" or
            selected_question == "quit" or
                selected_question == "q"):
            run = False
            print("Quit, bye!")
            exit()

        elif (selected_question == "1" or
              selected_question == "2"):
            question_selected = questions_list[int(selected_question)-1]
            print("Question selected: ", question_selected)
            run = False
        else :
            print("Invalid option, try again")

    return question_selected

def get_data_from_csv():
    with open('data.csv', mode="r") as file:
        data = file.read()
        print(data)
    print("We read the Csv file")


def handle_question_input_data(question_selected):
    run = True
    print("===========================================")
    print("REQUESTED QUESTIONS:")
    print(question_selected)
    print("===========================================")
    get_data_from_csv()
    while run:
        input_user = input("Wanna do another question? Y/N: ")
    
        if input_user == "Y" or input_user == "y":
            print("""
        
                RETURNING TO THE MAIN MENU
        
            """)
            run = False
            return True

        elif input_user == "N" or input_user == "n": 
            print("Quit, bye!")
            run = False
            return False
    
        else:
            print("Invalid option, try again")
            run = True
        
        

        

        
            
            
        
