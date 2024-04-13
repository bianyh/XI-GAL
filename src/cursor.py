# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:10:02 2024

@author: 11494
"""

import cv2 as cv
import win32api
import win32con

import button


def mouse_evt(event: object, x: int, y: int, flags: object, param: object) -> None:
    # Mouse is Moving
    win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))
    if event == cv.EVENT_MOUSEMOVE:
       inspect_text_loction(x,y, param[0])
    if event == cv.EVENT_LBUTTONDOWN or event == cv.EVENT_LBUTTONDBLCLK:
        click_color_noexe(x, y, param[0])
    elif event == cv.EVENT_LBUTTONUP:
        click_color_exe(x, y, param[0])

def inspect_text_loction(x: int, y: int, window: button.Text) -> None:
    """

    :param x: 检测坐标x
    :param y: 检测坐标y
    :param window: 所检测的窗口
    """
    panduan = 0
    for i in window.Button:
        #print(i.is_hover(x, y))
        if i.is_hover(x, y):
            i.flush_color((125, 125, 125))
            panduan = 1
            win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_HAND))
        else:
            i.re_color((0, 0, 0))
        if panduan ==0:
            win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))

def click_color_noexe(x: int, y: int, window: button.Text) -> None:
    """

    :param x: 检测坐标x
    :param y: 检测坐标y
    :param window: 所检测的窗口
    """
    for i in window.Button:
        if i.is_hover(x,y):
            i.click_color_alter((255,0,0))
            break

def click_color_exe(x: int, y: int, window: button.Text) -> None:
    """

    :param x: 检测坐标x
    :param y: 检测坐标y
    :param window: 所检测的窗口
    """
    for i in window.Button:
        if i.is_hover(x,y):
            i.click_color_exe((0,0,255))
            break

    