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

# Enumerations
PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="initial")
    }
)

# Classes
compositestates_Region = Class(name="compositestates::Region")
NamedElement = Class(name="NamedElement")
compositestates_AbstractState = Class(name="compositestates::AbstractState", is_abstract=True)
compositestates_State = Class(name="compositestates::State")
AbstractState = Class(name="AbstractState")
compositestates_Transition = Class(name="compositestates::Transition")
compositestates_Pseudostate = Class(name="compositestates::Pseudostate")
compositestates_NamedElement = Class(name="compositestates::NamedElement", is_abstract=True)

# compositestates_Region class attributes and methods
compositestates_Region_m_initRegion: Method = Method(name="initRegion", parameters={Parameter(name='context')})
compositestates_Region.methods={compositestates_Region_m_initRegion}

# NamedElement class attributes and methods

# compositestates_AbstractState class attributes and methods

# compositestates_State class attributes and methods
compositestates_State_m_evalState: Method = Method(name="evalState", parameters={Parameter(name='context')})
compositestates_State.methods={compositestates_State_m_evalState}

# AbstractState class attributes and methods

# compositestates_Transition class attributes and methods

# compositestates_Pseudostate class attributes and methods
compositestates_Pseudostate_kind: Property = Property(name="kind", type=StringType)
compositestates_Pseudostate.attributes={compositestates_Pseudostate_kind}

# compositestates_NamedElement class attributes and methods
compositestates_NamedElement_name: Property = Property(name="name", type=StringType)
compositestates_NamedElement.attributes={compositestates_NamedElement_name}

# Relationships
subvertex0: BinaryAssociation = BinaryAssociation(
    name="subvertex0",
    ends={
        Property(name="1", type=compositestates_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=compositestates_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerState2: BinaryAssociation = BinaryAssociation(
    name="ownerState2",
    ends={
        Property(name="4", type=compositestates_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=compositestates_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedRegions5: BinaryAssociation = BinaryAssociation(
    name="ownedRegions5",
    ends={
        Property(name="7", type=compositestates_State, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=compositestates_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="10", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=compositestates_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="13", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=compositestates_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion14: BinaryAssociation = BinaryAssociation(
    name="ownerRegion14",
    ends={
        Property(name="16", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=compositestates_Region, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="19", type=compositestates_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="22", type=compositestates_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_compositestates_Region_NamedElement = Generalization(general=NamedElement, specific=compositestates_Region)
gen_compositestates_State_AbstractState = Generalization(general=AbstractState, specific=compositestates_State)
gen_compositestates_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=compositestates_Pseudostate)

# Domain Model
domain_model = DomainModel(
    name="compositestates",
    types={compositestates_Region, NamedElement, compositestates_AbstractState, compositestates_State, AbstractState, compositestates_Transition, compositestates_Pseudostate, compositestates_NamedElement, PseudostateKind},
    associations={subvertex0, ownerState2, ownedRegions5, incoming8, outgoing11, ownerRegion14, source17, target20},
    generalizations={gen_compositestates_Region_NamedElement, gen_compositestates_State_AbstractState, gen_compositestates_Pseudostate_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)