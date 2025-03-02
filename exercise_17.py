import matplotlib.pyplot as plt
import math

def read_data(filename):
    with open(filename, 'r') as file:
        data = file.readline().strip().split()
        x1, y1, R1, x2, y2, R2, x3, y3, R3 = map(float, data)
    return (x1, y1, R1), (x2, y2, R2), (x3, y3, R3)

def circles_intersect(circle1, circle2):
    (x1, y1, R1) = circle1
    (x2, y2, R2) = circle2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return abs(R1 - R2) <= distance <= (R1 + R2)

def plot_circles(circle1, circle2, circle3):
    fig, ax = plt.subplots()
    
    for (x, y, r) in [circle1, circle2, circle3]:
        circle = plt.Circle((x, y), r, color='blue', fill=False)
        ax.add_artist(circle)
    
    ax.set_aspect('equal', adjustable='datalim')
    ax.plot()
    plt.xlim(min(circle1[0] - circle1[2], circle2[0] - circle2[2], circle3[0] - circle3[2]) - 1,
             max(circle1[0] + circle1[2], circle2[0] + circle2[2], circle3[0] + circle3[2]) + 1)
    plt.ylim(min(circle1[1] - circle1[2], circle2[1] - circle2[2], circle3[1] - circle3[2]) - 1,
             max(circle1[1] + circle1[2], circle2[1] + circle2[2], circle3[1] + circle3[2]) + 1)
    plt.show()

def main():
    filename = input("Введите имя файла с данными: ")
    circle1, circle2, circle3 = read_data(filename)
    
    if (circles_intersect(circle1, circle2) and
        circles_intersect(circle1, circle3) and
        circles_intersect(circle2, circle3)):
        print("Все окружности пересекаются.")
        plot_circles(circle1, circle2, circle3)
    else:
        print("Окружности не пересекаются. Проверьте исходные данные.")

if __name__ == "__main__":
    main()
