from pyfirmata import Arduino
import os
import time
import sys
print("Initialising...")
board = Arduino("COM3")  # Change to correct COM port; seems to be COM6 for PC and COM3 for XPS
pin = board.get_pin('d:9:s') # Change to correct digital pin on Arduino
pin.write(90)  # Setting it to a default value in-case of a misaligned servo
try:
    os.remove(sys.argv[0][:-34] + "listener/a.txt")
except FileNotFoundError:
    print("")

print("Done. Waiting for update")
i = 0
try:
    while True:
        if os.listdir(sys.argv[0][:-34] + "listener") == ['a.txt']:
            print("\nReceived update.")
            f = open("on_off.txt", "r")
            on_off = int(f.readlines()[0])  # I've found for my switch that 45 and 125 are good angles without buzz.
            if on_off == 0:
                pin.write(45)
                on_off = 1
            elif on_off == 1:
                pin.write(125)
                on_off = 0
            q = open("on_off.txt", "w")
            q.write(str(on_off))
            q.close()
            f.close()
            os.remove(sys.argv[0][:-34] + "listener/a.txt")
            print("Completed update.")
            time.sleep(1)
            pin.write(90)
        time.sleep(0.1)
except (KeyboardInterrupt, SystemExit):
    print("\n! Received keyboard interrupt, quitting.\n")
