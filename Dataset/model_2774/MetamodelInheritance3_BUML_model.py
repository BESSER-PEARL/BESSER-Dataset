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
MetamodelInheritance3_ChildC = Class(name="MetamodelInheritance3::ChildC")
BaseContaineeC = Class(name="BaseContaineeC")
MetamodelInheritance3_ChildD = Class(name="MetamodelInheritance3::ChildD")
ChildContaineeD = Class(name="ChildContaineeD")
MetamodelInheritance3_BaseContaineeA = Class(name="MetamodelInheritance3::BaseContaineeA")

# MetamodelInheritance3_ChildC class attributes and methods

# BaseContaineeC class attributes and methods

# MetamodelInheritance3_ChildD class attributes and methods

# ChildContaineeD class attributes and methods

# MetamodelInheritance3_BaseContaineeA class attributes and methods

# Relationships
d0: BinaryAssociation = BinaryAssociation(
    name="d0",
    ends={
        Property(name="ChildD", type=MetamodelInheritance3_ChildC, multiplicity=Multiplicity(1, 1)),
        Property(name="c", type=MetamodelInheritance3_ChildD, multiplicity=Multiplicity(0, 9999))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="ChildC", type=MetamodelInheritance3_ChildD, multiplicity=Multiplicity(1, 1)),
        Property(name="d", type=MetamodelInheritance3_ChildC, multiplicity=Multiplicity(0, 9999))
    }
)
a2: BinaryAssociation = BinaryAssociation(
    name="a2",
    ends={
        Property(name="MetamodelInheritance3_BaseContaineeA", type=MetamodelInheritance3_ChildD, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance3_ChildD", type=MetamodelInheritance3_BaseContaineeA, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_MetamodelInheritance3_ChildC_BaseContaineeC = Generalization(general=BaseContaineeC, specific=MetamodelInheritance3_ChildC)
gen_MetamodelInheritance3_ChildD_ChildContaineeD = Generalization(general=ChildContaineeD, specific=MetamodelInheritance3_ChildD)

# Domain Model
domain_model = DomainModel(
    name="MetamodelInheritance3",
    types={MetamodelInheritance3_ChildC, BaseContaineeC, MetamodelInheritance3_ChildD, ChildContaineeD, MetamodelInheritance3_BaseContaineeA},
    associations={d0, c1, a2},
    generalizations={gen_MetamodelInheritance3_ChildC_BaseContaineeC, gen_MetamodelInheritance3_ChildD_ChildContaineeD},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)