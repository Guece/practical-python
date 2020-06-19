height = 100
bounce = 3 / 5
bounceAmount = 10

for bounces in range(bounceAmount) :
    height = height * bounce
    print(round(height, 4))
