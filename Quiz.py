class Game: 
    print('We test how intelligent you are')
    def play_or_not():
        playgame_or_not = input('Are you ready to play this game (yes/no)? ')
        if playgame_or_not == 'yes':
            game()
        else:
            print('Okay')
            quit()

    def game():
        user_ans_list = []
        correct_ans_list = list(questions_answers.values())
        correct = 0
        print('Answer the following questions')
        for key in questions_answers:
            print(key)
            user_ans = input('Answer: ')
            user_ans_list.append(user_ans)
            correct += check_answer(user_ans, questions_answers.get(key))
        display_score(user_ans_list,correct_ans_list,correct)
        play_again()

    def check_answer(user_ans,correct_ans):
        if user_ans == correct_ans:
            print('Correct')
            return 1
        else:
            print('Wrong')
            return 0

    def display_score(user_ans_list,correct_ans_list,correct):
        print('Your answers are :')
        for i in user_ans_list:
            print(i,end='\n')
        print('--------------')
        print('The main answers are: ')
        for i in correct_ans_list:
            print(i,end='\n')
        if correct == len(questions_answers):
            print(f'Hurray!!! You had everything right')
        else:
            print(f'You had {correct}/{len(questions_answers)} correct')


    def play_again():
        playAgain = input('Would you like to play again(yes/no)? ')
        if playAgain == 'yes':
            game()
        else:
            quit()

    questions_answers = {
        'What year did Ghana win independence? ':'1957',
        'Who is the current president of Ghana? ':'Nana Akuffo Addo',
        'How many regions are in Ghana? ':'16',
        'What is the capital of Ghana? ':'Accra'
    }
    play_or_not()