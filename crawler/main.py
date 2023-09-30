import pandas
from pandas import DataFrame
bookmark = pandas.read_excel("trading.xlsx")
from urltitle import URLTitleReader
reader = URLTitleReader(verify_ssl=True)

def run(pd:DataFrame):
    for index, row in pd.iterrows():
        print(row["title"], row["url"])
        url = row["url"]
        try: 
            title = reader.title(url=url)
        except:
            title = None
        print(pd.at[index, "title"])
        pd.at[index, "title"] = title
        print(pd.at[index, "title"])
        
        print(title)

run(pd=bookmark)
print(bookmark)
# from requests_html import HTMLSession
# link = "https://www.douyin.com/video/7180736146123640121"
# session = HTMLSession()
# r = session.get(link)
# print(dir(r))
# r = requests.get(url=link)
# print(r.status_code)
# print(r.content.decode())
