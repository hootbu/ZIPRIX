from graphics import Canvas
import random
import time

'''
EEE 103 INTRO TO PROGRAMMING_GUZ2021
GAME NAME:
ZIPRIX
----------------
Students: 
EMIR YORGUN 2106102066
EKIN BUSE AKBAYDOGAN 2006102023
'''

#Some values
canvas = Canvas()
frameWidth = 1200
frameHeight = 800
neoHeight= 70
neoWidth = 120
buildingWidth = 100
neoVal = 200
buildingVal = 10
delay = 0.02
space_with_builds = 80

#Game's opening screen
def startScreen(frameWidth, frameHeight):
    kapakCount = 1
    kapak = canvas.create_image_with_size(0, 0, frameWidth, frameHeight, 'kapak.png')
    while kapakCount == 1:
        lol = canvas.get_new_key_presses()
        for press in lol:
            if press.keysym == "e":
                canvas.delete(kapak)
                kapakCount -= 1
        time.sleep(delay)
        canvas.update()

#Main functions
def main():
    #Canvas creating and set features.
    canvas.set_canvas_size(frameWidth, frameHeight)
    canvas.set_canvas_title("ZIPRIX")
    background = canvas.create_image_with_size(0, 0, frameWidth, frameHeight, 'back.png')
    startScreen(frameWidth, frameHeight)

    #Neo (the name of the flying man)
    neo = canvas.create_image_with_size(50, 350 , neoWidth, neoHeight, 'neo2.png')

    #Building lists.
    bina1_list = []
    bina2_list = []

    neo_overlapping = []
    change = 1
    while change == 1:
        #Building 1 is created and building 2 is created in proportion to building 1's height.
        buildingHeight = random.randint(40,550)
        bina1_list.append(canvas.create_image_with_size(frameWidth ,0, buildingWidth, buildingHeight, "bina2.png"))
        bina2_list.append(canvas.create_image_with_size(frameWidth , buildingHeight + neoVal, buildingWidth, frameWidth , "bina2.png"))
        
        for i in range(space_with_builds):
            if change == 1:
                #Neo jumps when 'Up' key is pressed.
                presses = canvas.get_new_key_presses()
                for press in presses:
                    if press.keysym == "Up":
                        canvas.move(neo, 0, -50)
                        time.sleep(0.0005)
                        canvas.update()
                #Neo descends when 'Down' button is pressed.
                    if press.keysym == "Down":
                        canvas.move(neo, 0, 50)
                        time.sleep(0.0005)
                        canvas.update()
                canvas.move(neo, 0, 5)

                #Building 1 and building 2 are moving towards neo.
                for bina1 in bina1_list:
                    canvas.move(bina1, -5, 0)

                for bina2 in bina2_list:
                    canvas.move(bina2, -5, 0)
                    
                #This code ends the game if Neo collides with more than three objects between it coordinates.
                neo_overlapping = canvas.find_overlapping(canvas.get_left_x(neo), canvas.get_top_y(neo), (canvas.get_left_x(neo) + neoWidth), (canvas.get_top_y(neo) + neoHeight))
                if len(neo_overlapping) == 3 or canvas.get_top_y(neo) <=0  or (canvas.get_top_y(neo) + neoHeight) >=frameHeight:
                    change -= 1

            canvas.update()
            time.sleep(delay)
    
    #Game over screen
    gameover = canvas.create_text((frameWidth/2), (frameHeight/2) - 65,  "GAME OVER")
    canvas.set_color(gameover, "white")
    canvas.set_font(gameover, 'Times New Roman', 60)

    #Score counter
    score = len(bina1_list) - 3
    if score <0:
        score = 0
    score_title = canvas.create_text((frameWidth/2), (frameHeight/2) + 40,  str(score))
    canvas.set_color(score_title, "white")
    canvas.set_font(score_title, 'Times New Roman', 100)
    canvas.update()
    
    restartGame()
    canvas.update()

#The function of returning of the main screen when we press the 'r' key.
def restartGame():
    restartGame = 1
    while restartGame == 1:
        restart = canvas.get_new_key_presses()
        for press in restart:
            print(press.keysym)
            if press.keysym == "r":
                canvas.delete_all()
                restartGame = 0
                main()
            time.sleep(delay)
        time.sleep(delay)
        canvas.update()

if __name__ == '__main__':
    main()
