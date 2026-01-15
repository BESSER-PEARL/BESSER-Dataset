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
Category: Enumeration = Enumeration(
    name="Category",
    literals={
            EnumerationLiteral(name="SF"),
			EnumerationLiteral(name="Polar"),
			EnumerationLiteral(name="Enfant")
    }
)

# Classes
Sample_Library = Class(name="Sample::Library")
Sample_Book = Class(name="Sample::Book")
Sample_Person = Class(name="Sample::Person")
Sample_EString = Class(name="Sample::EString")

# Sample_Library class attributes and methods
Sample_Library_name: Property = Property(name="name", type=StringType)
Sample_Library.attributes={Sample_Library_name}

# Sample_Book class attributes and methods
Sample_Book_name: Property = Property(name="name", type=StringType)
Sample_Book_category: Property = Property(name="category", type=StringType)
Sample_Book.attributes={Sample_Book_name, Sample_Book_category}

# Sample_Person class attributes and methods
Sample_Person_firstName: Property = Property(name="firstName", type=StringType)
Sample_Person_lastName: Property = Property(name="lastName", type=StringType)
Sample_Person.attributes={Sample_Person_firstName, Sample_Person_lastName}

# Sample_EString class attributes and methods

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Sample_Book", type=Sample_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Sample_Library", type=Sample_Book, multiplicity=Multiplicity(0, 9999))
    }
)
author1: BinaryAssociation = BinaryAssociation(
    name="author1",
    ends={
        Property(name="Sample_Person", type=Sample_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Sample_Book2", type=Sample_Person, multiplicity=Multiplicity(0, 1))
    }
)
string3: BinaryAssociation = BinaryAssociation(
    name="string3",
    ends={
        Property(name="Sample_EString", type=Sample_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="Sample_Book4", type=Sample_EString, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Sample",
    types={Sample_Library, Sample_Book, Sample_Person, Sample_EString, Category},
    associations={books0, author1, string3},
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