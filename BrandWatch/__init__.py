import investigate
import datetime

from Leet import Leet

class Watcher:
    def __init__(self, api_key=None, brand=None, exclude=None, days=1, limit=100, include_category=False):
        """Create a new Watcher instance

        Keyword arguments:
        api_key -- Investigate API Key for making queries
        brand -- Brand name string to include in pattern searches. Brands that are also very common names may return lots of results
        exclude -- (Optional) list of domains that should be excluded from searches
        """

        if api_key is None or brand is None:
            raise Exception('No API key or Brand defined')

        self.api_key = api_key
        self.brand = brand
        self.exclude = exclude
        self.days = days
        self.limit = limit
        self.include_category=include_category
        self.regex_list = []

        self.inv = investigate.Investigate(api_key)
        self.generate()

    def leet(self):
        l = Leet(self.brand)
        return '.*{0}.*'.format(l.get_regex_duplicate())

    def simple(self):
        # This is also covered by leet()
        return '.*{0}.*'.format(self.brand)

    def generate(self):
        # Simple is also covered by leet()
        # self.regex_list.append(self.simple())
        self.regex_list.append(self.leet())

    def search(self):
        for r in self.regex_list:
            results = self.inv.search(r, start=datetime.timedelta(days=self.days), limit=self.limit, include_category=self.include_category)
            if len(results['matches']) > 0:
                for result in results['matches']:
                    name = result['name']
                    if self.exclude is not None:
                        if name not in self.exclude:
                            print name
                    else:
                        print name

