"""This is Ella and Naomi's project"""

import pygame
import random
import sys

pygame.init()

# dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FantasyGame! - Simplified")

# 
font = pygame.font.Font(None, 48)
bg_color = (30, 30, 30)
text_color = (255, 255, 255)