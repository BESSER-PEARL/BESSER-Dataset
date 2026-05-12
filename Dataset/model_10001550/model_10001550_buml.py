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
MonoBehaviour = Class(name="MonoBehaviour")
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass9 = Class(name="MyClass9")
MyClass12 = Class(name="MyClass12")
MyClass13 = Class(name="MyClass13")
StopButton = Class(name="StopButton")
MyClass18 = Class(name="MyClass18")
MyClass19 = Class(name="MyClass19")

# MonoBehaviour class attributes and methods

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass9 class attributes and methods
MyClass9_h: Property = Property(name="h", type=IntegerType)
MyClass9.attributes={MyClass9_h}

# MyClass12 class attributes and methods

# MyClass13 class attributes and methods

# StopButton class attributes and methods

# MyClass18 class attributes and methods

# MyClass19 class attributes and methods

# Relationships
MyClass9_MyClass19: BinaryAssociation = BinaryAssociation(
    name="MyClass9_MyClass19",
    ends={
        Property(name="myClass190", type=MyClass19, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass91", type=MyClass9, multiplicity=Multiplicity(0, 1))
    }
)
MyClass19_MyClass13: BinaryAssociation = BinaryAssociation(
    name="MyClass19_MyClass13",
    ends={
        Property(name="myClass132", type=MyClass13, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass193", type=MyClass19, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_FH0OIM6NEeeMV96X50GAvA",
    types={MonoBehaviour, MyClass, MyClass2, MyClass3, MyClass4, MyClass6, MyClass7, MyClass9, MyClass12, MyClass13, StopButton, MyClass18, MyClass19},
    associations={MyClass9_MyClass19, MyClass19_MyClass13},
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