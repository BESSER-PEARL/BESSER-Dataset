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
ctmc_CTMC = Class(name="ctmc::CTMC")
IDBase = Class(name="IDBase")
ctmc_State = Class(name="ctmc::State")
ctmc_Transition = Class(name="ctmc::Transition")
ctmc_Label = Class(name="ctmc::Label")

# ctmc_CTMC class attributes and methods
ctmc_CTMC_name: Property = Property(name="name", type=StringType)
ctmc_CTMC.attributes={ctmc_CTMC_name}

# IDBase class attributes and methods

# ctmc_State class attributes and methods
ctmc_State_name: Property = Property(name="name", type=StringType)
ctmc_State_exitRate: Property = Property(name="exitRate", type=FloatType)
ctmc_State.attributes={ctmc_State_name, ctmc_State_exitRate}

# ctmc_Transition class attributes and methods
ctmc_Transition_prob: Property = Property(name="prob", type=FloatType)
ctmc_Transition_rate: Property = Property(name="rate", type=FloatType)
ctmc_Transition.attributes={ctmc_Transition_prob, ctmc_Transition_rate}

# ctmc_Label class attributes and methods
ctmc_Label_name: Property = Property(name="name", type=StringType)
ctmc_Label.attributes={ctmc_Label_name}

# Relationships
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="State12", type=ctmc_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=ctmc_State, multiplicity=Multiplicity(1, 1))
    }
)
States0: BinaryAssociation = BinaryAssociation(
    name="States0",
    ends={
        Property(name="ctmc_State", type=ctmc_CTMC, multiplicity=Multiplicity(1, 1)),
        Property(name="ctmc_CTMC", type=ctmc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="ctmc_State3", type=ctmc_CTMC, multiplicity=Multiplicity(1, 1)),
        Property(name="ctmc_CTMC2", type=ctmc_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition", type=ctmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=ctmc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition6", type=ctmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=ctmc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels7: BinaryAssociation = BinaryAssociation(
    name="labels7",
    ends={
        Property(name="Label", type=ctmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=ctmc_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from8: BinaryAssociation = BinaryAssociation(
    name="from8",
    ends={
        Property(name="State", type=ctmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=ctmc_State, multiplicity=Multiplicity(1, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="State10", type=ctmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=ctmc_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ctmc_CTMC_IDBase = Generalization(general=IDBase, specific=ctmc_CTMC)
gen_ctmc_State_IDBase = Generalization(general=IDBase, specific=ctmc_State)
gen_ctmc_Transition_IDBase = Generalization(general=IDBase, specific=ctmc_Transition)
gen_ctmc_Label_IDBase = Generalization(general=IDBase, specific=ctmc_Label)

# Domain Model
domain_model = DomainModel(
    name="ctmc",
    types={ctmc_CTMC, IDBase, ctmc_State, ctmc_Transition, ctmc_Label},
    associations={state11, States0, initialState1, incoming4, outgoing5, labels7, from8, to9},
    generalizations={gen_ctmc_CTMC_IDBase, gen_ctmc_State_IDBase, gen_ctmc_Transition_IDBase, gen_ctmc_Label_IDBase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)