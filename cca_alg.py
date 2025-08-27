from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import grayscale

label_image = measure.label(grayscale.binary_car_image) # labels each connected component
fig, (ax1) = plt.subplots(1)
ax1.imshow(grayscale.gray_car_image, cmap = "gray")

for region in regionprops(label_image):
    if region.area < 50: # the "iterator" thingy is a connected region from the regions we got earlier, if the number of pixels of the
        continue         # said area has less than 50 pixels, most likely noise/too small, so skip

    minRow, minCol, maxRow, maxCol = region.bbox # this is another property of the selected region, basically the bounding box
    rectBorder = patches.Rectangle((minCol, minRow), maxCol - minCol, maxRow - minRow, edgecolor = "red", linewidth = 2, fill = False)
    # creates rectangle with said proportions
    ax1.add_patch(rectBorder) # overlays the rectangle on top of the graph we drew earlier

plt.show()
