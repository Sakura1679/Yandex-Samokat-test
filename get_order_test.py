
#Александр Куринец, 11 когорта, финальный проект, Инженер по тестированию плюс.
#Не понимаю, почему не получается нужный результат, через Postman возвращается код 200

import sender_stand_request
import data

def test_get_order_by_track_success_response():
    create_order_response = sender_stand_request.post_new_order(data.create_order_body)
    track_number = create_order_response.json()['track']
    get_order_response = sender_stand_request.get_order(track_number)
    assert get_order_response.status_code == 200

