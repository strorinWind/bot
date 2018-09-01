import vk
import random

session = vk.Session()
api = vk.API(session, v=5.0)


def get_random_wall_picture(group_id, token):
    max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0, access_token=token)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num, access_token=token)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)

