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
gx10_Program = Class(name="gx10_Program")
gx10_Method = Class(name="gx10_Method")
gx10_Block = Class(name="gx10_Block")
gx10_ControlStructure = Class(name="gx10_ControlStructure", is_abstract=True)
gx10_BoolExpression = Class(name="gx10_BoolExpression", is_abstract=True)
gx10_IntExpression = Class(name="gx10_IntExpression", is_abstract=True)
Expression = Class(name="Expression")
gx10_MethodCallParameter = Class(name="gx10_MethodCallParameter")
gx10_If = Class(name="gx10_If")
ControlStructure = Class(name="ControlStructure")
gx10_While = Class(name="gx10_While")
gx10_True = Class(name="gx10_True")
BoolExpression = Class(name="BoolExpression")
gx10_MethodCall = Class(name="gx10_MethodCall")
gx10_Referentiable = Class(name="gx10_Referentiable")
Statement = Class(name="Statement")
gx10_Statement = Class(name="gx10_Statement", is_abstract=True)
gx10_Async = Class(name="gx10_Async")
gx10_Expression = Class(name="gx10_Expression", is_abstract=True)
gx10_Finish = Class(name="gx10_Finish")
gx10_Print = Class(name="gx10_Print")
gx10_BoolVar = Class(name="gx10_BoolVar")
gx10_False = Class(name="gx10_False")
gx10_Not = Class(name="gx10_Not")
gx10_And = Class(name="gx10_And")
gx10_IntConst = Class(name="gx10_IntConst")
IntExpression = Class(name="IntExpression")
gx10_IntBinaryOperation = Class(name="gx10_IntBinaryOperation", is_abstract=True)
gx10_Equal = Class(name="gx10_Equal")
gx10_IntVar = Class(name="gx10_IntVar")
gx10_IntVarAccess = Class(name="gx10_IntVarAccess")
gx10_BoolVarAccess = Class(name="gx10_BoolVarAccess")
gx10_Plus = Class(name="gx10_Plus")
IntBinaryOperation = Class(name="IntBinaryOperation")
gx10_Time = Class(name="gx10_Time")

# gx10_Program class attributes and methods

# gx10_Method class attributes and methods
gx10_Method_name: Property = Property(name="name", type=BooleanType)
gx10_Method.attributes={gx10_Method_name}

# gx10_Block class attributes and methods
gx10_Block_m_initBlock: Method = Method(name="initBlock", parameters={})
gx10_Block.methods={gx10_Block_m_initBlock}

# gx10_ControlStructure class attributes and methods

# gx10_BoolExpression class attributes and methods
gx10_BoolExpression_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_BoolExpression.methods={gx10_BoolExpression_m_getCurrentValue}

# gx10_IntExpression class attributes and methods
gx10_IntExpression_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_IntExpression.methods={gx10_IntExpression_m_getCurrentValue}

# Expression class attributes and methods

# gx10_MethodCallParameter class attributes and methods
gx10_MethodCallParameter_name: Property = Property(name="name", type=StringType)
gx10_MethodCallParameter.attributes={gx10_MethodCallParameter_name}

# gx10_If class attributes and methods

# ControlStructure class attributes and methods

# gx10_While class attributes and methods

# gx10_True class attributes and methods

# BoolExpression class attributes and methods

# gx10_MethodCall class attributes and methods
gx10_MethodCall_m_call: Method = Method(name="call", parameters={})
gx10_MethodCall.methods={gx10_MethodCall_m_call}

# gx10_Referentiable class attributes and methods
gx10_Referentiable_name: Property = Property(name="name", type=StringType)
gx10_Referentiable.attributes={gx10_Referentiable_name}

# Statement class attributes and methods

# gx10_Statement class attributes and methods

# gx10_Async class attributes and methods

# gx10_Expression class attributes and methods

# gx10_Finish class attributes and methods

# gx10_Print class attributes and methods
gx10_Print_m_print: Method = Method(name="print", parameters={})
gx10_Print.methods={gx10_Print_m_print}

# gx10_BoolVar class attributes and methods
gx10_BoolVar_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_BoolVar.methods={gx10_BoolVar_m_evaluate}

# gx10_False class attributes and methods

# gx10_Not class attributes and methods

# gx10_And class attributes and methods

# gx10_IntConst class attributes and methods
gx10_IntConst_value: Property = Property(name="value", type=IntegerType)
gx10_IntConst.attributes={gx10_IntConst_value}

# IntExpression class attributes and methods

# gx10_IntBinaryOperation class attributes and methods
gx10_IntBinaryOperation_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_IntBinaryOperation.methods={gx10_IntBinaryOperation_m_evaluate}

# gx10_Equal class attributes and methods
gx10_Equal_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_Equal.methods={gx10_Equal_m_evaluate}

# gx10_IntVar class attributes and methods
gx10_IntVar_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_IntVar.methods={gx10_IntVar_m_evaluate}

# gx10_IntVarAccess class attributes and methods

# gx10_BoolVarAccess class attributes and methods

# gx10_Plus class attributes and methods

# IntBinaryOperation class attributes and methods

# gx10_Time class attributes and methods

# Relationships
methods0: BinaryAssociation = BinaryAssociation(
    name="methods0",
    ends={
        Property(name="Method", type=gx10_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="inProgram", type=gx10_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startMethod1: BinaryAssociation = BinaryAssociation(
    name="startMethod1",
    ends={
        Property(name="gx10_Method", type=gx10_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Program", type=gx10_Method, multiplicity=Multiplicity(1, 1))
    }
)
inProgram2: BinaryAssociation = BinaryAssociation(
    name="inProgram2",
    ends={
        Property(name="Program", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=gx10_Program, multiplicity=Multiplicity(1, 1))
    }
)
inBlock9: BinaryAssociation = BinaryAssociation(
    name="inBlock9",
    ends={
        Property(name="blockStatements", type=gx10_Block, multiplicity=Multiplicity(0, 1)),
        Property(name="Block", type=gx10_Statement, multiplicity=Multiplicity(1, 1))
    }
)
controlStructureCondition10: BinaryAssociation = BinaryAssociation(
    name="controlStructureCondition10",
    ends={
        Property(name="gx10_BoolExpression", type=gx10_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_ControlStructure", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inMethodCallParameter11: BinaryAssociation = BinaryAssociation(
    name="inMethodCallParameter11",
    ends={
        Property(name="MethodCallParameter", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="methodCallParameterExpr", type=gx10_MethodCallParameter, multiplicity=Multiplicity(0, 1))
    }
)
thenBlock12: BinaryAssociation = BinaryAssociation(
    name="thenBlock12",
    ends={
        Property(name="gx10_Block13", type=gx10_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_If", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock14: BinaryAssociation = BinaryAssociation(
    name="elseBlock14",
    ends={
        Property(name="gx10_Block16", type=gx10_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_If15", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whileBlock17: BinaryAssociation = BinaryAssociation(
    name="whileBlock17",
    ends={
        Property(name="gx10_Block18", type=gx10_While, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_While", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodBlock3: BinaryAssociation = BinaryAssociation(
    name="methodBlock3",
    ends={
        Property(name="gx10_Block", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Method4", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
calledBy5: BinaryAssociation = BinaryAssociation(
    name="calledBy5",
    ends={
        Property(name="MethodCall", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methodToCall", type=gx10_MethodCall, multiplicity=Multiplicity(0, 9999))
    }
)
methodParameters6: BinaryAssociation = BinaryAssociation(
    name="methodParameters6",
    ends={
        Property(name="gx10_Referentiable", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Method7", type=gx10_Referentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockStatements8: BinaryAssociation = BinaryAssociation(
    name="blockStatements8",
    ends={
        Property(name="Statement", type=gx10_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="inBlock", type=gx10_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftBinaryExpression26: BinaryAssociation = BinaryAssociation(
    name="leftBinaryExpression26",
    ends={
        Property(name="gx10_IntExpression", type=gx10_IntBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntBinaryOperation", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightBinaryExpression27: BinaryAssociation = BinaryAssociation(
    name="rightBinaryExpression27",
    ends={
        Property(name="gx10_IntExpression29", type=gx10_IntBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntBinaryOperation28", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
asyncBlock30: BinaryAssociation = BinaryAssociation(
    name="asyncBlock30",
    ends={
        Property(name="gx10_Statement", type=gx10_Async, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Async", type=gx10_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodToCall31: BinaryAssociation = BinaryAssociation(
    name="methodToCall31",
    ends={
        Property(name="Method32", type=gx10_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="calledBy", type=gx10_Method, multiplicity=Multiplicity(1, 1))
    }
)
methodCallParameters33: BinaryAssociation = BinaryAssociation(
    name="methodCallParameters33",
    ends={
        Property(name="MethodCallParameter34", type=gx10_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="inMethodCall", type=gx10_MethodCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finishStatement35: BinaryAssociation = BinaryAssociation(
    name="finishStatement35",
    ends={
        Property(name="gx10_Statement36", type=gx10_Finish, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Finish", type=gx10_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toPrint37: BinaryAssociation = BinaryAssociation(
    name="toPrint37",
    ends={
        Property(name="gx10_Expression", type=gx10_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Print", type=gx10_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
notExpression19: BinaryAssociation = BinaryAssociation(
    name="notExpression19",
    ends={
        Property(name="gx10_BoolExpression20", type=gx10_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Not", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftAndExpression21: BinaryAssociation = BinaryAssociation(
    name="leftAndExpression21",
    ends={
        Property(name="gx10_BoolExpression22", type=gx10_And, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_And", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightAndExpression23: BinaryAssociation = BinaryAssociation(
    name="rightAndExpression23",
    ends={
        Property(name="gx10_BoolExpression25", type=gx10_And, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_And24", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolVarRef50: BinaryAssociation = BinaryAssociation(
    name="boolVarRef50",
    ends={
        Property(name="gx10_Referentiable51", type=gx10_BoolVarAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_BoolVarAccess", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1))
    }
)
boolVarExpr38: BinaryAssociation = BinaryAssociation(
    name="boolVarExpr38",
    ends={
        Property(name="gx10_BoolExpression39", type=gx10_BoolVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_BoolVar", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolVarName40: BinaryAssociation = BinaryAssociation(
    name="boolVarName40",
    ends={
        Property(name="gx10_Referentiable42", type=gx10_BoolVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_BoolVar41", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intVarExpr43: BinaryAssociation = BinaryAssociation(
    name="intVarExpr43",
    ends={
        Property(name="gx10_IntExpression44", type=gx10_IntVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntVar", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intVarName45: BinaryAssociation = BinaryAssociation(
    name="intVarName45",
    ends={
        Property(name="gx10_Referentiable47", type=gx10_IntVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntVar46", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intVarRef48: BinaryAssociation = BinaryAssociation(
    name="intVarRef48",
    ends={
        Property(name="gx10_Referentiable49", type=gx10_IntVarAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntVarAccess", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1))
    }
)
methodCallParameterExpr57: BinaryAssociation = BinaryAssociation(
    name="methodCallParameterExpr57",
    ends={
        Property(name="IntExpression", type=gx10_MethodCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="inMethodCallParameter", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inMethodCall58: BinaryAssociation = BinaryAssociation(
    name="inMethodCall58",
    ends={
        Property(name="MethodCall59", type=gx10_MethodCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="methodCallParameters", type=gx10_MethodCall, multiplicity=Multiplicity(1, 1))
    }
)
leftEqual52: BinaryAssociation = BinaryAssociation(
    name="leftEqual52",
    ends={
        Property(name="gx10_IntExpression53", type=gx10_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Equal", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightEqual54: BinaryAssociation = BinaryAssociation(
    name="rightEqual54",
    ends={
        Property(name="gx10_IntExpression56", type=gx10_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Equal55", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gx10_ControlStructure_Statement = Generalization(general=Statement, specific=gx10_ControlStructure)
gen_gx10_IntExpression_Expression = Generalization(general=Expression, specific=gx10_IntExpression)
gen_gx10_BoolExpression_Expression = Generalization(general=Expression, specific=gx10_BoolExpression)
gen_gx10_If_ControlStructure = Generalization(general=ControlStructure, specific=gx10_If)
gen_gx10_While_ControlStructure = Generalization(general=ControlStructure, specific=gx10_While)
gen_gx10_Block_Statement = Generalization(general=Statement, specific=gx10_Block)
gen_gx10_Async_Statement = Generalization(general=Statement, specific=gx10_Async)
gen_gx10_MethodCall_Expression = Generalization(general=Expression, specific=gx10_MethodCall)
gen_gx10_Expression_Statement = Generalization(general=Statement, specific=gx10_Expression)
gen_gx10_Finish_Statement = Generalization(general=Statement, specific=gx10_Finish)
gen_gx10_Print_Statement = Generalization(general=Statement, specific=gx10_Print)
gen_gx10_BoolVar_Expression = Generalization(general=Expression, specific=gx10_BoolVar)
gen_gx10_True_BoolExpression = Generalization(general=BoolExpression, specific=gx10_True)
gen_gx10_False_BoolExpression = Generalization(general=BoolExpression, specific=gx10_False)
gen_gx10_Not_BoolExpression = Generalization(general=BoolExpression, specific=gx10_Not)
gen_gx10_And_BoolExpression = Generalization(general=BoolExpression, specific=gx10_And)
gen_gx10_IntConst_IntExpression = Generalization(general=IntExpression, specific=gx10_IntConst)
gen_gx10_IntBinaryOperation_IntExpression = Generalization(general=IntExpression, specific=gx10_IntBinaryOperation)
gen_gx10_Equal_BoolExpression = Generalization(general=BoolExpression, specific=gx10_Equal)
gen_gx10_IntVar_Statement = Generalization(general=Statement, specific=gx10_IntVar)
gen_gx10_IntVarAccess_IntExpression = Generalization(general=IntExpression, specific=gx10_IntVarAccess)
gen_gx10_BoolVarAccess_BoolExpression = Generalization(general=BoolExpression, specific=gx10_BoolVarAccess)
gen_gx10_Plus_IntBinaryOperation = Generalization(general=IntBinaryOperation, specific=gx10_Plus)
gen_gx10_Time_IntBinaryOperation = Generalization(general=IntBinaryOperation, specific=gx10_Time)

# Domain Model
domain_model = DomainModel(
    name="gx10",
    types={gx10_Program, gx10_Method, gx10_Block, gx10_ControlStructure, gx10_BoolExpression, gx10_IntExpression, Expression, gx10_MethodCallParameter, gx10_If, ControlStructure, gx10_While, gx10_True, BoolExpression, gx10_MethodCall, gx10_Referentiable, Statement, gx10_Statement, gx10_Async, gx10_Expression, gx10_Finish, gx10_Print, gx10_BoolVar, gx10_False, gx10_Not, gx10_And, gx10_IntConst, IntExpression, gx10_IntBinaryOperation, gx10_Equal, gx10_IntVar, gx10_IntVarAccess, gx10_BoolVarAccess, gx10_Plus, IntBinaryOperation, gx10_Time},
    associations={methods0, startMethod1, inProgram2, inBlock9, controlStructureCondition10, inMethodCallParameter11, thenBlock12, elseBlock14, whileBlock17, methodBlock3, calledBy5, methodParameters6, blockStatements8, leftBinaryExpression26, rightBinaryExpression27, asyncBlock30, methodToCall31, methodCallParameters33, finishStatement35, toPrint37, notExpression19, leftAndExpression21, rightAndExpression23, boolVarRef50, boolVarExpr38, boolVarName40, intVarExpr43, intVarName45, intVarRef48, methodCallParameterExpr57, inMethodCall58, leftEqual52, rightEqual54},
    generalizations={gen_gx10_ControlStructure_Statement, gen_gx10_IntExpression_Expression, gen_gx10_BoolExpression_Expression, gen_gx10_If_ControlStructure, gen_gx10_While_ControlStructure, gen_gx10_Block_Statement, gen_gx10_Async_Statement, gen_gx10_MethodCall_Expression, gen_gx10_Expression_Statement, gen_gx10_Finish_Statement, gen_gx10_Print_Statement, gen_gx10_BoolVar_Expression, gen_gx10_True_BoolExpression, gen_gx10_False_BoolExpression, gen_gx10_Not_BoolExpression, gen_gx10_And_BoolExpression, gen_gx10_IntConst_IntExpression, gen_gx10_IntBinaryOperation_IntExpression, gen_gx10_Equal_BoolExpression, gen_gx10_IntVar_Statement, gen_gx10_IntVarAccess_IntExpression, gen_gx10_BoolVarAccess_BoolExpression, gen_gx10_Plus_IntBinaryOperation, gen_gx10_Time_IntBinaryOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)