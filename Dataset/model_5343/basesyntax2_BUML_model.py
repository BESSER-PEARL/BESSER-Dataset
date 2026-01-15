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
basesyntax2_B2 = Class(name="basesyntax2::B2")

# basesyntax2_B2 class attributes and methods
basesyntax2_B2_name: Property = Property(name="name", type=StringType)
basesyntax2_B2.attributes={basesyntax2_B2_name}

# Domain Model
domain_model = DomainModel(
    name="basesyntax2",
    types={basesyntax2_B2},
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