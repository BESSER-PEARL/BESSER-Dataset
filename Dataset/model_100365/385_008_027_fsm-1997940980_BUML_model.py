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

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="mult"),
			EnumerationLiteral(name="div")
    }
)

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="lessThanOrEqualTo"),
			EnumerationLiteral(name="greaterThanOrEqualTo"),
			EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="equals")
    }
)

# Classes
fsm_StateMachine = Class(name="fsm_StateMachine")
fsm_AbstractState = Class(name="fsm_AbstractState", is_abstract=True)
fsm_State = Class(name="fsm_State")
AbstractState = Class(name="AbstractState")
fsm_Program = Class(name="fsm_Program")
fsm_Transition = Class(name="fsm_Transition")
fsm_Statement = Class(name="fsm_Statement", is_abstract=True)
fsm_Constraint = Class(name="fsm_Constraint", is_abstract=True)
fsm_Trigger = Class(name="fsm_Trigger")
Statement = Class(name="Statement")
fsm_Conditional = Class(name="fsm_Conditional")
fsm_Pseudostate = Class(name="fsm_Pseudostate")
fsm_FinalState = Class(name="fsm_FinalState")
State = Class(name="State")
fsm_RelationalConstraint = Class(name="fsm_RelationalConstraint")
Constraint = Class(name="Constraint")
fsm_Expression = Class(name="fsm_Expression", is_abstract=True)
fsm_Loop = Class(name="fsm_Loop")
fsm_VarDecl = Class(name="fsm_VarDecl")
fsm_RelationalExpression = Class(name="fsm_RelationalExpression")
fsm_Literal = Class(name="fsm_Literal", is_abstract=True)
Expression = Class(name="Expression")
fsm_IntegerLit = Class(name="fsm_IntegerLit")
Literal = Class(name="Literal")
fsm_StringLit = Class(name="fsm_StringLit")
fsm_BoolLit = Class(name="fsm_BoolLit")
fsm_ArithmeticExpression = Class(name="fsm_ArithmeticExpression")
fsm_VarReference = Class(name="fsm_VarReference")
fsm_ConsoleOutput = Class(name="fsm_ConsoleOutput")
fsm_Wait = Class(name="fsm_Wait")
fsm_Println = Class(name="fsm_Println")
ConsoleOutput = Class(name="ConsoleOutput")
fsm_Print = Class(name="fsm_Print")
fsm_Assignation = Class(name="fsm_Assignation")

# fsm_StateMachine class attributes and methods
fsm_StateMachine_name: Property = Property(name="name", type=StringType)
fsm_StateMachine.attributes={fsm_StateMachine_name}

# fsm_AbstractState class attributes and methods
fsm_AbstractState_name: Property = Property(name="name", type=StringType)
fsm_AbstractState.attributes={fsm_AbstractState_name}

# fsm_State class attributes and methods

# AbstractState class attributes and methods

# fsm_Program class attributes and methods

# fsm_Transition class attributes and methods

# fsm_Statement class attributes and methods

# fsm_Constraint class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# Statement class attributes and methods

# fsm_Conditional class attributes and methods

# fsm_Pseudostate class attributes and methods
fsm_Pseudostate_kind: Property = Property(name="kind", type=StringType)
fsm_Pseudostate.attributes={fsm_Pseudostate_kind}

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_RelationalConstraint class attributes and methods

# Constraint class attributes and methods

# fsm_Expression class attributes and methods

# fsm_Loop class attributes and methods

# fsm_VarDecl class attributes and methods
fsm_VarDecl_key: Property = Property(name="key", type=StringType)
fsm_VarDecl.attributes={fsm_VarDecl_key}

# fsm_RelationalExpression class attributes and methods
fsm_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
fsm_RelationalExpression.attributes={fsm_RelationalExpression_operator}

# fsm_Literal class attributes and methods

# Expression class attributes and methods

# fsm_IntegerLit class attributes and methods
fsm_IntegerLit_value: Property = Property(name="value", type=IntegerType)
fsm_IntegerLit.attributes={fsm_IntegerLit_value}

# Literal class attributes and methods

# fsm_StringLit class attributes and methods
fsm_StringLit_value: Property = Property(name="value", type=StringType)
fsm_StringLit.attributes={fsm_StringLit_value}

# fsm_BoolLit class attributes and methods
fsm_BoolLit_value: Property = Property(name="value", type=BooleanType)
fsm_BoolLit.attributes={fsm_BoolLit_value}

# fsm_ArithmeticExpression class attributes and methods
fsm_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
fsm_ArithmeticExpression.attributes={fsm_ArithmeticExpression_operator}

# fsm_VarReference class attributes and methods
fsm_VarReference_key: Property = Property(name="key", type=StringType)
fsm_VarReference.attributes={fsm_VarReference_key}

# fsm_ConsoleOutput class attributes and methods
fsm_ConsoleOutput_input: Property = Property(name="input", type=StringType)
fsm_ConsoleOutput.attributes={fsm_ConsoleOutput_input}

# fsm_Wait class attributes and methods
fsm_Wait_miliseconds: Property = Property(name="miliseconds", type=StringType)
fsm_Wait.attributes={fsm_Wait_miliseconds}

# fsm_Println class attributes and methods

# ConsoleOutput class attributes and methods

# fsm_Print class attributes and methods

# fsm_Assignation class attributes and methods

# Relationships
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
doActivity6: BinaryAssociation = BinaryAssociation(
    name="doActivity6",
    ends={
        Property(name="fsm_Program", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry7: BinaryAssociation = BinaryAssociation(
    name="entry7",
    ends={
        Property(name="fsm_Program9", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State8", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subvertex0: BinaryAssociation = BinaryAssociation(
    name="subvertex0",
    ends={
        Property(name="fsm_AbstractState", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="fsm_Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine2", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
effect18: BinaryAssociation = BinaryAssociation(
    name="effect18",
    ends={
        Property(name="fsm_Statement", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition19", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard20: BinaryAssociation = BinaryAssociation(
    name="guard20",
    ends={
        Property(name="fsm_Constraint", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition21", type=fsm_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exit10: BinaryAssociation = BinaryAssociation(
    name="exit10",
    ends={
        Property(name="fsm_Program12", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State11", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger13: BinaryAssociation = BinaryAssociation(
    name="trigger13",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition14", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="AbstractState", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="AbstractState17", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
statements23: BinaryAssociation = BinaryAssociation(
    name="statements23",
    ends={
        Property(name="fsm_Statement25", type=fsm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Program24", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="fsm_Expression27", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression22: BinaryAssociation = BinaryAssociation(
    name="expression22",
    ends={
        Property(name="fsm_Expression", type=fsm_RelationalConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalConstraint", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard34: BinaryAssociation = BinaryAssociation(
    name="guard34",
    ends={
        Property(name="fsm_Expression35", type=fsm_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Loop", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body36: BinaryAssociation = BinaryAssociation(
    name="body36",
    ends={
        Property(name="fsm_Program38", type=fsm_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Loop37", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression39: BinaryAssociation = BinaryAssociation(
    name="expression39",
    ends={
        Property(name="fsm_Expression40", type=fsm_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_VarDecl", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenInstructions28: BinaryAssociation = BinaryAssociation(
    name="thenInstructions28",
    ends={
        Property(name="fsm_Program30", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional29", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseInstructions31: BinaryAssociation = BinaryAssociation(
    name="elseInstructions31",
    ends={
        Property(name="fsm_Program33", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional32", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right43: BinaryAssociation = BinaryAssociation(
    name="right43",
    ends={
        Property(name="fsm_Expression45", type=fsm_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_ArithmeticExpression44", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left41: BinaryAssociation = BinaryAssociation(
    name="left41",
    ends={
        Property(name="fsm_Expression42", type=fsm_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_ArithmeticExpression", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="fsm_Expression47", type=fsm_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalExpression", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right48: BinaryAssociation = BinaryAssociation(
    name="right48",
    ends={
        Property(name="fsm_Expression50", type=fsm_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalExpression49", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varRef51: BinaryAssociation = BinaryAssociation(
    name="varRef51",
    ends={
        Property(name="fsm_VarDecl52", type=fsm_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Assignation", type=fsm_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expression53: BinaryAssociation = BinaryAssociation(
    name="expression53",
    ends={
        Property(name="fsm_Expression55", type=fsm_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Assignation54", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fsm_State_AbstractState = Generalization(general=AbstractState, specific=fsm_State)
gen_fsm_Program_Statement = Generalization(general=Statement, specific=fsm_Program)
gen_fsm_Conditional_Statement = Generalization(general=Statement, specific=fsm_Conditional)
gen_fsm_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsm_Pseudostate)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_RelationalConstraint_Constraint = Generalization(general=Constraint, specific=fsm_RelationalConstraint)
gen_fsm_Loop_Statement = Generalization(general=Statement, specific=fsm_Loop)
gen_fsm_VarDecl_Statement = Generalization(general=Statement, specific=fsm_VarDecl)
gen_fsm_RelationalExpression_Expression = Generalization(general=Expression, specific=fsm_RelationalExpression)
gen_fsm_Literal_Expression = Generalization(general=Expression, specific=fsm_Literal)
gen_fsm_IntegerLit_Literal = Generalization(general=Literal, specific=fsm_IntegerLit)
gen_fsm_StringLit_Literal = Generalization(general=Literal, specific=fsm_StringLit)
gen_fsm_BoolLit_Literal = Generalization(general=Literal, specific=fsm_BoolLit)
gen_fsm_ArithmeticExpression_Expression = Generalization(general=Expression, specific=fsm_ArithmeticExpression)
gen_fsm_VarReference_Expression = Generalization(general=Expression, specific=fsm_VarReference)
gen_fsm_ConsoleOutput_Statement = Generalization(general=Statement, specific=fsm_ConsoleOutput)
gen_fsm_Wait_Statement = Generalization(general=Statement, specific=fsm_Wait)
gen_fsm_Println_ConsoleOutput = Generalization(general=ConsoleOutput, specific=fsm_Println)
gen_fsm_Print_ConsoleOutput = Generalization(general=ConsoleOutput, specific=fsm_Print)
gen_fsm_Assignation_Statement = Generalization(general=Statement, specific=fsm_Assignation)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, fsm_AbstractState, fsm_State, AbstractState, fsm_Program, fsm_Transition, fsm_Statement, fsm_Constraint, fsm_Trigger, Statement, fsm_Conditional, fsm_Pseudostate, fsm_FinalState, State, fsm_RelationalConstraint, Constraint, fsm_Expression, fsm_Loop, fsm_VarDecl, fsm_RelationalExpression, fsm_Literal, Expression, fsm_IntegerLit, Literal, fsm_StringLit, fsm_BoolLit, fsm_ArithmeticExpression, fsm_VarReference, fsm_ConsoleOutput, fsm_Wait, fsm_Println, ConsoleOutput, fsm_Print, fsm_Assignation, PseudostateKind, ArithmeticOperator, RelationalOperator},
    associations={outgoing4, doActivity6, entry7, subvertex0, transitions1, incoming3, effect18, guard20, exit10, trigger13, target15, source16, statements23, condition26, expression22, guard34, body36, expression39, thenInstructions28, elseInstructions31, right43, left41, left46, right48, varRef51, expression53},
    generalizations={gen_fsm_State_AbstractState, gen_fsm_Program_Statement, gen_fsm_Conditional_Statement, gen_fsm_Pseudostate_AbstractState, gen_fsm_FinalState_State, gen_fsm_RelationalConstraint_Constraint, gen_fsm_Loop_Statement, gen_fsm_VarDecl_Statement, gen_fsm_RelationalExpression_Expression, gen_fsm_Literal_Expression, gen_fsm_IntegerLit_Literal, gen_fsm_StringLit_Literal, gen_fsm_BoolLit_Literal, gen_fsm_ArithmeticExpression_Expression, gen_fsm_VarReference_Expression, gen_fsm_ConsoleOutput_Statement, gen_fsm_Wait_Statement, gen_fsm_Println_ConsoleOutput, gen_fsm_Print_ConsoleOutput, gen_fsm_Assignation_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)