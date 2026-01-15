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
DFAAutomaton_Transition = Class(name="DFAAutomaton::Transition")
DFAAutomaton_Symbol = Class(name="DFAAutomaton::Symbol")
DFAAutomaton_Automaton = Class(name="DFAAutomaton::Automaton")
DFAAutomaton_State = Class(name="DFAAutomaton::State")

# DFAAutomaton_Transition class attributes and methods

# DFAAutomaton_Symbol class attributes and methods
DFAAutomaton_Symbol_symbol: Property = Property(name="symbol", type=StringType)
DFAAutomaton_Symbol.attributes={DFAAutomaton_Symbol_symbol}

# DFAAutomaton_Automaton class attributes and methods
DFAAutomaton_Automaton_name: Property = Property(name="name", type=StringType)
DFAAutomaton_Automaton.attributes={DFAAutomaton_Automaton_name}

# DFAAutomaton_State class attributes and methods
DFAAutomaton_State_name: Property = Property(name="name", type=StringType)
DFAAutomaton_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
DFAAutomaton_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
DFAAutomaton_State.attributes={DFAAutomaton_State_isInitial, DFAAutomaton_State_isFinal, DFAAutomaton_State_name}

# Relationships
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
        Property(name="DFAAutomaton_Symbol", type=DFAAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Automaton4", type=DFAAutomaton_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="DFAAutomaton_State", type=DFAAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Automaton", type=DFAAutomaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src5: BinaryAssociation = BinaryAssociation(
    name="src5",
    ends={
        Property(name="DFAAutomaton_State7", type=DFAAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Transition6", type=DFAAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
tar8: BinaryAssociation = BinaryAssociation(
    name="tar8",
    ends={
        Property(name="DFAAutomaton_State10", type=DFAAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Transition9", type=DFAAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
symbol11: BinaryAssociation = BinaryAssociation(
    name="symbol11",
    ends={
        Property(name="DFAAutomaton_Symbol13", type=DFAAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="DFAAutomaton_Transition12", type=DFAAutomaton_Symbol, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DFAAutomaton",
    types={DFAAutomaton_Transition, DFAAutomaton_Symbol, DFAAutomaton_Automaton, DFAAutomaton_State},
    associations={transitions1, alphabet3, states0, src5, tar8, symbol11},
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