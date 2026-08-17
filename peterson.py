import threading
import time

counter = 100
def subtract_credits():
    global counter
    value = counter
    time.sleep(0.01)
    counter = value - 40

def add_credits():
    global counter
    value = counter
    time.sleep(0.01)
    counter = value + 25

def run_without_synchronization():
    global counter
    counter = 100
    thread1 = threading.Thread(target=subtract_credits)
    thread2 = threading.Thread(target=add_credits)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return counter

print("WITHOUT SYNCHRONIZATION")
for i in range(5):
    final_value = run_without_synchronization()
    print("Run", i + 1, "Final value:", final_value)


flag = [False, False]
turn = 0
counter = 100
def enter_critical_section(process):
    global turn
    other = 1 - process
    flag[process] = True
    turn = other
    while flag[other] and turn == other:
        pass

def leave_critical_section(process):
    flag[process] = False

def subtract_with_peterson():
    global counter
    enter_critical_section(0)
    value = counter
    time.sleep(0.01)
    counter = value - 40
    leave_critical_section(0)

def add_with_peterson():
    global counter
    enter_critical_section(1)
    value = counter
    time.sleep(0.01)
    counter = value + 25
    leave_critical_section(1)

def run_with_peterson():
    global counter
    global flag
    global turn
    counter = 100
    flag = [False, False]
    turn = 0
    thread1 = threading.Thread(target=subtract_with_peterson)
    thread2 = threading.Thread(target=add_with_peterson)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return counter

print("\nWITH PETERSON'S ALGORITHM")
for i in range(5):
    final_value = run_with_peterson()
    print("Run", i + 1, "Final value:", final_value)

