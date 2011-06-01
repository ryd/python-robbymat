
import serial, string

class Robbymat:
    def __init__(self, serial_instance):
        if serial_instance == None:
            self.serial = serial.Serial('/dev/ttyUSB0', 19200, 8, 'N', 1, timeout=1)
        else:
            self.serial = serial_instance
        self.dry_run = False
        self.print_result = False
        self.distance_x = 200
        self.distance_y = 200
        self.distance_z = 10

    def move_up(self):
        self.move_z(self.distance_z * -1)

    def move_down(self):
        self.move_z(self.distance_z)

    def move_left(self):
        self.move_x(self.distance_x * -1)

    def move_right(self):
        self.move_x(self.distance_x)

    def move_forward(self):
        self.move_y(self.distance_y * -1)

    def move_backward(self):
        self.move_y(self.distance_y)

    def execute(self, cmd, lines=1):
        if self.dry_run:
            print cmd[:-1]
        else:
            self.serial.write(cmd)
            for i in range(lines):
                r = self.serial.readline()
                if self.print_result:
                    print r[:-1]

    def move_x(self, distance):
        self.execute("X MOVE {0}\n".format(distance))

    def move_y(self, distance):
        self.execute("Y MOVE {0}\n".format(distance))

    def move_z(self, distance):
        self.execute("Z MOVE {0}\n".format(distance))

    def home(self):
        self.execute("XYZ HOME\n", 3)

    def move_xy(self, distance_x, distance_y):
        self.execute("XY MOVE {0},{1}\n".format(distance_x, distance_y), 2)
