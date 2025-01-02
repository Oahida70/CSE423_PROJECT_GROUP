def trees():
    global tree_or_power
    if tree_or_power==True:
        global tree_speed
        glEnable(GL_POINT_SMOOTH)
        for i in range(755-tree_speed,745-tree_speed,-1):
            draw_line(i,100,i,130,(165/255, 42/255, 42/255))
        #tree
        
        draw_line(t_u_l_x,t_u_l_y,t_l_l_x,t_l_l_y,(1,1,1))
        draw_line(t_l_r_x,t_l_r_y,t_u_r_x,t_u_r_y,(1,1,1))
        draw_line(t_u_l_x,t_u_l_y,t_u_r_x,t_u_r_y,(1,1,1))
        draw_line(t_l_l_x,t_l_l_y,t_l_r_x,t_l_r_y,(1,1,1))
        # draw_line
        glColor3f(0, 1, 0)
        glPointSize(20)
        glBegin(GL_POINTS)
        glVertex2f(750-tree_speed,140)
        glVertex2f(735-tree_speed,145)
        glVertex2f(765-tree_speed,145)
        glVertex2f(750-tree_speed,150)
        glVertex2f(750-tree_speed,166)

        glEnd()
