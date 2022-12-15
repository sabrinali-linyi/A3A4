from concurrent import futures
import logging

import grpc

import book_pb2_grpc
import book_pb2

books = {"123": book_pb2.Book(ISBN="123", title="The Great Gatsby", author="F. Scott Fitzgerald", genre=0,
                              publishing_year=1925),
         "12345": book_pb2.Book(ISBN="12345", title="Les Misérables", author="Victor Hugo", genre=0,
                                publishing_year=1862)}


class BookKeeper(book_pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):
        if not request.ISBN:
            return book_pb2.CreateBookResponse(Message="ISBN not found in request")

        if request.ISBN in books:
            return book_pb2.CreateBookResponse(Message="Book with given ISBN already exists")

        books[request.ISBN] = book_pb2.Book(ISBN=request.ISBN, title=request.title, author=request.author,
                                            genre=request.genre,
                                            publishing_year=request.publishing_year)

        return book_pb2.CreateBookResponse(Message="Book from ISBN %s created successfully!" % request.ISBN)

    def GetBook(self, request, context):
        if not request.ISBN:
            return book_pb2.Book(ISBN="")

        if request.ISBN not in books:
            return book_pb2.Book(ISBN="")

        return books[request.ISBN]


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_InventoryServiceServicer_to_server(BookKeeper(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
