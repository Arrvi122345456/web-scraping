from bs4 import BeautifulSoup
import requests

# User agent , browser id or someyhing like that, this way site dosent block us

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

# Website URL , WebNovel site of novel - shadow slave
html_text = requests.get("https://novelmax.net/n/shadow-slave/chapter1-nightmare-begins", headers=headers).text

# changes html with lxml
soup = BeautifulSoup(html_text, 'lxml')

# finds chapter div
chapter = soup.find("div", id = "chr-content", class_ = "chr-c")

# chapter title in h4 tag
chapter_title_n_number = chapter.find("h4").text

# space for readibility
chapter_title_n_number += "\n"

# chapter contents are stored in p tags
chapter_paragraphs = chapter.find_all("p")

# for loop, get text from html
chapter_text = ""
for paragraph in chapter_paragraphs:
    chapter_text += paragraph.text + "\n\n"

next_chapter_tag = soup.find("div", class_ = "btn-group")
next_chapter_link = soup.find("a", id = "next_chap" )


# print chapter titlr and number + chaper contents text
print( chapter_title_n_number + chapter_text)

print(next_chapter_link)