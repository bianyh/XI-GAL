


from home import home_page_config



if __name__ == '__main__':
    home_page=open('home//home_page.txt', encoding='utf8')

    home_page = home_page.readlines()
    for i in home_page:
        if i[0] == '@':
            speak_name = i[1:-1]
            print(speak_name)
        elif i[0] == 'T':
            speak_text = i[1:-1]
            print(speak_text)
        elif i[0] == 'L':
            speak_location = i[1:-1]
            print(speak_location)
        elif i[0] == 'C':
            speak_text_color = i[1:-1]
            print(speak_text_color)
        elif i[0] == 'M':
            music_name = i[1:-1]
            print(music_name)
        elif i[0] == '!':
            shut_music = i[1:-1]
            print(shut_music)
        elif i[0] == 'B':
            background_img = i[1:-1]
            print(background_img)
        elif i[0] == 'I':
            image = i[1:-1]
            print(image)



