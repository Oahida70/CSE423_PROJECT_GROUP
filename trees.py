tree_bottom_left_x = 719
tree_bottom_left_y = 100
tree_bottom_right_x = 774
tree_bottom_right_y = 100
tree_top_left_x = 719
tree_top_left_y = 178
tree_top_right_x = 774
tree_top_right_y = 178

item1_x, item1_y = 700, 100
item2_x, item2_y = 730, 130
item3_x, item3_y = 730, 100
item4_x, item4_y = 760, 130
item5_x, item5_y = 760, 100
item6_x, item6_y = 790, 130

is_tree_or_power_up = True

def trees():
    global is_tree_or_power_up
    if is_tree_or_power_up:
        global obstacle_speed
        glEnable(GL_POINT_SMOOTH)
        
        # Tree trunk (drawn as vertical lines)
        for i in range(755 - obstacle_speed, 745 - obstacle_speed, -1):
            draw_line_mpl(i, 100, i, 130, (165 / 255, 42 / 255, 42 / 255))  # Tree trunk
        
        # Tree bounding box (rectangle)
        glColor3f(1, 1, 1)
        draw_line_mpl(tree_bottom_left_x, tree_bottom_left_y, tree_bottom_right_x, tree_bottom_right_y, (1, 1, 1))  # Bottom line
        draw_line_mpl(tree_bottom_left_x, tree_bottom_left_y, tree_top_left_x, tree_top_left_y, (1, 1, 1))  # Left line
        draw_line_mpl(tree_top_left_x, tree_top_left_y, tree_top_right_x, tree_top_right_y, (1, 1, 1))  # Top line
        draw_line_mpl(tree_top_right_x, tree_top_right_y, tree_bottom_right_x, tree_bottom_right_y, (1, 1, 1))  # Right line
        
        # Tree foliage (drawn as points)
        glColor3f(0, 1, 0)
        glPointSize(20)
        glBegin(GL_POINTS)
        glVertex2f(750 - obstacle_speed, 140)
        glVertex2f(735 - obstacle_speed, 145)
        glVertex2f(765 - obstacle_speed, 145)
        glVertex2f(750 - obstacle_speed, 150)
        glVertex2f(750 - obstacle_speed, 166)
        glEnd()
    else:
        # Power-up or other items
        glPointSize(3)
        draw_line_mpl(item1_x, item1_y, item2_x, item2_y, (0, 0, 1))
        draw_line_mpl(item2_x, item2_y, item3_x, item3_y, (0, 1, 0))
        draw_line_mpl(item3_x, item3_y, item4_x, item4_y, (1, 0, 0))
        draw_line_mpl(item4_x, item4_y, item5_x, item5_y, (0, 0, 1))
        draw_line_mpl(item5_x, item5_y, item6_x, item6_y, (1, 0, 0))
