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
Enum1: Enumeration = Enumeration(
    name="Enum1",
    literals={
            EnumerationLiteral(name="LITERAL0"),
			EnumerationLiteral(name="LITERAL1")
    }
)

# Classes
testenums_Root = Class(name="testenums::Root")

# testenums_Root class attributes and methods
testenums_Root_enum: Property = Property(name="enum", type=StringType)
testenums_Root_enums: Property = Property(name="enums", type=StringType)
testenums_Root.attributes={testenums_Root_enums, testenums_Root_enum}

# Domain Model
domain_model = DomainModel(
    name="testenums",
    types={testenums_Root, Enum1},
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