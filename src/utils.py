def create_board_block(screen_position,color,position_x, position_y,block_method):
    block_parameters = 37
    relative_position_x = position_x
    relative_position_y = position_y
    if screen_position == "horizontal":
         for i in range(18):
            #rendering the red and yellow color blocks
            if (i==1 or i==7 or i==8 or i==9 or i==10 or i==11) and color == "red":
                block_method(True,color,relative_position_x, relative_position_y)
            elif (i==6 or i==7 or i==8 or i==9 or i==10 or i==16) and color == "yellow":
                block_method(True,color,relative_position_x, relative_position_y)
            else:
                block_method(False,color,relative_position_x,relative_position_y)
            relative_position_x += block_parameters #creates new block at new position
            #reset position at selected intervals
            if i == 5 or i==11: 
                relative_position_y += block_parameters
                relative_position_x = position_x
    elif screen_position == "vertical":
        for i in range(18):
            #rendering the blue and green color basics
            if (i==4 or i==6 or i==7 or i==8 or i==9 or i==10) and color=="blue":
                block_method(True,color,relative_position_x,relative_position_y)
            elif (i==7 or i==8 or i==9 or i==10 or i==11 or i==13) and color=="green":
                block_method(True,color,relative_position_x, relative_position_y)
            else:
                block_method(False,color,relative_position_x, relative_position_y)
            relative_position_y += block_parameters #creats new block at new position
            #reset position at selected image
            if i==5 or i==11:
                relative_position_x += block_parameters
                relative_position_y = position_y
    else:
        pass


def initial_positions():
    return{
        "1":[70,70],
        "2":[135,70],
        "3":[70,140],
        "4":[136,148]
        }
