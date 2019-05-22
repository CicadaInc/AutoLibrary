from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey, create_engine
from sqlalchemy.orm import relationship, Session

Base = declarative_base()
engine = create_engine('sqlite:///:memory:')
session = Session(engine)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)

    title_id = Column(Integer, ForeignKey('title.id'))
    title = relationship("Title")

    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship("Author")

    issue_id = Column(Integer, ForeignKey('issue.id'))
    issue = relationship("Issue")

    year_id = Column(Integer, ForeignKey('year.id'))
    year = relationship("Year")


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book')


class Title(Base):
    __tablename__ = 'title'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book')


class Issue(Base):
    __tablename__ = 'issue'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book')


class Year(Base):
    __tablename__ = 'year'

    id = Column(Integer, primary_key=True)
    year = Column(Integer, unique=True)
    books = relationship('Book')


Base.metadata.create_all(engine)

if __name__ == '__main__':
    author = Author(name='Вася Пупкин')
    title = Title(name='Математика 9 класс')
    issue = Issue(name='Просвещение')
    year = Year(year='2012')

    math = Book(author=author, title=title, issue=issue, year=year)
    eng = Book(author=Author(name='No name'), title=Title(name='Eng learning'),
               issue=Issue(name='Spotlight'), year=year)

    session.add(math)
    session.add(eng)
    session.commit()

    print([book.title.name for book in year.books])
