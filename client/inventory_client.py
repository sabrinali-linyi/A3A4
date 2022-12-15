import grpc
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../service'))
from service import book_pb2
from service import book_pb2_grpc


class InventoryClient():
    def __init__(self):
        self.stub = book_pb2_grpc.InventoryServiceStub(grpc.insecure_channel('localhost:50051'))

    def getBook(self, ISBN):
        book = self.stub.GetBook(book_pb2.GetBookRequest(ISBN=ISBN))
        return book

    def createBook(self, book):
        mybook = book_pb2.Book(ISBN=book["ISBN"], title=book["title"], author=book["author"],
                               publishing_year=int(book["publishing_year"]))
        response = self.stub.CreateBook(mybook)
        return response
