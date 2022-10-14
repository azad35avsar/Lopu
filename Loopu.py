"""
File: loopu.py
-------------------
A game that aims the user to move the Lopu character on the canvas using the arrow keys and to collect the fruits quickly by using the shortcuts.
"""
import time
from graphics import Canvas
import random

# The size of the canvas, in pixels
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

# The size of the baits
BAIT_SIZE = 30

# The number of pixels for Lopu to move for each key press
BALL_STEP_SIZE = 50

def create_outro(canvas, end,start):
    '''
    This function clears the graphic elements from the screen when the loop is finished and gives the user the elapsed time along with a special sentence.

    Parameters
    ----------
    end : float
        Represents the starting time after character and difficulty level selection.
    start : TYPE
        Represents the time at the end of the cycle, that is, at the end of the game.
    '''

    canvas.delete_all()
    canvas.create_image(0, 0, "mainbg.png")
    canvas.create_image(100, 75, "outrobanner.png")
    canvas.create_image(100, 275, "scortable.png")
    outro_text = canvas.create_text(250, 300, end-start)
    canvas.set_color(outro_text, "white")
    canvas.set_font(outro_text, "Arial", 15)
    canvas.create_image(100, 375, "outronames.png")
    if (end-start) < 10:
        canvas.create_image(100, 175, "scoretext1.png")
    elif 10 < (end - start) < 20:
        canvas.create_image(100, 175, "scoretext2.png")
    else:
        canvas.create_image(100, 175, "scoretext3.png")


def destroy(canvas, lopu, baits, score): 
    '''
    This function is positioned inside the loop and finds and deletes objects that fall within the character's coordinates.

    Parameters
    ----------
    baits : list
        It is a list of randomly generated baits based on difficulty selection.
    score : int
        Represents the number of objects removed.

    Returns
    -------
    score : int
        Represents the number of objects removed.

    '''

    x_1 = canvas.get_left_x(lopu)
    x_2 = canvas.get_left_x(lopu) + 50
    y_1 = canvas.get_top_y(lopu)
    y_2 = canvas.get_top_y(lopu) + 50
    results = canvas.find_overlapping(x_1, y_1, x_2, y_2)
    for object in results:
        if object in baits:
            canvas.delete(object)
            score += 1
    return score


def create_random_bait(canvas, bait_number):
    '''
    This function generates the desired number of random baits according to the difficulty level.

    Parameters
    ----------
    bait_number : int
        Represents the predetermined number of baits according to the difficulty level.

    Returns
    -------
    baits : list
        It is a list of randomly generated baits based on difficulty selection.

    '''

    baits = []
    for i in range((bait_number)//5):

        bait = canvas.create_image(0,0,"baita.png")
        baits.append(bait)
        random_x = random.randint(0, 470)
        random_y = random.randint(0, 470)
        canvas.moveto(bait,random_x,random_y) 
        bait2 = canvas.create_image(0,0,"baitc.png")
        baits.append(bait2)
        random_x2 = random.randint(0, 470)
        random_y2 = random.randint(0, 470)
        canvas.moveto(bait2,random_x2,random_y2)
        bait3 = canvas.create_image(0,0,"baitd.png")
        baits.append(bait3)
        random_x3 = random.randint(0, 470)
        random_y3 = random.randint(0, 470)
        canvas.moveto(bait3,random_x3,random_y3)
        bait4 = canvas.create_image(0,0,"baite.png")
        baits.append(bait4)
        random_x4 = random.randint(0, 470)
        random_y4 = random.randint(0, 470)
        canvas.moveto(bait4,random_x4,random_y4)
        bait5= canvas.create_image(0,0,"baitf.png")
        baits.append(bait5)
        random_x5 = random.randint(0, 470)
        random_y5 = random.randint(0, 470)
        canvas.moveto(bait5,random_x5,random_y5)
    return baits           
        
         
def create_lopus(canvas, character):
    '''
    This function generates the desired game character according to the data from the user.

    Parameters
    ----------
    character : int
        Represents the sequence number of the character selected by the user.

    Returns
    -------
    lopu : graphic
        Represents the character produced in the function.

    '''

    if character == 1:
        lopu = canvas.create_image_with_size(0, 0, 50, 50, "lopu.png")
    elif character == 2:
        lopu = canvas.create_image_with_size(0, 0, 50, 50, "lopu2.png")
    else:
        lopu = canvas.create_image_with_size(0, 0, 50, 50, "lopu3.png")
    
    return lopu


def create_intro(canvas):
    '''
    This function receives data about character and difficulty level selection from the user before the cycle starts.

    Returns
    -------
    bait_number : int
        Represents the predetermined number of baits according to the difficulty level.
    character : int
        Represents the sequence number of the character selected by the user.

    '''

    canvas.create_image(0, 0, "mainbg.png")
    canvas.create_image(100, 150, "leveltext.png")
    canvas.create_image(100, 250, "easy.png")
    canvas.create_image(225, 250, "medium.png")
    canvas.create_image(350, 250, "hard.png")
    a = 0
    while a<1:
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            if 100 < click.x < 150 and 250 < click.y < 300:
                bait_number = 10
                a += 1
                canvas.delete_all()
            if 225 < click.x < 275 and 250 < click.y < 300:
                bait_number = 20
                a += 1
                canvas.delete_all()
            if 350 < click.x < 400 and 250 < click.y < 300:
                bait_number = 30
                a += 1
                canvas.delete_all()
        canvas.update()
    canvas.create_image(0, 0, "mainbg.png")
    canvas.create_image(100, 150, "caractertext.png")
    canvas.create_image(100, 250, "lopu.png")
    canvas.create_image(225, 250, "lopu2.png")
    canvas.create_image(350, 250, "lopu3.png")
    while a<2:
        clicksc = canvas.get_new_mouse_clicks()
        for click in clicksc:
            if 100 < click.x < 150 and 250 < click.y < 300:
                character = 1
                a += 1
                canvas.delete_all()
                canvas.create_image(0, 0, "bg1.png")
            if 225 < click.x < 275 and 250 < click.y < 300:
                character = 2
                a += 1
                canvas.delete_all()
                canvas.create_image(0, 0, "bg3.png")
            if 350 < click.x < 400 and 250 < click.y < 300:
                character = 3
                a += 1
                canvas.delete_all()
                canvas.create_image(0, 0, "bg2.png")
        canvas.update()        
    
    return bait_number, character


def main():

    canvas = Canvas()
    # Create a canvas of the given sizes
    canvas.set_canvas_size(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Set the canvas title
    canvas.set_canvas_title("Lopu")
    # Apply the canvas background color.
    canvas.set_canvas_background_color("black")
    # Call the intro function
    bait_number, character= create_intro(canvas)
    score = 0
   
    if bait_number > 0:
        
        # Create random baits     
        baits= create_random_bait(canvas,bait_number)
        # Create Lopu, initially in the top-left corner
        lopu = create_lopus(canvas, character)
        canvas.update()
        # Get current time
        start = time.time()
        # Continually listen for new key presses to move Lopu
        while score != bait_number:
            key_presses = canvas.get_new_key_presses()
            for press in key_presses:
                # Move Lopu in the appropriate direction
                if press.keysym == "Left":
                    canvas.move(lopu, -BALL_STEP_SIZE, 0)
                elif press.keysym == "Right":
                    canvas.move(lopu, BALL_STEP_SIZE, 0)
                elif press.keysym == "Up":
                    canvas.move(lopu, 0, -BALL_STEP_SIZE)
                elif press.keysym == "Down":
                    canvas.move(lopu, 0, BALL_STEP_SIZE)
            # Teleport Lopu to the end of the map
            if canvas.get_top_y(lopu) + 50 > CANVAS_HEIGHT:
                canvas.move(lopu, 0, -CANVAS_HEIGHT)
            if canvas.get_top_y(lopu) < 0:
                canvas.move(lopu, 0, +CANVAS_HEIGHT)
            if canvas.get_left_x(lopu) < 0:
                canvas.move(lopu, +CANVAS_HEIGHT, 0)
            if canvas.get_left_x(lopu) + 50 > CANVAS_WIDTH:
                canvas.move(lopu, -CANVAS_HEIGHT, 0)
            score = destroy(canvas, lopu, baits, score)    
            canvas.update()
        # Get current time
        end = time.time()
        # Call the outro function
        create_outro(canvas, end, start)
        
    canvas.mainloop()   
        
if __name__ == "__main__":
    main()    
       


