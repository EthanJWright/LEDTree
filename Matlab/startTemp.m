temp = [-10 ,0, 20, 30, 40, 50, 60, 70, 80, 90, 95, 120]

red = [113, 15, 20 ,35, 63, 91, 119, 147, 175, 210, 255, 255]
green = [229, 200, 80, 60, 40, 36, 30, 24, 16, 12, 7, 2]
blue = [250, 250, 180, 150, 120, 100, 60, 30, 20, 15, 10, 5]
red_fit = polyfit(temp, red, 2)
green_fit = polyfit(temp, green, 2)
blue_fit = polyfit(temp, blue, 2)


for i = -50:1000
    solving = i/10
    rgb = [polyFind(solving, red_fit), polyFind(solving, green_fit), polyFind(solving, blue_fit)]
    r = rgb(1)/255
    g = rgb(2)/255
    b = rgb(3)/255
    bar(1, 'FaceColor', [r g b])
    pause(.001)
end

red_fit
green_fit
blue_fit