from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry

def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)


def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    arms = Line(Point(150, 190), Point(250, 190))
    arms.draw(win)
    left_leg = Line(Point(200, 240), Point(150, 290))
    left_leg.draw(win) 
    right_leg = Line(Point(200, 240), Point(250, 290))
    right_leg.draw(win)
    win.get_mouse()

    
def draw_circle():
    radius = int(input("Enter radius: "))
    win = Window()
    head = Circle(Point(200, 120), radius)
    
    head.draw(win)
    win.get_mouse()




def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()
    

def draw_circle():
    win = Window()
    radius = int(input("Enter radius: "))
    head = Circle(Point(200, 120), radius)
    head.outline_colour = "blue"
    head.draw(win)
    win.get_mouse()

def draw_archery_target():
    # Create a window
    win = Window("Archery Target", 400, 400)
    
    # Radius for the yellow circle
    yellow_radius = 40  
    
    # Create the Point for the center of the target
    center = Point(200, 200)  # Window is 400x400, so (200, 200) is the center
    
    # Create and draw the yellow circle (smallest circle)
    yellow_circle = Circle(center, yellow_radius)
    yellow_circle.outline_colour = "yellow"
    yellow_circle.fill_colour = "yellow"
    yellow_circle.draw(win)
    
    # Create and draw the red circle (radius is twice the yellow circle's radius)
    red_radius = yellow_radius * 2
    red_circle = Circle(center, red_radius)
    red_circle.outline_colour = "red"
    red_circle.fill_colour = "red"
    red_circle.draw(win)
    
    # Create and draw the blue circle (radius is three times the yellow circle's radius)
    blue_radius = yellow_radius * 3
    blue_circle = Circle(center, blue_radius)
    blue_circle.outline_colour = "blue"
    blue_circle.fill_colour = "blue"
    blue_circle.draw(win)
    
    # Wait for a mouse click to close the window
    win.get_mouse()

# Call the function to draw the archery target





def draw_rectangle():
    # Create a window of size 400x400
    win = Window("Centered Rectangle", 400, 400)
    
    # Ask the user for the height and width of the rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    
    # Check that the width and height are valid (less than the window size)
    if width >= 400 or height >= 400:
        print("Width and height must be less than 400.")
        return
    
    # Calculate the top-left corner coordinates
    top_left_x = (400 - width) // 2
    top_left_y = (400 - height) // 2
    
    # Create the top-left and bottom-right points of the rectangle
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(top_left_x + width, top_left_y + height)
    
    # Create a Rectangle object and set its attributes
    rectangle = Rectangle(top_left, bottom_right)
    rectangle.outline_colour = "black"
    rectangle.fill_colour = "lightblue"  # You can change this color as you like
    
    # Draw the rectangle on the window
    rectangle.draw(win)
    
    # Wait for a mouse click to close the window
    win.get_mouse()

# Call the function to draw the rectangle
draw_rectangle()