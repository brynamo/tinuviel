from datetime import datetime
import time

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

if __name__ == "__main__":
    while True:
        print_time()
#        time.sleep(1)
