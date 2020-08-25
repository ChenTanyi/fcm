#!/usr/bin/env python3
import os
import sys
import requests


def notify(key: str, title: str, body: str, **kwargs) -> requests.Response:
    r = requests.post(
        'https://fcm.googleapis.com/fcm/send',
        headers = {'Authorization': 'key={0}'.format(key)},
        json = {
            'notification': {
                'title': title,
                'body': body,
            },
            'data': {
                'message': body,
            },
            "condition": "!('test' in topics)",
        },
        timeout = kwargs.get('timeout'))
    return r


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            'Usage: {0} <title> <body>'.format(sys.argv[0]), file = sys.stderr)
        sys.exit(0)

    r = notify(
        os.environ['FIREBASE_SERVER_KEY'],
        sys.argv[1],
        sys.argv[2],
        timeout = 20)

    print(r.content)
    r.raise_for_status()
