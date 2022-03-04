#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos | imports
import sys
import pygame
from pygame.locals import *

# Constantes | constants declarations
WIDTH = 640
HEIGHT = 480

# Clases | local classes
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones | local functions
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------

# Funcion principal | main function definition
# --------------------------------------------------------------------- 
def main():
    # Crear una ventana | create window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame | Pygame Tutorial")

    # Mantener ventana abierta | keep window open
    while True:

        # Si queremos cerrar la ventana, deje de ejecutarse | exit on window quit
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
                pass
            pass
        pass
    
    return 0
    pass
# ---------------------------------------------------------------------


# Ejecutar solo si se ejecuta como aplicación principal 
# --
# Only execute if fun as main application
# ---------------------------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()
    
    pass
# ---------------------------------------------------------------------
