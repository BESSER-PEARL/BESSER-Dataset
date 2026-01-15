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
fsm_Model = Class(name="fsm::Model")
fsm_Constraint = Class(name="fsm::Constraint")
fsm_Language = Class(name="fsm::Language")
fsm_Machine = Class(name="fsm::Machine")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_Model class attributes and methods
fsm_Model_name: Property = Property(name="name", type=StringType)
fsm_Model.attributes={fsm_Model_name}

# fsm_Constraint class attributes and methods
fsm_Constraint_name: Property = Property(name="name", type=StringType)
fsm_Constraint_true: Property = Property(name="true", type=BooleanType)
fsm_Constraint.attributes={fsm_Constraint_true, fsm_Constraint_name}

# fsm_Language class attributes and methods
fsm_Language_name: Property = Property(name="name", type=StringType)
fsm_Language_target: Property = Property(name="target", type=StringType)
fsm_Language.attributes={fsm_Language_name, fsm_Language_target}

# fsm_Machine class attributes and methods

# fsm_State class attributes and methods
fsm_State_initial: Property = Property(name="initial", type=BooleanType)
fsm_State_final: Property = Property(name="final", type=BooleanType)
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name, fsm_State_initial, fsm_State_final}

# fsm_Transition class attributes and methods
fsm_Transition_event: Property = Property(name="event", type=StringType)
fsm_Transition.attributes={fsm_Transition_event}

# Relationships
constraints0: BinaryAssociation = BinaryAssociation(
    name="constraints0",
    ends={
        Property(name="fsm_Constraint", type=fsm_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Model", type=fsm_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
languages1: BinaryAssociation = BinaryAssociation(
    name="languages1",
    ends={
        Property(name="fsm_Language", type=fsm_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Model2", type=fsm_Language, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machine3: BinaryAssociation = BinaryAssociation(
    name="machine3",
    ends={
        Property(name="fsm_Machine", type=fsm_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Model4", type=fsm_Machine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="fsm_State", type=fsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Machine6", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions7: BinaryAssociation = BinaryAssociation(
    name="transitions7",
    ends={
        Property(name="fsm_Transition", type=fsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Machine8", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from9: BinaryAssociation = BinaryAssociation(
    name="from9",
    ends={
        Property(name="fsm_State11", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition10", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
to12: BinaryAssociation = BinaryAssociation(
    name="to12",
    ends={
        Property(name="fsm_State14", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition13", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Model, fsm_Constraint, fsm_Language, fsm_Machine, fsm_State, fsm_Transition},
    associations={constraints0, languages1, machine3, states5, transitions7, from9, to12},
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