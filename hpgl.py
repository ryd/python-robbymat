
import string, re, Robbymat

class HPGL:
    def __init__(self):
        self.pin_down = False
        self.x = 0
        self.y = 0
        self.deep = 10
        self.robby = Robbymat.Robbymat()

    def parse(self, token):
        cmd = token[0:2]
        if cmd == "IN":
            pass
        elif cmd == "PD":
            self.move_down()
            pos = re.split(",", token[3:])
            if len(pos) == 2:
                self.move(int(pos[0]), int(pos[1]))
            else:
                print "error parsing", token
        elif cmd == "PU":
            self.move_up()
        elif cmd == "PA":
            pass
        elif cmd == "IW":
            pass
        elif token == "\x0d\x0a" or token == "\x03\x0d\x0a" or token == '':
            pass
        else:
            print "Unknown command -", len(token)

    def move_up(self):
        if self.pin_down:
            self.pin_down = False
            self.robby.move_z(self.deep * -1)

    def move_down(self):
        if not self.pin_down:
            self.pin_down = True
            self.robby.move_z(self.deep)

    def move(self, pos_x, pos_y):
        self.robby.move_xy(pos_x - self.x, pos_y - self.y)
        self.x = pos_x
        self.y = pos_y


if __name__ == '__main__':
    print "Let's go"
    f = open('hpgl/attraktor-logo-original.prn', 'r')
    hpgl = HPGL()
    #hpgl.robby.dry_run = True
    for line in f:
        token = re.split("\;", line)
        print "len", len(line), " items", len(token)
        for t in token:
            hpgl.parse(t)
    f.close()

