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
hfsm_AbstractState = Class(name="hfsm::AbstractState")
hfsm_State = Class(name="hfsm::State")
AbstractState = Class(name="AbstractState")
hfsm_Region = Class(name="hfsm::Region")
NamedElement = Class(name="NamedElement")
hfsm_Transition = Class(name="hfsm::Transition")
hfsm_NamedElement = Class(name="hfsm::NamedElement")

# hfsm_AbstractState class attributes and methods

# hfsm_State class attributes and methods

# AbstractState class attributes and methods

# hfsm_Region class attributes and methods

# NamedElement class attributes and methods

# hfsm_Transition class attributes and methods

# hfsm_NamedElement class attributes and methods
hfsm_NamedElement_name: Property = Property(name="name", type=StringType)
hfsm_NamedElement.attributes={hfsm_NamedElement_name}

# Relationships
subvertex4: BinaryAssociation = BinaryAssociation(
    name="subvertex4",
    ends={
        Property(name="AbstractState", type=hfsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerRegion", type=hfsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRegions0: BinaryAssociation = BinaryAssociation(
    name="ownedRegions0",
    ends={
        Property(name="hfsm_Region", type=hfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsm_State", type=hfsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerState1: BinaryAssociation = BinaryAssociation(
    name="ownerState1",
    ends={
        Property(name="hfsm_State3", type=hfsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsm_Region2", type=hfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=hfsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=hfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion8: BinaryAssociation = BinaryAssociation(
    name="ownerRegion8",
    ends={
        Property(name="Region", type=hfsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=hfsm_Region, multiplicity=Multiplicity(1, 1))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition", type=hfsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=hfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="outgoing", type=hfsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="AbstractState12", type=hfsm_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="AbstractState10", type=hfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=hfsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_hfsm_State_AbstractState = Generalization(general=AbstractState, specific=hfsm_State)
gen_hfsm_Region_NamedElement = Generalization(general=NamedElement, specific=hfsm_Region)
gen_hfsm_AbstractState_NamedElement = Generalization(general=NamedElement, specific=hfsm_AbstractState)
gen_hfsm_Transition_NamedElement = Generalization(general=NamedElement, specific=hfsm_Transition)

# Domain Model
domain_model = DomainModel(
    name="hfsm",
    types={hfsm_AbstractState, hfsm_State, AbstractState, hfsm_Region, NamedElement, hfsm_Transition, hfsm_NamedElement},
    associations={subvertex4, ownedRegions0, ownerState1, outgoing6, ownerRegion8, incoming5, source11, target9},
    generalizations={gen_hfsm_State_AbstractState, gen_hfsm_Region_NamedElement, gen_hfsm_AbstractState_NamedElement, gen_hfsm_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)