# import colorgram
from turtle import Turtle, Screen
from random import choice

if __name__ == "__main__":
    # rgb_colors = []
    # colors = colorgram.extract('image.jpg', 30)
    # for color in colors:
    #     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

    # print(rgb_colors)

    color_list = [
        (202, 164, 110),
        (240, 245, 241),
        (149, 75, 50),
        (222, 201, 136),
        (53, 93, 123),
        (170, 154, 41),
        (138, 31, 20),
        (134, 163, 184),
        (197, 92, 73),
        (47, 121, 86),
        (73, 43, 35),
        (145, 178, 149),
        (14, 98, 70),
        (232, 176, 165),
        (160, 142, 158),
        (54, 45, 50),
        (101, 75, 77),
        (183, 205, 171),
        (36, 60, 74),
        (19, 86, 89),
        (82, 148, 129),
        (147, 17, 19),
        (27, 68, 102),
        (12, 70, 64),
        (107, 127, 153),
        (176, 192, 208),
        (168, 99, 102),
    ]

    t = Turtle()
    s = Screen()
    s.colormode(255)

    t.speed("fastest")
    t.penup()
    t.goto(-s.window_width() / 5, -s.window_height() / 5)
    t.pendown()
    t.speed("normal")

    for row in range(10):

        for _ in range(10):
            t.dot(20, choice(color_list))
            t.penup()
            t.forward(50)
            t.pendown()

        t.speed("fastest")
        t.penup()
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(50 * 10)
        t.left(180)

        t.pendown()
        t.speed("normal")

    s.exitonclick()
