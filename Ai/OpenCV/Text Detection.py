import cv2
import pytesseract


img = cv2.imread('1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))

# ##### Dectating Characters #####
# height,width,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     print(b)
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])   # converting coordinates into list
#     cv2.rectangle(img,(x,height-y),(w,height-h),(0,0,255),1)   # bounding boxes over text
#     cv2.putText(img,b[0],(x,height-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)

# ##### Dectating Words #####
# height,width,_ = img.shape
# boxes = pytesseract.image_to_data(img)
# #print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     if x != 0:
#         b = b.split()
#         print(b)
#         if len(b) == 12:
#             x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])   # converting coordinates into list
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)   # bounding boxes over text
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)

##### Dectating number #####
height,width,_ = img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img,config = cong)
#print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])   # converting coordinates into list
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)   # bounding boxes over text
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)



cv2.imshow('Result',img)
cv2.waitKey(0)
