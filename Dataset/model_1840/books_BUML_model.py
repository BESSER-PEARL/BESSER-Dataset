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
books_Bookstore = Class(name="books::Bookstore")
books_Book = Class(name="books::Book")
books_Title = Class(name="books::Title")

# books_Bookstore class attributes and methods

# books_Book class attributes and methods
books_Book_author: Property = Property(name="author", type=StringType)
books_Book_price: Property = Property(name="price", type=FloatType)
books_Book_year: Property = Property(name="year", type=StringType)
books_Book.attributes={books_Book_year, books_Book_author, books_Book_price}

# books_Title class attributes and methods
books_Title_lan: Property = Property(name="lan", type=StringType)
books_Title_text: Property = Property(name="text", type=StringType)
books_Title.attributes={books_Title_lan, books_Title_text}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="books_Book", type=books_Bookstore, multiplicity=Multiplicity(1, 1)),
        Property(name="books_Bookstore", type=books_Book, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
title1: BinaryAssociation = BinaryAssociation(
    name="title1",
    ends={
        Property(name="books_Title", type=books_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books_Book2", type=books_Title, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="books",
    types={books_Bookstore, books_Book, books_Title},
    associations={books0, title1},
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