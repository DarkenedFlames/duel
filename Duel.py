#!/usr/bin/env python3
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from game import Game

if __name__ == "__main__":
    g = Game()
    g.run()