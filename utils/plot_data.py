import os
import matplotlib.pyplot as plt

def create_figure(data, axis_names, figure_name,path):
    
    # Extract the X & Y data
    x_data, y_data = data
    x_label, y_label = axis_names
    
    # Default parameters
    title = 'Plot'
    plot_type = 'line'
    color = 'blue'
    thickness = 1
    #plt.figure(figsize=(8, 6))
    
    if plot_type == 'line':
        plt.plot(x_data, y_data, color=color, linewidth=thickness)
    elif plot_type == 'scatter':
        plt.scatter(x_data, y_data, color=color)
    elif plot_type == 'bar':
        plt.bar(x_data, y_data, color=color)
    else:
        raise ValueError("Invalid plot type. Choose 'line', 'scatter', or 'bar'.")
    
    
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show(block=False)
    plt.savefig(f'{path}/{figure_name}.png', bbox_inches='tight', dpi=420)    
    input('Press Enter to close')
    plt.close()

