'''
Export Hipchat history.

* History: https://www.hipchat.com/docs/api/method/rooms/history
* Auth: https://www.hipchat.com/docs/api/auth

'''
import datetime
import os
import urllib

import requests


class Hipchat(object):
    base = "https://api.hipchat.com/v1/"

    def __init__(self, auth_token):
        self.auth_token = auth_token

    def request(self, path):
        url = self.base + path

        response = requests.get(url)
        try:
            response.raise_for_status()
        except:
            raise

        data = response.json()
        return data

    def history(self, room_id, date=None):
        '''
        https://www.hipchat.com/docs/api/method/rooms/history

        '''
        date = date or datetime.datetime.now()
        date_str = date.strftime("%Y-%m-%d")

        query = {
            "room_id": room_id,
            "date": date_str,
            "timezone": "PST",
            "format": "json",
            "auth_token": self.auth_token
        }

        path = "rooms/history?{0}".format(urllib.urlencode(query))
        print path

        data = self.request(path)
        messages = data["messages"]
        return messages


def get_client(auth_token=None):
    auth_token = auth_token or os.environ.get("HIPCHAT_AUTH_TOKEN", None)
    if auth_token is None:
        raise

    client = Hipchat(auth_token=auth_token)
    return client



def main():
    room_id = os.environ.get("HIPCHAT_ROOM_ID", None)
    if room_id is None:
        raise

    client = get_client()
    client.history(room_id=room_id)


if __name__ == "__main__":
    main()