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
MyClass22 = Class(name="MyClass22")
MyClass42 = Class(name="MyClass42")
MyClass32 = Class(name="MyClass32")
MyClass6 = Class(name="MyClass6")
MyClass23 = Class(name="MyClass23")
MyClass43 = Class(name="MyClass43")
MyClass33 = Class(name="MyClass33")

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyClass22 class attributes and methods

# MyClass42 class attributes and methods

# MyClass32 class attributes and methods

# MyClass6 class attributes and methods

# MyClass23 class attributes and methods

# MyClass43 class attributes and methods

# MyClass33 class attributes and methods

# Relationships
MyClass2_MyClass: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass",
    ends={
        Property(name="myClass0", type=MyClass, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass21", type=MyClass2, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass3: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass3",
    ends={
        Property(name="MyClass2_MyClass3_02", type=MyClass3, multiplicity=Multiplicity(0, 1)),
        Property(name="MyClass2_MyClass3_13", type=MyClass2, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass4: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass4",
    ends={
        Property(name="myClass44", type=MyClass4, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass35", type=MyClass3, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass2",
    ends={
        Property(name="myClass6", type=MyClass5, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass27", type=MyClass22, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass32: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass32",
    ends={
        Property(name="MyClass2_MyClass32_08", type=MyClass32, multiplicity=Multiplicity(0, 1)),
        Property(name="MyClass2_MyClass32_19", type=MyClass22, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass42: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass42",
    ends={
        Property(name="myClass410", type=MyClass42, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass311", type=MyClass32, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass4: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass4",
    ends={
        Property(name="myClass12", type=MyClass6, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass213", type=MyClass23, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass33: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass33",
    ends={
        Property(name="MyClass2_MyClass33_014", type=MyClass33, multiplicity=Multiplicity(0, 1)),
        Property(name="MyClass2_MyClass33_115", type=MyClass23, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass43: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass43",
    ends={
        Property(name="myClass416", type=MyClass43, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass317", type=MyClass33, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_fOG08M9mEeeLcIicqHdTUQ",
    types={MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyClass22, MyClass42, MyClass32, MyClass6, MyClass23, MyClass43, MyClass33},
    associations={MyClass2_MyClass, MyClass2_MyClass3, MyClass3_MyClass4, MyClass2_MyClass2, MyClass2_MyClass32, MyClass3_MyClass42, MyClass2_MyClass4, MyClass2_MyClass33, MyClass3_MyClass43},
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