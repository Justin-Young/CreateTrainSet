import os
from . import pdf_utils
from . import docx_utils
from . import split_utils

debuglog = True


def resume2txt(resume_dir):
    """
    读取简历目录下的所有文件并返回读取到的文本字符串列表

    :param resume_dir: 要读取的简历目录
    :return text_list: 返回读取到的文本字符串列表
    """
    text_list = []
    # 将目录下的所有.doc文件转换成.docx文件
    for f in os.listdir(resume_dir):
        file_path = os.path.join(resume_dir, f)
        if os.path.isfile(file_path):
            if f.lower().endswith('.doc'):
                if debuglog:
                    print("doc_file: " + file_path)
                if not docx_utils.is_already_converted(file_path):
                    docx_utils.doc2docx(file_path)
    # 读取所有的.docx和.pdf文件
    for f in os.listdir(resume_dir):
        txt = None
        file_path = os.path.join(resume_dir, f)
        if debuglog:
            print("resume_file: " + file_path)
        if os.path.isfile(file_path):
            if f.lower().endswith('.docx'):
                txt = docx_utils.docx2string(file_path)
            elif f.lower().endswith('.pdf'):
                txt = pdf_utils.pdf2string(file_path)
        if txt is not None and len(txt):
            text_list.append(txt)
            if debuglog:
                print(txt)
    return text_list


def txt2sentences_list(text_list):
    """
    将字符串转为句子序列

    :param text_list:
    :return: 返回句子列表的列表
    """
    sequences_list = []
    for txt in text_list:
        sentences = split_utils.split2sentences(txt)
        if len(sentences):
            if debuglog:
                print(sentences)
            sequences_list.append(sentences)
    return sequences_list


