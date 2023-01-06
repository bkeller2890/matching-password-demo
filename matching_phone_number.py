#Matching Phone Number
#Benjamin A Keller 
#1/2/2022

phone_number = 2321242532 #This is a Made Up Phone Number for the purpose of this program 

insert_number = int(input("Insert Number in XXXXXXXXXX format: "))



if insert_number == phone_number: 
        number_match = "Correct"
else: 
    #Loop for the number of tries the user has before he/she gets locked out of account
    for tries in range (5): 
        
        tries += 1 
        next_try = int(input("Wrong Number, Please Try Again (XXXXXXXXXX fomat): "))

        insert_number = next_try

        if insert_number == phone_number: 
            number_match = "Correct"
            break 

        if tries == 5: 
            number_match = "Too Many Failed Attempts - You Have Been Locked Out "
            break
  

print(number_match)
