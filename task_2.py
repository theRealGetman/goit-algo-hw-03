import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    level = int(input("Enter the recursion level (e.g., 1, 2, 3): "))
    for _ in range(3):
        koch_curve(t, level, size)
        t.right(120)

    window.mainloop()

# Виклик функції
draw_koch_curve()
