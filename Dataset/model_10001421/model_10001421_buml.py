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
mypackage_T = Class(name="mypackage_T")
mypackage_T2 = Class(name="mypackage_T2")
mypackage_T3 = Class(name="mypackage_T3")
mypackage_T4 = Class(name="mypackage_T4")
mypackage_T5 = Class(name="mypackage_T5")
Class_ = Class(name="Class")
MyClass = Class(name="MyClass")
T = Class(name="T")
T2 = Class(name="T2")
T3 = Class(name="T3")
MyInterface_Interface = Class(name="MyInterface_Interface")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyInterface2_Interface = Class(name="MyInterface2_Interface")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyInterface3_Interface = Class(name="MyInterface3_Interface")

# mypackage_MyClass class attributes and methods

# mypackage_T class attributes and methods

# mypackage_T2 class attributes and methods

# mypackage_T3 class attributes and methods

# mypackage_T4 class attributes and methods

# mypackage_T5 class attributes and methods

# Class class attributes and methods

# MyClass class attributes and methods
MyClass_attribute: Property = Property(name="attribute", type=StringType)
MyClass_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass.attributes={MyClass_attribute, MyClass_attribute2}

# T class attributes and methods

# T2 class attributes and methods

# T3 class attributes and methods

# MyInterface_Interface class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyInterface2_Interface class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyInterface3_Interface class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_5eCEkLslEeedTfUoC_GfaA",
    types={mypackage_MyClass, mypackage_T, mypackage_T2, mypackage_T3, mypackage_T4, mypackage_T5, Class_, MyClass, T, T2, T3, MyInterface_Interface, MyClass2, MyClass3, MyInterface2_Interface, MyClass4, MyClass5, MyInterface3_Interface},
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