from datetime import datetime,date
import os
from pathlib import Path

MEETING_TITLE = 'Meeting Title'
PARTICIPANTS = 'Total Number of Participants'
MEETING_START = 'Meeting Start Time'
MEETING_END = 'Meeting End Time'

def filter_dates(first_date, last_date):
    first_date_split = first_date.split('/')
    last_date_split = last_date.split('/')
    date_list = []
    sum_days = abs(int(first_date_split[1]) - int(last_date_split[1]))
    sum_months = abs(int(first_date_split[0]) - int(last_date_split[0]))
    sum_years = abs(int(first_date_split[2]) - int(last_date_split[2]))
    if(sum_days > 0 and sum_months == 0 and sum_years == 0):
        for current_date in range(int(first_date_split[1]), int(last_date_split[1])+1):
            formatted_date = '{}/{}/{}'.format(current_date, first_date_split[0], first_date_split[2])
            date_list.append(formatted_date)
            print(formatted_date)

    return date_list


def question_menu(questions_list):
    for q in questions_list:
        print(questions_list.index(q)+1, q, sep=". ")


def handle_questions_menu():
    meeting_title = ''
    questions_list = [
        "What is the number of Partipants attending General Meeting per date, " 
    "date filter between 9/12/2022 and 9/16/2022?",
    "What is the Meeting duration of General Meeting per date, " 
    "date filter between between 9/12/2022 and 9/16/2022?"
    ]

    question_menu(questions_list)
    
    question_selected = resolve_option_menu_selected(questions_list)
    
    return question_selected


def resolve_option_menu_selected(questions_list):
    run = True
    question_selected = ''
    dict_question_selected = {}
    while run:
        selected_question = input("Select a question or Q to quit: ")

        if (selected_question == "Q" or
            selected_question == "quit" or
                selected_question == "q"):
            run = False
            print("Quit, bye!")
            exit()
        
        elif (selected_question.isdigit() and int(selected_question) < len(questions_list)):
            question_selected = questions_list[int(selected_question)-1]
            dict_question_selected[int(selected_question)] = question_selected
            print('Dict', dict_question_selected)
            print("Question selected: ", question_selected)
            run = False
        
        else:
            print("Invalid option, try again")

    return dict_question_selected
    # return question_selected


def finding_files():
    output = []
    with os.scandir("../attendace_reports/") as dirs:
        for entry in dirs:
            if entry.is_dir():
                get_csv_list(output, entry)
    
    return output
    print("We read the Csv file")


def get_csv_list(output, entry):
    with os.scandir(entry) as files:
        for file in files:
            if file.is_file() and file.name.endswith(".csv"):
                output.append(file)
    

def answer_questions(file_list, meeting_title, participants):
    current_participants = 0
    current_title = ''
    list_of_meetings = []
    for file in file_list:
        with open(file, 'r', encoding='UTF-16') as f:
            for line in f.readlines():
                if line.find(meeting_title) != -1:
                    current_title = line
                    current_title_formatted = current_title.strip('\n').split('\t')[1]
                
                elif line.find(participants) != -1:
                    current_participants = line
                    current_participants_formatted = current_participants.strip('\n').split('\t')[1]
            list_meeting_result = handle_result_data_formatted(
                current_participants_formatted, 
                current_title_formatted, 
                list_of_meetings
                )
    print("===========================================")
    print(list_meeting_result)

def handle_result_data_formatted(participants_formatted, title_formatted, list_of_meetings):
    dict_meeting = {
        'meeting_title': '',
        'participants': 0
    }
    dict_meeting['meeting_title'] = title_formatted
    dict_meeting['participants'] = participants_formatted
    list_of_meetings.append(dict_meeting)
    return list_of_meetings


def handle_question_input_data(question_selected):
    run = True
    print("===========================================")
    print("REQUESTED QUESTIONS:")
    value = [print(value) for value in question_selected.values()]
    print("===========================================")
    file_list = finding_files()
    answer_questions(file_list, MEETING_TITLE, PARTICIPANTS)

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
        
        

        

        
            
            
        
