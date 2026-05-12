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
Sprite = Class(name="Sprite")
MyClass2 = Class(name="MyClass2")
MyClass = Class(name="MyClass")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyInterface_Interface = Class(name="MyInterface_Interface")
MyInterface2_Interface = Class(name="MyInterface2_Interface")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")

# Sprite class attributes and methods
Sprite_ID: Property = Property(name="ID", type=StringType)
Sprite.attributes={Sprite_ID}

# MyClass2 class attributes and methods

# MyClass class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyInterface_Interface class attributes and methods

# MyInterface2_Interface class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_NO68IK6kEee6S77dw3LIvQ",
    types={Sprite, MyClass2, MyClass, MyClass3, MyClass4, MyClass5, MyInterface_Interface, MyInterface2_Interface, MyClass6, MyClass7, MyClass8},
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