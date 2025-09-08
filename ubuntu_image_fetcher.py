import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """
    Extract filename from URL path.
    If no filename or no extension, generate one using a hash of the URL.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    # Check if filename is empty or has no extension (e.g., no '.jpg')
    if not filename or '.' not in filename:
        # Generate a unique filename using MD5 hash of the URL
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
        filename = f"image_{url_hash}.jpg"
    return filename

def is_image_content(response):
    """
    Check if the response Content-Type header indicates an image.
    """
    content_type = response.headers.get('Content-Type', '')
    return content_type.startswith('image/')

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompt user for image URL or use default if empty
    url = input("Please enter the image URL (or press Enter to use a default image): ").strip()
    if not url:
        url = "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png"
        print(f"Using default image URL: {url}")

    # Create directory for saving images
    os.makedirs("Fetched_Images", exist_ok=True)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36"
        }
        # Fetch the image with a timeout of 10 seconds and custom headers
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)

        # Check if the response is an image
        if not is_image_content(response):
            print("✗ The URL does not point to an image resource.")
            return

        # Extract or generate filename
        filename = get_filename_from_url(url)

        # Full path to save the image
        filepath = os.path.join("Fetched_Images", filename)

        # Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()