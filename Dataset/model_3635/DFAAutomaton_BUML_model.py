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
DFAAutomaton_Automaton = Class(name="DFAAutomaton::Automaton")
DFAAutomaton_State = Class(name="DFAAutomaton::State")
DFAAutomaton_Transition = Class(name="DFAAutomaton::Transition")
DFAAutomaton_AlphabetSymbol = Class(name="DFAAutomaton::AlphabetSymbol")
DFAAutomaton_CompositeState = Class(name="DFAAutomaton::CompositeState")
State = Class(name="State")

# DFAAutomaton_Automaton class attributes and methods
DFAAutomaton_Automaton_name: Property = Property(name="name", type=StringType)
DFAAutomaton_Automaton.attributes={DFAAutomaton_Automaton_name}

# DFAAutomaton_State class attributes and methods
DFAAutomaton_State_name: Property = Property(name="name", type=StringType)
DFAAutomaton_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
DFAAutomaton_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
DFAAutomaton_State.attributes={DFAAutomaton_State_isFinal, DFAAutomaton_State_isInitial, DFAAutomaton_State_name}

# DFAAutomaton_Transition class attributes and methods

# DFAAutomaton_AlphabetSymbol class attributes and methods
DFAAutomaton_AlphabetSymbol_symbol: Property = Property(name="symbol", type=StringType)
DFAAutomaton_AlphabetSymbol.attributes={DFAAutomaton_AlphabetSymbol_symbol}

# DFAAutomaton_CompositeState class attributes and methods

# State class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="DFAAutomaton_State", type=DFAAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Automaton", type=DFAAutomaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="DFAAutomaton_Transition", type=DFAAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Automaton2", type=DFAAutomaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alphabet3: BinaryAssociation = BinaryAssociation(
    name="alphabet3",
    ends={
        Property(name="DFAAutomaton_AlphabetSymbol", type=DFAAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Automaton4", type=DFAAutomaton_AlphabetSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition", type=DFAAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=DFAAutomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="DFAAutomaton_State8", type=DFAAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Transition7", type=DFAAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="State", type=DFAAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=DFAAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
symbol10: BinaryAssociation = BinaryAssociation(
    name="symbol10",
    ends={
        Property(name="DFAAutomaton_AlphabetSymbol12", type=DFAAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Transition11", type=DFAAutomaton_AlphabetSymbol, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_DFAAutomaton_CompositeState_State = Generalization(general=State, specific=DFAAutomaton_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="DFAAutomaton",
    types={DFAAutomaton_Automaton, DFAAutomaton_State, DFAAutomaton_Transition, DFAAutomaton_AlphabetSymbol, DFAAutomaton_CompositeState, State},
    associations={states0, transitions1, alphabet3, incoming5, from6, to9, symbol10},
    generalizations={gen_DFAAutomaton_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)