from datetime import datetime

""" This countdown project will count the number of days, hours and minutes from till today to future dates, 
    that how many days you have to complete your course or project
    input for the goal - learn python:22.4.2023
    output - Time remaining for your goal: python is 374 hours
"""
def countdown_app():
    user_input = input("Enter your goal with the deadline separated by colon\n") #hello world
    user_list =user_input.split(":") #learn python:22.4.2023 = ['learn python','22.4.2023']
    # print(user_list)

    goal = user_list[0]
    deadline = user_list[1] #deadline date will be the future date

    deadline_date = datetime.strptime(deadline, '%d.%m.%Y')

    today_date = datetime.today() 

    time_till = deadline_date - today_date

    hours_till = int(time_till.total_seconds() / 60 / 60)

    # print(f"Time remaining for your goal: {goal} is {time_till} days")
    # print(f"Time remaining for your goal: {goal} is {time_till.days} days")
    # print(f"Time remaining for your goal: {goal} is {time_till.total_seconds() / 60 / 60} hours")
    return f"Time remaining for your goal: {goal} is {hours_till} hours"
    
remain_time = countdown_app()    
print(remain_time)

