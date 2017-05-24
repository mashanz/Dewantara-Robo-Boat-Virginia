#!/usr/bin/python3

from multiprocessing import Process, Pipe
from lib_detect import detect_shape, looper
from lib_motor import motor_input
from lib_area import area
import cv2
########################################################################################################################
#  .: = WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING = :.   #
#        these program require minimal 2 core processor that support pipeline minimal 2 process pipe line core         #
#                                                                                                                      #
#                    Main Program Set every function as different process to speed up processing                       #
########################################################################################################################

def test(conn):
    while(1):
        cv2.imshow('framez',conn)

if __name__ == '__main__':
    bentuk = "segitiga"

    parent_conn, child_conn = Pipe()
    cam_parent, cam_child = Pipe()
    deparent, dechild = Pipe()

    # Prepare for fatching routine
    p0 = Process(target=detect_shape, args=(child_conn, cam_child))
    p1 = Process(target=motor_input, args=(parent_conn, dechild, bentuk))
    p3 = Process(target=looper, args=(deparent,))
    p4 = Process(target=area, args=(cam_parent,))

    # Start routine
    p0.start()
    p1.start()
    p3.start()
    p4.start()

    # Join every routine that running
    p0.join()
    p1.join()
    p3.join()
    p4.join()


