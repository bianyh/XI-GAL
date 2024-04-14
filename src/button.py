# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:17:17 2024

@author: 11494
"""


from PIL import Image, ImageDraw, ImageFont
import freetype
import copy
import cv2 as cv
import numpy as np
import runningevent
class Text_Button:
    pass


class Text:
    #window是需要加文本的窗口，应当是一个PIL图片
    #color为文本的颜色
    #x,y分别为所加入的文本框的位置
    #width和height分别为所加入文本框的宽度与高度
    #font指定使用的文本字体的路径，默认为simsun.ttc
    def __init__(self, window):
        self.window = window
        self.yuan_window = copy.deepcopy(window)
        self.Button = []
        self.long = []
        self.Button_need_flush = []
        self.img_nums = 2
        img_path = './/test_img//text_box.png'
        self.text_box = cv.imread(img_path, 1)
        down_points = (int(self.window.shape[1] * 0.9), int(self.window.shape[0] * 0.3))
        self.text_box = cv.resize(self.text_box, down_points, interpolation=cv.INTER_LINEAR)

    def add(self, button: Text_Button) -> None:
        if type(button) == Text_Button:
            self.Button.append(button)
        elif type(button) == long_text:
            self.long.append(button)

    def add_need_flush(self, button: Text_Button) -> None:
        self.Button_need_flush.append(button)

    def draw_all(self):
        self.window = copy.deepcopy(self.yuan_window)
        self.Text_box()
        for button in self.Button:
            button.draw(self.window)
        for button in self.long:
            button.delay_draw(self.window, speed=1)

        return self.window
    #def draw_flush(self):
    def alter_the_image(self) -> None:
        self.img_nums = self.img_nums + 1
        img_path = '..//text_img//' + str(self.img_nums) + '.jpg'
        self.yuan_window = copy.deepcopy(cv.imread(img_path, 1))
        kernel = np.array([[0, -1, 0], [-1, 6, -1], [0, -1, 0]])  # 创建滤波器
        self.yuan_window = cv.filter2D(self.yuan_window, -1, kernel)  # 卷积
        down_points = (1200, 700)
        self.yuan_window = cv.resize(self.yuan_window, down_points, interpolation=cv.INTER_LINEAR)


    def print_all_Button_position(self):
        for button in self.Button:
            if type(button) == Text_Button:
                print(button.position + button.size)
                print(button.is_hover(1,1))

    def long_text_draw_complete(self):
        print('sadui')
        for button in self.long:
            button.count_text = len(button.text)
            button.now_char = button.text

    def Text_box(self):
        size = self.window.shape
        top_left = (int(size[1] * 0.05), int(size[0] * 0.7))
        alpha = 0.2  # Transparency factor.
        self.window = runningevent.addWeightedSmallImgToLargeImg(self.window, alpha, self.text_box, 1 - alpha, 0, regionTopLeftPos=top_left)
        # cv.rectangle(self.window, top_left, bottom_right, self.text_box_color, -1)

class Text_Button:
    def __init__(self, Textwindow: Text, text: str = '你好, XI GAL', color = (0,0,0), position = (0,0),
                 height: int = 30 , font_path: str = "..//font//simsun.ttf", click_operation: object = None ) -> None:
        """

        :param Textwindow: 需要写入按钮的窗口Text类
        :param text: 需要写入的文本
        :param color: 文本颜色
        :param position: 写入的位置
        :param height: 写入文本的高度
        :param font_path: 写入文本的字体路径
        :param click_operation: 当点击这个按钮时的触发函数
        """
        self.click_operation = click_operation
        self.Textwindow = Textwindow
        self.window = Textwindow.window
        self.text = text
        self.color = color
        self.position = position
        self.height = height
        self.font_path = font_path
        self.font = ImageFont.truetype(self.font_path, int(self.height * 0.8))
        self.ft = PutChineseText(self.font_path,text_size=self.height)
        self.Textwindow.add(self)
        self.draw(self.window)

    def draw(self, window=None) -> None:
        #position渴求一个元组，以代表文本镶嵌的起始位置
        if window is None:
            window = self.window
        # 加载字体文件
        # 计算文本大小
        #_,_, text_width, text_height = font.getbbox(self.text)
        #_,_,self.text_right, self.text_bottom = draw.textbbox(self.position, self.text, font=self.font)
        self.size = self.ft.get_text_size(self.text)
        # 在指定位置绘制文本
        window = self.ft.draw_text(window, self.position, self.text, self.color)
        return window

    def is_hover(self, mouse_x, mouse_y):
        # 检查鼠标坐标是否在文本框内

        x = self.position[0]
        y = self.position[1]
        # print(x <= mouse_x <= x + self.size[0] and
        #         y <= mouse_y <= y + self.size[1])
        return (x <= mouse_x <= x + self.size[0] and
                y <= mouse_y <= y + self.size[1])


    def flush_color(self, new_color):
        #当鼠标悬停在文本上面的时候刷新文本的颜色
        self.color = new_color
        self.draw()

    def re_color(self, re_color):
        #当鼠标移开时文本颜色归回
        self.color = re_color
        self.draw()

    def click_color_alter(self,new_color):
        #当鼠标悬停的时候的文本变色
        self.color = new_color
        self.draw()
    def click_color_exe(self, new_color: ()) -> None:
        #当鼠标点击up时的变色与执行对应函数
        if self.click_operation:
         self.click_operation()
        self.color = new_color
        self.draw()
#文本型按钮类，给屏幕上增加一个指定大小的可交互文本按钮

class long_text(Text_Button):
    def __init__(self, Textwindow: Text, text: str = '你好, XI GAL', color = (0,0,0), position = (0,0),
                 height: int = 30 , font_path: str = "..//font//simsun.ttf", click_operation: object = None ) -> None:
        """

                :param Textwindow: 需要写入按钮的窗口Text类
                :param text: 需要写入的文本
                :param color: 文本颜色
                :param position: 写入的位置
                :param height: 写入文本的高度
                :param font_path: 写入文本的字体路径
                :param click_operation: 当点击这个按钮时的触发函数
                """
        self.click_operation = click_operation
        self.Textwindow = Textwindow
        self.window = Textwindow.window
        self.text = text
        self.color = color
        self.position = position
        self.height = height
        self.font_path = font_path
        self.font = ImageFont.truetype(self.font_path, int(self.height * 0.8))
        self.ft = PutChineseText(self.font_path, text_size=self.height)
        self.count_text = 0
        self.maxsize = self.window.shape
        (self.max_width, self.max_height) = int(self.maxsize[1] * 0.9), int(self.maxsize[0] * 0.9)
        self.space_width, self.line_height = self.ft.get_text_size('汐')  # 空格宽度和行高
        self.Textwindow.add(self)
        self.delay_draw(self.window)

    def draw(self, window=None) -> None:
        if window is None:
            window = self.window
        #self.size = self.ft.get_text_size(self.text)#长文本不需要检验距离
        #print(self.position, self.size)

        #print(max_width)

        x, y = self.position
#        print(self.now_char)
        for char in self.now_char:
            # 计算当前字符的宽度
            size = self.ft.get_text_size(char)
            #char_width, _ = draw.textsize(char, font=self.font_path)
            # 检查是否需要换行
            if x + size[0] >= self.max_width:
                x = self.position[0]  # 重置到初始x坐标
                y += self.line_height  # 移动到下一行
            # 检查是否超出图片底部边界
            if y + self.line_height > self.max_height:
                break  # 超出边界，停止绘制
            # 绘制字符
            #draw.text((x, y), char, font=font)
            window = self.ft.draw_text(window, (x, y), char, self.color)
            x += size[0]  # 更新x坐标到下一个字符的位置

    def delay_draw(self, window=None, speed=1) -> bool:
        if window is None:
            window = self.window

        if not self.count_text == len(self.text):
            self.now_char = self.text[0:int(self.count_text)+1]
            self.count_text += speed
        self.draw(window)
        return self.window




    def is_hover(self, mouse_x, mouse_y):
        return False
        #return super().is_hover(mouse_x, mouse_y)

    def flush_color(self, new_color):
        super().flush_color(new_color)

    def re_color(self, re_color):
        super().re_color(re_color)

    def click_color_alter(self,new_color):
        super().click_color_alter(new_color)

    def click_color_exe(self, new_color):
        super().click_color_exe(new_color)

class PutChineseText(object):
    def __init__(self, ttf, text_size):
        self._face = freetype.Face(ttf)

        hscale = 1.0
        self.matrix = freetype.Matrix(int(hscale) * 0x10000, int(0.2 * 0x10000), int(0.0 * 0x10000), int(1.1 * 0x10000))
        self.cur_pen = freetype.Vector()
        self.pen_translate = freetype.Vector()
        self._face.set_transform(self.matrix, self.pen_translate)

        self._face.set_char_size(text_size * 64)
        metrics = self._face.size
        ascender = metrics.ascender / 64.0

        # descender = metrics.descender/64.0
        # height = metrics.height/64.0
        # linegap = height - ascender + descender
        self.ypos = int(ascender)

        self.pen = freetype.Vector()

    def draw_text(self, image, pos, text, text_color):
        '''
        draw chinese(or not) text with ttf
        :param image:     image(numpy.ndarray) to draw text
        :param pos:       where to draw text
        :param text:      the context, for chinese should be unicode type
        :param text_size: text size
        :param text_color:text color
        :return:          image
        '''

        # if not isinstance(text, unicode):
        #     text = text.decode('utf-8')
        image = self.draw_string(image, pos[0], pos[1] + self.ypos, text, text_color)

        return image

    def draw_string(self, img, x_pos, y_pos, text, color):
        '''
        draw string
        :param x_pos: text x-postion on text_img
        :param y_pos: text y-postion on text_img
        :param text:  text (unicode)
        :param color: text color
        :return:      image
        '''
        prev_char = 0

        self.pen.x = x_pos << 6  # div 64
        self.pen.y = y_pos << 6

        image = img
        #image = copy.deepcopy(text_img)

        for cur_char in text:
            self._face.load_char(cur_char)
            # kerning = self._face.get_kerning(prev_char, cur_char)
            # pen.x += kerning.x

            slot = self._face.glyph
            bitmap = slot.bitmap

            self.pen.x += 0
            self.cur_pen.x = self.pen.x
            self.cur_pen.y = self.pen.y - slot.bitmap_top * 64

            self.draw_ft_bitmap(image, bitmap, self.cur_pen, color)

            self.pen.x += slot.advance.x
            prev_char = cur_char
        return image

    def draw_ft_bitmap(self, img, bitmap, pen, color):
        '''
        draw each char
        :param bitmap: bitmap
        :param pen:    pen
        :param color:  pen color e.g.(0,0,255) - red
        :return:       image
        '''
        x_pos = pen.x >> 6
        y_pos = pen.y >> 6
        cols = bitmap.width
        rows = bitmap.rows

        glyph_pixels = bitmap.buffer

        for row in range(rows):
            for col in range(cols):
                if glyph_pixels[row * cols + col] != 0:
                    img[y_pos + row][x_pos + col][0] = color[0]
                    img[y_pos + row][x_pos + col][1] = color[1]
                    img[y_pos + row][x_pos + col][2] = color[2]

    def get_text_size(self, text):
        """
        计算给定文本的大小
        :param text: 文本内容
        :return: 文本的宽度和高度（以像素为单位）
        """
        width, height = 0, 0
        prev_char = 0
        for cur_char in text:
            self._face.load_char(cur_char)
            slot = self._face.glyph
            bitmap = slot.bitmap
            height = max(height, bitmap.rows)
            width += slot.advance.x >> 6  # 转换为像素单位
        return (width, height)
    
         
            
        
    
    
    
    
    
    
