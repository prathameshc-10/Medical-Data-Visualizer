"""Run the medical data visualizations and save both charts."""
import matplotlib.pyplot as plt
from medical_data_visualizer import draw_cat_plot, draw_heat_map

if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()
    plt.show()
