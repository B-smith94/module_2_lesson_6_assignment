first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

full_name = first_name + last_name

if len(first_name) < 3 or len(last_name) < 3:
    print("ERROR: Your first and last names must be more than 2 characters each.")    
else: 
    print(f"Your name has {len(full_name)} characters.")
       
    