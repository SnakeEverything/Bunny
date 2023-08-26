from Focus_Roots import *


def change():
    draw_circle(250,250,100,2)
    draw_ellipse(150,35,50,150,2)
    draw_ellipse(300,35,50,150,2)
    draw_circle(200,220,20,2)
    draw_circle(300,220,20,2)
    draw_line(start_pos=[200,280], end_pos=[300,280],width=2)
    draw_rect(230,280,20,20)
    draw_rect(250,280,20,20)
    write_text(text = "This is a money", x = 250, y=380, size=25)
draw(change)