def days_to_units(num_of_days, conversion_unit):  
    if conversion_unit == "hours":
       return f"{num_of_days} days are {num_of_days*24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days*24*60} minutes"
    else:
        return "unsupported unit"
  

def validate_and_execute():
    try:
        user_input_num = int(days_and_unit_dict["days"])
        
        if user_input_num > 0:
            calculate_value = days_to_units(user_input_num, days_and_unit_dict["unit"])
            print(calculate_value)
                
        elif user_input_num == 0:
            print("you entered 0. please enter positive number" )   
        
        else:
            print("Invalid number entered no conversion for you ")    
                            
    except ValueError:
        print("your input is not a valid")  

user_input = "" 
while user_input != "exit":     
    user_input = input("Enter a number of days and conversion unit\n")
    days_and_unit =  user_input.split(":")  
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    validate_and_execute()
    

# input = 40:hours or 30:minutes
# output = 40 days are 960 hours, 30 days are 43200 minutes

    
    