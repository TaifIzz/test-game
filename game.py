game = input("do you want to play guess game ? \n")
if game == "yes" :
    print("ok lets play.")
    print("you have onle 3 chans to guess the real number from (1-9) \n")
else :
    print("thank you by by") 
    exit()
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number :
        print("you won")
        break
else :
    print("sorry , you failed !")
