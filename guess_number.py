import random
min_num = int(input("Minimum number: "))
max_num = int(input("Maximum number: "))
num_of_guesses = 4
tried = 1
out_of_guess = False

a = random.randint(min_num,max_num)
guess_num = int(input("Enter your guess: "))

## TRIED ADDING OUT OF GUESSES - THIS STOPS THE PROGRAMME WHEN USER IS OUT OF GUESSES

## ATTEMPT 1 - DOES NOT WORK WHEN Ln19 IS ACTIVE
# while guess_num != a :
#     if tried < num_of_guesses:
#         guess_num = input("Enter your guess: ")
#         tried += 1
#     else:
#         #out_of_guess = True
#         print("You've used your chances")
#         break
# else: print("Bingo!")

## ATTEMPT 2 - DOES NOT WORK LIKE THE 1st ATTEMPT
# while guess_num != a:
#     if tried < num_of_guesses:
#         guess_num = input("Enter your guess: ")
#         tried += 1
#     else:
#         tried == num_of_guesses
#         print("You've used your chances")
#         break
# else: print("Bingo!")

## ATTEMPT 3 - WORKS CORRECTLY
while guess_num != a:
    if tried<num_of_guesses and not (out_of_guess):
        guess_num = int(input("Enter your guess:"))
        tried += 1
    else:
        out_of_guess = True
        print(f"You've exhausted your guess chances")
        tried +=1
        break
else: 
    print(f"Bingo! You had it on your {tried}th guess")
## YOU CAN MAKE CHANGES TO IT TO SUIT YOU
## USE BREAK TO STOP THE ITERATION OR ELSE THERE WILL BE A LOOP OF Ln42
## WORKS WITH A FUNCTION