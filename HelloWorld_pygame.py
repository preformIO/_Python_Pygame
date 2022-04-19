# Módulos | imports
# ---------------------------------------------------------------------
# region
import sys
import pygame
from pygame.locals import *
from sympy import Point, pi, sin, cos
# endregion
# ---------------------------------------------------------------------

# Constantes | constants declarations
# ---------------------------------------------------------------------
# region
WIDTH = 640
HEIGHT = 480
FRAMES_PER_SECOND = 30 
# endregion
# ---------------------------------------------------------------------

# Variables Globales | global variables
# ---------------------------------------------------------------------
# region
win_sfc = None # initialize global for testing drawing on game surface
render_i = None # gets incremented every draw loop
# endregion
# ---------------------------------------------------------------------
 
# Clases | local classes
# ---------------------------------------------------------------------
# region

# endregion
# ---------------------------------------------------------------------
 
# Funciones | local functions
# ---------------------------------------------------------------------
# region

# draw white circle with radius of 25
def drawCircle():
    # set up position veriables
    circ_pos = Point(100, 240)
    circ_radius = 25

    # draw circle
    color = Color(255, 255, 255)
    stroke = 0 # with 0 stroke, circle will be filled
    pygame.draw.circle(win_sfc, color, circ_pos, circ_radius, stroke)

    pass

# draw white circle outline  with radius of 25, stroke of 3
def drawCircleOutline():
    # set up position variables
    circ_pos = Point(175, 240)
    circ_radius = 25

    # draw circle outline
    color = Color(255, 255, 255)
    stroke = 3
    pygame.draw.circle(win_sfc, color, circ_pos, circ_radius, stroke)

    pass

# draw a red 3/4-circle arc from pi/2 to 2pi with stroke of 5
def drawArc():
    # set up position variables
    arc_pos = Point(275, 240)
    arc_radius_x = 50
    arc_radius_y = 25
    arc_rect = Rect(
        arc_pos.x - arc_radius_x, 
        arc_pos.y - arc_radius_y, 
        arc_radius_x * 2, 
        arc_radius_y * 2,
    )
    arc_start = pi / 2
    arc_end = 2*pi 

    # draw arc
    stroke = 5
    color = Color(255, 0, 0)
    pygame.draw.arc(win_sfc, color, arc_rect, arc_start, arc_end, stroke)

    pass    

# draw a solid black rectangle with a blue-gray outline
def drawRectangle():
    # set up position variables
    rect_pos = Point(350, 215)
    rect_width = 150
    rect_height = 50
    rect = Rect(rect_pos.x, rect_pos.y, rect_width, rect_height)

    # draw solid rectangle
    color = Color(0, 0, 0)
    pygame.draw.rect(win_sfc, color, rect)
    
    # draw rect outline
    color = Color(63, 63, 127)
    stroke = 5
    pygame.draw.rect(win_sfc, color, rect, stroke)

    pass    

# endregion
# ---------------------------------------------------------------------
 
# Funcion principal | main function definition
# --------------------------------------------------------------------- 
def main():
    # Crear una ventana | create window
    # -------------
    # region
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame | Pygame Tutorial")
    # get instance of window surface and store in global "win_sfc"
    # to use later in drawing funcitons
    global win_sfc
    win_sfc = pygame.display.get_surface()
    print(f'Got reference to surface "{win_sfc}"')
    # endregion#
    # -------------
    
    # enter main draw / game loop
    # -------------
    global render_i
    render_i = 0
    while True:
        # draw elements
        # -------------
        # region
        # clear background with dark grey
        win_sfc.fill((63, 63, 63))
        # draw foreground elements on top of background
        drawCircle()
        drawCircleOutline()
        drawArc()
        drawRectangle()
        # endregion
        # -------------

        # update display (must be done every render loop)
        # ----------
        pygame.display.update()
        pygame.time.delay(1000//FRAMES_PER_SECOND) # wait fraction of a second betwen updates
        # -------------

        # increment render count
        # ----------
        render_i = render_i + 1
        # -------------

        # handle events
        # ----------
        for evento in pygame.event.get():
            # keyboard input
            # ----------
            if evento.type == pygame.KEYDOWN or evento.type == pygame.KEYUP:
                # handle modifier key presses
                # ----------
                if evento.mod == pygame.KMOD_NONE:
                    print('No modifier keys were in a pressed state when this '
                        'event occurred.')
                else:
                    if evento.mod & pygame.KMOD_LSHIFT:
                        print('Left shift was in a pressed state when this event '
                            'occurred.')
                    if evento.mod & pygame.KMOD_RSHIFT:
                        print('Right shift was in a pressed state when this event '
                            'occurred.')
                    if evento.mod & pygame.KMOD_SHIFT:
                        print('Left shift or right shift or both were in a '
                            'pressed state when this event occurred.')            
                        pass
                    pass
                # ----------

                # handle general key presses
                # ----------
                print(f'Key event captured for key named "{pygame.key.name(evento.key)}"')
                # ----------

                # exit application on "Esc" pressed
                # ----------
                if evento.key == pygame.K_ESCAPE:
                    print("\nyou pressed ESCAPE, so exiting...\n")
                    sys.exit(0)
                    pass
                # ----------
                pass
            # -------------

            # exit application on window quit event
            # ----------
            if evento.type == QUIT:
                sys.exit(0)
                pass
            # -------------
            pass
        # -------------
        pass
    # -------------

    return 0
    pass
# ---------------------------------------------------------------------


# Ejecutar solo si se ejecuta como aplicación principal 
# --
# Only execute if run as main application
# ---------------------------------------------------------------------
if __name__ == '__main__':
    pygame.init()
    main()
    
    pass
# ---------------------------------------------------------------------
