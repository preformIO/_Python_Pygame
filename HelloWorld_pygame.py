# -*- coding: utf-8 -*-
 
# Módulos | imports
import sys
import keyboard
import pygame
from pygame.locals import *

# Constantes | constants declarations
WIDTH = 640
HEIGHT = 480

win_sfc = None # initialize global for testing drawing on game surface
render_i = None # gets incremented every draw loop
 
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
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame | Pygame Tutorial")
    # get instance of window surface and store in global "win_sfc"
    # to use later in drawing funcitons
    global win_sfc
    win_sfc = pygame.display.get_surface()
    print(f'Got reference to surface "{win_sfc}"')
    
    # enter main draw / game loop
    global render_i
    render_i = 0
    while True:
        # draw elements
        # -------------
        # clear background with dark grey
        win_sfc.fill((15, 15, 15))
        # draw other elements below this line

        # update display (must be done every render loop)
        # ----------
        pygame.display.update()
        pygame.time.delay(1000//30) # wait one 30th of a second betwen updates

        # increment render count
        # ----------
        render_i = render_i + 1

        # handle window quit event
        # ----------
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
                pass
            pass
        pass

        # handle keyboard input
        # ----------
        try:
            # respond to "ENTER" presses
            if keyboard.is_pressed('ENTER'):
                print("\nyou pressed Enter..\n")
                pass
            # quit exit on "Esc" pressed
            if keyboard.is_pressed('Esc'):
                print("\nyou pressed Esc, so exiting...\n")
                sys.exit(0)
                pass
            pass
        except:
            break

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
