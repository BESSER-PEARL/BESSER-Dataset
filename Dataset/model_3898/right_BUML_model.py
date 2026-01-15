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
            
    }
)

# Classes
extlibrary_Book = Class(name="extlibrary::Book")
extlibrary_Item = Class(name="extlibrary::Item", is_abstract=True)
extlibrary_Borrowable = Class(name="extlibrary::Borrowable", is_abstract=True)
extlibrary_Borrower = Class(name="extlibrary::Borrower")

# extlibrary_Book class attributes and methods

# extlibrary_Item class attributes and methods

# extlibrary_Borrowable class attributes and methods

# extlibrary_Borrower class attributes and methods

# Relationships
borrowed0: BinaryAssociation = BinaryAssociation(
    name="borrowed0",
    ends={
        Property(name="extlibrary_Borrowable", type=extlibrary_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Borrower", type=extlibrary_Borrowable, multiplicity=Multiplicity(0, 9999))
    }
)
containmentBorrowed1: BinaryAssociation = BinaryAssociation(
    name="containmentBorrowed1",
    ends={
        Property(name="extlibrary_Borrowable3", type=extlibrary_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Borrower2", type=extlibrary_Borrowable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="extlibrary",
    types={extlibrary_Book, extlibrary_Item, extlibrary_Borrowable, extlibrary_Borrower, BookCategory},
    associations={borrowed0, containmentBorrowed1},
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