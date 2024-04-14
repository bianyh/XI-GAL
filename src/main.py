# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:57:49 2024

@author: 11494
"""

import cv2 as cv
import numpy as np
import cursor
import button
import runningevent

if __name__ == '__main__':
    # 创建一个白色背景的窗口
    window_name = 'Xi Gal'
    cv.namedWindow(window_name)
    # 将OpenCV图像转换为PIL图像
    image = cv.imread('..//img//2.jpg', 1)
    kernel = np.array([[0,-1,0],[-1,6,-1],[0,-1,0]])#创建滤波器
    image = cv.filter2D(image, -1, kernel)  #卷积
    down_width = 500
    size = image.shape
    w = size[1]  # 宽度
    h = size[0]  # 高度
    down_height = 500#int(h * 500 / w)
    down_points = (down_width, down_height)
    image = cv.resize(image, down_points, interpolation=cv.INTER_LINEAR)

    # 设置字体和大小
    font_path = "..//font//simsun.ttf"  # 这里需要指定一个包含中文字符的字体文件路径
    font_size = 20
    
    # 在图像上绘制中文文本
    draw = button.Text(image)
    button.Text_Button(draw, 'xigal，启动！', (0, 0, 0), (50, 50), 30)
    button.Text_Button(draw, '教程 The Question', (0, 0, 0), (50, 100), 30)
    button.Text_Button(draw, '+ 创建新项目', (0, 0, 0), (50, 150), 30)
    button.Text_Button(draw, '打开目录', (0, 0, 0), (50, 200), 30)
    button.Text_Button(draw, '操作', (0, 0, 0), (50, 250), 30, click_operation=draw.print_all_Button_position)
    button.long_text(draw, '生成audsiohdasfuhhhhhfffffffffffffffffffffffffffffff', (0, 0, 0), (50, 300), 30)
    button.Text_Button(draw, '更换图片', (0, 0, 0), (50, 350), 30, click_operation=draw.alter_the_image)
    button.Text_Button(draw, '退出', (0, 0, 0), (50, 400), 30, click_operation=runningevent.Forced_exit)


    while True:
        image = draw.draw_all()

        #down_points = (400,500)
        #background = cv.resize(background, down_points, interpolation= cv.INTER_LINEAR)
        #指定鼠标光标样式
        cv.setMouseCallback(window_name, cursor.mouse_evt,[draw])
        # 显示窗口
        cv.imshow(window_name, image)
        cv.waitKey(1)
        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

