from src.tools.tools import web_search, scrape_url

#results = web_search("Latest news on AI Research")
#results = scrape_url("https://ai.meta.com/blog/")
results = scrape_url("https://www.reddit.com/r/artificial/")

print(results)