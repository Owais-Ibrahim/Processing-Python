frankpkgs = 0
bunpkgs = 0
hotdogs =0

def make_hotdogs(frankpkgs, bunpkgs):
    global hotdogs
    frank = frankpkgs*12
    buns = bunpkgs*8
    if(frank>buns):
        hotdogs = buns
    else:
        hotdogs = frank
       
def setup():
    global frankpkgs
    global bunpkgs
    global hotdogs
 
    print("Press the f/g key to increase/decrease the number of frank packages purchased")
    print("Press the b/n key to increase/decrease the number of buns packages purchased")
    size(500,500)
    text("pacakage(s) of franks" , 50,50)
    text("pacakage(s) of bun(s)" , 250,50)
    text("hotdogs made" , 150,200)
   
   
def draw():
    clear()
    text("pacakage(s) of franks" , 50,50)
    text("pacakage(s) of bun(s)" , 250,50)
    text("hotdogs made" , 150,200)
    text(frankpkgs , 75,100)
    text(bunpkgs , 275,100)
    text(hotdogs , 175,250)

def keyPressed():
     global frankpkgs
     global bunpkgs
     global hotdogs
     if key =="f" :
        frankpkgs += 1
        make_hotdogs(frankpkgs, bunpkgs)
     elif key =="g":
        if(frankpkgs==0):
            print("Sorry,none available")
        else:
            frankpkgs -= 1
            make_hotdogs(frankpkgs, bunpkgs)
     elif key =="b":
        bunpkgs += 1
        make_hotdogs(frankpkgs, bunpkgs)
     elif key =="n":
        if(bunpkgs==0):
            print("Sorry,none available")
        else:
            bunpkgs -= 1
            make_hotdogs(frankpkgs, bunpkgs)
