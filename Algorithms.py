def draw_line_mpl(x1, y1, x2, y2, color):
    glColor3f(*color)
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    d = 2 * dy - dx
    y = y1

    for x in range(int(x1), int(x2) + 1):
        if steep:
            glBegin(GL_POINTS)
            glVertex2f(int(y), int(x)) 
            glEnd()
        else:
            glBegin(GL_POINTS)
            glVertex2f(int(x), int(y))
            glEnd()
        
        if d > 0:
            y += 1 if y1 < y2 else -1 
            d -= 2 * dx  
        d += 2 * dy 





def circle_points(point_x, point_y, center_x, center_y):
    glVertex2f(point_x + center_x, point_y + center_y)
    glVertex2f(point_y + center_x, point_x + center_y)
    glVertex2f(point_y + center_x, -point_x + center_y)
    glVertex2f(point_x + center_x, -point_y + center_y)
    glVertex2f(-point_x + center_x, -point_y + center_y)
    glVertex2f(-point_y + center_x, -point_x + center_y)
    glVertex2f(-point_y + center_x, point_x + center_y)
    glVertex2f(-point_x + center_x, point_y + center_y)





def midpoint_circle(center_x, center_y, radius):
    decision_param = 1 - radius
    current_x = 0
    current_y = radius
    circle_points(current_x, current_y, center_x, center_y)
    while current_x < current_y:
        if decision_param < 0:
            decision_param = decision_param + 2 * current_x + 3
        else:
            decision_param = decision_param + 2 * (current_x - current_y) + 5
            current_y = current_y - 1
        current_x = current_x + 1
        circle_points(current_x, current_y, center_x, center_y)