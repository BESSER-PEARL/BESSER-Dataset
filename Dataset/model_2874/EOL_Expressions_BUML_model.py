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
eol_expression_Type = Class(name="eol::expression::Type")
eol_expression_OperatorExpression = Class(name="eol::expression::OperatorExpression", is_abstract=True)
Expression = Class(name="Expression")
eol_expression_Expression = Class(name="eol::expression::Expression", is_abstract=True)
eol_expression_FormalParameterExpression = Class(name="eol::expression::FormalParameterExpression")
VariableDeclarationExpression = Class(name="VariableDeclarationExpression")
eol_expression_FeatureCallExpression = Class(name="eol::expression::FeatureCallExpression", is_abstract=True)
eol_expression_UnaryOperatorExpression = Class(name="eol::expression::UnaryOperatorExpression", is_abstract=True)
OperatorExpression = Class(name="OperatorExpression")
eol_expression_NotOperatorExpression = Class(name="eol::expression::NotOperatorExpression")
UnaryOperatorExpression = Class(name="UnaryOperatorExpression")
eol_expression_NegativeOperatorExpression = Class(name="eol::expression::NegativeOperatorExpression")
eol_expression_BinaryOperatorExpression = Class(name="eol::expression::BinaryOperatorExpression", is_abstract=True)
eol_expression_LogicalOperatorExpression = Class(name="eol::expression::LogicalOperatorExpression", is_abstract=True)
BinaryOperatorExpression = Class(name="BinaryOperatorExpression")
eol_expression_AndOperatorExpression = Class(name="eol::expression::AndOperatorExpression")
LogicalOperatorExpression = Class(name="LogicalOperatorExpression")
eol_expression_XorOperatorExpression = Class(name="eol::expression::XorOperatorExpression")
eol_expression_OrOperatorExpression = Class(name="eol::expression::OrOperatorExpression")
eol_expression_ImpliesOperatorExpression = Class(name="eol::expression::ImpliesOperatorExpression")
eol_expression_ArithmeticOperatorExpression = Class(name="eol::expression::ArithmeticOperatorExpression", is_abstract=True)
eol_expression_DivideOperatorExpression = Class(name="eol::expression::DivideOperatorExpression")
ArithmeticOperatorExpression = Class(name="ArithmeticOperatorExpression")
eol_expression_MultiplyOperatorExpression = Class(name="eol::expression::MultiplyOperatorExpression")
eol_expression_MinusOperatorExpression = Class(name="eol::expression::MinusOperatorExpression")
eol_expression_PlusOperatorExpression = Class(name="eol::expression::PlusOperatorExpression")
eol_expression_ComparisonOperatorExpression = Class(name="eol::expression::ComparisonOperatorExpression", is_abstract=True)
eol_expression_GreaterThanOrEqualToOperatorExpression = Class(name="eol::expression::GreaterThanOrEqualToOperatorExpression")
ComparisonOperatorExpression = Class(name="ComparisonOperatorExpression")
eol_expression_GreaterThanOperatorExpression = Class(name="eol::expression::GreaterThanOperatorExpression")
eol_expression_LessThanOrEqualToOperatorExpression = Class(name="eol::expression::LessThanOrEqualToOperatorExpression")
eol_expression_LessThanOperatorExpression = Class(name="eol::expression::LessThanOperatorExpression")
eol_expression_NotEqualsOperatorExpression = Class(name="eol::expression::NotEqualsOperatorExpression")
eol_expression_EqualsOperatorExpression = Class(name="eol::expression::EqualsOperatorExpression")
eol_expression_VariableDeclarationExpression = Class(name="eol::expression::VariableDeclarationExpression")
eol_expression_NameExpression = Class(name="eol::expression::NameExpression")
eol_expression_CollectionExpression = Class(name="eol::expression::CollectionExpression", is_abstract=True)
eol_expression_CollectionInitialisationExpression = Class(name="eol::expression::CollectionInitialisationExpression", is_abstract=True)
eol_expression_PrimitiveExpression = Class(name="eol::expression::PrimitiveExpression", is_abstract=True)
eol_expression_ComparableExpression = Class(name="eol::expression::ComparableExpression", is_abstract=True)
PrimitiveExpression = Class(name="PrimitiveExpression")
eol_expression_MethodCallExpression = Class(name="eol::expression::MethodCallExpression")
FeatureCallExpression = Class(name="FeatureCallExpression")
eol_expression_PropertyCallExpression = Class(name="eol::expression::PropertyCallExpression")
eol_expression_FOLMethodCallExpression = Class(name="eol::expression::FOLMethodCallExpression")
eol_expression_KeyValueExpression = Class(name="eol::expression::KeyValueExpression")
eol_expression_NewExpression = Class(name="eol::expression::NewExpression")
eol_expression_MapExpression = Class(name="eol::expression::MapExpression")
eol_expression_Statement = Class(name="eol::expression::Statement", is_abstract=True)
eol_expression_SummableExpression = Class(name="eol::expression::SummableExpression", is_abstract=True)
eol_expression_StringExpression = Class(name="eol::expression::StringExpression")
ComparableExpression = Class(name="ComparableExpression")
SummableExpression = Class(name="SummableExpression")
eol_expression_BooleanExpression = Class(name="eol::expression::BooleanExpression")
eol_expression_RealExpression = Class(name="eol::expression::RealExpression")
eol_expression_IntegerExpression = Class(name="eol::expression::IntegerExpression")
eol_expression_BagExpression = Class(name="eol::expression::BagExpression")
CollectionExpression = Class(name="CollectionExpression")
eol_expression_SetExpression = Class(name="eol::expression::SetExpression")
UniqueCollection = Class(name="UniqueCollection")
eol_expression_OrderedSetExpression = Class(name="eol::expression::OrderedSetExpression")
OrderedCollection = Class(name="OrderedCollection")
eol_expression_SequenceExpression = Class(name="eol::expression::SequenceExpression")
eol_expression_OrderedCollection = Class(name="eol::expression::OrderedCollection", is_abstract=True)
eol_expression_UniqueCollection = Class(name="eol::expression::UniqueCollection", is_abstract=True)
eol_expression_EnumerationLiteralExpression = Class(name="eol::expression::EnumerationLiteralExpression")
eol_expression_ExpressionRange = Class(name="eol::expression::ExpressionRange")
CollectionInitialisationExpression = Class(name="CollectionInitialisationExpression")
eol_expression_ExpressionList = Class(name="eol::expression::ExpressionList")

# eol_expression_Type class attributes and methods

# eol_expression_OperatorExpression class attributes and methods

# Expression class attributes and methods

# eol_expression_Expression class attributes and methods
eol_expression_Expression_inBrackets: Property = Property(name="inBrackets", type=BooleanType)
eol_expression_Expression.attributes={eol_expression_Expression_inBrackets}

# eol_expression_FormalParameterExpression class attributes and methods

# VariableDeclarationExpression class attributes and methods

# eol_expression_FeatureCallExpression class attributes and methods
eol_expression_FeatureCallExpression_arrow: Property = Property(name="arrow", type=BooleanType)
eol_expression_FeatureCallExpression.attributes={eol_expression_FeatureCallExpression_arrow}

# eol_expression_UnaryOperatorExpression class attributes and methods

# OperatorExpression class attributes and methods

# eol_expression_NotOperatorExpression class attributes and methods

# UnaryOperatorExpression class attributes and methods

# eol_expression_NegativeOperatorExpression class attributes and methods

# eol_expression_BinaryOperatorExpression class attributes and methods

# eol_expression_LogicalOperatorExpression class attributes and methods

# BinaryOperatorExpression class attributes and methods

# eol_expression_AndOperatorExpression class attributes and methods

# LogicalOperatorExpression class attributes and methods

# eol_expression_XorOperatorExpression class attributes and methods

# eol_expression_OrOperatorExpression class attributes and methods

# eol_expression_ImpliesOperatorExpression class attributes and methods

# eol_expression_ArithmeticOperatorExpression class attributes and methods

# eol_expression_DivideOperatorExpression class attributes and methods

# ArithmeticOperatorExpression class attributes and methods

# eol_expression_MultiplyOperatorExpression class attributes and methods

# eol_expression_MinusOperatorExpression class attributes and methods

# eol_expression_PlusOperatorExpression class attributes and methods

# eol_expression_ComparisonOperatorExpression class attributes and methods

# eol_expression_GreaterThanOrEqualToOperatorExpression class attributes and methods

# ComparisonOperatorExpression class attributes and methods

# eol_expression_GreaterThanOperatorExpression class attributes and methods

# eol_expression_LessThanOrEqualToOperatorExpression class attributes and methods

# eol_expression_LessThanOperatorExpression class attributes and methods

# eol_expression_NotEqualsOperatorExpression class attributes and methods

# eol_expression_EqualsOperatorExpression class attributes and methods

# eol_expression_VariableDeclarationExpression class attributes and methods
eol_expression_VariableDeclarationExpression_create: Property = Property(name="create", type=BooleanType)
eol_expression_VariableDeclarationExpression.attributes={eol_expression_VariableDeclarationExpression_create}

# eol_expression_NameExpression class attributes and methods
eol_expression_NameExpression_name: Property = Property(name="name", type=StringType)
eol_expression_NameExpression_isType: Property = Property(name="isType", type=BooleanType)
eol_expression_NameExpression.attributes={eol_expression_NameExpression_isType, eol_expression_NameExpression_name}

# eol_expression_CollectionExpression class attributes and methods

# eol_expression_CollectionInitialisationExpression class attributes and methods

# eol_expression_PrimitiveExpression class attributes and methods

# eol_expression_ComparableExpression class attributes and methods

# PrimitiveExpression class attributes and methods

# eol_expression_MethodCallExpression class attributes and methods

# FeatureCallExpression class attributes and methods

# eol_expression_PropertyCallExpression class attributes and methods
eol_expression_PropertyCallExpression_extended: Property = Property(name="extended", type=BooleanType)
eol_expression_PropertyCallExpression.attributes={eol_expression_PropertyCallExpression_extended}

# eol_expression_FOLMethodCallExpression class attributes and methods

# eol_expression_KeyValueExpression class attributes and methods

# eol_expression_NewExpression class attributes and methods

# eol_expression_MapExpression class attributes and methods

# eol_expression_Statement class attributes and methods

# eol_expression_SummableExpression class attributes and methods

# eol_expression_StringExpression class attributes and methods
eol_expression_StringExpression_value: Property = Property(name="value", type=StringType)
eol_expression_StringExpression.attributes={eol_expression_StringExpression_value}

# ComparableExpression class attributes and methods

# SummableExpression class attributes and methods

# eol_expression_BooleanExpression class attributes and methods
eol_expression_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
eol_expression_BooleanExpression.attributes={eol_expression_BooleanExpression_value}

# eol_expression_RealExpression class attributes and methods
eol_expression_RealExpression_value: Property = Property(name="value", type=FloatType)
eol_expression_RealExpression.attributes={eol_expression_RealExpression_value}

# eol_expression_IntegerExpression class attributes and methods
eol_expression_IntegerExpression_value: Property = Property(name="value", type=IntegerType)
eol_expression_IntegerExpression.attributes={eol_expression_IntegerExpression_value}

# eol_expression_BagExpression class attributes and methods

# CollectionExpression class attributes and methods

# eol_expression_SetExpression class attributes and methods

# UniqueCollection class attributes and methods

# eol_expression_OrderedSetExpression class attributes and methods

# OrderedCollection class attributes and methods

# eol_expression_SequenceExpression class attributes and methods

# eol_expression_OrderedCollection class attributes and methods

# eol_expression_UniqueCollection class attributes and methods

# eol_expression_EnumerationLiteralExpression class attributes and methods

# eol_expression_ExpressionRange class attributes and methods

# CollectionInitialisationExpression class attributes and methods

# eol_expression_ExpressionList class attributes and methods

# Relationships
resolvedType0: BinaryAssociation = BinaryAssociation(
    name="resolvedType0",
    ends={
        Property(name="eol_expression_Type", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_Expression", type=eol_expression_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="eol_expression_Expression10", type=eol_expression_FeatureCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_FeatureCallExpression", type=eol_expression_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="eol_expression_Expression2", type=eol_expression_UnaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_UnaryOperatorExpression", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs3: BinaryAssociation = BinaryAssociation(
    name="lhs3",
    ends={
        Property(name="eol_expression_Expression4", type=eol_expression_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_BinaryOperatorExpression", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs5: BinaryAssociation = BinaryAssociation(
    name="rhs5",
    ends={
        Property(name="eol_expression_Expression7", type=eol_expression_BinaryOperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_BinaryOperatorExpression6", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name8: BinaryAssociation = BinaryAssociation(
    name="name8",
    ends={
        Property(name="eol_expression_NameExpression", type=eol_expression_VariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_VariableDeclarationExpression", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contents37: BinaryAssociation = BinaryAssociation(
    name="contents37",
    ends={
        Property(name="eol_expression_Expression38", type=eol_expression_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_CollectionExpression", type=eol_expression_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterList39: BinaryAssociation = BinaryAssociation(
    name="parameterList39",
    ends={
        Property(name="eol_expression_CollectionInitialisationExpression", type=eol_expression_CollectionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_CollectionExpression40", type=eol_expression_CollectionInitialisationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments11: BinaryAssociation = BinaryAssociation(
    name="arguments11",
    ends={
        Property(name="eol_expression_Expression12", type=eol_expression_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_MethodCallExpression", type=eol_expression_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method13: BinaryAssociation = BinaryAssociation(
    name="method13",
    ends={
        Property(name="eol_expression_NameExpression15", type=eol_expression_MethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_MethodCallExpression14", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property16: BinaryAssociation = BinaryAssociation(
    name="property16",
    ends={
        Property(name="eol_expression_NameExpression17", type=eol_expression_PropertyCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_PropertyCallExpression", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator18: BinaryAssociation = BinaryAssociation(
    name="iterator18",
    ends={
        Property(name="eol_expression_FormalParameterExpression", type=eol_expression_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_FOLMethodCallExpression", type=eol_expression_FormalParameterExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditions19: BinaryAssociation = BinaryAssociation(
    name="conditions19",
    ends={
        Property(name="eol_expression_Expression21", type=eol_expression_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_FOLMethodCallExpression20", type=eol_expression_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
method22: BinaryAssociation = BinaryAssociation(
    name="method22",
    ends={
        Property(name="eol_expression_NameExpression24", type=eol_expression_FOLMethodCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_FOLMethodCallExpression23", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key25: BinaryAssociation = BinaryAssociation(
    name="key25",
    ends={
        Property(name="eol_expression_Expression26", type=eol_expression_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_KeyValueExpression", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value27: BinaryAssociation = BinaryAssociation(
    name="value27",
    ends={
        Property(name="eol_expression_Expression29", type=eol_expression_KeyValueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_KeyValueExpression28", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeName30: BinaryAssociation = BinaryAssociation(
    name="typeName30",
    ends={
        Property(name="eol_expression_NameExpression31", type=eol_expression_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_NewExpression", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters32: BinaryAssociation = BinaryAssociation(
    name="parameters32",
    ends={
        Property(name="eol_expression_Expression34", type=eol_expression_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_NewExpression33", type=eol_expression_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyValues35: BinaryAssociation = BinaryAssociation(
    name="keyValues35",
    ends={
        Property(name="eol_expression_KeyValueExpression36", type=eol_expression_MapExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_MapExpression", type=eol_expression_KeyValueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal41: BinaryAssociation = BinaryAssociation(
    name="literal41",
    ends={
        Property(name="eol_expression_NameExpression42", type=eol_expression_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_EnumerationLiteralExpression", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumeration43: BinaryAssociation = BinaryAssociation(
    name="enumeration43",
    ends={
        Property(name="eol_expression_NameExpression45", type=eol_expression_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_EnumerationLiteralExpression44", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model46: BinaryAssociation = BinaryAssociation(
    name="model46",
    ends={
        Property(name="eol_expression_NameExpression48", type=eol_expression_EnumerationLiteralExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_EnumerationLiteralExpression47", type=eol_expression_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start49: BinaryAssociation = BinaryAssociation(
    name="start49",
    ends={
        Property(name="eol_expression_Expression50", type=eol_expression_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_ExpressionRange", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end51: BinaryAssociation = BinaryAssociation(
    name="end51",
    ends={
        Property(name="eol_expression_Expression53", type=eol_expression_ExpressionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_ExpressionRange52", type=eol_expression_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions54: BinaryAssociation = BinaryAssociation(
    name="expressions54",
    ends={
        Property(name="eol_expression_Expression55", type=eol_expression_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_expression_ExpressionList", type=eol_expression_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_eol_expression_OperatorExpression_Expression = Generalization(general=Expression, specific=eol_expression_OperatorExpression)
gen_eol_expression_FormalParameterExpression_VariableDeclarationExpression = Generalization(general=VariableDeclarationExpression, specific=eol_expression_FormalParameterExpression)
gen_eol_expression_NameExpression_Expression = Generalization(general=Expression, specific=eol_expression_NameExpression)
gen_eol_expression_FeatureCallExpression_Expression = Generalization(general=Expression, specific=eol_expression_FeatureCallExpression)
gen_eol_expression_UnaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_expression_UnaryOperatorExpression)
gen_eol_expression_NotOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_expression_NotOperatorExpression)
gen_eol_expression_NegativeOperatorExpression_UnaryOperatorExpression = Generalization(general=UnaryOperatorExpression, specific=eol_expression_NegativeOperatorExpression)
gen_eol_expression_BinaryOperatorExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=eol_expression_BinaryOperatorExpression)
gen_eol_expression_LogicalOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_expression_LogicalOperatorExpression)
gen_eol_expression_AndOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_expression_AndOperatorExpression)
gen_eol_expression_XorOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_expression_XorOperatorExpression)
gen_eol_expression_OrOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_expression_OrOperatorExpression)
gen_eol_expression_ImpliesOperatorExpression_LogicalOperatorExpression = Generalization(general=LogicalOperatorExpression, specific=eol_expression_ImpliesOperatorExpression)
gen_eol_expression_ArithmeticOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_expression_ArithmeticOperatorExpression)
gen_eol_expression_DivideOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_expression_DivideOperatorExpression)
gen_eol_expression_MultiplyOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_expression_MultiplyOperatorExpression)
gen_eol_expression_MinusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_expression_MinusOperatorExpression)
gen_eol_expression_PlusOperatorExpression_ArithmeticOperatorExpression = Generalization(general=ArithmeticOperatorExpression, specific=eol_expression_PlusOperatorExpression)
gen_eol_expression_ComparisonOperatorExpression_BinaryOperatorExpression = Generalization(general=BinaryOperatorExpression, specific=eol_expression_ComparisonOperatorExpression)
gen_eol_expression_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_expression_GreaterThanOrEqualToOperatorExpression)
gen_eol_expression_GreaterThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_expression_GreaterThanOperatorExpression)
gen_eol_expression_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_expression_LessThanOrEqualToOperatorExpression)
gen_eol_expression_LessThanOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_expression_LessThanOperatorExpression)
gen_eol_expression_NotEqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_expression_NotEqualsOperatorExpression)
gen_eol_expression_EqualsOperatorExpression_ComparisonOperatorExpression = Generalization(general=ComparisonOperatorExpression, specific=eol_expression_EqualsOperatorExpression)
gen_eol_expression_VariableDeclarationExpression_Expression = Generalization(general=Expression, specific=eol_expression_VariableDeclarationExpression)
gen_eol_expression_CollectionExpression_Expression = Generalization(general=Expression, specific=eol_expression_CollectionExpression)
gen_eol_expression_PrimitiveExpression_Expression = Generalization(general=Expression, specific=eol_expression_PrimitiveExpression)
gen_eol_expression_ComparableExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_expression_ComparableExpression)
gen_eol_expression_MethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_expression_MethodCallExpression)
gen_eol_expression_PropertyCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_expression_PropertyCallExpression)
gen_eol_expression_FOLMethodCallExpression_FeatureCallExpression = Generalization(general=FeatureCallExpression, specific=eol_expression_FOLMethodCallExpression)
gen_eol_expression_KeyValueExpression_Expression = Generalization(general=Expression, specific=eol_expression_KeyValueExpression)
gen_eol_expression_NewExpression_Expression = Generalization(general=Expression, specific=eol_expression_NewExpression)
gen_eol_expression_MapExpression_Expression = Generalization(general=Expression, specific=eol_expression_MapExpression)
gen_eol_expression_SummableExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_expression_SummableExpression)
gen_eol_expression_StringExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_expression_StringExpression)
gen_eol_expression_StringExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_expression_StringExpression)
gen_eol_expression_BooleanExpression_PrimitiveExpression = Generalization(general=PrimitiveExpression, specific=eol_expression_BooleanExpression)
gen_eol_expression_RealExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_expression_RealExpression)
gen_eol_expression_RealExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_expression_RealExpression)
gen_eol_expression_IntegerExpression_ComparableExpression = Generalization(general=ComparableExpression, specific=eol_expression_IntegerExpression)
gen_eol_expression_IntegerExpression_SummableExpression = Generalization(general=SummableExpression, specific=eol_expression_IntegerExpression)
gen_eol_expression_BagExpression_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_expression_BagExpression)
gen_eol_expression_SetExpression_UniqueCollection = Generalization(general=UniqueCollection, specific=eol_expression_SetExpression)
gen_eol_expression_OrderedSetExpression_OrderedCollection = Generalization(general=OrderedCollection, specific=eol_expression_OrderedSetExpression)
gen_eol_expression_OrderedSetExpression_UniqueCollection = Generalization(general=UniqueCollection, specific=eol_expression_OrderedSetExpression)
gen_eol_expression_SequenceExpression_OrderedCollection = Generalization(general=OrderedCollection, specific=eol_expression_SequenceExpression)
gen_eol_expression_OrderedCollection_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_expression_OrderedCollection)
gen_eol_expression_UniqueCollection_CollectionExpression = Generalization(general=CollectionExpression, specific=eol_expression_UniqueCollection)
gen_eol_expression_EnumerationLiteralExpression_Expression = Generalization(general=Expression, specific=eol_expression_EnumerationLiteralExpression)
gen_eol_expression_CollectionInitialisationExpression_Expression = Generalization(general=Expression, specific=eol_expression_CollectionInitialisationExpression)
gen_eol_expression_ExpressionRange_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_expression_ExpressionRange)
gen_eol_expression_ExpressionList_CollectionInitialisationExpression = Generalization(general=CollectionInitialisationExpression, specific=eol_expression_ExpressionList)

# Domain Model
domain_model = DomainModel(
    name="eol_expression",
    types={eol_expression_Type, eol_expression_OperatorExpression, Expression, eol_expression_Expression, eol_expression_FormalParameterExpression, VariableDeclarationExpression, eol_expression_FeatureCallExpression, eol_expression_UnaryOperatorExpression, OperatorExpression, eol_expression_NotOperatorExpression, UnaryOperatorExpression, eol_expression_NegativeOperatorExpression, eol_expression_BinaryOperatorExpression, eol_expression_LogicalOperatorExpression, BinaryOperatorExpression, eol_expression_AndOperatorExpression, LogicalOperatorExpression, eol_expression_XorOperatorExpression, eol_expression_OrOperatorExpression, eol_expression_ImpliesOperatorExpression, eol_expression_ArithmeticOperatorExpression, eol_expression_DivideOperatorExpression, ArithmeticOperatorExpression, eol_expression_MultiplyOperatorExpression, eol_expression_MinusOperatorExpression, eol_expression_PlusOperatorExpression, eol_expression_ComparisonOperatorExpression, eol_expression_GreaterThanOrEqualToOperatorExpression, ComparisonOperatorExpression, eol_expression_GreaterThanOperatorExpression, eol_expression_LessThanOrEqualToOperatorExpression, eol_expression_LessThanOperatorExpression, eol_expression_NotEqualsOperatorExpression, eol_expression_EqualsOperatorExpression, eol_expression_VariableDeclarationExpression, eol_expression_NameExpression, eol_expression_CollectionExpression, eol_expression_CollectionInitialisationExpression, eol_expression_PrimitiveExpression, eol_expression_ComparableExpression, PrimitiveExpression, eol_expression_MethodCallExpression, FeatureCallExpression, eol_expression_PropertyCallExpression, eol_expression_FOLMethodCallExpression, eol_expression_KeyValueExpression, eol_expression_NewExpression, eol_expression_MapExpression, eol_expression_Statement, eol_expression_SummableExpression, eol_expression_StringExpression, ComparableExpression, SummableExpression, eol_expression_BooleanExpression, eol_expression_RealExpression, eol_expression_IntegerExpression, eol_expression_BagExpression, CollectionExpression, eol_expression_SetExpression, UniqueCollection, eol_expression_OrderedSetExpression, OrderedCollection, eol_expression_SequenceExpression, eol_expression_OrderedCollection, eol_expression_UniqueCollection, eol_expression_EnumerationLiteralExpression, eol_expression_ExpressionRange, CollectionInitialisationExpression, eol_expression_ExpressionList},
    associations={resolvedType0, target9, expression1, lhs3, rhs5, name8, contents37, parameterList39, arguments11, method13, property16, iterator18, conditions19, method22, key25, value27, typeName30, parameters32, keyValues35, literal41, enumeration43, model46, start49, end51, expressions54},
    generalizations={gen_eol_expression_OperatorExpression_Expression, gen_eol_expression_FormalParameterExpression_VariableDeclarationExpression, gen_eol_expression_NameExpression_Expression, gen_eol_expression_FeatureCallExpression_Expression, gen_eol_expression_UnaryOperatorExpression_OperatorExpression, gen_eol_expression_NotOperatorExpression_UnaryOperatorExpression, gen_eol_expression_NegativeOperatorExpression_UnaryOperatorExpression, gen_eol_expression_BinaryOperatorExpression_OperatorExpression, gen_eol_expression_LogicalOperatorExpression_BinaryOperatorExpression, gen_eol_expression_AndOperatorExpression_LogicalOperatorExpression, gen_eol_expression_XorOperatorExpression_LogicalOperatorExpression, gen_eol_expression_OrOperatorExpression_LogicalOperatorExpression, gen_eol_expression_ImpliesOperatorExpression_LogicalOperatorExpression, gen_eol_expression_ArithmeticOperatorExpression_BinaryOperatorExpression, gen_eol_expression_DivideOperatorExpression_ArithmeticOperatorExpression, gen_eol_expression_MultiplyOperatorExpression_ArithmeticOperatorExpression, gen_eol_expression_MinusOperatorExpression_ArithmeticOperatorExpression, gen_eol_expression_PlusOperatorExpression_ArithmeticOperatorExpression, gen_eol_expression_ComparisonOperatorExpression_BinaryOperatorExpression, gen_eol_expression_GreaterThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_expression_GreaterThanOperatorExpression_ComparisonOperatorExpression, gen_eol_expression_LessThanOrEqualToOperatorExpression_ComparisonOperatorExpression, gen_eol_expression_LessThanOperatorExpression_ComparisonOperatorExpression, gen_eol_expression_NotEqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_expression_EqualsOperatorExpression_ComparisonOperatorExpression, gen_eol_expression_VariableDeclarationExpression_Expression, gen_eol_expression_CollectionExpression_Expression, gen_eol_expression_PrimitiveExpression_Expression, gen_eol_expression_ComparableExpression_PrimitiveExpression, gen_eol_expression_MethodCallExpression_FeatureCallExpression, gen_eol_expression_PropertyCallExpression_FeatureCallExpression, gen_eol_expression_FOLMethodCallExpression_FeatureCallExpression, gen_eol_expression_KeyValueExpression_Expression, gen_eol_expression_NewExpression_Expression, gen_eol_expression_MapExpression_Expression, gen_eol_expression_SummableExpression_PrimitiveExpression, gen_eol_expression_StringExpression_ComparableExpression, gen_eol_expression_StringExpression_SummableExpression, gen_eol_expression_BooleanExpression_PrimitiveExpression, gen_eol_expression_RealExpression_ComparableExpression, gen_eol_expression_RealExpression_SummableExpression, gen_eol_expression_IntegerExpression_ComparableExpression, gen_eol_expression_IntegerExpression_SummableExpression, gen_eol_expression_BagExpression_CollectionExpression, gen_eol_expression_SetExpression_UniqueCollection, gen_eol_expression_OrderedSetExpression_OrderedCollection, gen_eol_expression_OrderedSetExpression_UniqueCollection, gen_eol_expression_SequenceExpression_OrderedCollection, gen_eol_expression_OrderedCollection_CollectionExpression, gen_eol_expression_UniqueCollection_CollectionExpression, gen_eol_expression_EnumerationLiteralExpression_Expression, gen_eol_expression_CollectionInitialisationExpression_Expression, gen_eol_expression_ExpressionRange_CollectionInitialisationExpression, gen_eol_expression_ExpressionList_CollectionInitialisationExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)