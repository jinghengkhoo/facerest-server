import cv2


image_path = "1093687.jpg"
original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)

input_height, input_width, _ = original_image.shape

new_h = int( 32 * round( input_height / 32. ))
new_w = int( 32 * round( input_width / 32. ))

img = cv2.resize(original_image, (new_w, new_h), interpolation= cv2.INTER_LINEAR)

print(img.shape)

cv2.imwrite("scale.png", img)