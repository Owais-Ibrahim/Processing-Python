'''This program creates 20 random circles and then process the 
coordinates. Id's, coordinates, and size are stored within a dictionary
to allow for mouse pressed to check. The check function allows us to see if the 
mouse clicked is on a circle and turning it green. When a circle is clicked it 
is dependent on user inputs.'''

# this fuction allows us to see if the mouse press is equivalent to a circle
def check (circles,x,y):
    return(x-circles['x']) ** 2 + (y-circles['y']) ** 2< (circles['size']/2) ** 2

# A dictionary to hold circle information and selected to keep track if a 
# circle is selected
circles = []
selected = 0

# Createss a window of 600*600 and then randomizes cirlce information
# and stores in dictionary
def setup():
    size(600,600)
    for i in range(0,20):
        x = int(random(1,width))
        y = int(random(1, height))
        radius = int(random(20,50))
        circles.append({'id': i +1, 'size':radius, 'x':x, 'y':y})

# Then circles are drawn on a black background
def draw():
    background(0,0,0)
    for c in circles:
        if(c['id']==selected):
            fill(0,75,0)
        else:
            fill(150)
        circle(c['x'],c['y'],c['size'])
 
# Checking if the circle is in selected state    
def selection():
    for c in circles:
        if(c['id']==selected):
            return c
    return None

def keyPressed():
    # when key is pressed wwe wanted to see if no circle is selected return but 
    # if selected then we want to change circle information
    if(selected==0):
        return 
    
    selectionc = selection() 
    # if + or - is pressed then alter size accordingly
    if(key == '+'):
        selectionc['size'] = selectionc['size'] + 1
    if(key == '-'):
        if(selectionc['size']>=20):
            selectionc['size'] = selectionc['size'] - 1
    # if s or w is pressed move circle on y-axis accordingly    
    if(key == 's'):
        selectionc['y'] = selectionc['y'] + 1    
    if(key == 'w'):
        selectionc['y'] = selectionc['y'] - 1
    # if a or d is pressed move circle horizontally
    if(key == 'a'):
        selectionc['x'] = selectionc['x'] - 1
    if(key == 'd'):
        selectionc['x'] = selectionc['x'] + 1

# when mouse is clicked take mouse x and y to check if its a circle if it is then
# changing the state of that circle to selected
def mouseClicked():
    global selected
    for c in circles:
        if(check(c, mouseX, mouseY)):
            selected = c['id']
            return
    selected =0 
        
