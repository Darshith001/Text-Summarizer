import requests
from bs4 import BeautifulSoup

def fetch_website_contents(url: str) -> str:
    """
    Fetches the content of a website and returns the clean text from the body.

    Args:
        url: The URL of the website to scrape.

    Returns:
        The cleaned text content of the website's body, or an error message if fetching fails.
    """
    try:
        # Set a user-agent to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send a GET request to the URL with a timeout
        response = requests.get(url, headers=headers, timeout=15)
        
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Parse the HTML content and extract text from the body
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.body.get_text(separator='\n', strip=True)

    except requests.exceptions.RequestException as e:
        return f"Error fetching the URL {url}: {e}"
