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
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")
MyClass10 = Class(name="MyClass10")
MyClass11 = Class(name="MyClass11")
MyClass12 = Class(name="MyClass12")

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

# Relationships
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="end10", type=MyClass, multiplicity=Multiplicity(0, 1)),
        Property(name="end21", type=MyClass2, multiplicity=Multiplicity(0, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="end32", type=MyClass3, multiplicity=Multiplicity(0, 1)),
        Property(name="end43", type=MyClass4, multiplicity=Multiplicity(0, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="end54", type=MyClass5, multiplicity=Multiplicity(0, 1)),
        Property(name="end65", type=MyClass6, multiplicity=Multiplicity(0, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="end76", type=MyClass7, multiplicity=Multiplicity(0, 1)),
        Property(name="end87", type=MyClass8, multiplicity=Multiplicity(0, 9999))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="end98", type=MyClass9, multiplicity=Multiplicity(0, 1)),
        Property(name="end109", type=MyClass10, multiplicity=Multiplicity(0, 9999))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="end1110", type=MyClass11, multiplicity=Multiplicity(0, 1)),
        Property(name="end1211", type=MyClass12, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e9994542_b53f_4c36_ab46_bd170204206f",
    types={MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass7, MyClass8, MyClass9, MyClass10, MyClass11, MyClass12},
    associations={association2, association3, association4, association5, association6, association7},
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