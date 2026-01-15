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
lib_Cafeteria = Class(name="lib::Cafeteria")
lib_Library = Class(name="lib::Library")
lib_Book = Class(name="lib::Book")
lib_Address = Class(name="lib::Address")
lib_Person = Class(name="lib::Person")

# lib_Cafeteria class attributes and methods
lib_Cafeteria_name: Property = Property(name="name", type=StringType)
lib_Cafeteria.attributes={lib_Cafeteria_name}

# lib_Library class attributes and methods
lib_Library_name: Property = Property(name="name", type=StringType)
lib_Library.attributes={lib_Library_name}

# lib_Book class attributes and methods
lib_Book_title: Property = Property(name="title", type=StringType)
lib_Book.attributes={lib_Book_title}

# lib_Address class attributes and methods
lib_Address_postalCode: Property = Property(name="postalCode", type=StringType)
lib_Address.attributes={lib_Address_postalCode}

# lib_Person class attributes and methods
lib_Person_name: Property = Property(name="name", type=StringType)
lib_Person.attributes={lib_Person_name}

# Relationships
writers3: BinaryAssociation = BinaryAssociation(
    name="writers3",
    ends={
        Property(name="Person", type=lib_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=lib_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cafeteria4: BinaryAssociation = BinaryAssociation(
    name="cafeteria4",
    ends={
        Property(name="Cafeteria", type=lib_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library5", type=lib_Cafeteria, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
library6: BinaryAssociation = BinaryAssociation(
    name="library6",
    ends={
        Property(name="Library", type=lib_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=lib_Library, multiplicity=Multiplicity(0, 1))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="lib_Book", type=lib_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="lib_Library", type=lib_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address1: BinaryAssociation = BinaryAssociation(
    name="address1",
    ends={
        Property(name="lib_Address", type=lib_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="lib_Library2", type=lib_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
library7: BinaryAssociation = BinaryAssociation(
    name="library7",
    ends={
        Property(name="Library8", type=lib_Cafeteria, multiplicity=Multiplicity(1, 1)),
        Property(name="cafeteria", type=lib_Library, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="lib",
    types={lib_Cafeteria, lib_Library, lib_Book, lib_Address, lib_Person},
    associations={writers3, cafeteria4, library6, books0, address1, library7},
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