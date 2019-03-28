import json

def getDictionaryKeys():
    dictionaryFile = '/var/www/html/web-control/src/plugins/dictionary-plugin/dictionary.json'
    dictionary = {}

    with open(dictionaryFile) as json_file:
        data = json.load(json_file)
        for p in data['measurements']:
            dictionary[p['key']]=0
    return dictionary
