import requests
import csv
from bs4 import BeautifulSoup
import time
size_of_rows = 0
for npage in range(1,200):
    time.sleep(0.5)
    URL = "https://movie.naver.com/movie/point/af/list.naver?&page="
#URL = "https://movie.naver.com/movie/point/af/list.naver?&page=1"
    response = requests.get(URL+str(npage)) #+1,2,3
    soup = BeautifulSoup(
        response.text,'html.parser'
    )
    body = soup.find(name = "tbody")
#for title in headline.find_all(name = "strong", attrs={"class":"title"}):
#print(title.get_text())

    titles = body.find_all(name ="a",attrs = {"class":"movie color_b"})
    title = [title_row.get_text() for title_row in titles]
#print(title)

    stars = body.find_all(name ="em")
    star = [star_row.get_text() for star_row in stars]
#print(star)

    small_body = body.find_all(name="td", attrs={"class":"title"})
#print(small_body)

    sentences = [sen_row for sen_row in small_body]
    sentence = []
    for i in sentences:
        i = str(i)
        br_index = int(i.find("<br/>"))
        repo_index = int(i.find("<a class=\"report\""))
        comments = i[br_index+5:repo_index]
        sentence.append(comments.rstrip())
#print(sentence)
    if npage == 1:
        new_list = [["movie","sentence","score"]]
    else:
        new_list = []
    for trio in zip(title,sentence,star):
        if trio[1] == "" or trio[1].find("OO") != -1 :
        #print("no_sen")
            continue
        if size_of_rows == 1000:
            break
        new_cp = list(trio)
        new_list.append(new_cp)
        size_of_rows += 1
#print(new_list)
    if npage == 1:
        with open("testtext.csv","w",encoding="utf-8") as fd:
            pass

    with open("testtext.csv","a",encoding="utf-8") as fd:
        writer = csv.writer(fd, delimiter=",",quotechar='"')
        writer.writerows(i for i in new_list)
    if size_of_rows >= 1000:
        break
