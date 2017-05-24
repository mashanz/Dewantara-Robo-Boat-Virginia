import cv2
import numpy as np
import imutils
from lib_motor import motor_input

def track_color(thresh, erosi, dilatasi):
    kernelA = np.ones((erosi, erosi), np.uint8)
    kernelB = np.ones((dilatasi, dilatasi), np.uint8)
    img_erodila = cv2.erode(thresh, kernelA, iterations=1)
    img_erodila = cv2.erode(img_erodila, kernelA, iterations=1)
    img_erodila = cv2.dilate(img_erodila, kernelB, iterations=1)
    img_erodila = cv2.dilate(img_erodila, kernelB, iterations=1)
    cv2.imshow('mask', img_erodila)
    refArea = 10.
    for c in img_erodila:
        M = cv2.moments(img_erodila)
        if (M['m00']>refArea):
            x = M['m10']/M['m00']
            y = M['m01']/M['m00']
            motor_input(int(x), int(y))


def biru(erosi,dilatasi,cap):
    while(1):
        # Take each frame
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)                  # Tracking warna
        # print(mask)
        # Bitwise-AND mask and original image
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # print(hsv)
        # cv2.imshow('frame',frame)
        cv2.imshow('mask0',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def hijau(erosi,dilatasi,cap):
    while(1):
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([50,50,50])
        upper_blue = np.array([70,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def merah(erosi,dilatasi,cap):
    while(1):
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0,50,50])
        upper_blue = np.array([10,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def kuning(erosi,dilatasi,cap):
    while(1):
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([20,50,50])
        upper_blue = np.array([40,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def pink(erosi,dilatasi,cap):
    while(1):
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([140,50,50])
        upper_blue = np.array([160,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def cyan(erosi,dilatasi,cap):
    while(1):
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([80,50,50])
        upper_blue = np.array([100,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


def white(erosi,dilatasi,cap):
    while(1):
        _, frame = cap.read()
        frame = imutils.resize(frame, width=320)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([0,0,0])
        upper_blue = np.array([0,0,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        track_color(mask, erosi, dilatasi)
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        # cv2.imshow('frame',frame)
        # cv2.imshow('mask',mask)
        # cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

def cari_warna(cap,warna):
    if(warna=="biru"):
        biru(7,5,cap)
        cv2.destroyAllWindows()
    elif(warna=="hijau"):
        hijau(2,8,cap)
        cv2.destroyAllWindows()
    elif (warna == "merah"):
        merah(2,5,cap)
        cv2.destroyAllWindows()
    elif (warna == "kuning"):
        kuning(4,5,cap)
        cv2.destroyAllWindows()
    elif (warna == "ungu"):
        pink(1,2,cap)
        cv2.destroyAllWindows()
    elif (warna == "cyan"):
        cyan(1,2,cap)
        cv2.destroyAllWindows()
    elif (warna == "putih"):
        white(1,2,cap)
        cv2.destroyAllWindows()
    else:
        print("")

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    cari_warna(cap, "biru")

    """
    red = np.uint8([[[0, 0, 255]]])
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    print(hsv_red)

    green = np.uint8([[[0, 255, 0]]])
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    print(hsv_green)

    blue = np.uint8([[[255, 0, 0]]])
    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    print(hsv_blue)

    yellow = np.uint8([[[0, 255, 255]]])
    hsv_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
    print(hsv_yellow)

    pink = np.uint8([[[255, 0, 255]]])
    hsv_pink = cv2.cvtColor(pink, cv2.COLOR_BGR2HSV)
    print(hsv_pink)

    cyan = np.uint8([[[255, 255, 0]]])
    hsv_cyan = cv2.cvtColor(cyan, cv2.COLOR_BGR2HSV)
    print(hsv_cyan)

    white = np.uint8([[[255, 255, 255]]])
    hsv_white = cv2.cvtColor(white, cv2.COLOR_BGR2HSV)
    print(hsv_white)
    while(1):
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    """




