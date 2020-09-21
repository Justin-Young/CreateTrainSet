from tkinter import *
from tkinter import ttk

debuglog = True


def load_sentence_labels():
    """
    读取包目录下的sentence_labels，以获取句子分类标签列表，保存在self.sentence_labels
    :return: 返回句子标签列表
    """
    with open("./sentence_labels", "r") as f:
        text = f.read()
        return text.split('\n')


def load_entity_labels():
    """
    读取包目录下的entity_labels,以获取实体类别标签列表，保存在self.entity_labels
    :return: 返回实体标签列表
    """
    with open("./entity_labels", "r") as f:
        text = f.read()
        return text.split('\n')


class ClassifyGUI(Frame):
    """
    句子分类GUI
    """

    def __init__(self, master, sentences, save_path):
        super().__init__(master=master)
        self.master.title("Sentences Classification")
        # 设置顶级窗体的行列权重，否则子组件的拉伸不会填充整个窗体
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # 添加框架容器
        self.grid(column=0, row=0, columnspan=4, rowspan=4, sticky=(N, W, E, S))
        # 将句子列表添加至listbox,设置多行选中模式
        self.sentences = sentences
        sentences_var = StringVar(value=sentences)
        self.listbox = Listbox(self, listvariable=sentences_var,
                               selectmode=EXTENDED)
        # 为listbox添加滚动条
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL,
                                   command=self.listbox.yview)
        self.listbox['yscrollcommand'] = vscrollbar.set
        hscrollbar = ttk.Scrollbar(self, orient=HORIZONTAL,
                                   command=self.listbox.xview)
        self.listbox['xscrollcommand'] = hscrollbar.set
        # 添加提示
        tip_label = ttk.Label(self, text="      选定行的类别\n(先选类别再选行,可选多行)")
        # 加载句子分类标签列表
        self.sentence_labels = load_sentence_labels()
        if debuglog:
            print(self.sentence_labels)
        sentence_labels_var = StringVar()
        # print(sentence_labels_var.get())
        # 将标签添加至combobox
        self.combobox = ttk.Combobox(self, textvariable=sentence_labels_var)
        self.combobox['values'] = self.sentence_labels
        # 添加确定、丢弃并退出、保存并退出按钮
        confirm_button = ttk.Button(self, text="确定")
        discard_button = ttk.Button(self, text="丢弃并退出")
        save_button = ttk.Button(self, text="保存并退出")

        # 进行几何布局显示控件
        self.listbox.grid(column=0, row=0, rowspan=3, sticky=(N, W, E, S))
        vscrollbar.grid(column=1, row=0, rowspan=3, sticky=(N, S))
        hscrollbar.grid(column=0, row=3, sticky=(W, E))
        tip_label.grid(column=2, row=0, columnspan=2)
        self.combobox.grid(column=2, row=1, columnspan=2)
        confirm_button.grid(column=2, row=2, columnspan=2)
        discard_button.grid(column=2, row=3)
        save_button.grid(column=3, row=3)
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # 用于保存已经分过类的句子，元素为（sentence,label)
        self.classified_list = []
        self.save_path = save_path

        # 进行事件绑定
        confirm_button["command"] = self.tick_label
        # 绑定全局回车到确定按钮
        self.master.bind('<Return>', self.tick_label)
        self.listbox.bind('<Double-1>', self.tick_label)
        save_button["command"] = self.save2train_set
        discard_button["command"] = self.master.destroy

    def tick_label(self, *args):
        """
        选择类别标签，并添加至待保存列表

        :return:打标签
        """
        # args是绑定回车的形式约定，本函数中无实际意义
        # 获取类别标签
        clabel = self.combobox.get()
        # 获取选中行
        idxs = self.listbox.curselection()
        for item in idxs:
            idx = int(item)
            sentence = self.sentences[idx]
            # 添加至以分类列表，并修改背景色
            self.classified_list.append((str(idx), sentence, clabel))
            self.listbox.itemconfigure(idx, background='purple')

    def save2train_set(self):
        with open(self.save_path, "w", encoding='utf-8') as f:
            for item in self.classified_list:
                string = item[0] + "\t" + item[1] + "\t" + item[2] + "\n"
                f.write(string)
            if debuglog:
                print("saved to file")
        # self.quit()
        self.master.destroy()
