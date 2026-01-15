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
dfa_InitialState = Class(name="dfa::InitialState")
dfa_FinalState = Class(name="dfa::FinalState")
dfa_Dfa = Class(name="dfa::Dfa")
NamedElement = Class(name="NamedElement")
dfa_Language = Class(name="dfa::Language")
dfa_RegularState = Class(name="dfa::RegularState")
dfa_NamedElement = Class(name="dfa::NamedElement", is_abstract=True)
dfa_State = Class(name="dfa::State", is_abstract=True)
RegularState = Class(name="RegularState")
State = Class(name="State")
dfa_Transition = Class(name="dfa::Transition")
dfa_Symbol = Class(name="dfa::Symbol")

# dfa_InitialState class attributes and methods

# dfa_FinalState class attributes and methods

# dfa_Dfa class attributes and methods

# NamedElement class attributes and methods

# dfa_Language class attributes and methods

# dfa_RegularState class attributes and methods

# dfa_NamedElement class attributes and methods
dfa_NamedElement_name: Property = Property(name="name", type=StringType)
dfa_NamedElement.attributes={dfa_NamedElement_name}

# dfa_State class attributes and methods
dfa_State_description: Property = Property(name="description", type=StringType)
dfa_State.attributes={dfa_State_description}

# RegularState class attributes and methods

# State class attributes and methods

# dfa_Transition class attributes and methods

# dfa_Symbol class attributes and methods
dfa_Symbol_literal: Property = Property(name="literal", type=StringType)
dfa_Symbol_description: Property = Property(name="description", type=StringType)
dfa_Symbol_direction: Property = Property(name="direction", type=StringType)
dfa_Symbol.attributes={dfa_Symbol_description, dfa_Symbol_literal, dfa_Symbol_direction}

# Relationships
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="dfa_InitialState", type=dfa_Dfa, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Dfa4", type=dfa_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
finalStates5: BinaryAssociation = BinaryAssociation(
    name="finalStates5",
    ends={
        Property(name="dfa_FinalState", type=dfa_Dfa, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Dfa6", type=dfa_FinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
language0: BinaryAssociation = BinaryAssociation(
    name="language0",
    ends={
        Property(name="dfa_Language", type=dfa_Dfa, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Dfa", type=dfa_Language, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
regularStates1: BinaryAssociation = BinaryAssociation(
    name="regularStates1",
    ends={
        Property(name="dfa_RegularState", type=dfa_Dfa, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Dfa2", type=dfa_RegularState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbols10: BinaryAssociation = BinaryAssociation(
    name="symbols10",
    ends={
        Property(name="dfa_Symbol12", type=dfa_Language, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Language11", type=dfa_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions13: BinaryAssociation = BinaryAssociation(
    name="transitions13",
    ends={
        Property(name="dfa_Transition15", type=dfa_RegularState, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_RegularState14", type=dfa_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targetState7: BinaryAssociation = BinaryAssociation(
    name="targetState7",
    ends={
        Property(name="dfa_State", type=dfa_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Transition", type=dfa_State, multiplicity=Multiplicity(1, 1))
    }
)
symbols8: BinaryAssociation = BinaryAssociation(
    name="symbols8",
    ends={
        Property(name="dfa_Symbol", type=dfa_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dfa_Transition9", type=dfa_Symbol, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dfa_Dfa_NamedElement = Generalization(general=NamedElement, specific=dfa_Dfa)
gen_dfa_RegularState_State = Generalization(general=State, specific=dfa_RegularState)
gen_dfa_State_NamedElement = Generalization(general=NamedElement, specific=dfa_State)
gen_dfa_InitialState_RegularState = Generalization(general=RegularState, specific=dfa_InitialState)
gen_dfa_FinalState_State = Generalization(general=State, specific=dfa_FinalState)
gen_dfa_Language_NamedElement = Generalization(general=NamedElement, specific=dfa_Language)

# Domain Model
domain_model = DomainModel(
    name="dfa",
    types={dfa_InitialState, dfa_FinalState, dfa_Dfa, NamedElement, dfa_Language, dfa_RegularState, dfa_NamedElement, dfa_State, RegularState, State, dfa_Transition, dfa_Symbol},
    associations={initialState3, finalStates5, language0, regularStates1, symbols10, transitions13, targetState7, symbols8},
    generalizations={gen_dfa_Dfa_NamedElement, gen_dfa_RegularState_State, gen_dfa_State_NamedElement, gen_dfa_InitialState_RegularState, gen_dfa_FinalState_State, gen_dfa_Language_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)