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
T = Class(name="T")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
T1 = Class(name="T1")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")

# MyClass class attributes and methods
MyClass_attribute: Property = Property(name="attribute", type=StringType)
MyClass_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass_attribute3: Property = Property(name="attribute3", type=StringType)
MyClass_attribute4: Property = Property(name="attribute4", type=StringType)
MyClass.attributes={MyClass_attribute4, MyClass_attribute, MyClass_attribute3, MyClass_attribute2}

# T class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods
MyClass5_attribute: Property = Property(name="attribute", type=StringType)
MyClass5_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass5.attributes={MyClass5_attribute, MyClass5_attribute2}

# T1 class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# MyClass9 class attributes and methods

# Relationships
MyClass_MyClass8: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass8",
    ends={
        Property(name="myClass80", type=MyClass8, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass1", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jxYAEG2jEeeCSaocM3J_ZQ",
    types={MyClass, T, MyClass2, MyClass3, MyClass4, MyClass5, T1, MyClass6, MyClass7, MyClass8, MyClass9},
    associations={MyClass_MyClass8},
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