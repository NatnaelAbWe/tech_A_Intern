import random
import time

def num_guessing():
    c_guess = random.randint(1,10)
    count = 1
    while True:
        try:
            u_guess = int(input("enter your guess:\n"))
            if c_guess == u_guess:
                print("you have got the right answer the correct answwer is ",u_guess)
                print("number of trial: ",count)
                break
            elif c_guess > u_guess:
                print("your guess is lower than the value")
                count += 1
            else:
                print("your guess is higher than the expected value")
                count += 1
        except:
            print("INVALID INPUT")

def main():
    name = input("please input your name to continue\n")
    primary_msg = f'''hello {name} wellcome to the number gussing game this is developed by me nati 🥰 \n try it \n you have to guess the number between 1 and 10 if that is all the rull bro/sis \n'''
    for char in primary_msg:
        print(char, end = "", flush = True)
        time.sleep(0.05)
    print("=" * 60)
    num_guessing()

if __name__ == "__main__":
    main()


