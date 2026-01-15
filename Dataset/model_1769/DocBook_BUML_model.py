####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
book_DocBook = Class(name="book::DocBook")
book_Book = Class(name="book::Book")
book_Person = Class(name="book::Person")
book_Article = Class(name="book::Article")

# book_DocBook class attributes and methods

# book_Book class attributes and methods
book_Book_title: Property = Property(name="title", type=StringType)
book_Book.attributes={book_Book_title}

# book_Person class attributes and methods
book_Person_name: Property = Property(name="name", type=StringType)
book_Person.attributes={book_Person_name}

# book_Article class attributes and methods
book_Article_title: Property = Property(name="title", type=StringType)
book_Article.attributes={book_Article_title}

# Relationships
book0: BinaryAssociation = BinaryAssociation(
    name="book0",
    ends={
        Property(name="Book", type=book_DocBook, multiplicity=Multiplicity(1, 1)),
        Property(name="docBook", type=book_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
docBook1: BinaryAssociation = BinaryAssociation(
    name="docBook1",
    ends={
        Property(name="DocBook", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=book_DocBook, multiplicity=Multiplicity(1, 1))
    }
)
editor2: BinaryAssociation = BinaryAssociation(
    name="editor2",
    ends={
        Property(name="Person", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="edited", type=book_Person, multiplicity=Multiplicity(0, 9999))
    }
)
author3: BinaryAssociation = BinaryAssociation(
    name="author3",
    ends={
        Property(name="Person4", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="authored", type=book_Person, multiplicity=Multiplicity(0, 9999))
    }
)
articles5: BinaryAssociation = BinaryAssociation(
    name="articles5",
    ends={
        Property(name="Article", type=book_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book6", type=book_Article, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="Book8", type=book_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="articles", type=book_Book, multiplicity=Multiplicity(1, 1))
    }
)
author9: BinaryAssociation = BinaryAssociation(
    name="author9",
    ends={
        Property(name="Person11", type=book_Article, multiplicity=Multiplicity(1, 1)),
        Property(name="articles10", type=book_Person, multiplicity=Multiplicity(0, 9999))
    }
)
edited12: BinaryAssociation = BinaryAssociation(
    name="edited12",
    ends={
        Property(name="Book13", type=book_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="editor", type=book_Book, multiplicity=Multiplicity(0, 9999))
    }
)
authored14: BinaryAssociation = BinaryAssociation(
    name="authored14",
    ends={
        Property(name="Book15", type=book_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=book_Book, multiplicity=Multiplicity(0, 9999))
    }
)
articles16: BinaryAssociation = BinaryAssociation(
    name="articles16",
    ends={
        Property(name="Article18", type=book_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="author17", type=book_Article, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="book",
    types={book_DocBook, book_Book, book_Person, book_Article},
    associations={book0, docBook1, editor2, author3, articles5, book7, author9, edited12, authored14, articles16},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)