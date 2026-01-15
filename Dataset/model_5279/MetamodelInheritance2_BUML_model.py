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
MetamodelInheritance2_ChildA = Class(name="MetamodelInheritance2::ChildA")
BaseContaineeA = Class(name="BaseContaineeA")
MetamodelInheritance2_ChildB = Class(name="MetamodelInheritance2::ChildB")
MetamodelInheritance2_ChildContaineeD = Class(name="MetamodelInheritance2::ChildContaineeD")
MetamodelInheritance2_BaseContaineeC = Class(name="MetamodelInheritance2::BaseContaineeC")
BaseContaineeB = Class(name="BaseContaineeB")

# MetamodelInheritance2_ChildA class attributes and methods

# BaseContaineeA class attributes and methods

# MetamodelInheritance2_ChildB class attributes and methods

# MetamodelInheritance2_ChildContaineeD class attributes and methods

# MetamodelInheritance2_BaseContaineeC class attributes and methods

# BaseContaineeB class attributes and methods

# Relationships
a5: BinaryAssociation = BinaryAssociation(
    name="a5",
    ends={
        Property(name="MetamodelInheritance2_ChildA7", type=MetamodelInheritance2_ChildB, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance2_ChildB6", type=MetamodelInheritance2_ChildA, multiplicity=Multiplicity(0, 9999))
    }
)
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="MetamodelInheritance2_ChildB", type=MetamodelInheritance2_ChildA, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance2_ChildA", type=MetamodelInheritance2_ChildB, multiplicity=Multiplicity(0, 9999))
    }
)
childD1: BinaryAssociation = BinaryAssociation(
    name="childD1",
    ends={
        Property(name="MetamodelInheritance2_ChildContaineeD", type=MetamodelInheritance2_ChildA, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance2_ChildA2", type=MetamodelInheritance2_ChildContaineeD, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="MetamodelInheritance2_BaseContaineeC", type=MetamodelInheritance2_ChildA, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance2_ChildA4", type=MetamodelInheritance2_BaseContaineeC, multiplicity=Multiplicity(0, 9999))
    }
)
d8: BinaryAssociation = BinaryAssociation(
    name="d8",
    ends={
        Property(name="MetamodelInheritance2_ChildContaineeD10", type=MetamodelInheritance2_ChildB, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance2_ChildB9", type=MetamodelInheritance2_ChildContaineeD, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_MetamodelInheritance2_ChildA_BaseContaineeA = Generalization(general=BaseContaineeA, specific=MetamodelInheritance2_ChildA)
gen_MetamodelInheritance2_ChildB_BaseContaineeB = Generalization(general=BaseContaineeB, specific=MetamodelInheritance2_ChildB)

# Domain Model
domain_model = DomainModel(
    name="MetamodelInheritance2",
    types={MetamodelInheritance2_ChildA, BaseContaineeA, MetamodelInheritance2_ChildB, MetamodelInheritance2_ChildContaineeD, MetamodelInheritance2_BaseContaineeC, BaseContaineeB},
    associations={a5, b0, childD1, c3, d8},
    generalizations={gen_MetamodelInheritance2_ChildA_BaseContaineeA, gen_MetamodelInheritance2_ChildB_BaseContaineeB},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)