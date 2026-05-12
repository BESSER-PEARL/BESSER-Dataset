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
T2 = Class(name="T2")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")

# MyClass class attributes and methods

# T class attributes and methods

# T2 class attributes and methods

# MyClass2 class attributes and methods
MyClass2_attribute: Property = Property(name="attribute", type=IntegerType)
MyClass2_attribute2: Property = Property(name="attribute2", type=StringType)
MyClass2_attribute3: Property = Property(name="attribute3", type=StringType)
MyClass2.attributes={MyClass2_attribute3, MyClass2_attribute, MyClass2_attribute2}

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# Relationships
MyClass4_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass4_MyClass2",
    ends={
        Property(name="myClass20", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass41", type=MyClass4, multiplicity=Multiplicity(0, 1))
    }
)
MyClass5_MyClass3: BinaryAssociation = BinaryAssociation(
    name="MyClass5_MyClass3",
    ends={
        Property(name="myClass32", type=MyClass3, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass53", type=MyClass5, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_z9ZEMLotEeehVczkwiTSNA",
    types={MyClass, T, T2, MyClass2, MyClass3, MyClass4, MyClass5},
    associations={MyClass4_MyClass2, MyClass5_MyClass3},
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