import requests

def get_random_joke():
    """Fetch a random joke from the official Joke API"""
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)  # added timeout for reliability
        response.raise_for_status()  # raise an error for bad HTTP codes

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"

    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch joke. ({e})"


def main():
    print("😂 Welcome to the Random Joke Generator! 😂")
    while True:
        user_input = input("\nPress Enter for a new joke, or type 'q'/'exit' to quit: ").strip().lower()
        if user_input in ("q", "exit"):
            print("Goodbye! 👋")
            break

        joke = get_random_joke()
        print("\n" + joke)


if __name__ == "__main__":
    main()
