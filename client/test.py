# Description: Unit test for getBookTitles using mock server and live server
import unittest
import os
import sys
from unittest.mock import patch
from get_book_titles import getBookTitles
from inventory_client import InventoryClient

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../service'))
from service import book_pb2


class TestInventoryClient(unittest.TestCase):
    # unit test for getBookTitles using mock server
    @patch('client.inventory_client.InventoryClient')
    def test_inventory_client_mock(self, InventoryClient):
        InventoryClient.getBook = self.mock_get_book
        response = getBookTitles(InventoryClient, ["123", "12345"])
        self.assertEqual(response, ["The Great Gatsby", "Les Misérables"])

    # unit test for getBookTitles using live server
    def test_inventory_client(self):
        client = InventoryClient()
        response = getBookTitles(client, ["123", "12345"])
        self.assertEqual(response, ["The Great Gatsby", "Les Misérables"])

    # mock server for getBook
    def mock_get_book(self, ISBN):
        books = {"123": book_pb2.Book(ISBN="123", title="The Great Gatsby", author="F. Scott Fitzgerald", genre=0,
                                      publishing_year=1925),
                 "12345": book_pb2.Book(ISBN="12345", title="Les Misérables", author="Victor Hugo", genre=0,
                                        publishing_year=1862)}

        if ISBN in books:
            return books[ISBN]


if __name__ == '__main__':
    unittest.main()
