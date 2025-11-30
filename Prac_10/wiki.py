"""CP1404/CP5632 Practical
Wikipedia API demo
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    """Prompt for page titles and show details from Wikipedia."""
    wikipedia.set_lang("en")

    while True:
        title = input("Enter page title: ")
        if title == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title)
            print(page.title)
            print(page.summary)
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()