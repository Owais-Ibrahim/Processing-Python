def setup():
    size(600,300)
    global x
    global y
    global z
    global counter
    global fries
    global remainder
    x=0
    y=5
    z=1
    counter=0
    fries=0
   
   
def draw():
    global fries
    global counter
    global y
    global x
    global z
    global remainder
    global itr
    global m
    y=5
    x=0
    m=0
    remainder = counter % 20
    itr = counter / 20
    clear()
    background(255,255,255)
    if counter<20:
        for i in range (counter):
            fill(255,200,0)
            rect(x + (30*i),y,4,25)
            fill(255,200,0)
            rect(x+5+(30*i),y-3,4,35)
            fill(255,200,0)
            rect(x+10+(30*i),y+3,4,35)
            fill(255,200,0)
            rect(x+15+(30*i),y-3,4,35)
            fill(255,200,0)
            rect(x+19+(30*i),y+5,3,35)
            fill(255,0,0)
            rect(x-2+(30*i),y+13,25,30)
            fill(255,200,0)
            rect(x+5+(30*i),y+20,2,15)
            fill(255,200,0)
            rect(x+6+(30*i),y+20,10,2)
            fill(255,200,0)
            rect(x+5+(30*i),y+27,8,2)
    else:
        remainder = counter%20
        itr = counter/20
        for j in range(itr):
            for i in range (20):
                fill(255,200,0)
                rect(x + (30*i),y,4,25)
                fill(255,200,0)
                rect(x+5+(30*i),y-3,4,35)
                fill(255,200,0)
                rect(x+10+(30*i),y+3,4,35)
                fill(255,200,0)
                rect(x+15+(30*i),y-3,4,35)
                fill(255,200,0)
                rect(x+19+(30*i),y+5,3,35)
                fill(255,0,0)
                rect(x-2+(30*i),y+13,25,30)
                fill(255,200,0)
                rect(x+5+(30*i),y+20,2,15)
                fill(255,200,0)
                rect(x+6+(30*i),y+20,10,2)
                fill(255,200,0)
                rect(x+5+(30*i),y+27,8,2)
            m+=1
            x = 0
            y = 55*m
        for i in range (remainder):
            fill(255,200,0)
            rect(x + (30*i),y,4,25)
            fill(255,200,0)
            rect(x+5+(30*i),y-3,4,35)
            fill(255,200,0)
            rect(x+10+(30*i),y+3,4,35)
            fill(255,200,0)
            rect(x+15+(30*i),y-3,4,35)
            fill(255,200,0)
            rect(x+19+(30*i),y+5,3,35)
            fill(255,0,0)
            rect(x-2+(30*i),y+13,25,30)
            fill(255,200,0)
            rect(x+5+(30*i),y+20,2,15)
            fill(255,200,0)
            rect(x+6+(30*i),y+20,10,2)
            fill(255,200,0)
            rect(x+5+(30*i),y+27,8,2)
       

    text("Your order: " + str(fries) , 20,250)

def keyPressed():
     global x
     global y
     global z
     global counter
     global fries
     
     if key =="f" :
        counter += 1
        fries +=1
     elif key =="n":
        if(counter==0):
            print("Sorry,none available")
        else:
            counter -= 1
            fries-=1
