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
pp2_PuppetManifest = Class(name="pp2::PuppetManifest")
ExpressionBlock = Class(name="ExpressionBlock")
pp2_Expression = Class(name="pp2::Expression")
pp2_ResourceBody = Class(name="pp2::ResourceBody")
pp2_AttributeOperations = Class(name="pp2::AttributeOperations")
pp2_AttributeOperation = Class(name="pp2::AttributeOperation")
ICollectQuery = Class(name="ICollectQuery")
pp2_ExportedCollectQuery = Class(name="pp2::ExportedCollectQuery")
pp2_HostClassDefinition = Class(name="pp2::HostClassDefinition")
Definition = Class(name="Definition")
pp2_LiteralExpression = Class(name="pp2::LiteralExpression", is_abstract=True)
pp2_Definition = Class(name="pp2::Definition")
pp2_ICollectQuery = Class(name="pp2::ICollectQuery", is_abstract=True)
pp2_VirtualCollectQuery = Class(name="pp2::VirtualCollectQuery")
UnaryExpression = Class(name="UnaryExpression")
pp2_CaseExpression = Class(name="pp2::CaseExpression")
Expression = Class(name="Expression")
pp2_Case = Class(name="pp2::Case")
pp2_DefinitionArgumentList = Class(name="pp2::DefinitionArgumentList")
pp2_DefinitionArgument = Class(name="pp2::DefinitionArgument")
pp2_LiteralNameOrReference = Class(name="pp2::LiteralNameOrReference")
LiteralExpression = Class(name="LiteralExpression")
pp2_ResourceExpression = Class(name="pp2::ResourceExpression")
pp2_ImportExpression = Class(name="pp2::ImportExpression")
pp2_IfExpression = Class(name="pp2::IfExpression")
pp2_HashEntry = Class(name="pp2::HashEntry")
pp2_LiteralBoolean = Class(name="pp2::LiteralBoolean")
pp2_LiteralUndef = Class(name="pp2::LiteralUndef")
pp2_IQuotedString = Class(name="pp2::IQuotedString", is_abstract=True)
pp2_LiteralList = Class(name="pp2::LiteralList")
pp2_LiteralHash = Class(name="pp2::LiteralHash")
pp2_RelationshipExpression = Class(name="pp2::RelationshipExpression")
BinaryOpExpression = Class(name="BinaryOpExpression")
pp2_AssignmentExpression = Class(name="pp2::AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
pp2_AppendExpression = Class(name="pp2::AppendExpression")
pp2_OrExpression = Class(name="pp2::OrExpression")
pp2_AndExpression = Class(name="pp2::AndExpression")
pp2_RelationalExpression = Class(name="pp2::RelationalExpression")
pp2_EqualityExpression = Class(name="pp2::EqualityExpression")
pp2_ShiftExpression = Class(name="pp2::ShiftExpression")
pp2_LiteralDefault = Class(name="pp2::LiteralDefault")
pp2_LiteralRegex = Class(name="pp2::LiteralRegex")
pp2_LiteralName = Class(name="pp2::LiteralName")
pp2_VariableExpression = Class(name="pp2::VariableExpression")
pp2_SelectorExpression = Class(name="pp2::SelectorExpression")
pp2_SelectorEntry = Class(name="pp2::SelectorEntry")
pp2_FunctionCall = Class(name="pp2::FunctionCall")
WithLambdaExpression = Class(name="WithLambdaExpression")
pp2_AdditiveExpression = Class(name="pp2::AdditiveExpression")
pp2_MultiplicativeExpression = Class(name="pp2::MultiplicativeExpression")
pp2_MatchingExpression = Class(name="pp2::MatchingExpression")
pp2_InExpression = Class(name="pp2::InExpression")
pp2_AtExpression = Class(name="pp2::AtExpression")
ParameterizedExpression = Class(name="ParameterizedExpression")
pp2_CollectExpression = Class(name="pp2::CollectExpression")
pp2_ParameterizedExpression = Class(name="pp2::ParameterizedExpression", is_abstract=True)
pp2_NodeDefinition = Class(name="pp2::NodeDefinition")
pp2_BinaryOpExpression = Class(name="pp2::BinaryOpExpression", is_abstract=True)
pp2_BinaryExpression = Class(name="pp2::BinaryExpression", is_abstract=True)
pp2_ExpressionBlock = Class(name="pp2::ExpressionBlock", is_abstract=True)
pp2_ElseExpression = Class(name="pp2::ElseExpression")
pp2_ElseIfExpression = Class(name="pp2::ElseIfExpression")
IfExpression = Class(name="IfExpression")
pp2_VirtualNameOrReference = Class(name="pp2::VirtualNameOrReference")
pp2_ParenthesisedExpression = Class(name="pp2::ParenthesisedExpression")
pp2_UnaryExpression = Class(name="pp2::UnaryExpression", is_abstract=True)
pp2_UnaryMinusExpression = Class(name="pp2::UnaryMinusExpression")
pp2_UnaryNotExpression = Class(name="pp2::UnaryNotExpression")
pp2_TextExpression = Class(name="pp2::TextExpression", is_abstract=True)
pp2_SingleQuotedString = Class(name="pp2::SingleQuotedString")
pp2_StringExpression = Class(name="pp2::StringExpression", is_abstract=True)
pp2_UnquotedString = Class(name="pp2::UnquotedString")
pp2_ExprList = Class(name="pp2::ExprList")
pp2_DoubleQuotedString = Class(name="pp2::DoubleQuotedString")
StringExpression = Class(name="StringExpression")
IQuotedString = Class(name="IQuotedString")
pp2_VariableTE = Class(name="pp2::VariableTE")
pp2_LiteralClass = Class(name="pp2::LiteralClass")
pp2_UnlessExpression = Class(name="pp2::UnlessExpression")
pp2_InterpolatedVariable = Class(name="pp2::InterpolatedVariable")
pp2_VerbatimTE = Class(name="pp2::VerbatimTE")
TextExpression = Class(name="TextExpression")
pp2_ExpressionTE = Class(name="pp2::ExpressionTE")
pp2_MethodCall = Class(name="pp2::MethodCall")
pp2_WithLambdaExpression = Class(name="pp2::WithLambdaExpression")
pp2_Lambda = Class(name="pp2::Lambda", is_abstract=True)
pp2_NamedAccessExpression = Class(name="pp2::NamedAccessExpression")
pp2_JavaLambda = Class(name="pp2::JavaLambda")
Lambda = Class(name="Lambda")
pp2_RubyLambda = Class(name="pp2::RubyLambda")
pp2_SeparatorExpression = Class(name="pp2::SeparatorExpression")

# pp2_PuppetManifest class attributes and methods

# ExpressionBlock class attributes and methods

# pp2_Expression class attributes and methods

# pp2_ResourceBody class attributes and methods

# pp2_AttributeOperations class attributes and methods

# pp2_AttributeOperation class attributes and methods
pp2_AttributeOperation_key: Property = Property(name="key", type=StringType)
pp2_AttributeOperation_op: Property = Property(name="op", type=StringType)
pp2_AttributeOperation.attributes={pp2_AttributeOperation_key, pp2_AttributeOperation_op}

# ICollectQuery class attributes and methods

# pp2_ExportedCollectQuery class attributes and methods

# pp2_HostClassDefinition class attributes and methods

# Definition class attributes and methods

# pp2_LiteralExpression class attributes and methods

# pp2_Definition class attributes and methods
pp2_Definition_className: Property = Property(name="className", type=StringType)
pp2_Definition.attributes={pp2_Definition_className}

# pp2_ICollectQuery class attributes and methods

# pp2_VirtualCollectQuery class attributes and methods

# UnaryExpression class attributes and methods

# pp2_CaseExpression class attributes and methods

# Expression class attributes and methods

# pp2_Case class attributes and methods

# pp2_DefinitionArgumentList class attributes and methods

# pp2_DefinitionArgument class attributes and methods
pp2_DefinitionArgument_argName: Property = Property(name="argName", type=StringType)
pp2_DefinitionArgument_op: Property = Property(name="op", type=StringType)
pp2_DefinitionArgument.attributes={pp2_DefinitionArgument_op, pp2_DefinitionArgument_argName}

# pp2_LiteralNameOrReference class attributes and methods
pp2_LiteralNameOrReference_value: Property = Property(name="value", type=StringType)
pp2_LiteralNameOrReference.attributes={pp2_LiteralNameOrReference_value}

# LiteralExpression class attributes and methods

# pp2_ResourceExpression class attributes and methods

# pp2_ImportExpression class attributes and methods

# pp2_IfExpression class attributes and methods

# pp2_HashEntry class attributes and methods

# pp2_LiteralBoolean class attributes and methods
pp2_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
pp2_LiteralBoolean.attributes={pp2_LiteralBoolean_value}

# pp2_LiteralUndef class attributes and methods

# pp2_IQuotedString class attributes and methods

# pp2_LiteralList class attributes and methods

# pp2_LiteralHash class attributes and methods

# pp2_RelationshipExpression class attributes and methods

# BinaryOpExpression class attributes and methods

# pp2_AssignmentExpression class attributes and methods

# BinaryExpression class attributes and methods

# pp2_AppendExpression class attributes and methods

# pp2_OrExpression class attributes and methods

# pp2_AndExpression class attributes and methods

# pp2_RelationalExpression class attributes and methods

# pp2_EqualityExpression class attributes and methods

# pp2_ShiftExpression class attributes and methods

# pp2_LiteralDefault class attributes and methods

# pp2_LiteralRegex class attributes and methods
pp2_LiteralRegex_value: Property = Property(name="value", type=StringType)
pp2_LiteralRegex.attributes={pp2_LiteralRegex_value}

# pp2_LiteralName class attributes and methods
pp2_LiteralName_value: Property = Property(name="value", type=StringType)
pp2_LiteralName.attributes={pp2_LiteralName_value}

# pp2_VariableExpression class attributes and methods
pp2_VariableExpression_varName: Property = Property(name="varName", type=StringType)
pp2_VariableExpression.attributes={pp2_VariableExpression_varName}

# pp2_SelectorExpression class attributes and methods

# pp2_SelectorEntry class attributes and methods

# pp2_FunctionCall class attributes and methods

# WithLambdaExpression class attributes and methods

# pp2_AdditiveExpression class attributes and methods

# pp2_MultiplicativeExpression class attributes and methods

# pp2_MatchingExpression class attributes and methods

# pp2_InExpression class attributes and methods

# pp2_AtExpression class attributes and methods

# ParameterizedExpression class attributes and methods

# pp2_CollectExpression class attributes and methods

# pp2_ParameterizedExpression class attributes and methods

# pp2_NodeDefinition class attributes and methods

# pp2_BinaryOpExpression class attributes and methods
pp2_BinaryOpExpression_opName: Property = Property(name="opName", type=StringType)
pp2_BinaryOpExpression.attributes={pp2_BinaryOpExpression_opName}

# pp2_BinaryExpression class attributes and methods

# pp2_ExpressionBlock class attributes and methods

# pp2_ElseExpression class attributes and methods

# pp2_ElseIfExpression class attributes and methods

# IfExpression class attributes and methods

# pp2_VirtualNameOrReference class attributes and methods
pp2_VirtualNameOrReference_value: Property = Property(name="value", type=StringType)
pp2_VirtualNameOrReference_exported: Property = Property(name="exported", type=BooleanType)
pp2_VirtualNameOrReference.attributes={pp2_VirtualNameOrReference_exported, pp2_VirtualNameOrReference_value}

# pp2_ParenthesisedExpression class attributes and methods

# pp2_UnaryExpression class attributes and methods

# pp2_UnaryMinusExpression class attributes and methods

# pp2_UnaryNotExpression class attributes and methods

# pp2_TextExpression class attributes and methods

# pp2_SingleQuotedString class attributes and methods
pp2_SingleQuotedString_text: Property = Property(name="text", type=StringType)
pp2_SingleQuotedString.attributes={pp2_SingleQuotedString_text}

# pp2_StringExpression class attributes and methods

# pp2_UnquotedString class attributes and methods

# pp2_ExprList class attributes and methods

# pp2_DoubleQuotedString class attributes and methods

# StringExpression class attributes and methods

# IQuotedString class attributes and methods

# pp2_VariableTE class attributes and methods
pp2_VariableTE_varName: Property = Property(name="varName", type=StringType)
pp2_VariableTE.attributes={pp2_VariableTE_varName}

# pp2_LiteralClass class attributes and methods

# pp2_UnlessExpression class attributes and methods

# pp2_InterpolatedVariable class attributes and methods
pp2_InterpolatedVariable_varName: Property = Property(name="varName", type=StringType)
pp2_InterpolatedVariable.attributes={pp2_InterpolatedVariable_varName}

# pp2_VerbatimTE class attributes and methods
pp2_VerbatimTE_text: Property = Property(name="text", type=StringType)
pp2_VerbatimTE.attributes={pp2_VerbatimTE_text}

# TextExpression class attributes and methods

# pp2_ExpressionTE class attributes and methods

# pp2_MethodCall class attributes and methods
pp2_MethodCall_parenthesized: Property = Property(name="parenthesized", type=BooleanType)
pp2_MethodCall.attributes={pp2_MethodCall_parenthesized}

# pp2_WithLambdaExpression class attributes and methods

# pp2_Lambda class attributes and methods

# pp2_NamedAccessExpression class attributes and methods

# pp2_JavaLambda class attributes and methods
pp2_JavaLambda_farrow: Property = Property(name="farrow", type=BooleanType)
pp2_JavaLambda.attributes={pp2_JavaLambda_farrow}

# Lambda class attributes and methods

# pp2_RubyLambda class attributes and methods

# pp2_SeparatorExpression class attributes and methods

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="pp2_AttributeOperations", type=pp2_ResourceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ResourceBody", type=pp2_AttributeOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameExpr1: BinaryAssociation = BinaryAssociation(
    name="nameExpr1",
    ends={
        Property(name="pp2_Expression", type=pp2_ResourceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ResourceBody2", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="pp2_LiteralExpression", type=pp2_HostClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_HostClassDefinition", type=pp2_LiteralExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="pp2_Expression4", type=pp2_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_AttributeOperation", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="pp2_AttributeOperation7", type=pp2_AttributeOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_AttributeOperations6", type=pp2_AttributeOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="pp2_Expression17", type=pp2_DefinitionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_DefinitionArgument16", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpr18: BinaryAssociation = BinaryAssociation(
    name="switchExpr18",
    ends={
        Property(name="pp2_Expression19", type=pp2_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_CaseExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases20: BinaryAssociation = BinaryAssociation(
    name="cases20",
    ends={
        Property(name="pp2_Case", type=pp2_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_CaseExpression21", type=pp2_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments9: BinaryAssociation = BinaryAssociation(
    name="arguments9",
    ends={
        Property(name="pp2_DefinitionArgumentList", type=pp2_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_Definition", type=pp2_DefinitionArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="pp2_DefinitionArgument", type=pp2_DefinitionArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_DefinitionArgumentList11", type=pp2_DefinitionArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
puppetType12: BinaryAssociation = BinaryAssociation(
    name="puppetType12",
    ends={
        Property(name="pp2_Expression14", type=pp2_DefinitionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_DefinitionArgument13", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceExpr30: BinaryAssociation = BinaryAssociation(
    name="resourceExpr30",
    ends={
        Property(name="pp2_Expression31", type=pp2_ResourceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ResourceExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceData32: BinaryAssociation = BinaryAssociation(
    name="resourceData32",
    ends={
        Property(name="pp2_ResourceBody34", type=pp2_ResourceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ResourceExpression33", type=pp2_ResourceBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values22: BinaryAssociation = BinaryAssociation(
    name="values22",
    ends={
        Property(name="pp2_Expression24", type=pp2_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_Case23", type=pp2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condExpr25: BinaryAssociation = BinaryAssociation(
    name="condExpr25",
    ends={
        Property(name="pp2_Expression26", type=pp2_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_IfExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement27: BinaryAssociation = BinaryAssociation(
    name="elseStatement27",
    ends={
        Property(name="pp2_Expression29", type=pp2_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_IfExpression28", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements38: BinaryAssociation = BinaryAssociation(
    name="elements38",
    ends={
        Property(name="pp2_HashEntry", type=pp2_LiteralHash, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_LiteralHash", type=pp2_HashEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key39: BinaryAssociation = BinaryAssociation(
    name="key39",
    ends={
        Property(name="pp2_Expression41", type=pp2_HashEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_HashEntry40", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value42: BinaryAssociation = BinaryAssociation(
    name="value42",
    ends={
        Property(name="pp2_Expression44", type=pp2_HashEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_HashEntry43", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values35: BinaryAssociation = BinaryAssociation(
    name="values35",
    ends={
        Property(name="pp2_IQuotedString", type=pp2_ImportExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ImportExpression", type=pp2_IQuotedString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements36: BinaryAssociation = BinaryAssociation(
    name="elements36",
    ends={
        Property(name="pp2_Expression37", type=pp2_LiteralList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_LiteralList", type=pp2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classReference45: BinaryAssociation = BinaryAssociation(
    name="classReference45",
    ends={
        Property(name="pp2_Expression46", type=pp2_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_CollectExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query47: BinaryAssociation = BinaryAssociation(
    name="query47",
    ends={
        Property(name="pp2_ICollectQuery", type=pp2_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_CollectExpression48", type=pp2_ICollectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes49: BinaryAssociation = BinaryAssociation(
    name="attributes49",
    ends={
        Property(name="pp2_AttributeOperations51", type=pp2_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_CollectExpression50", type=pp2_AttributeOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExpr57: BinaryAssociation = BinaryAssociation(
    name="leftExpr57",
    ends={
        Property(name="pp2_Expression58", type=pp2_ParameterizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ParameterizedExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters59: BinaryAssociation = BinaryAssociation(
    name="parameters59",
    ends={
        Property(name="pp2_Expression61", type=pp2_ParameterizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ParameterizedExpression60", type=pp2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostNames62: BinaryAssociation = BinaryAssociation(
    name="hostNames62",
    ends={
        Property(name="pp2_Expression63", type=pp2_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_NodeDefinition", type=pp2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftExpr52: BinaryAssociation = BinaryAssociation(
    name="leftExpr52",
    ends={
        Property(name="pp2_Expression53", type=pp2_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_BinaryExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExpr54: BinaryAssociation = BinaryAssociation(
    name="rightExpr54",
    ends={
        Property(name="pp2_Expression56", type=pp2_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_BinaryExpression55", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements69: BinaryAssociation = BinaryAssociation(
    name="statements69",
    ends={
        Property(name="pp2_Expression70", type=pp2_ExpressionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ExpressionBlock", type=pp2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentName64: BinaryAssociation = BinaryAssociation(
    name="parentName64",
    ends={
        Property(name="pp2_Expression66", type=pp2_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_NodeDefinition65", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr67: BinaryAssociation = BinaryAssociation(
    name="expr67",
    ends={
        Property(name="pp2_Expression68", type=pp2_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_UnaryExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stringPart75: BinaryAssociation = BinaryAssociation(
    name="stringPart75",
    ends={
        Property(name="pp2_TextExpression", type=pp2_DoubleQuotedString, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_DoubleQuotedString", type=pp2_TextExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression76: BinaryAssociation = BinaryAssociation(
    name="expression76",
    ends={
        Property(name="pp2_Expression77", type=pp2_UnquotedString, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_UnquotedString", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr71: BinaryAssociation = BinaryAssociation(
    name="expr71",
    ends={
        Property(name="pp2_Expression72", type=pp2_ParenthesisedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ParenthesisedExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions73: BinaryAssociation = BinaryAssociation(
    name="expressions73",
    ends={
        Property(name="pp2_Expression74", type=pp2_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ExprList", type=pp2_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression78: BinaryAssociation = BinaryAssociation(
    name="expression78",
    ends={
        Property(name="pp2_Expression79", type=pp2_ExpressionTE, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_ExpressionTE", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr80: BinaryAssociation = BinaryAssociation(
    name="condExpr80",
    ends={
        Property(name="pp2_Expression81", type=pp2_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_UnlessExpression", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodExpr87: BinaryAssociation = BinaryAssociation(
    name="methodExpr87",
    ends={
        Property(name="pp2_Expression88", type=pp2_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_MethodCall", type=pp2_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement82: BinaryAssociation = BinaryAssociation(
    name="elseStatement82",
    ends={
        Property(name="pp2_Expression84", type=pp2_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_UnlessExpression83", type=pp2_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments85: BinaryAssociation = BinaryAssociation(
    name="arguments85",
    ends={
        Property(name="pp2_DefinitionArgumentList86", type=pp2_Lambda, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_Lambda", type=pp2_DefinitionArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lambda89: BinaryAssociation = BinaryAssociation(
    name="lambda89",
    ends={
        Property(name="pp2_Lambda90", type=pp2_WithLambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp2_WithLambdaExpression", type=pp2_Lambda, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pp2_PuppetManifest_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_PuppetManifest)
gen_pp2_VirtualCollectQuery_UnaryExpression = Generalization(general=UnaryExpression, specific=pp2_VirtualCollectQuery)
gen_pp2_VirtualCollectQuery_ICollectQuery = Generalization(general=ICollectQuery, specific=pp2_VirtualCollectQuery)
gen_pp2_ExportedCollectQuery_UnaryExpression = Generalization(general=UnaryExpression, specific=pp2_ExportedCollectQuery)
gen_pp2_ExportedCollectQuery_ICollectQuery = Generalization(general=ICollectQuery, specific=pp2_ExportedCollectQuery)
gen_pp2_HostClassDefinition_Definition = Generalization(general=Definition, specific=pp2_HostClassDefinition)
gen_pp2_Definition_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_Definition)
gen_pp2_CaseExpression_Expression = Generalization(general=Expression, specific=pp2_CaseExpression)
gen_pp2_Case_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_Case)
gen_pp2_LiteralExpression_Expression = Generalization(general=Expression, specific=pp2_LiteralExpression)
gen_pp2_LiteralNameOrReference_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralNameOrReference)
gen_pp2_ResourceExpression_Expression = Generalization(general=Expression, specific=pp2_ResourceExpression)
gen_pp2_IfExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_IfExpression)
gen_pp2_LiteralBoolean_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralBoolean)
gen_pp2_LiteralUndef_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralUndef)
gen_pp2_ImportExpression_Expression = Generalization(general=Expression, specific=pp2_ImportExpression)
gen_pp2_LiteralList_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralList)
gen_pp2_LiteralHash_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralHash)
gen_pp2_RelationshipExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_RelationshipExpression)
gen_pp2_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_AssignmentExpression)
gen_pp2_AppendExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_AppendExpression)
gen_pp2_OrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_OrExpression)
gen_pp2_AndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_AndExpression)
gen_pp2_RelationalExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_RelationalExpression)
gen_pp2_EqualityExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_EqualityExpression)
gen_pp2_LiteralDefault_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralDefault)
gen_pp2_LiteralRegex_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralRegex)
gen_pp2_LiteralName_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralName)
gen_pp2_VariableExpression_Expression = Generalization(general=Expression, specific=pp2_VariableExpression)
gen_pp2_SelectorExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp2_SelectorExpression)
gen_pp2_SelectorEntry_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_SelectorEntry)
gen_pp2_ShiftExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_ShiftExpression)
gen_pp2_AdditiveExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_AdditiveExpression)
gen_pp2_MultiplicativeExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_MultiplicativeExpression)
gen_pp2_MatchingExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_MatchingExpression)
gen_pp2_InExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp2_InExpression)
gen_pp2_AtExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp2_AtExpression)
gen_pp2_CollectExpression_Expression = Generalization(general=Expression, specific=pp2_CollectExpression)
gen_pp2_ParameterizedExpression_Expression = Generalization(general=Expression, specific=pp2_ParameterizedExpression)
gen_pp2_NodeDefinition_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_NodeDefinition)
gen_pp2_FunctionCall_WithLambdaExpression = Generalization(general=WithLambdaExpression, specific=pp2_FunctionCall)
gen_pp2_BinaryOpExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_BinaryOpExpression)
gen_pp2_BinaryExpression_Expression = Generalization(general=Expression, specific=pp2_BinaryExpression)
gen_pp2_ExpressionBlock_Expression = Generalization(general=Expression, specific=pp2_ExpressionBlock)
gen_pp2_ElseExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_ElseExpression)
gen_pp2_ElseIfExpression_IfExpression = Generalization(general=IfExpression, specific=pp2_ElseIfExpression)
gen_pp2_VirtualNameOrReference_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_VirtualNameOrReference)
gen_pp2_UnaryExpression_Expression = Generalization(general=Expression, specific=pp2_UnaryExpression)
gen_pp2_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=pp2_UnaryMinusExpression)
gen_pp2_UnaryNotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=pp2_UnaryNotExpression)
gen_pp2_DoubleQuotedString_IQuotedString = Generalization(general=IQuotedString, specific=pp2_DoubleQuotedString)
gen_pp2_SingleQuotedString_StringExpression = Generalization(general=StringExpression, specific=pp2_SingleQuotedString)
gen_pp2_SingleQuotedString_IQuotedString = Generalization(general=IQuotedString, specific=pp2_SingleQuotedString)
gen_pp2_StringExpression_Expression = Generalization(general=Expression, specific=pp2_StringExpression)
gen_pp2_UnquotedString_StringExpression = Generalization(general=StringExpression, specific=pp2_UnquotedString)
gen_pp2_ParenthesisedExpression_Expression = Generalization(general=Expression, specific=pp2_ParenthesisedExpression)
gen_pp2_ExprList_Expression = Generalization(general=Expression, specific=pp2_ExprList)
gen_pp2_DoubleQuotedString_StringExpression = Generalization(general=StringExpression, specific=pp2_DoubleQuotedString)
gen_pp2_ExpressionTE_TextExpression = Generalization(general=TextExpression, specific=pp2_ExpressionTE)
gen_pp2_VariableTE_TextExpression = Generalization(general=TextExpression, specific=pp2_VariableTE)
gen_pp2_LiteralClass_LiteralExpression = Generalization(general=LiteralExpression, specific=pp2_LiteralClass)
gen_pp2_UnlessExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_UnlessExpression)
gen_pp2_InterpolatedVariable_Expression = Generalization(general=Expression, specific=pp2_InterpolatedVariable)
gen_pp2_VerbatimTE_TextExpression = Generalization(general=TextExpression, specific=pp2_VerbatimTE)
gen_pp2_MethodCall_WithLambdaExpression = Generalization(general=WithLambdaExpression, specific=pp2_MethodCall)
gen_pp2_WithLambdaExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp2_WithLambdaExpression)
gen_pp2_Lambda_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp2_Lambda)
gen_pp2_NamedAccessExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp2_NamedAccessExpression)
gen_pp2_JavaLambda_Lambda = Generalization(general=Lambda, specific=pp2_JavaLambda)
gen_pp2_RubyLambda_Lambda = Generalization(general=Lambda, specific=pp2_RubyLambda)
gen_pp2_SeparatorExpression_Expression = Generalization(general=Expression, specific=pp2_SeparatorExpression)

# Domain Model
domain_model = DomainModel(
    name="pp2",
    types={pp2_PuppetManifest, ExpressionBlock, pp2_Expression, pp2_ResourceBody, pp2_AttributeOperations, pp2_AttributeOperation, ICollectQuery, pp2_ExportedCollectQuery, pp2_HostClassDefinition, Definition, pp2_LiteralExpression, pp2_Definition, pp2_ICollectQuery, pp2_VirtualCollectQuery, UnaryExpression, pp2_CaseExpression, Expression, pp2_Case, pp2_DefinitionArgumentList, pp2_DefinitionArgument, pp2_LiteralNameOrReference, LiteralExpression, pp2_ResourceExpression, pp2_ImportExpression, pp2_IfExpression, pp2_HashEntry, pp2_LiteralBoolean, pp2_LiteralUndef, pp2_IQuotedString, pp2_LiteralList, pp2_LiteralHash, pp2_RelationshipExpression, BinaryOpExpression, pp2_AssignmentExpression, BinaryExpression, pp2_AppendExpression, pp2_OrExpression, pp2_AndExpression, pp2_RelationalExpression, pp2_EqualityExpression, pp2_ShiftExpression, pp2_LiteralDefault, pp2_LiteralRegex, pp2_LiteralName, pp2_VariableExpression, pp2_SelectorExpression, pp2_SelectorEntry, pp2_FunctionCall, WithLambdaExpression, pp2_AdditiveExpression, pp2_MultiplicativeExpression, pp2_MatchingExpression, pp2_InExpression, pp2_AtExpression, ParameterizedExpression, pp2_CollectExpression, pp2_ParameterizedExpression, pp2_NodeDefinition, pp2_BinaryOpExpression, pp2_BinaryExpression, pp2_ExpressionBlock, pp2_ElseExpression, pp2_ElseIfExpression, IfExpression, pp2_VirtualNameOrReference, pp2_ParenthesisedExpression, pp2_UnaryExpression, pp2_UnaryMinusExpression, pp2_UnaryNotExpression, pp2_TextExpression, pp2_SingleQuotedString, pp2_StringExpression, pp2_UnquotedString, pp2_ExprList, pp2_DoubleQuotedString, StringExpression, IQuotedString, pp2_VariableTE, pp2_LiteralClass, pp2_UnlessExpression, pp2_InterpolatedVariable, pp2_VerbatimTE, TextExpression, pp2_ExpressionTE, pp2_MethodCall, pp2_WithLambdaExpression, pp2_Lambda, pp2_NamedAccessExpression, pp2_JavaLambda, Lambda, pp2_RubyLambda, pp2_SeparatorExpression},
    associations={attributes0, nameExpr1, parent8, value3, attributes5, value15, switchExpr18, cases20, arguments9, arguments10, puppetType12, resourceExpr30, resourceData32, values22, condExpr25, elseStatement27, elements38, key39, value42, values35, elements36, classReference45, query47, attributes49, leftExpr57, parameters59, hostNames62, leftExpr52, rightExpr54, statements69, parentName64, expr67, stringPart75, expression76, expr71, expressions73, expression78, condExpr80, methodExpr87, elseStatement82, arguments85, lambda89},
    generalizations={gen_pp2_PuppetManifest_ExpressionBlock, gen_pp2_VirtualCollectQuery_UnaryExpression, gen_pp2_VirtualCollectQuery_ICollectQuery, gen_pp2_ExportedCollectQuery_UnaryExpression, gen_pp2_ExportedCollectQuery_ICollectQuery, gen_pp2_HostClassDefinition_Definition, gen_pp2_Definition_ExpressionBlock, gen_pp2_CaseExpression_Expression, gen_pp2_Case_ExpressionBlock, gen_pp2_LiteralExpression_Expression, gen_pp2_LiteralNameOrReference_LiteralExpression, gen_pp2_ResourceExpression_Expression, gen_pp2_IfExpression_ExpressionBlock, gen_pp2_LiteralBoolean_LiteralExpression, gen_pp2_LiteralUndef_LiteralExpression, gen_pp2_ImportExpression_Expression, gen_pp2_LiteralList_LiteralExpression, gen_pp2_LiteralHash_LiteralExpression, gen_pp2_RelationshipExpression_BinaryOpExpression, gen_pp2_AssignmentExpression_BinaryExpression, gen_pp2_AppendExpression_BinaryExpression, gen_pp2_OrExpression_BinaryExpression, gen_pp2_AndExpression_BinaryExpression, gen_pp2_RelationalExpression_BinaryOpExpression, gen_pp2_EqualityExpression_BinaryOpExpression, gen_pp2_LiteralDefault_LiteralExpression, gen_pp2_LiteralRegex_LiteralExpression, gen_pp2_LiteralName_LiteralExpression, gen_pp2_VariableExpression_Expression, gen_pp2_SelectorExpression_ParameterizedExpression, gen_pp2_SelectorEntry_BinaryExpression, gen_pp2_ShiftExpression_BinaryOpExpression, gen_pp2_AdditiveExpression_BinaryOpExpression, gen_pp2_MultiplicativeExpression_BinaryOpExpression, gen_pp2_MatchingExpression_BinaryOpExpression, gen_pp2_InExpression_BinaryOpExpression, gen_pp2_AtExpression_ParameterizedExpression, gen_pp2_CollectExpression_Expression, gen_pp2_ParameterizedExpression_Expression, gen_pp2_NodeDefinition_ExpressionBlock, gen_pp2_FunctionCall_WithLambdaExpression, gen_pp2_BinaryOpExpression_BinaryExpression, gen_pp2_BinaryExpression_Expression, gen_pp2_ExpressionBlock_Expression, gen_pp2_ElseExpression_ExpressionBlock, gen_pp2_ElseIfExpression_IfExpression, gen_pp2_VirtualNameOrReference_LiteralExpression, gen_pp2_UnaryExpression_Expression, gen_pp2_UnaryMinusExpression_UnaryExpression, gen_pp2_UnaryNotExpression_UnaryExpression, gen_pp2_DoubleQuotedString_IQuotedString, gen_pp2_SingleQuotedString_StringExpression, gen_pp2_SingleQuotedString_IQuotedString, gen_pp2_StringExpression_Expression, gen_pp2_UnquotedString_StringExpression, gen_pp2_ParenthesisedExpression_Expression, gen_pp2_ExprList_Expression, gen_pp2_DoubleQuotedString_StringExpression, gen_pp2_ExpressionTE_TextExpression, gen_pp2_VariableTE_TextExpression, gen_pp2_LiteralClass_LiteralExpression, gen_pp2_UnlessExpression_ExpressionBlock, gen_pp2_InterpolatedVariable_Expression, gen_pp2_VerbatimTE_TextExpression, gen_pp2_MethodCall_WithLambdaExpression, gen_pp2_WithLambdaExpression_ParameterizedExpression, gen_pp2_Lambda_ExpressionBlock, gen_pp2_NamedAccessExpression_BinaryExpression, gen_pp2_JavaLambda_Lambda, gen_pp2_RubyLambda_Lambda, gen_pp2_SeparatorExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)