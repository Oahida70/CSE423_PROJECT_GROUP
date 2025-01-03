def update_ball():
    global ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, HEIGHT, WIDTH, car_bottom_left_x, car_bottom_right_x, car_bottom_left_y, car_top_left_y, car_top_right_x, car_bottom_right_y

    
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

   
    if ball_y - ball_radius <= 0:
        ball_y = ball_radius
        ball_velocity_y *= -1  

    
    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity_y *= -1

   
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_velocity_x *= -1



    if (car_bottom_left_x <= ball_x <= car_bottom_right_x) and (car_bottom_left_y <= ball_y <= car_top_left_y):
        ball_velocity_y *= -1  # Reverse vertical velocity
        ball_y = car_top_left_y + ball_radius
        ball_velocity_y *= +1  # Increase power-up points by 20


    if (tree_bottom_left_x <= ball_x <= tree_bottom_right_x) and (tree_bottom_left_y <= ball_y <= tree_top_left_y):
        ball_velocity_y *= -1
        ball_y = tree_top_left_y + ball_radius

