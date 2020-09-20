from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def pdf2string(path):
    """
    提取pdf文件中的文本并转化为字符串

    :param path: pdf文件的完整路径
    :return: 提取的字符串
    """
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    result = []

    with open(path, 'rb') as infile:
        for page in PDFPage.get_pages(infile):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        result = output.getvalue()
    return result
