from soup.tasks import my_map

res = my_map.delay("https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report")
print(res.get())
