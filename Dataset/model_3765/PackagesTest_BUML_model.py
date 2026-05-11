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
toppkg_TopClass2 = Class(name="toppkg_TopClass2")
Subpkg1Class1 = Class(name="Subpkg1Class1")
Subpkg2Class1 = Class(name="Subpkg2Class1")
toppkg_TopClass1 = Class(name="toppkg_TopClass1")
toppkg_subpkg1_Subpkg1Class1 = Class(name="toppkg_subpkg1_Subpkg1Class1")
Subpkg1Class2 = Class(name="Subpkg1Class2")
toppkg_subpkg1_Subpkg1Class2 = Class(name="toppkg_subpkg1_Subpkg1Class2")
toppkg_subpkg2_Subpkg2Class1 = Class(name="toppkg_subpkg2_Subpkg2Class1")
Subpkg2Class2 = Class(name="Subpkg2Class2")
toppkg_subpkg2_Subpkg2Class2 = Class(name="toppkg_subpkg2_Subpkg2Class2")
subpkg3_Subpkg3Class1 = Class(name="subpkg3_Subpkg3Class1")
toppkg_subpkg3_Subpkg3Class1 = Class(name="toppkg_subpkg3_Subpkg3Class1")
subpkg3_Subpkg3Class2 = Class(name="subpkg3_Subpkg3Class2")
toppkg_subpkg3_Subpkg3Class2 = Class(name="toppkg_subpkg3_Subpkg3Class2")

# toppkg_TopClass2 class attributes and methods

# Subpkg1Class1 class attributes and methods

# Subpkg2Class1 class attributes and methods

# toppkg_TopClass1 class attributes and methods

# toppkg_subpkg1_Subpkg1Class1 class attributes and methods

# Subpkg1Class2 class attributes and methods

# toppkg_subpkg1_Subpkg1Class2 class attributes and methods

# toppkg_subpkg2_Subpkg2Class1 class attributes and methods

# Subpkg2Class2 class attributes and methods

# toppkg_subpkg2_Subpkg2Class2 class attributes and methods

# subpkg3_Subpkg3Class1 class attributes and methods

# toppkg_subpkg3_Subpkg3Class1 class attributes and methods

# subpkg3_Subpkg3Class2 class attributes and methods

# toppkg_subpkg3_Subpkg3Class2 class attributes and methods

# Relationships
myTopClass20: BinaryAssociation = BinaryAssociation(
    name="myTopClass20",
    ends={
        Property(name="TopClass2", type=toppkg_TopClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="myTopClass1", type=toppkg_TopClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubPkg1Class11: BinaryAssociation = BinaryAssociation(
    name="mySubPkg1Class11",
    ends={
        Property(name="Subpkg1Class1", type=toppkg_TopClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_TopClass1", type=Subpkg1Class1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg2Class12: BinaryAssociation = BinaryAssociation(
    name="mySubpkg2Class12",
    ends={
        Property(name="Subpkg2Class1", type=toppkg_TopClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_TopClass13", type=Subpkg2Class1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myTopClass14: BinaryAssociation = BinaryAssociation(
    name="myTopClass14",
    ends={
        Property(name="TopClass1", type=toppkg_TopClass2, multiplicity=Multiplicity(1, 1)),
        Property(name="myTopClass2", type=toppkg_TopClass1, multiplicity=Multiplicity(0, 1))
    }
)
mySubpkg1Class25: BinaryAssociation = BinaryAssociation(
    name="mySubpkg1Class25",
    ends={
        Property(name="Subpkg1Class2", type=toppkg_subpkg1_Subpkg1Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg1_Subpkg1Class1", type=Subpkg1Class2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg2Class26: BinaryAssociation = BinaryAssociation(
    name="mySubpkg2Class26",
    ends={
        Property(name="Subpkg2Class2", type=toppkg_subpkg2_Subpkg2Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg2_Subpkg2Class1", type=Subpkg2Class2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg3Class17: BinaryAssociation = BinaryAssociation(
    name="mySubpkg3Class17",
    ends={
        Property(name="subpkg3_Subpkg3Class1", type=toppkg_subpkg2_Subpkg2Class2, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg2_Subpkg2Class2", type=subpkg3_Subpkg3Class1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg3Class28: BinaryAssociation = BinaryAssociation(
    name="mySubpkg3Class28",
    ends={
        Property(name="subpkg3_Subpkg3Class2", type=toppkg_subpkg3_Subpkg3Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg3_Subpkg3Class1", type=subpkg3_Subpkg3Class2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="toppkg",
    types={toppkg_TopClass2, Subpkg1Class1, Subpkg2Class1, toppkg_TopClass1, toppkg_subpkg1_Subpkg1Class1, Subpkg1Class2, toppkg_subpkg1_Subpkg1Class2, toppkg_subpkg2_Subpkg2Class1, Subpkg2Class2, toppkg_subpkg2_Subpkg2Class2, subpkg3_Subpkg3Class1, toppkg_subpkg3_Subpkg3Class1, subpkg3_Subpkg3Class2, toppkg_subpkg3_Subpkg3Class2},
    associations={myTopClass20, mySubPkg1Class11, mySubpkg2Class12, myTopClass14, mySubpkg1Class25, mySubpkg2Class26, mySubpkg3Class17, mySubpkg3Class28},
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