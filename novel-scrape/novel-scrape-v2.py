from bs4 import BeautifulSoup
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

html_text = requests.get("https://novelmax.net/n/shadow-slave/chapter1-nightmare-begins", headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
chapter = soup.find("div", id = "chr-content", class_ = "chr-c")
chapter_title_n_number = chapter.find("h4")
chapter_paragraphs = chapter.find_all("p")

chapter_text = ""
for paragraph in chapter_paragraphs:
    chapter_text += paragraph.text + "\n"

print(chapter_text)