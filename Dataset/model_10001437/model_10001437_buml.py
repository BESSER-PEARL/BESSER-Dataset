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
A = Class(name="A")
B = Class(name="B")

# A class attributes and methods
A_attA: Property = Property(name="attA", type=IntegerType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# Relationships
A_B: BinaryAssociation = BinaryAssociation(
    name="A_B",
    ends={
        Property(name="A_B_00", type=B, multiplicity=Multiplicity(0, 9999)),
        Property(name="g_re1", type=A, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6LV20O1gEei9dNtZPq67hQ",
    types={A, B},
    associations={A_B},
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