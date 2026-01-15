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
basesyntax1_B1 = Class(name="basesyntax1::B1")

# basesyntax1_B1 class attributes and methods
basesyntax1_B1_name: Property = Property(name="name", type=StringType)
basesyntax1_B1.attributes={basesyntax1_B1_name}

# Domain Model
domain_model = DomainModel(
    name="basesyntax1",
    types={basesyntax1_B1},
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