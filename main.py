from exa_py import Exa
exa = Exa(api_key='YOUR_EXA_API_KEY') #don't forget to replace with YOUR API key from Exa

# Take user's query input
query = input('Search here: ')

# Perform search 
response = exa.search(
    query,
    num_results=10,
    include_domains=["https://www.tiktok.com", "https://www.mynetdiary.com/"],
)

# Print results
for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
