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
arduinoDSL_Program = Class(name="arduinoDSL::Program")
arduinoDSL_EObject = Class(name="arduinoDSL::EObject")
arduinoDSL_Rule = Class(name="arduinoDSL::Rule")
arduinoDSL_BooleanExpression = Class(name="arduinoDSL::BooleanExpression")
arduinoDSL_RuleBody = Class(name="arduinoDSL::RuleBody")
arduinoDSL_Assignment = Class(name="arduinoDSL::Assignment")
SimpleStatement = Class(name="SimpleStatement")
arduinoDSL_VariableDeclaration = Class(name="arduinoDSL::VariableDeclaration")
arduinoDSL_Cast = Class(name="arduinoDSL::Cast")
arduinoDSL_NumberExpression = Class(name="arduinoDSL::NumberExpression")
arduinoDSL_BooleanExpressionBlock = Class(name="arduinoDSL::BooleanExpressionBlock")
BooleanExpression = Class(name="BooleanExpression")
arduinoDSL_BooleanOperator = Class(name="arduinoDSL::BooleanOperator")
arduinoDSL_CompareOperator = Class(name="arduinoDSL::CompareOperator")
arduinoDSL_NumberExpressionBlock = Class(name="arduinoDSL::NumberExpressionBlock")
NumberExpression = Class(name="NumberExpression")
arduinoDSL_Value = Class(name="arduinoDSL::Value")
arduinoDSL_Attribute = Class(name="arduinoDSL::Attribute")
Value = Class(name="Value")
arduinoDSL_Node = Class(name="arduinoDSL::Node")
arduinoDSL_Component = Class(name="arduinoDSL::Component")
arduinoDSL_Delta = Class(name="arduinoDSL::Delta")
arduinoDSL_BooleanLiteral = Class(name="arduinoDSL::BooleanLiteral")
arduinoDSL_NumberLiteral = Class(name="arduinoDSL::NumberLiteral")
arduinoDSL_State = Class(name="arduinoDSL::State")
arduinoDSL_SimpleStatement = Class(name="arduinoDSL::SimpleStatement")
arduinoDSL_AndOr = Class(name="arduinoDSL::AndOr")
arduinoDSL_VariableReference = Class(name="arduinoDSL::VariableReference")
arduinoDSL_NodeDefinition = Class(name="arduinoDSL::NodeDefinition")
arduinoDSL_Board = Class(name="arduinoDSL::Board")
arduinoDSL_ComponentBody = Class(name="arduinoDSL::ComponentBody")
arduinoDSL_Rate = Class(name="arduinoDSL::Rate")
arduinoDSL_Map = Class(name="arduinoDSL::Map")
arduinoDSL_Smoothing = Class(name="arduinoDSL::Smoothing")
arduinoDSL_Range = Class(name="arduinoDSL::Range")
arduinoDSL_Mult = Class(name="arduinoDSL::Mult")
arduinoDSL_Div = Class(name="arduinoDSL::Div")
arduinoDSL_Comparison = Class(name="arduinoDSL::Comparison")
arduinoDSL_And = Class(name="arduinoDSL::And")
BooleanOperator = Class(name="BooleanOperator")
arduinoDSL_Or = Class(name="arduinoDSL::Or")
arduinoDSL_Equals = Class(name="arduinoDSL::Equals")
CompareOperator = Class(name="CompareOperator")
arduinoDSL_NotEquals = Class(name="arduinoDSL::NotEquals")
arduinoDSL_GreaterThanEquals = Class(name="arduinoDSL::GreaterThanEquals")
arduinoDSL_Greater = Class(name="arduinoDSL::Greater")
arduinoDSL_SmallerThanEquals = Class(name="arduinoDSL::SmallerThanEquals")
arduinoDSL_Smaller = Class(name="arduinoDSL::Smaller")
arduinoDSL_Plus = Class(name="arduinoDSL::Plus")
arduinoDSL_Minus = Class(name="arduinoDSL::Minus")
arduinoDSL_Mod = Class(name="arduinoDSL::Mod")
arduinoDSL_IfStatement = Class(name="arduinoDSL::IfStatement")
arduinoDSL_ElseIfStatement = Class(name="arduinoDSL::ElseIfStatement")
arduinoDSL_ElseStatement = Class(name="arduinoDSL::ElseStatement")
arduinoDSL_VarRef = Class(name="arduinoDSL::VarRef")
VariableReference = Class(name="VariableReference")

# arduinoDSL_Program class attributes and methods

# arduinoDSL_EObject class attributes and methods

# arduinoDSL_Rule class attributes and methods
arduinoDSL_Rule_type: Property = Property(name="type", type=StringType)
arduinoDSL_Rule.attributes={arduinoDSL_Rule_type}

# arduinoDSL_BooleanExpression class attributes and methods

# arduinoDSL_RuleBody class attributes and methods

# arduinoDSL_Assignment class attributes and methods

# SimpleStatement class attributes and methods

# arduinoDSL_VariableDeclaration class attributes and methods
arduinoDSL_VariableDeclaration_type: Property = Property(name="type", type=StringType)
arduinoDSL_VariableDeclaration_name: Property = Property(name="name", type=StringType)
arduinoDSL_VariableDeclaration.attributes={arduinoDSL_VariableDeclaration_name, arduinoDSL_VariableDeclaration_type}

# arduinoDSL_Cast class attributes and methods
arduinoDSL_Cast_castType: Property = Property(name="castType", type=StringType)
arduinoDSL_Cast.attributes={arduinoDSL_Cast_castType}

# arduinoDSL_NumberExpression class attributes and methods

# arduinoDSL_BooleanExpressionBlock class attributes and methods

# BooleanExpression class attributes and methods

# arduinoDSL_BooleanOperator class attributes and methods

# arduinoDSL_CompareOperator class attributes and methods

# arduinoDSL_NumberExpressionBlock class attributes and methods

# NumberExpression class attributes and methods

# arduinoDSL_Value class attributes and methods

# arduinoDSL_Attribute class attributes and methods

# Value class attributes and methods

# arduinoDSL_Node class attributes and methods
arduinoDSL_Node_name: Property = Property(name="name", type=StringType)
arduinoDSL_Node.attributes={arduinoDSL_Node_name}

# arduinoDSL_Component class attributes and methods
arduinoDSL_Component_name: Property = Property(name="name", type=StringType)
arduinoDSL_Component.attributes={arduinoDSL_Component_name}

# arduinoDSL_Delta class attributes and methods

# arduinoDSL_BooleanLiteral class attributes and methods
arduinoDSL_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
arduinoDSL_BooleanLiteral.attributes={arduinoDSL_BooleanLiteral_value}

# arduinoDSL_NumberLiteral class attributes and methods
arduinoDSL_NumberLiteral_floatVal: Property = Property(name="floatVal", type=StringType)
arduinoDSL_NumberLiteral_intVal: Property = Property(name="intVal", type=IntegerType)
arduinoDSL_NumberLiteral.attributes={arduinoDSL_NumberLiteral_floatVal, arduinoDSL_NumberLiteral_intVal}

# arduinoDSL_State class attributes and methods
arduinoDSL_State_value: Property = Property(name="value", type=StringType)
arduinoDSL_State.attributes={arduinoDSL_State_value}

# arduinoDSL_SimpleStatement class attributes and methods

# arduinoDSL_AndOr class attributes and methods

# arduinoDSL_VariableReference class attributes and methods

# arduinoDSL_NodeDefinition class attributes and methods

# arduinoDSL_Board class attributes and methods
arduinoDSL_Board_b: Property = Property(name="b", type=StringType)
arduinoDSL_Board.attributes={arduinoDSL_Board_b}

# arduinoDSL_ComponentBody class attributes and methods
arduinoDSL_ComponentBody_io: Property = Property(name="io", type=StringType)
arduinoDSL_ComponentBody_type: Property = Property(name="type", type=StringType)
arduinoDSL_ComponentBody_pin: Property = Property(name="pin", type=IntegerType)
arduinoDSL_ComponentBody.attributes={arduinoDSL_ComponentBody_pin, arduinoDSL_ComponentBody_type, arduinoDSL_ComponentBody_io}

# arduinoDSL_Rate class attributes and methods
arduinoDSL_Rate_value: Property = Property(name="value", type=IntegerType)
arduinoDSL_Rate.attributes={arduinoDSL_Rate_value}

# arduinoDSL_Map class attributes and methods

# arduinoDSL_Smoothing class attributes and methods
arduinoDSL_Smoothing_value: Property = Property(name="value", type=FloatType)
arduinoDSL_Smoothing.attributes={arduinoDSL_Smoothing_value}

# arduinoDSL_Range class attributes and methods
arduinoDSL_Range_low: Property = Property(name="low", type=FloatType)
arduinoDSL_Range_high: Property = Property(name="high", type=FloatType)
arduinoDSL_Range.attributes={arduinoDSL_Range_high, arduinoDSL_Range_low}

# arduinoDSL_Mult class attributes and methods

# arduinoDSL_Div class attributes and methods

# arduinoDSL_Comparison class attributes and methods

# arduinoDSL_And class attributes and methods

# BooleanOperator class attributes and methods

# arduinoDSL_Or class attributes and methods

# arduinoDSL_Equals class attributes and methods

# CompareOperator class attributes and methods

# arduinoDSL_NotEquals class attributes and methods

# arduinoDSL_GreaterThanEquals class attributes and methods

# arduinoDSL_Greater class attributes and methods

# arduinoDSL_SmallerThanEquals class attributes and methods

# arduinoDSL_Smaller class attributes and methods

# arduinoDSL_Plus class attributes and methods

# arduinoDSL_Minus class attributes and methods

# arduinoDSL_Mod class attributes and methods

# arduinoDSL_IfStatement class attributes and methods

# arduinoDSL_ElseIfStatement class attributes and methods

# arduinoDSL_ElseStatement class attributes and methods

# arduinoDSL_VarRef class attributes and methods

# VariableReference class attributes and methods

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="arduinoDSL_EObject", type=arduinoDSL_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Program", type=arduinoDSL_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition1: BinaryAssociation = BinaryAssociation(
    name="condition1",
    ends={
        Property(name="arduinoDSL_BooleanExpression", type=arduinoDSL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Rule", type=arduinoDSL_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements12: BinaryAssociation = BinaryAssociation(
    name="statements12",
    ends={
        Property(name="arduinoDSL_SimpleStatement", type=arduinoDSL_RuleBody, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_RuleBody13", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute14: BinaryAssociation = BinaryAssociation(
    name="attribute14",
    ends={
        Property(name="arduinoDSL_Attribute15", type=arduinoDSL_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Assignment", type=arduinoDSL_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="arduinoDSL_EObject18", type=arduinoDSL_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Assignment17", type=arduinoDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cast19: BinaryAssociation = BinaryAssociation(
    name="cast19",
    ends={
        Property(name="arduinoDSL_Cast", type=arduinoDSL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_VariableDeclaration", type=arduinoDSL_Cast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="arduinoDSL_RuleBody", type=arduinoDSL_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Rule3", type=arduinoDSL_RuleBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block4: BinaryAssociation = BinaryAssociation(
    name="block4",
    ends={
        Property(name="arduinoDSL_BooleanExpression5", type=arduinoDSL_BooleanExpressionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_BooleanExpressionBlock", type=arduinoDSL_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block6: BinaryAssociation = BinaryAssociation(
    name="block6",
    ends={
        Property(name="arduinoDSL_NumberExpression", type=arduinoDSL_NumberExpressionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_NumberExpressionBlock", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name7: BinaryAssociation = BinaryAssociation(
    name="name7",
    ends={
        Property(name="arduinoDSL_Node", type=arduinoDSL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Attribute", type=arduinoDSL_Node, multiplicity=Multiplicity(0, 1))
    }
)
component8: BinaryAssociation = BinaryAssociation(
    name="component8",
    ends={
        Property(name="arduinoDSL_Component", type=arduinoDSL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Attribute9", type=arduinoDSL_Component, multiplicity=Multiplicity(0, 1))
    }
)
attr10: BinaryAssociation = BinaryAssociation(
    name="attr10",
    ends={
        Property(name="arduinoDSL_Attribute11", type=arduinoDSL_Delta, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Delta", type=arduinoDSL_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left43: BinaryAssociation = BinaryAssociation(
    name="left43",
    ends={
        Property(name="arduinoDSL_BooleanExpression44", type=arduinoDSL_AndOr, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_AndOr", type=arduinoDSL_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator45: BinaryAssociation = BinaryAssociation(
    name="operator45",
    ends={
        Property(name="arduinoDSL_BooleanOperator", type=arduinoDSL_AndOr, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_AndOr46", type=arduinoDSL_BooleanOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="arduinoDSL_EObject22", type=arduinoDSL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_VariableDeclaration21", type=arduinoDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
board23: BinaryAssociation = BinaryAssociation(
    name="board23",
    ends={
        Property(name="arduinoDSL_Board", type=arduinoDSL_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_NodeDefinition", type=arduinoDSL_Board, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
node24: BinaryAssociation = BinaryAssociation(
    name="node24",
    ends={
        Property(name="arduinoDSL_Node26", type=arduinoDSL_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_NodeDefinition25", type=arduinoDSL_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components27: BinaryAssociation = BinaryAssociation(
    name="components27",
    ends={
        Property(name="arduinoDSL_Component29", type=arduinoDSL_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Node28", type=arduinoDSL_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties30: BinaryAssociation = BinaryAssociation(
    name="properties30",
    ends={
        Property(name="arduinoDSL_ComponentBody", type=arduinoDSL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Component31", type=arduinoDSL_ComponentBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rate32: BinaryAssociation = BinaryAssociation(
    name="rate32",
    ends={
        Property(name="arduinoDSL_Rate", type=arduinoDSL_ComponentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ComponentBody33", type=arduinoDSL_Rate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
map34: BinaryAssociation = BinaryAssociation(
    name="map34",
    ends={
        Property(name="arduinoDSL_Map", type=arduinoDSL_ComponentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ComponentBody35", type=arduinoDSL_Map, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
smoothing36: BinaryAssociation = BinaryAssociation(
    name="smoothing36",
    ends={
        Property(name="arduinoDSL_Smoothing", type=arduinoDSL_ComponentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ComponentBody37", type=arduinoDSL_Smoothing, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in38: BinaryAssociation = BinaryAssociation(
    name="in38",
    ends={
        Property(name="arduinoDSL_Range", type=arduinoDSL_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Map39", type=arduinoDSL_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out40: BinaryAssociation = BinaryAssociation(
    name="out40",
    ends={
        Property(name="arduinoDSL_Range42", type=arduinoDSL_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Map41", type=arduinoDSL_Range, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left67: BinaryAssociation = BinaryAssociation(
    name="left67",
    ends={
        Property(name="arduinoDSL_NumberExpression68", type=arduinoDSL_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Mult", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right69: BinaryAssociation = BinaryAssociation(
    name="right69",
    ends={
        Property(name="arduinoDSL_NumberExpression71", type=arduinoDSL_Mult, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Mult70", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left72: BinaryAssociation = BinaryAssociation(
    name="left72",
    ends={
        Property(name="arduinoDSL_NumberExpression73", type=arduinoDSL_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Div", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="arduinoDSL_BooleanExpression49", type=arduinoDSL_AndOr, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_AndOr48", type=arduinoDSL_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left50: BinaryAssociation = BinaryAssociation(
    name="left50",
    ends={
        Property(name="arduinoDSL_NumberExpression51", type=arduinoDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Comparison", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operator52: BinaryAssociation = BinaryAssociation(
    name="operator52",
    ends={
        Property(name="arduinoDSL_CompareOperator", type=arduinoDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Comparison53", type=arduinoDSL_CompareOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right54: BinaryAssociation = BinaryAssociation(
    name="right54",
    ends={
        Property(name="arduinoDSL_NumberExpression56", type=arduinoDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Comparison55", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left57: BinaryAssociation = BinaryAssociation(
    name="left57",
    ends={
        Property(name="arduinoDSL_NumberExpression58", type=arduinoDSL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Plus", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right59: BinaryAssociation = BinaryAssociation(
    name="right59",
    ends={
        Property(name="arduinoDSL_NumberExpression61", type=arduinoDSL_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Plus60", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left62: BinaryAssociation = BinaryAssociation(
    name="left62",
    ends={
        Property(name="arduinoDSL_NumberExpression63", type=arduinoDSL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Minus", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right64: BinaryAssociation = BinaryAssociation(
    name="right64",
    ends={
        Property(name="arduinoDSL_NumberExpression66", type=arduinoDSL_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Minus65", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref106: BinaryAssociation = BinaryAssociation(
    name="ref106",
    ends={
        Property(name="arduinoDSL_VariableDeclaration107", type=arduinoDSL_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_VarRef", type=arduinoDSL_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
cast108: BinaryAssociation = BinaryAssociation(
    name="cast108",
    ends={
        Property(name="arduinoDSL_Cast110", type=arduinoDSL_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_VarRef109", type=arduinoDSL_Cast, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value111: BinaryAssociation = BinaryAssociation(
    name="value111",
    ends={
        Property(name="arduinoDSL_EObject113", type=arduinoDSL_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_VarRef112", type=arduinoDSL_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right74: BinaryAssociation = BinaryAssociation(
    name="right74",
    ends={
        Property(name="arduinoDSL_NumberExpression76", type=arduinoDSL_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Div75", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left77: BinaryAssociation = BinaryAssociation(
    name="left77",
    ends={
        Property(name="arduinoDSL_NumberExpression78", type=arduinoDSL_Mod, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Mod", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right79: BinaryAssociation = BinaryAssociation(
    name="right79",
    ends={
        Property(name="arduinoDSL_NumberExpression81", type=arduinoDSL_Mod, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_Mod80", type=arduinoDSL_NumberExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition82: BinaryAssociation = BinaryAssociation(
    name="condition82",
    ends={
        Property(name="arduinoDSL_BooleanExpression83", type=arduinoDSL_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_IfStatement", type=arduinoDSL_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements84: BinaryAssociation = BinaryAssociation(
    name="statements84",
    ends={
        Property(name="arduinoDSL_SimpleStatement86", type=arduinoDSL_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_IfStatement85", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseif87: BinaryAssociation = BinaryAssociation(
    name="elseif87",
    ends={
        Property(name="arduinoDSL_SimpleStatement89", type=arduinoDSL_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_IfStatement88", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else90: BinaryAssociation = BinaryAssociation(
    name="else90",
    ends={
        Property(name="arduinoDSL_SimpleStatement92", type=arduinoDSL_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_IfStatement91", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition93: BinaryAssociation = BinaryAssociation(
    name="condition93",
    ends={
        Property(name="arduinoDSL_BooleanExpression94", type=arduinoDSL_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ElseIfStatement", type=arduinoDSL_BooleanExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements95: BinaryAssociation = BinaryAssociation(
    name="statements95",
    ends={
        Property(name="arduinoDSL_SimpleStatement97", type=arduinoDSL_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ElseIfStatement96", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseif98: BinaryAssociation = BinaryAssociation(
    name="elseif98",
    ends={
        Property(name="arduinoDSL_SimpleStatement100", type=arduinoDSL_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ElseIfStatement99", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else101: BinaryAssociation = BinaryAssociation(
    name="else101",
    ends={
        Property(name="arduinoDSL_SimpleStatement103", type=arduinoDSL_ElseIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ElseIfStatement102", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements104: BinaryAssociation = BinaryAssociation(
    name="statements104",
    ends={
        Property(name="arduinoDSL_SimpleStatement105", type=arduinoDSL_ElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="arduinoDSL_ElseStatement", type=arduinoDSL_SimpleStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_arduinoDSL_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=arduinoDSL_Assignment)
gen_arduinoDSL_VariableDeclaration_SimpleStatement = Generalization(general=SimpleStatement, specific=arduinoDSL_VariableDeclaration)
gen_arduinoDSL_BooleanExpressionBlock_BooleanExpression = Generalization(general=BooleanExpression, specific=arduinoDSL_BooleanExpressionBlock)
gen_arduinoDSL_NumberExpressionBlock_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_NumberExpressionBlock)
gen_arduinoDSL_Value_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_Value)
gen_arduinoDSL_Attribute_Value = Generalization(general=Value, specific=arduinoDSL_Attribute)
gen_arduinoDSL_Delta_Value = Generalization(general=Value, specific=arduinoDSL_Delta)
gen_arduinoDSL_NumberLiteral_Value = Generalization(general=Value, specific=arduinoDSL_NumberLiteral)
gen_arduinoDSL_AndOr_BooleanExpression = Generalization(general=BooleanExpression, specific=arduinoDSL_AndOr)
gen_arduinoDSL_VariableReference_Value = Generalization(general=Value, specific=arduinoDSL_VariableReference)
gen_arduinoDSL_VariableReference_SimpleStatement = Generalization(general=SimpleStatement, specific=arduinoDSL_VariableReference)
gen_arduinoDSL_Mult_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_Mult)
gen_arduinoDSL_Div_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_Div)
gen_arduinoDSL_Comparison_BooleanExpression = Generalization(general=BooleanExpression, specific=arduinoDSL_Comparison)
gen_arduinoDSL_And_BooleanOperator = Generalization(general=BooleanOperator, specific=arduinoDSL_And)
gen_arduinoDSL_Or_BooleanOperator = Generalization(general=BooleanOperator, specific=arduinoDSL_Or)
gen_arduinoDSL_Equals_CompareOperator = Generalization(general=CompareOperator, specific=arduinoDSL_Equals)
gen_arduinoDSL_NotEquals_CompareOperator = Generalization(general=CompareOperator, specific=arduinoDSL_NotEquals)
gen_arduinoDSL_GreaterThanEquals_CompareOperator = Generalization(general=CompareOperator, specific=arduinoDSL_GreaterThanEquals)
gen_arduinoDSL_Greater_CompareOperator = Generalization(general=CompareOperator, specific=arduinoDSL_Greater)
gen_arduinoDSL_SmallerThanEquals_CompareOperator = Generalization(general=CompareOperator, specific=arduinoDSL_SmallerThanEquals)
gen_arduinoDSL_Smaller_CompareOperator = Generalization(general=CompareOperator, specific=arduinoDSL_Smaller)
gen_arduinoDSL_Plus_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_Plus)
gen_arduinoDSL_Minus_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_Minus)
gen_arduinoDSL_Mod_NumberExpression = Generalization(general=NumberExpression, specific=arduinoDSL_Mod)
gen_arduinoDSL_IfStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=arduinoDSL_IfStatement)
gen_arduinoDSL_ElseIfStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=arduinoDSL_ElseIfStatement)
gen_arduinoDSL_ElseStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=arduinoDSL_ElseStatement)
gen_arduinoDSL_VarRef_VariableReference = Generalization(general=VariableReference, specific=arduinoDSL_VarRef)

# Domain Model
domain_model = DomainModel(
    name="arduinoDSL",
    types={arduinoDSL_Program, arduinoDSL_EObject, arduinoDSL_Rule, arduinoDSL_BooleanExpression, arduinoDSL_RuleBody, arduinoDSL_Assignment, SimpleStatement, arduinoDSL_VariableDeclaration, arduinoDSL_Cast, arduinoDSL_NumberExpression, arduinoDSL_BooleanExpressionBlock, BooleanExpression, arduinoDSL_BooleanOperator, arduinoDSL_CompareOperator, arduinoDSL_NumberExpressionBlock, NumberExpression, arduinoDSL_Value, arduinoDSL_Attribute, Value, arduinoDSL_Node, arduinoDSL_Component, arduinoDSL_Delta, arduinoDSL_BooleanLiteral, arduinoDSL_NumberLiteral, arduinoDSL_State, arduinoDSL_SimpleStatement, arduinoDSL_AndOr, arduinoDSL_VariableReference, arduinoDSL_NodeDefinition, arduinoDSL_Board, arduinoDSL_ComponentBody, arduinoDSL_Rate, arduinoDSL_Map, arduinoDSL_Smoothing, arduinoDSL_Range, arduinoDSL_Mult, arduinoDSL_Div, arduinoDSL_Comparison, arduinoDSL_And, BooleanOperator, arduinoDSL_Or, arduinoDSL_Equals, CompareOperator, arduinoDSL_NotEquals, arduinoDSL_GreaterThanEquals, arduinoDSL_Greater, arduinoDSL_SmallerThanEquals, arduinoDSL_Smaller, arduinoDSL_Plus, arduinoDSL_Minus, arduinoDSL_Mod, arduinoDSL_IfStatement, arduinoDSL_ElseIfStatement, arduinoDSL_ElseStatement, arduinoDSL_VarRef, VariableReference},
    associations={program0, condition1, statements12, attribute14, value16, cast19, body2, block4, block6, name7, component8, attr10, left43, operator45, value20, board23, node24, components27, properties30, rate32, map34, smoothing36, in38, out40, left67, right69, left72, right47, left50, operator52, right54, left57, right59, left62, right64, ref106, cast108, value111, right74, left77, right79, condition82, statements84, elseif87, else90, condition93, statements95, elseif98, else101, statements104},
    generalizations={gen_arduinoDSL_Assignment_SimpleStatement, gen_arduinoDSL_VariableDeclaration_SimpleStatement, gen_arduinoDSL_BooleanExpressionBlock_BooleanExpression, gen_arduinoDSL_NumberExpressionBlock_NumberExpression, gen_arduinoDSL_Value_NumberExpression, gen_arduinoDSL_Attribute_Value, gen_arduinoDSL_Delta_Value, gen_arduinoDSL_NumberLiteral_Value, gen_arduinoDSL_AndOr_BooleanExpression, gen_arduinoDSL_VariableReference_Value, gen_arduinoDSL_VariableReference_SimpleStatement, gen_arduinoDSL_Mult_NumberExpression, gen_arduinoDSL_Div_NumberExpression, gen_arduinoDSL_Comparison_BooleanExpression, gen_arduinoDSL_And_BooleanOperator, gen_arduinoDSL_Or_BooleanOperator, gen_arduinoDSL_Equals_CompareOperator, gen_arduinoDSL_NotEquals_CompareOperator, gen_arduinoDSL_GreaterThanEquals_CompareOperator, gen_arduinoDSL_Greater_CompareOperator, gen_arduinoDSL_SmallerThanEquals_CompareOperator, gen_arduinoDSL_Smaller_CompareOperator, gen_arduinoDSL_Plus_NumberExpression, gen_arduinoDSL_Minus_NumberExpression, gen_arduinoDSL_Mod_NumberExpression, gen_arduinoDSL_IfStatement_SimpleStatement, gen_arduinoDSL_ElseIfStatement_SimpleStatement, gen_arduinoDSL_ElseStatement_SimpleStatement, gen_arduinoDSL_VarRef_VariableReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)