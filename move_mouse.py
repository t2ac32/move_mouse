import pyautogui
import time
from pick import pick
from colorama import init
from termcolor import colored

screenWidt, screenHeight = pyautogui.size()
init_mouseX, init_mouseY = pyautogui.position()

selected = 1
options = ['Endless mode', 'Input time limit']
total_options = len(options)

def endless_mode(*args):
    stop_time = 0
    timeup = False
    endless_mode = False
    if args:
        stop_time = args[0]
    else:
        endless_mode = True
        print('Running in Endless Mode...')
    while not(timeup):
        for i in range(200):
            if time.time() > stop_time and not(endless_mode):
                timeup = True
                print("Time complete, ending script")
                break
            pyautogui.moveTo(init_mouseX+i,init_mouseY)
        pyautogui.moveTo(init_mouseX, init_mouseY)

def timer_mode(runtime: int):
    stop_time = time.time() + runtime
    endless_mode(stop_time)

def show_menu():
    global selected
    print("\n" * 2)
    title = 'Please choose and option'
    option, index = pick(options, title)
    
    if index == 0:
        endless_mode()
    else:
        input_time()

def input_time():
    time_units = ['seconds','minutes','hours']
    units_title = 'Please input the time unit script will run, /n press Enter once done.'
    t_unit, index = pick(time_units,units_title)
    
    print(f"Input time lenght in {t_unit}:")
    delay = int(input())
    # var runtime: Script runtime in seconds
    runtime = 0
    
    if index == 1:
        runtime = delay * 60
    elif index==2:
        runtime = delay * 3600
    else:
        runtime = delay
    print(f"runtime {runtime}")
    print(f"Script will run for {delay} {t_unit}")
    try:
        input("Press enter to continue")
        timer_mode(runtime)
    except SyntaxError:
        pass

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    show_menu()

def down():
    global selected
    if selected == total_options:
        return
    selected += 1
    show_menu()

if __name__ == "__main__":
    init()
    print(colored('Welcome','magenta'))
    print(colored('... Initializing Morpeko','white','on_magenta'))
    show_menu()
