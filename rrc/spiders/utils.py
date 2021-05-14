from fontTools.ttLib import TTFont

def font_name(name):
    '''
    通过手敲的映射关系,解析字体文件
    '''
    number_map = {'eight': '8', 'five': '5', 'one': '1', 'nine': '9', 'period': '?', 'three': '3', 'six': '6',
                  'two': '2', 'seven': '7', 'four': '4', 'zero': '0'}
    # 下载下来的font文件
    font = TTFont(name)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 取出来font文件中的zero到nine,从第一个开始
    font_num = font.getGlyphOrder()[1:]
    # print('--------------',font_num)     # ['zero', 'one', 'two', 'three', 'four', 'five', 'seven', 'eight', 'six', 'nine']
    dic_font = dict(zip(num, font_num))
    # print('**************',dic_font)     # {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'seven', '7': 'eight', '8': 'six', '9': 'nine'}
    dict_num = {}
    for k, v in dic_font.items():
        for x, y in number_map.items():
            if dic_font[k] == x:
                dict_num[y] = k
    return dict_num


def base_font(dict, base_str):
    '''
    对照字典,解码字符串
    :param dict:
    :param base_str:
    :return:
    '''
    str_lis = []
    num_lis = list(dict.keys())
    for i in base_str:
        if i in num_lis:
            i = dict[i]
            str_lis.append(i)
        else:
            i = i
            str_lis.append(i)
    str_ = ''.join(str_lis)
    return str_
