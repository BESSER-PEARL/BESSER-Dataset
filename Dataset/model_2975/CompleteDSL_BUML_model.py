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
RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="lessThanOrEqualTo"),
			EnumerationLiteral(name="greaterThanOrEqualTo")
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

# Classes
CompleteDSLPckg_Expression = Class(name="CompleteDSLPckg::Expression", is_abstract=True)
CompleteDSLPckg_Literal = Class(name="CompleteDSLPckg::Literal", is_abstract=True)
Expression = Class(name="Expression")
CompleteDSLPckg_IntegerLit = Class(name="CompleteDSLPckg::IntegerLit")
CompleteDSLPckg_ArithmeticExpression = Class(name="CompleteDSLPckg::ArithmeticExpression")
Literal = Class(name="Literal")
CompleteDSLPckg_StringLit = Class(name="CompleteDSLPckg::StringLit")
CompleteDSLPckg_BoolLit = Class(name="CompleteDSLPckg::BoolLit")
CompleteDSLPckg_RelationalExpression = Class(name="CompleteDSLPckg::RelationalExpression")
CompleteDSLPckg_Block = Class(name="CompleteDSLPckg::Block")
CompleteDSLPckg_Statement = Class(name="CompleteDSLPckg::Statement", is_abstract=True)
CompleteDSLPckg_Conditional = Class(name="CompleteDSLPckg::Conditional")
Statement = Class(name="Statement")
CompleteDSLPckg_VarRef = Class(name="CompleteDSLPckg::VarRef")
CompleteDSLPckg_VarDecl = Class(name="CompleteDSLPckg::VarDecl")
CompleteDSLPckg_Loop = Class(name="CompleteDSLPckg::Loop")
CompleteDSLPckg_ConsoleOutput = Class(name="CompleteDSLPckg::ConsoleOutput")
CompleteDSLPckg_Println = Class(name="CompleteDSLPckg::Println")
ConsoleOutput = Class(name="ConsoleOutput")
CompleteDSLPckg_Print = Class(name="CompleteDSLPckg::Print")
CompleteDSLPckg_Assignation = Class(name="CompleteDSLPckg::Assignation")
CompleteDSLPckg_AbstractState = Class(name="CompleteDSLPckg::AbstractState", is_abstract=True)
CompleteDSLPckg_Transition = Class(name="CompleteDSLPckg::Transition")
CompleteDSLPckg_Wait = Class(name="CompleteDSLPckg::Wait")
CompleteDSLPckg_StateMachine = Class(name="CompleteDSLPckg::StateMachine")
NamedElement = Class(name="NamedElement")
CompleteDSLPckg_Region = Class(name="CompleteDSLPckg::Region")
CompleteDSLPckg_State = Class(name="CompleteDSLPckg::State")
AbstractState = Class(name="AbstractState")
CompleteDSLPckg_Trigger = Class(name="CompleteDSLPckg::Trigger")
CompleteDSLPckg_AndTrigger = Class(name="CompleteDSLPckg::AndTrigger")
CompleteDSLPckg_Pseudostate = Class(name="CompleteDSLPckg::Pseudostate", is_abstract=True)
CompleteDSLPckg_InitialState = Class(name="CompleteDSLPckg::InitialState")
Pseudostate = Class(name="Pseudostate")
CompleteDSLPckg_FinalState = Class(name="CompleteDSLPckg::FinalState")
State = Class(name="State")
CompleteDSLPckg_NamedElement = Class(name="CompleteDSLPckg::NamedElement")
CompleteDSLPckg_NotTrigger = Class(name="CompleteDSLPckg::NotTrigger")
Trigger = Class(name="Trigger")
CompleteDSLPckg_OrTrigger = Class(name="CompleteDSLPckg::OrTrigger")

# CompleteDSLPckg_Expression class attributes and methods

# CompleteDSLPckg_Literal class attributes and methods

# Expression class attributes and methods

# CompleteDSLPckg_IntegerLit class attributes and methods
CompleteDSLPckg_IntegerLit_value: Property = Property(name="value", type=IntegerType)
CompleteDSLPckg_IntegerLit.attributes={CompleteDSLPckg_IntegerLit_value}

# CompleteDSLPckg_ArithmeticExpression class attributes and methods
CompleteDSLPckg_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
CompleteDSLPckg_ArithmeticExpression.attributes={CompleteDSLPckg_ArithmeticExpression_operator}

# Literal class attributes and methods

# CompleteDSLPckg_StringLit class attributes and methods
CompleteDSLPckg_StringLit_value: Property = Property(name="value", type=StringType)
CompleteDSLPckg_StringLit.attributes={CompleteDSLPckg_StringLit_value}

# CompleteDSLPckg_BoolLit class attributes and methods
CompleteDSLPckg_BoolLit_value: Property = Property(name="value", type=BooleanType)
CompleteDSLPckg_BoolLit.attributes={CompleteDSLPckg_BoolLit_value}

# CompleteDSLPckg_RelationalExpression class attributes and methods
CompleteDSLPckg_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
CompleteDSLPckg_RelationalExpression.attributes={CompleteDSLPckg_RelationalExpression_operator}

# CompleteDSLPckg_Block class attributes and methods

# CompleteDSLPckg_Statement class attributes and methods

# CompleteDSLPckg_Conditional class attributes and methods

# Statement class attributes and methods

# CompleteDSLPckg_VarRef class attributes and methods
CompleteDSLPckg_VarRef_ref: Property = Property(name="ref", type=StringType)
CompleteDSLPckg_VarRef.attributes={CompleteDSLPckg_VarRef_ref}

# CompleteDSLPckg_VarDecl class attributes and methods
CompleteDSLPckg_VarDecl_name: Property = Property(name="name", type=StringType)
CompleteDSLPckg_VarDecl.attributes={CompleteDSLPckg_VarDecl_name}

# CompleteDSLPckg_Loop class attributes and methods

# CompleteDSLPckg_ConsoleOutput class attributes and methods
CompleteDSLPckg_ConsoleOutput_input: Property = Property(name="input", type=StringType)
CompleteDSLPckg_ConsoleOutput.attributes={CompleteDSLPckg_ConsoleOutput_input}

# CompleteDSLPckg_Println class attributes and methods

# ConsoleOutput class attributes and methods

# CompleteDSLPckg_Print class attributes and methods

# CompleteDSLPckg_Assignation class attributes and methods

# CompleteDSLPckg_AbstractState class attributes and methods

# CompleteDSLPckg_Transition class attributes and methods

# CompleteDSLPckg_Wait class attributes and methods
CompleteDSLPckg_Wait_miliseconds: Property = Property(name="miliseconds", type=StringType)
CompleteDSLPckg_Wait.attributes={CompleteDSLPckg_Wait_miliseconds}

# CompleteDSLPckg_StateMachine class attributes and methods

# NamedElement class attributes and methods

# CompleteDSLPckg_Region class attributes and methods

# CompleteDSLPckg_State class attributes and methods

# AbstractState class attributes and methods

# CompleteDSLPckg_Trigger class attributes and methods
CompleteDSLPckg_Trigger_expression: Property = Property(name="expression", type=StringType)
CompleteDSLPckg_Trigger.attributes={CompleteDSLPckg_Trigger_expression}

# CompleteDSLPckg_AndTrigger class attributes and methods

# CompleteDSLPckg_Pseudostate class attributes and methods

# CompleteDSLPckg_InitialState class attributes and methods

# Pseudostate class attributes and methods

# CompleteDSLPckg_FinalState class attributes and methods

# State class attributes and methods

# CompleteDSLPckg_NamedElement class attributes and methods
CompleteDSLPckg_NamedElement_name: Property = Property(name="name", type=StringType)
CompleteDSLPckg_NamedElement.attributes={CompleteDSLPckg_NamedElement_name}

# CompleteDSLPckg_NotTrigger class attributes and methods

# Trigger class attributes and methods

# CompleteDSLPckg_OrTrigger class attributes and methods

# Relationships
left0: BinaryAssociation = BinaryAssociation(
    name="left0",
    ends={
        Property(name="CompleteDSLPckg_Expression", type=CompleteDSLPckg_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ArithmeticExpression", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left4: BinaryAssociation = BinaryAssociation(
    name="left4",
    ends={
        Property(name="CompleteDSLPckg_Expression5", type=CompleteDSLPckg_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RelationalExpression", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right6: BinaryAssociation = BinaryAssociation(
    name="right6",
    ends={
        Property(name="CompleteDSLPckg_Expression8", type=CompleteDSLPckg_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_RelationalExpression7", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right1: BinaryAssociation = BinaryAssociation(
    name="right1",
    ends={
        Property(name="CompleteDSLPckg_Expression3", type=CompleteDSLPckg_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_ArithmeticExpression2", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements9: BinaryAssociation = BinaryAssociation(
    name="statements9",
    ends={
        Property(name="CompleteDSLPckg_Statement", type=CompleteDSLPckg_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Block", type=CompleteDSLPckg_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body17: BinaryAssociation = BinaryAssociation(
    name="body17",
    ends={
        Property(name="CompleteDSLPckg_Statement19", type=CompleteDSLPckg_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Loop18", type=CompleteDSLPckg_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="CompleteDSLPckg_Expression11", type=CompleteDSLPckg_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Conditional", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body12: BinaryAssociation = BinaryAssociation(
    name="body12",
    ends={
        Property(name="CompleteDSLPckg_Statement14", type=CompleteDSLPckg_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Conditional13", type=CompleteDSLPckg_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard15: BinaryAssociation = BinaryAssociation(
    name="guard15",
    ends={
        Property(name="CompleteDSLPckg_Expression16", type=CompleteDSLPckg_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Loop", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr20: BinaryAssociation = BinaryAssociation(
    name="expr20",
    ends={
        Property(name="CompleteDSLPckg_Expression21", type=CompleteDSLPckg_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_VarDecl", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varRef22: BinaryAssociation = BinaryAssociation(
    name="varRef22",
    ends={
        Property(name="CompleteDSLPckg_VarDecl23", type=CompleteDSLPckg_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Assignation", type=CompleteDSLPckg_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expression24: BinaryAssociation = BinaryAssociation(
    name="expression24",
    ends={
        Property(name="CompleteDSLPckg_Expression26", type=CompleteDSLPckg_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Assignation25", type=CompleteDSLPckg_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subvertex28: BinaryAssociation = BinaryAssociation(
    name="subvertex28",
    ends={
        Property(name="CompleteDSLPckg_AbstractState", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region29", type=CompleteDSLPckg_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions30: BinaryAssociation = BinaryAssociation(
    name="transitions30",
    ends={
        Property(name="CompleteDSLPckg_Transition", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region31", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regions27: BinaryAssociation = BinaryAssociation(
    name="regions27",
    ends={
        Property(name="CompleteDSLPckg_Region", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_StateMachine", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerRegion41: BinaryAssociation = BinaryAssociation(
    name="ownerRegion41",
    ends={
        Property(name="CompleteDSLPckg_Region43", type=CompleteDSLPckg_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AbstractState42", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1))
    }
)
entryAction44: BinaryAssociation = BinaryAssociation(
    name="entryAction44",
    ends={
        Property(name="CompleteDSLPckg_Block45", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State", type=CompleteDSLPckg_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownerStateMachine32: BinaryAssociation = BinaryAssociation(
    name="ownerStateMachine32",
    ends={
        Property(name="CompleteDSLPckg_StateMachine34", type=CompleteDSLPckg_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Region33", type=CompleteDSLPckg_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
incoming35: BinaryAssociation = BinaryAssociation(
    name="incoming35",
    ends={
        Property(name="CompleteDSLPckg_Transition37", type=CompleteDSLPckg_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AbstractState36", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing38: BinaryAssociation = BinaryAssociation(
    name="outgoing38",
    ends={
        Property(name="CompleteDSLPckg_Transition40", type=CompleteDSLPckg_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AbstractState39", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
target54: BinaryAssociation = BinaryAssociation(
    name="target54",
    ends={
        Property(name="CompleteDSLPckg_AbstractState56", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition55", type=CompleteDSLPckg_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source57: BinaryAssociation = BinaryAssociation(
    name="source57",
    ends={
        Property(name="CompleteDSLPckg_AbstractState59", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition58", type=CompleteDSLPckg_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
doAction46: BinaryAssociation = BinaryAssociation(
    name="doAction46",
    ends={
        Property(name="CompleteDSLPckg_Block48", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State47", type=CompleteDSLPckg_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitAction49: BinaryAssociation = BinaryAssociation(
    name="exitAction49",
    ends={
        Property(name="CompleteDSLPckg_Block51", type=CompleteDSLPckg_State, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_State50", type=CompleteDSLPckg_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger52: BinaryAssociation = BinaryAssociation(
    name="trigger52",
    ends={
        Property(name="CompleteDSLPckg_Trigger", type=CompleteDSLPckg_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_Transition53", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger60: BinaryAssociation = BinaryAssociation(
    name="trigger60",
    ends={
        Property(name="CompleteDSLPckg_Trigger61", type=CompleteDSLPckg_NotTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_NotTrigger", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left62: BinaryAssociation = BinaryAssociation(
    name="left62",
    ends={
        Property(name="CompleteDSLPckg_Trigger63", type=CompleteDSLPckg_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AndTrigger", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right64: BinaryAssociation = BinaryAssociation(
    name="right64",
    ends={
        Property(name="CompleteDSLPckg_Trigger66", type=CompleteDSLPckg_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_AndTrigger65", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left67: BinaryAssociation = BinaryAssociation(
    name="left67",
    ends={
        Property(name="CompleteDSLPckg_Trigger68", type=CompleteDSLPckg_OrTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OrTrigger", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="CompleteDSLPckg_Trigger71", type=CompleteDSLPckg_OrTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="CompleteDSLPckg_OrTrigger70", type=CompleteDSLPckg_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_CompleteDSLPckg_Literal_Expression = Generalization(general=Expression, specific=CompleteDSLPckg_Literal)
gen_CompleteDSLPckg_ArithmeticExpression_Expression = Generalization(general=Expression, specific=CompleteDSLPckg_ArithmeticExpression)
gen_CompleteDSLPckg_IntegerLit_Literal = Generalization(general=Literal, specific=CompleteDSLPckg_IntegerLit)
gen_CompleteDSLPckg_StringLit_Literal = Generalization(general=Literal, specific=CompleteDSLPckg_StringLit)
gen_CompleteDSLPckg_BoolLit_Literal = Generalization(general=Literal, specific=CompleteDSLPckg_BoolLit)
gen_CompleteDSLPckg_RelationalExpression_Expression = Generalization(general=Expression, specific=CompleteDSLPckg_RelationalExpression)
gen_CompleteDSLPckg_Conditional_Statement = Generalization(general=Statement, specific=CompleteDSLPckg_Conditional)
gen_CompleteDSLPckg_VarRef_Expression = Generalization(general=Expression, specific=CompleteDSLPckg_VarRef)
gen_CompleteDSLPckg_VarDecl_Statement = Generalization(general=Statement, specific=CompleteDSLPckg_VarDecl)
gen_CompleteDSLPckg_Loop_Statement = Generalization(general=Statement, specific=CompleteDSLPckg_Loop)
gen_CompleteDSLPckg_ConsoleOutput_Statement = Generalization(general=Statement, specific=CompleteDSLPckg_ConsoleOutput)
gen_CompleteDSLPckg_Println_ConsoleOutput = Generalization(general=ConsoleOutput, specific=CompleteDSLPckg_Println)
gen_CompleteDSLPckg_Print_ConsoleOutput = Generalization(general=ConsoleOutput, specific=CompleteDSLPckg_Print)
gen_CompleteDSLPckg_Assignation_Statement = Generalization(general=Statement, specific=CompleteDSLPckg_Assignation)
gen_CompleteDSLPckg_Region_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Region)
gen_CompleteDSLPckg_Wait_Statement = Generalization(general=Statement, specific=CompleteDSLPckg_Wait)
gen_CompleteDSLPckg_StateMachine_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_StateMachine)
gen_CompleteDSLPckg_State_AbstractState = Generalization(general=AbstractState, specific=CompleteDSLPckg_State)
gen_CompleteDSLPckg_AbstractState_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_AbstractState)
gen_CompleteDSLPckg_Transition_NamedElement = Generalization(general=NamedElement, specific=CompleteDSLPckg_Transition)
gen_CompleteDSLPckg_AndTrigger_Trigger = Generalization(general=Trigger, specific=CompleteDSLPckg_AndTrigger)
gen_CompleteDSLPckg_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=CompleteDSLPckg_Pseudostate)
gen_CompleteDSLPckg_InitialState_Pseudostate = Generalization(general=Pseudostate, specific=CompleteDSLPckg_InitialState)
gen_CompleteDSLPckg_FinalState_State = Generalization(general=State, specific=CompleteDSLPckg_FinalState)
gen_CompleteDSLPckg_NotTrigger_Trigger = Generalization(general=Trigger, specific=CompleteDSLPckg_NotTrigger)
gen_CompleteDSLPckg_OrTrigger_Trigger = Generalization(general=Trigger, specific=CompleteDSLPckg_OrTrigger)

# Domain Model
domain_model = DomainModel(
    name="CompleteDSLPckg",
    types={CompleteDSLPckg_Expression, CompleteDSLPckg_Literal, Expression, CompleteDSLPckg_IntegerLit, CompleteDSLPckg_ArithmeticExpression, Literal, CompleteDSLPckg_StringLit, CompleteDSLPckg_BoolLit, CompleteDSLPckg_RelationalExpression, CompleteDSLPckg_Block, CompleteDSLPckg_Statement, CompleteDSLPckg_Conditional, Statement, CompleteDSLPckg_VarRef, CompleteDSLPckg_VarDecl, CompleteDSLPckg_Loop, CompleteDSLPckg_ConsoleOutput, CompleteDSLPckg_Println, ConsoleOutput, CompleteDSLPckg_Print, CompleteDSLPckg_Assignation, CompleteDSLPckg_AbstractState, CompleteDSLPckg_Transition, CompleteDSLPckg_Wait, CompleteDSLPckg_StateMachine, NamedElement, CompleteDSLPckg_Region, CompleteDSLPckg_State, AbstractState, CompleteDSLPckg_Trigger, CompleteDSLPckg_AndTrigger, CompleteDSLPckg_Pseudostate, CompleteDSLPckg_InitialState, Pseudostate, CompleteDSLPckg_FinalState, State, CompleteDSLPckg_NamedElement, CompleteDSLPckg_NotTrigger, Trigger, CompleteDSLPckg_OrTrigger, RelationalOperator, ArithmeticOperator},
    associations={left0, left4, right6, right1, statements9, body17, condition10, body12, guard15, expr20, varRef22, expression24, subvertex28, transitions30, regions27, ownerRegion41, entryAction44, ownerStateMachine32, incoming35, outgoing38, target54, source57, doAction46, exitAction49, trigger52, trigger60, left62, right64, left67, right69},
    generalizations={gen_CompleteDSLPckg_Literal_Expression, gen_CompleteDSLPckg_ArithmeticExpression_Expression, gen_CompleteDSLPckg_IntegerLit_Literal, gen_CompleteDSLPckg_StringLit_Literal, gen_CompleteDSLPckg_BoolLit_Literal, gen_CompleteDSLPckg_RelationalExpression_Expression, gen_CompleteDSLPckg_Conditional_Statement, gen_CompleteDSLPckg_VarRef_Expression, gen_CompleteDSLPckg_VarDecl_Statement, gen_CompleteDSLPckg_Loop_Statement, gen_CompleteDSLPckg_ConsoleOutput_Statement, gen_CompleteDSLPckg_Println_ConsoleOutput, gen_CompleteDSLPckg_Print_ConsoleOutput, gen_CompleteDSLPckg_Assignation_Statement, gen_CompleteDSLPckg_Region_NamedElement, gen_CompleteDSLPckg_Wait_Statement, gen_CompleteDSLPckg_StateMachine_NamedElement, gen_CompleteDSLPckg_State_AbstractState, gen_CompleteDSLPckg_AbstractState_NamedElement, gen_CompleteDSLPckg_Transition_NamedElement, gen_CompleteDSLPckg_AndTrigger_Trigger, gen_CompleteDSLPckg_Pseudostate_AbstractState, gen_CompleteDSLPckg_InitialState_Pseudostate, gen_CompleteDSLPckg_FinalState_State, gen_CompleteDSLPckg_NotTrigger_Trigger, gen_CompleteDSLPckg_OrTrigger_Trigger},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)