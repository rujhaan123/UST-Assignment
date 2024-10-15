def validate_passwords(input_passwords):
    # Split the input string into a list of passwords
    passwords = input_passwords.split(',')
    
    # List to hold valid passwords
    valid_passwords = []
    
    # Check each password
    for password in passwords:
        # Check if the length is between 6 and 12 characters
        if len(password) < 6 or len(password) > 12:
            continue
        
        # Flags to track if password meets the criteria
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        
        # Check each character in the password
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in "$#@":
                has_special = True
        
        # If all criteria are met, add the password to the valid list
        if has_lower and has_upper and has_digit and has_special:
            valid_passwords.append(password)
    
    # Return valid passwords as a comma-separated string
    return ",".join(valid_passwords)
