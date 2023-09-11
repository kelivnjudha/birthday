import time
import random
from datetime import datetime, timedelta
import webbrowser
import os
import sys

os.system("start /max cmd.exe")

# Maximize the terminal window on macOS
os.system("osascript -e 'tell application \"Terminal\" to set zoomed of front window to true'")


wishes={
    1: """Happy 20th Birthday, Fring! 🎉
Though we've only met once, the impression you left was so memorable. 
May this special day be filled with joy, new adventures, and wonderful surprises. 
Here's to the next chapter in your life – may it be even more amazing than the last. 
Enjoy your day to the fullest!""",
    2: """Happy 20th Birthday, Fring! 🥳 
It's incredible how our paths crossed, and I'm grateful for that one meeting. 
May your day be as extraordinary as you are, and may the coming year bring you everything your heart desires. 
Have a blast!""",
    3: """Warmest birthday wishes to you, Fring, on your 20th! 🎈 
Though we've only met once, your positivity and enthusiasm are truly infectious. 
May this year be the start of an amazing journey filled with new experiences and beautiful memories. 
Enjoy your special day!"""
}


random_wishes = random.randint(1,3)


months = [
    "January", "February", "March", "April", "May",
    "June", "July", "August", "September", "October","November", "December"
]


def loop():
    
    loop_duration = 10
    end_time = datetime.now() + timedelta(seconds=loop_duration)
    while datetime.now() < end_time:
        random_day = random.randint(1, 30)
        random_number = random.randint(0, 11)
        years = random.randint(2003, 2023)
        random_month = months[random_number]
        print(f"\t\t\t>{random_day}\t\t<---->\t\t{random_month}     \t<---->\t\t [{years}]<")
        
    print("\n__________________________________________________________________________________________________________________________")
    print(f"\n\n\t\t\t>11\t\t<---->\t\t{months[8]}     \t<---->\t\t [2023]<\n\n")
    loading_animation(total_iterations)
    birthday()
        
        
def birthday():
    print(r"""


 __  __  ______  ____    ____    __    __      ____    ______   ____    ______  __  __  ____    ______   __    __ 
/\ \/\ \/\  _  \/\  _`\ /\  _`\ /\ \  /\ \    /\  _`\ /\__  _\ /\  _`\ /\__  _\/\ \/\ \/\  _`\ /\  _  \ /\ \  /\ \
\ \ \_\ \ \ \L\ \ \ \L\ \ \ \L\ \ `\`\\/'/    \ \ \L\ \/_/\ \/ \ \ \L\ \/_/\ \/\ \ \_\ \ \ \/\ \ \ \L\ \\ `\`\\/'/
 \ \  _  \ \  __ \ \ ,__/\ \ ,__/`\ `\ /'      \ \  _ <' \ \ \  \ \ ,  /  \ \ \ \ \  _  \ \ \ \ \ \  __ \`\ `\ /' 
  \ \ \ \ \ \ \/\ \ \ \/  \ \ \/   `\ \ \       \ \ \L\ \ \_\ \__\ \ \\ \  \ \ \ \ \ \ \ \ \ \_\ \ \ \/\ \ `\ \ \ 
   \ \_\ \_\ \_\ \_\ \_\   \ \_\     \ \_\       \ \____/ /\_____\\ \_\ \_\ \ \_\ \ \_\ \_\ \____/\ \_\ \_\  \ \_\
    \/_/\/_/\/_/\/_/\/_/    \/_/      \/_/        \/___/  \/_____/ \/_/\/ /  \/_/  \/_/\/_/\/___/  \/_/\/_/   \/_/
                                                                                                                  
                                                                                                                  
                                    ____    ____    ______   __  __  ____                                         
                                   /\  _`\ /\  _`\ /\__  _\ /\ \/\ \/\  _`\                                       
                                   \ \ \L\_\ \ \L\ \/_/\ \/ \ \ `\\ \ \ \L\_\                                     
                                    \ \  _\/\ \ ,  /  \ \ \  \ \ , ` \ \ \L_L                                     
                                     \ \ \/  \ \ \\ \  \_\ \__\ \ \`\ \ \ \/, \                                   
                                      \ \_\   \ \_\ \_\/\_____\\ \_\ \_\ \____/                                   
                                       \/_/    \/_/\/ /\/_____/ \/_/\/_/\/___/                                    
                                    
                                    
                                            BIRTHDAY WISH BY KELVIN JUDHA
                                                                                                                      
########################################################################################################################                                                                                                                  
""")
    
    try:
        wish = wishes[random_wishes]
        print(wish)
    except:
        print(wishes[3])
        
    birthdaysong()
    

def loading_animation(total_iterations):
    for i in range(total_iterations + 1):
        progress = i / total_iterations
        percentage = int(progress * 100)
        loading_bar = "#" * int(120 * progress)
        sys.stdout.write(f"\r[{loading_bar:<120}] {percentage}%")
        sys.stdout.flush()
        time.sleep(0.1)  # Adjust the sleep duration as needed

# Number of iterations for your loading animation
total_iterations = 50

def start_loading(total_iterations):
    for i in range(total_iterations + 1):
        progress = i / total_iterations
        percentage = int(progress * 100)
        loading_bar = "I" * int(120 * progress)
        sys.stdout.write(f"\r[{loading_bar:<120}] {percentage}%")
        sys.stdout.flush()
        time.sleep(0.1)
        
def verification():
    name = input("Enter your Name > ")
    password = int(input("Enter the password (Hint: add all your date of birth numbers) > "))
    if name.lower() == "fring" and password == 2023:
        start()
    else:
        print("TRY AGAIN..")
        verification()
        
def birthdaysong():
    print("\n\n########################################################################################################################  ")
    usr = input('\n\n\nEnter "yes" to continue for birthday song/ "no" to close the program > ').lower()
    if usr.startswith("y"):
        webbrowser.open_new("https://youtu.be/vhVBWw6rId0?si=M5R5itHBN69DUx8A")
    elif usr.startswith("n"):
        print("PROGRAM TERMINATED")
        print("\n\nHAPPY BIRTHDAY FRING")
    else:
        print("Unknown Input")
        birthdaysong()
  
def start():
    if __name__ =="__main__":
        print("PROGRAM IS STARTING....")
        start_loading(total_iterations)
        print("\n")
        loop()
        
verification()