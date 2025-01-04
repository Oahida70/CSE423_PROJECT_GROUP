def render_text(string, x, y):
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2f(x, y)
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))



def render_powerup_score():
    global powerup_score
    glColor3f(1.0, 1.0, 1.0)  
    glRasterPos2f(10, HEIGHT - 20)  
    score_string = f"Power: {powerup_score}"
    for char in score_string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))


def render_jump_score():
    global score_points
    glColor3f(1.0, 1.0, 1.0)  
    glRasterPos2f(650, HEIGHT - 20)  
    score_string = f"Bounce: {int(score_points / 29)}"
    for char in score_string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))


# Display
def display():

    global vehicle_trans_width, vehicle_trans_height, vehicle_velocity, jump_mechanism, car_bottom_left_y, car_top_left_y, car_top_right_y, car_bottom_right_y, game_over, background_color, health, angle

    glClearColor(*background_color) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(0.447, 1.0, 0.973)
    glPointSize(1)

    glBegin(GL_POINTS)
    for i in range(5):
        midpoint_circle(35 + vehicle_trans_width, 106 + vehicle_trans_height, i)
        midpoint_circle(60 + vehicle_trans_width, 106 + vehicle_trans_height, i)
    glEnd()

    if jump_mechanism:
        vehicle_trans_height += vehicle_velocity
        car_bottom_left_y += vehicle_velocity
        car_top_left_y += vehicle_velocity
        car_top_right_y += vehicle_velocity
        car_bottom_right_y += vehicle_velocity
        vehicle_velocity -= 0.2  # Adjust the gravity effect as needed
        if vehicle_trans_height <= 0:
            vehicle_trans_height = 0
            jump_mechanism = False
            vehicle_velocity = 0

    flower_ground()
    vehicle()
    trees()
    bird()
    move_birds()
    clouds()
    update()
    draw_ball()  
    update_ball()  
    render_powerup_score()  
    render_jump_score()

    if game_over:
        render_text("Game Over", WIDTH / 2 - 50, HEIGHT / 2)
    glutSwapBuffers()