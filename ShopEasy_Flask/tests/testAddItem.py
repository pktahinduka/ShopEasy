## shopping list class
import unittest
class ShoppingListTest(unittest.TestCase):

    def setUp(self):
        self.my_list = ShoppingList() # list=[]
        self.empty_shopping_list = ShoppingList()
        self.non_empty_shopping_list = ShoppingList(['item1', 'item2', 'item3'])


    def test_add_item_to_non_empty_list(self):

    ###Test for add item to a list with items###

        self.my_list.items.append('sugar')
        self.my_list.add_item_to_shopping_list('coffee')
        self.assertEqual(self.my_list.items, ['sugar', 'coffee'], msg='Can not add items to non empty list')

    def test_add_item_to_empty_shopping_list(self):
    #"""Test for add item to an empty list"""
        self.my_list.add_item_to_shopping_list('milk')
        self.assertEqual(self.my_list.items, ['milk'], msg='Method to add item to shopping \
        list does not add it')

    def test_add_item_to_non_empty_shopping_list(self):
    #"""Test for add item to a list with items"""
        self.my_list.items.append('sugar')
        self.my_list.add_item_to_shopping_list('coffee')
        self.assertEqual(self.my_list.items, ['sugar', 'coffee'], msg='Can not add \
        items to non empty list')

class ShoppingList():
    def __init__(self, my_list=[]):
        self.items = my_list

    def add_item_to_shopping_list(self,item):
        self.items.append(item)