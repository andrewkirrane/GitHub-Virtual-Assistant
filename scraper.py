import requests
from bs4 import BeautifulSoup
import json

data = []

url = "https://resources.github.com/faq/"
webpage = requests.get(url)

soup = BeautifulSoup(webpage.content, "html.parser")

faq_elements = soup.find("main", id = False, class_ = "container-xl mx-auto clearfix gutter gutter-lg-spacious minHeight-full-screen")

qa_pairs = faq_elements.find_all("div", class_ = "col-10 float-left clearfix mb-7 mb-md-6")

for qa_elements in qa_pairs:
    question_element = qa_elements.find("span", class_ = "f4 text-mono lh-big underline-dashed")
    question = question_element.text.strip()
    question = question.replace("\n            ", " ")[question.find(next(filter(str.isalpha, question))):-1]
    answer_element = qa_elements.find("div", class_ = "ml-5 d-flex flex-md-row flex-wrap gutter gutter-lg-spacious")
    answer = answer_element.text.strip()
    links = qa_elements.find_all("a")
    for link in links:
        link_url = link["href"]
        answer = answer + "\n" + link_url
    entry = {"tag": question, "patterns": [question], "responses": [answer.replace("\n            ", " ")]}
    data.append(entry)

with open("Github_FAQ_unedited.json", "w", encoding = "utf8") as f:
    json.dump({"data": data}, f, ensure_ascii = False)