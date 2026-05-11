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
compositestates_Region = Class(name="compositestates_Region")
NamedElement = Class(name="NamedElement")
compositestates_Transition = Class(name="compositestates_Transition")
compositestates_Pseudostate = Class(name="compositestates_Pseudostate")
compositestates_NamedElement = Class(name="compositestates_NamedElement", is_abstract=True)
compositestates_AbstractState = Class(name="compositestates_AbstractState", is_abstract=True)
compositestates_State = Class(name="compositestates_State")
AbstractState = Class(name="AbstractState")

# compositestates_Region class attributes and methods
compositestates_Region_m_initRegion: Method = Method(name="initRegion", parameters={Parameter(name='compositestates_context', type=StringType)})
compositestates_Region.methods={compositestates_Region_m_initRegion}

# NamedElement class attributes and methods

# compositestates_Transition class attributes and methods

# compositestates_Pseudostate class attributes and methods
compositestates_Pseudostate_kind: Property = Property(name="kind", type=StringType)
compositestates_Pseudostate.attributes={compositestates_Pseudostate_kind}

# compositestates_NamedElement class attributes and methods
compositestates_NamedElement_name: Property = Property(name="name", type=StringType)
compositestates_NamedElement.attributes={compositestates_NamedElement_name}

# compositestates_AbstractState class attributes and methods

# compositestates_State class attributes and methods
compositestates_State_m_evalState: Method = Method(name="evalState", parameters={Parameter(name='compositestates_context', type=StringType)})
compositestates_State.methods={compositestates_State_m_evalState}

# AbstractState class attributes and methods

# Relationships
ownedRegions2: BinaryAssociation = BinaryAssociation(
    name="ownedRegions2",
    ends={
        Property(name="Region", type=compositestates_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerState", type=compositestates_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=compositestates_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=compositestates_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion6: BinaryAssociation = BinaryAssociation(
    name="ownerRegion6",
    ends={
        Property(name="Region7", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=compositestates_Region, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="AbstractState9", type=compositestates_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="AbstractState11", type=compositestates_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=compositestates_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
subvertex0: BinaryAssociation = BinaryAssociation(
    name="subvertex0",
    ends={
        Property(name="AbstractState", type=compositestates_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerRegion", type=compositestates_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerState1: BinaryAssociation = BinaryAssociation(
    name="ownerState1",
    ends={
        Property(name="State", type=compositestates_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRegions", type=compositestates_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_compositestates_Region_NamedElement = Generalization(general=NamedElement, specific=compositestates_Region)
gen_compositestates_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=compositestates_Pseudostate)
gen_compositestates_State_AbstractState = Generalization(general=AbstractState, specific=compositestates_State)

# Domain Model
domain_model = DomainModel(
    name="compositestates",
    types={compositestates_Region, NamedElement, compositestates_Transition, compositestates_Pseudostate, compositestates_NamedElement, compositestates_AbstractState, compositestates_State, AbstractState, PseudostateKind},
    associations={ownedRegions2, incoming3, outgoing4, ownerRegion6, source8, target10, subvertex0, ownerState1},
    generalizations={gen_compositestates_Region_NamedElement, gen_compositestates_Pseudostate_AbstractState, gen_compositestates_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)