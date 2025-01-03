def ground():
    draw_line_mpl(0, 100, 800, 100, (1, 1, 1))
    for i in particles:
        glBegin(GL_POINTS)
        glVertex2f(i[0], i[1])
        glEnd()

for i in range(800):
        particles.append((i, random.randint(92, 99)))
