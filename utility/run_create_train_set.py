import getopt
import os.path
from tkinter import *
from utility import annotator_gui, io_utils

currentDir = os.getcwd()
resumeDir = os.path.join(currentDir, '../resume')
classTrainDir = os.path.join(currentDir, '../class_train_set')
nerTrainDir = os.path.join(currentDir, '../ner_train_set')


def run_classify(resume_dir, class_train_set):
    sentences_list = io_utils.txt2sentences_list(
        io_utils.resume2txt(resume_dir))
    for idx, sentences in enumerate(sentences_list):
        # 保存到文本文件（考虑换用csv）
        save_path = os.path.join(class_train_set, str(idx + 1) + ".txt")
        root = Tk()
        gui = annotator_gui.ClassifyGUI(root, sentences, save_path)
        # root.protocol("WM_DELETE_WINDOW", gui.save2train_set())
        gui.mainloop()


def run_ner(resume_dir, ner_train_set):
    print("run ner")


def main(argv):
    """
    生成句子分类和命名实体识别训练集, -h help, -c 进行分类标注, -n 进行命名实体识别标注, --r_dir 指定简历目录,
    --c_dir 指定输出的分类训练集目录, --n_dir 指定输出的命名实体识别训练集目录.
    默认目录 r_dir=../resume c_dir=../class_train_set n_dir=../ner_train_set

    :param argv: Usage : [-h] [-c] [-n] [--r_dir resume_dir] [--c_dir class_train_dir] [--n_dir ner_train_dir]
    :return: 展示标注窗口，产生标注训练集到 class_dir ner_dir
    """
    global resumeDir, classTrainDir, nerTrainDir
    classFlag = False
    nerFlag = False
    try:
        opts, args = getopt.getopt(argv, "hcn", ["r_dir=", "c_dir=", "n_dir="])
    except getopt.GetoptError:
        print("Usage: run_create_train_set.py [-h, -c, -n, --r_dir resume_dir, --c_dir class_train_dir, "
              "--n_dir ner_train_dir")
        sys.exit(1)
    # 不传参数则表示句子分类实体识别都做且目录采用默认目录
    if len(opts) == 0:
        classFlag = True
        nerFlag = False
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: run_create_train_set.py [-h, -c, -n, --r_dir resume_dir, --c_dir class_train_dir, "
                  "--n_dir ner_train_dir")
            sys.exit()
        elif opt == '-c':
            classFlag = True
        elif opt == '-n':
            nerFlag = True
        elif opt == '--r_dir':
            resumeDir = arg
        elif opt == '--c_dir':
            classTrainDir = arg
        elif opt == '--n_dir':
            nerTrainDir = arg
    print("flags:" + str(classFlag) + ' ' + str(nerFlag))
    print("dirs:" + str(resumeDir) + str(classTrainDir) + str(nerTrainDir))
    print(currentDir)
    if os.path.isdir(resumeDir) and os.path.isdir(classTrainDir) \
            and os.path.isdir(nerTrainDir):
        if classFlag:
            run_classify(resumeDir, classTrainDir)
        if nerFlag:
            run_ner(resumeDir, nerTrainDir)
    else:
        print("please confirm dirs are correct")


if __name__ == "__main__":
    main(sys.argv[1:])
