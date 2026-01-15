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
Library_Library = Class(name="Library::Library")
Library_Cards = Class(name="Library::Cards")

# Library_Library class attributes and methods

# Library_Cards class attributes and methods

# Relationships
cards0: BinaryAssociation = BinaryAssociation(
    name="cards0",
    ends={
        Property(name="Library_Cards", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library", type=Library_Cards, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Library_Library, Library_Cards},
    associations={cards0},
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