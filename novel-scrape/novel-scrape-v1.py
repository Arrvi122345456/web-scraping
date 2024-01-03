from bs4 import BeautifulSoup

with open ("novel-scrape/home.html", "r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")
    cards = soup.find_all("div", class_ = "card")
    for card in cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        
        print(f"{course_name} costs: {course_price}")