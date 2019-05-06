quest = 0
right_ans = 0
test = open('questions.txt', 'r')
while True:
    question = test.readline().strip()
# if test list end - close the file and break the endless cycle
    if not question:
        test.close()
        break
# read every line of the test file 
    answer1 = test.readline().strip()
    answer2 = test.readline().strip()
    answer3 = test.readline().strip()
    answer4 = test.readline().strip()
    key = test.readline().strip()

    print(question)
    print('  ' + answer1)
    print('  ' + answer2)
    print('  ' + answer3)
    print('  ' + answer4)
    right = str(input('Введіть Ваш варіант правильної відповіді та натисніть Enter\n'))
    
    quest = quest + 1
# if the answer is right, we increase the number of faithful answers
    if right == key:
        right_ans = right_ans + 1

print('Ви дали ' + str(right_ans) + ' правильних відповідей з ' + str(quest) + ' питань.')
