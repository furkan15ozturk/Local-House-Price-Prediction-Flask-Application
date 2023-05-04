import re

room = "3.5 + 1"
room_value = 0
numbers = re.findall(r'\d+\.\d+|\d+', room)
if len(numbers) == 2:
    room_value = eval(numbers[0] + '+' + numbers[1])
elif len(numbers) == 1:
    room_value = int(numbers[0])
else:
    room_value = None
print(room_value)
