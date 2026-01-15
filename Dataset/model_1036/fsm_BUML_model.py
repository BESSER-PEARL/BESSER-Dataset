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
fsm_StateMachine = Class(name="fsm::StateMachine")
fsm_AbstractState = Class(name="fsm::AbstractState", is_abstract=True)
fsm_Transition = Class(name="fsm::Transition")
fsm_State = Class(name="fsm::State")
AbstractState = Class(name="AbstractState")
fsm_Program = Class(name="fsm::Program")
fsm_Trigger = Class(name="fsm::Trigger")
fsm_Constraint = Class(name="fsm::Constraint", is_abstract=True)
fsm_Pseudostate = Class(name="fsm::Pseudostate")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
fsm_RelationalConstraint = Class(name="fsm::RelationalConstraint")
Constraint = Class(name="Constraint")
fsm_Expression = Class(name="fsm::Expression", is_abstract=True)
Statement = Class(name="Statement")
fsm_Conditional = Class(name="fsm::Conditional")
fsm_Loop = Class(name="fsm::Loop")
fsm_Statement = Class(name="fsm::Statement", is_abstract=True)
fsm_VarDecl = Class(name="fsm::VarDecl")
fsm_Literal = Class(name="fsm::Literal", is_abstract=True)
Expression = Class(name="Expression")
fsm_IntegerLit = Class(name="fsm::IntegerLit")
Literal = Class(name="Literal")
fsm_StringLit = Class(name="fsm::StringLit")
fsm_BoolLit = Class(name="fsm::BoolLit")
fsm_ArithmeticExpression = Class(name="fsm::ArithmeticExpression")
fsm_RelationalExpression = Class(name="fsm::RelationalExpression")
fsm_VarReference = Class(name="fsm::VarReference")
fsm_ConsoleOutput = Class(name="fsm::ConsoleOutput")
fsm_Println = Class(name="fsm::Println")
ConsoleOutput = Class(name="ConsoleOutput")
fsm_Print = Class(name="fsm::Print")
fsm_Assignation = Class(name="fsm::Assignation")
fsm_Wait = Class(name="fsm::Wait")

# fsm_StateMachine class attributes and methods
fsm_StateMachine_name: Property = Property(name="name", type=StringType)
fsm_StateMachine.attributes={fsm_StateMachine_name}

# fsm_AbstractState class attributes and methods
fsm_AbstractState_name: Property = Property(name="name", type=StringType)
fsm_AbstractState.attributes={fsm_AbstractState_name}

# fsm_Transition class attributes and methods

# fsm_State class attributes and methods

# AbstractState class attributes and methods

# fsm_Program class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Constraint class attributes and methods

# fsm_Pseudostate class attributes and methods
fsm_Pseudostate_kind: Property = Property(name="kind", type=StringType)
fsm_Pseudostate.attributes={fsm_Pseudostate_kind}

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_RelationalConstraint class attributes and methods

# Constraint class attributes and methods

# fsm_Expression class attributes and methods

# Statement class attributes and methods

# fsm_Conditional class attributes and methods

# fsm_Loop class attributes and methods

# fsm_Statement class attributes and methods

# fsm_VarDecl class attributes and methods
fsm_VarDecl_key: Property = Property(name="key", type=StringType)
fsm_VarDecl.attributes={fsm_VarDecl_key}

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

# fsm_RelationalExpression class attributes and methods
fsm_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
fsm_RelationalExpression.attributes={fsm_RelationalExpression_operator}

# fsm_VarReference class attributes and methods
fsm_VarReference_key: Property = Property(name="key", type=StringType)
fsm_VarReference.attributes={fsm_VarReference_key}

# fsm_ConsoleOutput class attributes and methods
fsm_ConsoleOutput_input: Property = Property(name="input", type=StringType)
fsm_ConsoleOutput.attributes={fsm_ConsoleOutput_input}

# fsm_Println class attributes and methods

# ConsoleOutput class attributes and methods

# fsm_Print class attributes and methods

# fsm_Assignation class attributes and methods

# fsm_Wait class attributes and methods
fsm_Wait_miliseconds: Property = Property(name="miliseconds", type=StringType)
fsm_Wait.attributes={fsm_Wait_miliseconds}

# Relationships
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
        Property(name="4", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="7", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
doActivity8: BinaryAssociation = BinaryAssociation(
    name="doActivity8",
    ends={
        Property(name="fsm_Program", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry9: BinaryAssociation = BinaryAssociation(
    name="entry9",
    ends={
        Property(name="fsm_Program11", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State10", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit12: BinaryAssociation = BinaryAssociation(
    name="exit12",
    ends={
        Property(name="fsm_Program14", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State13", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger15: BinaryAssociation = BinaryAssociation(
    name="trigger15",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition16", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard25: BinaryAssociation = BinaryAssociation(
    name="guard25",
    ends={
        Property(name="fsm_Constraint", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition26", type=fsm_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression27: BinaryAssociation = BinaryAssociation(
    name="expression27",
    ends={
        Property(name="fsm_Expression", type=fsm_RelationalConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalConstraint", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements28: BinaryAssociation = BinaryAssociation(
    name="statements28",
    ends={
        Property(name="fsm_Statement30", type=fsm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Program29", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="fsm_Expression32", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenInstructions33: BinaryAssociation = BinaryAssociation(
    name="thenInstructions33",
    ends={
        Property(name="fsm_Program35", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional34", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseInstructions36: BinaryAssociation = BinaryAssociation(
    name="elseInstructions36",
    ends={
        Property(name="fsm_Program38", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional37", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="19", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="22", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
effect23: BinaryAssociation = BinaryAssociation(
    name="effect23",
    ends={
        Property(name="fsm_Statement", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition24", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression44: BinaryAssociation = BinaryAssociation(
    name="expression44",
    ends={
        Property(name="fsm_Expression45", type=fsm_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_VarDecl", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="fsm_Expression47", type=fsm_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_ArithmeticExpression", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right48: BinaryAssociation = BinaryAssociation(
    name="right48",
    ends={
        Property(name="fsm_Expression50", type=fsm_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_ArithmeticExpression49", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left51: BinaryAssociation = BinaryAssociation(
    name="left51",
    ends={
        Property(name="fsm_Expression52", type=fsm_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalExpression", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right53: BinaryAssociation = BinaryAssociation(
    name="right53",
    ends={
        Property(name="fsm_Expression55", type=fsm_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalExpression54", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard39: BinaryAssociation = BinaryAssociation(
    name="guard39",
    ends={
        Property(name="fsm_Expression40", type=fsm_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Loop", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body41: BinaryAssociation = BinaryAssociation(
    name="body41",
    ends={
        Property(name="fsm_Program43", type=fsm_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Loop42", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varRef56: BinaryAssociation = BinaryAssociation(
    name="varRef56",
    ends={
        Property(name="fsm_VarDecl57", type=fsm_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Assignation", type=fsm_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expression58: BinaryAssociation = BinaryAssociation(
    name="expression58",
    ends={
        Property(name="fsm_Expression60", type=fsm_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Assignation59", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fsm_State_AbstractState = Generalization(general=AbstractState, specific=fsm_State)
gen_fsm_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsm_Pseudostate)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_RelationalConstraint_Constraint = Generalization(general=Constraint, specific=fsm_RelationalConstraint)
gen_fsm_Program_Statement = Generalization(general=Statement, specific=fsm_Program)
gen_fsm_Conditional_Statement = Generalization(general=Statement, specific=fsm_Conditional)
gen_fsm_Loop_Statement = Generalization(general=Statement, specific=fsm_Loop)
gen_fsm_VarDecl_Statement = Generalization(general=Statement, specific=fsm_VarDecl)
gen_fsm_Literal_Expression = Generalization(general=Expression, specific=fsm_Literal)
gen_fsm_IntegerLit_Literal = Generalization(general=Literal, specific=fsm_IntegerLit)
gen_fsm_StringLit_Literal = Generalization(general=Literal, specific=fsm_StringLit)
gen_fsm_BoolLit_Literal = Generalization(general=Literal, specific=fsm_BoolLit)
gen_fsm_ArithmeticExpression_Expression = Generalization(general=Expression, specific=fsm_ArithmeticExpression)
gen_fsm_RelationalExpression_Expression = Generalization(general=Expression, specific=fsm_RelationalExpression)
gen_fsm_VarReference_Expression = Generalization(general=Expression, specific=fsm_VarReference)
gen_fsm_ConsoleOutput_Statement = Generalization(general=Statement, specific=fsm_ConsoleOutput)
gen_fsm_Println_ConsoleOutput = Generalization(general=ConsoleOutput, specific=fsm_Println)
gen_fsm_Print_ConsoleOutput = Generalization(general=ConsoleOutput, specific=fsm_Print)
gen_fsm_Assignation_Statement = Generalization(general=Statement, specific=fsm_Assignation)
gen_fsm_Wait_Statement = Generalization(general=Statement, specific=fsm_Wait)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, fsm_AbstractState, fsm_Transition, fsm_State, AbstractState, fsm_Program, fsm_Trigger, fsm_Constraint, fsm_Pseudostate, fsm_FinalState, State, fsm_RelationalConstraint, Constraint, fsm_Expression, Statement, fsm_Conditional, fsm_Loop, fsm_Statement, fsm_VarDecl, fsm_Literal, Expression, fsm_IntegerLit, Literal, fsm_StringLit, fsm_BoolLit, fsm_ArithmeticExpression, fsm_RelationalExpression, fsm_VarReference, fsm_ConsoleOutput, fsm_Println, ConsoleOutput, fsm_Print, fsm_Assignation, fsm_Wait, PseudostateKind, ArithmeticOperator, RelationalOperator},
    associations={subvertex0, transitions1, incoming3, outgoing5, doActivity8, entry9, exit12, trigger15, guard25, expression27, statements28, condition31, thenInstructions33, elseInstructions36, target17, source20, effect23, expression44, left46, right48, left51, right53, guard39, body41, varRef56, expression58},
    generalizations={gen_fsm_State_AbstractState, gen_fsm_Pseudostate_AbstractState, gen_fsm_FinalState_State, gen_fsm_RelationalConstraint_Constraint, gen_fsm_Program_Statement, gen_fsm_Conditional_Statement, gen_fsm_Loop_Statement, gen_fsm_VarDecl_Statement, gen_fsm_Literal_Expression, gen_fsm_IntegerLit_Literal, gen_fsm_StringLit_Literal, gen_fsm_BoolLit_Literal, gen_fsm_ArithmeticExpression_Expression, gen_fsm_RelationalExpression_Expression, gen_fsm_VarReference_Expression, gen_fsm_ConsoleOutput_Statement, gen_fsm_Println_ConsoleOutput, gen_fsm_Print_ConsoleOutput, gen_fsm_Assignation_Statement, gen_fsm_Wait_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)