import json
import requests
import requests_cache
from pprint import pformat

from data import kanji_list

requests_cache.install_cache('kanji_cache', backend='sqlite', expire_after=999999)

def get_jisho_search(kanji):
    url = "https://jisho.org/api/v1/search/words"
    querystring = {"keyword": kanji}
    response = requests.request("GET", url,  params=querystring)
    response = json.loads(response.text)
    return response


if __name__ == "__main__":

    for kanji in kanji_list:

        response = get_jisho_search(kanji)

        print("Kanji {}: -------------------------".format(kanji))

        #si tuviera sólo una

        #print("\tenglish definitions: {}".format(response['data'][0]['senses'][0]['english_definitions']))

        #si queremos que busque si hay varias

        for data in response['data']:
            for senses in data['senses']:
                print("\tenglish definitions: {}".format(senses['english_definitions']))

        #print(pformat(response))

        



