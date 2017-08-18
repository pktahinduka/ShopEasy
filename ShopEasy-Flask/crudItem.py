import item

class createdItem:
    def __init__(self):
        self.items = {}
        self.last_item_id = 0

    def add_movie(self, movie):
        self.last_item_id += 1
        self.items[self.last_item_id] = item
        movie._id = self.last_item_id

    def delete_item(self, item_id):
        del self.items[item_id]

    def get_item(self, item_id):
        return self.items[item_id]

    def get_items(self):
        return self.items