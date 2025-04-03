import imageio.v3 as io
#importing image io library for image reading and writing as is alias

filenames=["flowers-animation_WPS Photos/flowers-animation_WPS Photos_1.png","flowers-animation_WPS Photos/flowers-animation_WPS Photos_2.png"]#list of images
image=[] #empty list to be used later
for filename in filenames:
    image.append(io.imread(filename))#usinf for loop for reading image data into image list using imread method

io.imwrite("flowers.gif",image,duration=500,loop=0)


