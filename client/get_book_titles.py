from inventory_client import InventoryClient


def getBookTitles(inventoryClient, ISBNs):
    titles = []
    for ISBN in ISBNs:
        book = inventoryClient.getBook(ISBN)
        titles.append(book.title)
    return titles


if __name__ == '__main__':
    inventoryClient = InventoryClient()
    ISBNs = ["123", "12345"]
    titles = getBookTitles(inventoryClient, ISBNs)
    print(titles)
