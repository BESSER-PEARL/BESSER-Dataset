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
gx10_Program = Class(name="gx10::Program")
gx10_Method = Class(name="gx10::Method")
gx10_BoolExpression = Class(name="gx10::BoolExpression", is_abstract=True)
gx10_IntExpression = Class(name="gx10::IntExpression", is_abstract=True)
Expression = Class(name="Expression")
gx10_MethodCallParameter = Class(name="gx10::MethodCallParameter")
gx10_If = Class(name="gx10::If")
ControlStructure = Class(name="ControlStructure")
gx10_While = Class(name="gx10::While")
gx10_Block = Class(name="gx10::Block")
gx10_MethodCall = Class(name="gx10::MethodCall")
gx10_Referentiable = Class(name="gx10::Referentiable")
Statement = Class(name="Statement")
gx10_Statement = Class(name="gx10::Statement", is_abstract=True)
gx10_ControlStructure = Class(name="gx10::ControlStructure", is_abstract=True)
gx10_IntConst = Class(name="gx10::IntConst")
IntExpression = Class(name="IntExpression")
gx10_True = Class(name="gx10::True")
BoolExpression = Class(name="BoolExpression")
gx10_IntBinaryOperation = Class(name="gx10::IntBinaryOperation", is_abstract=True)
gx10_False = Class(name="gx10::False")
gx10_Not = Class(name="gx10::Not")
gx10_Async = Class(name="gx10::Async")
gx10_And = Class(name="gx10::And")
gx10_Expression = Class(name="gx10::Expression", is_abstract=True)
gx10_Finish = Class(name="gx10::Finish")
gx10_Print = Class(name="gx10::Print")
gx10_BoolVar = Class(name="gx10::BoolVar")
gx10_IntVar = Class(name="gx10::IntVar")
gx10_IntVarAccess = Class(name="gx10::IntVarAccess")
gx10_BoolVarAccess = Class(name="gx10::BoolVarAccess")
gx10_Equal = Class(name="gx10::Equal")
gx10_Plus = Class(name="gx10::Plus")
IntBinaryOperation = Class(name="IntBinaryOperation")
gx10_Time = Class(name="gx10::Time")

# gx10_Program class attributes and methods

# gx10_Method class attributes and methods
gx10_Method_name: Property = Property(name="name", type=StringType)
gx10_Method.attributes={gx10_Method_name}

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

# gx10_Block class attributes and methods
gx10_Block_context: Property = Property(name="context", type=IntegerType)
gx10_Block_m_initBlock: Method = Method(name="initBlock", parameters={})
gx10_Block.attributes={gx10_Block_context}
gx10_Block.methods={gx10_Block_m_initBlock}

# gx10_MethodCall class attributes and methods
gx10_MethodCall_m_call: Method = Method(name="call", parameters={})
gx10_MethodCall.methods={gx10_MethodCall_m_call}

# gx10_Referentiable class attributes and methods
gx10_Referentiable_name: Property = Property(name="name", type=IntegerType)
gx10_Referentiable.attributes={gx10_Referentiable_name}

# Statement class attributes and methods

# gx10_Statement class attributes and methods

# gx10_ControlStructure class attributes and methods

# gx10_IntConst class attributes and methods
gx10_IntConst_value: Property = Property(name="value", type=BooleanType)
gx10_IntConst_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_IntConst.attributes={gx10_IntConst_value}
gx10_IntConst.methods={gx10_IntConst_m_getCurrentValue}

# IntExpression class attributes and methods

# gx10_True class attributes and methods
gx10_True_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_True.methods={gx10_True_m_getCurrentValue}

# BoolExpression class attributes and methods

# gx10_IntBinaryOperation class attributes and methods
gx10_IntBinaryOperation_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_IntBinaryOperation.methods={gx10_IntBinaryOperation_m_evaluate}

# gx10_False class attributes and methods
gx10_False_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_False.methods={gx10_False_m_getCurrentValue}

# gx10_Not class attributes and methods
gx10_Not_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_Not.methods={gx10_Not_m_getCurrentValue}

# gx10_Async class attributes and methods

# gx10_And class attributes and methods

# gx10_Expression class attributes and methods

# gx10_Finish class attributes and methods

# gx10_Print class attributes and methods
gx10_Print_m_print: Method = Method(name="print", parameters={})
gx10_Print.methods={gx10_Print_m_print}

# gx10_BoolVar class attributes and methods
gx10_BoolVar_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_BoolVar.methods={gx10_BoolVar_m_evaluate}

# gx10_IntVar class attributes and methods
gx10_IntVar_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_IntVar.methods={gx10_IntVar_m_evaluate}

# gx10_IntVarAccess class attributes and methods
gx10_IntVarAccess_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_IntVarAccess.methods={gx10_IntVarAccess_m_getCurrentValue}

# gx10_BoolVarAccess class attributes and methods
gx10_BoolVarAccess_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_BoolVarAccess.methods={gx10_BoolVarAccess_m_getCurrentValue}

# gx10_Equal class attributes and methods
gx10_Equal_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_Equal_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_Equal.methods={gx10_Equal_m_getCurrentValue, gx10_Equal_m_evaluate}

# gx10_Plus class attributes and methods
gx10_Plus_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_Plus_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_Plus.methods={gx10_Plus_m_evaluate, gx10_Plus_m_getCurrentValue}

# IntBinaryOperation class attributes and methods

# gx10_Time class attributes and methods
gx10_Time_m_evaluate: Method = Method(name="evaluate", parameters={})
gx10_Time_m_getCurrentValue: Method = Method(name="getCurrentValue", parameters={})
gx10_Time.methods={gx10_Time_m_getCurrentValue, gx10_Time_m_evaluate}

# Relationships
methods0: BinaryAssociation = BinaryAssociation(
    name="methods0",
    ends={
        Property(name="1", type=gx10_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=gx10_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startMethod2: BinaryAssociation = BinaryAssociation(
    name="startMethod2",
    ends={
        Property(name="gx10_Method", type=gx10_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Program", type=gx10_Method, multiplicity=Multiplicity(1, 1))
    }
)
inProgram3: BinaryAssociation = BinaryAssociation(
    name="inProgram3",
    ends={
        Property(name="5", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=gx10_Program, multiplicity=Multiplicity(1, 1))
    }
)
controlStructureCondition19: BinaryAssociation = BinaryAssociation(
    name="controlStructureCondition19",
    ends={
        Property(name="gx10_BoolExpression", type=gx10_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_ControlStructure", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inMethodCallParameter20: BinaryAssociation = BinaryAssociation(
    name="inMethodCallParameter20",
    ends={
        Property(name="22", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=gx10_MethodCallParameter, multiplicity=Multiplicity(0, 1))
    }
)
thenBlock23: BinaryAssociation = BinaryAssociation(
    name="thenBlock23",
    ends={
        Property(name="gx10_Block24", type=gx10_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_If", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock25: BinaryAssociation = BinaryAssociation(
    name="elseBlock25",
    ends={
        Property(name="gx10_Block27", type=gx10_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_If26", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whileBlock28: BinaryAssociation = BinaryAssociation(
    name="whileBlock28",
    ends={
        Property(name="gx10_Block29", type=gx10_While, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_While", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodBlock6: BinaryAssociation = BinaryAssociation(
    name="methodBlock6",
    ends={
        Property(name="gx10_Block", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Method7", type=gx10_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
calledBy8: BinaryAssociation = BinaryAssociation(
    name="calledBy8",
    ends={
        Property(name="10", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=gx10_MethodCall, multiplicity=Multiplicity(0, 9999))
    }
)
methodParameters11: BinaryAssociation = BinaryAssociation(
    name="methodParameters11",
    ends={
        Property(name="gx10_Referentiable", type=gx10_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Method12", type=gx10_Referentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockStatements13: BinaryAssociation = BinaryAssociation(
    name="blockStatements13",
    ends={
        Property(name="15", type=gx10_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=gx10_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inBlock16: BinaryAssociation = BinaryAssociation(
    name="inBlock16",
    ends={
        Property(name="18", type=gx10_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=gx10_Block, multiplicity=Multiplicity(0, 1))
    }
)
leftAndExpression32: BinaryAssociation = BinaryAssociation(
    name="leftAndExpression32",
    ends={
        Property(name="gx10_BoolExpression33", type=gx10_And, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_And", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightAndExpression34: BinaryAssociation = BinaryAssociation(
    name="rightAndExpression34",
    ends={
        Property(name="gx10_BoolExpression36", type=gx10_And, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_And35", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftBinaryExpression37: BinaryAssociation = BinaryAssociation(
    name="leftBinaryExpression37",
    ends={
        Property(name="gx10_IntExpression", type=gx10_IntBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntBinaryOperation", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightBinaryExpression38: BinaryAssociation = BinaryAssociation(
    name="rightBinaryExpression38",
    ends={
        Property(name="gx10_IntExpression40", type=gx10_IntBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntBinaryOperation39", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
notExpression30: BinaryAssociation = BinaryAssociation(
    name="notExpression30",
    ends={
        Property(name="gx10_BoolExpression31", type=gx10_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Not", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
asyncBlock41: BinaryAssociation = BinaryAssociation(
    name="asyncBlock41",
    ends={
        Property(name="gx10_Statement", type=gx10_Async, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Async", type=gx10_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodToCall42: BinaryAssociation = BinaryAssociation(
    name="methodToCall42",
    ends={
        Property(name="44", type=gx10_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="43", type=gx10_Method, multiplicity=Multiplicity(1, 1))
    }
)
methodCallParameters45: BinaryAssociation = BinaryAssociation(
    name="methodCallParameters45",
    ends={
        Property(name="47", type=gx10_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="46", type=gx10_MethodCallParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finishStatement48: BinaryAssociation = BinaryAssociation(
    name="finishStatement48",
    ends={
        Property(name="gx10_Statement49", type=gx10_Finish, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Finish", type=gx10_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toPrint50: BinaryAssociation = BinaryAssociation(
    name="toPrint50",
    ends={
        Property(name="gx10_Expression", type=gx10_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Print", type=gx10_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolVarExpr51: BinaryAssociation = BinaryAssociation(
    name="boolVarExpr51",
    ends={
        Property(name="gx10_BoolExpression52", type=gx10_BoolVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_BoolVar", type=gx10_BoolExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolVarName53: BinaryAssociation = BinaryAssociation(
    name="boolVarName53",
    ends={
        Property(name="gx10_Referentiable55", type=gx10_BoolVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_BoolVar54", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intVarExpr56: BinaryAssociation = BinaryAssociation(
    name="intVarExpr56",
    ends={
        Property(name="gx10_IntExpression57", type=gx10_IntVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntVar", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intVarName58: BinaryAssociation = BinaryAssociation(
    name="intVarName58",
    ends={
        Property(name="gx10_Referentiable60", type=gx10_IntVar, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntVar59", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intVarRef61: BinaryAssociation = BinaryAssociation(
    name="intVarRef61",
    ends={
        Property(name="gx10_Referentiable62", type=gx10_IntVarAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_IntVarAccess", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1))
    }
)
boolVarRef63: BinaryAssociation = BinaryAssociation(
    name="boolVarRef63",
    ends={
        Property(name="gx10_Referentiable64", type=gx10_BoolVarAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_BoolVarAccess", type=gx10_Referentiable, multiplicity=Multiplicity(1, 1))
    }
)
leftEqual65: BinaryAssociation = BinaryAssociation(
    name="leftEqual65",
    ends={
        Property(name="gx10_IntExpression66", type=gx10_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Equal", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightEqual67: BinaryAssociation = BinaryAssociation(
    name="rightEqual67",
    ends={
        Property(name="gx10_IntExpression69", type=gx10_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="gx10_Equal68", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodCallParameterExpr70: BinaryAssociation = BinaryAssociation(
    name="methodCallParameterExpr70",
    ends={
        Property(name="72", type=gx10_MethodCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="71", type=gx10_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inMethodCall73: BinaryAssociation = BinaryAssociation(
    name="inMethodCall73",
    ends={
        Property(name="75", type=gx10_MethodCallParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="74", type=gx10_MethodCall, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_gx10_IntExpression_Expression = Generalization(general=Expression, specific=gx10_IntExpression)
gen_gx10_BoolExpression_Expression = Generalization(general=Expression, specific=gx10_BoolExpression)
gen_gx10_If_ControlStructure = Generalization(general=ControlStructure, specific=gx10_If)
gen_gx10_While_ControlStructure = Generalization(general=ControlStructure, specific=gx10_While)
gen_gx10_Block_Statement = Generalization(general=Statement, specific=gx10_Block)
gen_gx10_ControlStructure_Statement = Generalization(general=Statement, specific=gx10_ControlStructure)
gen_gx10_IntConst_IntExpression = Generalization(general=IntExpression, specific=gx10_IntConst)
gen_gx10_True_BoolExpression = Generalization(general=BoolExpression, specific=gx10_True)
gen_gx10_IntBinaryOperation_IntExpression = Generalization(general=IntExpression, specific=gx10_IntBinaryOperation)
gen_gx10_False_BoolExpression = Generalization(general=BoolExpression, specific=gx10_False)
gen_gx10_Not_BoolExpression = Generalization(general=BoolExpression, specific=gx10_Not)
gen_gx10_Async_Statement = Generalization(general=Statement, specific=gx10_Async)
gen_gx10_MethodCall_Expression = Generalization(general=Expression, specific=gx10_MethodCall)
gen_gx10_And_BoolExpression = Generalization(general=BoolExpression, specific=gx10_And)
gen_gx10_Expression_Statement = Generalization(general=Statement, specific=gx10_Expression)
gen_gx10_Finish_Statement = Generalization(general=Statement, specific=gx10_Finish)
gen_gx10_Print_Statement = Generalization(general=Statement, specific=gx10_Print)
gen_gx10_BoolVar_Expression = Generalization(general=Expression, specific=gx10_BoolVar)
gen_gx10_IntVar_Statement = Generalization(general=Statement, specific=gx10_IntVar)
gen_gx10_IntVarAccess_IntExpression = Generalization(general=IntExpression, specific=gx10_IntVarAccess)
gen_gx10_BoolVarAccess_BoolExpression = Generalization(general=BoolExpression, specific=gx10_BoolVarAccess)
gen_gx10_Equal_BoolExpression = Generalization(general=BoolExpression, specific=gx10_Equal)
gen_gx10_Plus_IntBinaryOperation = Generalization(general=IntBinaryOperation, specific=gx10_Plus)
gen_gx10_Time_IntBinaryOperation = Generalization(general=IntBinaryOperation, specific=gx10_Time)

# Domain Model
domain_model = DomainModel(
    name="gx10",
    types={gx10_Program, gx10_Method, gx10_BoolExpression, gx10_IntExpression, Expression, gx10_MethodCallParameter, gx10_If, ControlStructure, gx10_While, gx10_Block, gx10_MethodCall, gx10_Referentiable, Statement, gx10_Statement, gx10_ControlStructure, gx10_IntConst, IntExpression, gx10_True, BoolExpression, gx10_IntBinaryOperation, gx10_False, gx10_Not, gx10_Async, gx10_And, gx10_Expression, gx10_Finish, gx10_Print, gx10_BoolVar, gx10_IntVar, gx10_IntVarAccess, gx10_BoolVarAccess, gx10_Equal, gx10_Plus, IntBinaryOperation, gx10_Time},
    associations={methods0, startMethod2, inProgram3, controlStructureCondition19, inMethodCallParameter20, thenBlock23, elseBlock25, whileBlock28, methodBlock6, calledBy8, methodParameters11, blockStatements13, inBlock16, leftAndExpression32, rightAndExpression34, leftBinaryExpression37, rightBinaryExpression38, notExpression30, asyncBlock41, methodToCall42, methodCallParameters45, finishStatement48, toPrint50, boolVarExpr51, boolVarName53, intVarExpr56, intVarName58, intVarRef61, boolVarRef63, leftEqual65, rightEqual67, methodCallParameterExpr70, inMethodCall73},
    generalizations={gen_gx10_IntExpression_Expression, gen_gx10_BoolExpression_Expression, gen_gx10_If_ControlStructure, gen_gx10_While_ControlStructure, gen_gx10_Block_Statement, gen_gx10_ControlStructure_Statement, gen_gx10_IntConst_IntExpression, gen_gx10_True_BoolExpression, gen_gx10_IntBinaryOperation_IntExpression, gen_gx10_False_BoolExpression, gen_gx10_Not_BoolExpression, gen_gx10_Async_Statement, gen_gx10_MethodCall_Expression, gen_gx10_And_BoolExpression, gen_gx10_Expression_Statement, gen_gx10_Finish_Statement, gen_gx10_Print_Statement, gen_gx10_BoolVar_Expression, gen_gx10_IntVar_Statement, gen_gx10_IntVarAccess_IntExpression, gen_gx10_BoolVarAccess_BoolExpression, gen_gx10_Equal_BoolExpression, gen_gx10_Plus_IntBinaryOperation, gen_gx10_Time_IntBinaryOperation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)