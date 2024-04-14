window_config = {
    'window_size': (1200, 700),
}

text_config = {
    'text_color': (0, 0, 0),
    'text_font': 'home//source//simsun.ttf',
    'text_font_size': 30,
    'text_position': (int(window_config['window_size'][0] * 0.1),
                      int(window_config['window_size'][1] * 0.8)),
}

text_box_config = {
    'text_box_position': (int(window_config['window_size'][0] * 0.05),
                          int(window_config['window_size'][1] * 0.7)),
    'text_box_size': (int(window_config['window_size'][0] * 0.9),
                      int(window_config['window_size'][1] * 0.3)),
    'text_box_path': 'home//source//text_box.png',
    'text_box_alpha': 0.2,
}