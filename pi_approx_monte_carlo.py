import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image as Im
import os
from IPython.display import Image, display

#number of sample points
N = 10000

inside_circle = 0
x_inside, y_inside = [], []
x_outside, y_outside = [], []

iteration = 0 
plots = 0

for _ in range(N):
    iteration += 1
    x, y = np.random.uniform(0, 1, 2)  # Generate random (x, y) in unit square
    distance = x**2 + y**2  # Check if inside the quadrant
    
    # all circle points are 1 from origin, so if distance is less than 1, it is inside the circle
    if distance <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

    estimate = (inside_circle / iteration) * 4  

    
    if iteration % 100 == 0:

        plots += 1

        fig, ax = plt.subplots(figsize=(6,6))
        ax.scatter(x_inside, y_inside, color='blue', s=5)
        ax.scatter(x_outside, y_outside, color='red', s=5) 

        #circle
        circle = plt.Circle((0, 0), 1, color='black', fill=False)
        ax.add_patch(circle)

        #square 
        square_outline = plt.Polygon([[0, 0], [1, 0], [1, 1], [0, 1]], closed=True, edgecolor='black', fill=None)
        ax.add_patch(square_outline)

        plt.subplots_adjust(bottom=0.2)


        ax.set_xlim(0, 1.1)
        ax.set_ylim(0, 1.1)
        ax.set_aspect('equal')
        ax.set_xticks(np.arange(0, 1.1, 0.1))
        ax.set_yticks(np.arange(0, 1.1, 0.1))

        plt.text(0.2, 1.05, f'n = r + b = {iteration}', ha='center')

        plt.text(0.6, 1.05, f'b = {len(x_inside)}', ha='center', color='blue')
        plt.text(0.8, 1.05, f'r = {len(x_outside)}', ha='center', color='red')

        plt.text(0.1, -0.15, r'$\frac{\pi}{4} \approx \frac{r}{n}$', ha='center', transform=ax.transAxes, fontsize=16)
        plt.text(0.5, -0.15, r'$\pi = 4 \cdot \frac{{{}}}{{{}}} = {:.4f}$'.format(len(x_outside), iteration, estimate), ha='center', transform=ax.transAxes, fontsize=16)

        output_dir = 'c:/Desktop/CS projects/monte_carlo/pi_solve_img'
        os.makedirs(output_dir, exist_ok=True)

        # Save the plot as an image file
        filename = os.path.join(output_dir, f'plot_variant_{iteration}.png')
        plt.savefig(filename, bbox_inches='tight')

        if iteration != N:
            plt.close()

print(f'Estimation of pi: {estimate}')

# Create a list of images
images_pi_solving = [Im.open(f'monte_carlo/pi_solve_img/plot_variant_{(i + 1) * 100}.png') for i in range(plots)]
# Save the images as a GIF
images_pi_solving[0].save('monte_carlo/solving_gif/pi_solver_monte-carlo.gif', save_all=True, append_images=images_pi_solving[1:], optimize=False, duration=500, loop=0)
