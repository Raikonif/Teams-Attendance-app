def question_menu(questions_list):
    for q in questions_list:
        print(questions_list.index(q)+1, q, sep=". ")
    print('Q. Quit')

def handle_questions_menu():
    counter = 0
    run = True
    array_questions = []
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
                selected_question == "q" and
                array_questions == []):
            run = False
            print("Quit, bye!")
            exit()
        elif (selected_question == "Q" or
                selected_question == "quit" or
                selected_question == "q" and
                array_questions != []):
            run = False
            print("Quit, bye!")
            return array_questions

        elif (selected_question == "1" or
              selected_question == "2"):
            array_questions.append(questions_lists[int(selected_question)-1])
            counter += 1
            print("Question selected: ", selected_question)
            print("Questions selected: ", array_questions)
            print("counter: ", counter)
    return selected_question


def handle_question_input_data(selected_question):
    counter = 0
    run = True
    while run:
        print("=======REQUESTED QUESTIONS:")
        for question in selected_question:
            counter += 1
            print(f"question: {counter}", question)

        print("Q. Quit")
        print("===========================")

        input_user = input("Select a question (Q to quit): ")
        counter = 0
        for q in selected_question:
            if (input_user == selected_question.index(q)):
                print("===========================")
                participants = input("Enter the number of participants: ")
                print("===========================")
            elif(input_user == "Q" or
                input_user == "quit" or
                input_user == "q"):
                run = False
                print("Quit, bye!")
                exit()

        

        
            
            
        
