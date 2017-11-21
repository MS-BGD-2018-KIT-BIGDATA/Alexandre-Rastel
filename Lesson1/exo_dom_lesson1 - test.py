import requests
import json


def randomJoke(url):
    """
    This function is outputing the text of one random joke from
    url which should be the current url for icndb websitte

    Parameters
    ----------
    url : string
        current URL pointing to ICNDB api

    Return
    ------
    text : string
        the joke as one or several sentences
    """

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

    text = data['value']['joke']

    return text


if __name__ == '__main__':
    url="https://api.icndb.com/jokes/random"
    current_joke=randomJoke(url)
    print(current_joke)
