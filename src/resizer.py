
import os
import cv2
def resizer_fun(location,w,h):
    l =location
    w = w
    h = h
    print(w,h)
    for filename in os.listdir(l):
        img = cv2.imread(os.path.join(l,filename))
        # print(img)
    # for root, directories, files in os.walk(l, topdown=False):
    #     # for name in files:
    #     print(root)
            # path = os.path.join(root, name)
        rez = cv2.resize(img,(w,h),interpolation=cv2.INTER_AREA)
        #writing the resized image
        n = filename + ".jpg"
        cv2.imwrite(filename,rez) 
        #loading the resized image and seeing the height & width
        # resized = cv2.imread("resized_image.jpg")  
        # (height,width) = resized.shape[:2]
        # print ("Resized Height & Width  ---> \n Height : {} Width : {}".format(height,width))
    
