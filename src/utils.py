def create_board_block(screen_position,position_x, position_y,block_method):
    block_parameters = 37
    relative_position_x = position_x
    relative_position_y = position_y
    if screen_position == "horizontal":
         for i in range(18):
            block_method(False,relative_position_x,relative_position_y)
            relative_position_x += block_parameters
            if i == 5 or i==11: 
                relative_position_y += block_parameters
                relative_position_x = position_x
    elif screen_position == "vertical":
        for i in range(18):
            block_method(False, relative_position_x, relative_position_y)
            relative_position_y += block_parameters
            if i==5 or i==11:
                relative_position_x += block_parameters
                relative_position_y = position_y
    else:
        pass
