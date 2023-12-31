# Write a program to make a chess board

import turtle
sc=turtle.Screen()
cb=turtle.turtle()

# Method to draw sqaure 

def draw():
    for i in range(4):
        cb.forward(30)
        cb.left(90)
    cb.forward(30)
    
# Driver code

if __name__ == "__main__":
    
    # set screen
    
    sc.setup(400,600)
    
    # set turtle object speed
    
    cb.speed(100)
    
    # loops for board
    
    for i in range(8):
        
        # not ready to draw
        
        cb.up()
        
        # set position for every row
        
        cb.setpos(-100,30*i)
        
        # ready to draw
        
        cb.down()
        
        # row
        
        for j in range(8):
            
            # condition for alternative colors
            
            if (i+j)%2==0:
                col='black'
            else:
                col='white'
            
            # fill with given color
            
            cb.fillcolor(col)
            
            # start filling with color
            
            cb.begin_fill()
            
            # call method
            
            draw()
            
            # stop filling
            
            cb.end_fill()
            
            # hide the turtle
            
    cb.hideturtle()
    turtle.done()
