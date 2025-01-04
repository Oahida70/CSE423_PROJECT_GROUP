#Day Night Transition


day_color = [0.53, 0.81, 0.92, 1.0]  # Sky blue (day)
night_color = [0.0, 0.0, 0.0, 1.0]  # Black (night)
transition_speed = 0.01  # Speed of color transition
transitioning_to_day = False
transitioning_to_night = False

def update_background_color(target_color):
    global background_color, transition_speed
    for i in range(3):  
        if background_color[i] < target_color[i]:
            background_color[i] += transition_speed
            if background_color[i] > target_color[i]:
                background_color[i] = target_color[i]
        elif background_color[i] > target_color[i]:
            background_color[i] -= transition_speed
            if background_color[i] < target_color[i]:
                background_color[i] = target_color[i]



# Game Display

game_paused = False


def keyboard(key, x, y):
    global vehicle_trans_height, vehicle_velocity, jump_mechanism, background_color, game_paused
    global transitioning_to_day, transitioning_to_night, day_color, night_color

    if key == b' ' and not jump_mechanism and not game_paused:
        jump_mechanism = True
        vehicle_velocity = 9  
    elif key == b'd':
        transitioning_to_day = True  # Start the transition to day color
        transitioning_to_night = False
    elif key == b'n':
        transitioning_to_night = True  # Start the transition to night color
        transitioning_to_day = False
    elif key == b'p':
        game_paused = True  # Pause the game
    elif key == b's':
        game_paused = False  # Resume the game





def animation():
    global transitioning_to_day, transitioning_to_night, day_color, night_color
    if not game_paused:
        if transitioning_to_day:
            update_background_color(day_color)
            if background_color == day_color:
                transitioning_to_day = False
        elif transitioning_to_night:
            update_background_color(night_color)
            if background_color == night_color:
                transitioning_to_night = False
        glutPostRedisplay()



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
