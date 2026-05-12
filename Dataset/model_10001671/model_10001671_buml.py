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
MyClass3 = Class(name="MyClass3")
MyClass2 = Class(name="MyClass2")

# MyClass class attributes and methods

# MyClass3 class attributes and methods

# MyClass2 class attributes and methods

# Relationships
MyClass_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass2",
    ends={
        Property(name="myClass20", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass1", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyClass3: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass3",
    ends={
        Property(name="myClass32", type=MyClass3, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass3", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass2",
    ends={
        Property(name="myClass24", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass35", type=MyClass3, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass22: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass22",
    ends={
        Property(name="myClass26", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass37", type=MyClass3, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass23: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass23",
    ends={
        Property(name="myClass28", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass39", type=MyClass3, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyClass22: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass22",
    ends={
        Property(name="myClass210", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass11", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)
MyClass3_MyClass: BinaryAssociation = BinaryAssociation(
    name="MyClass3_MyClass",
    ends={
        Property(name="myClass12", type=MyClass, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass313", type=MyClass3, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_NlV94MuJEeeM1PgT03_3Vg",
    types={MyClass, MyClass3, MyClass2},
    associations={MyClass_MyClass2, MyClass_MyClass3, MyClass3_MyClass2, MyClass3_MyClass22, MyClass3_MyClass23, MyClass_MyClass22, MyClass3_MyClass},
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