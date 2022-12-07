from enum import Enum

choice = ''


class Choice(Enum):
    Add = 'A'
    Insert = 'I'
    Search = 'S'
    Quit = 'Q'


def welcome():
    print('===================================================================')
    print('Welcome to the student and assesment management system')
    print('<Add> Enter A to add details of a student.')
    print('<Insert> Enter I to insert assignment marks of a student.')
    print('<Search> Enter S to search assesment marks of a student.')
    print('<Quit> Enter Q to quit.')
    print('===================================================================')


def take_user_choice():
    return input().upper()


def validate_choice(choice):
    try:
        Choice(choice)
        return True
    except ValueError:
        print('You gave a wrong choice')
        return False


def initial_screen():
    welcome()
    global choice
    choice = take_user_choice()
    if not validate_choice(choice):
        return False

    return True


if __name__ == '__main__':
    while initial_screen():
        if Choice(choice) == Choice.Quit:
            print('Good bye!!!')
            break
