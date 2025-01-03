car_bottom_left_x = 47
car_bottom_left_y = 100
car_bottom_right_x = 108
car_bottom_right_y = 100
car_top_left_x = 47
car_top_left_y = 135
car_top_right_x = 108
car_top_right_y = 135

def vehicle():
    global vehicle_trans_width, vehicle_trans_height

    draw_line_mpl(20 + vehicle_trans_width, 110 + vehicle_trans_height, 75 + vehicle_trans_width, 110 + vehicle_trans_height, (1, 1, 1))  # Lower straight line
    draw_line_mpl(20 + vehicle_trans_width, 110 + vehicle_trans_height, 20 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Left attached line
    draw_line_mpl(75 + vehicle_trans_width, 110 + vehicle_trans_height, 75 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Right attached line
    draw_line_mpl(20 + vehicle_trans_width, 120 + vehicle_trans_height, 30 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Left attached line to the right
    draw_line_mpl(30 + vehicle_trans_width, 120 + vehicle_trans_height, 30 + vehicle_trans_width, 130 + vehicle_trans_height, (1, 1, 1))  # To the right
    draw_line_mpl(75 + vehicle_trans_width, 120 + vehicle_trans_height, 65 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Right attached line to the left
    draw_line_mpl(65 + vehicle_trans_width, 120 + vehicle_trans_height, 65 + vehicle_trans_width, 130 + vehicle_trans_height, (1, 1, 1))  # To the left
    draw_line_mpl(30 + vehicle_trans_width, 130 + vehicle_trans_height, 65 + vehicle_trans_width, 130 + vehicle_trans_height, (1, 1, 1))  # Head

    draw_line_mpl(car_bottom_left_x, car_bottom_left_y, car_top_left_x, car_top_left_y, (0, 0, 0))
    draw_line_mpl(car_top_left_x, car_top_left_y, car_top_right_x, car_top_right_y, (0, 0, 0))
    draw_line_mpl(car_bottom_right_x, car_bottom_right_y, car_top_right_x, car_top_right_y, (0, 0, 0))
    draw_line_mpl(car_bottom_right_x, car_bottom_right_y, car_bottom_left_x, car_bottom_left_y, (0, 0, 0))
