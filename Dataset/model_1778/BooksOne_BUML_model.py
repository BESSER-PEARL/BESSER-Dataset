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
Books_Chapter = Class(name="Books::Chapter")
Books_System = Class(name="Books::System")
Books_Book = Class(name="Books::Book")
Books_Author = Class(name="Books::Author")

# Books_Chapter class attributes and methods
Books_Chapter_title: Property = Property(name="title", type=StringType)
Books_Chapter.attributes={Books_Chapter_title}

# Books_System class attributes and methods
Books_System_name: Property = Property(name="name", type=StringType)
Books_System.attributes={Books_System_name}

# Books_Book class attributes and methods
Books_Book_collecName: Property = Property(name="collecName", type=StringType)
Books_Book_title: Property = Property(name="title", type=StringType)
Books_Book.attributes={Books_Book_collecName, Books_Book_title}

# Books_Author class attributes and methods
Books_Author_name: Property = Property(name="name", type=StringType)
Books_Author.attributes={Books_Author_name}

# Relationships
chaps3: BinaryAssociation = BinaryAssociation(
    name="chaps3",
    ends={
        Property(name="Chapter", type=Books_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="itsbook", type=Books_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auths4: BinaryAssociation = BinaryAssociation(
    name="auths4",
    ends={
        Property(name="Author", type=Books_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="mybs", type=Books_Author, multiplicity=Multiplicity(0, 9999))
    }
)
itsbook5: BinaryAssociation = BinaryAssociation(
    name="itsbook5",
    ends={
        Property(name="Book", type=Books_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="chaps", type=Books_Book, multiplicity=Multiplicity(1, 1))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Books_Book", type=Books_System, multiplicity=Multiplicity(1, 1)),
        Property(name="Books_System", type=Books_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Books_Author", type=Books_System, multiplicity=Multiplicity(1, 1)),
        Property(name="Books_System2", type=Books_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mybs6: BinaryAssociation = BinaryAssociation(
    name="mybs6",
    ends={
        Property(name="Book7", type=Books_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="auths", type=Books_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Books",
    types={Books_Chapter, Books_System, Books_Book, Books_Author},
    associations={chaps3, auths4, itsbook5, books0, authors1, mybs6},
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