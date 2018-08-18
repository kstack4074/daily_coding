from random import uniform

def generate():
    return (uniform(-1,1), uniform(-1,1))

def is_in_circle(coords):
    return (coords[0] * coords[0] + coords[1] * coords[1]) < 1

def estimate():
    iterations = 10000000
    in_circle = 0
    n = 0
    pi = 0
    keep_calc = True

    while keep_calc:
        n += 1
        if is_in_circle(generate()):
            in_circle += 1

        new_pi = 4 * (in_circle/n)

        if abs(new_pi - pi) < 0.0001 and n >= iterations:
            keep_calc = False

        pi = new_pi
    return pi


print(estimate())
