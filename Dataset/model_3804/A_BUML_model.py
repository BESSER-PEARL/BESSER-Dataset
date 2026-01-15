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
A_A1 = Class(name="A::A1")
A_A2 = Class(name="A::A2")
A_A3 = Class(name="A::A3")

# A_A1 class attributes and methods

# A_A2 class attributes and methods
A_A2_f: Property = Property(name="f", type=StringType)
A_A2.attributes={A_A2_f}

# A_A3 class attributes and methods

# Relationships
assoc0: BinaryAssociation = BinaryAssociation(
    name="assoc0",
    ends={
        Property(name="A_A2", type=A_A1, multiplicity=Multiplicity(1, 1)),
        Property(name="A_A1", type=A_A2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="A",
    types={A_A1, A_A2, A_A3},
    associations={assoc0},
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