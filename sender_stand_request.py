import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

response = post_new_order(data.create_order_body);
track = response.json()['track']
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t":track})
