import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


response = post_new_order(data.create_order_body);

print(response.json())

track = response.json()['track']
print(track)


def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, track_number)


response = get_order(track)
print(response.status_code)
print(response.json())
