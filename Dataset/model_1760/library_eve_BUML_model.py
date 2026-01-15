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
library_Customer = Class(name="library::Customer")
library_CityLibrary = Class(name="library::CityLibrary")
library_Borrowable = Class(name="library::Borrowable", is_abstract=True)
library_borrowables_CD = Class(name="library::borrowables::CD")
Borrowable = Class(name="Borrowable")
library_borrowables_Magazine = Class(name="library::borrowables::Magazine")
library_borrowables_Book = Class(name="library::borrowables::Book")

# library_Customer class attributes and methods
library_Customer_name: Property = Property(name="name", type=StringType)
library_Customer.attributes={library_Customer_name}

# library_CityLibrary class attributes and methods
library_CityLibrary_address: Property = Property(name="address", type=StringType)
library_CityLibrary.attributes={library_CityLibrary_address}

# library_Borrowable class attributes and methods
library_Borrowable_title: Property = Property(name="title", type=StringType)
library_Borrowable_copiesAvailable: Property = Property(name="copiesAvailable", type=IntegerType)
library_Borrowable.attributes={library_Borrowable_title, library_Borrowable_copiesAvailable}

# library_borrowables_CD class attributes and methods

# Borrowable class attributes and methods

# library_borrowables_Magazine class attributes and methods

# library_borrowables_Book class attributes and methods
library_borrowables_Book_authors: Property = Property(name="authors", type=StringType)
library_borrowables_Book.attributes={library_borrowables_Book_authors}

# Relationships
customers1: BinaryAssociation = BinaryAssociation(
    name="customers1",
    ends={
        Property(name="library_Customer", type=library_CityLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="library_CityLibrary", type=library_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowables0: BinaryAssociation = BinaryAssociation(
    name="borrowables0",
    ends={
        Property(name="Borrowable", type=library_CityLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=library_Borrowable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowed2: BinaryAssociation = BinaryAssociation(
    name="borrowed2",
    ends={
        Property(name="library_Borrowable", type=library_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Customer3", type=library_Borrowable, multiplicity=Multiplicity(0, 9999))
    }
)
library4: BinaryAssociation = BinaryAssociation(
    name="library4",
    ends={
        Property(name="CityLibrary", type=library_Borrowable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowables", type=library_CityLibrary, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_library_borrowables_CD_Borrowable = Generalization(general=Borrowable, specific=library_borrowables_CD)
gen_library_borrowables_Magazine_Borrowable = Generalization(general=Borrowable, specific=library_borrowables_Magazine)
gen_library_borrowables_Book_Borrowable = Generalization(general=Borrowable, specific=library_borrowables_Book)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Customer, library_CityLibrary, library_Borrowable, library_borrowables_CD, Borrowable, library_borrowables_Magazine, library_borrowables_Book},
    associations={customers1, borrowables0, borrowed2, library4},
    generalizations={gen_library_borrowables_CD_Borrowable, gen_library_borrowables_Magazine_Borrowable, gen_library_borrowables_Book_Borrowable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)