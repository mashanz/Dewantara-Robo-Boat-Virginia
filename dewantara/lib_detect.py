import cv2
import imutils
from lib_motor import motor_input
outlist = [0, 0, 0, 0, "", ""]

########################################################################################################################
# Deteksi Bentuk
########################################################################################################################


def detect_shape(conn,conn1):
    camera = cv2.VideoCapture(0)
    while True:
        (grabbed, frames) = camera.read()
        frame = imutils.resize(frames, width=640)
        if not grabbed:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0) #(7,7)
        edged = cv2.Canny(blurred, 50, 2000, apertureSize=5) #10 ,250
        im2, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #cam_conn.send(frame)
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.01 * peri, True) #0.01
            if len(approx) >= 3 and len(approx) <= 15:
                (x, y, w, h) = cv2.boundingRect(approx)
                aspectRatio = w / float(h)
                area = cv2.contourArea(c)
                hullArea = cv2.contourArea(cv2.convexHull(c))
                solidity = area / float(hullArea)
                keepDims = w > 25 and h > 25
                keepSolidity = solidity > 0.25 # 0.5
                keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 2.2
                if keepDims and keepSolidity and keepAspectRatio:
                    shape = len(approx)
                    color = "none"
                    if (shape >= 3 and shape <=3 ):
                        outlist = [x, y, w, h, "segitiga", color]
                        conn.send(outlist)
                        conn1.send(outlist)
                        #motor_input(int(x), int(y))
                    elif (shape == 12):
                        outlist = [x, y, w, h, "cross", color]
                        conn.send(outlist)
                        conn1.send(outlist)
                    elif (shape >= 13 ):
                        outlist = [x, y, w, h, "lingkaran", color]
                        conn.send(outlist)
                        conn1.send(outlist)
                    else:
                        continue
                    cv2.drawContours(frame, [approx], -1, (0, 255, 0), 1)
                    M = cv2.moments(approx)
                    (cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    (startX, endX) = (int(cX - (w * 0.2)), int(cX + (w * 0.2)))
                    (startY, endY) = (int(cY - (h * 0.2)), int(cY + (h * 0.2)))
                    cv2.line(frame, (startX, cY), (endX, cY), (255, 0, 0), 3)
                    cv2.line(frame, (cX, startY), (cX, endY), (255, 0, 0), 3)
        #cv2.imshow("Frame1", im2)
        #cv2.imshow("Frame2", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    camera.release()
    cv2.destroyAllWindows()

########################################################################################################################
# Deteksi Warna Pada Bentuk
########################################################################################################################


def detect_color(connr, connt):
    while(1):
        outlist = connr.recv()
        if outlist.__getitem__(4)=="segitiga":
            connt.send()
        elif outlist.__getitem__(4)=="cross":
            connt.send()
        elif outlist.__getitem__(4)=="lingkaran":
            connt.send()
        else:
            connt.send()

########################################################################################################################
# Test pipeline connection
########################################################################################################################


def looper(conn):
    while(1):
        outlist = conn.recv()
        print(outlist.__getitem__(0), outlist.__getitem__(1), # x,y
              outlist.__getitem__(2), outlist.__getitem__(3), # w, h
              outlist.__getitem__(4), outlist.__getitem__(5)) # shape, color
