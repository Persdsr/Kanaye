import requests


def get_vk(domain):
    token = '175e41cf175e41cf175e41cf94144fc1de1175e175e41cf742b1c35e95cf87e30174d8c'
    version = 5.131
    domain = domain

    r = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': 12,
                            })

    data = r.json()['response']['items']
    all_items = []

    for d in data:
        try:
            all_items.append(d['attachments'][0]['photo']['sizes'][0]['url'])
        except:
            continue

    return all_items
