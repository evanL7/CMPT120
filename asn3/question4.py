'''
 This program grades the user's exam using a predefined list of correct answers and
 determines if the student has passed or failed and details the answers that were incorrect.
'''

# This function changes the student's answers to a nested list so that the question number and the student's answer are paired together
def change_stu_ans_to_list():
    student_answers = []
    file = open("answers.txt","r")
    count = 1 # This variable keeps count of the question number
    for choice in file:
        choice = choice.strip() # This line removes the end of line character and any potential spaces in front of the student's choice
        if choice == "": # This line ensures that empty lines in the text file are not included in the list
            continue
        # Since our correct answers are uppercase, we use the upper method call on the student's answers to match the uppercase text
        student_answers.append([count,choice.upper()]) # Here we append a list that contains the question number and the student's answer to a nested list
        count += 1
    file.close()
    return student_answers

# This function changes the correct answers to a nested list so that the question number and the correct answer are paired together
def change_correct_ans_to_list():
    # These are the correct answers in order
    correct_answers = ['A', 'D', 'B', 'A', 'C', 'D', 'A', 'D', 'C', 'C', 'D', 'D', 'B', 'C', 'A', 'B', 'C', 'D', 'D', 'B']
    count = 0
    for letter in correct_answers:
        correct_answers[count] = [count + 1, letter] # This line changes the correct answers list to a nested list that shows the question number and the correct answer
        count += 1
    return correct_answers

# This function checks the student's answer and checks if their answer is wrong and if it is, appends the incorrect answer to the list
def wrong_answers(correct_ans,stu_ans):
    wrong_ans_list = []
    for pairs in range(len(stu_ans)):
        if correct_ans[pairs] == stu_ans[pairs]: # If the student's answer is correct, we just continue to the next item
            continue
        wrong_ans_list.append(stu_ans[pairs]) # This line appends the wrong answer to the list which includes the question number and the student's answer
    return wrong_ans_list

# This function validates the student's answer and checks if their answer is correct, and if it is adds the item to the list
# so that we can count the total number of correct answers the student got
def correct_answers(correct_ans,stu_ans):
    correct_ans_list = []
    for pairs in range(len(stu_ans)):
        if correct_ans[pairs] == stu_ans[pairs]: # If the answer is correct, append their answer to the correct answer list
            correct_ans_list.append(stu_ans[pairs])
    return correct_ans_list

def main():
    try:
        student_choices = change_stu_ans_to_list() # Stores a nested list of pairs of the student's choices
        correct_choices = change_correct_ans_to_list() # Stores a nested list of pairs of the correct answers
    except FileNotFoundError: # This line ensures that if the answers.txt file doesn't exist, the user is informed
        print('''File not found! Please ensure there exists an "answers.txt" text file within this file's directory.''')
        return
    except: # This line captures any other potential errors that may arise.
        print("There is an error. Please check the text file.")
        return

    student_wrong_ans = wrong_answers(correct_choices,student_choices) # Stores a nested list of pairs of the student's wrong answers
    student_right_ans = correct_answers(correct_choices,student_choices) # Stores a nested list of pairs of the student's correct answers

    print("Correctly Answered Questions:", len(student_right_ans))
    print("Incorrectly Answered Questions:", len(student_wrong_ans))
    print()

    # This condition applies only if the student got all the questions correct and therefore we do not need to format the student's incorrect answers
    if len(student_right_ans) == 20: 
        print("You passed the exam.")
        return

    print("Incorrect Answers and Solutions:")
    # This loop is used to display the question number the student got wrong, the student's answer, and the correct answer
    for item in student_wrong_ans:
        
        # This loop searches for the correct answer to show the user what the correct answer should have been
        for pair in correct_choices:
            if item[0] == pair[0]:
                correct_pair = pair
        print("Question", str(item[0]) + ":\n  Your Answer:",item[1],"\n  Correct Answer:",correct_pair[1])
        print()
    
    if len(student_right_ans) >= 15: # If the student has 15 or more correct answers, they pass the exam
        print("You passed the exam.")
        return
    else:
        print("You failed the exam.")
        return

main()
