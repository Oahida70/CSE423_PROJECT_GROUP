def update():
    global tree_speed,shifting_magnitude, t_l_l_x,t_u_l_x,t_u_r_x,t_l_r_x,t_u_r_y,c_l_l_x,c_l_l_y
    global c_l_r_x,c_l_r_y,c_u_l_x,c_u_l_y,c_u_r_x,c_u_r_y,score,start,tree_or_power
    if tree_or_power==True:
        if start==True:
            if tree_speed>=750:
                tree_speed=4
                t_l_l_x,t_l_l_y=719,100
                t_u_l_x,t_u_l_y=719,178
                t_u_r_x,t_u_r_y=774,178
                t_l_r_x,t_l_r_y=774,100
                tree_or_power=not tree_or_power
            tree_speed+=4
            t_l_l_x-=4
            t_u_l_x-=4
            t_u_r_x-=4
            t_l_r_x-=4
            if ((c_l_l_x<=t_l_l_x<=c_l_r_x) or (c_l_l_x<=t_l_r_x<=c_l_r_x)) and ((c_l_r_y>=t_u_r_y)):
                score+=1
                if score%29==0:
                    print(int(score/29))
                    if score%2==0:
                        if shifting_magnitude==720:
                            shifting_magnitude-=720
                        shifting_magnitude+=40
                        print(shifting_magnitude,"sm")
            elif ((c_l_l_x<=t_l_l_x<=c_l_r_x) or (c_l_l_x<=t_l_r_x<=c_l_r_x)) and ((c_l_r_y<=t_u_r_y)):
                print("game over")
                start=False
    else:
        global power_speed, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12
        if start==True:

                # Incrementing x-coordinates for horizontal movement
            p1 -= power_speed
            p3 -= power_speed
            p5 -= power_speed
            p7 -= power_speed
            p9 -= power_speed
            p11 -= power_speed
        if p11 < 0 or p1< 0 :
            p1 =700
            p3 = 730
            p5 = 730
            p7 =760
            p9 = 769
            p11 =790 
            tree_or_power=not tree_or_power