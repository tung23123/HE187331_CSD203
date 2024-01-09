base_10 = [8.5, 8.0, 7.0, 6.5, 5.5, 5.0, 4.0, 3.9]
base_letter = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
base_4 = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

# PROMPT POINT IN BASE 10:
grade = input('Enter your grade in decimal base(0.0-10.0): ')
while True:
    try:
        grade = round(float(grade),1)
    except:
        grade = input('Re-Enter your grade in decimal base(0.0-10.0): ')
    if type(grade) == float and 0 <= grade <= 10.0:
        break
    else:
        grade = input('Please enter a number (0.0 - 10.0): ')

# MAPPING POINT
for grade_check in base_10:
    if not grade >= grade_check:
        continue
    else:
        pos = base_10.index(grade_check)
        break
    
print('Your grade in 10-base is {} \nYour grade in 4-base is {} \nYour grade in letter is {}'.format(grade, base_4[pos], base_letter[pos]))


