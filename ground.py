def ground():
    
    draw_line(0,100,800,100,(1,1,1))
    for i in gravels:
        glBegin(GL_POINTS)
        glVertex2f(i[0],i[1])
        glEnd()