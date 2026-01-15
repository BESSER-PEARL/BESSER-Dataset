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
myAtl_Module = Class(name="myAtl::Module")
myAtl_ModuleElement = Class(name="myAtl::ModuleElement")
myAtl_MatchedRule = Class(name="myAtl::MatchedRule")
ModuleElement = Class(name="ModuleElement")
myAtl_InPattern = Class(name="myAtl::InPattern")
myAtl_RuleVariableDeclaration = Class(name="myAtl::RuleVariableDeclaration")
myAtl_NameExpCS = Class(name="myAtl::NameExpCS")
myAtl_QueryRule = Class(name="myAtl::QueryRule")
myAtl_OutPattern = Class(name="myAtl::OutPattern")
myAtl_ActionBlock = Class(name="myAtl::ActionBlock")
myAtl_CalledRule = Class(name="myAtl::CalledRule")
myAtl_ExpCS = Class(name="myAtl::ExpCS")
myAtl_Helper = Class(name="myAtl::Helper")
myAtl_ATLParameterCS = Class(name="myAtl::ATLParameterCS")
myAtl_ATLType = Class(name="myAtl::ATLType")
myAtl_ATLDefCS = Class(name="myAtl::ATLDefCS")
myAtl_InPatternElement = Class(name="myAtl::InPatternElement")
myAtl_SimpleOutPatternElement = Class(name="myAtl::SimpleOutPatternElement")
OutPatternElement = Class(name="OutPatternElement")
myAtl_OutPatternElement = Class(name="myAtl::OutPatternElement")
myAtl_Binding = Class(name="myAtl::Binding")
myAtl_ForEachOutPatternElement = Class(name="myAtl::ForEachOutPatternElement")
myAtl_TypeExpCS = Class(name="myAtl::TypeExpCS")
myAtl_CollectionTypeCS = Class(name="myAtl::CollectionTypeCS")
TypeLiteralCS = Class(name="TypeLiteralCS")
myAtl_Statement = Class(name="myAtl::Statement")
myAtl_BindingStat = Class(name="myAtl::BindingStat")
Statement = Class(name="Statement")
PrimaryExpCS = Class(name="PrimaryExpCS")
myAtl_TupleLiteralExpCS = Class(name="myAtl::TupleLiteralExpCS")
myAtl_TupleLiteralPartCS = Class(name="myAtl::TupleLiteralPartCS")
myAtl_NumberLiteralExpCS = Class(name="myAtl::NumberLiteralExpCS")
myAtl_TupleTypeCS = Class(name="myAtl::TupleTypeCS")
myAtl_tuplePartCS = Class(name="myAtl::tuplePartCS")
myAtl_PrimitiveLiteralExpCS = Class(name="myAtl::PrimitiveLiteralExpCS")
myAtl_NullLiteralExpCS = Class(name="myAtl::NullLiteralExpCS")
myAtl_PrimitiveTypeCS = Class(name="myAtl::PrimitiveTypeCS")
myAtl_TypeLiteralCS = Class(name="myAtl::TypeLiteralCS")
TypeExpCS = Class(name="TypeExpCS")
myAtl_TypeLiteralExpCS = Class(name="myAtl::TypeLiteralExpCS")
myAtl_TypeNameExpCS = Class(name="myAtl::TypeNameExpCS")
PrimitiveLiteralExpCS = Class(name="PrimitiveLiteralExpCS")
myAtl_StringLiteralExpCS = Class(name="myAtl::StringLiteralExpCS")
myAtl_BooleanLiteralExpCS = Class(name="myAtl::BooleanLiteralExpCS")
myAtl_UnlimitedNaturalLiteralExpCS = Class(name="myAtl::UnlimitedNaturalLiteralExpCS")
myAtl_InvalidLiteralExpCS = Class(name="myAtl::InvalidLiteralExpCS")
myAtl_NavigatingBarArgCS = Class(name="myAtl::NavigatingBarArgCS")
myAtl_NavigatingCommaArgCS = Class(name="myAtl::NavigatingCommaArgCS")
myAtl_NavigatingArgCS = Class(name="myAtl::NavigatingArgCS")
myAtl_NavigatingArgExpCS = Class(name="myAtl::NavigatingArgExpCS")
myAtl_LetExpCS = Class(name="myAtl::LetExpCS")
myAtl_LetVariableCS = Class(name="myAtl::LetVariableCS")
myAtl_NavigatingSemiArgCS = Class(name="myAtl::NavigatingSemiArgCS")
myAtl_IfExpCS = Class(name="myAtl::IfExpCS")
myAtl_BinaryOperatorCS = Class(name="myAtl::BinaryOperatorCS")
myAtl_InfixOperatorCS = Class(name="myAtl::InfixOperatorCS")
BinaryOperatorCS = Class(name="BinaryOperatorCS")
myAtl_NavigationOperatorCS = Class(name="myAtl::NavigationOperatorCS")
myAtl_PrefixedExpCS = Class(name="myAtl::PrefixedExpCS")
InfixedExpCS = Class(name="InfixedExpCS")
myAtl_UnaryOperatorCS = Class(name="myAtl::UnaryOperatorCS")
myAtl_IndexExpCS = Class(name="myAtl::IndexExpCS")
NavigatingExpCS_Base = Class(name="NavigatingExpCS::Base")
myAtl_NavigatingExpCS_Base = Class(name="myAtl::NavigatingExpCS::Base")
NavigatingExpCS = Class(name="NavigatingExpCS")
myAtl_NavigatingExpCS = Class(name="myAtl::NavigatingExpCS")
myAtl_NestedExpCS = Class(name="myAtl::NestedExpCS")
myAtl_SelfExpCS = Class(name="myAtl::SelfExpCS")
myAtl_PrimaryExpCS = Class(name="myAtl::PrimaryExpCS")
PrefixedExpCS = Class(name="PrefixedExpCS")
myAtl_StringExpCs = Class(name="myAtl::StringExpCs")
IndexExpCS = Class(name="IndexExpCS")
NavigatingArgExpCS = Class(name="NavigatingArgExpCS")
myAtl_InfixedExpCS = Class(name="myAtl::InfixedExpCS")
ExpCS = Class(name="ExpCS")
myAtl_EObject = Class(name="myAtl::EObject")
myAtl_InfixExpCS = Class(name="myAtl::InfixExpCS")
myAtl_PrefixExpCS = Class(name="myAtl::PrefixExpCS")

# myAtl_Module class attributes and methods
myAtl_Module_name: Property = Property(name="name", type=StringType)
myAtl_Module.attributes={myAtl_Module_name}

# myAtl_ModuleElement class attributes and methods
myAtl_ModuleElement_name: Property = Property(name="name", type=StringType)
myAtl_ModuleElement.attributes={myAtl_ModuleElement_name}

# myAtl_MatchedRule class attributes and methods

# ModuleElement class attributes and methods

# myAtl_InPattern class attributes and methods

# myAtl_RuleVariableDeclaration class attributes and methods
myAtl_RuleVariableDeclaration_varName: Property = Property(name="varName", type=StringType)
myAtl_RuleVariableDeclaration.attributes={myAtl_RuleVariableDeclaration_varName}

# myAtl_NameExpCS class attributes and methods
myAtl_NameExpCS_namespace: Property = Property(name="namespace", type=StringType)
myAtl_NameExpCS_element: Property = Property(name="element", type=StringType)
myAtl_NameExpCS.attributes={myAtl_NameExpCS_element, myAtl_NameExpCS_namespace}

# myAtl_QueryRule class attributes and methods

# myAtl_OutPattern class attributes and methods

# myAtl_ActionBlock class attributes and methods

# myAtl_CalledRule class attributes and methods

# myAtl_ExpCS class attributes and methods

# myAtl_Helper class attributes and methods

# myAtl_ATLParameterCS class attributes and methods
myAtl_ATLParameterCS_varName: Property = Property(name="varName", type=StringType)
myAtl_ATLParameterCS.attributes={myAtl_ATLParameterCS_varName}

# myAtl_ATLType class attributes and methods
myAtl_ATLType_modelName: Property = Property(name="modelName", type=StringType)
myAtl_ATLType.attributes={myAtl_ATLType_modelName}

# myAtl_ATLDefCS class attributes and methods
myAtl_ATLDefCS_varName: Property = Property(name="varName", type=StringType)
myAtl_ATLDefCS.attributes={myAtl_ATLDefCS_varName}

# myAtl_InPatternElement class attributes and methods
myAtl_InPatternElement_varName: Property = Property(name="varName", type=StringType)
myAtl_InPatternElement.attributes={myAtl_InPatternElement_varName}

# myAtl_SimpleOutPatternElement class attributes and methods
myAtl_SimpleOutPatternElement_varName: Property = Property(name="varName", type=StringType)
myAtl_SimpleOutPatternElement.attributes={myAtl_SimpleOutPatternElement_varName}

# OutPatternElement class attributes and methods

# myAtl_OutPatternElement class attributes and methods

# myAtl_Binding class attributes and methods
myAtl_Binding_propertyName: Property = Property(name="propertyName", type=StringType)
myAtl_Binding.attributes={myAtl_Binding_propertyName}

# myAtl_ForEachOutPatternElement class attributes and methods

# myAtl_TypeExpCS class attributes and methods

# myAtl_CollectionTypeCS class attributes and methods

# TypeLiteralCS class attributes and methods

# myAtl_Statement class attributes and methods

# myAtl_BindingStat class attributes and methods
myAtl_BindingStat_propertyName: Property = Property(name="propertyName", type=StringType)
myAtl_BindingStat.attributes={myAtl_BindingStat_propertyName}

# Statement class attributes and methods

# PrimaryExpCS class attributes and methods

# myAtl_TupleLiteralExpCS class attributes and methods

# myAtl_TupleLiteralPartCS class attributes and methods
myAtl_TupleLiteralPartCS_name: Property = Property(name="name", type=StringType)
myAtl_TupleLiteralPartCS.attributes={myAtl_TupleLiteralPartCS_name}

# myAtl_NumberLiteralExpCS class attributes and methods
myAtl_NumberLiteralExpCS_name: Property = Property(name="name", type=StringType)
myAtl_NumberLiteralExpCS.attributes={myAtl_NumberLiteralExpCS_name}

# myAtl_TupleTypeCS class attributes and methods
myAtl_TupleTypeCS_backtrack: Property = Property(name="backtrack", type=StringType)
myAtl_TupleTypeCS.attributes={myAtl_TupleTypeCS_backtrack}

# myAtl_tuplePartCS class attributes and methods
myAtl_tuplePartCS_name: Property = Property(name="name", type=StringType)
myAtl_tuplePartCS.attributes={myAtl_tuplePartCS_name}

# myAtl_PrimitiveLiteralExpCS class attributes and methods

# myAtl_NullLiteralExpCS class attributes and methods

# myAtl_PrimitiveTypeCS class attributes and methods

# myAtl_TypeLiteralCS class attributes and methods
myAtl_TypeLiteralCS_name: Property = Property(name="name", type=StringType)
myAtl_TypeLiteralCS.attributes={myAtl_TypeLiteralCS_name}

# TypeExpCS class attributes and methods

# myAtl_TypeLiteralExpCS class attributes and methods

# myAtl_TypeNameExpCS class attributes and methods
myAtl_TypeNameExpCS_namespace: Property = Property(name="namespace", type=StringType)
myAtl_TypeNameExpCS_element: Property = Property(name="element", type=StringType)
myAtl_TypeNameExpCS.attributes={myAtl_TypeNameExpCS_element, myAtl_TypeNameExpCS_namespace}

# PrimitiveLiteralExpCS class attributes and methods

# myAtl_StringLiteralExpCS class attributes and methods
myAtl_StringLiteralExpCS_name: Property = Property(name="name", type=StringType)
myAtl_StringLiteralExpCS.attributes={myAtl_StringLiteralExpCS_name}

# myAtl_BooleanLiteralExpCS class attributes and methods
myAtl_BooleanLiteralExpCS_name: Property = Property(name="name", type=StringType)
myAtl_BooleanLiteralExpCS.attributes={myAtl_BooleanLiteralExpCS_name}

# myAtl_UnlimitedNaturalLiteralExpCS class attributes and methods

# myAtl_InvalidLiteralExpCS class attributes and methods

# myAtl_NavigatingBarArgCS class attributes and methods
myAtl_NavigatingBarArgCS_prefix: Property = Property(name="prefix", type=StringType)
myAtl_NavigatingBarArgCS.attributes={myAtl_NavigatingBarArgCS_prefix}

# myAtl_NavigatingCommaArgCS class attributes and methods
myAtl_NavigatingCommaArgCS_prefix: Property = Property(name="prefix", type=StringType)
myAtl_NavigatingCommaArgCS.attributes={myAtl_NavigatingCommaArgCS_prefix}

# myAtl_NavigatingArgCS class attributes and methods

# myAtl_NavigatingArgExpCS class attributes and methods

# myAtl_LetExpCS class attributes and methods

# myAtl_LetVariableCS class attributes and methods
myAtl_LetVariableCS_name: Property = Property(name="name", type=StringType)
myAtl_LetVariableCS.attributes={myAtl_LetVariableCS_name}

# myAtl_NavigatingSemiArgCS class attributes and methods
myAtl_NavigatingSemiArgCS_prefix: Property = Property(name="prefix", type=StringType)
myAtl_NavigatingSemiArgCS.attributes={myAtl_NavigatingSemiArgCS_prefix}

# myAtl_IfExpCS class attributes and methods

# myAtl_BinaryOperatorCS class attributes and methods
myAtl_BinaryOperatorCS_name: Property = Property(name="name", type=StringType)
myAtl_BinaryOperatorCS.attributes={myAtl_BinaryOperatorCS_name}

# myAtl_InfixOperatorCS class attributes and methods

# BinaryOperatorCS class attributes and methods

# myAtl_NavigationOperatorCS class attributes and methods

# myAtl_PrefixedExpCS class attributes and methods

# InfixedExpCS class attributes and methods

# myAtl_UnaryOperatorCS class attributes and methods
myAtl_UnaryOperatorCS_name: Property = Property(name="name", type=StringType)
myAtl_UnaryOperatorCS.attributes={myAtl_UnaryOperatorCS_name}

# myAtl_IndexExpCS class attributes and methods

# NavigatingExpCS_Base class attributes and methods

# myAtl_NavigatingExpCS_Base class attributes and methods

# NavigatingExpCS class attributes and methods

# myAtl_NavigatingExpCS class attributes and methods

# myAtl_NestedExpCS class attributes and methods

# myAtl_SelfExpCS class attributes and methods

# myAtl_PrimaryExpCS class attributes and methods

# PrefixedExpCS class attributes and methods

# myAtl_StringExpCs class attributes and methods
myAtl_StringExpCs_name: Property = Property(name="name", type=StringType)
myAtl_StringExpCs.attributes={myAtl_StringExpCs_name}

# IndexExpCS class attributes and methods

# NavigatingArgExpCS class attributes and methods

# myAtl_InfixedExpCS class attributes and methods

# ExpCS class attributes and methods

# myAtl_EObject class attributes and methods

# myAtl_InfixExpCS class attributes and methods

# myAtl_PrefixExpCS class attributes and methods

# Relationships
elements7: BinaryAssociation = BinaryAssociation(
    name="elements7",
    ends={
        Property(name="myAtl_ModuleElement", type=myAtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_Module8", type=myAtl_ModuleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inPattern9: BinaryAssociation = BinaryAssociation(
    name="inPattern9",
    ends={
        Property(name="myAtl_InPattern", type=myAtl_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_MatchedRule", type=myAtl_InPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables10: BinaryAssociation = BinaryAssociation(
    name="variables10",
    ends={
        Property(name="myAtl_RuleVariableDeclaration", type=myAtl_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_MatchedRule11", type=myAtl_RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outModels0: BinaryAssociation = BinaryAssociation(
    name="outModels0",
    ends={
        Property(name="myAtl_NameExpCS", type=myAtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_Module", type=myAtl_NameExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inModels1: BinaryAssociation = BinaryAssociation(
    name="inModels1",
    ends={
        Property(name="myAtl_NameExpCS3", type=myAtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_Module2", type=myAtl_NameExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varName4: BinaryAssociation = BinaryAssociation(
    name="varName4",
    ends={
        Property(name="myAtl_NameExpCS6", type=myAtl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_Module5", type=myAtl_NameExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock21: BinaryAssociation = BinaryAssociation(
    name="actionBlock21",
    ends={
        Property(name="myAtl_ActionBlock23", type=myAtl_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_CalledRule22", type=myAtl_ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outPattern12: BinaryAssociation = BinaryAssociation(
    name="outPattern12",
    ends={
        Property(name="myAtl_OutPattern", type=myAtl_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_MatchedRule13", type=myAtl_OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionBlock14: BinaryAssociation = BinaryAssociation(
    name="actionBlock14",
    ends={
        Property(name="myAtl_ActionBlock", type=myAtl_MatchedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_MatchedRule15", type=myAtl_ActionBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables16: BinaryAssociation = BinaryAssociation(
    name="variables16",
    ends={
        Property(name="myAtl_RuleVariableDeclaration17", type=myAtl_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_CalledRule", type=myAtl_RuleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outPattern18: BinaryAssociation = BinaryAssociation(
    name="outPattern18",
    ends={
        Property(name="myAtl_OutPattern20", type=myAtl_CalledRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_CalledRule19", type=myAtl_OutPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression25: BinaryAssociation = BinaryAssociation(
    name="initExpression25",
    ends={
        Property(name="myAtl_ExpCS", type=myAtl_QueryRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_QueryRule26", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="myAtl_ATLParameterCS", type=myAtl_QueryRule, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_QueryRule", type=myAtl_ATLParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters28: BinaryAssociation = BinaryAssociation(
    name="parameters28",
    ends={
        Property(name="myAtl_ATLParameterCS30", type=myAtl_ATLDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ATLDefCS29", type=myAtl_ATLParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition27: BinaryAssociation = BinaryAssociation(
    name="definition27",
    ends={
        Property(name="myAtl_ATLDefCS", type=myAtl_Helper, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_Helper", type=myAtl_ATLDefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="myAtl_ATLType38", type=myAtl_ATLParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ATLParameterCS37", type=myAtl_ATLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="myAtl_ATLType", type=myAtl_ATLDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ATLDefCS32", type=myAtl_ATLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression33: BinaryAssociation = BinaryAssociation(
    name="initExpression33",
    ends={
        Property(name="myAtl_ExpCS35", type=myAtl_ATLDefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ATLDefCS34", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression42: BinaryAssociation = BinaryAssociation(
    name="initExpression42",
    ends={
        Property(name="myAtl_ExpCS44", type=myAtl_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_RuleVariableDeclaration43", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="myAtl_ATLType41", type=myAtl_RuleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_RuleVariableDeclaration40", type=myAtl_ATLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements45: BinaryAssociation = BinaryAssociation(
    name="elements45",
    ends={
        Property(name="myAtl_InPatternElement", type=myAtl_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_InPattern46", type=myAtl_InPatternElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filter47: BinaryAssociation = BinaryAssociation(
    name="filter47",
    ends={
        Property(name="myAtl_ExpCS49", type=myAtl_InPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_InPattern48", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="myAtl_ATLType52", type=myAtl_InPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_InPatternElement51", type=myAtl_ATLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements53: BinaryAssociation = BinaryAssociation(
    name="elements53",
    ends={
        Property(name="myAtl_OutPatternElement", type=myAtl_OutPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_OutPattern54", type=myAtl_OutPatternElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings57: BinaryAssociation = BinaryAssociation(
    name="bindings57",
    ends={
        Property(name="myAtl_Binding", type=myAtl_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_SimpleOutPatternElement58", type=myAtl_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="myAtl_ATLType56", type=myAtl_SimpleOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_SimpleOutPatternElement", type=myAtl_ATLType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="myAtl_ExpCS63", type=myAtl_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_Binding62", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection59: BinaryAssociation = BinaryAssociation(
    name="collection59",
    ends={
        Property(name="myAtl_ExpCS60", type=myAtl_ForEachOutPatternElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ForEachOutPatternElement", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source66: BinaryAssociation = BinaryAssociation(
    name="source66",
    ends={
        Property(name="myAtl_BindingStat", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myAtl_ExpCS67", type=myAtl_BindingStat, multiplicity=Multiplicity(1, 1))
    }
)
value68: BinaryAssociation = BinaryAssociation(
    name="value68",
    ends={
        Property(name="myAtl_ExpCS70", type=myAtl_BindingStat, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_BindingStat69", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="myAtl_TypeExpCS", type=myAtl_ATLType, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ATLType72", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements64: BinaryAssociation = BinaryAssociation(
    name="statements64",
    ends={
        Property(name="myAtl_Statement", type=myAtl_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_ActionBlock65", type=myAtl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParts79: BinaryAssociation = BinaryAssociation(
    name="ownedParts79",
    ends={
        Property(name="myAtl_TupleLiteralPartCS", type=myAtl_TupleLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_TupleLiteralExpCS", type=myAtl_TupleLiteralPartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType80: BinaryAssociation = BinaryAssociation(
    name="ownedType80",
    ends={
        Property(name="myAtl_TypeExpCS82", type=myAtl_TupleLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_TupleLiteralPartCS81", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression83: BinaryAssociation = BinaryAssociation(
    name="initExpression83",
    ends={
        Property(name="myAtl_ExpCS85", type=myAtl_TupleLiteralPartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_TupleLiteralPartCS84", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType73: BinaryAssociation = BinaryAssociation(
    name="ownedType73",
    ends={
        Property(name="myAtl_TypeExpCS74", type=myAtl_CollectionTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_CollectionTypeCS", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts75: BinaryAssociation = BinaryAssociation(
    name="ownedParts75",
    ends={
        Property(name="myAtl_tuplePartCS", type=myAtl_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_TupleTypeCS", type=myAtl_tuplePartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType76: BinaryAssociation = BinaryAssociation(
    name="ownedType76",
    ends={
        Property(name="myAtl_TypeExpCS78", type=myAtl_tuplePartCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_tuplePartCS77", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType86: BinaryAssociation = BinaryAssociation(
    name="ownedType86",
    ends={
        Property(name="myAtl_TypeLiteralCS", type=myAtl_TypeLiteralExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_TypeLiteralExpCS", type=myAtl_TypeLiteralCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType88: BinaryAssociation = BinaryAssociation(
    name="ownedType88",
    ends={
        Property(name="myAtl_TypeExpCS90", type=myAtl_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingArgCS89", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init91: BinaryAssociation = BinaryAssociation(
    name="init91",
    ends={
        Property(name="myAtl_ExpCS93", type=myAtl_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingArgCS92", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name94: BinaryAssociation = BinaryAssociation(
    name="name94",
    ends={
        Property(name="myAtl_NavigatingArgExpCS95", type=myAtl_NavigatingBarArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingBarArgCS", type=myAtl_NavigatingArgExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType96: BinaryAssociation = BinaryAssociation(
    name="ownedType96",
    ends={
        Property(name="myAtl_TypeExpCS98", type=myAtl_NavigatingBarArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingBarArgCS97", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init99: BinaryAssociation = BinaryAssociation(
    name="init99",
    ends={
        Property(name="myAtl_ExpCS101", type=myAtl_NavigatingBarArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingBarArgCS100", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name87: BinaryAssociation = BinaryAssociation(
    name="name87",
    ends={
        Property(name="myAtl_NavigatingArgExpCS", type=myAtl_NavigatingArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingArgCS", type=myAtl_NavigatingArgExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition118: BinaryAssociation = BinaryAssociation(
    name="condition118",
    ends={
        Property(name="myAtl_ExpCS119", type=myAtl_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_IfExpCS", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpression120: BinaryAssociation = BinaryAssociation(
    name="thenExpression120",
    ends={
        Property(name="myAtl_ExpCS122", type=myAtl_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_IfExpCS121", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression123: BinaryAssociation = BinaryAssociation(
    name="elseExpression123",
    ends={
        Property(name="myAtl_ExpCS125", type=myAtl_IfExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_IfExpCS124", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable126: BinaryAssociation = BinaryAssociation(
    name="variable126",
    ends={
        Property(name="myAtl_LetVariableCS", type=myAtl_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_LetExpCS", type=myAtl_LetVariableCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in127: BinaryAssociation = BinaryAssociation(
    name="in127",
    ends={
        Property(name="myAtl_ExpCS129", type=myAtl_LetExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_LetExpCS128", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType130: BinaryAssociation = BinaryAssociation(
    name="ownedType130",
    ends={
        Property(name="myAtl_TypeExpCS132", type=myAtl_LetVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_LetVariableCS131", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression133: BinaryAssociation = BinaryAssociation(
    name="initExpression133",
    ends={
        Property(name="myAtl_ExpCS135", type=myAtl_LetVariableCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_LetVariableCS134", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name102: BinaryAssociation = BinaryAssociation(
    name="name102",
    ends={
        Property(name="myAtl_NavigatingArgExpCS103", type=myAtl_NavigatingCommaArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingCommaArgCS", type=myAtl_NavigatingArgExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType104: BinaryAssociation = BinaryAssociation(
    name="ownedType104",
    ends={
        Property(name="myAtl_TypeExpCS106", type=myAtl_NavigatingCommaArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingCommaArgCS105", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init107: BinaryAssociation = BinaryAssociation(
    name="init107",
    ends={
        Property(name="myAtl_ExpCS109", type=myAtl_NavigatingCommaArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingCommaArgCS108", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name110: BinaryAssociation = BinaryAssociation(
    name="name110",
    ends={
        Property(name="myAtl_NavigatingArgExpCS111", type=myAtl_NavigatingSemiArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingSemiArgCS", type=myAtl_NavigatingArgExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType112: BinaryAssociation = BinaryAssociation(
    name="ownedType112",
    ends={
        Property(name="myAtl_TypeExpCS114", type=myAtl_NavigatingSemiArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingSemiArgCS113", type=myAtl_TypeExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init115: BinaryAssociation = BinaryAssociation(
    name="init115",
    ends={
        Property(name="myAtl_ExpCS117", type=myAtl_NavigatingSemiArgCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingSemiArgCS116", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstIndexes138: BinaryAssociation = BinaryAssociation(
    name="firstIndexes138",
    ends={
        Property(name="myAtl_ExpCS139", type=myAtl_IndexExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_IndexExpCS", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
secondIndexes140: BinaryAssociation = BinaryAssociation(
    name="secondIndexes140",
    ends={
        Property(name="myAtl_ExpCS142", type=myAtl_IndexExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_IndexExpCS141", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namedExp143: BinaryAssociation = BinaryAssociation(
    name="namedExp143",
    ends={
        Property(name="myAtl_NavigatingExpCS_Base", type=myAtl_NavigatingExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingExpCS", type=myAtl_NavigatingExpCS_Base, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source136: BinaryAssociation = BinaryAssociation(
    name="source136",
    ends={
        Property(name="myAtl_ExpCS137", type=myAtl_NestedExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NestedExpCS", type=myAtl_ExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument144: BinaryAssociation = BinaryAssociation(
    name="argument144",
    ends={
        Property(name="myAtl_EObject", type=myAtl_NavigatingExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_NavigatingExpCS145", type=myAtl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpression146: BinaryAssociation = BinaryAssociation(
    name="ownedExpression146",
    ends={
        Property(name="myAtl_PrefixedExpCS", type=myAtl_InfixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_InfixExpCS", type=myAtl_PrefixedExpCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperator147: BinaryAssociation = BinaryAssociation(
    name="ownedOperator147",
    ends={
        Property(name="myAtl_BinaryOperatorCS", type=myAtl_InfixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_InfixExpCS148", type=myAtl_BinaryOperatorCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperator149: BinaryAssociation = BinaryAssociation(
    name="ownedOperator149",
    ends={
        Property(name="myAtl_UnaryOperatorCS", type=myAtl_PrefixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_PrefixExpCS", type=myAtl_UnaryOperatorCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpression150: BinaryAssociation = BinaryAssociation(
    name="ownedExpression150",
    ends={
        Property(name="myAtl_PrimaryExpCS", type=myAtl_PrefixExpCS, multiplicity=Multiplicity(1, 1)),
        Property(name="myAtl_PrefixExpCS151", type=myAtl_PrimaryExpCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myAtl_MatchedRule_ModuleElement = Generalization(general=ModuleElement, specific=myAtl_MatchedRule)
gen_myAtl_QueryRule_ModuleElement = Generalization(general=ModuleElement, specific=myAtl_QueryRule)
gen_myAtl_CalledRule_ModuleElement = Generalization(general=ModuleElement, specific=myAtl_CalledRule)
gen_myAtl_Helper_ModuleElement = Generalization(general=ModuleElement, specific=myAtl_Helper)
gen_myAtl_SimpleOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=myAtl_SimpleOutPatternElement)
gen_myAtl_ForEachOutPatternElement_OutPatternElement = Generalization(general=OutPatternElement, specific=myAtl_ForEachOutPatternElement)
gen_myAtl_CollectionTypeCS_TypeLiteralCS = Generalization(general=TypeLiteralCS, specific=myAtl_CollectionTypeCS)
gen_myAtl_BindingStat_Statement = Generalization(general=Statement, specific=myAtl_BindingStat)
gen_myAtl_PrimitiveLiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_PrimitiveLiteralExpCS)
gen_myAtl_TupleLiteralExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_TupleLiteralExpCS)
gen_myAtl_TupleTypeCS_TypeLiteralCS = Generalization(general=TypeLiteralCS, specific=myAtl_TupleTypeCS)
gen_myAtl_InvalidLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=myAtl_InvalidLiteralExpCS)
gen_myAtl_NullLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=myAtl_NullLiteralExpCS)
gen_myAtl_PrimitiveTypeCS_TypeLiteralCS = Generalization(general=TypeLiteralCS, specific=myAtl_PrimitiveTypeCS)
gen_myAtl_TypeLiteralCS_TypeExpCS = Generalization(general=TypeExpCS, specific=myAtl_TypeLiteralCS)
gen_myAtl_TypeNameExpCS_TypeExpCS = Generalization(general=TypeExpCS, specific=myAtl_TypeNameExpCS)
gen_myAtl_NumberLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=myAtl_NumberLiteralExpCS)
gen_myAtl_StringLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=myAtl_StringLiteralExpCS)
gen_myAtl_BooleanLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=myAtl_BooleanLiteralExpCS)
gen_myAtl_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS = Generalization(general=PrimitiveLiteralExpCS, specific=myAtl_UnlimitedNaturalLiteralExpCS)
gen_myAtl_LetExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_LetExpCS)
gen_myAtl_IfExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_IfExpCS)
gen_myAtl_InfixOperatorCS_BinaryOperatorCS = Generalization(general=BinaryOperatorCS, specific=myAtl_InfixOperatorCS)
gen_myAtl_NavigationOperatorCS_BinaryOperatorCS = Generalization(general=BinaryOperatorCS, specific=myAtl_NavigationOperatorCS)
gen_myAtl_PrefixedExpCS_InfixedExpCS = Generalization(general=InfixedExpCS, specific=myAtl_PrefixedExpCS)
gen_myAtl_IndexExpCS_NavigatingExpCS_Base = Generalization(general=NavigatingExpCS_Base, specific=myAtl_IndexExpCS)
gen_myAtl_NavigatingExpCS_Base_NavigatingExpCS = Generalization(general=NavigatingExpCS, specific=myAtl_NavigatingExpCS_Base)
gen_myAtl_NavigatingExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_NavigatingExpCS)
gen_myAtl_NestedExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_NestedExpCS)
gen_myAtl_SelfExpCS_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_SelfExpCS)
gen_myAtl_PrimaryExpCS_PrefixedExpCS = Generalization(general=PrefixedExpCS, specific=myAtl_PrimaryExpCS)
gen_myAtl_StringExpCs_PrimaryExpCS = Generalization(general=PrimaryExpCS, specific=myAtl_StringExpCs)
gen_myAtl_NameExpCS_IndexExpCS = Generalization(general=IndexExpCS, specific=myAtl_NameExpCS)
gen_myAtl_ExpCS_NavigatingArgExpCS = Generalization(general=NavigatingArgExpCS, specific=myAtl_ExpCS)
gen_myAtl_InfixedExpCS_ExpCS = Generalization(general=ExpCS, specific=myAtl_InfixedExpCS)
gen_myAtl_InfixExpCS_InfixedExpCS = Generalization(general=InfixedExpCS, specific=myAtl_InfixExpCS)
gen_myAtl_PrefixExpCS_PrefixedExpCS = Generalization(general=PrefixedExpCS, specific=myAtl_PrefixExpCS)

# Domain Model
domain_model = DomainModel(
    name="myAtl",
    types={myAtl_Module, myAtl_ModuleElement, myAtl_MatchedRule, ModuleElement, myAtl_InPattern, myAtl_RuleVariableDeclaration, myAtl_NameExpCS, myAtl_QueryRule, myAtl_OutPattern, myAtl_ActionBlock, myAtl_CalledRule, myAtl_ExpCS, myAtl_Helper, myAtl_ATLParameterCS, myAtl_ATLType, myAtl_ATLDefCS, myAtl_InPatternElement, myAtl_SimpleOutPatternElement, OutPatternElement, myAtl_OutPatternElement, myAtl_Binding, myAtl_ForEachOutPatternElement, myAtl_TypeExpCS, myAtl_CollectionTypeCS, TypeLiteralCS, myAtl_Statement, myAtl_BindingStat, Statement, PrimaryExpCS, myAtl_TupleLiteralExpCS, myAtl_TupleLiteralPartCS, myAtl_NumberLiteralExpCS, myAtl_TupleTypeCS, myAtl_tuplePartCS, myAtl_PrimitiveLiteralExpCS, myAtl_NullLiteralExpCS, myAtl_PrimitiveTypeCS, myAtl_TypeLiteralCS, TypeExpCS, myAtl_TypeLiteralExpCS, myAtl_TypeNameExpCS, PrimitiveLiteralExpCS, myAtl_StringLiteralExpCS, myAtl_BooleanLiteralExpCS, myAtl_UnlimitedNaturalLiteralExpCS, myAtl_InvalidLiteralExpCS, myAtl_NavigatingBarArgCS, myAtl_NavigatingCommaArgCS, myAtl_NavigatingArgCS, myAtl_NavigatingArgExpCS, myAtl_LetExpCS, myAtl_LetVariableCS, myAtl_NavigatingSemiArgCS, myAtl_IfExpCS, myAtl_BinaryOperatorCS, myAtl_InfixOperatorCS, BinaryOperatorCS, myAtl_NavigationOperatorCS, myAtl_PrefixedExpCS, InfixedExpCS, myAtl_UnaryOperatorCS, myAtl_IndexExpCS, NavigatingExpCS_Base, myAtl_NavigatingExpCS_Base, NavigatingExpCS, myAtl_NavigatingExpCS, myAtl_NestedExpCS, myAtl_SelfExpCS, myAtl_PrimaryExpCS, PrefixedExpCS, myAtl_StringExpCs, IndexExpCS, NavigatingArgExpCS, myAtl_InfixedExpCS, ExpCS, myAtl_EObject, myAtl_InfixExpCS, myAtl_PrefixExpCS},
    associations={elements7, inPattern9, variables10, outModels0, inModels1, varName4, actionBlock21, outPattern12, actionBlock14, variables16, outPattern18, initExpression25, parameters24, parameters28, definition27, type36, type31, initExpression33, initExpression42, type39, elements45, filter47, type50, elements53, bindings57, type55, value61, collection59, source66, value68, type71, statements64, ownedParts79, ownedType80, initExpression83, ownedType73, ownedParts75, ownedType76, ownedType86, ownedType88, init91, name94, ownedType96, init99, name87, condition118, thenExpression120, elseExpression123, variable126, in127, ownedType130, initExpression133, name102, ownedType104, init107, name110, ownedType112, init115, firstIndexes138, secondIndexes140, namedExp143, source136, argument144, ownedExpression146, ownedOperator147, ownedOperator149, ownedExpression150},
    generalizations={gen_myAtl_MatchedRule_ModuleElement, gen_myAtl_QueryRule_ModuleElement, gen_myAtl_CalledRule_ModuleElement, gen_myAtl_Helper_ModuleElement, gen_myAtl_SimpleOutPatternElement_OutPatternElement, gen_myAtl_ForEachOutPatternElement_OutPatternElement, gen_myAtl_CollectionTypeCS_TypeLiteralCS, gen_myAtl_BindingStat_Statement, gen_myAtl_PrimitiveLiteralExpCS_PrimaryExpCS, gen_myAtl_TupleLiteralExpCS_PrimaryExpCS, gen_myAtl_TupleTypeCS_TypeLiteralCS, gen_myAtl_InvalidLiteralExpCS_PrimitiveLiteralExpCS, gen_myAtl_NullLiteralExpCS_PrimitiveLiteralExpCS, gen_myAtl_PrimitiveTypeCS_TypeLiteralCS, gen_myAtl_TypeLiteralCS_TypeExpCS, gen_myAtl_TypeNameExpCS_TypeExpCS, gen_myAtl_NumberLiteralExpCS_PrimitiveLiteralExpCS, gen_myAtl_StringLiteralExpCS_PrimitiveLiteralExpCS, gen_myAtl_BooleanLiteralExpCS_PrimitiveLiteralExpCS, gen_myAtl_UnlimitedNaturalLiteralExpCS_PrimitiveLiteralExpCS, gen_myAtl_LetExpCS_PrimaryExpCS, gen_myAtl_IfExpCS_PrimaryExpCS, gen_myAtl_InfixOperatorCS_BinaryOperatorCS, gen_myAtl_NavigationOperatorCS_BinaryOperatorCS, gen_myAtl_PrefixedExpCS_InfixedExpCS, gen_myAtl_IndexExpCS_NavigatingExpCS_Base, gen_myAtl_NavigatingExpCS_Base_NavigatingExpCS, gen_myAtl_NavigatingExpCS_PrimaryExpCS, gen_myAtl_NestedExpCS_PrimaryExpCS, gen_myAtl_SelfExpCS_PrimaryExpCS, gen_myAtl_PrimaryExpCS_PrefixedExpCS, gen_myAtl_StringExpCs_PrimaryExpCS, gen_myAtl_NameExpCS_IndexExpCS, gen_myAtl_ExpCS_NavigatingArgExpCS, gen_myAtl_InfixedExpCS_ExpCS, gen_myAtl_InfixExpCS_InfixedExpCS, gen_myAtl_PrefixExpCS_PrefixedExpCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)