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
pp_ResourceBody = Class(name="pp::ResourceBody")
pp_AttributeOperations = Class(name="pp::AttributeOperations")
pp_AttributeOperation = Class(name="pp::AttributeOperation")
pp_PuppetManifest = Class(name="pp::PuppetManifest")
ExpressionBlock = Class(name="ExpressionBlock")
pp_Expression = Class(name="pp::Expression")
pp_Definition = Class(name="pp::Definition")
pp_DefinitionArgumentList = Class(name="pp::DefinitionArgumentList")
pp_ICollectQuery = Class(name="pp::ICollectQuery", is_abstract=True)
pp_VirtualCollectQuery = Class(name="pp::VirtualCollectQuery")
UnaryExpression = Class(name="UnaryExpression")
ICollectQuery = Class(name="ICollectQuery")
pp_DefinitionArgument = Class(name="pp::DefinitionArgument")
pp_ExportedCollectQuery = Class(name="pp::ExportedCollectQuery")
pp_HostClassDefinition = Class(name="pp::HostClassDefinition")
Definition = Class(name="Definition")
pp_LiteralExpression = Class(name="pp::LiteralExpression", is_abstract=True)
pp_CaseExpression = Class(name="pp::CaseExpression")
Expression = Class(name="Expression")
pp_Case = Class(name="pp::Case")
pp_IfExpression = Class(name="pp::IfExpression")
pp_LiteralNameOrReference = Class(name="pp::LiteralNameOrReference")
LiteralExpression = Class(name="LiteralExpression")
pp_ResourceExpression = Class(name="pp::ResourceExpression")
pp_ImportExpression = Class(name="pp::ImportExpression")
pp_IQuotedString = Class(name="pp::IQuotedString", is_abstract=True)
pp_LiteralList = Class(name="pp::LiteralList")
pp_LiteralHash = Class(name="pp::LiteralHash")
pp_HashEntry = Class(name="pp::HashEntry")
pp_LiteralBoolean = Class(name="pp::LiteralBoolean")
pp_LiteralUndef = Class(name="pp::LiteralUndef")
pp_LiteralDefault = Class(name="pp::LiteralDefault")
pp_RelationalExpression = Class(name="pp::RelationalExpression")
pp_LiteralRegex = Class(name="pp::LiteralRegex")
pp_LiteralName = Class(name="pp::LiteralName")
pp_VariableExpression = Class(name="pp::VariableExpression")
pp_RelationshipExpression = Class(name="pp::RelationshipExpression")
BinaryOpExpression = Class(name="BinaryOpExpression")
pp_AssignmentExpression = Class(name="pp::AssignmentExpression")
BinaryExpression = Class(name="BinaryExpression")
pp_AppendExpression = Class(name="pp::AppendExpression")
pp_OrExpression = Class(name="pp::OrExpression")
pp_AndExpression = Class(name="pp::AndExpression")
pp_EqualityExpression = Class(name="pp::EqualityExpression")
pp_ShiftExpression = Class(name="pp::ShiftExpression")
pp_AdditiveExpression = Class(name="pp::AdditiveExpression")
pp_MultiplicativeExpression = Class(name="pp::MultiplicativeExpression")
pp_MatchingExpression = Class(name="pp::MatchingExpression")
pp_InExpression = Class(name="pp::InExpression")
pp_AtExpression = Class(name="pp::AtExpression")
ParameterizedExpression = Class(name="ParameterizedExpression")
pp_CollectExpression = Class(name="pp::CollectExpression")
pp_SelectorExpression = Class(name="pp::SelectorExpression")
pp_SelectorEntry = Class(name="pp::SelectorEntry")
pp_FunctionCall = Class(name="pp::FunctionCall")
WithLambdaExpression = Class(name="WithLambdaExpression")
pp_BinaryOpExpression = Class(name="pp::BinaryOpExpression", is_abstract=True)
pp_BinaryExpression = Class(name="pp::BinaryExpression", is_abstract=True)
pp_ParameterizedExpression = Class(name="pp::ParameterizedExpression", is_abstract=True)
pp_NodeDefinition = Class(name="pp::NodeDefinition")
pp_ElseExpression = Class(name="pp::ElseExpression")
pp_UnaryExpression = Class(name="pp::UnaryExpression", is_abstract=True)
pp_UnaryMinusExpression = Class(name="pp::UnaryMinusExpression")
pp_UnaryNotExpression = Class(name="pp::UnaryNotExpression")
pp_ExpressionBlock = Class(name="pp::ExpressionBlock", is_abstract=True)
StringExpression = Class(name="StringExpression")
IQuotedString = Class(name="IQuotedString")
pp_ElseIfExpression = Class(name="pp::ElseIfExpression")
IfExpression = Class(name="IfExpression")
pp_VirtualNameOrReference = Class(name="pp::VirtualNameOrReference")
pp_ParenthesisedExpression = Class(name="pp::ParenthesisedExpression")
pp_ExprList = Class(name="pp::ExprList")
pp_DoubleQuotedString = Class(name="pp::DoubleQuotedString")
pp_TextExpression = Class(name="pp::TextExpression", is_abstract=True)
pp_SingleQuotedString = Class(name="pp::SingleQuotedString")
pp_StringExpression = Class(name="pp::StringExpression", is_abstract=True)
pp_UnquotedString = Class(name="pp::UnquotedString")
pp_InterpolatedVariable = Class(name="pp::InterpolatedVariable")
pp_VerbatimTE = Class(name="pp::VerbatimTE")
TextExpression = Class(name="TextExpression")
pp_ExpressionTE = Class(name="pp::ExpressionTE")
pp_VariableTE = Class(name="pp::VariableTE")
pp_LiteralClass = Class(name="pp::LiteralClass")
pp_UnlessExpression = Class(name="pp::UnlessExpression")
pp_Lambda = Class(name="pp::Lambda", is_abstract=True)
pp_NamedAccessExpression = Class(name="pp::NamedAccessExpression")
pp_MethodCall = Class(name="pp::MethodCall")
pp_WithLambdaExpression = Class(name="pp::WithLambdaExpression")
pp_JavaLambda = Class(name="pp::JavaLambda")
Lambda = Class(name="Lambda")
pp_RubyLambda = Class(name="pp::RubyLambda")
pp_SeparatorExpression = Class(name="pp::SeparatorExpression")

# pp_ResourceBody class attributes and methods

# pp_AttributeOperations class attributes and methods

# pp_AttributeOperation class attributes and methods
pp_AttributeOperation_key: Property = Property(name="key", type=StringType)
pp_AttributeOperation_op: Property = Property(name="op", type=StringType)
pp_AttributeOperation.attributes={pp_AttributeOperation_op, pp_AttributeOperation_key}

# pp_PuppetManifest class attributes and methods

# ExpressionBlock class attributes and methods

# pp_Expression class attributes and methods

# pp_Definition class attributes and methods
pp_Definition_className: Property = Property(name="className", type=StringType)
pp_Definition.attributes={pp_Definition_className}

# pp_DefinitionArgumentList class attributes and methods

# pp_ICollectQuery class attributes and methods

# pp_VirtualCollectQuery class attributes and methods

# UnaryExpression class attributes and methods

# ICollectQuery class attributes and methods

# pp_DefinitionArgument class attributes and methods
pp_DefinitionArgument_argName: Property = Property(name="argName", type=StringType)
pp_DefinitionArgument_op: Property = Property(name="op", type=StringType)
pp_DefinitionArgument.attributes={pp_DefinitionArgument_argName, pp_DefinitionArgument_op}

# pp_ExportedCollectQuery class attributes and methods

# pp_HostClassDefinition class attributes and methods

# Definition class attributes and methods

# pp_LiteralExpression class attributes and methods

# pp_CaseExpression class attributes and methods

# Expression class attributes and methods

# pp_Case class attributes and methods

# pp_IfExpression class attributes and methods

# pp_LiteralNameOrReference class attributes and methods
pp_LiteralNameOrReference_value: Property = Property(name="value", type=StringType)
pp_LiteralNameOrReference.attributes={pp_LiteralNameOrReference_value}

# LiteralExpression class attributes and methods

# pp_ResourceExpression class attributes and methods

# pp_ImportExpression class attributes and methods

# pp_IQuotedString class attributes and methods

# pp_LiteralList class attributes and methods

# pp_LiteralHash class attributes and methods

# pp_HashEntry class attributes and methods

# pp_LiteralBoolean class attributes and methods
pp_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
pp_LiteralBoolean.attributes={pp_LiteralBoolean_value}

# pp_LiteralUndef class attributes and methods

# pp_LiteralDefault class attributes and methods

# pp_RelationalExpression class attributes and methods

# pp_LiteralRegex class attributes and methods
pp_LiteralRegex_value: Property = Property(name="value", type=StringType)
pp_LiteralRegex.attributes={pp_LiteralRegex_value}

# pp_LiteralName class attributes and methods
pp_LiteralName_value: Property = Property(name="value", type=StringType)
pp_LiteralName.attributes={pp_LiteralName_value}

# pp_VariableExpression class attributes and methods
pp_VariableExpression_varName: Property = Property(name="varName", type=StringType)
pp_VariableExpression.attributes={pp_VariableExpression_varName}

# pp_RelationshipExpression class attributes and methods

# BinaryOpExpression class attributes and methods

# pp_AssignmentExpression class attributes and methods

# BinaryExpression class attributes and methods

# pp_AppendExpression class attributes and methods

# pp_OrExpression class attributes and methods

# pp_AndExpression class attributes and methods

# pp_EqualityExpression class attributes and methods

# pp_ShiftExpression class attributes and methods

# pp_AdditiveExpression class attributes and methods

# pp_MultiplicativeExpression class attributes and methods

# pp_MatchingExpression class attributes and methods

# pp_InExpression class attributes and methods

# pp_AtExpression class attributes and methods

# ParameterizedExpression class attributes and methods

# pp_CollectExpression class attributes and methods

# pp_SelectorExpression class attributes and methods

# pp_SelectorEntry class attributes and methods

# pp_FunctionCall class attributes and methods

# WithLambdaExpression class attributes and methods

# pp_BinaryOpExpression class attributes and methods
pp_BinaryOpExpression_opName: Property = Property(name="opName", type=StringType)
pp_BinaryOpExpression.attributes={pp_BinaryOpExpression_opName}

# pp_BinaryExpression class attributes and methods

# pp_ParameterizedExpression class attributes and methods

# pp_NodeDefinition class attributes and methods

# pp_ElseExpression class attributes and methods

# pp_UnaryExpression class attributes and methods

# pp_UnaryMinusExpression class attributes and methods

# pp_UnaryNotExpression class attributes and methods

# pp_ExpressionBlock class attributes and methods

# StringExpression class attributes and methods

# IQuotedString class attributes and methods

# pp_ElseIfExpression class attributes and methods

# IfExpression class attributes and methods

# pp_VirtualNameOrReference class attributes and methods
pp_VirtualNameOrReference_value: Property = Property(name="value", type=StringType)
pp_VirtualNameOrReference_exported: Property = Property(name="exported", type=BooleanType)
pp_VirtualNameOrReference.attributes={pp_VirtualNameOrReference_value, pp_VirtualNameOrReference_exported}

# pp_ParenthesisedExpression class attributes and methods

# pp_ExprList class attributes and methods

# pp_DoubleQuotedString class attributes and methods

# pp_TextExpression class attributes and methods

# pp_SingleQuotedString class attributes and methods
pp_SingleQuotedString_text: Property = Property(name="text", type=StringType)
pp_SingleQuotedString.attributes={pp_SingleQuotedString_text}

# pp_StringExpression class attributes and methods

# pp_UnquotedString class attributes and methods

# pp_InterpolatedVariable class attributes and methods
pp_InterpolatedVariable_varName: Property = Property(name="varName", type=StringType)
pp_InterpolatedVariable.attributes={pp_InterpolatedVariable_varName}

# pp_VerbatimTE class attributes and methods
pp_VerbatimTE_text: Property = Property(name="text", type=StringType)
pp_VerbatimTE.attributes={pp_VerbatimTE_text}

# TextExpression class attributes and methods

# pp_ExpressionTE class attributes and methods

# pp_VariableTE class attributes and methods
pp_VariableTE_varName: Property = Property(name="varName", type=StringType)
pp_VariableTE.attributes={pp_VariableTE_varName}

# pp_LiteralClass class attributes and methods

# pp_UnlessExpression class attributes and methods

# pp_Lambda class attributes and methods

# pp_NamedAccessExpression class attributes and methods

# pp_MethodCall class attributes and methods
pp_MethodCall_parenthesized: Property = Property(name="parenthesized", type=BooleanType)
pp_MethodCall.attributes={pp_MethodCall_parenthesized}

# pp_WithLambdaExpression class attributes and methods

# pp_JavaLambda class attributes and methods
pp_JavaLambda_farrow: Property = Property(name="farrow", type=BooleanType)
pp_JavaLambda.attributes={pp_JavaLambda_farrow}

# Lambda class attributes and methods

# pp_RubyLambda class attributes and methods

# pp_SeparatorExpression class attributes and methods

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="pp_AttributeOperations", type=pp_ResourceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ResourceBody", type=pp_AttributeOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameExpr1: BinaryAssociation = BinaryAssociation(
    name="nameExpr1",
    ends={
        Property(name="pp_Expression", type=pp_ResourceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ResourceBody2", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="pp_Expression4", type=pp_AttributeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_AttributeOperation", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="pp_HostClassDefinition", type=pp_LiteralExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pp_LiteralExpression", type=pp_HostClassDefinition, multiplicity=Multiplicity(1, 1))
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="pp_AttributeOperation7", type=pp_AttributeOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_AttributeOperations6", type=pp_AttributeOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments9: BinaryAssociation = BinaryAssociation(
    name="arguments9",
    ends={
        Property(name="pp_DefinitionArgumentList", type=pp_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_Definition", type=pp_DefinitionArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="pp_DefinitionArgument", type=pp_DefinitionArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_DefinitionArgumentList11", type=pp_DefinitionArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
puppetType12: BinaryAssociation = BinaryAssociation(
    name="puppetType12",
    ends={
        Property(name="pp_Expression14", type=pp_DefinitionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_DefinitionArgument13", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="pp_Expression17", type=pp_DefinitionArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_DefinitionArgument16", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchExpr18: BinaryAssociation = BinaryAssociation(
    name="switchExpr18",
    ends={
        Property(name="pp_Expression19", type=pp_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_CaseExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases20: BinaryAssociation = BinaryAssociation(
    name="cases20",
    ends={
        Property(name="pp_Case", type=pp_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_CaseExpression21", type=pp_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values22: BinaryAssociation = BinaryAssociation(
    name="values22",
    ends={
        Property(name="pp_Expression24", type=pp_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_Case23", type=pp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condExpr25: BinaryAssociation = BinaryAssociation(
    name="condExpr25",
    ends={
        Property(name="pp_Expression26", type=pp_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_IfExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement27: BinaryAssociation = BinaryAssociation(
    name="elseStatement27",
    ends={
        Property(name="pp_Expression29", type=pp_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_IfExpression28", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceExpr30: BinaryAssociation = BinaryAssociation(
    name="resourceExpr30",
    ends={
        Property(name="pp_Expression31", type=pp_ResourceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ResourceExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceData32: BinaryAssociation = BinaryAssociation(
    name="resourceData32",
    ends={
        Property(name="pp_ResourceBody34", type=pp_ResourceExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ResourceExpression33", type=pp_ResourceBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values35: BinaryAssociation = BinaryAssociation(
    name="values35",
    ends={
        Property(name="pp_IQuotedString", type=pp_ImportExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ImportExpression", type=pp_IQuotedString, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements36: BinaryAssociation = BinaryAssociation(
    name="elements36",
    ends={
        Property(name="pp_Expression37", type=pp_LiteralList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_LiteralList", type=pp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements38: BinaryAssociation = BinaryAssociation(
    name="elements38",
    ends={
        Property(name="pp_HashEntry", type=pp_LiteralHash, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_LiteralHash", type=pp_HashEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key39: BinaryAssociation = BinaryAssociation(
    name="key39",
    ends={
        Property(name="pp_Expression41", type=pp_HashEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_HashEntry40", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value42: BinaryAssociation = BinaryAssociation(
    name="value42",
    ends={
        Property(name="pp_Expression44", type=pp_HashEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_HashEntry43", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classReference45: BinaryAssociation = BinaryAssociation(
    name="classReference45",
    ends={
        Property(name="pp_Expression46", type=pp_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_CollectExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExpr52: BinaryAssociation = BinaryAssociation(
    name="leftExpr52",
    ends={
        Property(name="pp_Expression53", type=pp_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_BinaryExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
query47: BinaryAssociation = BinaryAssociation(
    name="query47",
    ends={
        Property(name="pp_ICollectQuery", type=pp_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_CollectExpression48", type=pp_ICollectQuery, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes49: BinaryAssociation = BinaryAssociation(
    name="attributes49",
    ends={
        Property(name="pp_AttributeOperations51", type=pp_CollectExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_CollectExpression50", type=pp_AttributeOperations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightExpr54: BinaryAssociation = BinaryAssociation(
    name="rightExpr54",
    ends={
        Property(name="pp_Expression56", type=pp_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_BinaryExpression55", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftExpr57: BinaryAssociation = BinaryAssociation(
    name="leftExpr57",
    ends={
        Property(name="pp_Expression58", type=pp_ParameterizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ParameterizedExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters59: BinaryAssociation = BinaryAssociation(
    name="parameters59",
    ends={
        Property(name="pp_Expression61", type=pp_ParameterizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ParameterizedExpression60", type=pp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hostNames62: BinaryAssociation = BinaryAssociation(
    name="hostNames62",
    ends={
        Property(name="pp_Expression63", type=pp_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_NodeDefinition", type=pp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentName64: BinaryAssociation = BinaryAssociation(
    name="parentName64",
    ends={
        Property(name="pp_Expression66", type=pp_NodeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_NodeDefinition65", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr67: BinaryAssociation = BinaryAssociation(
    name="expr67",
    ends={
        Property(name="pp_Expression68", type=pp_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_UnaryExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements69: BinaryAssociation = BinaryAssociation(
    name="statements69",
    ends={
        Property(name="pp_Expression70", type=pp_ExpressionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ExpressionBlock", type=pp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr71: BinaryAssociation = BinaryAssociation(
    name="expr71",
    ends={
        Property(name="pp_Expression72", type=pp_ParenthesisedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ParenthesisedExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions73: BinaryAssociation = BinaryAssociation(
    name="expressions73",
    ends={
        Property(name="pp_Expression74", type=pp_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ExprList", type=pp_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringPart75: BinaryAssociation = BinaryAssociation(
    name="stringPart75",
    ends={
        Property(name="pp_TextExpression", type=pp_DoubleQuotedString, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_DoubleQuotedString", type=pp_TextExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression76: BinaryAssociation = BinaryAssociation(
    name="expression76",
    ends={
        Property(name="pp_Expression77", type=pp_UnquotedString, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_UnquotedString", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement82: BinaryAssociation = BinaryAssociation(
    name="elseStatement82",
    ends={
        Property(name="pp_Expression84", type=pp_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_UnlessExpression83", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression78: BinaryAssociation = BinaryAssociation(
    name="expression78",
    ends={
        Property(name="pp_Expression79", type=pp_ExpressionTE, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_ExpressionTE", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr80: BinaryAssociation = BinaryAssociation(
    name="condExpr80",
    ends={
        Property(name="pp_Expression81", type=pp_UnlessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_UnlessExpression", type=pp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments85: BinaryAssociation = BinaryAssociation(
    name="arguments85",
    ends={
        Property(name="pp_DefinitionArgumentList86", type=pp_Lambda, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_Lambda", type=pp_DefinitionArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodExpr87: BinaryAssociation = BinaryAssociation(
    name="methodExpr87",
    ends={
        Property(name="pp_Expression88", type=pp_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_MethodCall", type=pp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lambda89: BinaryAssociation = BinaryAssociation(
    name="lambda89",
    ends={
        Property(name="pp_Lambda90", type=pp_WithLambdaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pp_WithLambdaExpression", type=pp_Lambda, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_pp_PuppetManifest_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_PuppetManifest)
gen_pp_Definition_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_Definition)
gen_pp_VirtualCollectQuery_UnaryExpression = Generalization(general=UnaryExpression, specific=pp_VirtualCollectQuery)
gen_pp_VirtualCollectQuery_ICollectQuery = Generalization(general=ICollectQuery, specific=pp_VirtualCollectQuery)
gen_pp_ExportedCollectQuery_UnaryExpression = Generalization(general=UnaryExpression, specific=pp_ExportedCollectQuery)
gen_pp_ExportedCollectQuery_ICollectQuery = Generalization(general=ICollectQuery, specific=pp_ExportedCollectQuery)
gen_pp_HostClassDefinition_Definition = Generalization(general=Definition, specific=pp_HostClassDefinition)
gen_pp_CaseExpression_Expression = Generalization(general=Expression, specific=pp_CaseExpression)
gen_pp_Case_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_Case)
gen_pp_IfExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_IfExpression)
gen_pp_LiteralExpression_Expression = Generalization(general=Expression, specific=pp_LiteralExpression)
gen_pp_LiteralNameOrReference_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralNameOrReference)
gen_pp_ResourceExpression_Expression = Generalization(general=Expression, specific=pp_ResourceExpression)
gen_pp_ImportExpression_Expression = Generalization(general=Expression, specific=pp_ImportExpression)
gen_pp_LiteralList_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralList)
gen_pp_LiteralDefault_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralDefault)
gen_pp_LiteralHash_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralHash)
gen_pp_LiteralBoolean_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralBoolean)
gen_pp_LiteralUndef_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralUndef)
gen_pp_LiteralRegex_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralRegex)
gen_pp_LiteralName_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralName)
gen_pp_VariableExpression_Expression = Generalization(general=Expression, specific=pp_VariableExpression)
gen_pp_RelationshipExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_RelationshipExpression)
gen_pp_AssignmentExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_AssignmentExpression)
gen_pp_AppendExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_AppendExpression)
gen_pp_OrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_OrExpression)
gen_pp_AndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_AndExpression)
gen_pp_RelationalExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_RelationalExpression)
gen_pp_EqualityExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_EqualityExpression)
gen_pp_ShiftExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_ShiftExpression)
gen_pp_AdditiveExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_AdditiveExpression)
gen_pp_MultiplicativeExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_MultiplicativeExpression)
gen_pp_MatchingExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_MatchingExpression)
gen_pp_InExpression_BinaryOpExpression = Generalization(general=BinaryOpExpression, specific=pp_InExpression)
gen_pp_AtExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp_AtExpression)
gen_pp_CollectExpression_Expression = Generalization(general=Expression, specific=pp_CollectExpression)
gen_pp_SelectorExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp_SelectorExpression)
gen_pp_SelectorEntry_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_SelectorEntry)
gen_pp_FunctionCall_WithLambdaExpression = Generalization(general=WithLambdaExpression, specific=pp_FunctionCall)
gen_pp_BinaryOpExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_BinaryOpExpression)
gen_pp_BinaryExpression_Expression = Generalization(general=Expression, specific=pp_BinaryExpression)
gen_pp_ParameterizedExpression_Expression = Generalization(general=Expression, specific=pp_ParameterizedExpression)
gen_pp_NodeDefinition_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_NodeDefinition)
gen_pp_ElseExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_ElseExpression)
gen_pp_UnaryExpression_Expression = Generalization(general=Expression, specific=pp_UnaryExpression)
gen_pp_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=pp_UnaryMinusExpression)
gen_pp_UnaryNotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=pp_UnaryNotExpression)
gen_pp_ExpressionBlock_Expression = Generalization(general=Expression, specific=pp_ExpressionBlock)
gen_pp_DoubleQuotedString_StringExpression = Generalization(general=StringExpression, specific=pp_DoubleQuotedString)
gen_pp_DoubleQuotedString_IQuotedString = Generalization(general=IQuotedString, specific=pp_DoubleQuotedString)
gen_pp_ElseIfExpression_IfExpression = Generalization(general=IfExpression, specific=pp_ElseIfExpression)
gen_pp_VirtualNameOrReference_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_VirtualNameOrReference)
gen_pp_ParenthesisedExpression_Expression = Generalization(general=Expression, specific=pp_ParenthesisedExpression)
gen_pp_ExprList_Expression = Generalization(general=Expression, specific=pp_ExprList)
gen_pp_SingleQuotedString_StringExpression = Generalization(general=StringExpression, specific=pp_SingleQuotedString)
gen_pp_SingleQuotedString_IQuotedString = Generalization(general=IQuotedString, specific=pp_SingleQuotedString)
gen_pp_StringExpression_Expression = Generalization(general=Expression, specific=pp_StringExpression)
gen_pp_UnquotedString_StringExpression = Generalization(general=StringExpression, specific=pp_UnquotedString)
gen_pp_InterpolatedVariable_Expression = Generalization(general=Expression, specific=pp_InterpolatedVariable)
gen_pp_VerbatimTE_TextExpression = Generalization(general=TextExpression, specific=pp_VerbatimTE)
gen_pp_ExpressionTE_TextExpression = Generalization(general=TextExpression, specific=pp_ExpressionTE)
gen_pp_VariableTE_TextExpression = Generalization(general=TextExpression, specific=pp_VariableTE)
gen_pp_LiteralClass_LiteralExpression = Generalization(general=LiteralExpression, specific=pp_LiteralClass)
gen_pp_UnlessExpression_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_UnlessExpression)
gen_pp_Lambda_ExpressionBlock = Generalization(general=ExpressionBlock, specific=pp_Lambda)
gen_pp_NamedAccessExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=pp_NamedAccessExpression)
gen_pp_MethodCall_WithLambdaExpression = Generalization(general=WithLambdaExpression, specific=pp_MethodCall)
gen_pp_WithLambdaExpression_ParameterizedExpression = Generalization(general=ParameterizedExpression, specific=pp_WithLambdaExpression)
gen_pp_JavaLambda_Lambda = Generalization(general=Lambda, specific=pp_JavaLambda)
gen_pp_RubyLambda_Lambda = Generalization(general=Lambda, specific=pp_RubyLambda)
gen_pp_SeparatorExpression_Expression = Generalization(general=Expression, specific=pp_SeparatorExpression)

# Domain Model
domain_model = DomainModel(
    name="pp",
    types={pp_ResourceBody, pp_AttributeOperations, pp_AttributeOperation, pp_PuppetManifest, ExpressionBlock, pp_Expression, pp_Definition, pp_DefinitionArgumentList, pp_ICollectQuery, pp_VirtualCollectQuery, UnaryExpression, ICollectQuery, pp_DefinitionArgument, pp_ExportedCollectQuery, pp_HostClassDefinition, Definition, pp_LiteralExpression, pp_CaseExpression, Expression, pp_Case, pp_IfExpression, pp_LiteralNameOrReference, LiteralExpression, pp_ResourceExpression, pp_ImportExpression, pp_IQuotedString, pp_LiteralList, pp_LiteralHash, pp_HashEntry, pp_LiteralBoolean, pp_LiteralUndef, pp_LiteralDefault, pp_RelationalExpression, pp_LiteralRegex, pp_LiteralName, pp_VariableExpression, pp_RelationshipExpression, BinaryOpExpression, pp_AssignmentExpression, BinaryExpression, pp_AppendExpression, pp_OrExpression, pp_AndExpression, pp_EqualityExpression, pp_ShiftExpression, pp_AdditiveExpression, pp_MultiplicativeExpression, pp_MatchingExpression, pp_InExpression, pp_AtExpression, ParameterizedExpression, pp_CollectExpression, pp_SelectorExpression, pp_SelectorEntry, pp_FunctionCall, WithLambdaExpression, pp_BinaryOpExpression, pp_BinaryExpression, pp_ParameterizedExpression, pp_NodeDefinition, pp_ElseExpression, pp_UnaryExpression, pp_UnaryMinusExpression, pp_UnaryNotExpression, pp_ExpressionBlock, StringExpression, IQuotedString, pp_ElseIfExpression, IfExpression, pp_VirtualNameOrReference, pp_ParenthesisedExpression, pp_ExprList, pp_DoubleQuotedString, pp_TextExpression, pp_SingleQuotedString, pp_StringExpression, pp_UnquotedString, pp_InterpolatedVariable, pp_VerbatimTE, TextExpression, pp_ExpressionTE, pp_VariableTE, pp_LiteralClass, pp_UnlessExpression, pp_Lambda, pp_NamedAccessExpression, pp_MethodCall, pp_WithLambdaExpression, pp_JavaLambda, Lambda, pp_RubyLambda, pp_SeparatorExpression},
    associations={attributes0, nameExpr1, value3, parent8, attributes5, arguments9, arguments10, puppetType12, value15, switchExpr18, cases20, values22, condExpr25, elseStatement27, resourceExpr30, resourceData32, values35, elements36, elements38, key39, value42, classReference45, leftExpr52, query47, attributes49, rightExpr54, leftExpr57, parameters59, hostNames62, parentName64, expr67, statements69, expr71, expressions73, stringPart75, expression76, elseStatement82, expression78, condExpr80, arguments85, methodExpr87, lambda89},
    generalizations={gen_pp_PuppetManifest_ExpressionBlock, gen_pp_Definition_ExpressionBlock, gen_pp_VirtualCollectQuery_UnaryExpression, gen_pp_VirtualCollectQuery_ICollectQuery, gen_pp_ExportedCollectQuery_UnaryExpression, gen_pp_ExportedCollectQuery_ICollectQuery, gen_pp_HostClassDefinition_Definition, gen_pp_CaseExpression_Expression, gen_pp_Case_ExpressionBlock, gen_pp_IfExpression_ExpressionBlock, gen_pp_LiteralExpression_Expression, gen_pp_LiteralNameOrReference_LiteralExpression, gen_pp_ResourceExpression_Expression, gen_pp_ImportExpression_Expression, gen_pp_LiteralList_LiteralExpression, gen_pp_LiteralDefault_LiteralExpression, gen_pp_LiteralHash_LiteralExpression, gen_pp_LiteralBoolean_LiteralExpression, gen_pp_LiteralUndef_LiteralExpression, gen_pp_LiteralRegex_LiteralExpression, gen_pp_LiteralName_LiteralExpression, gen_pp_VariableExpression_Expression, gen_pp_RelationshipExpression_BinaryOpExpression, gen_pp_AssignmentExpression_BinaryExpression, gen_pp_AppendExpression_BinaryExpression, gen_pp_OrExpression_BinaryExpression, gen_pp_AndExpression_BinaryExpression, gen_pp_RelationalExpression_BinaryOpExpression, gen_pp_EqualityExpression_BinaryOpExpression, gen_pp_ShiftExpression_BinaryOpExpression, gen_pp_AdditiveExpression_BinaryOpExpression, gen_pp_MultiplicativeExpression_BinaryOpExpression, gen_pp_MatchingExpression_BinaryOpExpression, gen_pp_InExpression_BinaryOpExpression, gen_pp_AtExpression_ParameterizedExpression, gen_pp_CollectExpression_Expression, gen_pp_SelectorExpression_ParameterizedExpression, gen_pp_SelectorEntry_BinaryExpression, gen_pp_FunctionCall_WithLambdaExpression, gen_pp_BinaryOpExpression_BinaryExpression, gen_pp_BinaryExpression_Expression, gen_pp_ParameterizedExpression_Expression, gen_pp_NodeDefinition_ExpressionBlock, gen_pp_ElseExpression_ExpressionBlock, gen_pp_UnaryExpression_Expression, gen_pp_UnaryMinusExpression_UnaryExpression, gen_pp_UnaryNotExpression_UnaryExpression, gen_pp_ExpressionBlock_Expression, gen_pp_DoubleQuotedString_StringExpression, gen_pp_DoubleQuotedString_IQuotedString, gen_pp_ElseIfExpression_IfExpression, gen_pp_VirtualNameOrReference_LiteralExpression, gen_pp_ParenthesisedExpression_Expression, gen_pp_ExprList_Expression, gen_pp_SingleQuotedString_StringExpression, gen_pp_SingleQuotedString_IQuotedString, gen_pp_StringExpression_Expression, gen_pp_UnquotedString_StringExpression, gen_pp_InterpolatedVariable_Expression, gen_pp_VerbatimTE_TextExpression, gen_pp_ExpressionTE_TextExpression, gen_pp_VariableTE_TextExpression, gen_pp_LiteralClass_LiteralExpression, gen_pp_UnlessExpression_ExpressionBlock, gen_pp_Lambda_ExpressionBlock, gen_pp_NamedAccessExpression_BinaryExpression, gen_pp_MethodCall_WithLambdaExpression, gen_pp_WithLambdaExpression_ParameterizedExpression, gen_pp_JavaLambda_Lambda, gen_pp_RubyLambda_Lambda, gen_pp_SeparatorExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)