from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import grayscale

label_image = measure.label(grayscale.binary_car_image) # labels each connected component

# defines the min and max dimensions that the plate can be based on the images size
plate_dimesions = (0.08*label_image.shape[0], 0.2*label_image.shape[0], 0.15*label_image.shape[1], 0.4*label_image.shape[1])
min_height, max_height, min_width, max_width = plate_dimesions
plate_objects_cordinates = [] # list to keep the box coordinates of the filtered objects
plate_like_objects = [] # binary image of just the filtered objects

fig, (ax1) = plt.subplots(1)
ax1.imshow(grayscale.gray_car_image, cmap = "gray")
for region in regionprops(label_image):
    if region.area < 50: # the "iterator" thingy is a connected region from the regions we got earlier, if the number of pixels of the
        continue         # said area has less than 50 pixels, most likely noise/too small, so skip

    minRow, minCol, maxRow, maxCol = region.bbox # this is another property of the selected region, basically the bounding box
    regionHeight = maxRow - minRow
    regionWidth = maxCol - minCol
    # does the filtering
    if regionHeight >= min_height and regionHeight <= max_height and regionWidth >= min_width and regionWidth <= max_width and regionHeight < regionWidth:
        plate_like_objects.append(grayscale.binary_car_image[minRow:maxRow, minCol:maxCol])
        plate_objects_cordinates.append((minRow, minCol, maxRow, maxCol))
        rectBorder = patches.Rectangle((minCol, minRow), maxCol - minCol, maxRow - minRow, edgecolor = "red", linewidth = 2, fill = False)
        # draws rectangle
        ax1.add_patch(rectBorder) # overlays the rectangle on top of the graph we drew earlier

plt.show()
