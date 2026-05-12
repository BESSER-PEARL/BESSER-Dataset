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
ttt = Class(name="ttt")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")
MyClass10 = Class(name="MyClass10")

# MyClass class attributes and methods
MyClass_attribute: Property = Property(name="attribute", type=IntegerType)
MyClass_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass.attributes={MyClass_attribute, MyClass_attribute2}

# ttt class attributes and methods

# MyClass2 class attributes and methods
MyClass2_attribute: Property = Property(name="attribute", type=StringType)
MyClass2_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass2.attributes={MyClass2_attribute, MyClass2_attribute2}

# MyClass3 class attributes and methods
MyClass3_attribute: Property = Property(name="attribute", type=StringType)
MyClass3_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass3.attributes={MyClass3_attribute2, MyClass3_attribute}

# MyClass4 class attributes and methods
MyClass4_attribute: Property = Property(name="attribute", type=StringType)
MyClass4_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass4.attributes={MyClass4_attribute2, MyClass4_attribute}

# MyClass5 class attributes and methods
MyClass5_attribute: Property = Property(name="attribute", type=StringType)
MyClass5_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass5.attributes={MyClass5_attribute2, MyClass5_attribute}

# MyClass6 class attributes and methods
MyClass6_attribute: Property = Property(name="attribute", type=StringType)
MyClass6_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass6.attributes={MyClass6_attribute2, MyClass6_attribute}

# MyClass7 class attributes and methods
MyClass7_attribute: Property = Property(name="attribute", type=StringType)
MyClass7_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass7.attributes={MyClass7_attribute, MyClass7_attribute2}

# MyClass8 class attributes and methods
MyClass8_attribute: Property = Property(name="attribute", type=StringType)
MyClass8_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass8.attributes={MyClass8_attribute, MyClass8_attribute2}

# MyClass9 class attributes and methods
MyClass9_attribute: Property = Property(name="attribute", type=StringType)
MyClass9_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass9.attributes={MyClass9_attribute, MyClass9_attribute2}

# MyClass10 class attributes and methods
MyClass10_attribute: Property = Property(name="attribute", type=StringType)
MyClass10_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass10.attributes={MyClass10_attribute2, MyClass10_attribute}

# Domain Model
domain_model = DomainModel(
    name="_xSclEM9tEeWPJPZdFHJFGg",
    types={MyClass, ttt, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass7, MyClass8, MyClass9, MyClass10},
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