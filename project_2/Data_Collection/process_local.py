import cv2
def process_image():
	image = cv2.imread('IMG_1382.jpg', 0)
	resized_image = cv2.resize(image, (224,224))
	cv2.imwrite('IMG_1382_edited.jpg', resized_image)
	return

# Just prints 'Hello World! to screen.
#def hello_world():
#    print('Hello World!')
#    return

# TODO: Call process_image function.
def main():
#    hello_world()
	process_image()
    	return


if(__name__ == '__main__'):
    main()
