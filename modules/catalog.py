from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd

class Catalog():
    def __init__(self, catalog=None):
        self.catalog = catalog

    def search(self, input_search):
        list_results = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search.lower() in item.title.lower():
                    if type(item) == Book:
                            list_results.append(f'title : {item.title},Type Catalog: Book')
                    elif type(item) == Magazine:
                            list_results.append(f'title : {item.title},Type Catalog: Magazine')
                    elif type(item) == Dvd:
                            list_results.append(f'title : {item.title},Type Catalog: Dvd')
                    elif type(item) == Cd:
                            list_results.append(f'title : {item.title},Type Catalog: Cd')
                    else:
                        pass
        return list_results
