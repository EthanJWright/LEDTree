function color = polyFind(wind, pixel_fit)
color = pixel_fit(1) * (wind^2) + pixel_fit(2)*(wind) + pixel_fit(3)
