"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2021 RedFantom
"""
from unittest import TestCase
import tkinter as tk
import tksvg


class TestTkSVG(TestCase):
    def setUp(self):
        self.window = tk.Tk()

    def test_tksvg_load(self):
        tksvg.load(self.window)
        # Create test PhotoImage
        tk.PhotoImage(file="tests/orb.svg")
