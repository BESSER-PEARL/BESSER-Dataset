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
MetamodelInheritance_BaseContainer = Class(name="MetamodelInheritance::BaseContainer")
MetamodelInheritance_BaseContaineeA = Class(name="MetamodelInheritance::BaseContaineeA")
MetamodelInheritance_BaseContaineeB = Class(name="MetamodelInheritance::BaseContaineeB")
MetamodelInheritance_BaseContaineeC = Class(name="MetamodelInheritance::BaseContaineeC")

# MetamodelInheritance_BaseContainer class attributes and methods

# MetamodelInheritance_BaseContaineeA class attributes and methods

# MetamodelInheritance_BaseContaineeB class attributes and methods

# MetamodelInheritance_BaseContaineeC class attributes and methods

# Relationships
baseA0: BinaryAssociation = BinaryAssociation(
    name="baseA0",
    ends={
        Property(name="MetamodelInheritance_BaseContaineeA", type=MetamodelInheritance_BaseContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance_BaseContainer", type=MetamodelInheritance_BaseContaineeA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseB1: BinaryAssociation = BinaryAssociation(
    name="baseB1",
    ends={
        Property(name="MetamodelInheritance_BaseContaineeB", type=MetamodelInheritance_BaseContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance_BaseContainer2", type=MetamodelInheritance_BaseContaineeB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseC3: BinaryAssociation = BinaryAssociation(
    name="baseC3",
    ends={
        Property(name="MetamodelInheritance_BaseContaineeC", type=MetamodelInheritance_BaseContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="MetamodelInheritance_BaseContainer4", type=MetamodelInheritance_BaseContaineeC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="MetamodelInheritance",
    types={MetamodelInheritance_BaseContainer, MetamodelInheritance_BaseContaineeA, MetamodelInheritance_BaseContaineeB, MetamodelInheritance_BaseContaineeC},
    associations={baseA0, baseB1, baseC3},
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