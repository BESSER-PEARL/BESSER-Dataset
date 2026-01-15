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
hfsmReq_AbstractState = Class(name="hfsmReq::AbstractState")
hfsmReq_State = Class(name="hfsmReq::State")
AbstractState = Class(name="AbstractState")
hfsmReq_Region = Class(name="hfsmReq::Region")
NamedElement = Class(name="NamedElement")
hfsmReq_NamedElement = Class(name="hfsmReq::NamedElement")
hfsmReq_Transition = Class(name="hfsmReq::Transition")

# hfsmReq_AbstractState class attributes and methods

# hfsmReq_State class attributes and methods

# AbstractState class attributes and methods

# hfsmReq_Region class attributes and methods

# NamedElement class attributes and methods

# hfsmReq_NamedElement class attributes and methods
hfsmReq_NamedElement_name: Property = Property(name="name", type=StringType)
hfsmReq_NamedElement.attributes={hfsmReq_NamedElement_name}

# hfsmReq_Transition class attributes and methods

# Relationships
ownerState1: BinaryAssociation = BinaryAssociation(
    name="ownerState1",
    ends={
        Property(name="hfsmReq_State3", type=hfsmReq_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_Region2", type=hfsmReq_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedRegions0: BinaryAssociation = BinaryAssociation(
    name="ownedRegions0",
    ends={
        Property(name="hfsmReq_Region", type=hfsmReq_State, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_State", type=hfsmReq_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subvertex4: BinaryAssociation = BinaryAssociation(
    name="subvertex4",
    ends={
        Property(name="hfsmReq_AbstractState", type=hfsmReq_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_Region5", type=hfsmReq_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="hfsmReq_Transition", type=hfsmReq_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_AbstractState7", type=hfsmReq_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing8: BinaryAssociation = BinaryAssociation(
    name="outgoing8",
    ends={
        Property(name="hfsmReq_Transition10", type=hfsmReq_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_AbstractState9", type=hfsmReq_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion11: BinaryAssociation = BinaryAssociation(
    name="ownerRegion11",
    ends={
        Property(name="hfsmReq_Region13", type=hfsmReq_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_AbstractState12", type=hfsmReq_Region, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="hfsmReq_AbstractState16", type=hfsmReq_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_Transition15", type=hfsmReq_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="hfsmReq_AbstractState19", type=hfsmReq_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="hfsmReq_Transition18", type=hfsmReq_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_hfsmReq_State_AbstractState = Generalization(general=AbstractState, specific=hfsmReq_State)
gen_hfsmReq_Region_NamedElement = Generalization(general=NamedElement, specific=hfsmReq_Region)
gen_hfsmReq_AbstractState_NamedElement = Generalization(general=NamedElement, specific=hfsmReq_AbstractState)
gen_hfsmReq_Transition_NamedElement = Generalization(general=NamedElement, specific=hfsmReq_Transition)

# Domain Model
domain_model = DomainModel(
    name="hfsmReq",
    types={hfsmReq_AbstractState, hfsmReq_State, AbstractState, hfsmReq_Region, NamedElement, hfsmReq_NamedElement, hfsmReq_Transition},
    associations={ownerState1, ownedRegions0, subvertex4, incoming6, outgoing8, ownerRegion11, target14, source17},
    generalizations={gen_hfsmReq_State_AbstractState, gen_hfsmReq_Region_NamedElement, gen_hfsmReq_AbstractState_NamedElement, gen_hfsmReq_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)