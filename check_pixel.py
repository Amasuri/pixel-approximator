import PIL as pil
import math

#do play with the value! some files are good at 1, some at 5..
_MAGNITUDE = 1

def find_approximate(pixel, pallette_list):
    #don't change the alphas
    if(pixel[3] <= 0):
        return pixel

    #current method: compute the sum and see which is less diff
    pallette_pixel_sum = {}
    for color in pallette_list:
        r_sum = math.fabs(color[0] ** _MAGNITUDE - pixel[0] ** _MAGNITUDE)
        g_sum = math.fabs(color[1] ** _MAGNITUDE - pixel[1] ** _MAGNITUDE)
        b_sum = math.fabs(color[2] ** _MAGNITUDE - pixel[2] ** _MAGNITUDE)

        i_sum = r_sum + g_sum + b_sum
        pallette_pixel_sum[i_sum] = (color[0], color[1], color[2], pixel[3])

    npixel = pallette_pixel_sum[min(pallette_pixel_sum.keys())]
    return npixel
