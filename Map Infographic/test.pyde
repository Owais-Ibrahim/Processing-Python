#Setting size
size(500,425)
#loading image and resizeing to fit background
img_map = loadImage('Map.jpg')
img_map.resize(500,425)
image(img_map,0,0,width,height)

#opening data file with read rights
file = open('popdata.txt', 'r')
#creating a couter to help substring the data and process it 
#initilaizing an array to store useful data for each line
c = 0
x=0
data = []

while True:
    #reading line by line
    line = file.readline()
    #reading each character in line
    for element in range(c, len(line)):
        a = line[element]
        #if char is equal to comma
        if(a == ","):
            #we are appending coutnry name
            if(c==0):
                data.append(line[c:element])
            #we are appeding the data values
            else:
                data.append(line[c+1:element])
            c=element
            x=x+1
            #appending the last data value
            if(x==4):
                c=element
                data.append(line[c+1:len(line)-1])
    #if data is not empty
    if data:
        #turn string into floats
        xcord = (float(data[1]))
        ycord = (float(data[2]))
        inital = (float(data[3]))
        final = (float(data[4]))
        #calculate percent change
        change = ((final-inital))
        percent = change/(inital)
        #if the perecnet is increase or decrease by a certain magnitude perform color
        #and size instructions
        if (percent>=0.30):
            size = 10
            red = 0
            green =  100
            blue = 0
        elif((percent>0.0) & (percent<0.30)):
            size=5
            red = 0
            green =  100
            blue = 0
        elif (percent<=-0.30):
            size = 10
            red = 100
            green =  0
            blue = 0
        elif((percent<0.0) & (percent>-0.30)):
            size=5
            red = 100
            green =  0
            blue = 0
        #filling and creating circle based on data
        fill(red,green,blue)
        circle(xcord,ycord, size)
        #writting text and filling it blue
        fill(0,0,0)
        text(data[0], xcord-25, ycord)
        #clearing data array and counters for next line to read
        data= []
        c=0
        x=0
        #when file is done and next line empty end the loop and file
    if not line:
        break
