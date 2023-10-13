# pdf2word

一个基于python实现的pdf文档转word文档工具

## 使用方法

```
git clone https://github.com/artdong/pdf2word.git

cd pdf2word

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python main.py
```

## 配置修改

配置文件config.cfg

pdf_folder：指定存放pdf文件的文件夹，默认pdf

doc_folder：指定存放word文件的文件夹，默认doc

max_worker：同时工作的进程数，默认10
