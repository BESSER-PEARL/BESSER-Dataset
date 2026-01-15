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
statesmodel_StatesModel = Class(name="statesmodel::StatesModel")
statesmodel_State = Class(name="statesmodel::State")
statesmodel_Transition = Class(name="statesmodel::Transition")
statesmodel_ValueSnapshot = Class(name="statesmodel::ValueSnapshot")
statesmodel_ActivityNodeExecution = Class(name="statesmodel::ActivityNodeExecution")

# statesmodel_StatesModel class attributes and methods

# statesmodel_State class attributes and methods

# statesmodel_Transition class attributes and methods

# statesmodel_ValueSnapshot class attributes and methods

# statesmodel_ActivityNodeExecution class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statesmodel_State", type=statesmodel_StatesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesmodel_StatesModel", type=statesmodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statesmodel_Transition", type=statesmodel_StatesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="statesmodel_StatesModel2", type=statesmodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
snapshots3: BinaryAssociation = BinaryAssociation(
    name="snapshots3",
    ends={
        Property(name="statesmodel_ValueSnapshot", type=statesmodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statesmodel_State4", type=statesmodel_ValueSnapshot, multiplicity=Multiplicity(0, 9999))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="statesmodel_State7", type=statesmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statesmodel_Transition6", type=statesmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="statesmodel_State10", type=statesmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statesmodel_Transition9", type=statesmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
event11: BinaryAssociation = BinaryAssociation(
    name="event11",
    ends={
        Property(name="statesmodel_ActivityNodeExecution", type=statesmodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statesmodel_Transition12", type=statesmodel_ActivityNodeExecution, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statesmodel",
    types={statesmodel_StatesModel, statesmodel_State, statesmodel_Transition, statesmodel_ValueSnapshot, statesmodel_ActivityNodeExecution},
    associations={states0, transitions1, snapshots3, source5, target8, event11},
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