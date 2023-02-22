import sys
import requests
import time
from bs4 import BeautifulSoup as bs

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget,\
    QComboBox, QFileDialog, QListWidget
from PyQt6.QtGui import QPixmap, QImage
 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Парсинг научных статей')
        self.setFixedSize(QSize(900, 400))


        self.lh_main = QHBoxLayout()
        self.lv_1 = QVBoxLayout()
        self.lv_2 = QVBoxLayout()

        self.lh_1 = QHBoxLayout()
        self.label_1 = QLabel()
        self.label_1.setText('Ключевые слова')
        self.label_1.setFixedWidth(120)
        self.lh_1.addWidget(self.label_1)

        self.tb1 = QLineEdit()
        self.tb1.setText('')
        self.tb1.setFixedWidth(145)
        self.lh_1.addWidget(self.tb1)
        
        self.lv_1.addLayout(self.lh_1)


        self.lh_2 = QHBoxLayout()
        self.label_2 = QLabel()
        self.label_2.setText('Авторы')
        self.label_1.setFixedWidth(120)
        self.lh_2.addWidget(self.label_2)

        self.tb2 = QLineEdit()
        self.tb2.setText('')
        self.tb2.setFixedWidth(150)
        self.lh_2.addWidget(self.tb2)
        
        self.lv_1.addLayout(self.lh_2)


        self.lh_3 = QHBoxLayout()
        self.label_3 = QLabel()
        self.label_3.setText('Стоп-слова')
        self.label_1.setFixedWidth(120)
        self.lh_3.addWidget(self.label_3)

        self.tb3 = QLineEdit()
        self.tb3.setText('')
        self.tb3.setFixedWidth(150)
        self.lh_3.addWidget(self.tb3)
        
        self.lv_1.addLayout(self.lh_3)


        self.lh_4 = QHBoxLayout()
        self.label_4 = QLabel()
        self.label_4.setText('Макс. страниц рез.')
        self.label_1.setFixedWidth(120)
        self.lh_4.addWidget(self.label_4)

        self.tb4 = QLineEdit()
        self.tb4.setText('')
        self.tb4.setFixedWidth(150)
        self.tb4.setText("1")
        self.lh_4.addWidget(self.tb4)
        
        self.lv_1.addLayout(self.lh_4)


        self.list = QListWidget()
        self.list.setFixedWidth(450)
        self.list.setFixedHeight(300)


        self.btn1 = QPushButton('Сохранить в файл')
        self.btn1.setFixedWidth(150)
        self.btn1.setFixedHeight(34)
        self.btn1.clicked.connect(self.btn1_click)
        self.lv_2.addWidget(self.btn1)

        self.btn2 = QPushButton('Скачать выделенное')
        self.btn2.setFixedWidth(150)
        self.btn2.setFixedHeight(34)
        self.btn2.clicked.connect(self.btn2_click)
        self.lv_2.addWidget(self.btn2)

        self.btn3 = QPushButton('Скачать все файлы')
        self.btn3.setFixedWidth(150)
        self.btn3.setFixedHeight(34)
        self.btn3.clicked.connect(self.btn3_click)
        self.lv_2.addWidget(self.btn3)

        self.btn4 = QPushButton('Очистить список')
        self.btn4.setFixedWidth(150)
        self.btn4.setFixedHeight(34)
        self.btn4.clicked.connect(self.btn4_click)
        self.lv_2.addWidget(self.btn4)

        self.btn5 = QPushButton('Запустить парсинг')
        self.btn5.setFixedWidth(150)
        self.btn5.setFixedHeight(34)
        self.btn5.clicked.connect(self.btn5_click)
        self.lv_2.addWidget(self.btn5)


        self.lh_main.addLayout(self.lv_1)
        self.lh_main.addWidget(self.list)
        self.lh_main.addLayout(self.lv_2)

        
        container = QWidget()
        container.setLayout(self.lh_main)
        self.setCentralWidget(container)


    def download_file(self, url, file_path):
        headers_ = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Connection":"keep-alive",
            "Cookie":"browser=185.231.205.105.1670425944885398; arxiv_labs={%%22sameSite%22:%%22strict%22}; arxiv_browse=.eJwdjcEKgDAMQ39FehbB6-7eh-IHbLNIQbuxdYKI_27nLckLyQOB5AYDi3QWBXPxNe_QQ4gsxMgC5lGzoXamVQG789c1x4TwtmZlyW1jbnzHSGm4dIkiazhqVqpnJ-rd0a7sBO8Hgz0nbg.Y5CtWQ.gUQUSA9GKrjpqDmXvSooxvkNSRA; arxiv-search-parameters=\"{}\"",
            "Host":"arxiv.org", "Referer":"https://arxiv.org/", "Sec-Fetch-Dest":"document", "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin", "Sec-Fetch-User":"?1", "Upgrade-Insecure-Requests":"1", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}

        r = requests.get(url, headers = headers_)
        f = open(file_path, "wb")
        f.write(r.content) 
        f.close()

    # Кнопка - Сохранить в файл
    def btn1_click(self):
        f_p = QFileDialog.getSaveFileName(self, 'Сохранить результат', filter = ".txt")[0]
        if f_p == "":
            return

        f = open(f_p, 'w', encoding = 'utf-8')
        for i in range(self.list.count()):
            f.write(self.list.item(i).text() + "\n")
        f.close()
        
    # Кнопка - Скачать выделенное
    def btn2_click(self):
        if len(self.list.selectedItems()) == 0:
            return

        title = self.list.selectedItems()[0].text().split("\n")[0] + ".pdf"
        title = title.replace(":", "")
        f_p = QFileDialog.getSaveFileName(self, 'Скачать документ', title, filter = ".pdf")[0]
        if f_p == "":
            return
        
        url = self.list.selectedItems()[0].text().split("\n")[2] + ".pdf"
        self.download_file(url, f_p)

    # Кнопка - Скачать все файлы
    def btn3_click(self):
        f_p = QFileDialog.getExistingDirectory(self, 'Выберите каталог')[0]
        if f_p == "":
            return
        
        for i in range(self.list.count()):
            title = self.list.item(i).text().split("\n")[0] + ".pdf"
            title = title.replace(":", "")
            self.download_file(self.list.item(i).text().split("\n")[2] + ".pdf", f_p + ":/" + title)
    
    # Кнопка - Очистить список
    def btn4_click(self):
        self.list.clear()

    def parse_page(self, page):
        authors_list = self.tb2.text().split(", ")
        stop_words_list = self.tb3.text().split(", ")
        for i in range(len(stop_words_list)):
            stop_words_list[i] = stop_words_list[i].lower()

        soup = bs(page, "html.parser")
        results = soup.find_all("li", {"class": "arxiv-result"})
        for res in results:
            authors_check = False
            stow_words_check = True

            title = res.find("p", {"class":"title is-5 mathjax"}).text.replace("\\n", "").strip()
            link = res.find("p", {"class":"list-title is-inline-block"}).find_all("a")[1]["href"]
            authors = ""
            a_tmp = res.find("p", {"class":"authors"}).find_all("a")
            for a_link in a_tmp:
                authors += a_link.text + ", "

                if(len(authors_list) > 0 and authors_list[0] != ""):
                    if(a_link.text in authors_list):
                        authors_check = True
                else:
                    authors_check = True
                
                title_words = title.split(" ")
                if(len(title_words) > 0 and title_words[0] != ""):
                    for t_word in title_words:
                        if t_word.lower() in stop_words_list:
                            stow_words_check = False

            authors = authors[0:-2]

            #print(title)
            #print(link)
            #print(authors)

            if not authors_check or not stow_words_check:
                continue

            self.list.addItem(title + "\n(" + authors + ")\n" + link)

    # Кнопка - Запустить парсинг
    def btn5_click(self):
        self.list.clear()

        keywords = self.tb1.text()
        max_num = int(self.tb4.text())

        url = "https://arxiv.org/search/"
        headers_ = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br", "Accept-Language":"ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Connection":"keep-alive",
            "Cookie":"browser=185.231.205.105.1670425944885398; arxiv_labs={%%22sameSite%22:%%22strict%22}; arxiv_browse=.eJwdjcEKgDAMQ39FehbB6-7eh-IHbLNIQbuxdYKI_27nLckLyQOB5AYDi3QWBXPxNe_QQ4gsxMgC5lGzoXamVQG789c1x4TwtmZlyW1jbnzHSGm4dIkiazhqVqpnJ-rd0a7sBO8Hgz0nbg.Y5CtWQ.gUQUSA9GKrjpqDmXvSooxvkNSRA; arxiv-search-parameters=\"{}\"",
            "Host":"arxiv.org", "Referer":"https://arxiv.org/", "Sec-Fetch-Dest":"document", "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-Site":"same-origin", "Sec-Fetch-User":"?1", "Upgrade-Insecure-Requests":"1", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}

        r = requests.get(f"{url}?query={keywords}&searchtype=all&source=header&size=50", headers = headers_)
        page = r.text
        cur_num = 1

        #f = open('Z:/2.html', 'r')
        #page = f.read()
        #f.close()

        self.parse_page(page)

        while cur_num < max_num:
            try:
                start = 50 * cur_num
                cur_num += 1
                print(f"cur_num: {cur_num}")
                time.sleep(2)
                url = f"https://arxiv.org/search/"
                r = requests.get(f"{url}?query={keywords}&searchtype=all&source=header&size=50&start={start}", headers = headers_)
                page = r.text
                self.parse_page(page)
            except:
                print("exception when parsing")
                break


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

