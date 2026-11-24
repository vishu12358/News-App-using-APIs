import requests

query=input("what type of news you want to search for:\n ")
api="dc27d133fa2d4d7944ce7b2f69255e0"

url=f"https://newsapi.org/v2/everything?q={query}&apiKey=dc27d133fa2d4d7b944ce7b2f69255e0"

# print(url)

data=requests.get(url).json()
articles=data['articles']

for  index ,artical in enumerate(articles):
    print(f"{index + 1}. {artical['title']}")
    print(  artical['url'])
    print("\n*******************************\n")
    