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
l3_BuildComponent = Class(name="l3::BuildComponent")
l3_Component = Class(name="l3::Component")
l3_Metamodel = Class(name="l3::Metamodel")
l3_Model = Class(name="l3::Model")
l3_SystemModel = Class(name="l3::SystemModel")

# l3_BuildComponent class attributes and methods

# l3_Component class attributes and methods

# l3_Metamodel class attributes and methods

# l3_Model class attributes and methods

# l3_SystemModel class attributes and methods

# Relationships
base_Component0: BinaryAssociation = BinaryAssociation(
    name="base_Component0",
    ends={
        Property(name="l3_Component", type=l3_BuildComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="l3_BuildComponent", type=l3_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Model1: BinaryAssociation = BinaryAssociation(
    name="base_Model1",
    ends={
        Property(name="l3_Model", type=l3_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="l3_Metamodel", type=l3_Model, multiplicity=Multiplicity(1, 1))
    }
)
base_Model2: BinaryAssociation = BinaryAssociation(
    name="base_Model2",
    ends={
        Property(name="l3_Model3", type=l3_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="l3_SystemModel", type=l3_Model, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="l3",
    types={l3_BuildComponent, l3_Component, l3_Metamodel, l3_Model, l3_SystemModel},
    associations={base_Component0, base_Model1, base_Model2},
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