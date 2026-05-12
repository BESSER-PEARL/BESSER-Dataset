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
A1 = Class(name="A1")
B1 = Class(name="B1")
C1 = Class(name="C1")

# A1 class attributes and methods
A1_atta: Property = Property(name="atta", type=StringType)
A1.attributes={A1_atta}

# B1 class attributes and methods
B1_attb: Property = Property(name="attb", type=IntegerType)
B1.attributes={B1_attb}

# C1 class attributes and methods
C1_attc1: Property = Property(name="attc1", type=IntegerType)
C1_attc2: Property = Property(name="attc2", type=BooleanType)
C1.attributes={C1_attc1, C1_attc2}

# Relationships
Class_Class2: BinaryAssociation = BinaryAssociation(
    name="Class_Class2",
    ends={
        Property(name="b0", type=B1, multiplicity=Multiplicity(1, 9999)),
        Property(name="a1", type=A1, multiplicity=Multiplicity(0, 1))
    }
)
B_C: BinaryAssociation = BinaryAssociation(
    name="B_C",
    ends={
        Property(name="c2", type=C1, multiplicity=Multiplicity(0, 9999)),
        Property(name="b3", type=B1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GpvnsCVwEeiYD9TOdwevwA",
    types={A1, B1, C1},
    associations={Class_Class2, B_C},
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