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
library_Library = Class(name="library::Library")
library_Customer = Class(name="library::Customer")
library_Borrowable = Class(name="library::Borrowable", is_abstract=True)
library_Author = Class(name="library::Author")
library_CD = Class(name="library::CD")
Borrowable = Class(name="Borrowable")
library_Magazine = Class(name="library::Magazine")
library_Book = Class(name="library::Book")

# library_Library class attributes and methods
library_Library_address: Property = Property(name="address", type=StringType)
library_Library.attributes={library_Library_address}

# library_Customer class attributes and methods
library_Customer_name: Property = Property(name="name", type=StringType)
library_Customer.attributes={library_Customer_name}

# library_Borrowable class attributes and methods
library_Borrowable_title: Property = Property(name="title", type=StringType)
library_Borrowable_copiesAvailable: Property = Property(name="copiesAvailable", type=IntegerType)
library_Borrowable.attributes={library_Borrowable_copiesAvailable, library_Borrowable_title}

# library_Author class attributes and methods
library_Author_name: Property = Property(name="name", type=StringType)
library_Author.attributes={library_Author_name}

# library_CD class attributes and methods

# Borrowable class attributes and methods

# library_Magazine class attributes and methods

# library_Book class attributes and methods

# Relationships
borrowables0: BinaryAssociation = BinaryAssociation(
    name="borrowables0",
    ends={
        Property(name="Borrowable", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=library_Borrowable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
customers1: BinaryAssociation = BinaryAssociation(
    name="customers1",
    ends={
        Property(name="library_Customer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors2: BinaryAssociation = BinaryAssociation(
    name="authors2",
    ends={
        Property(name="Author", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library3", type=library_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library8: BinaryAssociation = BinaryAssociation(
    name="library8",
    ends={
        Property(name="Library10", type=library_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="authors9", type=library_Library, multiplicity=Multiplicity(0, 1))
    }
)
borrowed4: BinaryAssociation = BinaryAssociation(
    name="borrowed4",
    ends={
        Property(name="library_Borrowable", type=library_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Customer5", type=library_Borrowable, multiplicity=Multiplicity(0, 9999))
    }
)
library6: BinaryAssociation = BinaryAssociation(
    name="library6",
    ends={
        Property(name="Library", type=library_Borrowable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowables", type=library_Library, multiplicity=Multiplicity(0, 1))
    }
)
writtenBooks7: BinaryAssociation = BinaryAssociation(
    name="writtenBooks7",
    ends={
        Property(name="Book", type=library_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
authors11: BinaryAssociation = BinaryAssociation(
    name="authors11",
    ends={
        Property(name="Author12", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="writtenBooks", type=library_Author, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_library_CD_Borrowable = Generalization(general=Borrowable, specific=library_CD)
gen_library_Magazine_Borrowable = Generalization(general=Borrowable, specific=library_Magazine)
gen_library_Book_Borrowable = Generalization(general=Borrowable, specific=library_Book)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Customer, library_Borrowable, library_Author, library_CD, Borrowable, library_Magazine, library_Book},
    associations={borrowables0, customers1, authors2, library8, borrowed4, library6, writtenBooks7, authors11},
    generalizations={gen_library_CD_Borrowable, gen_library_Magazine_Borrowable, gen_library_Book_Borrowable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)