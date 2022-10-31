from datetime import datetime

odds = [1, 2, 5, 7,33,44]
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("achei")
else:
    print(right_this_minute)
    print("não achei")
