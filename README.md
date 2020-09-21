# Usage
 ###设置命令行参数   
    -c 进行分类标注, 
    -n 进行命名实体识别标注(目前命名实体识别标注尚未完成), 
    --r_dir 指定简历目录,
    --c_dir 指定输出的分类训练集目录, 
    --n_dir 指定输出的命名实体识别训练集目录,
    不指定任何参数，则使用默认目录，并同时进行命名分类标注和命名实体标注. 
### 默认目录
    r_dir=../resume c_dir=../class_train_set n_dir=../ner_train_set
### 设置标签
    分类标签目录在utility/sentence_labels下
    命名实体标签目录在utility/entity_labels下
### 标注工具
    tip 
    注意先选类别再选行，可选多行，要点击确定或者回车或者双击单行
    才能选上类别，已选定类别的行的背景色变为紫色，
    最后要点击保存才会保存，否则不会保存（特别是关闭窗口不会保存）
### 输出
    目前只有句子分类的输出，输出的格式为index[tab]sentence[tab]label
### tika环境配置
    1. pip install tika
    2. tika工具依赖tika_server.jar包，该包位于工程的lib目录下，可以移出到自定义目录
    2. 添加环境变量 TIKA_SERVER_JAR="file:///<yourpath>/tika-server-1.24.jar
# Dependencies
* **python-tika** 
* **pdfminer.six**   *(conflict with other pdfminer)*
* **python-docx**
* **pywin32(已弃用,换用python-tika)**

