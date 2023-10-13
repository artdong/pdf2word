import os
import logging
from configparser import ConfigParser
from concurrent.futures import ProcessPoolExecutor
from pdf2docx import Converter

def pdf_to_doc(pdf_file_path, doc_file_path):
    cv = Converter(pdf_file_path)
    cv.convert(doc_file_path)
    cv.close()

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_pdf_file(pdf_file, pdf_folder, doc_folder):
    file_name, extension_name = os.path.splitext(pdf_file)
    if extension_name != ".pdf":
        return

    pdf_file_path = os.path.join(pdf_folder, pdf_file)
    doc_file_path = os.path.join(doc_folder, file_name + ".docx")

    print("⌛️正在处理：" + pdf_file)
    pdf_to_doc(pdf_file_path, doc_file_path)
    print(pdf_file + "处理完成✅")

def main():
    logging.getLogger().setLevel(logging.ERROR)

    config_parser = ConfigParser()
    config_parser.read("config.cfg")
    config = config_parser["default"]

    pdf_folder = config["pdf_folder"]
    doc_folder = config["doc_folder"]
    max_workers = int(config["max_worker"])

    if not os.path.exists(pdf_folder):
        print(f"'{pdf_folder}'文件夹不存在，请创建该文件夹。")
        return

    create_directory_if_not_exists(doc_folder)

    pdf_files = [file for file in os.listdir(pdf_folder) if file.endswith(".pdf")]

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for pdf_file in pdf_files:
            executor.submit(process_pdf_file, pdf_file, pdf_folder, doc_folder)

    print("所有文件处理完成✅")

if __name__ == "__main__":
    main()
