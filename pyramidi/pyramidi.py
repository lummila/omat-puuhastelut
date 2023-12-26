def pyramid(layers):
    stars = 1
    for i in range(layers - 1):
        stars += 2

    output = []
    for i in range(layers):
        star = "*"
        for x in range(i):
            star += "**"

        layer = star.center(stars)
        output.append(layer)

    return output


layers = int(input("Layers: "))
result = pyramid(layers)

for entry in result:
    print(entry)
