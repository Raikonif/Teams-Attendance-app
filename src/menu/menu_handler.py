from datetime import datetime,date


def question_menu(questions_list):
    for q in questions_list:
        print(questions_list.index(q)+1, q, sep=". ")


def filter_dates(first_date, last_date):
    first_date_strip = first_date.split('/')
    last_date_strip = last_date.split('/')
    sum_days = abs(int(first_date_strip[1]) - int(last_date_strip[1]))
    sum_months = abs(int(first_date_strip[0]) - int(last_date_strip[0]))
    sum_years = abs(int(first_date_strip[2]) - int(last_date_strip[2]))
    print("DAYS ", sum_days)
    print("MONTHS", sum_months)
    print("YEARS", sum_years)
    if(sum_days > 0 and sum_months == 0 and sum_years == 0):
        date_list = [
            current_date for current_date in range(int(first_date_strip[1]), int(last_date_strip[1])+1)
            ]
        
    print(date_list)
    

    # sum_months = abs(int(first_date[1]) - int(last_date[1]))
    # sum_years = abs(int(first_date[2]) - int(last_date[2]))
    # print("{}, {}, {}".format(sum_days, sum_months, sum_years))

def handle_questions_menu():
    run = True
    question_selected = ''
    meeting_title = ''
    data_datetime = {
        "start_date":'9/12/2022',
        "end_date":'9/16/2022',
        "participants":0,
    }
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

    pass


def handle_question_input_data(question_selected):
    run = True
    print("===========================================")
    print("REQUESTED QUESTIONS:")
    print(question_selected)
    print("===========================================")
    print('We print the Result of the read the Csv file')
    while run:
        input_user = input("Wanna do another question? Y/N: ")
    
        if input_user == "Y" or input_user == "y":
            print("""
        
                RETURNING TO THE MAIN MENU
        
            """)
            run = False
            return True

        elif input_user == "N" or input_user == "n": 
            run = False
            return False
    
        else:
            print("Invalid option, try again")
            run = True
        
        

        

        
            
            
        
