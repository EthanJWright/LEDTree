wind = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

red = [175, 186, 201, 219, 234, 220, 208, 188, 167, 139, 119]
green = [206, 212, 223, 232, 242, 226, 212, 191, 170, 149, 128]
blue = [255,255, 255, 255, 255, 237, 219, 196, 175, 165, 142]

red_fit = polyfit(wind, red, 3)
green_fit = polyfit(wind, green, 3)
blue_fit = polyfit(wind, blue, 3)

for i = 0:100
    rgb = get_rgb((i/100), red_fit, green_fit, blue_fit)
    r = rgb(1)/255
    g = rgb(2)/255
    b = rgb(3)/255
    bar(1, 'FaceColor', [r g b])
    pause(.1)
end