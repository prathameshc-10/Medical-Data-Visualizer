"""Basic tests for the Medical Data Visualizer project."""
import os
import unittest
import pandas as pd
from medical_data_visualizer import draw_cat_plot, draw_heat_map


class MedicalDataVisualizerTests(unittest.TestCase):
    def test_cat_plot_returns_figure(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)
        self.assertTrue(os.path.exists("catplot.png"))

    def test_heat_map_returns_figure(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig)
        self.assertTrue(os.path.exists("heatmap.png"))


if __name__ == "__main__":
    unittest.main()
