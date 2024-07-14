import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited_links = set()

def get_subpages(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve {base_url}: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for link in soup.find_all('a', href=True):
        url = link['href']
        if not urlparse(url).netloc:  # Handle relative URLs
            url = urljoin(base_url, url)
        if url.startswith(base_url) and url not in visited_links:
            visited_links.add(url)
            links.append(url)

    return links

def write_links_to_file(links, filename="Links.txt"):
    with open(filename, 'w') as file:
        for link in links:
            file.write(f"{link}\n")

def crawl_website(base_url, max_links=100):
    pages_to_visit = [base_url]
    all_subpages = []

    while pages_to_visit and len(all_subpages) < max_links:
        current_page = pages_to_visit.pop()
        subpages = get_subpages(current_page)
        for subpage in subpages:
            if len(all_subpages) < max_links:
                all_subpages.append(subpage)
            else:
                break
        pages_to_visit.extend(subpages)
        
        print(f"Number of links found: {len(all_subpages)}")

    write_links_to_file(all_subpages)
    return all_subpages

if __name__ == "__main__":
    base_url = "https://wiki.redmodding.org/cyberpunk-2077-modding"  # Replace with the target URL
    max_links = 100  # Set the maximum number of links to find
    all_subpages = crawl_website(base_url, max_links)
    print("Crawling completed. Links have been saved to Links.txt.")
