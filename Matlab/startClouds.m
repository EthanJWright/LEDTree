wind = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

red = [176, 201, 221, 230, 240, 250, 255, 254, 240, 210, 200]
green = [194, 215, 230 240, 250, 255, 255, 252, 240, 210, 200]
%blue = [255,255, 255, 255, 255, 237, 219, 196, 175, 165, 142]
blue = [255,255, 255, 255, 255,255,255, 255, 220, 210, 200]
red_fit = polyfit(wind, red, 2)
green_fit = polyfit(wind, green, 2)
blue_fit = polyfit(wind, blue, 2)


for i = 0:100
    rgb = get_rgb(i, red_fit, green_fit, blue_fit)
    r = (rgb(1) - 3)/255
    g = (rgb(2) - 3)/255
    b = (rgb(3) - 6)/255
    bar(1, 'FaceColor', [r g b])
    pause(.1)
end
