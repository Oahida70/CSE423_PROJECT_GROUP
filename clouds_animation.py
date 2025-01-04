def clouds():
    global cloud_shift_amount

    glEnable(GL_POINT_SMOOTH)
    glColor3f(0, 0, 1)
    glPointSize(20)
    glBegin(GL_POINTS)

    cloud_positions = [(100, 450), (300, 430), (500, 390), (700, 370)]
    
    for x, y in cloud_positions:
        glVertex2f(x + cloud_shift_amount, y)
        glVertex2f(x + 20 + cloud_shift_amount, y)
        glVertex2f(x + 40 + cloud_shift_amount, y)
        glVertex2f(x + 10 + cloud_shift_amount, y + 10)
        glVertex2f(x + 30 + cloud_shift_amount, y + 10)

    glEnd()

    cloud_shift_amount -= 0.5
    if cloud_shift_amount < -WIDTH:
        cloud_shift_amount = WIDTH 
