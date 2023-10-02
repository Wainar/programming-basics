users_input_seconds = int(input("Insert number of seconds: "))

days = users_input_seconds // 86400
users_input_seconds -= days * 86400

hours = users_input_seconds // 3600
users_input_seconds -= hours * 3600

minutes = users_input_seconds // 60
users_input_seconds -= minutes * 60

print(str(days) + ':' + str(f'{hours:0>2}') + ':' + str(f'{minutes:0>2}') + ':' + str(f'{users_input_seconds:0>2}'))