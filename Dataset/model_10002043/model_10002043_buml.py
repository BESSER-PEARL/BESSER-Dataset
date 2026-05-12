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
PolicyImage = Class(name="PolicyImage")
Class_ = Class(name="Class")
BaseBO = Class(name="BaseBO")
Location = Class(name="Location")
Location2 = Class(name="Location2")
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyInterface_Interface = Class(name="MyInterface_Interface")
mypackage2_MyClass = Class(name="mypackage2_MyClass")
mypackage2_MyInterface_Interface = Class(name="mypackage2_MyInterface_Interface")
mypackage2_MyClass2 = Class(name="mypackage2_MyClass2")
MyClass9 = Class(name="MyClass9")

# PolicyImage class attributes and methods
PolicyImage_serialVersionID: Property = Property(name="serialVersionID", type=StringType)
PolicyImage.attributes={PolicyImage_serialVersionID}

# Class class attributes and methods

# BaseBO class attributes and methods
BaseBO_testString: Property = Property(name="testString", type=StringType)
BaseBO_newInt: Property = Property(name="newInt", type=IntegerType)
BaseBO_newBool: Property = Property(name="newBool", type=BooleanType)
BaseBO.attributes={BaseBO_testString, BaseBO_newBool, BaseBO_newInt}

# Location class attributes and methods
Location_location: Property = Property(name="location", type=StringType)
Location.attributes={Location_location}

# Location2 class attributes and methods

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# MyInterface_Interface class attributes and methods

# mypackage2_MyClass class attributes and methods

# mypackage2_MyInterface_Interface class attributes and methods

# mypackage2_MyClass2 class attributes and methods

# MyClass9 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_l66JgJdSEeeaCsv2qBF4QA",
    types={PolicyImage, Class_, BaseBO, Location, Location2, MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass7, MyClass8, MyInterface_Interface, mypackage2_MyClass, mypackage2_MyInterface_Interface, mypackage2_MyClass2, MyClass9},
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