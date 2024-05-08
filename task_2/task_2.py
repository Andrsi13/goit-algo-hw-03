import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0) 

    for _ in range(3):  # Малюємо три відрізки для створення сніжинки
        koch_curve(t, order, size)
        t.right(120)  # Поворот на 120 градусів для наступного відрізка

    window.mainloop()

def main():
    order = int(input("Введіть рівень рекурсії (ціле число): "))
    draw_koch_curve(order)

if __name__ == "__main__":
    main()
