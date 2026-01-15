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
gfsm_IntOperation = Class(name="gfsm::IntOperation", is_abstract=True)
gfsm_Transition = Class(name="gfsm::Transition")
gfsm_BooleanExpression = Class(name="gfsm::BooleanExpression", is_abstract=True)
gfsm_FSM = Class(name="gfsm::FSM")
gfsm_State = Class(name="gfsm::State")
gfsm_IntBinaryExpression = Class(name="gfsm::IntBinaryExpression", is_abstract=True)
IntExpression = Class(name="IntExpression")
gfsm_FinalState = Class(name="gfsm::FinalState")
State = Class(name="State")
gfsm_InitialState = Class(name="gfsm::InitialState")
gfsm_ConstExpr = Class(name="gfsm::ConstExpr")
gfsm_IntVarAssign = Class(name="gfsm::IntVarAssign")
IntOperation = Class(name="IntOperation")
gfsm_IntExpression = Class(name="gfsm::IntExpression", is_abstract=True)
gfsm_IntAdd = Class(name="gfsm::IntAdd")
IntBinaryExpression = Class(name="IntBinaryExpression")
gfsm_IntMult = Class(name="gfsm::IntMult")
gfsm_IntNeg = Class(name="gfsm::IntNeg")
gfsm_IntVarRef = Class(name="gfsm::IntVarRef")
gfsm_BooleanCompareExpression = Class(name="gfsm::BooleanCompareExpression", is_abstract=True)
gfsm_IntBlock = Class(name="gfsm::IntBlock")
gfsm_BooleanEqual = Class(name="gfsm::BooleanEqual")
BooleanCompareExpression = Class(name="BooleanCompareExpression")
gfsm_BooleanOr = Class(name="gfsm::BooleanOr")
BooleanBinaryExpression = Class(name="BooleanBinaryExpression")
gfsm_BooleanAnd = Class(name="gfsm::BooleanAnd")
gfsm_BooleanGreaterThan = Class(name="gfsm::BooleanGreaterThan")
gfsm_BooleanBinaryExpression = Class(name="gfsm::BooleanBinaryExpression", is_abstract=True)
BooleanExpression = Class(name="BooleanExpression")

# gfsm_IntOperation class attributes and methods

# gfsm_Transition class attributes and methods
gfsm_Transition_event: Property = Property(name="event", type=StringType)
gfsm_Transition.attributes={gfsm_Transition_event}

# gfsm_BooleanExpression class attributes and methods

# gfsm_FSM class attributes and methods
gfsm_FSM_name: Property = Property(name="name", type=StringType)
gfsm_FSM.attributes={gfsm_FSM_name}

# gfsm_State class attributes and methods
gfsm_State_name: Property = Property(name="name", type=StringType)
gfsm_State.attributes={gfsm_State_name}

# gfsm_IntBinaryExpression class attributes and methods

# IntExpression class attributes and methods

# gfsm_FinalState class attributes and methods

# State class attributes and methods

# gfsm_InitialState class attributes and methods

# gfsm_ConstExpr class attributes and methods
gfsm_ConstExpr_value: Property = Property(name="value", type=IntegerType)
gfsm_ConstExpr.attributes={gfsm_ConstExpr_value}

# gfsm_IntVarAssign class attributes and methods
gfsm_IntVarAssign_name: Property = Property(name="name", type=StringType)
gfsm_IntVarAssign.attributes={gfsm_IntVarAssign_name}

# IntOperation class attributes and methods

# gfsm_IntExpression class attributes and methods

# gfsm_IntAdd class attributes and methods

# IntBinaryExpression class attributes and methods

# gfsm_IntMult class attributes and methods

# gfsm_IntNeg class attributes and methods

# gfsm_IntVarRef class attributes and methods
gfsm_IntVarRef_name: Property = Property(name="name", type=StringType)
gfsm_IntVarRef.attributes={gfsm_IntVarRef_name}

# gfsm_BooleanCompareExpression class attributes and methods

# gfsm_IntBlock class attributes and methods

# gfsm_BooleanEqual class attributes and methods

# BooleanCompareExpression class attributes and methods

# gfsm_BooleanOr class attributes and methods

# BooleanBinaryExpression class attributes and methods

# gfsm_BooleanAnd class attributes and methods

# gfsm_BooleanGreaterThan class attributes and methods

# gfsm_BooleanBinaryExpression class attributes and methods

# BooleanExpression class attributes and methods

# Relationships
inExpression5: BinaryAssociation = BinaryAssociation(
    name="inExpression5",
    ends={
        Property(name="gfsm_IntOperation", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_State", type=gfsm_IntOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outExpression6: BinaryAssociation = BinaryAssociation(
    name="outExpression6",
    ends={
        Property(name="gfsm_IntOperation8", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_State7", type=gfsm_IntOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fsm9: BinaryAssociation = BinaryAssociation(
    name="fsm9",
    ends={
        Property(name="FSM10", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=gfsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
guard0: BinaryAssociation = BinaryAssociation(
    name="guard0",
    ends={
        Property(name="gfsm_BooleanExpression", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_Transition", type=gfsm_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fsm1: BinaryAssociation = BinaryAssociation(
    name="fsm1",
    ends={
        Property(name="FSM", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=gfsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
from2: BinaryAssociation = BinaryAssociation(
    name="from2",
    ends={
        Property(name="State", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingtransitions", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
to3: BinaryAssociation = BinaryAssociation(
    name="to3",
    ends={
        Property(name="State4", type=gfsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incommingtransitions", type=gfsm_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions16: BinaryAssociation = BinaryAssociation(
    name="transitions16",
    ends={
        Property(name="Transition18", type=gfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm17", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate19: BinaryAssociation = BinaryAssociation(
    name="initialstate19",
    ends={
        Property(name="gfsm_InitialState", type=gfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_FSM", type=gfsm_InitialState, multiplicity=Multiplicity(1, 1))
    }
)
currentState20: BinaryAssociation = BinaryAssociation(
    name="currentState20",
    ends={
        Property(name="gfsm_State22", type=gfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_FSM21", type=gfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoingtransitions11: BinaryAssociation = BinaryAssociation(
    name="outgoingtransitions11",
    ends={
        Property(name="Transition", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incommingtransitions12: BinaryAssociation = BinaryAssociation(
    name="incommingtransitions12",
    ends={
        Property(name="Transition13", type=gfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=gfsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
states14: BinaryAssociation = BinaryAssociation(
    name="states14",
    ends={
        Property(name="State15", type=gfsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=gfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression123: BinaryAssociation = BinaryAssociation(
    name="expression123",
    ends={
        Property(name="gfsm_IntExpression", type=gfsm_IntBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_IntBinaryExpression", type=gfsm_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression224: BinaryAssociation = BinaryAssociation(
    name="expression224",
    ends={
        Property(name="gfsm_IntExpression26", type=gfsm_IntBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_IntBinaryExpression25", type=gfsm_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression27: BinaryAssociation = BinaryAssociation(
    name="expression27",
    ends={
        Property(name="gfsm_IntExpression28", type=gfsm_IntNeg, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_IntNeg", type=gfsm_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolExpression133: BinaryAssociation = BinaryAssociation(
    name="boolExpression133",
    ends={
        Property(name="gfsm_BooleanExpression34", type=gfsm_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_BooleanBinaryExpression", type=gfsm_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolExpression235: BinaryAssociation = BinaryAssociation(
    name="boolExpression235",
    ends={
        Property(name="gfsm_BooleanExpression37", type=gfsm_BooleanBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_BooleanBinaryExpression36", type=gfsm_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression138: BinaryAssociation = BinaryAssociation(
    name="expression138",
    ends={
        Property(name="gfsm_IntExpression39", type=gfsm_BooleanCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_BooleanCompareExpression", type=gfsm_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression29: BinaryAssociation = BinaryAssociation(
    name="expression29",
    ends={
        Property(name="gfsm_IntExpression30", type=gfsm_IntVarAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_IntVarAssign", type=gfsm_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations31: BinaryAssociation = BinaryAssociation(
    name="operations31",
    ends={
        Property(name="gfsm_IntVarAssign32", type=gfsm_IntBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_IntBlock", type=gfsm_IntVarAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression240: BinaryAssociation = BinaryAssociation(
    name="expression240",
    ends={
        Property(name="gfsm_IntExpression42", type=gfsm_BooleanCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gfsm_BooleanCompareExpression41", type=gfsm_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gfsm_FinalState_State = Generalization(general=State, specific=gfsm_FinalState)
gen_gfsm_InitialState_State = Generalization(general=State, specific=gfsm_InitialState)
gen_gfsm_ConstExpr_IntExpression = Generalization(general=IntExpression, specific=gfsm_ConstExpr)
gen_gfsm_IntVarAssign_IntOperation = Generalization(general=IntOperation, specific=gfsm_IntVarAssign)
gen_gfsm_IntBinaryExpression_IntExpression = Generalization(general=IntExpression, specific=gfsm_IntBinaryExpression)
gen_gfsm_IntAdd_IntBinaryExpression = Generalization(general=IntBinaryExpression, specific=gfsm_IntAdd)
gen_gfsm_IntMult_IntBinaryExpression = Generalization(general=IntBinaryExpression, specific=gfsm_IntMult)
gen_gfsm_IntNeg_IntExpression = Generalization(general=IntExpression, specific=gfsm_IntNeg)
gen_gfsm_IntVarRef_IntExpression = Generalization(general=IntExpression, specific=gfsm_IntVarRef)
gen_gfsm_BooleanCompareExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=gfsm_BooleanCompareExpression)
gen_gfsm_IntBlock_IntOperation = Generalization(general=IntOperation, specific=gfsm_IntBlock)
gen_gfsm_BooleanEqual_BooleanCompareExpression = Generalization(general=BooleanCompareExpression, specific=gfsm_BooleanEqual)
gen_gfsm_BooleanOr_BooleanBinaryExpression = Generalization(general=BooleanBinaryExpression, specific=gfsm_BooleanOr)
gen_gfsm_BooleanAnd_BooleanBinaryExpression = Generalization(general=BooleanBinaryExpression, specific=gfsm_BooleanAnd)
gen_gfsm_BooleanGreaterThan_BooleanCompareExpression = Generalization(general=BooleanCompareExpression, specific=gfsm_BooleanGreaterThan)
gen_gfsm_BooleanBinaryExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=gfsm_BooleanBinaryExpression)

# Domain Model
domain_model = DomainModel(
    name="gfsm",
    types={gfsm_IntOperation, gfsm_Transition, gfsm_BooleanExpression, gfsm_FSM, gfsm_State, gfsm_IntBinaryExpression, IntExpression, gfsm_FinalState, State, gfsm_InitialState, gfsm_ConstExpr, gfsm_IntVarAssign, IntOperation, gfsm_IntExpression, gfsm_IntAdd, IntBinaryExpression, gfsm_IntMult, gfsm_IntNeg, gfsm_IntVarRef, gfsm_BooleanCompareExpression, gfsm_IntBlock, gfsm_BooleanEqual, BooleanCompareExpression, gfsm_BooleanOr, BooleanBinaryExpression, gfsm_BooleanAnd, gfsm_BooleanGreaterThan, gfsm_BooleanBinaryExpression, BooleanExpression},
    associations={inExpression5, outExpression6, fsm9, guard0, fsm1, from2, to3, transitions16, initialstate19, currentState20, outgoingtransitions11, incommingtransitions12, states14, expression123, expression224, expression27, boolExpression133, boolExpression235, expression138, expression29, operations31, expression240},
    generalizations={gen_gfsm_FinalState_State, gen_gfsm_InitialState_State, gen_gfsm_ConstExpr_IntExpression, gen_gfsm_IntVarAssign_IntOperation, gen_gfsm_IntBinaryExpression_IntExpression, gen_gfsm_IntAdd_IntBinaryExpression, gen_gfsm_IntMult_IntBinaryExpression, gen_gfsm_IntNeg_IntExpression, gen_gfsm_IntVarRef_IntExpression, gen_gfsm_BooleanCompareExpression_BooleanExpression, gen_gfsm_IntBlock_IntOperation, gen_gfsm_BooleanEqual_BooleanCompareExpression, gen_gfsm_BooleanOr_BooleanBinaryExpression, gen_gfsm_BooleanAnd_BooleanBinaryExpression, gen_gfsm_BooleanGreaterThan_BooleanCompareExpression, gen_gfsm_BooleanBinaryExpression_BooleanExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)