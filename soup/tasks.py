from bs4 import BeautifulSoup
import requests
from collections import Counter
from celery_app import app


@app.task()
def my_map(url):
    c = Counter()
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    for word in soup.get_text().split():
        if word not in c:
            c[word] = 0
        c[word] += 1
    return c


@app.task
def my_reduce(counters):
    res = counters[0]
    for c in counters[1:]:
        res += c
    return res


if __name__ == "__main__":
    app.start()
