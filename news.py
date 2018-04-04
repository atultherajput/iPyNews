import requests     
 
def PyNews(option, c, q):
    apiKey = "9f6bb23dade24e2a9215192*********" #get api from https://newsapi.org

    top_headlines = "https://newsapi.org/v2/top-headlines?country="+c+"&apiKey="+apiKey
    everything = "https://newsapi.org/v2/everything?language=en&sortBy=popularity&q="+q+"&apiKey="+apiKey
    sources = "https://newsapi.org/v2/sources?apiKey="+apiKey

    results = []

    if option == 1:
        news = requests.get(top_headlines).json()
        articles = news["articles"]
        for article in articles:
            results.append(article["title"])
    
    elif option == 2:
        news = requests.get(everything).json()
        articles = news["articles"]
        for article in articles:
            results.append(article["title"]+":\n"+ article["description"])

    elif option == 3:
        news = requests.get(sources).json()
        articles = news["sources"]
        for article in articles:
            results.append(article["name"])
         
    for i in range(len(results)):
        print(str(i + 1)+'.', results[i])           
 

def driver(option=1, c="in", q="india"):
        option = int(input("1. Top Headlines by country \n2. Everything by keyword \n3. News Sources \nSelect option: "))
        if option == 1:
            c = input("Enter two digit country code: ")
        elif option == 2:
            q = input("Search Keyword: ")
        elif option == 3:
            pass
        else:
            print("Wrong Option!")
            driver()

        PyNews(option, c, q)

if __name__ == '__main__':
    driver()
