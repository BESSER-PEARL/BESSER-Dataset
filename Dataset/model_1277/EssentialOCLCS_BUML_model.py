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
TypedRefCS = Class(name="TypedRefCS")
Nameable = Class(name="Nameable")
essentialoclcs_TypedRefCS = Class(name="essentialoclcs::TypedRefCS")
essentialoclcs_AbstractNameExpCS = Class(name="essentialoclcs::AbstractNameExpCS", is_abstract=True)
ExpCS = Class(name="ExpCS")
essentialoclcs_BinaryOperatorCS = Class(name="essentialoclcs::BinaryOperatorCS")
OperatorCS = Class(name="OperatorCS")
essentialoclcs_ExpCS = Class(name="essentialoclcs::ExpCS")
essentialoclcs_BooleanLiteralExpCS = Class(name="essentialoclcs::BooleanLiteralExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
essentialoclcs_CollectionLiteralExpCS = Class(name="essentialoclcs::CollectionLiteralExpCS")
LiteralExpCS = Class(name="LiteralExpCS")
essentialoclcs_CollectionTypeCS = Class(name="essentialoclcs::CollectionTypeCS")
essentialoclcs_CollectionLiteralPartCS = Class(name="essentialoclcs::CollectionLiteralPartCS")
ModelElementCS = Class(name="ModelElementCS")
essentialoclcs_ConstructorExpCS = Class(name="essentialoclcs::ConstructorExpCS")
NamedExpCS = Class(name="NamedExpCS")
essentialoclcs_ConstructorPartCS = Class(name="essentialoclcs::ConstructorPartCS")
essentialoclcs_Property = Class(name="essentialoclcs::Property")
essentialoclcs_ContextCS = Class(name="essentialoclcs::ContextCS")
NamedElementCS = Class(name="NamedElementCS")
RootCS = Class(name="RootCS")
essentialoclcs_OperatorCS = Class(name="essentialoclcs::OperatorCS", is_abstract=True)
essentialoclcs_ExpSpecificationCS = Class(name="essentialoclcs::ExpSpecificationCS")
SpecificationCS = Class(name="SpecificationCS")
essentialoclcs_IfExpCS = Class(name="essentialoclcs::IfExpCS")
essentialoclcs_IndexExpCS = Class(name="essentialoclcs::IndexExpCS")
essentialoclcs_InfixExpCS = Class(name="essentialoclcs::InfixExpCS")
essentialoclcs_InvalidLiteralExpCS = Class(name="essentialoclcs::InvalidLiteralExpCS")
essentialoclcs_InvocationExpCS = Class(name="essentialoclcs::InvocationExpCS")
essentialoclcs_NavigatingArgCS = Class(name="essentialoclcs::NavigatingArgCS")
essentialoclcs_LetExpCS = Class(name="essentialoclcs::LetExpCS")
essentialoclcs_LetVariableCS = Class(name="essentialoclcs::LetVariableCS")
VariableCS = Class(name="VariableCS")
essentialoclcs_LiteralExpCS = Class(name="essentialoclcs::LiteralExpCS")
essentialoclcs_NameExpCS = Class(name="essentialoclcs::NameExpCS")
AbstractNameExpCS = Class(name="AbstractNameExpCS")
essentialoclcs_PathNameCS = Class(name="essentialoclcs::PathNameCS")
essentialoclcs_NamedExpCS = Class(name="essentialoclcs::NamedExpCS", is_abstract=True)
essentialoclcs_TypeLiteralExpCS = Class(name="essentialoclcs::TypeLiteralExpCS")
essentialoclcs_NavigationOperatorCS = Class(name="essentialoclcs::NavigationOperatorCS")
BinaryOperatorCS = Class(name="BinaryOperatorCS")
essentialoclcs_NestedExpCS = Class(name="essentialoclcs::NestedExpCS")
essentialoclcs_NullLiteralExpCS = Class(name="essentialoclcs::NullLiteralExpCS")
essentialoclcs_NumberLiteralExpCS = Class(name="essentialoclcs::NumberLiteralExpCS")
essentialoclcs_PrefixExpCS = Class(name="essentialoclcs::PrefixExpCS")
essentialoclcs_UnaryOperatorCS = Class(name="essentialoclcs::UnaryOperatorCS")
essentialoclcs_PrimitiveLiteralExpCS = Class(name="essentialoclcs::PrimitiveLiteralExpCS")
essentialoclcs_SelfExpCS = Class(name="essentialoclcs::SelfExpCS")
essentialoclcs_StringLiteralExpCS = Class(name="essentialoclcs::StringLiteralExpCS")
essentialoclcs_TupleLiteralExpCS = Class(name="essentialoclcs::TupleLiteralExpCS")
essentialoclcs_TupleLiteralPartCS = Class(name="essentialoclcs::TupleLiteralPartCS")
essentialoclcs_TypeNameExpCS = Class(name="essentialoclcs::TypeNameExpCS")
essentialoclcs_Type = Class(name="essentialoclcs::Type")
essentialoclcs_UnlimitedNaturalLiteralExpCS = Class(name="essentialoclcs::UnlimitedNaturalLiteralExpCS")
essentialoclcs_VariableCS = Class(name="essentialoclcs::VariableCS")

# TypedRefCS class attributes and methods

# Nameable class attributes and methods

# essentialoclcs_TypedRefCS class attributes and methods

# essentialoclcs_AbstractNameExpCS class attributes and methods
essentialoclcs_AbstractNameExpCS_m_getNamedElement: Method = Method(name="getNamedElement", parameters={}, type=StringType)
essentialoclcs_AbstractNameExpCS_m_getNameExp: Method = Method(name="getNameExp", parameters={}, type=StringType)
essentialoclcs_AbstractNameExpCS_m_getPathName: Method = Method(name="getPathName", parameters={}, type=StringType)
essentialoclcs_AbstractNameExpCS.methods={essentialoclcs_AbstractNameExpCS_m_getPathName, essentialoclcs_AbstractNameExpCS_m_getNamedElement, essentialoclcs_AbstractNameExpCS_m_getNameExp}

# ExpCS class attributes and methods

# essentialoclcs_BinaryOperatorCS class attributes and methods

# OperatorCS class attributes and methods

# essentialoclcs_ExpCS class attributes and methods

# essentialoclcs_BooleanLiteralExpCS class attributes and methods
essentialoclcs_BooleanLiteralExpCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_BooleanLiteralExpCS.attributes={essentialoclcs_BooleanLiteralExpCS_name}

# PrimitiveLiteralExpCS class attributes and methods

# essentialoclcs_CollectionLiteralExpCS class attributes and methods

# LiteralExpCS class attributes and methods

# essentialoclcs_CollectionTypeCS class attributes and methods
essentialoclcs_CollectionTypeCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_CollectionTypeCS.attributes={essentialoclcs_CollectionTypeCS_name}

# essentialoclcs_CollectionLiteralPartCS class attributes and methods

# ModelElementCS class attributes and methods

# essentialoclcs_ConstructorExpCS class attributes and methods
essentialoclcs_ConstructorExpCS_value: Property = Property(name="value", type=StringType)
essentialoclcs_ConstructorExpCS.attributes={essentialoclcs_ConstructorExpCS_value}

# NamedExpCS class attributes and methods

# essentialoclcs_ConstructorPartCS class attributes and methods

# essentialoclcs_Property class attributes and methods

# essentialoclcs_ContextCS class attributes and methods

# NamedElementCS class attributes and methods

# RootCS class attributes and methods

# essentialoclcs_OperatorCS class attributes and methods

# essentialoclcs_ExpSpecificationCS class attributes and methods

# SpecificationCS class attributes and methods

# essentialoclcs_IfExpCS class attributes and methods

# essentialoclcs_IndexExpCS class attributes and methods
essentialoclcs_IndexExpCS_atPre: Property = Property(name="atPre", type=BooleanType)
essentialoclcs_IndexExpCS.attributes={essentialoclcs_IndexExpCS_atPre}

# essentialoclcs_InfixExpCS class attributes and methods

# essentialoclcs_InvalidLiteralExpCS class attributes and methods

# essentialoclcs_InvocationExpCS class attributes and methods

# essentialoclcs_NavigatingArgCS class attributes and methods
essentialoclcs_NavigatingArgCS_role: Property = Property(name="role", type=StringType)
essentialoclcs_NavigatingArgCS_prefix: Property = Property(name="prefix", type=StringType)
essentialoclcs_NavigatingArgCS.attributes={essentialoclcs_NavigatingArgCS_role, essentialoclcs_NavigatingArgCS_prefix}

# essentialoclcs_LetExpCS class attributes and methods

# essentialoclcs_LetVariableCS class attributes and methods

# VariableCS class attributes and methods

# essentialoclcs_LiteralExpCS class attributes and methods

# essentialoclcs_NameExpCS class attributes and methods
essentialoclcs_NameExpCS_atPre: Property = Property(name="atPre", type=BooleanType)
essentialoclcs_NameExpCS.attributes={essentialoclcs_NameExpCS_atPre}

# AbstractNameExpCS class attributes and methods

# essentialoclcs_PathNameCS class attributes and methods

# essentialoclcs_NamedExpCS class attributes and methods

# essentialoclcs_TypeLiteralExpCS class attributes and methods

# essentialoclcs_NavigationOperatorCS class attributes and methods

# BinaryOperatorCS class attributes and methods

# essentialoclcs_NestedExpCS class attributes and methods

# essentialoclcs_NullLiteralExpCS class attributes and methods

# essentialoclcs_NumberLiteralExpCS class attributes and methods
essentialoclcs_NumberLiteralExpCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_NumberLiteralExpCS.attributes={essentialoclcs_NumberLiteralExpCS_name}

# essentialoclcs_PrefixExpCS class attributes and methods

# essentialoclcs_UnaryOperatorCS class attributes and methods

# essentialoclcs_PrimitiveLiteralExpCS class attributes and methods

# essentialoclcs_SelfExpCS class attributes and methods
essentialoclcs_SelfExpCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_SelfExpCS.attributes={essentialoclcs_SelfExpCS_name}

# essentialoclcs_StringLiteralExpCS class attributes and methods
essentialoclcs_StringLiteralExpCS_name: Property = Property(name="name", type=StringType)
essentialoclcs_StringLiteralExpCS.attributes={essentialoclcs_StringLiteralExpCS_name}

# essentialoclcs_TupleLiteralExpCS class attributes and methods

# essentialoclcs_TupleLiteralPartCS class attributes and methods

# essentialoclcs_TypeNameExpCS class attributes and methods

# essentialoclcs_Type class attributes and methods

# essentialoclcs_UnlimitedNaturalLiteralExpCS class attributes and methods

# essentialoclcs_VariableCS class attributes and methods

# Relationships
argument0: BinaryAssociation = BinaryAssociation(
    name="argument0",
    ends={
        Property(name="essentialoclcs_ExpCS", type=essentialoclcs_BinaryOperatorCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_BinaryOperatorCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1))
    }
)
ownedType1: BinaryAssociation = BinaryAssociation(
    name="ownedType1",
    ends={
        Property(name="essentialoclcs_CollectionTypeCS", type=essentialoclcs_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralExpCS", type=essentialoclcs_CollectionTypeCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts2: BinaryAssociation = BinaryAssociation(
    name="ownedParts2",
    ends={
        Property(name="essentialoclcs_CollectionLiteralPartCS", type=essentialoclcs_CollectionLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralExpCS3", type=essentialoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionCS4: BinaryAssociation = BinaryAssociation(
    name="expressionCS4",
    ends={
        Property(name="essentialoclcs_ExpCS6", type=essentialoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralPartCS5", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastExpressionCS7: BinaryAssociation = BinaryAssociation(
    name="lastExpressionCS7",
    ends={
        Property(name="essentialoclcs_ExpCS9", type=essentialoclcs_CollectionLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionLiteralPartCS8", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstIndexes32: BinaryAssociation = BinaryAssociation(
    name="firstIndexes32",
    ends={
        Property(name="essentialoclcs_ExpCS33", type=essentialoclcs_IndexExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IndexExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
secondIndexes34: BinaryAssociation = BinaryAssociation(
    name="secondIndexes34",
    ends={
        Property(name="essentialoclcs_ExpCS36", type=essentialoclcs_IndexExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IndexExpCS35", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType10: BinaryAssociation = BinaryAssociation(
    name="ownedType10",
    ends={
        Property(name="essentialoclcs_TypedRefCS", type=essentialoclcs_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_CollectionTypeCS11", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts12: BinaryAssociation = BinaryAssociation(
    name="ownedParts12",
    ends={
        Property(name="essentialoclcs_ConstructorPartCS", type=essentialoclcs_ConstructorExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ConstructorExpCS", type=essentialoclcs_ConstructorPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property13: BinaryAssociation = BinaryAssociation(
    name="property13",
    ends={
        Property(name="essentialoclcs_Property", type=essentialoclcs_ConstructorPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ConstructorPartCS14", type=essentialoclcs_Property, multiplicity=Multiplicity(1, 1))
    }
)
initExpression15: BinaryAssociation = BinaryAssociation(
    name="initExpression15",
    ends={
        Property(name="essentialoclcs_ExpCS17", type=essentialoclcs_ConstructorPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ConstructorPartCS16", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedExpression18: BinaryAssociation = BinaryAssociation(
    name="ownedExpression18",
    ends={
        Property(name="essentialoclcs_ExpCS19", type=essentialoclcs_ContextCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ContextCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent20: BinaryAssociation = BinaryAssociation(
    name="parent20",
    ends={
        Property(name="essentialoclcs_OperatorCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpCS21", type=essentialoclcs_OperatorCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedExpression22: BinaryAssociation = BinaryAssociation(
    name="ownedExpression22",
    ends={
        Property(name="essentialoclcs_ExpCS23", type=essentialoclcs_ExpSpecificationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_ExpSpecificationCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="essentialoclcs_ExpCS25", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression26: BinaryAssociation = BinaryAssociation(
    name="thenExpression26",
    ends={
        Property(name="essentialoclcs_ExpCS28", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS27", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression29: BinaryAssociation = BinaryAssociation(
    name="elseExpression29",
    ends={
        Property(name="essentialoclcs_ExpCS31", type=essentialoclcs_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_IfExpCS30", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExpression37: BinaryAssociation = BinaryAssociation(
    name="ownedExpression37",
    ends={
        Property(name="essentialoclcs_ExpCS38", type=essentialoclcs_InfixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_InfixExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
ownedOperator39: BinaryAssociation = BinaryAssociation(
    name="ownedOperator39",
    ends={
        Property(name="essentialoclcs_BinaryOperatorCS41", type=essentialoclcs_InfixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_InfixExpCS40", type=essentialoclcs_BinaryOperatorCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
argument42: BinaryAssociation = BinaryAssociation(
    name="argument42",
    ends={
        Property(name="NavigatingArgCS", type=essentialoclcs_InvocationExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="navigatingExp", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable43: BinaryAssociation = BinaryAssociation(
    name="variable43",
    ends={
        Property(name="LetVariableCS", type=essentialoclcs_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="letExpression", type=essentialoclcs_LetVariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in44: BinaryAssociation = BinaryAssociation(
    name="in44",
    ends={
        Property(name="essentialoclcs_ExpCS45", type=essentialoclcs_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_LetExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExpression46: BinaryAssociation = BinaryAssociation(
    name="letExpression46",
    ends={
        Property(name="LetExpCS", type=essentialoclcs_LetVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=essentialoclcs_LetExpCS, multiplicity=Multiplicity(0, 1))
    }
)
pathName47: BinaryAssociation = BinaryAssociation(
    name="pathName47",
    ends={
        Property(name="essentialoclcs_PathNameCS", type=essentialoclcs_NameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NameExpCS", type=essentialoclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameExp48: BinaryAssociation = BinaryAssociation(
    name="nameExp48",
    ends={
        Property(name="essentialoclcs_NameExpCS49", type=essentialoclcs_NamedExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NamedExpCS", type=essentialoclcs_NameExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
navigatingExp50: BinaryAssociation = BinaryAssociation(
    name="navigatingExp50",
    ends={
        Property(name="InvocationExpCS", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="argument", type=essentialoclcs_InvocationExpCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedType69: BinaryAssociation = BinaryAssociation(
    name="ownedType69",
    ends={
        Property(name="essentialoclcs_TypedRefCS70", type=essentialoclcs_TypeLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeLiteralExpCS", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name51: BinaryAssociation = BinaryAssociation(
    name="name51",
    ends={
        Property(name="essentialoclcs_ExpCS52", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NavigatingArgCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType53: BinaryAssociation = BinaryAssociation(
    name="ownedType53",
    ends={
        Property(name="essentialoclcs_TypedRefCS55", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NavigatingArgCS54", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init56: BinaryAssociation = BinaryAssociation(
    name="init56",
    ends={
        Property(name="essentialoclcs_ExpCS58", type=essentialoclcs_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NavigatingArgCS57", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source59: BinaryAssociation = BinaryAssociation(
    name="source59",
    ends={
        Property(name="essentialoclcs_ExpCS60", type=essentialoclcs_NestedExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_NestedExpCS", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source61: BinaryAssociation = BinaryAssociation(
    name="source61",
    ends={
        Property(name="essentialoclcs_ExpCS63", type=essentialoclcs_OperatorCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_OperatorCS62", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(1, 1))
    }
)
ownedOperator64: BinaryAssociation = BinaryAssociation(
    name="ownedOperator64",
    ends={
        Property(name="essentialoclcs_UnaryOperatorCS", type=essentialoclcs_PrefixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_PrefixExpCS", type=essentialoclcs_UnaryOperatorCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpression65: BinaryAssociation = BinaryAssociation(
    name="ownedExpression65",
    ends={
        Property(name="essentialoclcs_ExpCS67", type=essentialoclcs_PrefixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_PrefixExpCS66", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts68: BinaryAssociation = BinaryAssociation(
    name="ownedParts68",
    ends={
        Property(name="essentialoclcs_TupleLiteralPartCS", type=essentialoclcs_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TupleLiteralExpCS", type=essentialoclcs_TupleLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName71: BinaryAssociation = BinaryAssociation(
    name="pathName71",
    ends={
        Property(name="essentialoclcs_PathNameCS72", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeNameExpCS", type=essentialoclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element73: BinaryAssociation = BinaryAssociation(
    name="element73",
    ends={
        Property(name="essentialoclcs_Type", type=essentialoclcs_TypeNameExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_TypeNameExpCS74", type=essentialoclcs_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedType75: BinaryAssociation = BinaryAssociation(
    name="ownedType75",
    ends={
        Property(name="essentialoclcs_TypedRefCS76", type=essentialoclcs_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_VariableCS", type=essentialoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression77: BinaryAssociation = BinaryAssociation(
    name="initExpression77",
    ends={
        Property(name="essentialoclcs_ExpCS79", type=essentialoclcs_VariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialoclcs_VariableCS78", type=essentialoclcs_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_essentialoclcs_CollectionTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=essentialoclcs_CollectionTypeCS)
gen_essentialoclcs_CollectionTypeCS_Nameable = Generalization(general=Nameable, specific=essentialoclcs_CollectionTypeCS)
gen_essentialoclcs_AbstractNameExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_AbstractNameExpCS)
gen_essentialoclcs_BinaryOperatorCS_OperatorCS = Generalization(general=OperatorCS, specific=essentialoclcs_BinaryOperatorCS)
gen_essentialoclcs_BooleanLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_BooleanLiteralExpCS)
gen_essentialoclcs_CollectionLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_CollectionLiteralExpCS)
gen_essentialoclcs_CollectionLiteralPartCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_CollectionLiteralPartCS)
gen_essentialoclcs_IndexExpCS_NamedExpCS = Generalization(general=NamedExpCS, specific=essentialoclcs_IndexExpCS)
gen_essentialoclcs_ConstructorExpCS_NamedExpCS = Generalization(general=NamedExpCS, specific=essentialoclcs_ConstructorExpCS)
gen_essentialoclcs_ConstructorPartCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_ConstructorPartCS)
gen_essentialoclcs_ConstructorPartCS_Nameable = Generalization(general=Nameable, specific=essentialoclcs_ConstructorPartCS)
gen_essentialoclcs_ContextCS_NamedElementCS = Generalization(general=NamedElementCS, specific=essentialoclcs_ContextCS)
gen_essentialoclcs_ContextCS_RootCS = Generalization(general=RootCS, specific=essentialoclcs_ContextCS)
gen_essentialoclcs_ExpCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_ExpCS)
gen_essentialoclcs_ExpSpecificationCS_SpecificationCS = Generalization(general=SpecificationCS, specific=essentialoclcs_ExpSpecificationCS)
gen_essentialoclcs_IfExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_IfExpCS)
gen_essentialoclcs_InfixExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_InfixExpCS)
gen_essentialoclcs_InvalidLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_InvalidLiteralExpCS)
gen_essentialoclcs_InvocationExpCS_NamedExpCS = Generalization(general=NamedExpCS, specific=essentialoclcs_InvocationExpCS)
gen_essentialoclcs_LetExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_LetExpCS)
gen_essentialoclcs_LetVariableCS_VariableCS = Generalization(general=VariableCS, specific=essentialoclcs_LetVariableCS)
gen_essentialoclcs_LetVariableCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_LetVariableCS)
gen_essentialoclcs_LiteralExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_LiteralExpCS)
gen_essentialoclcs_NameExpCS_AbstractNameExpCS = Generalization(general=AbstractNameExpCS, specific=essentialoclcs_NameExpCS)
gen_essentialoclcs_NamedExpCS_AbstractNameExpCS = Generalization(general=AbstractNameExpCS, specific=essentialoclcs_NamedExpCS)
gen_essentialoclcs_TupleLiteralPartCS_VariableCS = Generalization(general=VariableCS, specific=essentialoclcs_TupleLiteralPartCS)
gen_essentialoclcs_NavigatingArgCS_ModelElementCS = Generalization(general=ModelElementCS, specific=essentialoclcs_NavigatingArgCS)
gen_essentialoclcs_TypeLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_TypeLiteralExpCS)
gen_essentialoclcs_NavigationOperatorCS_BinaryOperatorCS = Generalization(general=BinaryOperatorCS, specific=essentialoclcs_NavigationOperatorCS)
gen_essentialoclcs_NestedExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_NestedExpCS)
gen_essentialoclcs_NullLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_NullLiteralExpCS)
gen_essentialoclcs_NumberLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_NumberLiteralExpCS)
gen_essentialoclcs_OperatorCS_NamedElementCS = Generalization(general=NamedElementCS, specific=essentialoclcs_OperatorCS)
gen_essentialoclcs_OperatorCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_OperatorCS)
gen_essentialoclcs_PrefixExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_PrefixExpCS)
gen_essentialoclcs_PrimitiveLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_PrimitiveLiteralExpCS)
gen_essentialoclcs_SelfExpCS_ExpCS = Generalization(general=ExpCS, specific=essentialoclcs_SelfExpCS)
gen_essentialoclcs_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_StringLiteralExpCS)
gen_essentialoclcs_TupleLiteralExpCS_LiteralExpCS = Generalization(general=LiteralExpCS, specific=essentialoclcs_TupleLiteralExpCS)
gen_essentialoclcs_TypeNameExpCS_TypedRefCS = Generalization(general=TypedRefCS, specific=essentialoclcs_TypeNameExpCS)
gen_essentialoclcs_UnaryOperatorCS_OperatorCS = Generalization(general=OperatorCS, specific=essentialoclcs_UnaryOperatorCS)
gen_essentialoclcs_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=essentialoclcs_UnlimitedNaturalLiteralExpCS)
gen_essentialoclcs_VariableCS_NamedElementCS = Generalization(general=NamedElementCS, specific=essentialoclcs_VariableCS)

# Domain Model
domain_model = DomainModel(
    name="essentialoclcs",
    types={TypedRefCS, Nameable, essentialoclcs_TypedRefCS, essentialoclcs_AbstractNameExpCS, ExpCS, essentialoclcs_BinaryOperatorCS, OperatorCS, essentialoclcs_ExpCS, essentialoclcs_BooleanLiteralExpCS, PrimitiveLiteralExpCS, essentialoclcs_CollectionLiteralExpCS, LiteralExpCS, essentialoclcs_CollectionTypeCS, essentialoclcs_CollectionLiteralPartCS, ModelElementCS, essentialoclcs_ConstructorExpCS, NamedExpCS, essentialoclcs_ConstructorPartCS, essentialoclcs_Property, essentialoclcs_ContextCS, NamedElementCS, RootCS, essentialoclcs_OperatorCS, essentialoclcs_ExpSpecificationCS, SpecificationCS, essentialoclcs_IfExpCS, essentialoclcs_IndexExpCS, essentialoclcs_InfixExpCS, essentialoclcs_InvalidLiteralExpCS, essentialoclcs_InvocationExpCS, essentialoclcs_NavigatingArgCS, essentialoclcs_LetExpCS, essentialoclcs_LetVariableCS, VariableCS, essentialoclcs_LiteralExpCS, essentialoclcs_NameExpCS, AbstractNameExpCS, essentialoclcs_PathNameCS, essentialoclcs_NamedExpCS, essentialoclcs_TypeLiteralExpCS, essentialoclcs_NavigationOperatorCS, BinaryOperatorCS, essentialoclcs_NestedExpCS, essentialoclcs_NullLiteralExpCS, essentialoclcs_NumberLiteralExpCS, essentialoclcs_PrefixExpCS, essentialoclcs_UnaryOperatorCS, essentialoclcs_PrimitiveLiteralExpCS, essentialoclcs_SelfExpCS, essentialoclcs_StringLiteralExpCS, essentialoclcs_TupleLiteralExpCS, essentialoclcs_TupleLiteralPartCS, essentialoclcs_TypeNameExpCS, essentialoclcs_Type, essentialoclcs_UnlimitedNaturalLiteralExpCS, essentialoclcs_VariableCS, NavigationRole},
    associations={argument0, ownedType1, ownedParts2, expressionCS4, lastExpressionCS7, firstIndexes32, secondIndexes34, ownedType10, ownedParts12, property13, initExpression15, ownedExpression18, parent20, ownedExpression22, condition24, thenExpression26, elseExpression29, ownedExpression37, ownedOperator39, argument42, variable43, in44, letExpression46, pathName47, nameExp48, navigatingExp50, ownedType69, name51, ownedType53, init56, source59, source61, ownedOperator64, ownedExpression65, ownedParts68, pathName71, element73, ownedType75, initExpression77},
    generalizations={gen_essentialoclcs_CollectionTypeCS_TypedRefCS, gen_essentialoclcs_CollectionTypeCS_Nameable, gen_essentialoclcs_AbstractNameExpCS_ExpCS, gen_essentialoclcs_BinaryOperatorCS_OperatorCS, gen_essentialoclcs_BooleanLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_CollectionLiteralExpCS_LiteralExpCS, gen_essentialoclcs_CollectionLiteralPartCS_ModelElementCS, gen_essentialoclcs_IndexExpCS_NamedExpCS, gen_essentialoclcs_ConstructorExpCS_NamedExpCS, gen_essentialoclcs_ConstructorPartCS_ModelElementCS, gen_essentialoclcs_ConstructorPartCS_Nameable, gen_essentialoclcs_ContextCS_NamedElementCS, gen_essentialoclcs_ContextCS_RootCS, gen_essentialoclcs_ExpCS_ModelElementCS, gen_essentialoclcs_ExpSpecificationCS_SpecificationCS, gen_essentialoclcs_IfExpCS_ExpCS, gen_essentialoclcs_InfixExpCS_ExpCS, gen_essentialoclcs_InvalidLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_InvocationExpCS_NamedExpCS, gen_essentialoclcs_LetExpCS_ExpCS, gen_essentialoclcs_LetVariableCS_VariableCS, gen_essentialoclcs_LetVariableCS_ExpCS, gen_essentialoclcs_LiteralExpCS_ExpCS, gen_essentialoclcs_NameExpCS_AbstractNameExpCS, gen_essentialoclcs_NamedExpCS_AbstractNameExpCS, gen_essentialoclcs_TupleLiteralPartCS_VariableCS, gen_essentialoclcs_NavigatingArgCS_ModelElementCS, gen_essentialoclcs_TypeLiteralExpCS_LiteralExpCS, gen_essentialoclcs_NavigationOperatorCS_BinaryOperatorCS, gen_essentialoclcs_NestedExpCS_ExpCS, gen_essentialoclcs_NullLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_NumberLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_OperatorCS_NamedElementCS, gen_essentialoclcs_OperatorCS_ExpCS, gen_essentialoclcs_PrefixExpCS_ExpCS, gen_essentialoclcs_PrimitiveLiteralExpCS_LiteralExpCS, gen_essentialoclcs_SelfExpCS_ExpCS, gen_essentialoclcs_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_TupleLiteralExpCS_LiteralExpCS, gen_essentialoclcs_TypeNameExpCS_TypedRefCS, gen_essentialoclcs_UnaryOperatorCS_OperatorCS, gen_essentialoclcs_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS, gen_essentialoclcs_VariableCS_NamedElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)