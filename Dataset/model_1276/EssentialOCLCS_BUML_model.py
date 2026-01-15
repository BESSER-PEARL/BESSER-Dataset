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
NavigationRole: Enumeration = Enumeration(
    name="NavigationRole",
    literals={
            EnumerationLiteral(name="ITERATOR"),
			EnumerationLiteral(name="ACCUMULATOR"),
			EnumerationLiteral(name="EXPRESSION")
    }
)

# Classes
essentialoclcs_AssociationClassCallExpCS = Class(name="essentialoclcs::AssociationClassCallExpCS", is_abstract=True)
CallExpCS = Class(name="CallExpCS")
essentialoclcs_AssociationClass = Class(name="essentialoclcs::AssociationClass")
essentialoclcs_BooleanLiteralExpCS = Class(name="essentialoclcs::BooleanLiteralExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
essentialoclcs_AbstractNameExpCS = Class(name="essentialoclcs::AbstractNameExpCS", is_abstract=True)
ExpCS = Class(name="ExpCS")
essentialoclcs_CurlyBracketedClauseCS = Class(name="essentialoclcs::CurlyBracketedClauseCS")
essentialoclcs_PathNameCS = Class(name="essentialoclcs::PathNameCS")
essentialoclcs_RoundBracketedClauseCS = Class(name="essentialoclcs::RoundBracketedClauseCS")
essentialoclcs_SquareBracketedClauseCS = Class(name="essentialoclcs::SquareBracketedClauseCS")
essentialoclcs_Type = Class(name="essentialoclcs::Type")
Nameable = Class(name="Nameable")
essentialoclcs_TypedRefCS = Class(name="essentialoclcs::TypedRefCS")
essentialoclcs_ContextCS = Class(name="essentialoclcs::ContextCS")
NamedElementCS = Class(name="NamedElementCS")
RootCS = Class(name="RootCS")
essentialoclcs_CallExpCS = Class(name="essentialoclcs::CallExpCS", is_abstract=True)
AbstractNameExpCS = Class(name="AbstractNameExpCS")
essentialoclcs_ExpCS = Class(name="essentialoclcs::ExpCS")
essentialoclcs_CollectionLiteralExpCS = Class(name="essentialoclcs::CollectionLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
essentialoclcs_CollectionLiteralPartCS = Class(name="essentialoclcs::CollectionLiteralPartCS")
essentialoclcs_CollectionTypeCS = Class(name="essentialoclcs::CollectionTypeCS")
ModelElementCS = Class(name="ModelElementCS")
essentialoclcs_CollectionPatternCS = Class(name="essentialoclcs::CollectionPatternCS")
TypedRefCS = Class(name="TypedRefCS")
essentialoclcs_PatternExpCS = Class(name="essentialoclcs::PatternExpCS")
ContextLessElementCS = Class(name="ContextLessElementCS")
essentialoclcs_ShadowPartCS = Class(name="essentialoclcs::ShadowPartCS")
essentialoclcs_Precedence = Class(name="essentialoclcs::Precedence")
essentialoclcs_ExpSpecificationCS = Class(name="essentialoclcs::ExpSpecificationCS")
SpecificationCS = Class(name="SpecificationCS")
essentialoclcs_IfExpCS = Class(name="essentialoclcs::IfExpCS")
essentialoclcs_OperatorExpCS = Class(name="essentialoclcs::OperatorExpCS", is_abstract=True)
essentialoclcs_IterationCallExpCS = Class(name="essentialoclcs::IterationCallExpCS", is_abstract=True)
essentialoclcs_Iteration = Class(name="essentialoclcs::Iteration")
essentialoclcs_LambdaLiteralExpCS = Class(name="essentialoclcs::LambdaLiteralExpCS")
essentialoclcs_IfThenExpCS = Class(name="essentialoclcs::IfThenExpCS")
essentialoclcs_InfixExpCS = Class(name="essentialoclcs::InfixExpCS")
OperatorExpCS = Class(name="OperatorExpCS")
essentialoclcs_InvalidLiteralExpCS = Class(name="essentialoclcs::InvalidLiteralExpCS")
essentialoclcs_IterateCallExpCS = Class(name="essentialoclcs::IterateCallExpCS", is_abstract=True)
IterationCallExpCS = Class(name="IterationCallExpCS")
essentialoclcs_VariableCS = Class(name="essentialoclcs::VariableCS")
essentialoclcs_NameExpCS = Class(name="essentialoclcs::NameExpCS")
AssociationClassCallExpCS = Class(name="AssociationClassCallExpCS")
ShadowExpCS = Class(name="ShadowExpCS")
IterateCallExpCS = Class(name="IterateCallExpCS")
essentialoclcs_LetExpCS = Class(name="essentialoclcs::LetExpCS")
essentialoclcs_LetVariableCS = Class(name="essentialoclcs::LetVariableCS")
VariableCS = Class(name="VariableCS")
essentialoclcs_LiteralExpCS = Class(name="essentialoclcs::LiteralExpCS")
essentialoclcs_MapLiteralExpCS = Class(name="essentialoclcs::MapLiteralExpCS")
essentialoclcs_MapLiteralPartCS = Class(name="essentialoclcs::MapLiteralPartCS")
essentialoclcs_MapTypeCS = Class(name="essentialoclcs::MapTypeCS")
OperationCallExpCS = Class(name="OperationCallExpCS")
PropertyCallExpCS = Class(name="PropertyCallExpCS")
VariableExpCS = Class(name="VariableExpCS")
essentialoclcs_NavigatingArgCS = Class(name="essentialoclcs::NavigatingArgCS")
essentialoclcs_NestedExpCS = Class(name="essentialoclcs::NestedExpCS")
essentialoclcs_NullLiteralExpCS = Class(name="essentialoclcs::NullLiteralExpCS")
essentialoclcs_NumberLiteralExpCS = Class(name="essentialoclcs::NumberLiteralExpCS")
essentialoclcs_OperationCallExpCS = Class(name="essentialoclcs::OperationCallExpCS", is_abstract=True)
essentialoclcs_Operation = Class(name="essentialoclcs::Operation")
essentialoclcs_TypeRefCS = Class(name="essentialoclcs::TypeRefCS")
essentialoclcs_PrefixExpCS = Class(name="essentialoclcs::PrefixExpCS")
essentialoclcs_PrimitiveLiteralExpCS = Class(name="essentialoclcs::PrimitiveLiteralExpCS")
essentialoclcs_PropertyCallExpCS = Class(name="essentialoclcs::PropertyCallExpCS", is_abstract=True)
essentialoclcs_Property = Class(name="essentialoclcs::Property")
essentialoclcs_SelfExpCS = Class(name="essentialoclcs::SelfExpCS")
essentialoclcs_ShadowExpCS = Class(name="essentialoclcs::ShadowExpCS", is_abstract=True)
essentialoclcs_TypeNameExpCS = Class(name="essentialoclcs::TypeNameExpCS")
essentialoclcs_UnlimitedNaturalLiteralExpCS = Class(name="essentialoclcs::UnlimitedNaturalLiteralExpCS")
essentialoclcs_StringLiteralExpCS = Class(name="essentialoclcs::StringLiteralExpCS")
essentialoclcs_TupleLiteralExpCS = Class(name="essentialoclcs::TupleLiteralExpCS")
essentialoclcs_TupleLiteralPartCS = Class(name="essentialoclcs::TupleLiteralPartCS")
essentialoclcs_TypeLiteralExpCS = Class(name="essentialoclcs::TypeLiteralExpCS")
essentialoclcs_VariableExpCS = Class(name="essentialoclcs::VariableExpCS", is_abstract=True)
essentialoclcs_Variable = Class(name="essentialoclcs::Variable")

# essentialoclcs_AssociationClassCallExpCS class attributes and methods

# CallExpCS class attributes and methods

# essentialoclcs_AssociationClass class attributes and methods

# essentialoclcs_BooleanLiteralExpCS class attributes and methods
essentialoclcs_BooleanLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
essentialoclcs_BooleanLiteralExpCS.attributes={essentialoclcs_BooleanLiteralExpCS_symbol}

# PrimitiveLiteralExpCS class attributes and methods

# essentialoclcs_AbstractNameExpCS class attributes and methods
essentialoclcs_AbstractNameExpCS_isPre: Property = Property(name="isPre", type=BooleanType)
essentialoclcs_AbstractNameExpCS.attributes={essentialoclcs_AbstractNameExpCS_isPre}

# ExpCS class attributes and methods

# essentialoclcs_CurlyBracketedClauseCS class attributes and methods
essentialoclcs_CurlyBracketedClauseCS_value: Property = Property(name="value", type=StringType)
essentialoclcs_CurlyBracketedClauseCS.attributes={essentialoclcs_CurlyBracketedClauseCS_value}

# essentialoclcs_PathNameCS class attributes and methods

# essentialoclcs_RoundBracketedClauseCS class attributes and methods

# essentialoclcs_SquareBracketedClauseCS class attributes and methods

# essentialoclcs_Type class attributes and methods

# Nameable class attributes and methods

# essentialoclcs_TypedRefCS class attributes and methods

# essentialoclcs_ContextCS class attributes and methods

# NamedElementCS class attributes and methods

# RootCS class attributes and methods

# essentialoclcs_CallExpCS class attributes and methods

# AbstractNameExpCS class attributes and methods

# essentialoclcs_ExpCS class attributes and methods
essentialoclcs_ExpCS_hasError: Property = Property(name="hasError", type=BooleanType)
essentialoclcs_ExpCS_m_isLocalLeftAncestorOf: Method = Method(name="isLocalLeftAncestorOf", parameters={Parameter(name='csExp')}, type=BooleanType)
essentialoclcs_ExpCS_m_isLocalRightAncestorOf: Method = Method(name="isLocalRightAncestorOf", parameters={Parameter(name='csExp')}, type=BooleanType)
essentialoclcs_ExpCS.attributes={essentialoclcs_ExpCS_hasError}
essentialoclcs_ExpCS.methods={essentialoclcs_ExpCS_m_isLocalRightAncestorOf, essentialoclcs_ExpCS_m_isLocalLeftAncestorOf}

# essentialoclcs_CollectionLiteralExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# essentialoclcs_CollectionLiteralPartCS class attributes and methods

# essentialoclcs_CollectionTypeCS class attributes and methods
essentialoclcs_CollectionTypeCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_CollectionTypeCS.attributes={essentialoclcs_CollectionTypeCS_name}

# ModelElementCS class attributes and methods

# essentialoclcs_CollectionPatternCS class attributes and methods
essentialoclcs_CollectionPatternCS_restVariableName: Property = Property(name="restVariableName", type=StringType)
essentialoclcs_CollectionPatternCS.attributes={essentialoclcs_CollectionPatternCS_restVariableName}

# TypedRefCS class attributes and methods

# essentialoclcs_PatternExpCS class attributes and methods
essentialoclcs_PatternExpCS_patternVariableName: Property = Property(name="patternVariableName", type=StringType)
essentialoclcs_PatternExpCS.attributes={essentialoclcs_PatternExpCS_patternVariableName}

# ContextLessElementCS class attributes and methods

# essentialoclcs_ShadowPartCS class attributes and methods

# essentialoclcs_Precedence class attributes and methods

# essentialoclcs_ExpSpecificationCS class attributes and methods

# SpecificationCS class attributes and methods

# essentialoclcs_IfExpCS class attributes and methods
essentialoclcs_IfExpCS_isImplicit: Property = Property(name="isImplicit", type=BooleanType)
essentialoclcs_IfExpCS.attributes={essentialoclcs_IfExpCS_isImplicit}

# essentialoclcs_OperatorExpCS class attributes and methods

# essentialoclcs_IterationCallExpCS class attributes and methods

# essentialoclcs_Iteration class attributes and methods

# essentialoclcs_LambdaLiteralExpCS class attributes and methods

# essentialoclcs_IfThenExpCS class attributes and methods

# essentialoclcs_InfixExpCS class attributes and methods

# OperatorExpCS class attributes and methods

# essentialoclcs_InvalidLiteralExpCS class attributes and methods

# essentialoclcs_IterateCallExpCS class attributes and methods

# IterationCallExpCS class attributes and methods

# essentialoclcs_VariableCS class attributes and methods

# essentialoclcs_NameExpCS class attributes and methods

# AssociationClassCallExpCS class attributes and methods

# ShadowExpCS class attributes and methods

# IterateCallExpCS class attributes and methods

# essentialoclcs_LetExpCS class attributes and methods
essentialoclcs_LetExpCS_isImplicit: Property = Property(name="isImplicit", type=BooleanType)
essentialoclcs_LetExpCS.attributes={essentialoclcs_LetExpCS_isImplicit}

# essentialoclcs_LetVariableCS class attributes and methods

# VariableCS class attributes and methods

# essentialoclcs_LiteralExpCS class attributes and methods

# essentialoclcs_MapLiteralExpCS class attributes and methods

# essentialoclcs_MapLiteralPartCS class attributes and methods

# essentialoclcs_MapTypeCS class attributes and methods
essentialoclcs_MapTypeCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_MapTypeCS.attributes={essentialoclcs_MapTypeCS_name}

# OperationCallExpCS class attributes and methods

# PropertyCallExpCS class attributes and methods

# VariableExpCS class attributes and methods

# essentialoclcs_NavigatingArgCS class attributes and methods
essentialoclcs_NavigatingArgCS_prefix: Property = Property(name="prefix", type=StringType)
essentialoclcs_NavigatingArgCS_role: Property = Property(name="role", type=StringType)
essentialoclcs_NavigatingArgCS.attributes={essentialoclcs_NavigatingArgCS_role, essentialoclcs_NavigatingArgCS_prefix}

# essentialoclcs_NestedExpCS class attributes and methods

# essentialoclcs_NullLiteralExpCS class attributes and methods

# essentialoclcs_NumberLiteralExpCS class attributes and methods
essentialoclcs_NumberLiteralExpCS_symbol: Property = Property(name="symbol", type=StringType)
essentialoclcs_NumberLiteralExpCS.attributes={essentialoclcs_NumberLiteralExpCS_symbol}

# essentialoclcs_OperationCallExpCS class attributes and methods

# essentialoclcs_Operation class attributes and methods

# essentialoclcs_TypeRefCS class attributes and methods

# essentialoclcs_PrefixExpCS class attributes and methods

# essentialoclcs_PrimitiveLiteralExpCS class attributes and methods

# essentialoclcs_PropertyCallExpCS class attributes and methods

# essentialoclcs_Property class attributes and methods

# essentialoclcs_SelfExpCS class attributes and methods
essentialoclcs_SelfExpCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_SelfExpCS.attributes={essentialoclcs_SelfExpCS_name}

# essentialoclcs_ShadowExpCS class attributes and methods
essentialoclcs_ShadowExpCS_value: Property = Property(name="value", type=StringType)
essentialoclcs_ShadowExpCS.attributes={essentialoclcs_ShadowExpCS_value}

# essentialoclcs_TypeNameExpCS class attributes and methods

# essentialoclcs_UnlimitedNaturalLiteralExpCS class attributes and methods

# essentialoclcs_StringLiteralExpCS class attributes and methods
essentialoclcs_StringLiteralExpCS_segments: Property = Property(name="segments", type=StringType)
essentialoclcs_StringLiteralExpCS.attributes={essentialoclcs_StringLiteralExpCS_segments}

# essentialoclcs_TupleLiteralExpCS class attributes and methods

# essentialoclcs_TupleLiteralPartCS class attributes and methods

# essentialoclcs_TypeLiteralExpCS class attributes and methods

# essentialoclcs_VariableExpCS class attributes and methods

# essentialoclcs_Variable class attributes and methods

# Relationships
referredAssociation11: BinaryAssociation = BinaryAssociation(
    name="referredAssociation11",
    ends={
        Property(name="essentialoclcs_AssociationClass", type=essentialoclcs_AssociationClassCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_AssociationClassCallExpCS", type=essentialoclcs_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
ownedCurlyBracketedClause0: BinaryAssociation = BinaryAssociation(
    name="ownedCurlyBracketedClause0",
    ends={
        Property(name="CurlyBracketedClauseCS", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningNameExp", type=essentialoclcs_CurlyBracketedClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPathName1: BinaryAssociation = BinaryAssociation(
    name="ownedPathName1",
    ends={
        Property(name="essentialoclcs_PathNameCS", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_AbstractNameExpCS", type=essentialoclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRoundBracketedClause2: BinaryAssociation = BinaryAssociation(
    name="ownedRoundBracketedClause2",
    ends={
        Property(name="RoundBracketedClauseCS", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningNameExp3", type=essentialoclcs_RoundBracketedClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedSquareBracketedClauses4: BinaryAssociation = BinaryAssociation(
    name="ownedSquareBracketedClauses4",
    ends={
        Property(name="SquareBracketedClauseCS", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningNameExp5", type=essentialoclcs_SquareBracketedClauseCS, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
sourceType6: BinaryAssociation = BinaryAssociation(
    name="sourceType6",
    ends={
        Property(name="essentialoclcs_Type", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_AbstractNameExpCS7", type=essentialoclcs_Type, multiplicity=Multiplicity(0, 1))
    }
)
sourceTypeValue8: BinaryAssociation = BinaryAssociation(
    name="sourceTypeValue8",
    ends={
        Property(name="essentialoclcs_Type10", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_AbstractNameExpCS9", type=essentialoclcs_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedType32: BinaryAssociation = BinaryAssociation(
    name="ownedType32",
    ends={
        Property(name="essentialoclcs_TypedRefCS", type=essentialoclcs_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionTypeCS33", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments12: BinaryAssociation = BinaryAssociation(
    name="arguments12",
    ends={
        Property(name="essentialoclcs_ExpCS", type=essentialoclcs_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CallExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 9999))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="essentialoclcs_ExpCS15", type=essentialoclcs_CallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CallExpCS14", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedParts16: BinaryAssociation = BinaryAssociation(
    name="ownedParts16",
    ends={
        Property(name="essentialoclcs_CollectionLiteralPartCS", type=essentialoclcs_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralExpCS", type=essentialoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType17: BinaryAssociation = BinaryAssociation(
    name="ownedType17",
    ends={
        Property(name="essentialoclcs_CollectionTypeCS", type=essentialoclcs_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralExpCS18", type=essentialoclcs_CollectionTypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExpression19: BinaryAssociation = BinaryAssociation(
    name="ownedExpression19",
    ends={
        Property(name="essentialoclcs_ExpCS21", type=essentialoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralPartCS20", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLastExpression22: BinaryAssociation = BinaryAssociation(
    name="ownedLastExpression22",
    ends={
        Property(name="essentialoclcs_ExpCS24", type=essentialoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralPartCS23", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts25: BinaryAssociation = BinaryAssociation(
    name="ownedParts25",
    ends={
        Property(name="essentialoclcs_PatternExpCS", type=essentialoclcs_CollectionPatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionPatternCS", type=essentialoclcs_PatternExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPatternGuard26: BinaryAssociation = BinaryAssociation(
    name="ownedPatternGuard26",
    ends={
        Property(name="essentialoclcs_ExpCS28", type=essentialoclcs_CollectionPatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionPatternCS27", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType29: BinaryAssociation = BinaryAssociation(
    name="ownedType29",
    ends={
        Property(name="essentialoclcs_CollectionTypeCS31", type=essentialoclcs_CollectionPatternCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionPatternCS30", type=essentialoclcs_CollectionTypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExpression34: BinaryAssociation = BinaryAssociation(
    name="ownedExpression34",
    ends={
        Property(name="essentialoclcs_ExpCS35", type=essentialoclcs_ContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ContextCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts36: BinaryAssociation = BinaryAssociation(
    name="ownedParts36",
    ends={
        Property(name="ShadowPartCS", type=essentialoclcs_CurlyBracketedClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCurlyBracketClause", type=essentialoclcs_ShadowPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precedence52: BinaryAssociation = BinaryAssociation(
    name="precedence52",
    ends={
        Property(name="essentialoclcs_Precedence", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS53", type=essentialoclcs_Precedence, multiplicity=Multiplicity(0, 1))
    }
)
ownedExpression54: BinaryAssociation = BinaryAssociation(
    name="ownedExpression54",
    ends={
        Property(name="essentialoclcs_ExpCS55", type=essentialoclcs_ExpSpecificationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpSpecificationCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningNameExp37: BinaryAssociation = BinaryAssociation(
    name="owningNameExp37",
    ends={
        Property(name="AbstractNameExpCS", type=essentialoclcs_CurlyBracketedClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCurlyBracketedClause", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(0, 1))
    }
)
localLeft39: BinaryAssociation = BinaryAssociation(
    name="localLeft39",
    ends={
        Property(name="essentialoclcs_ExpCS40", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS38", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1))
    }
)
localLeftmostDescendant42: BinaryAssociation = BinaryAssociation(
    name="localLeftmostDescendant42",
    ends={
        Property(name="essentialoclcs_ExpCS43", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS41", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1))
    }
)
localParent44: BinaryAssociation = BinaryAssociation(
    name="localParent44",
    ends={
        Property(name="essentialoclcs_OperatorExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS45", type=essentialoclcs_OperatorExpCS, multiplicity=Multiplicity(0, 1))
    }
)
localRight47: BinaryAssociation = BinaryAssociation(
    name="localRight47",
    ends={
        Property(name="essentialoclcs_ExpCS48", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS46", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1))
    }
)
localRightmostDescendant50: BinaryAssociation = BinaryAssociation(
    name="localRightmostDescendant50",
    ends={
        Property(name="essentialoclcs_ExpCS51", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS49", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1))
    }
)
iterators78: BinaryAssociation = BinaryAssociation(
    name="iterators78",
    ends={
        Property(name="essentialoclcs_VariableCS79", type=essentialoclcs_IterationCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IterationCallExpCS", type=essentialoclcs_VariableCS, multiplicity=Multiplicity(0, 9999))
    }
)
referredIteration80: BinaryAssociation = BinaryAssociation(
    name="referredIteration80",
    ends={
        Property(name="essentialoclcs_Iteration", type=essentialoclcs_IterationCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IterationCallExpCS81", type=essentialoclcs_Iteration, multiplicity=Multiplicity(0, 1))
    }
)
ownedExpressionCS82: BinaryAssociation = BinaryAssociation(
    name="ownedExpressionCS82",
    ends={
        Property(name="essentialoclcs_ExpCS83", type=essentialoclcs_LambdaLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_LambdaLiteralExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedCondition56: BinaryAssociation = BinaryAssociation(
    name="ownedCondition56",
    ends={
        Property(name="essentialoclcs_ExpCS57", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedElseExpression58: BinaryAssociation = BinaryAssociation(
    name="ownedElseExpression58",
    ends={
        Property(name="essentialoclcs_ExpCS60", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS59", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedIfThenExpressions61: BinaryAssociation = BinaryAssociation(
    name="ownedIfThenExpressions61",
    ends={
        Property(name="essentialoclcs_IfThenExpCS", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS62", type=essentialoclcs_IfThenExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedThenExpression63: BinaryAssociation = BinaryAssociation(
    name="ownedThenExpression63",
    ends={
        Property(name="essentialoclcs_ExpCS65", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS64", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedCondition66: BinaryAssociation = BinaryAssociation(
    name="ownedCondition66",
    ends={
        Property(name="essentialoclcs_ExpCS68", type=essentialoclcs_IfThenExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfThenExpCS67", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedThenExpression69: BinaryAssociation = BinaryAssociation(
    name="ownedThenExpression69",
    ends={
        Property(name="essentialoclcs_ExpCS71", type=essentialoclcs_IfThenExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfThenExpCS70", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument72: BinaryAssociation = BinaryAssociation(
    name="argument72",
    ends={
        Property(name="essentialoclcs_ExpCS73", type=essentialoclcs_InfixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_InfixExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedLeft74: BinaryAssociation = BinaryAssociation(
    name="ownedLeft74",
    ends={
        Property(name="essentialoclcs_ExpCS76", type=essentialoclcs_InfixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_InfixExpCS75", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accumulators77: BinaryAssociation = BinaryAssociation(
    name="accumulators77",
    ends={
        Property(name="essentialoclcs_VariableCS", type=essentialoclcs_IterateCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IterateCallExpCS", type=essentialoclcs_VariableCS, multiplicity=Multiplicity(0, 9999))
    }
)
ownedKeyType98: BinaryAssociation = BinaryAssociation(
    name="ownedKeyType98",
    ends={
        Property(name="essentialoclcs_TypedRefCS100", type=essentialoclcs_MapTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_MapTypeCS99", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedValueType101: BinaryAssociation = BinaryAssociation(
    name="ownedValueType101",
    ends={
        Property(name="essentialoclcs_TypedRefCS103", type=essentialoclcs_MapTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_MapTypeCS102", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedInExpression84: BinaryAssociation = BinaryAssociation(
    name="ownedInExpression84",
    ends={
        Property(name="essentialoclcs_ExpCS85", type=essentialoclcs_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_LetExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedVariables86: BinaryAssociation = BinaryAssociation(
    name="ownedVariables86",
    ends={
        Property(name="LetVariableCS", type=essentialoclcs_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLetExpression", type=essentialoclcs_LetVariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRoundBracketedClause87: BinaryAssociation = BinaryAssociation(
    name="ownedRoundBracketedClause87",
    ends={
        Property(name="essentialoclcs_RoundBracketedClauseCS", type=essentialoclcs_LetVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_LetVariableCS", type=essentialoclcs_RoundBracketedClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningLetExpression88: BinaryAssociation = BinaryAssociation(
    name="owningLetExpression88",
    ends={
        Property(name="LetExpCS", type=essentialoclcs_LetVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedVariables", type=essentialoclcs_LetExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedParts89: BinaryAssociation = BinaryAssociation(
    name="ownedParts89",
    ends={
        Property(name="essentialoclcs_MapLiteralPartCS", type=essentialoclcs_MapLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_MapLiteralExpCS", type=essentialoclcs_MapLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType90: BinaryAssociation = BinaryAssociation(
    name="ownedType90",
    ends={
        Property(name="essentialoclcs_MapTypeCS", type=essentialoclcs_MapLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_MapLiteralExpCS91", type=essentialoclcs_MapTypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedKey92: BinaryAssociation = BinaryAssociation(
    name="ownedKey92",
    ends={
        Property(name="essentialoclcs_ExpCS94", type=essentialoclcs_MapLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_MapLiteralPartCS93", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedValue95: BinaryAssociation = BinaryAssociation(
    name="ownedValue95",
    ends={
        Property(name="essentialoclcs_ExpCS97", type=essentialoclcs_MapLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_MapLiteralPartCS96", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRight117: BinaryAssociation = BinaryAssociation(
    name="ownedRight117",
    ends={
        Property(name="essentialoclcs_ExpCS119", type=essentialoclcs_OperatorExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_OperatorExpCS118", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source120: BinaryAssociation = BinaryAssociation(
    name="source120",
    ends={
        Property(name="essentialoclcs_ExpCS122", type=essentialoclcs_OperatorExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_OperatorExpCS121", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedInitExpression104: BinaryAssociation = BinaryAssociation(
    name="ownedInitExpression104",
    ends={
        Property(name="essentialoclcs_ExpCS105", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NavigatingArgCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedNameExpression106: BinaryAssociation = BinaryAssociation(
    name="ownedNameExpression106",
    ends={
        Property(name="essentialoclcs_ExpCS108", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NavigatingArgCS107", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType109: BinaryAssociation = BinaryAssociation(
    name="ownedType109",
    ends={
        Property(name="essentialoclcs_TypedRefCS111", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NavigatingArgCS110", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningRoundBracketedClause112: BinaryAssociation = BinaryAssociation(
    name="owningRoundBracketedClause112",
    ends={
        Property(name="RoundBracketedClauseCS113", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedArguments", type=essentialoclcs_RoundBracketedClauseCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedExpression114: BinaryAssociation = BinaryAssociation(
    name="ownedExpression114",
    ends={
        Property(name="essentialoclcs_ExpCS115", type=essentialoclcs_NestedExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NestedExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredOperation116: BinaryAssociation = BinaryAssociation(
    name="referredOperation116",
    ends={
        Property(name="essentialoclcs_Operation", type=essentialoclcs_OperationCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_OperationCallExpCS", type=essentialoclcs_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ownedInitExpression132: BinaryAssociation = BinaryAssociation(
    name="ownedInitExpression132",
    ends={
        Property(name="essentialoclcs_ExpCS134", type=essentialoclcs_ShadowPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ShadowPartCS133", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningCurlyBracketClause135: BinaryAssociation = BinaryAssociation(
    name="owningCurlyBracketClause135",
    ends={
        Property(name="CurlyBracketedClauseCS136", type=essentialoclcs_ShadowPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParts", type=essentialoclcs_CurlyBracketedClauseCS, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty137: BinaryAssociation = BinaryAssociation(
    name="referredProperty137",
    ends={
        Property(name="essentialoclcs_Property139", type=essentialoclcs_ShadowPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ShadowPartCS138", type=essentialoclcs_Property, multiplicity=Multiplicity(1, 1))
    }
)
ownedPatternType123: BinaryAssociation = BinaryAssociation(
    name="ownedPatternType123",
    ends={
        Property(name="essentialoclcs_TypeRefCS", type=essentialoclcs_PatternExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_PatternExpCS124", type=essentialoclcs_TypeRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredProperty125: BinaryAssociation = BinaryAssociation(
    name="referredProperty125",
    ends={
        Property(name="essentialoclcs_Property", type=essentialoclcs_PropertyCallExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_PropertyCallExpCS", type=essentialoclcs_Property, multiplicity=Multiplicity(0, 1))
    }
)
ownedArguments126: BinaryAssociation = BinaryAssociation(
    name="ownedArguments126",
    ends={
        Property(name="NavigatingArgCS", type=essentialoclcs_RoundBracketedClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningRoundBracketedClause", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningNameExp127: BinaryAssociation = BinaryAssociation(
    name="owningNameExp127",
    ends={
        Property(name="AbstractNameExpCS128", type=essentialoclcs_RoundBracketedClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRoundBracketedClause", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(0, 1))
    }
)
parts129: BinaryAssociation = BinaryAssociation(
    name="parts129",
    ends={
        Property(name="essentialoclcs_ShadowPartCS", type=essentialoclcs_ShadowExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ShadowExpCS", type=essentialoclcs_ShadowPartCS, multiplicity=Multiplicity(0, 9999))
    }
)
typeName130: BinaryAssociation = BinaryAssociation(
    name="typeName130",
    ends={
        Property(name="essentialoclcs_TypeNameExpCS", type=essentialoclcs_ShadowExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ShadowExpCS131", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedInitExpression161: BinaryAssociation = BinaryAssociation(
    name="ownedInitExpression161",
    ends={
        Property(name="essentialoclcs_ExpCS163", type=essentialoclcs_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_VariableCS162", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType164: BinaryAssociation = BinaryAssociation(
    name="ownedType164",
    ends={
        Property(name="essentialoclcs_TypedRefCS166", type=essentialoclcs_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_VariableCS165", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTerms140: BinaryAssociation = BinaryAssociation(
    name="ownedTerms140",
    ends={
        Property(name="essentialoclcs_ExpCS141", type=essentialoclcs_SquareBracketedClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_SquareBracketedClauseCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
owningNameExp142: BinaryAssociation = BinaryAssociation(
    name="owningNameExp142",
    ends={
        Property(name="AbstractNameExpCS143", type=essentialoclcs_SquareBracketedClauseCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSquareBracketedClauses", type=essentialoclcs_AbstractNameExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedParts144: BinaryAssociation = BinaryAssociation(
    name="ownedParts144",
    ends={
        Property(name="essentialoclcs_TupleLiteralPartCS", type=essentialoclcs_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TupleLiteralExpCS", type=essentialoclcs_TupleLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPathName145: BinaryAssociation = BinaryAssociation(
    name="ownedPathName145",
    ends={
        Property(name="essentialoclcs_PathNameCS146", type=essentialoclcs_TypeLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeLiteralExpCS", type=essentialoclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType147: BinaryAssociation = BinaryAssociation(
    name="ownedType147",
    ends={
        Property(name="essentialoclcs_TypedRefCS149", type=essentialoclcs_TypeLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeLiteralExpCS148", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element150: BinaryAssociation = BinaryAssociation(
    name="element150",
    ends={
        Property(name="essentialoclcs_Type152", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeNameExpCS151", type=essentialoclcs_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedCurlyBracketedClause153: BinaryAssociation = BinaryAssociation(
    name="ownedCurlyBracketedClause153",
    ends={
        Property(name="essentialoclcs_CurlyBracketedClauseCS", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeNameExpCS154", type=essentialoclcs_CurlyBracketedClauseCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPathName155: BinaryAssociation = BinaryAssociation(
    name="ownedPathName155",
    ends={
        Property(name="essentialoclcs_PathNameCS157", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeNameExpCS156", type=essentialoclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPatternGuard158: BinaryAssociation = BinaryAssociation(
    name="ownedPatternGuard158",
    ends={
        Property(name="essentialoclcs_ExpCS160", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeNameExpCS159", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable167: BinaryAssociation = BinaryAssociation(
    name="referredVariable167",
    ends={
        Property(name="essentialoclcs_Variable", type=essentialoclcs_VariableExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_VariableExpCS", type=essentialoclcs_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_essentialoclcs_AssociationClassCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=essentialoclcs_AssociationClassCallExpCS)
gen_essentialoclcs_BooleanLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_BooleanLiteralExpCS)
gen_essentialoclcs_AbstractNameExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_AbstractNameExpCS)
gen_essentialoclcs_CollectionTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=essentialoclcs_CollectionTypeCS)
gen_essentialoclcs_CollectionTypeCS_Nameable = Generalization(general=Nameable, specific=essentialoclcs_CollectionTypeCS)
gen_essentialoclcs_ContextCS_NamedElementCS = Generalization(general=NamedElementCS, specific=essentialoclcs_ContextCS)
gen_essentialoclcs_ContextCS_RootCS = Generalization(general=RootCS, specific=essentialoclcs_ContextCS)
gen_essentialoclcs_CallExpCS_AbstractNameExpCS = Generalization(general=AbstractNameExpCS, specific=essentialoclcs_CallExpCS)
gen_essentialoclcs_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_CollectionLiteralExpCS)
gen_essentialoclcs_CollectionLiteralPartCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_CollectionLiteralPartCS)
gen_essentialoclcs_CollectionPatternCS_TypedRefCS = Generalization(general=TypedRefCS, specific=essentialoclcs_CollectionPatternCS)
gen_essentialoclcs_CurlyBracketedClauseCS_ContextLessElementCS = Generalization(general=ContextLessElementCS, specific=essentialoclcs_CurlyBracketedClauseCS)
gen_essentialoclcs_ExpSpecificationCS_SpecificationCS = Generalization(general=SpecificationCS, specific=essentialoclcs_ExpSpecificationCS)
gen_essentialoclcs_IfExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_IfExpCS)
gen_essentialoclcs_ExpCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_ExpCS)
gen_essentialoclcs_IterationCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=essentialoclcs_IterationCallExpCS)
gen_essentialoclcs_LambdaLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_LambdaLiteralExpCS)
gen_essentialoclcs_IfThenExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_IfThenExpCS)
gen_essentialoclcs_InfixExpCS_OperatorExpCS = Generalization(general=OperatorExpCS, specific=essentialoclcs_InfixExpCS)
gen_essentialoclcs_InvalidLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_InvalidLiteralExpCS)
gen_essentialoclcs_IterateCallExpCS_IterationCallExpCS = Generalization(general=IterationCallExpCS, specific=essentialoclcs_IterateCallExpCS)
gen_essentialoclcs_MapTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=essentialoclcs_MapTypeCS)
gen_essentialoclcs_MapTypeCS_Nameable = Generalization(general=Nameable, specific=essentialoclcs_MapTypeCS)
gen_essentialoclcs_NameExpCS_AssociationClassCallExpCS = Generalization(general=AssociationClassCallExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NameExpCS_ShadowExpCS = Generalization(general=ShadowExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_LetExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_LetExpCS)
gen_essentialoclcs_LetVariableCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_LetVariableCS)
gen_essentialoclcs_LetVariableCS_VariableCS = Generalization(general=VariableCS, specific=essentialoclcs_LetVariableCS)
gen_essentialoclcs_LiteralExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_LiteralExpCS)
gen_essentialoclcs_MapLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_MapLiteralExpCS)
gen_essentialoclcs_MapLiteralPartCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_MapLiteralPartCS)
gen_essentialoclcs_OperatorExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_OperatorExpCS)
gen_essentialoclcs_OperatorExpCS_NamedElementCS = Generalization(general=NamedElementCS, specific=essentialoclcs_OperatorExpCS)
gen_essentialoclcs_NameExpCS_IterateCallExpCS = Generalization(general=IterateCallExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NameExpCS_IterationCallExpCS = Generalization(general=IterationCallExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NameExpCS_OperationCallExpCS = Generalization(general=OperationCallExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NameExpCS_PropertyCallExpCS = Generalization(general=PropertyCallExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NameExpCS_VariableExpCS = Generalization(general=VariableExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NavigatingArgCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_NavigatingArgCS)
gen_essentialoclcs_NestedExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_NestedExpCS)
gen_essentialoclcs_NullLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_NullLiteralExpCS)
gen_essentialoclcs_NumberLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_NumberLiteralExpCS)
gen_essentialoclcs_OperationCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=essentialoclcs_OperationCallExpCS)
gen_essentialoclcs_SquareBracketedClauseCS_ContextLessElementCS = Generalization(general=ContextLessElementCS, specific=essentialoclcs_SquareBracketedClauseCS)
gen_essentialoclcs_PatternExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_PatternExpCS)
gen_essentialoclcs_PrefixExpCS_OperatorExpCS = Generalization(general=OperatorExpCS, specific=essentialoclcs_PrefixExpCS)
gen_essentialoclcs_PrimitiveLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_PrimitiveLiteralExpCS)
gen_essentialoclcs_PropertyCallExpCS_CallExpCS = Generalization(general=CallExpCS, specific=essentialoclcs_PropertyCallExpCS)
gen_essentialoclcs_RoundBracketedClauseCS_ContextLessElementCS = Generalization(general=ContextLessElementCS, specific=essentialoclcs_RoundBracketedClauseCS)
gen_essentialoclcs_SelfExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_SelfExpCS)
gen_essentialoclcs_ShadowExpCS_AbstractNameExpCS = Generalization(general=AbstractNameExpCS, specific=essentialoclcs_ShadowExpCS)
gen_essentialoclcs_ShadowPartCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_ShadowPartCS)
gen_essentialoclcs_ShadowPartCS_Nameable = Generalization(general=Nameable, specific=essentialoclcs_ShadowPartCS)
gen_essentialoclcs_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_UnlimitedNaturalLiteralExpCS)
gen_essentialoclcs_VariableCS_NamedElementCS = Generalization(general=NamedElementCS, specific=essentialoclcs_VariableCS)
gen_essentialoclcs_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_StringLiteralExpCS)
gen_essentialoclcs_TupleLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_TupleLiteralExpCS)
gen_essentialoclcs_TupleLiteralPartCS_VariableCS = Generalization(general=VariableCS, specific=essentialoclcs_TupleLiteralPartCS)
gen_essentialoclcs_TypeLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_TypeLiteralExpCS)
gen_essentialoclcs_TypeNameExpCS_TypedRefCS = Generalization(general=TypedRefCS, specific=essentialoclcs_TypeNameExpCS)
gen_essentialoclcs_VariableExpCS_AbstractNameExpCS = Generalization(general=AbstractNameExpCS, specific=essentialoclcs_VariableExpCS)

# Domain Model
domain_model = DomainModel(
    name="essentialoclcs",
    types={essentialoclcs_AssociationClassCallExpCS, CallExpCS, essentialoclcs_AssociationClass, essentialoclcs_BooleanLiteralExpCS, PrimitiveLiteralExpCS, essentialoclcs_AbstractNameExpCS, ExpCS, essentialoclcs_CurlyBracketedClauseCS, essentialoclcs_PathNameCS, essentialoclcs_RoundBracketedClauseCS, essentialoclcs_SquareBracketedClauseCS, essentialoclcs_Type, Nameable, essentialoclcs_TypedRefCS, essentialoclcs_ContextCS, NamedElementCS, RootCS, essentialoclcs_CallExpCS, AbstractNameExpCS, essentialoclcs_ExpCS, essentialoclcs_CollectionLiteralExpCS, LiteralExpCS, essentialoclcs_CollectionLiteralPartCS, essentialoclcs_CollectionTypeCS, ModelElementCS, essentialoclcs_CollectionPatternCS, TypedRefCS, essentialoclcs_PatternExpCS, ContextLessElementCS, essentialoclcs_ShadowPartCS, essentialoclcs_Precedence, essentialoclcs_ExpSpecificationCS, SpecificationCS, essentialoclcs_IfExpCS, essentialoclcs_OperatorExpCS, essentialoclcs_IterationCallExpCS, essentialoclcs_Iteration, essentialoclcs_LambdaLiteralExpCS, essentialoclcs_IfThenExpCS, essentialoclcs_InfixExpCS, OperatorExpCS, essentialoclcs_InvalidLiteralExpCS, essentialoclcs_IterateCallExpCS, IterationCallExpCS, essentialoclcs_VariableCS, essentialoclcs_NameExpCS, AssociationClassCallExpCS, ShadowExpCS, IterateCallExpCS, essentialoclcs_LetExpCS, essentialoclcs_LetVariableCS, VariableCS, essentialoclcs_LiteralExpCS, essentialoclcs_MapLiteralExpCS, essentialoclcs_MapLiteralPartCS, essentialoclcs_MapTypeCS, OperationCallExpCS, PropertyCallExpCS, VariableExpCS, essentialoclcs_NavigatingArgCS, essentialoclcs_NestedExpCS, essentialoclcs_NullLiteralExpCS, essentialoclcs_NumberLiteralExpCS, essentialoclcs_OperationCallExpCS, essentialoclcs_Operation, essentialoclcs_TypeRefCS, essentialoclcs_PrefixExpCS, essentialoclcs_PrimitiveLiteralExpCS, essentialoclcs_PropertyCallExpCS, essentialoclcs_Property, essentialoclcs_SelfExpCS, essentialoclcs_ShadowExpCS, essentialoclcs_TypeNameExpCS, essentialoclcs_UnlimitedNaturalLiteralExpCS, essentialoclcs_StringLiteralExpCS, essentialoclcs_TupleLiteralExpCS, essentialoclcs_TupleLiteralPartCS, essentialoclcs_TypeLiteralExpCS, essentialoclcs_VariableExpCS, essentialoclcs_Variable, NavigationRole},
    associations={referredAssociation11, ownedCurlyBracketedClause0, ownedPathName1, ownedRoundBracketedClause2, ownedSquareBracketedClauses4, sourceType6, sourceTypeValue8, ownedType32, arguments12, source13, ownedParts16, ownedType17, ownedExpression19, ownedLastExpression22, ownedParts25, ownedPatternGuard26, ownedType29, ownedExpression34, ownedParts36, precedence52, ownedExpression54, owningNameExp37, localLeft39, localLeftmostDescendant42, localParent44, localRight47, localRightmostDescendant50, iterators78, referredIteration80, ownedExpressionCS82, ownedCondition56, ownedElseExpression58, ownedIfThenExpressions61, ownedThenExpression63, ownedCondition66, ownedThenExpression69, argument72, ownedLeft74, accumulators77, ownedKeyType98, ownedValueType101, ownedInExpression84, ownedVariables86, ownedRoundBracketedClause87, owningLetExpression88, ownedParts89, ownedType90, ownedKey92, ownedValue95, ownedRight117, source120, ownedInitExpression104, ownedNameExpression106, ownedType109, owningRoundBracketedClause112, ownedExpression114, referredOperation116, ownedInitExpression132, owningCurlyBracketClause135, referredProperty137, ownedPatternType123, referredProperty125, ownedArguments126, owningNameExp127, parts129, typeName130, ownedInitExpression161, ownedType164, ownedTerms140, owningNameExp142, ownedParts144, ownedPathName145, ownedType147, element150, ownedCurlyBracketedClause153, ownedPathName155, ownedPatternGuard158, referredVariable167},
    generalizations={gen_essentialoclcs_AssociationClassCallExpCS_CallExpCS, gen_essentialoclcs_BooleanLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_AbstractNameExpCS_ExpCS, gen_essentialoclcs_CollectionTypeCS_TypedRefCS, gen_essentialoclcs_CollectionTypeCS_Nameable, gen_essentialoclcs_ContextCS_NamedElementCS, gen_essentialoclcs_ContextCS_RootCS, gen_essentialoclcs_CallExpCS_AbstractNameExpCS, gen_essentialoclcs_CollectionLiteralExpCS_LiteralExpCS, gen_essentialoclcs_CollectionLiteralPartCS_ModelElementCS, gen_essentialoclcs_CollectionPatternCS_TypedRefCS, gen_essentialoclcs_CurlyBracketedClauseCS_ContextLessElementCS, gen_essentialoclcs_ExpSpecificationCS_SpecificationCS, gen_essentialoclcs_IfExpCS_ExpCS, gen_essentialoclcs_ExpCS_ModelElementCS, gen_essentialoclcs_IterationCallExpCS_CallExpCS, gen_essentialoclcs_LambdaLiteralExpCS_LiteralExpCS, gen_essentialoclcs_IfThenExpCS_ExpCS, gen_essentialoclcs_InfixExpCS_OperatorExpCS, gen_essentialoclcs_InvalidLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_IterateCallExpCS_IterationCallExpCS, gen_essentialoclcs_MapTypeCS_TypedRefCS, gen_essentialoclcs_MapTypeCS_Nameable, gen_essentialoclcs_NameExpCS_AssociationClassCallExpCS, gen_essentialoclcs_NameExpCS_ShadowExpCS, gen_essentialoclcs_LetExpCS_ExpCS, gen_essentialoclcs_LetVariableCS_ExpCS, gen_essentialoclcs_LetVariableCS_VariableCS, gen_essentialoclcs_LiteralExpCS_ExpCS, gen_essentialoclcs_MapLiteralExpCS_LiteralExpCS, gen_essentialoclcs_MapLiteralPartCS_ModelElementCS, gen_essentialoclcs_OperatorExpCS_ExpCS, gen_essentialoclcs_OperatorExpCS_NamedElementCS, gen_essentialoclcs_NameExpCS_IterateCallExpCS, gen_essentialoclcs_NameExpCS_IterationCallExpCS, gen_essentialoclcs_NameExpCS_OperationCallExpCS, gen_essentialoclcs_NameExpCS_PropertyCallExpCS, gen_essentialoclcs_NameExpCS_VariableExpCS, gen_essentialoclcs_NavigatingArgCS_ModelElementCS, gen_essentialoclcs_NestedExpCS_ExpCS, gen_essentialoclcs_NullLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_NumberLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_OperationCallExpCS_CallExpCS, gen_essentialoclcs_SquareBracketedClauseCS_ContextLessElementCS, gen_essentialoclcs_PatternExpCS_ExpCS, gen_essentialoclcs_PrefixExpCS_OperatorExpCS, gen_essentialoclcs_PrimitiveLiteralExpCS_LiteralExpCS, gen_essentialoclcs_PropertyCallExpCS_CallExpCS, gen_essentialoclcs_RoundBracketedClauseCS_ContextLessElementCS, gen_essentialoclcs_SelfExpCS_ExpCS, gen_essentialoclcs_ShadowExpCS_AbstractNameExpCS, gen_essentialoclcs_ShadowPartCS_ModelElementCS, gen_essentialoclcs_ShadowPartCS_Nameable, gen_essentialoclcs_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_VariableCS_NamedElementCS, gen_essentialoclcs_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_TupleLiteralExpCS_LiteralExpCS, gen_essentialoclcs_TupleLiteralPartCS_VariableCS, gen_essentialoclcs_TypeLiteralExpCS_LiteralExpCS, gen_essentialoclcs_TypeNameExpCS_TypedRefCS, gen_essentialoclcs_VariableExpCS_AbstractNameExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)