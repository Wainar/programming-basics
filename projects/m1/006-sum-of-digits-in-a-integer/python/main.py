integer_num = int(input('Please enter a fourth-digits number: '))

string_num = str(integer_num)

if len(string_num) !=4:
    print('You have to enter a fourth digits number.')

else:
    sum_of_digits = int(string_num[0])+int(string_num[1])+int(string_num[2])+int(string_num[3])
    print('The digits sum of the number', integer_num,'is', sum_of_digits)