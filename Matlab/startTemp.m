%temp = [20, 30, 40, 50, 60, 70, 80, 90, 100] 
%red = [255, 174, 34, 0, 0, 63, 255, 255, 255]
%green = [0, 0, 0, 178, 255, 255, 255, 127, 0]
%blue = [250, 255, 255, 255, 140, 0, 0, 0, 0]

temp = [1, 8, 16, 24, 30] 
red = [255, 255, 255, 255, 0]
green = [0, 0, 255, 255, 255]
blue = [255, 0, 0, 255, 255]

red_fit = polyfit(temp, red, 2)
green_fit = polyfit(temp, green, 2)
blue_fit = polyfit(temp, blue, 2)


for i = 0:300
    solving = (300 - i)/10
    rgb = [polyFind(solving, red_fit), polyFind(solving, green_fit), polyFind(solving, blue_fit)]    
    r = rgb_balance(rgb(1))/255
    g = rgb_balance(rgb(2))/255
    b = rgb_balance(rgb(3))/255
    bar(1, 'FaceColor', [r g b])
    pause(.001)
end

red_fit
green_fit
blue_fit