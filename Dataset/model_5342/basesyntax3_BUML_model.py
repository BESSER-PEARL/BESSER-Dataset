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
basesyntax3_B3 = Class(name="basesyntax3::B3")

# basesyntax3_B3 class attributes and methods
basesyntax3_B3_name: Property = Property(name="name", type=StringType)
basesyntax3_B3.attributes={basesyntax3_B3_name}

# Domain Model
domain_model = DomainModel(
    name="basesyntax3",
    types={basesyntax3_B3},
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