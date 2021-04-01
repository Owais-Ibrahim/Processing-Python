pokedex = {}
name=""

def setup():
    #Black background
    background(0)
    #White foreground
    size( 600, 400)
    fill (255)
    text("Type in a pokemon's name",0,50)
   
       
    #Filling in data
    allData = loadStrings("pokedex.txt")
    for line in allData:
        (key, val) = line.split(",")
        pokedex[key] = val
       

       
def draw():
    #needed to access global variable
    global name
   
    if (keyPressed):
        #to clear screen in a way, and write the update value
        #of name variable
        background (0)
        text("Type in a pokemon's name",0,50)
        name+=key
        text(name, 0,100)
        #Delay to prevent multiple assignments on a signgle keypress
        delay(200 )
        text("Click to report pokemon type", 0,150)

    if (mousePressed):
        background (0)
        if(pokedex.has_key(name)):
            fill(255,255,255)
            fill (255)
            text("Type in a pokemon's name",0,50)
            text(name, 0,100)
            text("Click to report pokemon type", 0,150)
            text(name+"'s type is: "+pokedex.get(name), 0, 300)
        else:
            fill (255)
            text("Type in a pokemon's name",0,50)
            text(name, 0,100)
            text("Click to report pokemon type", 0,150)
            text("Pokemon not Found", 0, 300)
               
        #clearing name back to blank
        name = ""
        delay(500)
