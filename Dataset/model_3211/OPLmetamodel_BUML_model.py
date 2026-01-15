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
BinaryOp: Enumeration = Enumeration(
    name="BinaryOp",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="subtract"),
			EnumerationLiteral(name="multiply"),
			EnumerationLiteral(name="divide"),
			EnumerationLiteral(name="percent"),
			EnumerationLiteral(name="mod"),
			EnumerationLiteral(name="inter"),
			EnumerationLiteral(name="union"),
			EnumerationLiteral(name="diff"),
			EnumerationLiteral(name="symdiff"),
			EnumerationLiteral(name="power")
    }
)

AggOp: Enumeration = Enumeration(
    name="AggOp",
    literals={
            EnumerationLiteral(name="sum"),
			EnumerationLiteral(name="min"),
			EnumerationLiteral(name="max"),
			EnumerationLiteral(name="prod"),
			EnumerationLiteral(name="inter"),
			EnumerationLiteral(name="union"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="and")
    }
)

SetOp: Enumeration = Enumeration(
    name="SetOp",
    literals={
            EnumerationLiteral(name="symdiff"),
			EnumerationLiteral(name="diff"),
			EnumerationLiteral(name="union"),
			EnumerationLiteral(name="inter")
    }
)

UnaryOp: Enumeration = Enumeration(
    name="UnaryOp",
    literals={
            EnumerationLiteral(name="unaryMinus"),
			EnumerationLiteral(name="negate")
    }
)

LogicalOp: Enumeration = Enumeration(
    name="LogicalOp",
    literals={
            EnumerationLiteral(name="negation"),
			EnumerationLiteral(name="disjunction"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="conjunction")
    }
)

MembershipOp: Enumeration = Enumeration(
    name="MembershipOp",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="not_in"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="conjunction")
    }
)

OptimizationMode: Enumeration = Enumeration(
    name="OptimizationMode",
    literals={
            EnumerationLiteral(name="minimize"),
			EnumerationLiteral(name="maximize"),
			EnumerationLiteral(name="solve")
    }
)

Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="forAll")
    }
)

RelationalOp: Enumeration = Enumeration(
    name="RelationalOp",
    literals={
            EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="greaterThanOrEqualTo"),
			EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="lessThanOrEqualTo"),
			EnumerationLiteral(name="equalTo"),
			EnumerationLiteral(name="notEqualTo")
    }
)

# Classes
OPLmetamodel_Expression = Class(name="OPLmetamodel::Expression", is_abstract=True)
OPLmetamodel_AllExpression = Class(name="OPLmetamodel::AllExpression")
OPLmetamodel_AbstractBinaryOperator = Class(name="OPLmetamodel::AbstractBinaryOperator", is_abstract=True)
OPLmetamodel_AbstractType = Class(name="OPLmetamodel::AbstractType", is_abstract=True)
OPLmetamodel_ActivityDeclaration = Class(name="OPLmetamodel::ActivityDeclaration")
Declaration = Class(name="Declaration")
OPLmetamodel_Number = Class(name="OPLmetamodel::Number")
OPLmetamodel_AggregateExp = Class(name="OPLmetamodel::AggregateExp")
Expression = Class(name="Expression")
OPLmetamodel_FormalParameter = Class(name="OPLmetamodel::FormalParameter")
OPLmetamodel_ArrayValue = Class(name="OPLmetamodel::ArrayValue")
OPLmetamodel_ArrayDereference = Class(name="OPLmetamodel::ArrayDereference")
PathExpression = Class(name="PathExpression")
OPLmetamodel_PathExpression = Class(name="OPLmetamodel::PathExpression", is_abstract=True)
OPLmetamodel_ArraySlotConstraint = Class(name="OPLmetamodel::ArraySlotConstraint")
OPLmetamodel_ArrayType = Class(name="OPLmetamodel::ArrayType")
DefinedType = Class(name="DefinedType")
OPLmetamodel_DataRef = Class(name="OPLmetamodel::DataRef")
OPLmetamodel_BooleanExpression = Class(name="OPLmetamodel::BooleanExpression")
PrimitiveExpression = Class(name="PrimitiveExpression")
OPLmetamodel_Assertion = Class(name="OPLmetamodel::Assertion")
OPLmetamodel_Constraint = Class(name="OPLmetamodel::Constraint")
OPLmetamodel_BinaryExpression = Class(name="OPLmetamodel::BinaryExpression")
OPLmetamodel_BinaryOperator = Class(name="OPLmetamodel::BinaryOperator")
AbstractBinaryOperator = Class(name="AbstractBinaryOperator")
OPLmetamodel_BindingRef = Class(name="OPLmetamodel::BindingRef")
Reference = Class(name="Reference")
OPLmetamodel_BlockExpression = Class(name="OPLmetamodel::BlockExpression")
OPLmetamodel_BooleanBlock = Class(name="OPLmetamodel::BooleanBlock")
OPLmetamodel_Initialization = Class(name="OPLmetamodel::Initialization", is_abstract=True)
OPLmetamodel_BooleanType = Class(name="OPLmetamodel::BooleanType")
PrimitiveType = Class(name="PrimitiveType")
OPLmetamodel_BuiltInFunction = Class(name="OPLmetamodel::BuiltInFunction")
Function = Class(name="Function")
OPLmetamodel_CollectionExpression = Class(name="OPLmetamodel::CollectionExpression")
OPLmetamodel_Comprehension = Class(name="OPLmetamodel::Comprehension")
CollectionExpression = Class(name="CollectionExpression")
OPLmetamodel_CumulativeFunction = Class(name="OPLmetamodel::CumulativeFunction")
OPLmetamodel_DataDeclaration = Class(name="OPLmetamodel::DataDeclaration")
OPLmetamodel_ParameterDeclaration = Class(name="OPLmetamodel::ParameterDeclaration")
OPLmetamodel_DataInitMethods = Class(name="OPLmetamodel::DataInitMethods", is_abstract=True)
OPLmetamodel_DataObject = Class(name="OPLmetamodel::DataObject")
Initialization = Class(name="Initialization")
OPLmetamodel_Declaration = Class(name="OPLmetamodel::Declaration", is_abstract=True)
OPLmetamodel_DeferredInit = Class(name="OPLmetamodel::DeferredInit")
OPLmetamodel_DefinedType = Class(name="OPLmetamodel::DefinedType", is_abstract=True)
AbstractType = Class(name="AbstractType")
OPLmetamodel_Function = Class(name="OPLmetamodel::Function", is_abstract=True)
OPLmetamodel_DisplayInstruction = Class(name="OPLmetamodel::DisplayInstruction")
OPLmetamodel_EnumerationType = Class(name="OPLmetamodel::EnumerationType")
SetType = Class(name="SetType")
OPLmetamodel_EnumLiteral = Class(name="OPLmetamodel::EnumLiteral")
OPLmetamodel_Entity = Class(name="OPLmetamodel::Entity")
OPLmetamodel_Error = Class(name="OPLmetamodel::Error")
OPLmetamodel_FloatRangeType = Class(name="OPLmetamodel::FloatRangeType")
FloatType = Class(name="FloatType")
RangeType = Class(name="RangeType")
OPLmetamodel_FloatType = Class(name="OPLmetamodel::FloatType")
NumericType = Class(name="NumericType")
OPLmetamodel_ParameterDomain = Class(name="OPLmetamodel::ParameterDomain", is_abstract=True)
OPLmetamodel_Extension = Class(name="OPLmetamodel::Extension")
OPLmetamodel_FloatExpression = Class(name="OPLmetamodel::FloatExpression")
NumericExpression = Class(name="NumericExpression")
OPLmetamodel_ForAllConstraint = Class(name="OPLmetamodel::ForAllConstraint")
Constraint = Class(name="Constraint")
OPLmetamodel_NumericType = Class(name="OPLmetamodel::NumericType")
OPLmetamodel_StepFunction = Class(name="OPLmetamodel::StepFunction")
OPLmetamodel_FunctionRef = Class(name="OPLmetamodel::FunctionRef")
OPLmetamodel_Reference = Class(name="OPLmetamodel::Reference", is_abstract=True)
OPLmetamodel_FunctionCall = Class(name="OPLmetamodel::FunctionCall")
OPLmetamodel_IfConstraint = Class(name="OPLmetamodel::IfConstraint")
OPLmetamodel_IfExpression = Class(name="OPLmetamodel::IfExpression")
OPLmetamodel_In = Class(name="OPLmetamodel::In")
OPLmetamodel_IntegerType = Class(name="OPLmetamodel::IntegerType")
OPLmetamodel_Interval = Class(name="OPLmetamodel::Interval")
OPLmetamodel_RangeType = Class(name="OPLmetamodel::RangeType", is_abstract=True)
OPLmetamodel_ResourceDeclaration = Class(name="OPLmetamodel::ResourceDeclaration")
OPLmetamodel_IntegerExpression = Class(name="OPLmetamodel::IntegerExpression")
OPLmetamodel_IntegerRangeType = Class(name="OPLmetamodel::IntegerRangeType")
IntegerType = Class(name="IntegerType")
OPLmetamodel_IndexValuePair = Class(name="OPLmetamodel::IndexValuePair")
OPLmetamodel_Model = Class(name="OPLmetamodel::Model")
OPLmetamodel_Objective = Class(name="OPLmetamodel::Objective")
OPLmetamodel_PiecewiseExpression = Class(name="OPLmetamodel::PiecewiseExpression")
OPLmetamodel_PiecewiseLinearFunction = Class(name="OPLmetamodel::PiecewiseLinearFunction")
OPLmetamodel_ScheduleInitialization = Class(name="OPLmetamodel::ScheduleInitialization")
OPLmetamodel_Script = Class(name="OPLmetamodel::Script")
OPLmetamodel_Setting = Class(name="OPLmetamodel::Setting")
OPLmetamodel_SearchProcedure = Class(name="OPLmetamodel::SearchProcedure")
OPLmetamodel_NumericExpression = Class(name="OPLmetamodel::NumericExpression", is_abstract=True)
OPLmetamodel_Operator = Class(name="OPLmetamodel::Operator")
OPLmetamodel_ParameterRef = Class(name="OPLmetamodel::ParameterRef")
OPLmetamodel_PathDereference = Class(name="OPLmetamodel::PathDereference", is_abstract=True)
OPLmetamodel_PositiveFloatType = Class(name="OPLmetamodel::PositiveFloatType")
OPLmetamodel_PrimitiveExpression = Class(name="OPLmetamodel::PrimitiveExpression", is_abstract=True)
OPLmetamodel_ReadFile = Class(name="OPLmetamodel::ReadFile")
OPLmetamodel_PrimitiveType = Class(name="OPLmetamodel::PrimitiveType", is_abstract=True)
OPLmetamodel_PositiveIntegerType = Class(name="OPLmetamodel::PositiveIntegerType")
OPLmetamodel_QueryUser = Class(name="OPLmetamodel::QueryUser")
DataInitMethods = Class(name="DataInitMethods")
OPLmetamodel_RangeExpression = Class(name="OPLmetamodel::RangeExpression")
OPLmetamodel_ReflectiveFunction = Class(name="OPLmetamodel::ReflectiveFunction")
BuiltInFunction = Class(name="BuiltInFunction")
OPLmetamodel_RelationalExpression = Class(name="OPLmetamodel::RelationalExpression")
BinaryExpression = Class(name="BinaryExpression")
BooleanExpression = Class(name="BooleanExpression")
OPLmetamodel_RelationalInit = Class(name="OPLmetamodel::RelationalInit")
OPLmetamodel_VariableBinding = Class(name="OPLmetamodel::VariableBinding")
OPLmetamodel_Record = Class(name="OPLmetamodel::Record")
ParameterDomain = Class(name="ParameterDomain")
OPLmetamodel_RecordField = Class(name="OPLmetamodel::RecordField")
OPLmetamodel_RecordValue = Class(name="OPLmetamodel::RecordValue")
OPLmetamodel_SetValue = Class(name="OPLmetamodel::SetValue")
OPLmetamodel_StateFunction = Class(name="OPLmetamodel::StateFunction")
PiecewiseLinearFunction = Class(name="PiecewiseLinearFunction")
OPLmetamodel_StringExpression = Class(name="OPLmetamodel::StringExpression")
OPLmetamodel_StringType = Class(name="OPLmetamodel::StringType")
OPLmetamodel_TupleBinding = Class(name="OPLmetamodel::TupleBinding")
OPLmetamodel_RelationalOperator = Class(name="OPLmetamodel::RelationalOperator")
OPLmetamodel_ScriptStatement = Class(name="OPLmetamodel::ScriptStatement", is_abstract=True)
OPLmetamodel_Sequence = Class(name="OPLmetamodel::Sequence")
OPLmetamodel_SetType = Class(name="OPLmetamodel::SetType")
OPLmetamodel_UnaryExpression = Class(name="OPLmetamodel::UnaryExpression")
OPLmetamodel_Writeln = Class(name="OPLmetamodel::Writeln")
ScriptStatement = Class(name="ScriptStatement")

# OPLmetamodel_Expression class attributes and methods

# OPLmetamodel_AllExpression class attributes and methods

# OPLmetamodel_AbstractBinaryOperator class attributes and methods

# OPLmetamodel_AbstractType class attributes and methods

# OPLmetamodel_ActivityDeclaration class attributes and methods
OPLmetamodel_ActivityDeclaration_earliestStartTime: Property = Property(name="earliestStartTime", type=StringType)
OPLmetamodel_ActivityDeclaration_latestEndTime: Property = Property(name="latestEndTime", type=StringType)
OPLmetamodel_ActivityDeclaration.attributes={OPLmetamodel_ActivityDeclaration_latestEndTime, OPLmetamodel_ActivityDeclaration_earliestStartTime}

# Declaration class attributes and methods

# OPLmetamodel_Number class attributes and methods

# OPLmetamodel_AggregateExp class attributes and methods
OPLmetamodel_AggregateExp_op: Property = Property(name="op", type=StringType)
OPLmetamodel_AggregateExp.attributes={OPLmetamodel_AggregateExp_op}

# Expression class attributes and methods

# OPLmetamodel_FormalParameter class attributes and methods
OPLmetamodel_FormalParameter_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
OPLmetamodel_FormalParameter.attributes={OPLmetamodel_FormalParameter_isOrdered}

# OPLmetamodel_ArrayValue class attributes and methods

# OPLmetamodel_ArrayDereference class attributes and methods

# PathExpression class attributes and methods

# OPLmetamodel_PathExpression class attributes and methods

# OPLmetamodel_ArraySlotConstraint class attributes and methods

# OPLmetamodel_ArrayType class attributes and methods

# DefinedType class attributes and methods

# OPLmetamodel_DataRef class attributes and methods

# OPLmetamodel_BooleanExpression class attributes and methods
OPLmetamodel_BooleanExpression_body: Property = Property(name="body", type=StringType)
OPLmetamodel_BooleanExpression.attributes={OPLmetamodel_BooleanExpression_body}

# PrimitiveExpression class attributes and methods

# OPLmetamodel_Assertion class attributes and methods

# OPLmetamodel_Constraint class attributes and methods
OPLmetamodel_Constraint_name: Property = Property(name="name", type=StringType)
OPLmetamodel_Constraint.attributes={OPLmetamodel_Constraint_name}

# OPLmetamodel_BinaryExpression class attributes and methods

# OPLmetamodel_BinaryOperator class attributes and methods
OPLmetamodel_BinaryOperator_op: Property = Property(name="op", type=StringType)
OPLmetamodel_BinaryOperator.attributes={OPLmetamodel_BinaryOperator_op}

# AbstractBinaryOperator class attributes and methods

# OPLmetamodel_BindingRef class attributes and methods

# Reference class attributes and methods

# OPLmetamodel_BlockExpression class attributes and methods

# OPLmetamodel_BooleanBlock class attributes and methods

# OPLmetamodel_Initialization class attributes and methods

# OPLmetamodel_BooleanType class attributes and methods

# PrimitiveType class attributes and methods

# OPLmetamodel_BuiltInFunction class attributes and methods

# Function class attributes and methods

# OPLmetamodel_CollectionExpression class attributes and methods
OPLmetamodel_CollectionExpression_isUnique: Property = Property(name="isUnique", type=BooleanType)
OPLmetamodel_CollectionExpression.attributes={OPLmetamodel_CollectionExpression_isUnique}

# OPLmetamodel_Comprehension class attributes and methods

# CollectionExpression class attributes and methods

# OPLmetamodel_CumulativeFunction class attributes and methods

# OPLmetamodel_DataDeclaration class attributes and methods
OPLmetamodel_DataDeclaration_isDecisionVar: Property = Property(name="isDecisionVar", type=BooleanType)
OPLmetamodel_DataDeclaration_isDecisionExpr: Property = Property(name="isDecisionExpr", type=BooleanType)
OPLmetamodel_DataDeclaration.attributes={OPLmetamodel_DataDeclaration_isDecisionExpr, OPLmetamodel_DataDeclaration_isDecisionVar}

# OPLmetamodel_ParameterDeclaration class attributes and methods

# OPLmetamodel_DataInitMethods class attributes and methods

# OPLmetamodel_DataObject class attributes and methods
OPLmetamodel_DataObject_body: Property = Property(name="body", type=StringType)
OPLmetamodel_DataObject.attributes={OPLmetamodel_DataObject_body}

# Initialization class attributes and methods

# OPLmetamodel_Declaration class attributes and methods
OPLmetamodel_Declaration_order: Property = Property(name="order", type=IntegerType)
OPLmetamodel_Declaration.attributes={OPLmetamodel_Declaration_order}

# OPLmetamodel_DeferredInit class attributes and methods

# OPLmetamodel_DefinedType class attributes and methods

# AbstractType class attributes and methods

# OPLmetamodel_Function class attributes and methods

# OPLmetamodel_DisplayInstruction class attributes and methods

# OPLmetamodel_EnumerationType class attributes and methods

# SetType class attributes and methods

# OPLmetamodel_EnumLiteral class attributes and methods

# OPLmetamodel_Entity class attributes and methods

# OPLmetamodel_Error class attributes and methods

# OPLmetamodel_FloatRangeType class attributes and methods

# FloatType class attributes and methods

# RangeType class attributes and methods

# OPLmetamodel_FloatType class attributes and methods

# NumericType class attributes and methods

# OPLmetamodel_ParameterDomain class attributes and methods

# OPLmetamodel_Extension class attributes and methods

# OPLmetamodel_FloatExpression class attributes and methods
OPLmetamodel_FloatExpression_body: Property = Property(name="body", type=StringType)
OPLmetamodel_FloatExpression.attributes={OPLmetamodel_FloatExpression_body}

# NumericExpression class attributes and methods

# OPLmetamodel_ForAllConstraint class attributes and methods

# Constraint class attributes and methods

# OPLmetamodel_NumericType class attributes and methods

# OPLmetamodel_StepFunction class attributes and methods

# OPLmetamodel_FunctionRef class attributes and methods
OPLmetamodel_FunctionRef_name: Property = Property(name="name", type=StringType)
OPLmetamodel_FunctionRef.attributes={OPLmetamodel_FunctionRef_name}

# OPLmetamodel_Reference class attributes and methods
OPLmetamodel_Reference_name: Property = Property(name="name", type=StringType)
OPLmetamodel_Reference.attributes={OPLmetamodel_Reference_name}

# OPLmetamodel_FunctionCall class attributes and methods
OPLmetamodel_FunctionCall_functionName: Property = Property(name="functionName", type=StringType)
OPLmetamodel_FunctionCall.attributes={OPLmetamodel_FunctionCall_functionName}

# OPLmetamodel_IfConstraint class attributes and methods

# OPLmetamodel_IfExpression class attributes and methods

# OPLmetamodel_In class attributes and methods

# OPLmetamodel_IntegerType class attributes and methods

# OPLmetamodel_Interval class attributes and methods
OPLmetamodel_Interval_isOptional: Property = Property(name="isOptional", type=BooleanType)
OPLmetamodel_Interval.attributes={OPLmetamodel_Interval_isOptional}

# OPLmetamodel_RangeType class attributes and methods

# OPLmetamodel_ResourceDeclaration class attributes and methods

# OPLmetamodel_IntegerExpression class attributes and methods
OPLmetamodel_IntegerExpression_body: Property = Property(name="body", type=StringType)
OPLmetamodel_IntegerExpression.attributes={OPLmetamodel_IntegerExpression_body}

# OPLmetamodel_IntegerRangeType class attributes and methods

# IntegerType class attributes and methods

# OPLmetamodel_IndexValuePair class attributes and methods

# OPLmetamodel_Model class attributes and methods
OPLmetamodel_Model_id: Property = Property(name="id", type=StringType)
OPLmetamodel_Model_isConstraintProblem: Property = Property(name="isConstraintProblem", type=BooleanType)
OPLmetamodel_Model.attributes={OPLmetamodel_Model_id, OPLmetamodel_Model_isConstraintProblem}

# OPLmetamodel_Objective class attributes and methods
OPLmetamodel_Objective_action: Property = Property(name="action", type=StringType)
OPLmetamodel_Objective_isLinearRelaxation: Property = Property(name="isLinearRelaxation", type=BooleanType)
OPLmetamodel_Objective.attributes={OPLmetamodel_Objective_action, OPLmetamodel_Objective_isLinearRelaxation}

# OPLmetamodel_PiecewiseExpression class attributes and methods

# OPLmetamodel_PiecewiseLinearFunction class attributes and methods

# OPLmetamodel_ScheduleInitialization class attributes and methods

# OPLmetamodel_Script class attributes and methods
OPLmetamodel_Script_isMain: Property = Property(name="isMain", type=BooleanType)
OPLmetamodel_Script.attributes={OPLmetamodel_Script_isMain}

# OPLmetamodel_Setting class attributes and methods

# OPLmetamodel_SearchProcedure class attributes and methods

# OPLmetamodel_NumericExpression class attributes and methods

# OPLmetamodel_Operator class attributes and methods

# OPLmetamodel_ParameterRef class attributes and methods

# OPLmetamodel_PathDereference class attributes and methods

# OPLmetamodel_PositiveFloatType class attributes and methods

# OPLmetamodel_PrimitiveExpression class attributes and methods

# OPLmetamodel_ReadFile class attributes and methods
OPLmetamodel_ReadFile_path: Property = Property(name="path", type=StringType)
OPLmetamodel_ReadFile.attributes={OPLmetamodel_ReadFile_path}

# OPLmetamodel_PrimitiveType class attributes and methods

# OPLmetamodel_PositiveIntegerType class attributes and methods

# OPLmetamodel_QueryUser class attributes and methods
OPLmetamodel_QueryUser_ask: Property = Property(name="ask", type=StringType)
OPLmetamodel_QueryUser.attributes={OPLmetamodel_QueryUser_ask}

# DataInitMethods class attributes and methods

# OPLmetamodel_RangeExpression class attributes and methods

# OPLmetamodel_ReflectiveFunction class attributes and methods

# BuiltInFunction class attributes and methods

# OPLmetamodel_RelationalExpression class attributes and methods
OPLmetamodel_RelationalExpression_redefinedOp: Property = Property(name="redefinedOp", type=StringType)
OPLmetamodel_RelationalExpression.attributes={OPLmetamodel_RelationalExpression_redefinedOp}

# BinaryExpression class attributes and methods

# BooleanExpression class attributes and methods

# OPLmetamodel_RelationalInit class attributes and methods

# OPLmetamodel_VariableBinding class attributes and methods

# OPLmetamodel_Record class attributes and methods
OPLmetamodel_Record_name: Property = Property(name="name", type=StringType)
OPLmetamodel_Record_isTuple: Property = Property(name="isTuple", type=BooleanType)
OPLmetamodel_Record.attributes={OPLmetamodel_Record_isTuple, OPLmetamodel_Record_name}

# ParameterDomain class attributes and methods

# OPLmetamodel_RecordField class attributes and methods
OPLmetamodel_RecordField_name: Property = Property(name="name", type=StringType)
OPLmetamodel_RecordField.attributes={OPLmetamodel_RecordField_name}

# OPLmetamodel_RecordValue class attributes and methods

# OPLmetamodel_SetValue class attributes and methods

# OPLmetamodel_StateFunction class attributes and methods

# PiecewiseLinearFunction class attributes and methods

# OPLmetamodel_StringExpression class attributes and methods
OPLmetamodel_StringExpression_body: Property = Property(name="body", type=StringType)
OPLmetamodel_StringExpression.attributes={OPLmetamodel_StringExpression_body}

# OPLmetamodel_StringType class attributes and methods

# OPLmetamodel_TupleBinding class attributes and methods

# OPLmetamodel_RelationalOperator class attributes and methods
OPLmetamodel_RelationalOperator_op: Property = Property(name="op", type=StringType)
OPLmetamodel_RelationalOperator.attributes={OPLmetamodel_RelationalOperator_op}

# OPLmetamodel_ScriptStatement class attributes and methods

# OPLmetamodel_Sequence class attributes and methods

# OPLmetamodel_SetType class attributes and methods
OPLmetamodel_SetType_name: Property = Property(name="name", type=StringType)
OPLmetamodel_SetType.attributes={OPLmetamodel_SetType_name}

# OPLmetamodel_UnaryExpression class attributes and methods
OPLmetamodel_UnaryExpression_op: Property = Property(name="op", type=StringType)
OPLmetamodel_UnaryExpression.attributes={OPLmetamodel_UnaryExpression_op}

# OPLmetamodel_Writeln class attributes and methods
OPLmetamodel_Writeln_string: Property = Property(name="string", type=StringType)
OPLmetamodel_Writeln_arg: Property = Property(name="arg", type=StringType)
OPLmetamodel_Writeln.attributes={OPLmetamodel_Writeln_arg, OPLmetamodel_Writeln_string}

# ScriptStatement class attributes and methods

# Relationships
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="OPLmetamodel_Expression", type=OPLmetamodel_AggregateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_AggregateExp3", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifiers4: BinaryAssociation = BinaryAssociation(
    name="qualifiers4",
    ends={
        Property(name="OPLmetamodel_FormalParameter5", type=OPLmetamodel_AllExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_AllExpression", type=OPLmetamodel_FormalParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
duration0: BinaryAssociation = BinaryAssociation(
    name="duration0",
    ends={
        Property(name="OPLmetamodel_Number", type=OPLmetamodel_ActivityDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ActivityDeclaration", type=OPLmetamodel_Number, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="OPLmetamodel_FormalParameter", type=OPLmetamodel_AggregateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_AggregateExp", type=OPLmetamodel_FormalParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
items18: BinaryAssociation = BinaryAssociation(
    name="items18",
    ends={
        Property(name="OPLmetamodel_Expression19", type=OPLmetamodel_ArrayValue, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ArrayValue", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body6: BinaryAssociation = BinaryAssociation(
    name="body6",
    ends={
        Property(name="OPLmetamodel_Expression8", type=OPLmetamodel_AllExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_AllExpression7", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array9: BinaryAssociation = BinaryAssociation(
    name="array9",
    ends={
        Property(name="OPLmetamodel_PathExpression", type=OPLmetamodel_ArrayDereference, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ArrayDereference", type=OPLmetamodel_PathExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index10: BinaryAssociation = BinaryAssociation(
    name="index10",
    ends={
        Property(name="OPLmetamodel_Expression12", type=OPLmetamodel_ArrayDereference, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ArrayDereference11", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="OPLmetamodel_ArrayDereference14", type=OPLmetamodel_ArraySlotConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ArraySlotConstraint", type=OPLmetamodel_ArrayDereference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
baseType15: BinaryAssociation = BinaryAssociation(
    name="baseType15",
    ends={
        Property(name="OPLmetamodel_AbstractType", type=OPLmetamodel_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ArrayType", type=OPLmetamodel_AbstractType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subscripts16: BinaryAssociation = BinaryAssociation(
    name="subscripts16",
    ends={
        Property(name="OPLmetamodel_DataRef", type=OPLmetamodel_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ArrayType17", type=OPLmetamodel_DataRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exp20: BinaryAssociation = BinaryAssociation(
    name="exp20",
    ends={
        Property(name="OPLmetamodel_Constraint", type=OPLmetamodel_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Assertion", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs21: BinaryAssociation = BinaryAssociation(
    name="lhs21",
    ends={
        Property(name="OPLmetamodel_Expression22", type=OPLmetamodel_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_BinaryExpression", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs23: BinaryAssociation = BinaryAssociation(
    name="rhs23",
    ends={
        Property(name="OPLmetamodel_Expression25", type=OPLmetamodel_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_BinaryExpression24", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op26: BinaryAssociation = BinaryAssociation(
    name="op26",
    ends={
        Property(name="OPLmetamodel_AbstractBinaryOperator", type=OPLmetamodel_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_BinaryExpression27", type=OPLmetamodel_AbstractBinaryOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
blocks28: BinaryAssociation = BinaryAssociation(
    name="blocks28",
    ends={
        Property(name="OPLmetamodel_BooleanBlock", type=OPLmetamodel_BlockExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_BlockExpression", type=OPLmetamodel_BooleanBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="OPLmetamodel_AbstractType36", type=OPLmetamodel_DataDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_DataDeclaration35", type=OPLmetamodel_AbstractType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="OPLmetamodel_Initialization", type=OPLmetamodel_DataDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_DataDeclaration38", type=OPLmetamodel_Initialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp29: BinaryAssociation = BinaryAssociation(
    name="exp29",
    ends={
        Property(name="OPLmetamodel_Expression31", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Constraint30", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable32: BinaryAssociation = BinaryAssociation(
    name="variable32",
    ends={
        Property(name="OPLmetamodel_DataRef33", type=OPLmetamodel_DataDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_DataDeclaration", type=OPLmetamodel_DataRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exps42: BinaryAssociation = BinaryAssociation(
    name="exps42",
    ends={
        Property(name="OPLmetamodel_Expression43", type=OPLmetamodel_DisplayInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_DisplayInstruction", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters44: BinaryAssociation = BinaryAssociation(
    name="parameters44",
    ends={
        Property(name="OPLmetamodel_ParameterDeclaration", type=OPLmetamodel_DisplayInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_DisplayInstruction45", type=OPLmetamodel_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueConstraint39: BinaryAssociation = BinaryAssociation(
    name="valueConstraint39",
    ends={
        Property(name="OPLmetamodel_Expression41", type=OPLmetamodel_DataDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_DataDeclaration40", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps58: BinaryAssociation = BinaryAssociation(
    name="exps58",
    ends={
        Property(name="OPLmetamodel_Constraint60", type=OPLmetamodel_ForAllConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ForAllConstraint59", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
redefinedBaseType46: BinaryAssociation = BinaryAssociation(
    name="redefinedBaseType46",
    ends={
        Property(name="OPLmetamodel_EnumLiteral", type=OPLmetamodel_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_EnumerationType", type=OPLmetamodel_EnumLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domain47: BinaryAssociation = BinaryAssociation(
    name="domain47",
    ends={
        Property(name="OPLmetamodel_ParameterDomain", type=OPLmetamodel_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_FormalParameter48", type=OPLmetamodel_ParameterDomain, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boundVars49: BinaryAssociation = BinaryAssociation(
    name="boundVars49",
    ends={
        Property(name="OPLmetamodel_BindingRef", type=OPLmetamodel_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_FormalParameter50", type=OPLmetamodel_BindingRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
require51: BinaryAssociation = BinaryAssociation(
    name="require51",
    ends={
        Property(name="OPLmetamodel_Expression53", type=OPLmetamodel_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_FormalParameter52", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exps54: BinaryAssociation = BinaryAssociation(
    name="exps54",
    ends={
        Property(name="OPLmetamodel_Expression55", type=OPLmetamodel_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Extension", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers56: BinaryAssociation = BinaryAssociation(
    name="qualifiers56",
    ends={
        Property(name="OPLmetamodel_FormalParameter57", type=OPLmetamodel_ForAllConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_ForAllConstraint", type=OPLmetamodel_FormalParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bounds84: BinaryAssociation = BinaryAssociation(
    name="bounds84",
    ends={
        Property(name="OPLmetamodel_RangeType", type=OPLmetamodel_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Interval", type=OPLmetamodel_RangeType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size85: BinaryAssociation = BinaryAssociation(
    name="size85",
    ends={
        Property(name="OPLmetamodel_NumericType", type=OPLmetamodel_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Interval86", type=OPLmetamodel_NumericType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intensity87: BinaryAssociation = BinaryAssociation(
    name="intensity87",
    ends={
        Property(name="OPLmetamodel_StepFunction", type=OPLmetamodel_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Interval88", type=OPLmetamodel_StepFunction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name61: BinaryAssociation = BinaryAssociation(
    name="name61",
    ends={
        Property(name="OPLmetamodel_FunctionRef", type=OPLmetamodel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Function", type=OPLmetamodel_FunctionRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body62: BinaryAssociation = BinaryAssociation(
    name="body62",
    ends={
        Property(name="OPLmetamodel_Expression64", type=OPLmetamodel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Function63", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters65: BinaryAssociation = BinaryAssociation(
    name="parameters65",
    ends={
        Property(name="OPLmetamodel_Reference", type=OPLmetamodel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Function66", type=OPLmetamodel_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
args67: BinaryAssociation = BinaryAssociation(
    name="args67",
    ends={
        Property(name="OPLmetamodel_Expression68", type=OPLmetamodel_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_FunctionCall", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test69: BinaryAssociation = BinaryAssociation(
    name="test69",
    ends={
        Property(name="OPLmetamodel_BooleanExpression", type=OPLmetamodel_IfConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IfConstraint", type=OPLmetamodel_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then70: BinaryAssociation = BinaryAssociation(
    name="then70",
    ends={
        Property(name="OPLmetamodel_Constraint72", type=OPLmetamodel_IfConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IfConstraint71", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else73: BinaryAssociation = BinaryAssociation(
    name="else73",
    ends={
        Property(name="OPLmetamodel_Constraint75", type=OPLmetamodel_IfConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IfConstraint74", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
test76: BinaryAssociation = BinaryAssociation(
    name="test76",
    ends={
        Property(name="OPLmetamodel_BooleanExpression77", type=OPLmetamodel_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IfExpression", type=OPLmetamodel_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then78: BinaryAssociation = BinaryAssociation(
    name="then78",
    ends={
        Property(name="OPLmetamodel_Expression80", type=OPLmetamodel_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IfExpression79", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else81: BinaryAssociation = BinaryAssociation(
    name="else81",
    ends={
        Property(name="OPLmetamodel_Expression83", type=OPLmetamodel_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IfExpression82", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resources109: BinaryAssociation = BinaryAssociation(
    name="resources109",
    ends={
        Property(name="OPLmetamodel_ResourceDeclaration", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model110", type=OPLmetamodel_ResourceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertions111: BinaryAssociation = BinaryAssociation(
    name="assertions111",
    ends={
        Property(name="OPLmetamodel_Constraint113", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model112", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
index89: BinaryAssociation = BinaryAssociation(
    name="index89",
    ends={
        Property(name="OPLmetamodel_Expression90", type=OPLmetamodel_IndexValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IndexValuePair", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value91: BinaryAssociation = BinaryAssociation(
    name="value91",
    ends={
        Property(name="OPLmetamodel_Expression93", type=OPLmetamodel_IndexValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_IndexValuePair92", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types94: BinaryAssociation = BinaryAssociation(
    name="types94",
    ends={
        Property(name="OPLmetamodel_DefinedType", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model", type=OPLmetamodel_DefinedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data95: BinaryAssociation = BinaryAssociation(
    name="data95",
    ends={
        Property(name="OPLmetamodel_DataDeclaration97", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model96", type=OPLmetamodel_DataDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints98: BinaryAssociation = BinaryAssociation(
    name="constraints98",
    ends={
        Property(name="OPLmetamodel_Constraint100", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model99", type=OPLmetamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instruction101: BinaryAssociation = BinaryAssociation(
    name="instruction101",
    ends={
        Property(name="OPLmetamodel_Objective", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model102", type=OPLmetamodel_Objective, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
functions103: BinaryAssociation = BinaryAssociation(
    name="functions103",
    ends={
        Property(name="OPLmetamodel_Function105", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model104", type=OPLmetamodel_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activities106: BinaryAssociation = BinaryAssociation(
    name="activities106",
    ends={
        Property(name="OPLmetamodel_ActivityDeclaration108", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model107", type=OPLmetamodel_ActivityDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scheduleInit114: BinaryAssociation = BinaryAssociation(
    name="scheduleInit114",
    ends={
        Property(name="OPLmetamodel_ScheduleInitialization", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model115", type=OPLmetamodel_ScheduleInitialization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scripts116: BinaryAssociation = BinaryAssociation(
    name="scripts116",
    ends={
        Property(name="OPLmetamodel_Script", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model117", type=OPLmetamodel_Script, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
settings118: BinaryAssociation = BinaryAssociation(
    name="settings118",
    ends={
        Property(name="OPLmetamodel_Setting", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model119", type=OPLmetamodel_Setting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations120: BinaryAssociation = BinaryAssociation(
    name="declarations120",
    ends={
        Property(name="OPLmetamodel_Declaration", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model121", type=OPLmetamodel_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
search122: BinaryAssociation = BinaryAssociation(
    name="search122",
    ends={
        Property(name="OPLmetamodel_SearchProcedure", type=OPLmetamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Model123", type=OPLmetamodel_SearchProcedure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="OPLmetamodel_Expression126", type=OPLmetamodel_Objective, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Objective125", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
deref127: BinaryAssociation = BinaryAssociation(
    name="deref127",
    ends={
        Property(name="OPLmetamodel_Reference128", type=OPLmetamodel_PathDereference, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_PathDereference", type=OPLmetamodel_Reference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base129: BinaryAssociation = BinaryAssociation(
    name="base129",
    ends={
        Property(name="OPLmetamodel_PathExpression131", type=OPLmetamodel_PathDereference, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_PathDereference130", type=OPLmetamodel_PathExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound139: BinaryAssociation = BinaryAssociation(
    name="upperBound139",
    ends={
        Property(name="OPLmetamodel_NumericType141", type=OPLmetamodel_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RangeType140", type=OPLmetamodel_NumericType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerBound142: BinaryAssociation = BinaryAssociation(
    name="lowerBound142",
    ends={
        Property(name="OPLmetamodel_NumericType144", type=OPLmetamodel_RangeType, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RangeType143", type=OPLmetamodel_NumericType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerLimit132: BinaryAssociation = BinaryAssociation(
    name="lowerLimit132",
    ends={
        Property(name="OPLmetamodel_NumericExpression", type=OPLmetamodel_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RangeExpression", type=OPLmetamodel_NumericExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperLimit133: BinaryAssociation = BinaryAssociation(
    name="upperLimit133",
    ends={
        Property(name="OPLmetamodel_NumericExpression135", type=OPLmetamodel_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RangeExpression134", type=OPLmetamodel_NumericExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type136: BinaryAssociation = BinaryAssociation(
    name="type136",
    ends={
        Property(name="OPLmetamodel_NumericType138", type=OPLmetamodel_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RangeExpression137", type=OPLmetamodel_NumericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindingVar151: BinaryAssociation = BinaryAssociation(
    name="bindingVar151",
    ends={
        Property(name="OPLmetamodel_BindingRef152", type=OPLmetamodel_RelationalInit, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RelationalInit", type=OPLmetamodel_BindingRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sources153: BinaryAssociation = BinaryAssociation(
    name="sources153",
    ends={
        Property(name="OPLmetamodel_VariableBinding", type=OPLmetamodel_RelationalInit, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RelationalInit154", type=OPLmetamodel_VariableBinding, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relation155: BinaryAssociation = BinaryAssociation(
    name="relation155",
    ends={
        Property(name="OPLmetamodel_RelationalExpression", type=OPLmetamodel_RelationalInit, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RelationalInit156", type=OPLmetamodel_RelationalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fields145: BinaryAssociation = BinaryAssociation(
    name="fields145",
    ends={
        Property(name="OPLmetamodel_RecordField", type=OPLmetamodel_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Record", type=OPLmetamodel_RecordField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type146: BinaryAssociation = BinaryAssociation(
    name="type146",
    ends={
        Property(name="OPLmetamodel_AbstractType148", type=OPLmetamodel_RecordField, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RecordField147", type=OPLmetamodel_AbstractType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fieldPairs149: BinaryAssociation = BinaryAssociation(
    name="fieldPairs149",
    ends={
        Property(name="OPLmetamodel_IndexValuePair150", type=OPLmetamodel_RecordValue, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_RecordValue", type=OPLmetamodel_IndexValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseType167: BinaryAssociation = BinaryAssociation(
    name="baseType167",
    ends={
        Property(name="OPLmetamodel_SetType", type=OPLmetamodel_AbstractType, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OPLmetamodel_AbstractType168", type=OPLmetamodel_SetType, multiplicity=Multiplicity(1, 1))
    }
)
elements169: BinaryAssociation = BinaryAssociation(
    name="elements169",
    ends={
        Property(name="OPLmetamodel_Entity", type=OPLmetamodel_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_SetType170", type=OPLmetamodel_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items171: BinaryAssociation = BinaryAssociation(
    name="items171",
    ends={
        Property(name="OPLmetamodel_Expression172", type=OPLmetamodel_SetValue, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_SetValue", type=OPLmetamodel_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionMatrix173: BinaryAssociation = BinaryAssociation(
    name="transitionMatrix173",
    ends={
        Property(name="OPLmetamodel_SetType174", type=OPLmetamodel_StateFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_StateFunction", type=OPLmetamodel_SetType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id157: BinaryAssociation = BinaryAssociation(
    name="id157",
    ends={
        Property(name="OPLmetamodel_Reference159", type=OPLmetamodel_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Script158", type=OPLmetamodel_Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements160: BinaryAssociation = BinaryAssociation(
    name="statements160",
    ends={
        Property(name="OPLmetamodel_ScriptStatement", type=OPLmetamodel_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Script161", type=OPLmetamodel_ScriptStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
intervals162: BinaryAssociation = BinaryAssociation(
    name="intervals162",
    ends={
        Property(name="OPLmetamodel_Interval163", type=OPLmetamodel_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Sequence", type=OPLmetamodel_Interval, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
types164: BinaryAssociation = BinaryAssociation(
    name="types164",
    ends={
        Property(name="OPLmetamodel_DefinedType166", type=OPLmetamodel_Sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_Sequence165", type=OPLmetamodel_DefinedType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vars175: BinaryAssociation = BinaryAssociation(
    name="vars175",
    ends={
        Property(name="OPLmetamodel_BindingRef176", type=OPLmetamodel_TupleBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_TupleBinding", type=OPLmetamodel_BindingRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exp177: BinaryAssociation = BinaryAssociation(
    name="exp177",
    ends={
        Property(name="OPLmetamodel_Expression178", type=OPLmetamodel_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_UnaryExpression", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vars179: BinaryAssociation = BinaryAssociation(
    name="vars179",
    ends={
        Property(name="OPLmetamodel_BindingRef181", type=OPLmetamodel_VariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_VariableBinding180", type=OPLmetamodel_BindingRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
domain182: BinaryAssociation = BinaryAssociation(
    name="domain182",
    ends={
        Property(name="OPLmetamodel_Expression184", type=OPLmetamodel_VariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="OPLmetamodel_VariableBinding183", type=OPLmetamodel_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_OPLmetamodel_ActivityDeclaration_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_ActivityDeclaration)
gen_OPLmetamodel_AggregateExp_Expression = Generalization(general=Expression, specific=OPLmetamodel_AggregateExp)
gen_OPLmetamodel_ArrayValue_Expression = Generalization(general=Expression, specific=OPLmetamodel_ArrayValue)
gen_OPLmetamodel_ArrayDereference_PathExpression = Generalization(general=PathExpression, specific=OPLmetamodel_ArrayDereference)
gen_OPLmetamodel_ArraySlotConstraint_Expression = Generalization(general=Expression, specific=OPLmetamodel_ArraySlotConstraint)
gen_OPLmetamodel_ArrayType_DefinedType = Generalization(general=DefinedType, specific=OPLmetamodel_ArrayType)
gen_OPLmetamodel_BooleanExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=OPLmetamodel_BooleanExpression)
gen_OPLmetamodel_Assertion_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_Assertion)
gen_OPLmetamodel_BinaryExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_BinaryExpression)
gen_OPLmetamodel_BinaryOperator_AbstractBinaryOperator = Generalization(general=AbstractBinaryOperator, specific=OPLmetamodel_BinaryOperator)
gen_OPLmetamodel_BindingRef_Reference = Generalization(general=Reference, specific=OPLmetamodel_BindingRef)
gen_OPLmetamodel_BlockExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_BlockExpression)
gen_OPLmetamodel_BooleanType_PrimitiveType = Generalization(general=PrimitiveType, specific=OPLmetamodel_BooleanType)
gen_OPLmetamodel_BuiltInFunction_Function = Generalization(general=Function, specific=OPLmetamodel_BuiltInFunction)
gen_OPLmetamodel_CollectionExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_CollectionExpression)
gen_OPLmetamodel_Constraint_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_Constraint)
gen_OPLmetamodel_Comprehension_CollectionExpression = Generalization(general=CollectionExpression, specific=OPLmetamodel_Comprehension)
gen_OPLmetamodel_CumulativeFunction_Function = Generalization(general=Function, specific=OPLmetamodel_CumulativeFunction)
gen_OPLmetamodel_DataDeclaration_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_DataDeclaration)
gen_OPLmetamodel_DataObject_Initialization = Generalization(general=Initialization, specific=OPLmetamodel_DataObject)
gen_OPLmetamodel_DataRef_Reference = Generalization(general=Reference, specific=OPLmetamodel_DataRef)
gen_OPLmetamodel_DefinedType_AbstractType = Generalization(general=AbstractType, specific=OPLmetamodel_DefinedType)
gen_OPLmetamodel_DefinedType_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_DefinedType)
gen_OPLmetamodel_Function_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_Function)
gen_OPLmetamodel_EnumerationType_SetType = Generalization(general=SetType, specific=OPLmetamodel_EnumerationType)
gen_OPLmetamodel_EnumLiteral_PrimitiveType = Generalization(general=PrimitiveType, specific=OPLmetamodel_EnumLiteral)
gen_OPLmetamodel_EnumLiteral_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=OPLmetamodel_EnumLiteral)
gen_OPLmetamodel_FloatRangeType_FloatType = Generalization(general=FloatType, specific=OPLmetamodel_FloatRangeType)
gen_OPLmetamodel_FloatRangeType_RangeType = Generalization(general=RangeType, specific=OPLmetamodel_FloatRangeType)
gen_OPLmetamodel_FloatType_NumericType = Generalization(general=NumericType, specific=OPLmetamodel_FloatType)
gen_OPLmetamodel_Extension_CollectionExpression = Generalization(general=CollectionExpression, specific=OPLmetamodel_Extension)
gen_OPLmetamodel_FloatExpression_NumericExpression = Generalization(general=NumericExpression, specific=OPLmetamodel_FloatExpression)
gen_OPLmetamodel_ForAllConstraint_Constraint = Generalization(general=Constraint, specific=OPLmetamodel_ForAllConstraint)
gen_OPLmetamodel_FunctionCall_PathExpression = Generalization(general=PathExpression, specific=OPLmetamodel_FunctionCall)
gen_OPLmetamodel_IfConstraint_Constraint = Generalization(general=Constraint, specific=OPLmetamodel_IfConstraint)
gen_OPLmetamodel_IfExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_IfExpression)
gen_OPLmetamodel_IntegerType_NumericType = Generalization(general=NumericType, specific=OPLmetamodel_IntegerType)
gen_OPLmetamodel_IntegerExpression_NumericExpression = Generalization(general=NumericExpression, specific=OPLmetamodel_IntegerExpression)
gen_OPLmetamodel_IntegerRangeType_IntegerType = Generalization(general=IntegerType, specific=OPLmetamodel_IntegerRangeType)
gen_OPLmetamodel_IntegerRangeType_RangeType = Generalization(general=RangeType, specific=OPLmetamodel_IntegerRangeType)
gen_OPLmetamodel_IndexValuePair_Expression = Generalization(general=Expression, specific=OPLmetamodel_IndexValuePair)
gen_OPLmetamodel_PathExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_PathExpression)
gen_OPLmetamodel_NumericExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=OPLmetamodel_NumericExpression)
gen_OPLmetamodel_NumericType_PrimitiveType = Generalization(general=PrimitiveType, specific=OPLmetamodel_NumericType)
gen_OPLmetamodel_Objective_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_Objective)
gen_OPLmetamodel_ParameterRef_Reference = Generalization(general=Reference, specific=OPLmetamodel_ParameterRef)
gen_OPLmetamodel_PathDereference_PathExpression = Generalization(general=PathExpression, specific=OPLmetamodel_PathDereference)
gen_OPLmetamodel_PiecewiseLinearFunction_Function = Generalization(general=Function, specific=OPLmetamodel_PiecewiseLinearFunction)
gen_OPLmetamodel_PositiveFloatType_FloatType = Generalization(general=FloatType, specific=OPLmetamodel_PositiveFloatType)
gen_OPLmetamodel_PrimitiveExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_PrimitiveExpression)
gen_OPLmetamodel_ReadFile_DataInitMethods = Generalization(general=DataInitMethods, specific=OPLmetamodel_ReadFile)
gen_OPLmetamodel_PrimitiveType_AbstractType = Generalization(general=AbstractType, specific=OPLmetamodel_PrimitiveType)
gen_OPLmetamodel_PositiveIntegerType_IntegerType = Generalization(general=IntegerType, specific=OPLmetamodel_PositiveIntegerType)
gen_OPLmetamodel_QueryUser_DataInitMethods = Generalization(general=DataInitMethods, specific=OPLmetamodel_QueryUser)
gen_OPLmetamodel_RangeExpression_NumericExpression = Generalization(general=NumericExpression, specific=OPLmetamodel_RangeExpression)
gen_OPLmetamodel_RangeType_SetType = Generalization(general=SetType, specific=OPLmetamodel_RangeType)
gen_OPLmetamodel_ReflectiveFunction_BuiltInFunction = Generalization(general=BuiltInFunction, specific=OPLmetamodel_ReflectiveFunction)
gen_OPLmetamodel_RelationalExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=OPLmetamodel_RelationalExpression)
gen_OPLmetamodel_RelationalExpression_BooleanExpression = Generalization(general=BooleanExpression, specific=OPLmetamodel_RelationalExpression)
gen_OPLmetamodel_RelationalInit_Initialization = Generalization(general=Initialization, specific=OPLmetamodel_RelationalInit)
gen_OPLmetamodel_Record_ParameterDomain = Generalization(general=ParameterDomain, specific=OPLmetamodel_Record)
gen_OPLmetamodel_Record_DefinedType = Generalization(general=DefinedType, specific=OPLmetamodel_Record)
gen_OPLmetamodel_RecordValue_Expression = Generalization(general=Expression, specific=OPLmetamodel_RecordValue)
gen_OPLmetamodel_Reference_Expression = Generalization(general=Expression, specific=OPLmetamodel_Reference)
gen_OPLmetamodel_SetValue_Expression = Generalization(general=Expression, specific=OPLmetamodel_SetValue)
gen_OPLmetamodel_StateFunction_Function = Generalization(general=Function, specific=OPLmetamodel_StateFunction)
gen_OPLmetamodel_StepFunction_PiecewiseLinearFunction = Generalization(general=PiecewiseLinearFunction, specific=OPLmetamodel_StepFunction)
gen_OPLmetamodel_StringExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=OPLmetamodel_StringExpression)
gen_OPLmetamodel_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=OPLmetamodel_StringType)
gen_OPLmetamodel_RelationalOperator_AbstractBinaryOperator = Generalization(general=AbstractBinaryOperator, specific=OPLmetamodel_RelationalOperator)
gen_OPLmetamodel_ResourceDeclaration_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_ResourceDeclaration)
gen_OPLmetamodel_ScheduleInitialization_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_ScheduleInitialization)
gen_OPLmetamodel_Script_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_Script)
gen_OPLmetamodel_Setting_Declaration = Generalization(general=Declaration, specific=OPLmetamodel_Setting)
gen_OPLmetamodel_SetType_DefinedType = Generalization(general=DefinedType, specific=OPLmetamodel_SetType)
gen_OPLmetamodel_SetType_ParameterDomain = Generalization(general=ParameterDomain, specific=OPLmetamodel_SetType)
gen_OPLmetamodel_UnaryExpression_Expression = Generalization(general=Expression, specific=OPLmetamodel_UnaryExpression)
gen_OPLmetamodel_Writeln_ScriptStatement = Generalization(general=ScriptStatement, specific=OPLmetamodel_Writeln)

# Domain Model
domain_model = DomainModel(
    name="OPLmetamodel",
    types={OPLmetamodel_Expression, OPLmetamodel_AllExpression, OPLmetamodel_AbstractBinaryOperator, OPLmetamodel_AbstractType, OPLmetamodel_ActivityDeclaration, Declaration, OPLmetamodel_Number, OPLmetamodel_AggregateExp, Expression, OPLmetamodel_FormalParameter, OPLmetamodel_ArrayValue, OPLmetamodel_ArrayDereference, PathExpression, OPLmetamodel_PathExpression, OPLmetamodel_ArraySlotConstraint, OPLmetamodel_ArrayType, DefinedType, OPLmetamodel_DataRef, OPLmetamodel_BooleanExpression, PrimitiveExpression, OPLmetamodel_Assertion, OPLmetamodel_Constraint, OPLmetamodel_BinaryExpression, OPLmetamodel_BinaryOperator, AbstractBinaryOperator, OPLmetamodel_BindingRef, Reference, OPLmetamodel_BlockExpression, OPLmetamodel_BooleanBlock, OPLmetamodel_Initialization, OPLmetamodel_BooleanType, PrimitiveType, OPLmetamodel_BuiltInFunction, Function, OPLmetamodel_CollectionExpression, OPLmetamodel_Comprehension, CollectionExpression, OPLmetamodel_CumulativeFunction, OPLmetamodel_DataDeclaration, OPLmetamodel_ParameterDeclaration, OPLmetamodel_DataInitMethods, OPLmetamodel_DataObject, Initialization, OPLmetamodel_Declaration, OPLmetamodel_DeferredInit, OPLmetamodel_DefinedType, AbstractType, OPLmetamodel_Function, OPLmetamodel_DisplayInstruction, OPLmetamodel_EnumerationType, SetType, OPLmetamodel_EnumLiteral, OPLmetamodel_Entity, OPLmetamodel_Error, OPLmetamodel_FloatRangeType, FloatType, RangeType, OPLmetamodel_FloatType, NumericType, OPLmetamodel_ParameterDomain, OPLmetamodel_Extension, OPLmetamodel_FloatExpression, NumericExpression, OPLmetamodel_ForAllConstraint, Constraint, OPLmetamodel_NumericType, OPLmetamodel_StepFunction, OPLmetamodel_FunctionRef, OPLmetamodel_Reference, OPLmetamodel_FunctionCall, OPLmetamodel_IfConstraint, OPLmetamodel_IfExpression, OPLmetamodel_In, OPLmetamodel_IntegerType, OPLmetamodel_Interval, OPLmetamodel_RangeType, OPLmetamodel_ResourceDeclaration, OPLmetamodel_IntegerExpression, OPLmetamodel_IntegerRangeType, IntegerType, OPLmetamodel_IndexValuePair, OPLmetamodel_Model, OPLmetamodel_Objective, OPLmetamodel_PiecewiseExpression, OPLmetamodel_PiecewiseLinearFunction, OPLmetamodel_ScheduleInitialization, OPLmetamodel_Script, OPLmetamodel_Setting, OPLmetamodel_SearchProcedure, OPLmetamodel_NumericExpression, OPLmetamodel_Operator, OPLmetamodel_ParameterRef, OPLmetamodel_PathDereference, OPLmetamodel_PositiveFloatType, OPLmetamodel_PrimitiveExpression, OPLmetamodel_ReadFile, OPLmetamodel_PrimitiveType, OPLmetamodel_PositiveIntegerType, OPLmetamodel_QueryUser, DataInitMethods, OPLmetamodel_RangeExpression, OPLmetamodel_ReflectiveFunction, BuiltInFunction, OPLmetamodel_RelationalExpression, BinaryExpression, BooleanExpression, OPLmetamodel_RelationalInit, OPLmetamodel_VariableBinding, OPLmetamodel_Record, ParameterDomain, OPLmetamodel_RecordField, OPLmetamodel_RecordValue, OPLmetamodel_SetValue, OPLmetamodel_StateFunction, PiecewiseLinearFunction, OPLmetamodel_StringExpression, OPLmetamodel_StringType, OPLmetamodel_TupleBinding, OPLmetamodel_RelationalOperator, OPLmetamodel_ScriptStatement, OPLmetamodel_Sequence, OPLmetamodel_SetType, OPLmetamodel_UnaryExpression, OPLmetamodel_Writeln, ScriptStatement, BinaryOp, AggOp, SetOp, UnaryOp, LogicalOp, MembershipOp, OptimizationMode, Quantifier, RelationalOp},
    associations={body2, qualifiers4, duration0, parameters1, items18, body6, array9, index10, target13, baseType15, subscripts16, exp20, lhs21, rhs23, op26, blocks28, type34, value37, exp29, variable32, exps42, parameters44, valueConstraint39, exps58, redefinedBaseType46, domain47, boundVars49, require51, exps54, qualifiers56, bounds84, size85, intensity87, name61, body62, parameters65, args67, test69, then70, else73, test76, then78, else81, resources109, assertions111, index89, value91, types94, data95, constraints98, instruction101, functions103, activities106, scheduleInit114, scripts116, settings118, declarations120, search122, expression124, deref127, base129, upperBound139, lowerBound142, lowerLimit132, upperLimit133, type136, bindingVar151, sources153, relation155, fields145, type146, fieldPairs149, baseType167, elements169, items171, transitionMatrix173, id157, statements160, intervals162, types164, vars175, exp177, vars179, domain182},
    generalizations={gen_OPLmetamodel_ActivityDeclaration_Declaration, gen_OPLmetamodel_AggregateExp_Expression, gen_OPLmetamodel_ArrayValue_Expression, gen_OPLmetamodel_ArrayDereference_PathExpression, gen_OPLmetamodel_ArraySlotConstraint_Expression, gen_OPLmetamodel_ArrayType_DefinedType, gen_OPLmetamodel_BooleanExpression_PrimitiveExpression, gen_OPLmetamodel_Assertion_Declaration, gen_OPLmetamodel_BinaryExpression_Expression, gen_OPLmetamodel_BinaryOperator_AbstractBinaryOperator, gen_OPLmetamodel_BindingRef_Reference, gen_OPLmetamodel_BlockExpression_Expression, gen_OPLmetamodel_BooleanType_PrimitiveType, gen_OPLmetamodel_BuiltInFunction_Function, gen_OPLmetamodel_CollectionExpression_Expression, gen_OPLmetamodel_Constraint_Declaration, gen_OPLmetamodel_Comprehension_CollectionExpression, gen_OPLmetamodel_CumulativeFunction_Function, gen_OPLmetamodel_DataDeclaration_Declaration, gen_OPLmetamodel_DataObject_Initialization, gen_OPLmetamodel_DataRef_Reference, gen_OPLmetamodel_DefinedType_AbstractType, gen_OPLmetamodel_DefinedType_Declaration, gen_OPLmetamodel_Function_Declaration, gen_OPLmetamodel_EnumerationType_SetType, gen_OPLmetamodel_EnumLiteral_PrimitiveType, gen_OPLmetamodel_EnumLiteral_PrimitiveExpression, gen_OPLmetamodel_FloatRangeType_FloatType, gen_OPLmetamodel_FloatRangeType_RangeType, gen_OPLmetamodel_FloatType_NumericType, gen_OPLmetamodel_Extension_CollectionExpression, gen_OPLmetamodel_FloatExpression_NumericExpression, gen_OPLmetamodel_ForAllConstraint_Constraint, gen_OPLmetamodel_FunctionCall_PathExpression, gen_OPLmetamodel_IfConstraint_Constraint, gen_OPLmetamodel_IfExpression_Expression, gen_OPLmetamodel_IntegerType_NumericType, gen_OPLmetamodel_IntegerExpression_NumericExpression, gen_OPLmetamodel_IntegerRangeType_IntegerType, gen_OPLmetamodel_IntegerRangeType_RangeType, gen_OPLmetamodel_IndexValuePair_Expression, gen_OPLmetamodel_PathExpression_Expression, gen_OPLmetamodel_NumericExpression_PrimitiveExpression, gen_OPLmetamodel_NumericType_PrimitiveType, gen_OPLmetamodel_Objective_Declaration, gen_OPLmetamodel_ParameterRef_Reference, gen_OPLmetamodel_PathDereference_PathExpression, gen_OPLmetamodel_PiecewiseLinearFunction_Function, gen_OPLmetamodel_PositiveFloatType_FloatType, gen_OPLmetamodel_PrimitiveExpression_Expression, gen_OPLmetamodel_ReadFile_DataInitMethods, gen_OPLmetamodel_PrimitiveType_AbstractType, gen_OPLmetamodel_PositiveIntegerType_IntegerType, gen_OPLmetamodel_QueryUser_DataInitMethods, gen_OPLmetamodel_RangeExpression_NumericExpression, gen_OPLmetamodel_RangeType_SetType, gen_OPLmetamodel_ReflectiveFunction_BuiltInFunction, gen_OPLmetamodel_RelationalExpression_BinaryExpression, gen_OPLmetamodel_RelationalExpression_BooleanExpression, gen_OPLmetamodel_RelationalInit_Initialization, gen_OPLmetamodel_Record_ParameterDomain, gen_OPLmetamodel_Record_DefinedType, gen_OPLmetamodel_RecordValue_Expression, gen_OPLmetamodel_Reference_Expression, gen_OPLmetamodel_SetValue_Expression, gen_OPLmetamodel_StateFunction_Function, gen_OPLmetamodel_StepFunction_PiecewiseLinearFunction, gen_OPLmetamodel_StringExpression_PrimitiveExpression, gen_OPLmetamodel_StringType_PrimitiveType, gen_OPLmetamodel_RelationalOperator_AbstractBinaryOperator, gen_OPLmetamodel_ResourceDeclaration_Declaration, gen_OPLmetamodel_ScheduleInitialization_Declaration, gen_OPLmetamodel_Script_Declaration, gen_OPLmetamodel_Setting_Declaration, gen_OPLmetamodel_SetType_DefinedType, gen_OPLmetamodel_SetType_ParameterDomain, gen_OPLmetamodel_UnaryExpression_Expression, gen_OPLmetamodel_Writeln_ScriptStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)