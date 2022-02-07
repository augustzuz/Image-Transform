import numpy as np
from PIL import Image

img = Image.open("cat.png")
#img.show()

I = np.array(img)

alpha = 2
I *= 2

I[I > 255] = 295

Image.fromarray(I).show()
