import random


def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    question = (f'\nСкільки буде {num1} {operator} {num2}?\nВведіть відповідь: ')
    if operator == '/':
        while num1 % num2 != 0:
            num1 = random.randint(1, 50)
            num2 = random.randint(1, 50)
        question = (f'\nСкільки буде {num1} {operator} {num2}?\nВведіть відповідь: ')
    return question, eval(f'{num1}{operator}{num2}')


def ask(question):
    return input(question)


def evaluate_answer(user_answer, correct_answer):
    if user_answer.lower() == 'quit':
        return 'quit'
    elif int(user_answer) == correct_answer:
        print('Правильно!',)
        return True
    else:
        print('Неправильно!')
        print('Вірна відповідь:',correct_answer)
        return False

def finish(user_input):
    if user_input.lower() == 'quit':
        print("Гра завершена користувачем!")
        return True
    return False

def start():
    print("Шалом! Давайте тренувати ваші арифметичні навички↓")
    correct_answers = 0
    hearts = 3
    incorrect_answers = 0
    total_questions = 10

    while hearts > 0:
        question, correct_answer = generate_numbers()
        user_answer = ask(question)
        if finish(user_answer):
            break
        elif evaluate_answer(user_answer, correct_answer):
            correct_answers += 1
            print('Поточний рахунок: ', correct_answers)
            print('Кількість ваших сердечок❤️: ', hearts)
        else:
            incorrect_answers += 1
            hearts -= 1
            print(f"Ви втратили одне сердечко💔! Залишилось сердечок❤️: {hearts}")
            print('Поточний рахунок: ', correct_answers)

    def textt(text):
        print("\033[34m{}".format(text))
    textt("Game Over!")

    print(f"Ви відповіли правильно на {correct_answers} з {total_questions} питань! Та {incorrect_answers} неправильних!")
    print('Ваш остаточний рахунок: ', correct_answers)
if __name__ == "__main__":
    start()