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
NumberOperator: Enumeration = Enumeration(
    name="NumberOperator",
    literals={
            EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="Unequal")
    }
)

DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="Number"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="String")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="Unequal")
    }
)

StringOperator: Enumeration = Enumeration(
    name="StringOperator",
    literals={
            EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="Unequal")
    }
)

# Classes
automata_Automaton = Class(name="automata::Automaton")
automata_State = Class(name="automata::State")
automata_Transition = Class(name="automata::Transition")
automata_Variable = Class(name="automata::Variable")
automata_Guard = Class(name="automata::Guard")
automata_BooleanGuard = Class(name="automata::BooleanGuard")
Guard = Class(name="Guard")
automata_StringGuard = Class(name="automata::StringGuard")
automata_NumberGuard = Class(name="automata::NumberGuard")
automata_Action = Class(name="automata::Action")

# automata_Automaton class attributes and methods

# automata_State class attributes and methods
automata_State_name: Property = Property(name="name", type=StringType)
automata_State_initial: Property = Property(name="initial", type=BooleanType)
automata_State.attributes={automata_State_name, automata_State_initial}

# automata_Transition class attributes and methods

# automata_Variable class attributes and methods
automata_Variable_name: Property = Property(name="name", type=StringType)
automata_Variable_type: Property = Property(name="type", type=StringType)
automata_Variable.attributes={automata_Variable_type, automata_Variable_name}

# automata_Guard class attributes and methods

# automata_BooleanGuard class attributes and methods
automata_BooleanGuard_value: Property = Property(name="value", type=BooleanType)
automata_BooleanGuard_operator: Property = Property(name="operator", type=StringType)
automata_BooleanGuard.attributes={automata_BooleanGuard_operator, automata_BooleanGuard_value}

# Guard class attributes and methods

# automata_StringGuard class attributes and methods
automata_StringGuard_value: Property = Property(name="value", type=StringType)
automata_StringGuard_operator: Property = Property(name="operator", type=StringType)
automata_StringGuard.attributes={automata_StringGuard_value, automata_StringGuard_operator}

# automata_NumberGuard class attributes and methods
automata_NumberGuard_operator: Property = Property(name="operator", type=StringType)
automata_NumberGuard_value: Property = Property(name="value", type=StringType)
automata_NumberGuard.attributes={automata_NumberGuard_operator, automata_NumberGuard_value}

# automata_Action class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="automata_State", type=automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automaton", type=automata_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="automata_Transition", type=automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automaton2", type=automata_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="automata_Variable", type=automata_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Automaton4", type=automata_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="automata_State7", type=automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Transition6", type=automata_State, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="automata_State10", type=automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Transition9", type=automata_State, multiplicity=Multiplicity(1, 1))
    }
)
guard11: BinaryAssociation = BinaryAssociation(
    name="guard11",
    ends={
        Property(name="automata_Guard", type=automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Transition12", type=automata_Guard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="automata_Variable15", type=automata_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Guard14", type=automata_Variable, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="automata_Variable17", type=automata_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Action", type=automata_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_automata_BooleanGuard_Guard = Generalization(general=Guard, specific=automata_BooleanGuard)
gen_automata_StringGuard_Guard = Generalization(general=Guard, specific=automata_StringGuard)
gen_automata_NumberGuard_Guard = Generalization(general=Guard, specific=automata_NumberGuard)

# Domain Model
domain_model = DomainModel(
    name="automata",
    types={automata_Automaton, automata_State, automata_Transition, automata_Variable, automata_Guard, automata_BooleanGuard, Guard, automata_StringGuard, automata_NumberGuard, automata_Action, NumberOperator, DataType, BooleanOperator, StringOperator},
    associations={states0, transitions1, variables3, source5, target8, guard11, source13, target16},
    generalizations={gen_automata_BooleanGuard_Guard, gen_automata_StringGuard_Guard, gen_automata_NumberGuard_Guard},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)