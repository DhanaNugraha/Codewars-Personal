h = 3 
bounce = 1 
window = 1.5

def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        output = 0
        while h > window:
            output += 1
            h = h * bounce
            if h > window:
                output += 1

        return output
    return -1

print(bouncing_ball(h, bounce, window))