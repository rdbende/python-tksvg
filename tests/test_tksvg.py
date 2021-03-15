"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2021 RedFantom
"""
from unittest import TestCase
import tkinter as tk
import tksvg
import os


class TestTkSVG(TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self._path = os.path.abspath(os.path.dirname(__file__))

    def test_tksvg_load(self):
        tksvg.load(self.window)
        # Create test PhotoImage
        tk.PhotoImage(file=os.path.join(self._path, "orb.svg"))

    def test_svg_image(self):
        tksvg.load(self.window)
        image = tksvg.SvgImage(file=os.path.join(self._path, "orb.svg"), scale=0.5)
        self.assertEqual(image.cget("scale"), 0.5)
        self.assertEqual(image.cget("scale"), image["scale"])

        label = tk.Label(self.window, image=image)
        label.pack()
        self.window.update()

    def tearDown(self):
        self.window.destroy()
