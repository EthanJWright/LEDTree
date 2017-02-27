function rgb = get_rgb(wind, red_fit, green_fit, blue_fit)
    rgb = [polyFind(wind, red_fit), polyFind(wind, green_fit), polyFind(wind, blue_fit)]
    
