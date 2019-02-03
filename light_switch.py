from pyfirmata import Arduino
board = Arduino("COM6")  # Change to correct COM port
pin9 = board.get_pin('d:9:s')
pin9.write(90)
i = 0
while i == 0:
    angle = int(input("What angle, degrees? "))
    pin9.write(angle)
