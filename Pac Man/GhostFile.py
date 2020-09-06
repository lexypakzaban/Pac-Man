__author__ = 'Lexy'
import pygame


class Ghost:
    STATE_DRIVING = 0

    DIRECTION_LEFT = 0
    DIRECTION_RIGHT = 1
    DIRECTION_UP = 2
    DIRECTION_DOWN = 3

    def __init__(self):
        """
        This is where we set up the variables for this particular object as soon as it is created.
        """
        self.x = 398
        self.y = 400
        self.vx = 0
        self.vy = 0
        self.width = 20
        self.height = 20
        self.i_am_alive = True
        self.my_image = pygame.image.load("PacManGraphics/ghost.png")
        self.state = Ghost.STATE_DRIVING
        self.facing_direction = Ghost.DIRECTION_UP

    def draw_self(self, surface, world_offset_x = 0, world_offset_y= 0):
        """
        It is this object's responsibility to draw itself on the surface. It will be told to do this often!
        :param surface:
        :return: None
        """
        surface.blit(self.my_image, self.get_collision_box())

        if self.facing_direction == Ghost.DIRECTION_RIGHT:
            surface.blit(self.my_image, self.get_collision_box())

        if self.facing_direction == Ghost.DIRECTION_LEFT:
            surface.blit(self.my_image, self.get_collision_box())

        if self.facing_direction == Ghost.DIRECTION_DOWN:
            #down_surf = pygame.transform.flip(self.driving_images[self.animation_frame], False, True)
            #surface.blit(down_surf, (self.x - 100, self.y - 100))

            surface.blit(self.my_image, self.get_collision_box())

        if self.facing_direction == Ghost.DIRECTION_UP:
            #up_surf = pygame.transform.flip(self.driving_images[self.animation_frame], True, False)
            #surface.blit(up_surf, (self.x - 100, self.y - 100))

            surface.blit(self.my_image, self.get_collision_box())


    def get_collision_box(self):
        r = pygame.Rect(self.x-self.width/2, self.y - self.height, self.width, self.height)
        return r

    def step(self, delta_T):
        """
        In order to change over time, this method gets called very often. The delta_T variable is the amount of time it
        has been since the last time we called "step()" usually about 1/20 -1/60 of a second.
        :param delta_T:
        :return: None
        """
        if self.facing_direction == Ghost.DIRECTION_UP:
            self.vx = 0
            self.vy = -100

        if self.facing_direction == Ghost.DIRECTION_DOWN:
            self.vx = 0
            self.vy = 100

        if self.facing_direction == Ghost.DIRECTION_RIGHT:
            self.vx = 100
            self.vy = 0

        if self.facing_direction == Ghost.DIRECTION_LEFT:
            self.vx = -100
            self.vy = 0

        self.x = self.x + self.vx * delta_T
        self.y = self.y + self.vy * delta_T


    def is_dead(self):
        """
        lets another object know whether this object is still live and on the board. Used by the main loop to clear objects
        in need of removal.
        :return: True or False - is this object dead?
        """
        if self.i_am_alive:
            return False
        else:
            return True
        # alternative (1-line) version of this function:
        #  "return not self.i_am_alive"


    def die(self):
        """
        change the status of this object so that it is dead.
        :return: None
        """
        self.i_am_alive = False