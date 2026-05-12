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
mypackage2_MyClass = Class(name="mypackage2_MyClass")
mypackage2_MyClass2 = Class(name="mypackage2_MyClass2")
mypackage2_MyClass3 = Class(name="mypackage2_MyClass3")
mypackage2_MyClass4 = Class(name="mypackage2_MyClass4")
mypackage3_MyClass = Class(name="mypackage3_MyClass")
mypackage3_MyClass2 = Class(name="mypackage3_MyClass2")
mypackage3_MyClass3 = Class(name="mypackage3_MyClass3")
mypackage3_MyClass4 = Class(name="mypackage3_MyClass4")
mypackage4_MyClass = Class(name="mypackage4_MyClass")
mypackage4_MyClass2 = Class(name="mypackage4_MyClass2")
mypackage4_MyClass3 = Class(name="mypackage4_MyClass3")
mypackage4_MyClass4 = Class(name="mypackage4_MyClass4")
mypackage5_MyClass = Class(name="mypackage5_MyClass")
mypackage5_MyClass2 = Class(name="mypackage5_MyClass2")
mypackage5_MyClass3 = Class(name="mypackage5_MyClass3")
mypackage5_MyClass4 = Class(name="mypackage5_MyClass4")

# mypackage_MyClass class attributes and methods

# mypackage_MyClass2 class attributes and methods

# mypackage_MyClass3 class attributes and methods

# mypackage_MyClass4 class attributes and methods

# mypackage2_MyClass class attributes and methods

# mypackage2_MyClass2 class attributes and methods

# mypackage2_MyClass3 class attributes and methods

# mypackage2_MyClass4 class attributes and methods

# mypackage3_MyClass class attributes and methods

# mypackage3_MyClass2 class attributes and methods

# mypackage3_MyClass3 class attributes and methods

# mypackage3_MyClass4 class attributes and methods

# mypackage4_MyClass class attributes and methods

# mypackage4_MyClass2 class attributes and methods

# mypackage4_MyClass3 class attributes and methods

# mypackage4_MyClass4 class attributes and methods

# mypackage5_MyClass class attributes and methods

# mypackage5_MyClass2 class attributes and methods

# mypackage5_MyClass3 class attributes and methods

# mypackage5_MyClass4 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_QphcgM7qEeeLcIicqHdTUQ",
    types={mypackage_MyClass, mypackage_MyClass2, mypackage_MyClass3, mypackage_MyClass4, mypackage2_MyClass, mypackage2_MyClass2, mypackage2_MyClass3, mypackage2_MyClass4, mypackage3_MyClass, mypackage3_MyClass2, mypackage3_MyClass3, mypackage3_MyClass4, mypackage4_MyClass, mypackage4_MyClass2, mypackage4_MyClass3, mypackage4_MyClass4, mypackage5_MyClass, mypackage5_MyClass2, mypackage5_MyClass3, mypackage5_MyClass4},
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