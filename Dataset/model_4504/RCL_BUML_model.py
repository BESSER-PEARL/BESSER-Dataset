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
NumericOperator: Enumeration = Enumeration(
    name="NumericOperator",
    literals={
            EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="leq"),
			EnumerationLiteral(name="geq")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="neq")
    }
)

StringOperator: Enumeration = Enumeration(
    name="StringOperator",
    literals={
            EnumerationLiteral(name="neq"),
			EnumerationLiteral(name="eq")
    }
)

# Classes
rcl_RoverProgram = Class(name="rcl::RoverProgram")
rcl_Param = Class(name="rcl::Param")
rcl_RclBlock = Class(name="rcl::RclBlock")
rcl_Statement = Class(name="rcl::Statement", is_abstract=True)
rcl_VarAssignment = Class(name="rcl::VarAssignment")
Statement = Class(name="Statement")
rcl_RoverValue = Class(name="rcl::RoverValue", is_abstract=True)
rcl_Conditional = Class(name="rcl::Conditional")
rcl_RoverExpression = Class(name="rcl::RoverExpression", is_abstract=True)
rcl_Loop = Class(name="rcl::Loop")
rcl_MessageQuery = Class(name="rcl::MessageQuery")
StringValue = Class(name="StringValue")
rcl_ObstacleQuery = Class(name="rcl::ObstacleQuery")
BooleanValue = Class(name="BooleanValue")
rcl_NumericExpression = Class(name="rcl::NumericExpression")
RoverExpression = Class(name="RoverExpression")
rcl_NumberValue = Class(name="rcl::NumberValue")
rcl_StringExpression = Class(name="rcl::StringExpression")
rcl_StringValue = Class(name="rcl::StringValue")
rcl_BooleanExpression = Class(name="rcl::BooleanExpression")
rcl_BooleanValue = Class(name="rcl::BooleanValue")
RoverValue = Class(name="RoverValue")
rcl_Query = Class(name="rcl::Query", is_abstract=True)
rcl_TemperatureQuery = Class(name="rcl::TemperatureQuery")
Query = Class(name="Query")
NumberValue = Class(name="NumberValue")
rcl_HumidityQuery = Class(name="rcl::HumidityQuery")
rcl_Action = Class(name="rcl::Action", is_abstract=True)
rcl_ForwardAction = Class(name="rcl::ForwardAction")
Action = Class(name="Action")
rcl_ForwardMinAction = Class(name="rcl::ForwardMinAction")
rcl_BackwardAction = Class(name="rcl::BackwardAction")
rcl_BackwardMinAction = Class(name="rcl::BackwardMinAction")
rcl_TurnAction = Class(name="rcl::TurnAction")
rcl_TurnDegAction = Class(name="rcl::TurnDegAction")
rcl_StopAction = Class(name="rcl::StopAction")
rcl_LogAction = Class(name="rcl::LogAction")
rcl_SendAction = Class(name="rcl::SendAction")
rcl_VarRef = Class(name="rcl::VarRef")

# rcl_RoverProgram class attributes and methods
rcl_RoverProgram_name: Property = Property(name="name", type=StringType)
rcl_RoverProgram.attributes={rcl_RoverProgram_name}

# rcl_Param class attributes and methods
rcl_Param_name: Property = Property(name="name", type=StringType)
rcl_Param.attributes={rcl_Param_name}

# rcl_RclBlock class attributes and methods

# rcl_Statement class attributes and methods

# rcl_VarAssignment class attributes and methods
rcl_VarAssignment_name: Property = Property(name="name", type=StringType)
rcl_VarAssignment.attributes={rcl_VarAssignment_name}

# Statement class attributes and methods

# rcl_RoverValue class attributes and methods

# rcl_Conditional class attributes and methods

# rcl_RoverExpression class attributes and methods

# rcl_Loop class attributes and methods

# rcl_MessageQuery class attributes and methods

# StringValue class attributes and methods

# rcl_ObstacleQuery class attributes and methods
rcl_ObstacleQuery_front: Property = Property(name="front", type=BooleanType)
rcl_ObstacleQuery.attributes={rcl_ObstacleQuery_front}

# BooleanValue class attributes and methods

# rcl_NumericExpression class attributes and methods
rcl_NumericExpression_op: Property = Property(name="op", type=StringType)
rcl_NumericExpression.attributes={rcl_NumericExpression_op}

# RoverExpression class attributes and methods

# rcl_NumberValue class attributes and methods
rcl_NumberValue_nValue: Property = Property(name="nValue", type=IntegerType)
rcl_NumberValue.attributes={rcl_NumberValue_nValue}

# rcl_StringExpression class attributes and methods
rcl_StringExpression_op: Property = Property(name="op", type=StringType)
rcl_StringExpression.attributes={rcl_StringExpression_op}

# rcl_StringValue class attributes and methods
rcl_StringValue_sValue: Property = Property(name="sValue", type=StringType)
rcl_StringValue.attributes={rcl_StringValue_sValue}

# rcl_BooleanExpression class attributes and methods
rcl_BooleanExpression_op: Property = Property(name="op", type=StringType)
rcl_BooleanExpression.attributes={rcl_BooleanExpression_op}

# rcl_BooleanValue class attributes and methods
rcl_BooleanValue_bValue: Property = Property(name="bValue", type=BooleanType)
rcl_BooleanValue.attributes={rcl_BooleanValue_bValue}

# RoverValue class attributes and methods

# rcl_Query class attributes and methods

# rcl_TemperatureQuery class attributes and methods

# Query class attributes and methods

# NumberValue class attributes and methods

# rcl_HumidityQuery class attributes and methods

# rcl_Action class attributes and methods

# rcl_ForwardAction class attributes and methods

# Action class attributes and methods

# rcl_ForwardMinAction class attributes and methods

# rcl_BackwardAction class attributes and methods

# rcl_BackwardMinAction class attributes and methods

# rcl_TurnAction class attributes and methods

# rcl_TurnDegAction class attributes and methods

# rcl_StopAction class attributes and methods

# rcl_LogAction class attributes and methods
rcl_LogAction_message: Property = Property(name="message", type=StringType)
rcl_LogAction.attributes={rcl_LogAction_message}

# rcl_SendAction class attributes and methods
rcl_SendAction_message: Property = Property(name="message", type=StringType)
rcl_SendAction.attributes={rcl_SendAction_message}

# rcl_VarRef class attributes and methods
rcl_VarRef_name: Property = Property(name="name", type=StringType)
rcl_VarRef.attributes={rcl_VarRef_name}

# Relationships
params0: BinaryAssociation = BinaryAssociation(
    name="params0",
    ends={
        Property(name="rcl_Param", type=rcl_RoverProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_RoverProgram", type=rcl_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block1: BinaryAssociation = BinaryAssociation(
    name="block1",
    ends={
        Property(name="rcl_RclBlock", type=rcl_RoverProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_RoverProgram2", type=rcl_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enclosing3: BinaryAssociation = BinaryAssociation(
    name="enclosing3",
    ends={
        Property(name="4", type=rcl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=rcl_RclBlock, multiplicity=Multiplicity(0, 1))
    }
)
value5: BinaryAssociation = BinaryAssociation(
    name="value5",
    ends={
        Property(name="rcl_RoverValue", type=rcl_VarAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_VarAssignment", type=rcl_RoverValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr6: BinaryAssociation = BinaryAssociation(
    name="expr6",
    ends={
        Property(name="rcl_RoverExpression", type=rcl_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_Conditional", type=rcl_RoverExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condTrue7: BinaryAssociation = BinaryAssociation(
    name="condTrue7",
    ends={
        Property(name="rcl_RclBlock9", type=rcl_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_Conditional8", type=rcl_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condFalse10: BinaryAssociation = BinaryAssociation(
    name="condFalse10",
    ends={
        Property(name="rcl_RclBlock12", type=rcl_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_Conditional11", type=rcl_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr13: BinaryAssociation = BinaryAssociation(
    name="expr13",
    ends={
        Property(name="rcl_RoverExpression14", type=rcl_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_Loop", type=rcl_RoverExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block15: BinaryAssociation = BinaryAssociation(
    name="block15",
    ends={
        Property(name="rcl_RclBlock17", type=rcl_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_Loop16", type=rcl_RclBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts18: BinaryAssociation = BinaryAssociation(
    name="stmts18",
    ends={
        Property(name="20", type=rcl_RclBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="19", type=rcl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs21: BinaryAssociation = BinaryAssociation(
    name="lhs21",
    ends={
        Property(name="rcl_NumberValue", type=rcl_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_NumericExpression", type=rcl_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs22: BinaryAssociation = BinaryAssociation(
    name="rhs22",
    ends={
        Property(name="rcl_NumberValue24", type=rcl_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_NumericExpression23", type=rcl_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs25: BinaryAssociation = BinaryAssociation(
    name="lhs25",
    ends={
        Property(name="rcl_StringValue", type=rcl_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_StringExpression", type=rcl_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs26: BinaryAssociation = BinaryAssociation(
    name="rhs26",
    ends={
        Property(name="rcl_StringValue28", type=rcl_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_StringExpression27", type=rcl_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs29: BinaryAssociation = BinaryAssociation(
    name="lhs29",
    ends={
        Property(name="rcl_BooleanValue", type=rcl_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_BooleanExpression", type=rcl_BooleanValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs30: BinaryAssociation = BinaryAssociation(
    name="rhs30",
    ends={
        Property(name="rcl_BooleanValue32", type=rcl_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_BooleanExpression31", type=rcl_BooleanValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distance33: BinaryAssociation = BinaryAssociation(
    name="distance33",
    ends={
        Property(name="rcl_NumberValue34", type=rcl_ForwardMinAction, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_ForwardMinAction", type=rcl_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
distance35: BinaryAssociation = BinaryAssociation(
    name="distance35",
    ends={
        Property(name="rcl_NumberValue36", type=rcl_BackwardMinAction, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_BackwardMinAction", type=rcl_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
degrees37: BinaryAssociation = BinaryAssociation(
    name="degrees37",
    ends={
        Property(name="rcl_NumberValue38", type=rcl_TurnDegAction, multiplicity=Multiplicity(1, 1)),
        Property(name="rcl_TurnDegAction", type=rcl_NumberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_rcl_VarAssignment_Statement = Generalization(general=Statement, specific=rcl_VarAssignment)
gen_rcl_Conditional_Statement = Generalization(general=Statement, specific=rcl_Conditional)
gen_rcl_Loop_Statement = Generalization(general=Statement, specific=rcl_Loop)
gen_rcl_RclBlock_Statement = Generalization(general=Statement, specific=rcl_RclBlock)
gen_rcl_HumidityQuery_NumberValue = Generalization(general=NumberValue, specific=rcl_HumidityQuery)
gen_rcl_MessageQuery_Query = Generalization(general=Query, specific=rcl_MessageQuery)
gen_rcl_MessageQuery_StringValue = Generalization(general=StringValue, specific=rcl_MessageQuery)
gen_rcl_ObstacleQuery_Query = Generalization(general=Query, specific=rcl_ObstacleQuery)
gen_rcl_ObstacleQuery_BooleanValue = Generalization(general=BooleanValue, specific=rcl_ObstacleQuery)
gen_rcl_NumericExpression_RoverExpression = Generalization(general=RoverExpression, specific=rcl_NumericExpression)
gen_rcl_StringExpression_RoverExpression = Generalization(general=RoverExpression, specific=rcl_StringExpression)
gen_rcl_BooleanExpression_RoverExpression = Generalization(general=RoverExpression, specific=rcl_BooleanExpression)
gen_rcl_NumberValue_RoverValue = Generalization(general=RoverValue, specific=rcl_NumberValue)
gen_rcl_StringValue_RoverValue = Generalization(general=RoverValue, specific=rcl_StringValue)
gen_rcl_BooleanValue_RoverValue = Generalization(general=RoverValue, specific=rcl_BooleanValue)
gen_rcl_TemperatureQuery_Query = Generalization(general=Query, specific=rcl_TemperatureQuery)
gen_rcl_TemperatureQuery_NumberValue = Generalization(general=NumberValue, specific=rcl_TemperatureQuery)
gen_rcl_HumidityQuery_Query = Generalization(general=Query, specific=rcl_HumidityQuery)
gen_rcl_Action_Statement = Generalization(general=Statement, specific=rcl_Action)
gen_rcl_ForwardAction_Action = Generalization(general=Action, specific=rcl_ForwardAction)
gen_rcl_ForwardMinAction_Action = Generalization(general=Action, specific=rcl_ForwardMinAction)
gen_rcl_BackwardAction_Action = Generalization(general=Action, specific=rcl_BackwardAction)
gen_rcl_BackwardMinAction_Action = Generalization(general=Action, specific=rcl_BackwardMinAction)
gen_rcl_TurnAction_Action = Generalization(general=Action, specific=rcl_TurnAction)
gen_rcl_TurnDegAction_Action = Generalization(general=Action, specific=rcl_TurnDegAction)
gen_rcl_StopAction_Action = Generalization(general=Action, specific=rcl_StopAction)
gen_rcl_LogAction_Action = Generalization(general=Action, specific=rcl_LogAction)
gen_rcl_SendAction_Action = Generalization(general=Action, specific=rcl_SendAction)
gen_rcl_VarRef_BooleanValue = Generalization(general=BooleanValue, specific=rcl_VarRef)
gen_rcl_VarRef_NumberValue = Generalization(general=NumberValue, specific=rcl_VarRef)
gen_rcl_VarRef_StringValue = Generalization(general=StringValue, specific=rcl_VarRef)
gen_rcl_VarRef_Statement = Generalization(general=Statement, specific=rcl_VarRef)

# Domain Model
domain_model = DomainModel(
    name="rcl",
    types={rcl_RoverProgram, rcl_Param, rcl_RclBlock, rcl_Statement, rcl_VarAssignment, Statement, rcl_RoverValue, rcl_Conditional, rcl_RoverExpression, rcl_Loop, rcl_MessageQuery, StringValue, rcl_ObstacleQuery, BooleanValue, rcl_NumericExpression, RoverExpression, rcl_NumberValue, rcl_StringExpression, rcl_StringValue, rcl_BooleanExpression, rcl_BooleanValue, RoverValue, rcl_Query, rcl_TemperatureQuery, Query, NumberValue, rcl_HumidityQuery, rcl_Action, rcl_ForwardAction, Action, rcl_ForwardMinAction, rcl_BackwardAction, rcl_BackwardMinAction, rcl_TurnAction, rcl_TurnDegAction, rcl_StopAction, rcl_LogAction, rcl_SendAction, rcl_VarRef, NumericOperator, BooleanOperator, StringOperator},
    associations={params0, block1, enclosing3, value5, expr6, condTrue7, condFalse10, expr13, block15, stmts18, lhs21, rhs22, lhs25, rhs26, lhs29, rhs30, distance33, distance35, degrees37},
    generalizations={gen_rcl_VarAssignment_Statement, gen_rcl_Conditional_Statement, gen_rcl_Loop_Statement, gen_rcl_RclBlock_Statement, gen_rcl_HumidityQuery_NumberValue, gen_rcl_MessageQuery_Query, gen_rcl_MessageQuery_StringValue, gen_rcl_ObstacleQuery_Query, gen_rcl_ObstacleQuery_BooleanValue, gen_rcl_NumericExpression_RoverExpression, gen_rcl_StringExpression_RoverExpression, gen_rcl_BooleanExpression_RoverExpression, gen_rcl_NumberValue_RoverValue, gen_rcl_StringValue_RoverValue, gen_rcl_BooleanValue_RoverValue, gen_rcl_TemperatureQuery_Query, gen_rcl_TemperatureQuery_NumberValue, gen_rcl_HumidityQuery_Query, gen_rcl_Action_Statement, gen_rcl_ForwardAction_Action, gen_rcl_ForwardMinAction_Action, gen_rcl_BackwardAction_Action, gen_rcl_BackwardMinAction_Action, gen_rcl_TurnAction_Action, gen_rcl_TurnDegAction_Action, gen_rcl_StopAction_Action, gen_rcl_LogAction_Action, gen_rcl_SendAction_Action, gen_rcl_VarRef_BooleanValue, gen_rcl_VarRef_NumberValue, gen_rcl_VarRef_StringValue, gen_rcl_VarRef_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)