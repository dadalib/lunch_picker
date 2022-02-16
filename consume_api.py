import requests
import json

# API path for stackexchange questions
API_PATH = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

# Consume stackoverflow  questions api
def questions_stackoverflow(api_path):
    """Call the questions api from stackoverflow

    Parameters
    ----------
    api_path : str
        The web path for call the questions api from stackexhange

    Returns
    -------
    nothing
    """
    # Response of the API call
    response = requests.get(API_PATH)
    # Loop all the question
    for data in response.json()["items"]:

        if data["answer_count"] == 0:
            # By tittle
            print(data["title"])
            # By link
            print(data["link"])

        else:
            print("skipped")
        print()

        # List of questions
        # print (response.json()['items'])

        # Print response code
        # print(response.json)

        # Print data json
        # print(response.json)


if __name__ == "__main__":
    API_PATH = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
    questions_stackoverflow(API_PATH)
