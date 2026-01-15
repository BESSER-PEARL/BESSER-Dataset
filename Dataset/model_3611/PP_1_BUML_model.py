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
pp1_PuppetManifest = Class(name="pp1::PuppetManifest")
ExpressionBlock = Class(name="ExpressionBlock")
pp1_Expression = Class(name="pp1::Expression")
pp1_ResourceBody = Class(name="pp1::ResourceBody")
pp1_AttributeOperations = Class(name="pp1::AttributeOperations")
pp1_Case = Class(name="pp1::Case")
pp1_AttributeOperation = Class(name="pp1::AttributeOperation")
pp1_ICollectQuery = Class(name="pp1::ICollectQuery", is_abstract=True)
pp1_VirtualCollectQuery = Class(name="pp1::VirtualCollectQuery")
UnaryExpression = Class(name="UnaryExpression")
ICollectQuery = Class(name="ICollectQuery")
pp1_ExportedCollectQuery = Class(name="pp1::ExportedCollectQuery")
pp1_HostClassDefinition = Class(name="pp1::HostClassDefinition")
Definition = Class(name="Definition")
pp1_LiteralExpression = Class(name="pp1::LiteralExpression", is_abstract=True)
pp1_Definition = Class(name="pp1::Definition")
Expression = Class(name="Expression")
pp1_DefinitionArgumentList = Class(name="pp1::DefinitionArgumentList")
pp1_DefinitionArgument = Class(name="pp1::DefinitionArgument")
pp1_CaseExpression = Class(name="pp1::CaseExpression")
pp1_IfExpression = Class(name="pp1::IfExpression")
pp1_LiteralNameOrReference = Class(name="pp1::LiteralNameOrReference")
LiteralExpression = Class(name="LiteralExpression")
pp1_ResourceExpression = Class(name="pp1::ResourceExpression")
pp1_ImportExpression = Class(name="pp1::ImportExpression")
pp1_IQuotedString = Class(name="pp1::IQuotedString", is_abstract=True)
pp1_LiteralList = Class(name="pp1::LiteralList")
pp1_LiteralHash = Class(name="pp1::LiteralHash")
pp1_HashEntry = Class(name="pp1::HashEntry")
pp1_SelectorEntry = Class(name="pp1::SelectorEntry")
pp1_FunctionCall = Class(name="pp1::FunctionCall")
WithLambdaExpression = Class(name="WithLambdaExpression")
pp1_LiteralBoolean = Class(name="pp1::LiteralBoolean")
pp1_LiteralUndef = Class(name="pp1::LiteralUndef")
pp1_LiteralDefault = Class(name="pp1::LiteralDefault")
pp1_LiteralRegex = Class(name="pp1::LiteralRegex")
pp1_LiteralName = Class(name="pp1::LiteralName")
pp1_VariableExpression = Class(name="pp1::VariableExpression")
pp1_RelationshipExpression = Class(name="pp1::RelationshipExpression")
BinaryOpExpression = Class(name="BinaryOpExpression")
pp1_AssignmentExpression = Class(name="pp1::AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
pp1_AppendExpression = Class(name="pp1::AppendExpression")
pp1_OrExpression = Class(name="pp1::OrExpression")
pp1_AndExpression = Class(name="pp1::AndExpression")
pp1_RelationalExpression = Class(name="pp1::RelationalExpression")
pp1_EqualityExpression = Class(name="pp1::EqualityExpression")
pp1_ShiftExpression = Class(name="pp1::ShiftExpression")
pp1_AdditiveExpression = Class(name="pp1::AdditiveExpression")
pp1_MultiplicativeExpression = Class(name="pp1::MultiplicativeExpression")
pp1_MatchingExpression = Class(name="pp1::MatchingExpression")
pp1_InExpression = Class(name="pp1::InExpression")
pp1_AtExpression = Class(name="pp1::AtExpression")
ParameterizedExpression = Class(name="ParameterizedExpression")
pp1_CollectExpression = Class(name="pp1::CollectExpression")
pp1_SelectorExpression = Class(name="pp1::SelectorExpression")
pp1_UnaryNotExpression = Class(name="pp1::UnaryNotExpression")
pp1_BinaryOpExpression = Class(name="pp1::BinaryOpExpression", is_abstract=True)
pp1_BinaryExpression = Class(name="pp1::BinaryExpression", is_abstract=True)
pp1_ParameterizedExpression = Class(name="pp1::ParameterizedExpression", is_abstract=True)
pp1_NodeDefinition = Class(name="pp1::NodeDefinition")
pp1_UnaryExpression = Class(name="pp1::UnaryExpression", is_abstract=True)
pp1_UnaryMinusExpression = Class(name="pp1::UnaryMinusExpression")
pp1_TextExpression = Class(name="pp1::TextExpression", is_abstract=True)
pp1_ExpressionBlock = Class(name="pp1::ExpressionBlock", is_abstract=True)
pp1_ElseExpression = Class(name="pp1::ElseExpression")
pp1_ElseIfExpression = Class(name="pp1::ElseIfExpression")
IfExpression = Class(name="IfExpression")
pp1_VirtualNameOrReference = Class(name="pp1::VirtualNameOrReference")
pp1_ParenthesisedExpression = Class(name="pp1::ParenthesisedExpression")
pp1_ExprList = Class(name="pp1::ExprList")
pp1_DoubleQuotedString = Class(name="pp1::DoubleQuotedString")
StringExpression = Class(name="StringExpression")
IQuotedString = Class(name="IQuotedString")
pp1_SingleQuotedString = Class(name="pp1::SingleQuotedString")
pp1_StringExpression = Class(name="pp1::StringExpression", is_abstract=True)
pp1_UnquotedString = Class(name="pp1::UnquotedString")
pp1_InterpolatedVariable = Class(name="pp1::InterpolatedVariable")
pp1_VerbatimTE = Class(name="pp1::VerbatimTE")
TextExpression = Class(name="TextExpression")
pp1_ExpressionTE = Class(name="pp1::ExpressionTE")
pp1_VariableTE = Class(name="pp1::VariableTE")
pp1_WithLambdaExpression = Class(name="pp1::WithLambdaExpression")
pp1_LiteralClass = Class(name="pp1::LiteralClass")
pp1_UnlessExpression = Class(name="pp1::UnlessExpression")
pp1_Lambda = Class(name="pp1::Lambda", is_abstract=True)
pp1_NamedAccessExpression = Class(name="pp1::NamedAccessExpression")
pp1_MethodCall = Class(name="pp1::MethodCall")
pp1_JavaLambda = Class(name="pp1::JavaLambda")
Lambda = Class(name="Lambda")
pp1_RubyLambda = Class(name="pp1::RubyLambda")
pp1_SeparatorExpression = Class(name="pp1::SeparatorExpression")

# pp1_PuppetManifest class attributes and methods

# ExpressionBlock class attributes and methods

# pp1_Expression class attributes and methods

# pp1_ResourceBody class attributes and methods

# pp1_AttributeOperations class attributes and methods

# pp1_Case class attributes and methods

# pp1_AttributeOperation class attributes and methods
pp1_AttributeOperation_key: Property = Property(name="key", type=StringType)
pp1_AttributeOperation_op: Property = Property(name="op", type=StringType)
pp1_AttributeOperation.attributes={pp1_AttributeOperation_key, pp1_AttributeOperation_op}

# pp1_ICollectQuery class attributes and methods

# pp1_VirtualCollectQuery class attributes and methods

# UnaryExpression class attributes and methods

# ICollectQuery class attributes and methods

# pp1_ExportedCollectQuery class attributes and methods

# pp1_HostClassDefinition class attributes and methods

# Definition class attributes and methods

# pp1_LiteralExpression class attributes and methods

# pp1_Definition class attributes and methods
pp1_Definition_className: Property = Property(name="className", type=StringType)
pp1_Definition.attributes={pp1_Definition_className}

# Expression class attributes and methods

# pp1_DefinitionArgumentList class attributes and methods

# pp1_DefinitionArgument class attributes and methods
pp1_DefinitionArgument_argName: Property = Property(name="argName", type=StringType)
pp1_DefinitionArgument_op: Property = Property(name="op", type=StringType)
pp1_DefinitionArgument.attributes={pp1_DefinitionArgument_argName, pp1_DefinitionArgument_op}

# pp1_CaseExpression class attributes and methods

# pp1_IfExpression class attributes and methods

# pp1_LiteralNameOrReference class attributes and methods
pp1_LiteralNameOrReference_value: Property = Property(name="value", type=StringType)
pp1_LiteralNameOrReference.attributes={pp1_LiteralNameOrReference_value}

# LiteralExpression class attributes and methods

# pp1_ResourceExpression class attributes and methods

# pp1_ImportExpression class attributes and methods

# pp1_IQuotedString class attributes and methods

# pp1_LiteralList class attributes and methods

# pp1_LiteralHash class attributes and methods

# pp1_HashEntry class attributes and methods

# pp1_SelectorEntry class attributes and methods

# pp1_FunctionCall class attributes and methods

# WithLambdaExpression class attributes and methods

# pp1_LiteralBoolean class attributes and methods
pp1_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
pp1_LiteralBoolean.attributes={pp1_LiteralBoolean_value}

# pp1_LiteralUndef class attributes and methods

# pp1_LiteralDefault class attributes and methods

# pp1_LiteralRegex class attributes and methods
pp1_LiteralRegex_value: Property = Property(name="value", type=StringType)
pp1_LiteralRegex.attributes={pp1_LiteralRegex_value}

# pp1_LiteralName class attributes and methods
pp1_LiteralName_value: Property = Property(name="value", type=StringType)
pp1_LiteralName.attributes={pp1_LiteralName_value}

# pp1_VariableExpression class attributes and methods
pp1_VariableExpression_varName: Property = Property(name="varName", type=StringType)
pp1_VariableExpression.attributes={pp1_VariableExpression_varName}

# pp1_RelationshipExpression class attributes and methods

# BinaryOpExpression class attributes and methods

# pp1_AssignmentExpression class attributes and methods

# BinaryExpression class attributes and methods

# pp1_AppendExpression class attributes and methods

# pp1_OrExpression class attributes and methods

# pp1_AndExpression class attributes and methods

# pp1_RelationalExpression class attributes and methods

# pp1_EqualityExpression class attributes and methods

# pp1_ShiftExpression class attributes and methods

# pp1_AdditiveExpression class attributes and methods

# pp1_MultiplicativeExpression class attributes and methods

# pp1_MatchingExpression class attributes and methods

# pp1_InExpression class attributes and methods

# pp1_AtExpression class attributes and methods

# ParameterizedExpression class attributes and methods

# pp1_CollectExpression class attributes and methods

# pp1_SelectorExpression class attributes and methods

# pp1_UnaryNotExpression class attributes and methods

# pp1_BinaryOpExpression class attributes and methods
pp1_BinaryOpExpression_opName: Property = Property(name="opName", type=StringType)
pp1_BinaryOpExpression.attributes={pp1_BinaryOpExpression_opName}

# pp1_BinaryExpression class attributes and methods

# pp1_ParameterizedExpression class attributes and methods

# pp1_NodeDefinition class attributes and methods

# pp1_UnaryExpression class attributes and methods

# pp1_UnaryMinusExpression class attributes and methods

# pp1_TextExpression class attributes and methods

# pp1_ExpressionBlock class attributes and methods

# pp1_ElseExpression class attributes and methods

# pp1_ElseIfExpression class attributes and methods

# IfExpression class attributes and methods

# pp1_VirtualNameOrReference class attributes and methods
pp1_VirtualNameOrReference_value: Property = Property(name="value", type=StringType)
pp1_VirtualNameOrReference_exported: Property = Property(name="exported", type=BooleanType)
pp1_VirtualNameOrReference.attributes={pp1_VirtualNameOrReference_exported, pp1_VirtualNameOrReference_value}

# pp1_ParenthesisedExpression class attributes and methods

# pp1_ExprList class attributes and methods

# pp1_DoubleQuotedString class attributes and methods

# StringExpression class attributes and methods

# IQuotedString class attributes and methods

# pp1_SingleQuotedString class attributes and methods
pp1_SingleQuotedString_text: Property = Property(name="text", type=StringType)
pp1_SingleQuotedString.attributes={pp1_SingleQuotedString_text}

# pp1_StringExpression class attributes and methods

# pp1_UnquotedString class attributes and methods

# pp1_InterpolatedVariable class attributes and methods
pp1_InterpolatedVariable_varName: Property = Property(name="varName", type=StringType)
pp1_InterpolatedVariable.attributes={pp1_InterpolatedVariable_varName}

# pp1_VerbatimTE class attributes and methods
pp1_VerbatimTE_text: Property = Property(name="text", type=StringType)
pp1_VerbatimTE.attributes={pp1_VerbatimTE_text}

# TextExpression class attributes and methods

# pp1_ExpressionTE class attributes and methods

# pp1_VariableTE class attributes and methods
pp1_VariableTE_varName: Property = Property(name="varName", type=StringType)
pp1_VariableTE.attributes={pp1_VariableTE_varName}

# pp1_WithLambdaExpression class attributes and methods

# pp1_LiteralClass class attributes and methods

# pp1_UnlessExpression class attributes and methods

# pp1_Lambda class attributes and methods

# pp1_NamedAccessExpression class attributes and methods

# pp1_MethodCall class attributes and methods
pp1_MethodCall_parenthesized: Property = Property(name="parenthesized", type=BooleanType)
pp1_MethodCall.attributes={pp1_MethodCall_parenthesized}

# pp1_JavaLambda class attributes and methods
pp1_JavaLambda_farrow: Property = Property(name="farrow", type=BooleanType)
pp1_JavaLambda.attributes={pp1_JavaLambda_farrow}

# Lambda class attributes and methods

# pp1_RubyLambda class attributes and methods

# pp1_SeparatorExpression class attributes and methods

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="pp1_ResourceBody", type=pp1_AttributeOperations, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pp1_AttributeOperations", type=pp1_ResourceBody, multiplicity=Multiplicity(1, 1))
    }
)
cases20: BinaryAssociation = BinaryAssociation(
    name="cases20",
    ends={
        Property(name="pp1_Case", type=pp1_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_CaseExpression21", type=pp1_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameExpr1: BinaryAssociation = BinaryAssociation(
    name="nameExpr1",
    ends={
        Property(name="pp1_Expression", type=pp1_ResourceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ResourceBody2", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="pp1_Expression4", type=pp1_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_AttributeOperation", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="pp1_AttributeOperation7", type=pp1_AttributeOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_AttributeOperations6", type=pp1_AttributeOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="pp1_LiteralExpression", type=pp1_HostClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_HostClassDefinition", type=pp1_LiteralExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments9: BinaryAssociation = BinaryAssociation(
    name="arguments9",
    ends={
        Property(name="pp1_DefinitionArgumentList", type=pp1_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_Definition", type=pp1_DefinitionArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="pp1_Expression12", type=pp1_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_Definition11", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments13: BinaryAssociation = BinaryAssociation(
    name="arguments13",
    ends={
        Property(name="pp1_DefinitionArgument", type=pp1_DefinitionArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_DefinitionArgumentList14", type=pp1_DefinitionArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="pp1_Expression17", type=pp1_DefinitionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_DefinitionArgument16", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpr18: BinaryAssociation = BinaryAssociation(
    name="switchExpr18",
    ends={
        Property(name="pp1_Expression19", type=pp1_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_CaseExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value48: BinaryAssociation = BinaryAssociation(
    name="value48",
    ends={
        Property(name="pp1_Expression50", type=pp1_HashEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_HashEntry49", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements22: BinaryAssociation = BinaryAssociation(
    name="statements22",
    ends={
        Property(name="pp1_Expression24", type=pp1_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_Case23", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values25: BinaryAssociation = BinaryAssociation(
    name="values25",
    ends={
        Property(name="pp1_Expression27", type=pp1_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_Case26", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condExpr28: BinaryAssociation = BinaryAssociation(
    name="condExpr28",
    ends={
        Property(name="pp1_Expression29", type=pp1_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_IfExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatements30: BinaryAssociation = BinaryAssociation(
    name="thenStatements30",
    ends={
        Property(name="pp1_Expression32", type=pp1_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_IfExpression31", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement33: BinaryAssociation = BinaryAssociation(
    name="elseStatement33",
    ends={
        Property(name="pp1_Expression35", type=pp1_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_IfExpression34", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceExpr36: BinaryAssociation = BinaryAssociation(
    name="resourceExpr36",
    ends={
        Property(name="pp1_Expression37", type=pp1_ResourceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ResourceExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceData38: BinaryAssociation = BinaryAssociation(
    name="resourceData38",
    ends={
        Property(name="pp1_ResourceBody40", type=pp1_ResourceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ResourceExpression39", type=pp1_ResourceBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values41: BinaryAssociation = BinaryAssociation(
    name="values41",
    ends={
        Property(name="pp1_IQuotedString", type=pp1_ImportExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ImportExpression", type=pp1_IQuotedString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements42: BinaryAssociation = BinaryAssociation(
    name="elements42",
    ends={
        Property(name="pp1_Expression43", type=pp1_LiteralList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_LiteralList", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements44: BinaryAssociation = BinaryAssociation(
    name="elements44",
    ends={
        Property(name="pp1_HashEntry", type=pp1_LiteralHash, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_LiteralHash", type=pp1_HashEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key45: BinaryAssociation = BinaryAssociation(
    name="key45",
    ends={
        Property(name="pp1_Expression47", type=pp1_HashEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_HashEntry46", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classReference51: BinaryAssociation = BinaryAssociation(
    name="classReference51",
    ends={
        Property(name="pp1_Expression52", type=pp1_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_CollectExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query53: BinaryAssociation = BinaryAssociation(
    name="query53",
    ends={
        Property(name="pp1_ICollectQuery", type=pp1_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_CollectExpression54", type=pp1_ICollectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes55: BinaryAssociation = BinaryAssociation(
    name="attributes55",
    ends={
        Property(name="pp1_AttributeOperations57", type=pp1_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_CollectExpression56", type=pp1_AttributeOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExpr58: BinaryAssociation = BinaryAssociation(
    name="leftExpr58",
    ends={
        Property(name="pp1_Expression59", type=pp1_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_BinaryExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExpr60: BinaryAssociation = BinaryAssociation(
    name="rightExpr60",
    ends={
        Property(name="pp1_Expression62", type=pp1_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_BinaryExpression61", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExpr63: BinaryAssociation = BinaryAssociation(
    name="leftExpr63",
    ends={
        Property(name="pp1_Expression64", type=pp1_ParameterizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ParameterizedExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters65: BinaryAssociation = BinaryAssociation(
    name="parameters65",
    ends={
        Property(name="pp1_Expression67", type=pp1_ParameterizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ParameterizedExpression66", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostNames68: BinaryAssociation = BinaryAssociation(
    name="hostNames68",
    ends={
        Property(name="pp1_Expression69", type=pp1_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_NodeDefinition", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentName70: BinaryAssociation = BinaryAssociation(
    name="parentName70",
    ends={
        Property(name="pp1_Expression72", type=pp1_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_NodeDefinition71", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements73: BinaryAssociation = BinaryAssociation(
    name="statements73",
    ends={
        Property(name="pp1_Expression75", type=pp1_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_NodeDefinition74", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr76: BinaryAssociation = BinaryAssociation(
    name="expr76",
    ends={
        Property(name="pp1_Expression77", type=pp1_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_UnaryExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements78: BinaryAssociation = BinaryAssociation(
    name="statements78",
    ends={
        Property(name="pp1_Expression79", type=pp1_ExpressionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ExpressionBlock", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr80: BinaryAssociation = BinaryAssociation(
    name="expr80",
    ends={
        Property(name="pp1_Expression81", type=pp1_ParenthesisedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ParenthesisedExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions82: BinaryAssociation = BinaryAssociation(
    name="expressions82",
    ends={
        Property(name="pp1_Expression83", type=pp1_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ExprList", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringPart84: BinaryAssociation = BinaryAssociation(
    name="stringPart84",
    ends={
        Property(name="pp1_TextExpression", type=pp1_DoubleQuotedString, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_DoubleQuotedString", type=pp1_TextExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression85: BinaryAssociation = BinaryAssociation(
    name="expression85",
    ends={
        Property(name="pp1_Expression86", type=pp1_UnquotedString, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_UnquotedString", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression87: BinaryAssociation = BinaryAssociation(
    name="expression87",
    ends={
        Property(name="pp1_Expression88", type=pp1_ExpressionTE, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_ExpressionTE", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lambda101: BinaryAssociation = BinaryAssociation(
    name="lambda101",
    ends={
        Property(name="pp1_Lambda102", type=pp1_WithLambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_WithLambdaExpression", type=pp1_Lambda, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr89: BinaryAssociation = BinaryAssociation(
    name="condExpr89",
    ends={
        Property(name="pp1_Expression90", type=pp1_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_UnlessExpression", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatements91: BinaryAssociation = BinaryAssociation(
    name="thenStatements91",
    ends={
        Property(name="pp1_Expression93", type=pp1_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_UnlessExpression92", type=pp1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatement94: BinaryAssociation = BinaryAssociation(
    name="elseStatement94",
    ends={
        Property(name="pp1_Expression96", type=pp1_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_UnlessExpression95", type=pp1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments97: BinaryAssociation = BinaryAssociation(
    name="arguments97",
    ends={
        Property(name="pp1_DefinitionArgumentList98", type=pp1_Lambda, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_Lambda", type=pp1_DefinitionArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodExpr99: BinaryAssociation = BinaryAssociation(
    name="methodExpr99",
    ends={
        Property(name="pp1_Expression100", type=pp1_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pp1_MethodCall", type=pp1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_pp1_PuppetManifest_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp1_PuppetManifest)
gen_pp1_VirtualCollectQuery_UnaryExpression = Generalization(general=UnaryExpression, specific=pp1_VirtualCollectQuery)
gen_pp1_VirtualCollectQuery_ICollectQuery = Generalization(general=ICollectQuery, specific=pp1_VirtualCollectQuery)
gen_pp1_ExportedCollectQuery_UnaryExpression = Generalization(general=UnaryExpression, specific=pp1_ExportedCollectQuery)
gen_pp1_ExportedCollectQuery_ICollectQuery = Generalization(general=ICollectQuery, specific=pp1_ExportedCollectQuery)
gen_pp1_HostClassDefinition_Definition = Generalization(general=Definition, specific=pp1_HostClassDefinition)
gen_pp1_Definition_Expression = Generalization(general=Expression, specific=pp1_Definition)
gen_pp1_CaseExpression_Expression = Generalization(general=Expression, specific=pp1_CaseExpression)
gen_pp1_IfExpression_Expression = Generalization(general=Expression, specific=pp1_IfExpression)
gen_pp1_LiteralExpression_Expression = Generalization(general=Expression, specific=pp1_LiteralExpression)
gen_pp1_LiteralNameOrReference_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralNameOrReference)
gen_pp1_ResourceExpression_Expression = Generalization(general=Expression, specific=pp1_ResourceExpression)
gen_pp1_ImportExpression_Expression = Generalization(general=Expression, specific=pp1_ImportExpression)
gen_pp1_LiteralList_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralList)
gen_pp1_LiteralHash_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralHash)
gen_pp1_SelectorEntry_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_SelectorEntry)
gen_pp1_FunctionCall_WithLambdaExpression = Generalization(general=WithLambdaExpression, specific=pp1_FunctionCall)
gen_pp1_LiteralBoolean_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralBoolean)
gen_pp1_LiteralUndef_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralUndef)
gen_pp1_LiteralDefault_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralDefault)
gen_pp1_LiteralRegex_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralRegex)
gen_pp1_LiteralName_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralName)
gen_pp1_VariableExpression_Expression = Generalization(general=Expression, specific=pp1_VariableExpression)
gen_pp1_RelationshipExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_RelationshipExpression)
gen_pp1_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_AssignmentExpression)
gen_pp1_AppendExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_AppendExpression)
gen_pp1_OrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_OrExpression)
gen_pp1_AndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_AndExpression)
gen_pp1_RelationalExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_RelationalExpression)
gen_pp1_EqualityExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_EqualityExpression)
gen_pp1_ShiftExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_ShiftExpression)
gen_pp1_AdditiveExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_AdditiveExpression)
gen_pp1_MultiplicativeExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_MultiplicativeExpression)
gen_pp1_MatchingExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_MatchingExpression)
gen_pp1_InExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp1_InExpression)
gen_pp1_AtExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp1_AtExpression)
gen_pp1_CollectExpression_Expression = Generalization(general=Expression, specific=pp1_CollectExpression)
gen_pp1_SelectorExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp1_SelectorExpression)
gen_pp1_UnaryNotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=pp1_UnaryNotExpression)
gen_pp1_BinaryOpExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_BinaryOpExpression)
gen_pp1_BinaryExpression_Expression = Generalization(general=Expression, specific=pp1_BinaryExpression)
gen_pp1_ParameterizedExpression_Expression = Generalization(general=Expression, specific=pp1_ParameterizedExpression)
gen_pp1_NodeDefinition_Expression = Generalization(general=Expression, specific=pp1_NodeDefinition)
gen_pp1_UnaryExpression_Expression = Generalization(general=Expression, specific=pp1_UnaryExpression)
gen_pp1_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=pp1_UnaryMinusExpression)
gen_pp1_ExpressionBlock_Expression = Generalization(general=Expression, specific=pp1_ExpressionBlock)
gen_pp1_ElseExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp1_ElseExpression)
gen_pp1_ElseIfExpression_IfExpression = Generalization(general=IfExpression, specific=pp1_ElseIfExpression)
gen_pp1_VirtualNameOrReference_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_VirtualNameOrReference)
gen_pp1_ParenthesisedExpression_Expression = Generalization(general=Expression, specific=pp1_ParenthesisedExpression)
gen_pp1_ExprList_Expression = Generalization(general=Expression, specific=pp1_ExprList)
gen_pp1_DoubleQuotedString_StringExpression = Generalization(general=StringExpression, specific=pp1_DoubleQuotedString)
gen_pp1_DoubleQuotedString_IQuotedString = Generalization(general=IQuotedString, specific=pp1_DoubleQuotedString)
gen_pp1_VariableTE_TextExpression = Generalization(general=TextExpression, specific=pp1_VariableTE)
gen_pp1_SingleQuotedString_StringExpression = Generalization(general=StringExpression, specific=pp1_SingleQuotedString)
gen_pp1_SingleQuotedString_IQuotedString = Generalization(general=IQuotedString, specific=pp1_SingleQuotedString)
gen_pp1_StringExpression_Expression = Generalization(general=Expression, specific=pp1_StringExpression)
gen_pp1_UnquotedString_StringExpression = Generalization(general=StringExpression, specific=pp1_UnquotedString)
gen_pp1_InterpolatedVariable_Expression = Generalization(general=Expression, specific=pp1_InterpolatedVariable)
gen_pp1_VerbatimTE_TextExpression = Generalization(general=TextExpression, specific=pp1_VerbatimTE)
gen_pp1_ExpressionTE_TextExpression = Generalization(general=TextExpression, specific=pp1_ExpressionTE)
gen_pp1_WithLambdaExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp1_WithLambdaExpression)
gen_pp1_LiteralClass_LiteralExpression = Generalization(general=LiteralExpression, specific=pp1_LiteralClass)
gen_pp1_UnlessExpression_Expression = Generalization(general=Expression, specific=pp1_UnlessExpression)
gen_pp1_Lambda_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp1_Lambda)
gen_pp1_NamedAccessExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp1_NamedAccessExpression)
gen_pp1_MethodCall_WithLambdaExpression = Generalization(general=WithLambdaExpression, specific=pp1_MethodCall)
gen_pp1_JavaLambda_Lambda = Generalization(general=Lambda, specific=pp1_JavaLambda)
gen_pp1_RubyLambda_Lambda = Generalization(general=Lambda, specific=pp1_RubyLambda)
gen_pp1_SeparatorExpression_Expression = Generalization(general=Expression, specific=pp1_SeparatorExpression)

# Domain Model
domain_model = DomainModel(
    name="pp1",
    types={pp1_PuppetManifest, ExpressionBlock, pp1_Expression, pp1_ResourceBody, pp1_AttributeOperations, pp1_Case, pp1_AttributeOperation, pp1_ICollectQuery, pp1_VirtualCollectQuery, UnaryExpression, ICollectQuery, pp1_ExportedCollectQuery, pp1_HostClassDefinition, Definition, pp1_LiteralExpression, pp1_Definition, Expression, pp1_DefinitionArgumentList, pp1_DefinitionArgument, pp1_CaseExpression, pp1_IfExpression, pp1_LiteralNameOrReference, LiteralExpression, pp1_ResourceExpression, pp1_ImportExpression, pp1_IQuotedString, pp1_LiteralList, pp1_LiteralHash, pp1_HashEntry, pp1_SelectorEntry, pp1_FunctionCall, WithLambdaExpression, pp1_LiteralBoolean, pp1_LiteralUndef, pp1_LiteralDefault, pp1_LiteralRegex, pp1_LiteralName, pp1_VariableExpression, pp1_RelationshipExpression, BinaryOpExpression, pp1_AssignmentExpression, BinaryExpression, pp1_AppendExpression, pp1_OrExpression, pp1_AndExpression, pp1_RelationalExpression, pp1_EqualityExpression, pp1_ShiftExpression, pp1_AdditiveExpression, pp1_MultiplicativeExpression, pp1_MatchingExpression, pp1_InExpression, pp1_AtExpression, ParameterizedExpression, pp1_CollectExpression, pp1_SelectorExpression, pp1_UnaryNotExpression, pp1_BinaryOpExpression, pp1_BinaryExpression, pp1_ParameterizedExpression, pp1_NodeDefinition, pp1_UnaryExpression, pp1_UnaryMinusExpression, pp1_TextExpression, pp1_ExpressionBlock, pp1_ElseExpression, pp1_ElseIfExpression, IfExpression, pp1_VirtualNameOrReference, pp1_ParenthesisedExpression, pp1_ExprList, pp1_DoubleQuotedString, StringExpression, IQuotedString, pp1_SingleQuotedString, pp1_StringExpression, pp1_UnquotedString, pp1_InterpolatedVariable, pp1_VerbatimTE, TextExpression, pp1_ExpressionTE, pp1_VariableTE, pp1_WithLambdaExpression, pp1_LiteralClass, pp1_UnlessExpression, pp1_Lambda, pp1_NamedAccessExpression, pp1_MethodCall, pp1_JavaLambda, Lambda, pp1_RubyLambda, pp1_SeparatorExpression},
    associations={attributes0, cases20, nameExpr1, value3, attributes5, parent8, arguments9, statements10, arguments13, value15, switchExpr18, value48, statements22, values25, condExpr28, thenStatements30, elseStatement33, resourceExpr36, resourceData38, values41, elements42, elements44, key45, classReference51, query53, attributes55, leftExpr58, rightExpr60, leftExpr63, parameters65, hostNames68, parentName70, statements73, expr76, statements78, expr80, expressions82, stringPart84, expression85, expression87, lambda101, condExpr89, thenStatements91, elseStatement94, arguments97, methodExpr99},
    generalizations={gen_pp1_PuppetManifest_ExpressionBlock, gen_pp1_VirtualCollectQuery_UnaryExpression, gen_pp1_VirtualCollectQuery_ICollectQuery, gen_pp1_ExportedCollectQuery_UnaryExpression, gen_pp1_ExportedCollectQuery_ICollectQuery, gen_pp1_HostClassDefinition_Definition, gen_pp1_Definition_Expression, gen_pp1_CaseExpression_Expression, gen_pp1_IfExpression_Expression, gen_pp1_LiteralExpression_Expression, gen_pp1_LiteralNameOrReference_LiteralExpression, gen_pp1_ResourceExpression_Expression, gen_pp1_ImportExpression_Expression, gen_pp1_LiteralList_LiteralExpression, gen_pp1_LiteralHash_LiteralExpression, gen_pp1_SelectorEntry_BinaryExpression, gen_pp1_FunctionCall_WithLambdaExpression, gen_pp1_LiteralBoolean_LiteralExpression, gen_pp1_LiteralUndef_LiteralExpression, gen_pp1_LiteralDefault_LiteralExpression, gen_pp1_LiteralRegex_LiteralExpression, gen_pp1_LiteralName_LiteralExpression, gen_pp1_VariableExpression_Expression, gen_pp1_RelationshipExpression_BinaryOpExpression, gen_pp1_AssignmentExpression_BinaryExpression, gen_pp1_AppendExpression_BinaryExpression, gen_pp1_OrExpression_BinaryExpression, gen_pp1_AndExpression_BinaryExpression, gen_pp1_RelationalExpression_BinaryOpExpression, gen_pp1_EqualityExpression_BinaryOpExpression, gen_pp1_ShiftExpression_BinaryOpExpression, gen_pp1_AdditiveExpression_BinaryOpExpression, gen_pp1_MultiplicativeExpression_BinaryOpExpression, gen_pp1_MatchingExpression_BinaryOpExpression, gen_pp1_InExpression_BinaryOpExpression, gen_pp1_AtExpression_ParameterizedExpression, gen_pp1_CollectExpression_Expression, gen_pp1_SelectorExpression_ParameterizedExpression, gen_pp1_UnaryNotExpression_UnaryExpression, gen_pp1_BinaryOpExpression_BinaryExpression, gen_pp1_BinaryExpression_Expression, gen_pp1_ParameterizedExpression_Expression, gen_pp1_NodeDefinition_Expression, gen_pp1_UnaryExpression_Expression, gen_pp1_UnaryMinusExpression_UnaryExpression, gen_pp1_ExpressionBlock_Expression, gen_pp1_ElseExpression_ExpressionBlock, gen_pp1_ElseIfExpression_IfExpression, gen_pp1_VirtualNameOrReference_LiteralExpression, gen_pp1_ParenthesisedExpression_Expression, gen_pp1_ExprList_Expression, gen_pp1_DoubleQuotedString_StringExpression, gen_pp1_DoubleQuotedString_IQuotedString, gen_pp1_VariableTE_TextExpression, gen_pp1_SingleQuotedString_StringExpression, gen_pp1_SingleQuotedString_IQuotedString, gen_pp1_StringExpression_Expression, gen_pp1_UnquotedString_StringExpression, gen_pp1_InterpolatedVariable_Expression, gen_pp1_VerbatimTE_TextExpression, gen_pp1_ExpressionTE_TextExpression, gen_pp1_WithLambdaExpression_ParameterizedExpression, gen_pp1_LiteralClass_LiteralExpression, gen_pp1_UnlessExpression_Expression, gen_pp1_Lambda_ExpressionBlock, gen_pp1_NamedAccessExpression_BinaryExpression, gen_pp1_MethodCall_WithLambdaExpression, gen_pp1_JavaLambda_Lambda, gen_pp1_RubyLambda_Lambda, gen_pp1_SeparatorExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)