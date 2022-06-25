import sys
import random
import pygame as pg
import config as cf


class CloseButton(pg.sprite.Sprite):
    """Button to X out"""
    def __init__(self, groups):
        super().__init__(groups)
        self.image = cf.load_image(cf.CLOSE_BTN)
        self.image = pg.transform.smoothscale(self.image, (50, 50))
        test = pg.transform.get_smoothscale_backend()
        self.rect = self.image.get_rect()
        self.rect.topleft = (cf.SCREEN_RECT.right-self.rect.w, 0)


def handle_particles(all_ptcl):
    for particle in all_ptcl:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        pg.draw.circle(cf.SCREEN,
                       particle[3],
                       (int(particle[0][0]), int(particle[0][1])),
                       int(particle[2]))
        if particle[2] <= 0:
            all_ptcl.remove(particle)


def spawn_colors(num_part, part_list, pos, col):
    for _ in range(num_part):
        x_pos = cf.SCREEN_NINTH*pos-(cf.SCREEN_NINTH/2) + random.randint(-40, 40)
        y_pos = cf.SCREEN_RECT.h-15
        x_vel = random.randint(0, 20)/10 - 1
        y_vel = -random.randint(2, 7)
        size = random.randint(4, 20)

        part_list.append([[x_pos, y_pos],
                          [x_vel, y_vel],
                          size,
                          col])


def main():

    everything = pg.sprite.RenderPlain()
    buttons = pg.sprite.RenderPlain()

    background = pg.Surface(cf.SCREEN.get_size()).convert()
    close_btn = CloseButton((buttons))
    background.fill(cf.BLACK)

    particles = []

    locked = True
    while locked:
        cf.CLOCK.tick(60)
        mouse_pos = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_LSHIFT
                   or event.key == pg.K_LESS
                   or event.key == pg.K_LCTRL
                   or event.key == pg.K_CAPSLOCK
                   or event.key == pg.K_a
                   or event.key == pg.K_TAB
                   or event.key == pg.K_q
                   or event.key == 124
                   or event.key == pg.K_1
                   or event.key == pg.K_F1
                   or event.key == pg.K_ESCAPE):
                    spawn_colors(20, particles, 1, cf.COL_1)
                if (event.key == pg.K_z
                   or event.key == pg.K_x
                   or event.key == pg.K_LMETA
                   or event.key == pg.K_LALT
                   or event.key == pg.K_s
                   or event.key == pg.K_d
                   or event.key == pg.K_w
                   or event.key == pg.K_e
                   or event.key == pg.K_2
                   or event.key == pg.K_3
                   or event.key == pg.K_F2
                   or event.key == pg.K_F3):
                    spawn_colors(20, particles, 2, cf.COL_2)
                if (event.key == pg.K_c
                   or event.key == pg.K_v
                   or event.key == pg.K_f
                   or event.key == pg.K_g
                   or event.key == pg.K_r
                   or event.key == pg.K_t
                   or event.key == pg.K_4
                   or event.key == pg.K_5
                   or event.key == pg.K_F4
                   or event.key == pg.K_F5
                   or event.key == pg.K_F6):
                   spawn_colors(20, particles, 3, cf.COL_3)
                if (event.key == pg.K_b
                   or event.key == pg.K_n
                   or event.key == pg.K_h
                   or event.key == pg.K_j
                   or event.key == pg.K_y
                   or event.key == pg.K_u
                   or event.key == pg.K_6
                   or event.key == pg.K_7
                   or event.key == pg.K_F7
                   or event.key == pg.K_F8):
                   spawn_colors(20, particles, 4, cf.COL_4)
                if (event.key == pg.K_m
                   or event.key == pg.K_COMMA
                   or event.key == pg.K_RALT
                   or event.key == pg.K_k
                   or event.key == pg.K_l
                   or event.key == pg.K_i
                   or event.key == pg.K_o
                   or event.key == pg.K_8
                   or event.key == pg.K_9
                   or event.key == pg.K_F9
                   or event.key == pg.K_F10):
                   spawn_colors(20, particles, 5, cf.COL_5)
                if (event.key == pg.K_PERIOD
                   or event.key == pg.K_MINUS
                   or event.key == pg.K_MENU
                   or event.key == pg.K_RCTRL
                   or event.key == 248
                   or event.key == 230
                   or event.key == pg.K_p
                   or event.key == 229
                   or event.key == pg.K_0
                   or event.key == pg.K_PLUS
                   or event.key == pg.K_F11
                   or event.key == pg.K_F12):
                   spawn_colors(20, particles, 6, cf.COL_6)
                if (event.key == pg.K_RSHIFT
                   or event.key == pg.K_UP
                   or event.key == pg.K_LEFT
                   or event.key == pg.K_DOWN
                   or event.key == pg.K_QUOTE
                   or event.key == pg.K_RETURN
                   or event.key == 1073741824
                   or event.key == pg.K_BACKSLASH
                   or event.key == pg.K_BACKSPACE
                   or event.key == pg.K_INSERT
                   or event.key == pg.K_DELETE):
                   spawn_colors(20, particles, 7, cf.COL_7)
                if (event.key == pg.K_KP1
                   or event.key == pg.K_KP2
                   or event.key == pg.K_RIGHT
                   or event.key == pg.K_KP0
                   or event.key == pg.K_KP4
                   or event.key == pg.K_KP5
                   or event.key == pg.K_KP7
                   or event.key == pg.K_KP8
                   or event.key == pg.K_NUMLOCK
                   or event.key == pg.K_KP_DIVIDE
                   or event.key == pg.K_HOME
                   or event.key == pg.K_END):
                   spawn_colors(20, particles, 8, cf.COL_8)
                if (event.key == pg.K_KP3
                   or event.key == pg.K_KP_ENTER
                   or event.key == pg.K_KP_PERIOD
                   or event.key == pg.K_KP6
                   or event.key == pg.K_KP_PLUS
                   or event.key == pg.K_KP9
                   or event.key == pg.K_KP_MULTIPLY
                   or event.key == pg.K_KP_MINUS
                   or event.key == pg.K_PAGEUP
                   or event.key == pg.K_PAGEDOWN):
                   spawn_colors(20, particles, 9, cf.COL_9)

            if event.type == pg.MOUSEBUTTONDOWN and close_btn.rect.collidepoint(mouse_pos):
                locked = False

        cf.SCREEN.blit(background, (0, 0))
        everything.draw(cf.SCREEN)
        if close_btn.rect.collidepoint(mouse_pos):
            buttons.draw(cf.SCREEN)
        handle_particles(particles)
        pg.display.flip()

if __name__ == "__main__":
    main()
