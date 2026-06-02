#!/usr/bin/env python3
"""
CodeAlpha Python Internship
Task 3: Task Automation - Script 3: Webpage Title Scraper

Automates scraping the HTML title tag of any webpage. Fetches the page using 
requests, extracts the text using BeautifulSoup, and saves it to an output file.
"""

import os
import requests
from bs4 import BeautifulSoup


def scrape_webpage_title(url, output_filepath):
    """
    Downloads webpage at url, extracts the title, and saves it to output_filepath.
    Handles network errors gracefully.
    """
    output_filepath = os.path.abspath(output_filepath)
    
    # 1. Standardize URL format
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\n[+] Scrape Target URL:  {url}")
    print(f"[+] Output Destination: {output_filepath}")
    print("[~] Sending request, please wait...\n")

    # 2. Add realistic User-Agent to avoid scraping blocks/defenses
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        # Fetch webpage (with a 10-second timeout)
        response = requests.get(url, headers=headers, timeout=10)
        
        # Raise HTTPError for bad status codes (4xx, 5xx)
        response.raise_for_status()
        
    except requests.exceptions.HTTPError as http_err:
        print(f"[-] HTTP Error occurred: {http_err}")
        return
    except requests.exceptions.ConnectionError:
        print("[-] Connection Error: Could not connect to the server. Please check your network or spelling.")
        return
    except requests.exceptions.Timeout:
        print("[-] Timeout Error: The server took too long to respond.")
        return
    except requests.exceptions.RequestException as req_err:
        print(f"[-] An unexpected network error occurred: {req_err}")
        return

    # 3. Parse HTML using BeautifulSoup
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the <title> tag
        title_tag = soup.find('title')
        
        if title_tag and title_tag.string:
            # Strip trailing whitespaces or newline tags
            webpage_title = title_tag.string.strip()
        else:
            webpage_title = "No Title Tag Found"

        print(f"[+] Webpage Title Found: \"{webpage_title}\"")

        # 4. Save to text file
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(f"Webpage Scraped: {url}\n")
            f.write(f"Scraped Title:   {webpage_title}\n")
            
        print(f"[+] Success: Saved details to '{output_filepath}'\n")

    except Exception as e:
        print(f"[-] Error parsing webpage content: {e}")


def main():
    """
    Main controller. Uses default example or prompts user for a custom URL.
    """
    print("=" * 50)
    print("       WEB SCRAPER: WEBPAGE TITLE EXTRACTOR     ")
    print("=" * 50)

    # Pre-configured defaults
    default_url = "https://example.com"
    default_output = "scraped_title.txt"

    print(f"\nDefault Test URL:  {default_url}")
    print(f"Default Output:    {default_output}")

    choice = input("\nUse default test URL? (yes/no) [Default: yes]: ").strip().lower()

    if choice in ['n', 'no']:
        url_input = input("Enter webpage URL to scrape: ").strip()
        output_input = input("Enter output file path: ").strip()

        if not url_input:
            print("[-] URL cannot be empty! Reverting to default.")
            scrape_webpage_title(default_url, default_output)
        else:
            output_path = output_input if output_input else default_output
            scrape_webpage_title(url_input, output_path)
    else:
        scrape_webpage_title(default_url, default_output)


if __name__ == "__main__":
    main()
