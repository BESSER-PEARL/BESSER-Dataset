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
Test = Class(name="Test")
_ = Class(name="_")
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
mypackage2_MyInterface_Interface = Class(name="mypackage2_MyInterface_Interface")
mypackage2_MyClass = Class(name="mypackage2_MyClass")
mypackage2_MyInterface2_Interface = Class(name="mypackage2_MyInterface2_Interface")
mypackage2_MyClass2 = Class(name="mypackage2_MyClass2")
mypackage3_MyInterface_Interface = Class(name="mypackage3_MyInterface_Interface")
mypackage3_MyClass = Class(name="mypackage3_MyClass")
mypackage3_MyClass2 = Class(name="mypackage3_MyClass2")
MyClass3 = Class(name="MyClass3")
MyInterface_Interface = Class(name="MyInterface_Interface")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyInterface2_Interface = Class(name="MyInterface2_Interface")
MyInterface3_Interface = Class(name="MyInterface3_Interface")

# Test class attributes and methods

# _ class attributes and methods

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# mypackage2_MyInterface_Interface class attributes and methods

# mypackage2_MyClass class attributes and methods

# mypackage2_MyInterface2_Interface class attributes and methods

# mypackage2_MyClass2 class attributes and methods

# mypackage3_MyInterface_Interface class attributes and methods

# mypackage3_MyClass class attributes and methods

# mypackage3_MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyInterface_Interface class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyInterface2_Interface class attributes and methods

# MyInterface3_Interface class attributes and methods

# Relationships
Test__: BinaryAssociation = BinaryAssociation(
    name="Test__",
    ends={
        Property(name="_0", type=_, multiplicity=Multiplicity(0, 1)),
        Property(name="test1", type=Test, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9vFQwKoTEeeEQN1ZyOr__g",
    types={Test, _, MyClass, MyClass2, mypackage2_MyInterface_Interface, mypackage2_MyClass, mypackage2_MyInterface2_Interface, mypackage2_MyClass2, mypackage3_MyInterface_Interface, mypackage3_MyClass, mypackage3_MyClass2, MyClass3, MyInterface_Interface, MyClass4, MyClass5, MyInterface2_Interface, MyInterface3_Interface},
    associations={Test__},
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