import datetime 

class Book:
    def __init__(self, title, author, pages, publish_date, description, isbn):
        self.title = title,
        self.author = author,
        self.pages = pages,
        self.publish_date = publish_date,
        self.description = description,
        self.isbn = isbn
    
        def to_json(self):
            return {
                "title": self.title,
                "autor": self.author,
                "pages": self.pages,
                "publish_date": datetime.datetime.strptime(str(self.publish_date), "%Y-%m-%d"),
                "description": self.description,
                "isbn": self.isbn
            }