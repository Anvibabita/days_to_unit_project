calculate_to_unit = 24
unit_name = "hours"


def calculate_days(num_of_days):
       return f"{num_of_days} days are {num_of_days*calculate_to_unit} {unit_name}"
  

def validate_and_execute():
    try:
        user_input_num = int(num_of_days_element)
        
        # we want to do conversion only for positive integers
        if user_input_num > 0:
            calculate_value = calculate_days(user_input_num)
            print(calculate_value)
                
        elif user_input_num == 0:
            print("you entered 0. please enter positive number" )   
        
        else:
            print("Invalid number entered no conversion for you ")    
                            
    except ValueError:
        print("your input is not a valid")  

user_input = "" 
while user_input != "exit":     
    # print(type(user_input.split(",")))
    # print(type(set(user_input.split(","))))
    user_input = input("Enter a number of days as a comma saperated list\n")
    # print(set(user_input.split(",")))    
    for num_of_days_element in set(user_input.split(",")):    
        validate_and_execute()
        
#input = 56,32,21    
#output =
# 21 days are 504 hours
# 56 days are 1344 hours
# 32 days are 768 hours