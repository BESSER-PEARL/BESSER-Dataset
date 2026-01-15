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
esm_Machine = Class(name="esm::Machine")
esm_State = Class(name="esm::State")
esm_Transition = Class(name="esm::Transition")
esm_EndState = Class(name="esm::EndState")
State = Class(name="State")
esm_EObject = Class(name="esm::EObject")

# esm_Machine class attributes and methods

# esm_State class attributes and methods
esm_State_name: Property = Property(name="name", type=StringType)
esm_State.attributes={esm_State_name}

# esm_Transition class attributes and methods
esm_Transition_action: Property = Property(name="action", type=StringType)
esm_Transition.attributes={esm_Transition_action}

# esm_EndState class attributes and methods

# State class attributes and methods

# esm_EObject class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="esm_State", type=esm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_Machine", type=esm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="esm_Transition", type=esm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_Machine2", type=esm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=esm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=esm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=esm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=esm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
actionImpl6: BinaryAssociation = BinaryAssociation(
    name="actionImpl6",
    ends={
        Property(name="esm_EObject", type=esm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_Transition7", type=esm_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="State", type=esm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=esm_State, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="State10", type=esm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=esm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_esm_EndState_State = Generalization(general=State, specific=esm_EndState)

# Domain Model
domain_model = DomainModel(
    name="esm",
    types={esm_Machine, esm_State, esm_Transition, esm_EndState, State, esm_EObject},
    associations={states0, transitions1, incoming3, outgoing4, actionImpl6, source8, target9},
    generalizations={gen_esm_EndState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)