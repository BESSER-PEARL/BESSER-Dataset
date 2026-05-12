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
Z = Class(name="Z")
Y = Class(name="Y")
R = Class(name="R")
A = Class(name="A", is_abstract=True)
B = Class(name="B")
C = Class(name="C", is_abstract=True)
C3 = Class(name="C3")
C2 = Class(name="C2")
Class_ = Class(name="Class")

# Z class attributes and methods

# Y class attributes and methods
Y_attY: Property = Property(name="attY", type=StringType)
Y.attributes={Y_attY}

# R class attributes and methods

# A class attributes and methods
A_attA: Property = Property(name="attA", type=StringType)
A.attributes={A_attA}

# B class attributes and methods
B_attB: Property = Property(name="attB", type=IntegerType)
B.attributes={B_attB}

# C class attributes and methods
C_attC1: Property = Property(name="attC1", type=IntegerType)
C_attC2: Property = Property(name="attC2", type=BooleanType)
C.attributes={C_attC2, C_attC1}

# C3 class attributes and methods

# C2 class attributes and methods

# Class class attributes and methods

# Relationships
MyClass3_MyClass4: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass4",
    ends={
        Property(name="aR0", type=A, multiplicity=Multiplicity(0, 9999)),
        Property(name="r1", type=R, multiplicity=Multiplicity(0, 1))
    }
)
MyClass4_MyClass5: BinaryAssociation = BinaryAssociation(
    name="MyClass4_MyClass5",
    ends={
        Property(name="b2", type=B, multiplicity=Multiplicity(1, 9999)),
        Property(name="a3", type=A, multiplicity=Multiplicity(0, 1))
    }
)
MyClass5_MyClass6: BinaryAssociation = BinaryAssociation(
    name="MyClass5_MyClass6",
    ends={
        Property(name="c4", type=C, multiplicity=Multiplicity(0, 9999)),
        Property(name="myClass55", type=B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ejN2kMUuEeeWu_SLkciAbg",
    types={Z, Y, R, A, B, C, C3, C2, Class_},
    associations={MyClass3_MyClass4, MyClass4_MyClass5, MyClass5_MyClass6},
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