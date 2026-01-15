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
fSM_Model = Class(name="fSM::Model")
fSM_EnumerationType = Class(name="fSM::EnumerationType")
fSM_FSM = Class(name="fSM::FSM")
fSM_State = Class(name="fSM::State")
fSM_EnumerationLiteral = Class(name="fSM::EnumerationLiteral")
fSM_Transition = Class(name="fSM::Transition")

# fSM_Model class attributes and methods

# fSM_EnumerationType class attributes and methods
fSM_EnumerationType_name: Property = Property(name="name", type=StringType)
fSM_EnumerationType.attributes={fSM_EnumerationType_name}

# fSM_FSM class attributes and methods

# fSM_State class attributes and methods

# fSM_EnumerationLiteral class attributes and methods
fSM_EnumerationLiteral_name: Property = Property(name="name", type=StringType)
fSM_EnumerationLiteral.attributes={fSM_EnumerationLiteral_name}

# fSM_Transition class attributes and methods

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="fSM_EnumerationType", type=fSM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_Model", type=fSM_EnumerationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm1: BinaryAssociation = BinaryAssociation(
    name="fsm1",
    ends={
        Property(name="fSM_FSM", type=fSM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_Model2", type=fSM_FSM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="fSM_EnumerationType5", type=fSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_FSM4", type=fSM_EnumerationType, multiplicity=Multiplicity(0, 1))
    }
)
ownedState6: BinaryAssociation = BinaryAssociation(
    name="ownedState6",
    ends={
        Property(name="fSM_State", type=fSM_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_FSM7", type=fSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal8: BinaryAssociation = BinaryAssociation(
    name="literal8",
    ends={
        Property(name="fSM_EnumerationLiteral", type=fSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_State9", type=fSM_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransition10: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition10",
    ends={
        Property(name="fSM_Transition", type=fSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_State11", type=fSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="fSM_State14", type=fSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_Transition13", type=fSM_State, multiplicity=Multiplicity(0, 1))
    }
)
literals15: BinaryAssociation = BinaryAssociation(
    name="literals15",
    ends={
        Property(name="fSM_EnumerationLiteral17", type=fSM_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="fSM_EnumerationType16", type=fSM_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fSM",
    types={fSM_Model, fSM_EnumerationType, fSM_FSM, fSM_State, fSM_EnumerationLiteral, fSM_Transition},
    associations={types0, fsm1, type3, ownedState6, literal8, outgoingTransition10, target12, literals15},
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