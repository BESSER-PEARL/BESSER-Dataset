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
Subpkg1Class1 = Class(name="Subpkg1Class1")
toppkg_TopClass1 = Class(name="toppkg::TopClass1")
toppkg_TopClass2 = Class(name="toppkg::TopClass2")
Subpkg1Class2 = Class(name="Subpkg1Class2")
toppkg_subpkg1_Subpkg1Class2 = Class(name="toppkg::subpkg1::Subpkg1Class2")
Subpkg2Class1 = Class(name="Subpkg2Class1")
toppkg_subpkg1_Subpkg1Class1 = Class(name="toppkg::subpkg1::Subpkg1Class1")
toppkg_subpkg3_Subpkg3Class1 = Class(name="toppkg::subpkg3::Subpkg3Class1")
subpkg3_Subpkg3Class2 = Class(name="subpkg3::Subpkg3Class2")
toppkg_subpkg2_Subpkg2Class1 = Class(name="toppkg::subpkg2::Subpkg2Class1")
Subpkg2Class2 = Class(name="Subpkg2Class2")
toppkg_subpkg2_Subpkg2Class2 = Class(name="toppkg::subpkg2::Subpkg2Class2")
subpkg3_Subpkg3Class1 = Class(name="subpkg3::Subpkg3Class1")
toppkg_subpkg3_Subpkg3Class2 = Class(name="toppkg::subpkg3::Subpkg3Class2")

# Subpkg1Class1 class attributes and methods

# toppkg_TopClass1 class attributes and methods

# toppkg_TopClass2 class attributes and methods

# Subpkg1Class2 class attributes and methods

# toppkg_subpkg1_Subpkg1Class2 class attributes and methods

# Subpkg2Class1 class attributes and methods

# toppkg_subpkg1_Subpkg1Class1 class attributes and methods

# toppkg_subpkg3_Subpkg3Class1 class attributes and methods

# subpkg3_Subpkg3Class2 class attributes and methods

# toppkg_subpkg2_Subpkg2Class1 class attributes and methods

# Subpkg2Class2 class attributes and methods

# toppkg_subpkg2_Subpkg2Class2 class attributes and methods

# subpkg3_Subpkg3Class1 class attributes and methods

# toppkg_subpkg3_Subpkg3Class2 class attributes and methods

# Relationships
mySubPkg1Class12: BinaryAssociation = BinaryAssociation(
    name="mySubPkg1Class12",
    ends={
        Property(name="Subpkg1Class1", type=toppkg_TopClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_TopClass1", type=Subpkg1Class1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myTopClass20: BinaryAssociation = BinaryAssociation(
    name="myTopClass20",
    ends={
        Property(name="1", type=toppkg_TopClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=toppkg_TopClass2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg1Class28: BinaryAssociation = BinaryAssociation(
    name="mySubpkg1Class28",
    ends={
        Property(name="Subpkg1Class2", type=toppkg_subpkg1_Subpkg1Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg1_Subpkg1Class1", type=Subpkg1Class2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg2Class13: BinaryAssociation = BinaryAssociation(
    name="mySubpkg2Class13",
    ends={
        Property(name="Subpkg2Class1", type=toppkg_TopClass1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_TopClass14", type=Subpkg2Class1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myTopClass15: BinaryAssociation = BinaryAssociation(
    name="myTopClass15",
    ends={
        Property(name="7", type=toppkg_TopClass2, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=toppkg_TopClass1, multiplicity=Multiplicity(0, 1))
    }
)
mySubpkg3Class211: BinaryAssociation = BinaryAssociation(
    name="mySubpkg3Class211",
    ends={
        Property(name="subpkg3_Subpkg3Class2", type=toppkg_subpkg3_Subpkg3Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg3_Subpkg3Class1", type=subpkg3_Subpkg3Class2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg2Class29: BinaryAssociation = BinaryAssociation(
    name="mySubpkg2Class29",
    ends={
        Property(name="Subpkg2Class2", type=toppkg_subpkg2_Subpkg2Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg2_Subpkg2Class1", type=Subpkg2Class2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mySubpkg3Class110: BinaryAssociation = BinaryAssociation(
    name="mySubpkg3Class110",
    ends={
        Property(name="subpkg3_Subpkg3Class1", type=toppkg_subpkg2_Subpkg2Class2, multiplicity=Multiplicity(1, 1)),
        Property(name="toppkg_subpkg2_Subpkg2Class2", type=subpkg3_Subpkg3Class1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="toppkg",
    types={Subpkg1Class1, toppkg_TopClass1, toppkg_TopClass2, Subpkg1Class2, toppkg_subpkg1_Subpkg1Class2, Subpkg2Class1, toppkg_subpkg1_Subpkg1Class1, toppkg_subpkg3_Subpkg3Class1, subpkg3_Subpkg3Class2, toppkg_subpkg2_Subpkg2Class1, Subpkg2Class2, toppkg_subpkg2_Subpkg2Class2, subpkg3_Subpkg3Class1, toppkg_subpkg3_Subpkg3Class2},
    associations={mySubPkg1Class12, myTopClass20, mySubpkg1Class28, mySubpkg2Class13, myTopClass15, mySubpkg3Class211, mySubpkg2Class29, mySubpkg3Class110},
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