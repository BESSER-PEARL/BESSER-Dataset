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
            EnumerationLiteral(name="MYSTERY"),
			EnumerationLiteral(name="SCIENCE_FICTION"),
			EnumerationLiteral(name="BIOGRAPHY")
    }
)

# Classes
Library_Writer = Class(name="Library::Writer")
Library_Book = Class(name="Library::Book")
Library_Library = Class(name="Library::Library")

# Library_Writer class attributes and methods

# Library_Book class attributes and methods

# Library_Library class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Library_Writer, Library_Book, Library_Library, BookCategory},
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