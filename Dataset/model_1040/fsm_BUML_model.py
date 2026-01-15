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
fsm_StateMachine = Class(name="fsm::StateMachine")
fsm_Region = Class(name="fsm::Region")
fsm_Trigger = Class(name="fsm::Trigger")
fsm_Statement = Class(name="fsm::Statement", is_abstract=True)
fsm_Constraint = Class(name="fsm::Constraint")
fsm_AbstractState = Class(name="fsm::AbstractState", is_abstract=True)
fsm_Transition = Class(name="fsm::Transition")
fsm_State = Class(name="fsm::State")
AbstractState = Class(name="AbstractState")
fsm_Block = Class(name="fsm::Block")
fsm_OrTrigger = Class(name="fsm::OrTrigger")
fsm_Pseudostate = Class(name="fsm::Pseudostate", is_abstract=True)
fsm_InitialState = Class(name="fsm::InitialState")
Pseudostate = Class(name="Pseudostate")
fsm_Fork = Class(name="fsm::Fork")
fsm_Join = Class(name="fsm::Join")
fsm_NotTrigger = Class(name="fsm::NotTrigger")
Trigger = Class(name="Trigger")
fsm_AndTrigger = Class(name="fsm::AndTrigger")
fsm_Loop = Class(name="fsm::Loop")
fsm_Expression = Class(name="fsm::Expression", is_abstract=True)
fsm_Conditional = Class(name="fsm::Conditional")
fsm_DeepHistory = Class(name="fsm::DeepHistory")
fsm_ShallowHistory = Class(name="fsm::ShallowHistory")
fsm_Junction = Class(name="fsm::Junction")
fsm_Condition = Class(name="fsm::Condition")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
fsm_Context = Class(name="fsm::Context")
Statement = Class(name="Statement")
fsm_ArithmeticExpression = Class(name="fsm::ArithmeticExpression")
fsm_Literal = Class(name="fsm::Literal", is_abstract=True)
fsm_Integer = Class(name="fsm::Integer")
Literal = Class(name="Literal")
fsm_Boolean = Class(name="fsm::Boolean")
fsm_Real = Class(name="fsm::Real")
fsm_String = Class(name="fsm::String")
fsm_VarRef = Class(name="fsm::VarRef")
fsm_VarDecl = Class(name="fsm::VarDecl")
fsm_Assignation = Class(name="fsm::Assignation")
fsm_RelationalExpression = Class(name="fsm::RelationalExpression")
Expression = Class(name="Expression")

# fsm_StateMachine class attributes and methods

# fsm_Region class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Statement class attributes and methods

# fsm_Constraint class attributes and methods

# fsm_AbstractState class attributes and methods

# fsm_Transition class attributes and methods

# fsm_State class attributes and methods

# AbstractState class attributes and methods

# fsm_Block class attributes and methods

# fsm_OrTrigger class attributes and methods

# fsm_Pseudostate class attributes and methods

# fsm_InitialState class attributes and methods

# Pseudostate class attributes and methods

# fsm_Fork class attributes and methods

# fsm_Join class attributes and methods

# fsm_NotTrigger class attributes and methods

# Trigger class attributes and methods

# fsm_AndTrigger class attributes and methods

# fsm_Loop class attributes and methods

# fsm_Expression class attributes and methods

# fsm_Conditional class attributes and methods

# fsm_DeepHistory class attributes and methods

# fsm_ShallowHistory class attributes and methods

# fsm_Junction class attributes and methods

# fsm_Condition class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_Context class attributes and methods

# Statement class attributes and methods

# fsm_ArithmeticExpression class attributes and methods

# fsm_Literal class attributes and methods

# fsm_Integer class attributes and methods

# Literal class attributes and methods

# fsm_Boolean class attributes and methods

# fsm_Real class attributes and methods

# fsm_String class attributes and methods

# fsm_VarRef class attributes and methods
fsm_VarRef_varId: Property = Property(name="varId", type=StringType)
fsm_VarRef.attributes={fsm_VarRef_varId}

# fsm_VarDecl class attributes and methods

# fsm_Assignation class attributes and methods

# fsm_RelationalExpression class attributes and methods

# Expression class attributes and methods

# Relationships
regions0: BinaryAssociation = BinaryAssociation(
    name="regions0",
    ends={
        Property(name="fsm_Region", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRegions10: BinaryAssociation = BinaryAssociation(
    name="ownedRegions10",
    ends={
        Property(name="Region11", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger12: BinaryAssociation = BinaryAssociation(
    name="trigger12",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition13", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="AbstractState15", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
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
subvertex1: BinaryAssociation = BinaryAssociation(
    name="subvertex1",
    ends={
        Property(name="AbstractState", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="fsm_Transition", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine4: BinaryAssociation = BinaryAssociation(
    name="stateMachine4",
    ends={
        Property(name="State", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRegions", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
region8: BinaryAssociation = BinaryAssociation(
    name="region8",
    ends={
        Property(name="Region", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=fsm_Region, multiplicity=Multiplicity(1, 1))
    }
)
doActivity9: BinaryAssociation = BinaryAssociation(
    name="doActivity9",
    ends={
        Property(name="fsm_Block", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left29: BinaryAssociation = BinaryAssociation(
    name="left29",
    ends={
        Property(name="fsm_Trigger30", type=fsm_OrTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_OrTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
right31: BinaryAssociation = BinaryAssociation(
    name="right31",
    ends={
        Property(name="fsm_Trigger33", type=fsm_OrTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_OrTrigger32", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
trigger22: BinaryAssociation = BinaryAssociation(
    name="trigger22",
    ends={
        Property(name="fsm_Trigger23", type=fsm_NotTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_NotTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
left24: BinaryAssociation = BinaryAssociation(
    name="left24",
    ends={
        Property(name="fsm_Trigger25", type=fsm_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_AndTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
right26: BinaryAssociation = BinaryAssociation(
    name="right26",
    ends={
        Property(name="fsm_Trigger28", type=fsm_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_AndTrigger27", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
statements36: BinaryAssociation = BinaryAssociation(
    name="statements36",
    ends={
        Property(name="fsm_Block37", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="fsm_Statement38", type=fsm_Block, multiplicity=Multiplicity(1, 1))
    }
)
body39: BinaryAssociation = BinaryAssociation(
    name="body39",
    ends={
        Property(name="fsm_Block40", type=fsm_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Loop", type=fsm_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard41: BinaryAssociation = BinaryAssociation(
    name="guard41",
    ends={
        Property(name="fsm_Expression", type=fsm_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Loop42", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body43: BinaryAssociation = BinaryAssociation(
    name="body43",
    ends={
        Property(name="fsm_Block44", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional", type=fsm_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context34: BinaryAssociation = BinaryAssociation(
    name="context34",
    ends={
        Property(name="fsm_Context", type=fsm_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Constraint35", type=fsm_Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="fsm_Expression58", type=fsm_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_ArithmeticExpression", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="fsm_Expression61", type=fsm_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_ArithmeticExpression60", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard45: BinaryAssociation = BinaryAssociation(
    name="guard45",
    ends={
        Property(name="fsm_Expression47", type=fsm_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Conditional46", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr48: BinaryAssociation = BinaryAssociation(
    name="expr48",
    ends={
        Property(name="fsm_Expression49", type=fsm_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_VarDecl", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr50: BinaryAssociation = BinaryAssociation(
    name="expr50",
    ends={
        Property(name="fsm_Expression51", type=fsm_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Assignation", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left52: BinaryAssociation = BinaryAssociation(
    name="left52",
    ends={
        Property(name="fsm_Expression53", type=fsm_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalExpression", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right54: BinaryAssociation = BinaryAssociation(
    name="right54",
    ends={
        Property(name="fsm_Expression56", type=fsm_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RelationalExpression55", type=fsm_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_fsm_State_AbstractState = Generalization(general=AbstractState, specific=fsm_State)
gen_fsm_OrTrigger_Trigger = Generalization(general=Trigger, specific=fsm_OrTrigger)
gen_fsm_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsm_Pseudostate)
gen_fsm_InitialState_Pseudostate = Generalization(general=Pseudostate, specific=fsm_InitialState)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_NotTrigger_Trigger = Generalization(general=Trigger, specific=fsm_NotTrigger)
gen_fsm_AndTrigger_Trigger = Generalization(general=Trigger, specific=fsm_AndTrigger)
gen_fsm_Loop_Statement = Generalization(general=Statement, specific=fsm_Loop)
gen_fsm_Conditional_Statement = Generalization(general=Statement, specific=fsm_Conditional)
gen_fsm_DeepHistory_Pseudostate = Generalization(general=Pseudostate, specific=fsm_DeepHistory)
gen_fsm_ShallowHistory_Pseudostate = Generalization(general=Pseudostate, specific=fsm_ShallowHistory)
gen_fsm_Junction_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Junction)
gen_fsm_Condition_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Condition)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_Block_Statement = Generalization(general=Statement, specific=fsm_Block)
gen_fsm_ArithmeticExpression_Expression = Generalization(general=Expression, specific=fsm_ArithmeticExpression)
gen_fsm_Literal_Expression = Generalization(general=Expression, specific=fsm_Literal)
gen_fsm_Integer_Literal = Generalization(general=Literal, specific=fsm_Integer)
gen_fsm_Boolean_Literal = Generalization(general=Literal, specific=fsm_Boolean)
gen_fsm_Real_Literal = Generalization(general=Literal, specific=fsm_Real)
gen_fsm_String_Literal = Generalization(general=Literal, specific=fsm_String)
gen_fsm_VarRef_Literal = Generalization(general=Literal, specific=fsm_VarRef)
gen_fsm_VarDecl_Statement = Generalization(general=Statement, specific=fsm_VarDecl)
gen_fsm_Assignation_Statement = Generalization(general=Statement, specific=fsm_Assignation)
gen_fsm_RelationalExpression_Expression = Generalization(general=Expression, specific=fsm_RelationalExpression)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, fsm_Region, fsm_Trigger, fsm_Statement, fsm_Constraint, fsm_AbstractState, fsm_Transition, fsm_State, AbstractState, fsm_Block, fsm_OrTrigger, fsm_Pseudostate, fsm_InitialState, Pseudostate, fsm_Fork, fsm_Join, fsm_NotTrigger, Trigger, fsm_AndTrigger, fsm_Loop, fsm_Expression, fsm_Conditional, fsm_DeepHistory, fsm_ShallowHistory, fsm_Junction, fsm_Condition, fsm_FinalState, State, fsm_Context, Statement, fsm_ArithmeticExpression, fsm_Literal, fsm_Integer, Literal, fsm_Boolean, fsm_Real, fsm_String, fsm_VarRef, fsm_VarDecl, fsm_Assignation, fsm_RelationalExpression, Expression},
    associations={regions0, ownedRegions10, trigger12, target14, source16, effect18, guard20, subvertex1, transitions2, stateMachine4, incoming5, outgoing6, region8, doActivity9, left29, right31, trigger22, left24, right26, statements36, body39, guard41, body43, context34, left57, right59, guard45, expr48, expr50, left52, right54},
    generalizations={gen_fsm_State_AbstractState, gen_fsm_OrTrigger_Trigger, gen_fsm_Pseudostate_AbstractState, gen_fsm_InitialState_Pseudostate, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_NotTrigger_Trigger, gen_fsm_AndTrigger_Trigger, gen_fsm_Loop_Statement, gen_fsm_Conditional_Statement, gen_fsm_DeepHistory_Pseudostate, gen_fsm_ShallowHistory_Pseudostate, gen_fsm_Junction_Pseudostate, gen_fsm_Condition_Pseudostate, gen_fsm_FinalState_State, gen_fsm_Block_Statement, gen_fsm_ArithmeticExpression_Expression, gen_fsm_Literal_Expression, gen_fsm_Integer_Literal, gen_fsm_Boolean_Literal, gen_fsm_Real_Literal, gen_fsm_String_Literal, gen_fsm_VarRef_Literal, gen_fsm_VarDecl_Statement, gen_fsm_Assignation_Statement, gen_fsm_RelationalExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)