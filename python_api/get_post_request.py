import requests


def get_request(url: str, params: dict = None) -> requests.Response:


    response = requests.get(url, params)

    if response.status_code == 200:
        json_data = response.json()
        print(f"{json_data}, type: {type(json_data)}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 1}
    get_request(url, params)