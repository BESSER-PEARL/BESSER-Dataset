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
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")
MyClass10 = Class(name="MyClass10")
MyClass11 = Class(name="MyClass11")
MyInterface_Interface = Class(name="MyInterface_Interface")
MyClass12 = Class(name="MyClass12")
MyClass13 = Class(name="MyClass13")
MyClass14 = Class(name="MyClass14")
MyClass15 = Class(name="MyClass15")
MyClass16 = Class(name="MyClass16")
MyClass17 = Class(name="MyClass17")
MyClass18 = Class(name="MyClass18")
MyClass19 = Class(name="MyClass19")

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# MyClass9 class attributes and methods

# MyClass10 class attributes and methods

# MyClass11 class attributes and methods

# MyInterface_Interface class attributes and methods

# MyClass12 class attributes and methods
MyClass12_attribute: Property = Property(name="attribute", type=StringType)
MyClass12.attributes={MyClass12_attribute}

# MyClass13 class attributes and methods

# MyClass14 class attributes and methods

# MyClass15 class attributes and methods

# MyClass16 class attributes and methods

# MyClass17 class attributes and methods

# MyClass18 class attributes and methods
MyClass18_attribute: Property = Property(name="attribute", type=StringType)
MyClass18.attributes={MyClass18_attribute}

# MyClass19 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="__kiZkK_bEee6S77dw3LIvQ",
    types={MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass7, MyClass8, MyClass9, MyClass10, MyClass11, MyInterface_Interface, MyClass12, MyClass13, MyClass14, MyClass15, MyClass16, MyClass17, MyClass18, MyClass19},
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