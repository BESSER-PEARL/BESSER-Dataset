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
library_Borrowable = Class(name="library::Borrowable", is_abstract=True)
library_Customer = Class(name="library::Customer")
library_Book = Class(name="library::Book")
Borrowable = Class(name="Borrowable")
library_Magazine = Class(name="library::Magazine")
library_CD = Class(name="library::CD")

# library_Library class attributes and methods
library_Library_address: Property = Property(name="address", type=StringType)
library_Library.attributes={library_Library_address}

# library_Borrowable class attributes and methods
library_Borrowable_title: Property = Property(name="title", type=StringType)
library_Borrowable_copiesAvailable: Property = Property(name="copiesAvailable", type=IntegerType)
library_Borrowable.attributes={library_Borrowable_copiesAvailable, library_Borrowable_title}

# library_Customer class attributes and methods
library_Customer_name: Property = Property(name="name", type=StringType)
library_Customer.attributes={library_Customer_name}

# library_Book class attributes and methods
library_Book_author: Property = Property(name="author", type=StringType)
library_Book.attributes={library_Book_author}

# Borrowable class attributes and methods

# library_Magazine class attributes and methods

# library_CD class attributes and methods

# Relationships
borrowables0: BinaryAssociation = BinaryAssociation(
    name="borrowables0",
    ends={
        Property(name="Borrowable", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=library_Borrowable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library4: BinaryAssociation = BinaryAssociation(
    name="library4",
    ends={
        Property(name="Library", type=library_Borrowable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowables", type=library_Library, multiplicity=Multiplicity(0, 1))
    }
)
customers1: BinaryAssociation = BinaryAssociation(
    name="customers1",
    ends={
        Property(name="library_Customer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowed2: BinaryAssociation = BinaryAssociation(
    name="borrowed2",
    ends={
        Property(name="library_Borrowable", type=library_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Customer3", type=library_Borrowable, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_library_Book_Borrowable = Generalization(general=Borrowable, specific=library_Book)
gen_library_Magazine_Borrowable = Generalization(general=Borrowable, specific=library_Magazine)
gen_library_CD_Borrowable = Generalization(general=Borrowable, specific=library_CD)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Borrowable, library_Customer, library_Book, Borrowable, library_Magazine, library_CD},
    associations={borrowables0, library4, customers1, borrowed2},
    generalizations={gen_library_Book_Borrowable, gen_library_Magazine_Borrowable, gen_library_CD_Borrowable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)