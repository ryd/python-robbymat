
import string, re, Robbymat

class HPGL:
    def __init__(self):
        self.pin_down = True
        self.x = 0
        self.y = 0
        self.deep = 50
        self.robby = Robbymat.Robbymat()
        self.robby.ramp(5)
        self.robby.minspeed(300)
        self.robby.maxspeed(1000)
        self.faktor = 1

    def parse(self, token):
        cmd = token[0:2]
        if cmd == "IN":
            pass
        elif cmd == "PD":
            self.move_down()
            pos = re.split(",", token[2:])
            if len(pos) == 2:
                self.move(int(float(pos[0]) / self.faktor), int(float(pos[1]) / self.faktor))
            else:
                print "error parsing", token
        elif cmd == "PU":
            self.move_up()
            pos = re.split(",", token[2:])
            if len(pos) == 2:
                self.move(int(float(pos[0]) / self.faktor), int(float(pos[1]) / self.faktor))
            else:
                print "error parsing", token
        elif cmd == "PA":
            print "Using absolut number"
        elif cmd == "PR":
            print "Relative numbers mode not supported"
            sys.exit()
        elif cmd == "IW":
            pass
        elif token == "\x0d\x0a" or token == "\x03\x0d\x0a" or token == '':
            pass
        else:
            print "Unknown command -", len(token)

    def move_up(self):
        if self.pin_down:
            self.pin_down = False
            print "Pin UP"
            self.robby.move_z(-100)

    def move_down(self):
        if self.pin_down == False:
            self.pin_down = True
            print "Pin DOWN"
            self.robby.move_z(100)

    def move(self, pos_x, pos_y):
        self.robby.move_xy(pos_x - self.x, pos_y - self.y)
        self.x = pos_x
        self.y = pos_y


if __name__ == '__main__':
    print "Let's go"
    f = open('hpgl/duke_Nukem__by_DeadCamper.prn', 'r')
    hpgl = HPGL()
    #hpgl.robby.dry_run = True
    for line in f:
        token = re.split("\;", line)
        print "len", len(line), " items", len(token)
        for t in token:
            hpgl.parse(t)
    f.close()

