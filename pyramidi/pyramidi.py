def pyramid(layers):
    stars = layers * 2 - 1

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
