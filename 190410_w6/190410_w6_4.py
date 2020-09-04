import imageio
img = imageio.imread('carry_grant.jpg')

size = img.shape
print(size)

pixel = img[77][100]
print(pixel)