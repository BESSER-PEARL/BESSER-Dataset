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
mypackage_MyClass = Class(name="mypackage_MyClass")
mypackage_MyClass2 = Class(name="mypackage_MyClass2")
mypackage_MyClass3 = Class(name="mypackage_MyClass3")
mypackage_MyClass4 = Class(name="mypackage_MyClass4")
mypackage_MyClass5 = Class(name="mypackage_MyClass5")
mypackage_MyClass6 = Class(name="mypackage_MyClass6")
mypackage_MyClass7 = Class(name="mypackage_MyClass7")
mypackage_MyClass8 = Class(name="mypackage_MyClass8")
mypackage_MyClass9 = Class(name="mypackage_MyClass9")
mypackage_MyClass10 = Class(name="mypackage_MyClass10")
mypackage_MyClass11 = Class(name="mypackage_MyClass11")
mypackage_MyClass12 = Class(name="mypackage_MyClass12")
mypackage_MyClass13 = Class(name="mypackage_MyClass13")
mypackage_MyClass14 = Class(name="mypackage_MyClass14")
mypackage_MyClass15 = Class(name="mypackage_MyClass15")
mypackage_MyClass16 = Class(name="mypackage_MyClass16")
mypackage_MyClass17 = Class(name="mypackage_MyClass17")
mypackage_MyClass18 = Class(name="mypackage_MyClass18")
mypackage_MyClass19 = Class(name="mypackage_MyClass19")
mypackage_MyClass20 = Class(name="mypackage_MyClass20")

# mypackage_MyClass class attributes and methods
mypackage_MyClass_haarfarbe: Property = Property(name="haarfarbe", type=StringType)
mypackage_MyClass.attributes={mypackage_MyClass_haarfarbe}

# mypackage_MyClass2 class attributes and methods

# mypackage_MyClass3 class attributes and methods

# mypackage_MyClass4 class attributes and methods

# mypackage_MyClass5 class attributes and methods

# mypackage_MyClass6 class attributes and methods

# mypackage_MyClass7 class attributes and methods

# mypackage_MyClass8 class attributes and methods

# mypackage_MyClass9 class attributes and methods

# mypackage_MyClass10 class attributes and methods

# mypackage_MyClass11 class attributes and methods

# mypackage_MyClass12 class attributes and methods

# mypackage_MyClass13 class attributes and methods

# mypackage_MyClass14 class attributes and methods

# mypackage_MyClass15 class attributes and methods

# mypackage_MyClass16 class attributes and methods

# mypackage_MyClass17 class attributes and methods

# mypackage_MyClass18 class attributes and methods

# mypackage_MyClass19 class attributes and methods

# mypackage_MyClass20 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_24LpMNN6EeehRMl7r1_c5g",
    types={mypackage_MyClass, mypackage_MyClass2, mypackage_MyClass3, mypackage_MyClass4, mypackage_MyClass5, mypackage_MyClass6, mypackage_MyClass7, mypackage_MyClass8, mypackage_MyClass9, mypackage_MyClass10, mypackage_MyClass11, mypackage_MyClass12, mypackage_MyClass13, mypackage_MyClass14, mypackage_MyClass15, mypackage_MyClass16, mypackage_MyClass17, mypackage_MyClass18, mypackage_MyClass19, mypackage_MyClass20},
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