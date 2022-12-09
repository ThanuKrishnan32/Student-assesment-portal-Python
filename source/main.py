from enum import Enum
import os

choice = ''
student_id = ''
student_name = ''
course = ''
to_continue = True


class Choice(Enum):
    Add = 'A'
    Insert = 'I'
    Search = 'S'
    Quit = 'Q'


def welcome():
    print('='*60)
    print('Welcome to the student and assessment management system')
    print('=' * 60)
    print('<Add> Enter A to add details of a student.')
    print('<Insert> Enter I to insert assignment marks of a student.')
    print('<Search> Enter S to search assessment marks of a student.')
    print('<Quit> Enter Q to quit.')
    print('='*60)


def check_whether_to_continue(display_text):
    global to_continue, choice, student_id
    user_choice = take_user_input(display_text, 1)
    if user_choice == 'Y' or user_choice == 'y':
        to_continue = True
    elif user_choice == 'N' or user_choice == 'n':
        choice = ''
        student_id = ''
    else:
        print('Please enter either Y or N')
        check_whether_to_continue(display_text)


def take_user_input(display_str='', val=0):
    if val == 0:
        return input().upper()
    else:
        return input(display_str)


def validate_choice(user_choice):
    global choice
    try:
        choice = Choice(user_choice)
        return True
    except ValueError:
        print('You gave a wrong choice')
        return False


def initial_screen():
    global choice
    welcome()
    user_choice = take_user_input()
    if not validate_choice(user_choice):
        initial_screen()
    return True


def write_to_file(filename, data):
    if os.path.isfile(filename):
        mode = 'a'
        data_to_write = '\n' + ','.join([str(i) for i in data])
    else:
        mode = 'w'
        data_to_write = ','.join([str(i) for i in data])
    with open(filename, mode=mode) as f:
        f.write(data_to_write)
    print(f'The record has been successfully added to the {filename} file.')


def add_student():
    global student_id, student_name, course
    student_id = take_user_input('Please enter the student ID: ', 1)
    student_name = take_user_input('Please enter the student name: ', 1)
    course = take_user_input('Please enter the course: ', 1)
    print('Thank you')
    print('The details of the student you entered are as follows: ')
    print('Student ID: ', student_id)
    print('Student Name: ', student_name)
    print('Course: ', course)
    write_to_file('students.txt', [student_id, student_name, course])
    check_whether_to_continue('Do you want to enter details for another student (Y/N)? ')
    # TODO validation


def insert_assessment():
    global student_id
    if student_id == '':
        student_id = take_user_input('Please enter the student ID: ', 1)
    subject_code = take_user_input('Please enter the subject code: ', 1)
    assessment_no = take_user_input('Please enter the assessment no: ', 1)
    assessment_marks = take_user_input('Please enter the assessment marks: ', 1)
    print('Thank you')
    print('The details of the student you entered are as follows: ')
    print('Student ID: ', student_id)
    print('subject_code: ', subject_code)
    print('assessment_no: ', assessment_no)
    print('assessment_marks: ', assessment_marks)
    write_to_file('assessments.txt', [student_id, subject_code, assessment_no, assessment_marks])
    check_whether_to_continue('Do you want to enter marks for another assessment (Y/N)? ')
    # TODO validation


if __name__ == '__main__':
    while to_continue:
        if not choice:
            initial_screen()
        if choice == Choice.Quit:
            print('Good bye!!!')
            break
        elif choice == Choice.Add:
            add_student()
        elif choice == Choice.Insert:
            insert_assessment()
        elif choice == Choice.Search:
            pass
