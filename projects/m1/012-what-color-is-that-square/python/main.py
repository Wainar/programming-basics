#Target focus "The letter identifies the column, while the number identifies the row by the User!"
blackwhite_column_input = str(input("Please select the column black or white for examples(a1-h8)to start: ")).lower()

black_column = ["a", "c", "e", "g"]
white_column = ["b", "d", "f", "h"]

letter = blackwhite_column_input[0]
row_number = int(blackwhite_column_input[1])

if letter in black_column:
    if row_number %2 == 0:
        print("The square is white")
    else:
        print("The square is black")
elif letter in white_column:
    if row_number %2 == 0:
        print("The square is black")
    else:
        print("The square is white")