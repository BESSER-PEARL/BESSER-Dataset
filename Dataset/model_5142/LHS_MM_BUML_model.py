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
lhs_A = Class(name="lhs::A")
lhs_B = Class(name="lhs::B")

# lhs_A class attributes and methods
lhs_A_a: Property = Property(name="a", type=StringType)
lhs_A.attributes={lhs_A_a}

# lhs_B class attributes and methods
lhs_B_b: Property = Property(name="b", type=StringType)
lhs_B.attributes={lhs_B_b}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="lhs_B", type=lhs_A, multiplicity=Multiplicity(1, 1)),
        Property(name="lhs_A", type=lhs_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="lhs",
    types={lhs_A, lhs_B},
    associations={b0},
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