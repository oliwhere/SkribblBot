import ctypes
from time import sleep

brush = 3
canvas = (483, 217), (814, 610)
MODE = 1

if MODE == 1:
    def draw(img):
        click(1034, 860)
        for current_color in colors:
            if current_color == (255, 255, 255):
                continue
            change_color(current_color)
            for y, ly in enumerate(img):
                last_color = None
                for x, pixel_color in enumerate(ly):
                    pos = (x*brush+brush/2+canvas[0][0],
                           y*brush+brush/2+canvas[0][1])

                    if pixel_color == current_color:
                        if last_color != pixel_color:
                            ctypes.windll.user32.mouse_event(1 + 0x8000,
                                int(65535 * pos[0] / ctypes.windll.user32.GetSystemMetrics(0) + 1),
                                int(65535 * pos[1] / ctypes.windll.user32.GetSystemMetrics(1) + 1), 0, 0)
                            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
                        elif last_color == pixel_color:
                            ctypes.windll.user32.mouse_event(1 + 0x8000,
                                int(65535 * pos[0] / ctypes.windll.user32.GetSystemMetrics(0) + 1),
                                int(65535 * pos[1] / ctypes.windll.user32.GetSystemMetrics(1) + 1), 0, 0)
                    elif last_color == current_color:
                        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
                        sleep(.005)
                    last_color = pixel_color
                ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
elif MODE == 0:
    def draw(img):
        click(1034, 860)
        for y, ly in enumerate(img):
            for x, pixel_color in enumerate(ly):
                if pixel_color == (255, 255, 255):
                    continue
                change_color(pixel_color)
                click(x * brush + brush / 2 + canvas[0][0],
                      y * brush + brush / 2 + canvas[0][1])
                sleep(.005)


def change_color(color):
    i = colors.index(color)
    if i <= 10:
        x = i*24 + 580
        y = 840
    else:
        x = (i-11)*24 + 580
        y = 860
    click(x, y)

def cahnge_brushsize(size):
    pass

def click(x, y, t=.005):
    ctypes.windll.user32.mouse_event(1 + 0x8000,
        int(65535 * x / ctypes.windll.user32.GetSystemMetrics(0) + 1),
        int(65535 * y / ctypes.windll.user32.GetSystemMetrics(1) + 1), 0, 0)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
    sleep(t)


colors = ((255, 255, 255), (193, 193, 193), (239, 19, 11),
          (255, 113, 0), (255, 228, 0), (0, 204, 0),
          (0, 178, 255), (35, 31, 211), (163, 0, 186),
          (211, 124, 170), (160, 82, 42),
          (0, 0, 0), (76, 76, 76), (116, 11, 7),
          (194, 56, 0), (232, 162, 0), (0, 85, 16),
          (0, 86, 158), (14, 8, 101), (85, 0, 105),
          (167, 85, 116), (99, 48, 13))
