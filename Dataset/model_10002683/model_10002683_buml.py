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
Actor_Actor = Class(name="Actor_Actor")
mypackage_UseCase_UseCase = Class(name="mypackage_UseCase_UseCase")
mypackage_UseCase2_UseCase = Class(name="mypackage_UseCase2_UseCase")
mypackage_UseCase3_UseCase = Class(name="mypackage_UseCase3_UseCase")
mypackage2_MyClass2 = Class(name="mypackage2_MyClass2")
mypackage3_MyClass3 = Class(name="mypackage3_MyClass3")
mypackage3_MyClass5 = Class(name="mypackage3_MyClass5")
Actor2_Actor = Class(name="Actor2_Actor")

# Actor_Actor class attributes and methods

# mypackage_UseCase_UseCase class attributes and methods

# mypackage_UseCase2_UseCase class attributes and methods

# mypackage_UseCase3_UseCase class attributes and methods

# mypackage2_MyClass2 class attributes and methods
mypackage2_MyClass2_attribute2_1: Property = Property(name="attribute2_1", type=StringType)
mypackage2_MyClass2_attribute2_2: Property = Property(name="attribute2_2", type=FloatType)
mypackage2_MyClass2.attributes={mypackage2_MyClass2_attribute2_2, mypackage2_MyClass2_attribute2_1}

# mypackage3_MyClass3 class attributes and methods
mypackage3_MyClass3_attribute3_1: Property = Property(name="attribute3_1", type=StringType)
mypackage3_MyClass3.attributes={mypackage3_MyClass3_attribute3_1}

# mypackage3_MyClass5 class attributes and methods
mypackage3_MyClass5_attribute: Property = Property(name="attribute", type=StringType)
mypackage3_MyClass5.attributes={mypackage3_MyClass5_attribute}

# Actor2_Actor class attributes and methods

# Relationships
MyClass2_MyClass3: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass3",
    ends={
        Property(name="This_is_a0", type=mypackage3_MyClass3, multiplicity=Multiplicity(0, 3)),
        Property(name="This_is_a1", type=mypackage2_MyClass2, multiplicity=Multiplicity(1, 3))
    }
)
Actor_UseCase: BinaryAssociation = BinaryAssociation(
    name="Actor_UseCase",
    ends={
        Property(name="useCase2", type=mypackage_UseCase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="actor3", type=Actor_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="cebfa942_8fee_496b_9dc6_ec4f50dc7443",
    types={Actor_Actor, mypackage_UseCase_UseCase, mypackage_UseCase2_UseCase, mypackage_UseCase3_UseCase, mypackage2_MyClass2, mypackage3_MyClass3, mypackage3_MyClass5, Actor2_Actor},
    associations={MyClass2_MyClass3, Actor_UseCase},
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