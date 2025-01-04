# Birds
bird1_position = [305, 380]
bird2_position = [335, 400]
bird_wing_angle = 0
bird_wing_direction = 1  # 1 for flapping down, -1 for flapping up

def bird():
    global bird1_position, bird2_position, bird_wing_angle, bird_wing_direction

    glColor3f(0.447, 1.0, 0.973)
    glPointSize(1)

    
    bird_wing_angle += bird_wing_direction * 5
    if bird_wing_angle > 20 or bird_wing_angle < -20:
        bird_wing_direction *= -1

    # Bird 1
    draw_line_mpl(bird1_position[0], bird1_position[1], bird1_position[0] + 15, bird1_position[1], (.447, 1, .973))
    draw_line_mpl(bird1_position[0], bird1_position[1], bird1_position[0] + 13, bird1_position[1] + 8 + bird_wing_angle / 2, (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 13, bird1_position[1] + 8 + bird_wing_angle / 2, bird1_position[0] + 5, bird1_position[1], (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 5, bird1_position[1], bird1_position[0] + 5, bird1_position[1] - 10, (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 5, bird1_position[1] - 10, bird1_position[0], bird1_position[1], (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 13, bird1_position[1] + 8 + bird_wing_angle / 2, bird1_position[0] + 20, bird1_position[1] + 8 + bird_wing_angle / 2 + 10, (.447, 1, .973))

    # Bird 2
    draw_line_mpl(bird2_position[0], bird2_position[1], bird2_position[0] + 15, bird2_position[1], (.447, 1, .973))
    draw_line_mpl(bird2_position[0], bird2_position[1], bird2_position[0] + 13, bird2_position[1] + 8 + bird_wing_angle / 2, (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 13, bird2_position[1] + 8 + bird_wing_angle / 2, bird2_position[0] + 5, bird2_position[1], (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 5, bird2_position[1], bird2_position[0] + 5, bird2_position[1] - 10, (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 5, bird2_position[1] - 10, bird2_position[0], bird2_position[1], (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 13, bird2_position[1] + 8 + bird_wing_angle / 2, bird2_position[0] + 20, bird2_position[1] + 8 + bird_wing_angle / 2 + 10, (.447, 1, .973))


def move_birds():
    global bird1_position, bird2_position

    # Move birds horizontally
    bird1_position[0] += 1
    bird2_position[0] += 1

    # Loop the birds back to the left side of the screen
    if bird1_position[0] > WIDTH:
        bird1_position[0] = 0
    if bird2_position[0] > WIDTH:
        bird2_position[0] = 0