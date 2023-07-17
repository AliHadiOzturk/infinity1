from .base import Base

class News(Base):
    def __init__(self, title, description, content, author, date, url):
        self.title = title
        self.description = description
        self.content = content
        self.author = author
        self.date = date
        self.url = url
        pass