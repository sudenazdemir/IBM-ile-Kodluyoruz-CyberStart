import math

# Noktaların Tanımlanması
points = [(3, 5), (6, 20), (8, 12), (5, 8)]  

# Öklid Mesafesi İçin  Fonksiyon 
def oklidMesafe(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mesafelerin Hesaplanması
mesafeler = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        mesafe = oklidMesafe(points[i], points[j])
        mesafeler.append(mesafe)

# Minimum Mesafenin Bulunması
min_mesafe = min(mesafeler)
print("Minimum mesafe:", min_mesafe)
