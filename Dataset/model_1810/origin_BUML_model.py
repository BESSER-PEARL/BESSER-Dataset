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

# Enumerations
BookCategory: Enumeration = Enumeration(
    name="BookCategory",
    literals={
            EnumerationLiteral(name="Encyclopedia"),
			EnumerationLiteral(name="Dictionary")
    }
)

# Classes
extlibrary_Book = Class(name="extlibrary::Book")
extlibrary_Borrowable = Class(name="extlibrary::Borrowable", is_abstract=True)
extlibrary_Borrower = Class(name="extlibrary::Borrower")

# extlibrary_Book class attributes and methods
extlibrary_Book_title: Property = Property(name="title", type=StringType)
extlibrary_Book.attributes={extlibrary_Book_title}

# extlibrary_Borrowable class attributes and methods

# extlibrary_Borrower class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="extlibrary",
    types={extlibrary_Book, extlibrary_Borrowable, extlibrary_Borrower, BookCategory},
    associations={},
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