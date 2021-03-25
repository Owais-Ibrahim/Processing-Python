x = []
y = []
s = []

def setup():
    size(300, 300)
    background(0)
    fill(255)
    
def draw():
    pass

def mousePressed():
    global x, y, s
    sz = random(10, 30)
    x.append(mouseX)
    y.append(mouseY)
    s.append((int(sz)))
    ellipse(mouseX, mouseY, sz, sz)
    
def keyPressed():
    global x, y, s
    file = open('dots.txt', 'w')
    for i in range(len(x)):
        file.write("{} {} {}\n" .format(x[i], y[i], s[i]))
    file.close()
    exit()
    
