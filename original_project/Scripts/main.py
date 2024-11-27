import numpy as np
from PIL import ImageGrab
import cv2
import time
from draw_lanes import draw_lanes
from check_lane_departure import check_lane_departure

def roi(img, vertices):
    
    #blank mask:
    mask = np.zeros_like(img)   
    
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, 255)
    
    #returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked



def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    
    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
    
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)

    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                                     rho   theta   thresh  min length, max gap:        
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,      20,       15)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1,m2 = draw_lanes(original_image,lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        print(str(e))
        pass
    
    return processed_img,original_image, m1, m2, l1, l2



def main():
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen,original_image, m1, m2, l1, l2 = process_img(screen)
        #cv2.imshow('window', new_screen)
        img_width = original_image.shape[1]

        warning_text, color = check_lane_departure(l1, l2, img_width)
        cv2.putText(original_image, warning_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)


        cv2.imshow('Lane Departure Warning System', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()

