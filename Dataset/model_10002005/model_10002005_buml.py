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

# MyClass class attributes and methods
MyClass_asdf: Property = Property(name="asdf", type=StringType)
MyClass.attributes={MyClass_asdf}

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods
MyClass3_attribute: Property = Property(name="attribute", type=StringType)
MyClass3.attributes={MyClass3_attribute}

# MyClass4 class attributes and methods

# Relationships
MyClass_MyClass3: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass3",
    ends={
        Property(name="myClass30", type=MyClass3, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass1", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)
MyClass4_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass4_MyClass2",
    ends={
        Property(name="myClass22", type=MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass43", type=MyClass4, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass3: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass3",
    ends={
        Property(name="myClass34", type=MyClass3, multiplicity=Multiplicity(0, 1)),
        Property(name="dfgd5", type=MyClass2, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyClass4: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass4",
    ends={
        Property(name="myClass46", type=MyClass4, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass7", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_inS18L5dEeedTfUoC_GfaA",
    types={MyClass, MyClass2, MyClass3, MyClass4},
    associations={MyClass_MyClass3, MyClass4_MyClass2, MyClass2_MyClass3, MyClass_MyClass4},
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