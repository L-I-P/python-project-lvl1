from random import randint
import prompt


def welcome_user() -> str:
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def hi():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def question() -> bool:
    random_number = randint(1, 100)
    print('Question: {}'.format(random_number))
    print('Your answer: ', end='')
    answer_user = str(input())
    if random_number % 2 == 0:
        if answer_user == 'yes':
            print('Correct!')
            return True
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return False
    else:
        if answer_user == 'no':
            print('Correct!')
            return True
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False


def logic() -> bool:
    hi()
    count_true_answer = 1
    while question() and count_true_answer != 3:
        count_true_answer += 1
    if count_true_answer == 3:
        return True
    return False


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if logic():
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
