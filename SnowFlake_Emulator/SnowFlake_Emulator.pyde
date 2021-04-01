snowflakes = []
SNOWFLAKE_COUNT= 100
MIN_SIZE = 2
MAX_SIZE = 6
SPEED = 2
kp = True

def setup():
    # size set to 400, 400
    size (400, 400)
    # generating random snowflakes
    for i in range (SNOWFLAKE_COUNT):
        x = random(0, width - 1)
        y = random(0, height - 1)
        size = random(MIN_SIZE, MAX_SIZE)
        snowflakes.append({"x" : x, "y" : y,  'size' : size})
         
def draw ():
    global kp
    # clears screen and sets background color to black
    clear()
    background (0)
    # drawing and updating snow flakes
    # if(kp):
    for snowflake in snowflakes:
        circle (snowflake["x"], snowflake['y'], snowflake['size'])
        snowflake["y"] += SPEED
       
        # if snowflake has reached the bottom
        if snowflake ["y"] >= height:
            snowflake["x"] = random(0, width - 1)
            snowflake ["size"] = random(MIN_SIZE, MAX_SIZE)
            snowflake ["y"]=0
               
    delay (50)
   
def keyPressed():
    global kp
    if(kp):
        noLoop()
        kp=False
    elif(kp==False):
        loop()
        kp = True 
