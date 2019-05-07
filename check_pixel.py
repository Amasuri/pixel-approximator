import PIL as pil
import math

#do play with the value! some files are good at 1, some at 5..
_MAGNITUDE = 1

def find_approximate(pixel):
    """Return a pixel from the pallette that is the closest to the specified one."""
    #don't change the alphas
    if(pixel[3] <= 0):
        return pixel

    #current method: compute the sum and see which is less diff
    pallette_pixel_sum = {}
    for color in _COMPILED_PALETTE.keys():
        r_sum = math.fabs(_COMPILED_PALETTE[color][0] - pixel[0] ** _MAGNITUDE)
        g_sum = math.fabs(_COMPILED_PALETTE[color][1] - pixel[1] ** _MAGNITUDE)
        b_sum = math.fabs(_COMPILED_PALETTE[color][2] - pixel[2] ** _MAGNITUDE)

        i_sum = r_sum + g_sum + b_sum
        pallette_pixel_sum[i_sum] = (color[0], color[1], color[2], pixel[3])

    npixel = pallette_pixel_sum[min(pallette_pixel_sum.keys())]
    return npixel

def compile_palette(palette_list):
    """Set the numeric values ready so they won't be calculated at each call."""
    global _COMPILED_PALETTE
    _COMPILED_PALETTE = {}

    for color in palette_list:
        r_sum = math.fabs(color[0] ** _MAGNITUDE)
        g_sum = math.fabs(color[1] ** _MAGNITUDE)
        b_sum = math.fabs(color[2] ** _MAGNITUDE)

        _COMPILED_PALETTE[color] = [r_sum, g_sum, b_sum]
