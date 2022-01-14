# Julia set generator with a GUI
import time
x1, x2 = -1.5, 1.5
y1, y2 = -1.5, 1.5

c_real, c_imag = -0.8, 0.156


def calc_pure_python(desired_width, max_iterations):
    '''Create a list of complex coordinates (zs) and complex parameteres(cs), 
    build Julia set and return number of iterations for each'''
    x_step = (x2 - x1) / desired_width
    y_step = (y2 - y1) / desired_width
    x, y = [], []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removbed,
    # we use it to simulate a real-world scenario with several input to our function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    print("Length of x:", len(x))
    print("total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__+" took ", secs, " seconds.")


def calculate_z_serial_purepython(maxiter, zs, cs):
    '''Calculate output list using Julia update rule'''
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z*z + c
            n += 1
        output[i] = n
    return output


if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with reasonable defaults
    # to match the C++ example.
    calc_pure_python(desired_width=1000, max_iterations=300)
