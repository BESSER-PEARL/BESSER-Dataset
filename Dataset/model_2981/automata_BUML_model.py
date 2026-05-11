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

NumberOperator: Enumeration = Enumeration(
    name="NumberOperator",
    literals={
            EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="Unequal"),
			EnumerationLiteral(name="LessThan"),
			EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="GreaterOrEqualThan"),
			EnumerationLiteral(name="LessOrEqualThan")
    }
)

# Classes
automata_Automaton = Class(name="automata_Automaton")
automata_StringGuard = Class(name="automata_StringGuard")
automata_State = Class(name="automata_State")
automata_Transition = Class(name="automata_Transition")
automata_Variable = Class(name="automata_Variable", is_abstract=True)
automata_Guard = Class(name="automata_Guard", is_abstract=True)
automata_Action = Class(name="automata_Action", is_abstract=True)
automata_StringVariable = Class(name="automata_StringVariable")
Variable = Class(name="Variable")
automata_NumberVariable = Class(name="automata_NumberVariable")
automata_BooleanVariable = Class(name="automata_BooleanVariable")
automata_BooleanGuard = Class(name="automata_BooleanGuard")
Guard = Class(name="Guard")
automata_NumberGuard = Class(name="automata_NumberGuard")
automata_StringAction = Class(name="automata_StringAction")
Action = Class(name="Action")
automata_NumberAction = Class(name="automata_NumberAction")
automata_BooleanAction = Class(name="automata_BooleanAction")

# automata_Automaton class attributes and methods

# automata_StringGuard class attributes and methods
automata_StringGuard_value: Property = Property(name="value", type=StringType)
automata_StringGuard_operator: Property = Property(name="operator", type=StringType)
automata_StringGuard.attributes={automata_StringGuard_operator, automata_StringGuard_value}

# automata_State class attributes and methods
automata_State_name: Property = Property(name="name", type=StringType)
automata_State_initial: Property = Property(name="initial", type=BooleanType)
automata_State.attributes={automata_State_name, automata_State_initial}

# automata_Transition class attributes and methods

# automata_Variable class attributes and methods
automata_Variable_name: Property = Property(name="name", type=StringType)
automata_Variable.attributes={automata_Variable_name}

# automata_Guard class attributes and methods

# automata_Action class attributes and methods

# automata_StringVariable class attributes and methods
automata_StringVariable_initialValue: Property = Property(name="initialValue", type=StringType)
automata_StringVariable.attributes={automata_StringVariable_initialValue}

# Variable class attributes and methods

# automata_NumberVariable class attributes and methods
automata_NumberVariable_initialValue: Property = Property(name="initialValue", type=StringType)
automata_NumberVariable.attributes={automata_NumberVariable_initialValue}

# automata_BooleanVariable class attributes and methods
automata_BooleanVariable_initialValue: Property = Property(name="initialValue", type=BooleanType)
automata_BooleanVariable.attributes={automata_BooleanVariable_initialValue}

# automata_BooleanGuard class attributes and methods
automata_BooleanGuard_operator: Property = Property(name="operator", type=StringType)
automata_BooleanGuard_value: Property = Property(name="value", type=BooleanType)
automata_BooleanGuard.attributes={automata_BooleanGuard_value, automata_BooleanGuard_operator}

# Guard class attributes and methods

# automata_NumberGuard class attributes and methods
automata_NumberGuard_value: Property = Property(name="value", type=StringType)
automata_NumberGuard_operator: Property = Property(name="operator", type=StringType)
automata_NumberGuard.attributes={automata_NumberGuard_operator, automata_NumberGuard_value}

# automata_StringAction class attributes and methods
automata_StringAction_value: Property = Property(name="value", type=StringType)
automata_StringAction.attributes={automata_StringAction_value}

# Action class attributes and methods

# automata_NumberAction class attributes and methods
automata_NumberAction_value: Property = Property(name="value", type=StringType)
automata_NumberAction.attributes={automata_NumberAction_value}

# automata_BooleanAction class attributes and methods
automata_BooleanAction_value: Property = Property(name="value", type=BooleanType)
automata_BooleanAction.attributes={automata_BooleanAction_value}

# Relationships
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="automata_BooleanVariable", type=automata_BooleanGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_BooleanGuard", type=automata_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)
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
action13: BinaryAssociation = BinaryAssociation(
    name="action13",
    ends={
        Property(name="automata_Action", type=automata_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_Transition14", type=automata_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="automata_StringVariable", type=automata_StringGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_StringGuard", type=automata_StringVariable, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="automata_NumberVariable", type=automata_NumberGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_NumberGuard", type=automata_NumberVariable, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="automata_StringVariable19", type=automata_StringAction, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_StringAction", type=automata_StringVariable, multiplicity=Multiplicity(1, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="automata_NumberVariable21", type=automata_NumberAction, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_NumberAction", type=automata_NumberVariable, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="automata_BooleanVariable23", type=automata_BooleanAction, multiplicity=Multiplicity(1, 1)),
        Property(name="automata_BooleanAction", type=automata_BooleanVariable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_automata_StringGuard_Guard = Generalization(general=Guard, specific=automata_StringGuard)
gen_automata_StringVariable_Variable = Generalization(general=Variable, specific=automata_StringVariable)
gen_automata_NumberVariable_Variable = Generalization(general=Variable, specific=automata_NumberVariable)
gen_automata_BooleanVariable_Variable = Generalization(general=Variable, specific=automata_BooleanVariable)
gen_automata_BooleanGuard_Guard = Generalization(general=Guard, specific=automata_BooleanGuard)
gen_automata_NumberGuard_Guard = Generalization(general=Guard, specific=automata_NumberGuard)
gen_automata_StringAction_Action = Generalization(general=Action, specific=automata_StringAction)
gen_automata_NumberAction_Action = Generalization(general=Action, specific=automata_NumberAction)
gen_automata_BooleanAction_Action = Generalization(general=Action, specific=automata_BooleanAction)

# Domain Model
domain_model = DomainModel(
    name="automata",
    types={automata_Automaton, automata_StringGuard, automata_State, automata_Transition, automata_Variable, automata_Guard, automata_Action, automata_StringVariable, Variable, automata_NumberVariable, automata_BooleanVariable, automata_BooleanGuard, Guard, automata_NumberGuard, automata_StringAction, Action, automata_NumberAction, automata_BooleanAction, BooleanOperator, StringOperator, NumberOperator},
    associations={source15, states0, transitions1, variables3, source5, target8, guard11, action13, source16, source17, target18, target20, target22},
    generalizations={gen_automata_StringGuard_Guard, gen_automata_StringVariable_Variable, gen_automata_NumberVariable_Variable, gen_automata_BooleanVariable_Variable, gen_automata_BooleanGuard_Guard, gen_automata_NumberGuard_Guard, gen_automata_StringAction_Action, gen_automata_NumberAction_Action, gen_automata_BooleanAction_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)