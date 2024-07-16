import requests
from urllib.parse import urlparse

def download_url_content(urls, retries=3):
   
    results = {}
    for url in urls:
        for attempt in range(retries + 1):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
                results[url] = response.content
                break
            except requests.exceptions.RequestException as e:
                if attempt < retries:
                    print(f"Error downloading {url}: {e}. Retrying...")
                else:
                    print(f"Failed to download {url} after {retries} attempts: {e}")
            except Exception as e:
                print(f"Unexpected error downloading {url}: {e}")
                break
    return results

urls = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]
results = download_url_content(urls)
print(results)