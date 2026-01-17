import random 

random_number=random.randint(1,10)
print("Let's start the guess game!!\nYou'll only have 3 tries so be carefull!")


for attempt in range(3):
    try:
           number=int(input("Enter the number between 1-10:-\n"))
    except ValueError:
        print("Invalid input Error 404")
        continue 
    if number>10 or number<1:
        print("Invalid input.Error 404!!")
        break 
    if attempt==2:
        if number!=random_number:
            print(f"Game Over.\nThe secret number was {random_number}")  
            break    
    if number == random_number:
        print("Congratulations!!!\nFinally someone got this correct!.")
        break
    else:
     print("Oops it's wrong\nTry Again")
    
     
