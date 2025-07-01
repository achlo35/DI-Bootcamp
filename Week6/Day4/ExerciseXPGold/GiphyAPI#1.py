import requests

def fetch_hilarious_gifs():
    # Set up parameters
    api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
    query = "hilarious"
    rating = "g"
    limit = 10  # Only return the first 10 gifs

    # Build the URL using f-strings
    url = (
        f"https://api.giphy.com/v1/gifs/search"
        f"?q={query}&rating={rating}&api_key={api_key}&limit={limit}"
    )

    # Fetch the gifs
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Only return gifs with height > 100
        filtered_gifs = [
            gif for gif in data["data"]
            if int(gif["images"]["original"]["height"]) > 100
        ]
        print(f"Number of gifs received: {len(data['data'])}")
        print(f"Number of gifs with height > 100: {len(filtered_gifs)}")
        return filtered_gifs
    else:
        print("Failed to fetch gifs.")
        return None

# Example usage:
if __name__ == "__main__":
    gifs = fetch_hilarious_gifs()
    if gifs:
        for gif in gifs:
            print(gif["url"])