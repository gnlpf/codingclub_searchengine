__author__ = 'frosch'

class Index:
    def __init__(self):
        pass

    '''
    index is structured like
    index = [[<keyword1>, [<url1>, <url2>]],
             [<keyword2>, [<url3>]],
             ...]
    '''
    index = []

    def add_to_index(self, keyword, url):
        key_exists = False
        for keyList in self.index:
            if keyword == keyList[0]:
                keyList[1].append(url)
                key_exists = True

        if not key_exists:
            self.index.append([keyword, [url]])

    def lookup(self, keyword):
        for keylist in self.index:
            if keyword == keylist[0]:
                return keylist[1]
        return []
