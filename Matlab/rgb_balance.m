function balance = rgb_balance(color)
balance = color
if balance < 0
    balance = 0
end
if balance > 255
    balance = 255
end

