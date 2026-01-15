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
AcceptanceKind: Enumeration = Enumeration(
    name="AcceptanceKind",
    literals={
            EnumerationLiteral(name="Finite"),
			EnumerationLiteral(name="Infinite"),
			EnumerationLiteral(name="Probabilistic")
    }
)

# Classes
autopl_Symbol = Class(name="autopl::Symbol")
autopl_Automaton = Class(name="autopl::Automaton")
autopl_Alphabet = Class(name="autopl::Alphabet")
autopl_State = Class(name="autopl::State")
autopl_Transition = Class(name="autopl::Transition")
autopl_HierarchicalState = Class(name="autopl::HierarchicalState")
State = Class(name="State")

# autopl_Symbol class attributes and methods
autopl_Symbol_name: Property = Property(name="name", type=StringType)
autopl_Symbol.attributes={autopl_Symbol_name}

# autopl_Automaton class attributes and methods
autopl_Automaton_m_acceptanceCondition: Method = Method(name="acceptanceCondition", parameters={}, type=StringType)
autopl_Automaton.methods={autopl_Automaton_m_acceptanceCondition}

# autopl_Alphabet class attributes and methods

# autopl_State class attributes and methods
autopl_State_name: Property = Property(name="name", type=StringType)
autopl_State_isInitial: Property = Property(name="isInitial", type=StringType)
autopl_State_isFinal: Property = Property(name="isFinal", type=StringType)
autopl_State_m_outTrans: Method = Method(name="outTrans", parameters={}, type=StringType)
autopl_State_m_adjacent: Method = Method(name="adjacent", parameters={}, type=StringType)
autopl_State_m_inTrans: Method = Method(name="inTrans", parameters={}, type=StringType)
autopl_State.attributes={autopl_State_isFinal, autopl_State_isInitial, autopl_State_name}
autopl_State.methods={autopl_State_m_outTrans, autopl_State_m_inTrans, autopl_State_m_adjacent}

# autopl_Transition class attributes and methods
autopl_Transition_probability: Property = Property(name="probability", type=StringType)
autopl_Transition.attributes={autopl_Transition_probability}

# autopl_HierarchicalState class attributes and methods

# State class attributes and methods

# Relationships
initialStackSymbol7: BinaryAssociation = BinaryAssociation(
    name="initialStackSymbol7",
    ends={
        Property(name="autopl_Symbol", type=autopl_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Automaton8", type=autopl_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
inputAlphabet0: BinaryAssociation = BinaryAssociation(
    name="inputAlphabet0",
    ends={
        Property(name="autopl_Alphabet", type=autopl_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Automaton", type=autopl_Alphabet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputAlphabet1: BinaryAssociation = BinaryAssociation(
    name="outputAlphabet1",
    ends={
        Property(name="autopl_Alphabet3", type=autopl_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Automaton2", type=autopl_Alphabet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stackAlphabet4: BinaryAssociation = BinaryAssociation(
    name="stackAlphabet4",
    ends={
        Property(name="autopl_Alphabet6", type=autopl_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Automaton5", type=autopl_Alphabet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
input16: BinaryAssociation = BinaryAssociation(
    name="input16",
    ends={
        Property(name="autopl_Symbol18", type=autopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Transition17", type=autopl_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
states9: BinaryAssociation = BinaryAssociation(
    name="states9",
    ends={
        Property(name="autopl_State", type=autopl_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Automaton10", type=autopl_State, multiplicity=Multiplicity(0, 9999))
    }
)
transitions11: BinaryAssociation = BinaryAssociation(
    name="transitions11",
    ends={
        Property(name="autopl_Transition", type=autopl_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Automaton12", type=autopl_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
symbols13: BinaryAssociation = BinaryAssociation(
    name="symbols13",
    ends={
        Property(name="autopl_Symbol15", type=autopl_Alphabet, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Alphabet14", type=autopl_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from28: BinaryAssociation = BinaryAssociation(
    name="from28",
    ends={
        Property(name="autopl_State30", type=autopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Transition29", type=autopl_State, multiplicity=Multiplicity(1, 1))
    }
)
to31: BinaryAssociation = BinaryAssociation(
    name="to31",
    ends={
        Property(name="autopl_State33", type=autopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Transition32", type=autopl_State, multiplicity=Multiplicity(1, 1))
    }
)
output19: BinaryAssociation = BinaryAssociation(
    name="output19",
    ends={
        Property(name="autopl_Symbol21", type=autopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Transition20", type=autopl_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
stackCheck22: BinaryAssociation = BinaryAssociation(
    name="stackCheck22",
    ends={
        Property(name="autopl_Symbol24", type=autopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Transition23", type=autopl_Symbol, multiplicity=Multiplicity(1, 1))
    }
)
stackPush25: BinaryAssociation = BinaryAssociation(
    name="stackPush25",
    ends={
        Property(name="autopl_Symbol27", type=autopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_Transition26", type=autopl_Symbol, multiplicity=Multiplicity(2, 2))
    }
)
states34: BinaryAssociation = BinaryAssociation(
    name="states34",
    ends={
        Property(name="autopl_State35", type=autopl_HierarchicalState, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_HierarchicalState", type=autopl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions36: BinaryAssociation = BinaryAssociation(
    name="transitions36",
    ends={
        Property(name="autopl_Transition38", type=autopl_HierarchicalState, multiplicity=Multiplicity(1, 1)),
        Property(name="autopl_HierarchicalState37", type=autopl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_autopl_HierarchicalState_State = Generalization(general=State, specific=autopl_HierarchicalState)

# Domain Model
domain_model = DomainModel(
    name="autopl",
    types={autopl_Symbol, autopl_Automaton, autopl_Alphabet, autopl_State, autopl_Transition, autopl_HierarchicalState, State, AcceptanceKind},
    associations={initialStackSymbol7, inputAlphabet0, outputAlphabet1, stackAlphabet4, input16, states9, transitions11, symbols13, from28, to31, output19, stackCheck22, stackPush25, states34, transitions36},
    generalizations={gen_autopl_HierarchicalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)