"""
Program: Solar System Explorer - Settings
Author: Xinyi Yang
Purpose: Store the settings for the Solar System Explorer, including screen size, FPS, and background.
Starter/resources: Python Crash Course
Date: November 2026
"""
from pathlib import Path

class Settings:
    """A class to store all settings for Solar System Explorer."""
    def __init__(self):
        self.name = "Solar System Explorer"
        self.screen_w = 900
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path(__file__).parent / "Assets" / "images" / "star_sky.jpg"
