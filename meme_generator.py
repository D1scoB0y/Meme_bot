import requests as r
import random

class MemeGenerator:

    @classmethod
    def return_meme(cls):
        '''
            Возвращает ссылку на случайный мем из Reddit
        '''
        responce = r.get(
                    'https://www.reddit.com/r/memes/random.json?limit=1',
                    headers = {'User-agent': str(random.randint(1000, 9999))}
                    ).json()
        
        meme_image_url = responce[0]['data']['children'][0]['data']['url']

        return meme_image_url
            