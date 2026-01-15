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
books_Catalog = Class(name="books::Catalog")
books_Book = Class(name="books::Book")
books_Writer = Class(name="books::Writer")

# books_Catalog class attributes and methods

# books_Book class attributes and methods
books_Book_isbn: Property = Property(name="isbn", type=StringType)
books_Book_title: Property = Property(name="title", type=StringType)
books_Book_pages: Property = Property(name="pages", type=IntegerType)
books_Book.attributes={books_Book_title, books_Book_isbn, books_Book_pages}

# books_Writer class attributes and methods

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="books_Book", type=books_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="books_Catalog", type=books_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="writers.ecoreWriter", type=books_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=books_Writer, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="books",
    types={books_Catalog, books_Book, books_Writer},
    associations={books0, authors1},
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