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
MyInterface_Interface = Class(name="MyInterface_Interface")
MyClass6 = Class(name="MyClass6")
MyInterface2_Interface = Class(name="MyInterface2_Interface")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")
MyClass10 = Class(name="MyClass10")
MyClass11 = Class(name="MyClass11")
MyClass12 = Class(name="MyClass12")
MyClass13 = Class(name="MyClass13")
MyClass14 = Class(name="MyClass14")
MyClass15 = Class(name="MyClass15")
MyInterface3_Interface = Class(name="MyInterface3_Interface")

# MyClass class attributes and methods
MyClass_asdasda__: Property = Property(name="asdasda__", type=StringType)
MyClass.attributes={MyClass_asdasda__}

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyInterface_Interface class attributes and methods

# MyClass6 class attributes and methods

# MyInterface2_Interface class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# MyClass9 class attributes and methods

# MyClass10 class attributes and methods

# MyClass11 class attributes and methods

# MyClass12 class attributes and methods

# MyClass13 class attributes and methods

# MyClass14 class attributes and methods

# MyClass15 class attributes and methods

# MyInterface3_Interface class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_TTjf4HYAEeeZ3IbHHpTTiA",
    types={MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyInterface_Interface, MyClass6, MyInterface2_Interface, MyClass7, MyClass8, MyClass9, MyClass10, MyClass11, MyClass12, MyClass13, MyClass14, MyClass15, MyInterface3_Interface},
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