import PIL as pil
import math

_MAGNITUDE = 10

def find_approximate(pixel, pallette_list):
    #don't change the alphas
    if(pixel[3] <= 0):
        return pixel

    #current (ineffective) method: compute the sum and see which is less diff
    pixel_sum = pixel[0]**_MAGNITUDE + pixel[1]**_MAGNITUDE + pixel[2]**_MAGNITUDE
    pallette_pixel_sum = {}
    for color in pallette_list:
        i_sum = math.fabs(color[0]**_MAGNITUDE + color[1]**_MAGNITUDE + color[2]**_MAGNITUDE - pixel_sum)
        pallette_pixel_sum[i_sum] = color

    npixel = pallette_pixel_sum[min(pallette_pixel_sum.keys())]
    return npixel
