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
ArtworkViewModel = Class(name="ArtworkViewModel")
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")
MyClass10 = Class(name="MyClass10")
MyClass11 = Class(name="MyClass11")
MyClass12 = Class(name="MyClass12")
MyClass13 = Class(name="MyClass13")

# ArtworkViewModel class attributes and methods

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# MyClass9 class attributes and methods

# MyClass10 class attributes and methods

# MyClass11 class attributes and methods

# MyClass12 class attributes and methods

# MyClass13 class attributes and methods

# Relationships
ArtworkViewModel_MyClass12: BinaryAssociation = BinaryAssociation(
    name="ArtworkViewModel_MyClass12",
    ends={
        Property(name="artworkViewModel1", type=ArtworkViewModel, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass120", type=MyClass12, multiplicity=Multiplicity(0, 1))
    }
)
MyClass12_MyClass6: BinaryAssociation = BinaryAssociation(
    name="MyClass12_MyClass6",
    ends={
        Property(name="myClass62", type=MyClass6, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass123", type=MyClass12, multiplicity=Multiplicity(0, 1))
    }
)
MyClass6_MyClass13: BinaryAssociation = BinaryAssociation(
    name="MyClass6_MyClass13",
    ends={
        Property(name="myClass134", type=MyClass13, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass65", type=MyClass6, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyClass12: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass12",
    ends={
        Property(name="myClass126", type=MyClass12, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass7", type=MyClass, multiplicity=Multiplicity(0, 1))
    }
)
MyClass11_MyClass: BinaryAssociation = BinaryAssociation(
    name="MyClass11_MyClass",
    ends={
        Property(name="myClass8", type=MyClass, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass119", type=MyClass11, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_rBLF0F0UEeeJB7TzzxqmtA",
    types={ArtworkViewModel, MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass7, MyClass8, MyClass9, MyClass10, MyClass11, MyClass12, MyClass13},
    associations={ArtworkViewModel_MyClass12, MyClass12_MyClass6, MyClass6_MyClass13, MyClass_MyClass12, MyClass11_MyClass},
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