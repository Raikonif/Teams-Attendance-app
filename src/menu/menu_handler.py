def handle_questions_menu():
    counter = 0
    run = True
    array_questions = []
    data_question = {
        "meeting_name":'',
        "start_date":'',
        "end_date":'',
    }
    questions_lists = [
        "What is the number of Partipants attending General Meeting per date, " 
    "date filter between 9/12/2022 and 9/16/2022?",
    "What is the Meeting duration of General Meeting per date, " 
    "date filter between between 9/12/2022 and 9/16/2022?"
    ]
    for q in questions_lists:
        print(questions_lists.index(q), q)
    print("""MENU OPTIONS:
    1. What is the number of Partipants attending General Meeting per date, 
    date filter between 9/12/2022 and 9/16/2022?
    2. What is the Meeting duration of General Meeting per date, 
    date filter between between 9/12/2022 and 9/16/2022?
    Q. Quit""")
    while run:
        selected_question = input("Select a question Q to quit: ")

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
            array_questions.append(selected_question)
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
                print ("selected question: ", q)
                print("===========================")
            elif(input_user == "Q" or
                input_user == "quit" or
                input_user == "q"):
                run = False
                print("Quit, bye!")
                exit()

        

        
            
            
        
