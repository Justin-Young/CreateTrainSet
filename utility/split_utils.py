import re


def split2sentences(string):
    """
    将获得的简历文本分成一个个的句子

    :param string: 从简历中获取的文本
    :return: 分句后的句子序列
    """
    # 去掉特殊符号，项目符号
    string = re.sub(r'[•⚫�]', '', string)
    # 去掉空行
    string = re.sub(r' *\n', '##', string)
    # 去掉句中换行
    # string = re.sub(r'(\n)', '', string)
    # 去掉连续的 ##,只保留一个
    string = re.sub(r'(#{2,})', '##\n',string)
    # 去掉字符串起始的 ##\n
    string = re.sub(r'^##\n', '', string)
    # 去掉句首前导符
    # string = re.sub(r'(##\n-( )?)|(##\n[\uf06c|\uf026]( )?)', '', string)
    # 遇到连续的4个或以上空格另算一句
    string = re.sub(r' {4,}', '##\n', string)
    # 返回分句后和句子列表
    return re.split(r'##\n', string)