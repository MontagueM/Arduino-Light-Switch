from pyfirmata import Arduino
board = Arduino("COM6")  # Change to correct COM port
pin = board.get_pin('d:9:s') # Change to correct digital pin on Arduino
pin.write(90)
i = 0
while i == 0:
    angle = int(input("What angle, degrees? "))
    pin.write(angle)
