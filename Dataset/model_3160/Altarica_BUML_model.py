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
PrimitiveTypeKind: Enumeration = Enumeration(
    name="PrimitiveTypeKind",
    literals={
            EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="BOOLEAN")
    }
)

FlowKind: Enumeration = Enumeration(
    name="FlowKind",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

# Classes
altarica_System = Class(name="altarica::System")
altarica_AbstractDeclaration = Class(name="altarica::AbstractDeclaration")
altarica_ConstantDefinition = Class(name="altarica::ConstantDefinition")
AbstractDeclaration = Class(name="AbstractDeclaration")
altarica_Constant = Class(name="altarica::Constant")
altarica_AbstractDefinitionConstant = Class(name="altarica::AbstractDefinitionConstant")
altarica_DomainConstant = Class(name="altarica::DomainConstant")
altarica_AbstractDomain = Class(name="altarica::AbstractDomain")
altarica_Domain = Class(name="altarica::Domain")
AbstractTypeRef = Class(name="AbstractTypeRef")
altarica_Range = Class(name="altarica::Range")
AbstractDomain = Class(name="AbstractDomain")
NonNavigableVariable = Class(name="NonNavigableVariable")
altarica_Expression = Class(name="altarica::Expression")
altarica_ExpressionConstant = Class(name="altarica::ExpressionConstant")
AbstractDefinitionConstant = Class(name="AbstractDefinitionConstant")
altarica_PrimitiveType = Class(name="altarica::PrimitiveType")
altarica_Node = Class(name="altarica::Node")
altarica_Enumeration = Class(name="altarica::Enumeration")
altarica_Literal = Class(name="altarica::Literal")
altarica_VariableAttribute = Class(name="altarica::VariableAttribute")
altarica_InitSpecification = Class(name="altarica::InitSpecification")
AbstractSpecification = Class(name="AbstractSpecification")
altarica_InitStatement = Class(name="altarica::InitStatement")
altarica_Affectation = Class(name="altarica::Affectation")
altarica_ExternalSpecification = Class(name="altarica::ExternalSpecification")
altarica_ExternalDirective = Class(name="altarica::ExternalDirective")
altarica_AbstractSpecification = Class(name="altarica::AbstractSpecification")
altarica_Flow = Class(name="altarica::Flow")
altarica_AbstractTypeRef = Class(name="altarica::AbstractTypeRef")
altarica_FlowSpecification = Class(name="altarica::FlowSpecification")
altarica_FlowDeclaration = Class(name="altarica::FlowDeclaration")
NavigableVariable = Class(name="NavigableVariable")
altarica_Priority = Class(name="altarica::Priority")
altarica_AbstractExpression = Class(name="altarica::AbstractExpression")
altarica_StateSpecification = Class(name="altarica::StateSpecification")
altarica_StateDeclaration = Class(name="altarica::StateDeclaration")
altarica_EventSpecification = Class(name="altarica::EventSpecification")
altarica_EventDeclaration = Class(name="altarica::EventDeclaration")
altarica_Event = Class(name="altarica::Event")
altarica_DomainRef = Class(name="altarica::DomainRef")
altarica_NodeInstanceSpecification = Class(name="altarica::NodeInstanceSpecification")
altarica_NodeInstanceDeclaration = Class(name="altarica::NodeInstanceDeclaration")
altarica_State = Class(name="altarica::State")
altarica_AssertSpecification = Class(name="altarica::AssertSpecification")
altarica_Assert = Class(name="altarica::Assert")
altarica_AbstractBooleanExpression = Class(name="altarica::AbstractBooleanExpression")
altarica_VectorSpecification = Class(name="altarica::VectorSpecification")
altarica_Vector = Class(name="altarica::Vector")
altarica_VectorParameter = Class(name="altarica::VectorParameter")
altarica_NodeInstance = Class(name="altarica::NodeInstance")
altarica_TransitionSpecification = Class(name="altarica::TransitionSpecification")
altarica_Transition = Class(name="altarica::Transition")
altarica_Cardinality = Class(name="altarica::Cardinality")
altarica_EventRef = Class(name="altarica::EventRef")
altarica_Switch = Class(name="altarica::Switch")
AbstractExpression = Class(name="AbstractExpression")
AbstractBooleanExpression = Class(name="AbstractBooleanExpression")
altarica_CaseExpression = Class(name="altarica::CaseExpression")
altarica_NavigableVariable = Class(name="altarica::NavigableVariable")
altarica_VariableRef = Class(name="altarica::VariableRef")
Expression = Class(name="Expression")
altarica_IfThenElse = Class(name="altarica::IfThenElse")
altarica_EObject = Class(name="altarica::EObject")
altarica_EString = Class(name="altarica::EString")
altarica_EInteger = Class(name="altarica::EInteger")
altarica_Addition = Class(name="altarica::Addition")
altarica_NonNavigableVariable = Class(name="altarica::NonNavigableVariable")
altarica_EBoolean = Class(name="altarica::EBoolean")
altarica_Multiplication = Class(name="altarica::Multiplication")
altarica_Division = Class(name="altarica::Division")
altarica_Minus = Class(name="altarica::Minus")
altarica_Or = Class(name="altarica::Or")
altarica_Equal = Class(name="altarica::Equal")
altarica_And = Class(name="altarica::And")
altarica_StrictLower = Class(name="altarica::StrictLower")
altarica_Lower = Class(name="altarica::Lower")
altarica_NotEqual = Class(name="altarica::NotEqual")
altarica_Upper = Class(name="altarica::Upper")
altarica_StrictUpper = Class(name="altarica::StrictUpper")
altarica_NestedQualifiedEventRef = Class(name="altarica::NestedQualifiedEventRef")
EventRef = Class(name="EventRef")
altarica_NestedQualifiedVariableRef = Class(name="altarica::NestedQualifiedVariableRef")
VariableRef = Class(name="VariableRef")
altarica_Imply = Class(name="altarica::Imply")

# altarica_System class attributes and methods

# altarica_AbstractDeclaration class attributes and methods

# altarica_ConstantDefinition class attributes and methods

# AbstractDeclaration class attributes and methods

# altarica_Constant class attributes and methods

# altarica_AbstractDefinitionConstant class attributes and methods

# altarica_DomainConstant class attributes and methods

# altarica_AbstractDomain class attributes and methods

# altarica_Domain class attributes and methods
altarica_Domain_name: Property = Property(name="name", type=StringType)
altarica_Domain.attributes={altarica_Domain_name}

# AbstractTypeRef class attributes and methods

# altarica_Range class attributes and methods

# AbstractDomain class attributes and methods

# NonNavigableVariable class attributes and methods

# altarica_Expression class attributes and methods

# altarica_ExpressionConstant class attributes and methods

# AbstractDefinitionConstant class attributes and methods

# altarica_PrimitiveType class attributes and methods
altarica_PrimitiveType_name: Property = Property(name="name", type=StringType)
altarica_PrimitiveType.attributes={altarica_PrimitiveType_name}

# altarica_Node class attributes and methods
altarica_Node_isMain: Property = Property(name="isMain", type=BooleanType)
altarica_Node_name: Property = Property(name="name", type=StringType)
altarica_Node.attributes={altarica_Node_isMain, altarica_Node_name}

# altarica_Enumeration class attributes and methods

# altarica_Literal class attributes and methods

# altarica_VariableAttribute class attributes and methods
altarica_VariableAttribute_name: Property = Property(name="name", type=StringType)
altarica_VariableAttribute.attributes={altarica_VariableAttribute_name}

# altarica_InitSpecification class attributes and methods

# AbstractSpecification class attributes and methods

# altarica_InitStatement class attributes and methods

# altarica_Affectation class attributes and methods

# altarica_ExternalSpecification class attributes and methods

# altarica_ExternalDirective class attributes and methods
altarica_ExternalDirective_directive: Property = Property(name="directive", type=StringType)
altarica_ExternalDirective.attributes={altarica_ExternalDirective_directive}

# altarica_AbstractSpecification class attributes and methods

# altarica_Flow class attributes and methods

# altarica_AbstractTypeRef class attributes and methods

# altarica_FlowSpecification class attributes and methods

# altarica_FlowDeclaration class attributes and methods
altarica_FlowDeclaration_kind: Property = Property(name="kind", type=StringType)
altarica_FlowDeclaration.attributes={altarica_FlowDeclaration_kind}

# NavigableVariable class attributes and methods

# altarica_Priority class attributes and methods

# altarica_AbstractExpression class attributes and methods

# altarica_StateSpecification class attributes and methods

# altarica_StateDeclaration class attributes and methods

# altarica_EventSpecification class attributes and methods

# altarica_EventDeclaration class attributes and methods

# altarica_Event class attributes and methods

# altarica_DomainRef class attributes and methods

# altarica_NodeInstanceSpecification class attributes and methods

# altarica_NodeInstanceDeclaration class attributes and methods

# altarica_State class attributes and methods

# altarica_AssertSpecification class attributes and methods

# altarica_Assert class attributes and methods

# altarica_AbstractBooleanExpression class attributes and methods

# altarica_VectorSpecification class attributes and methods

# altarica_Vector class attributes and methods

# altarica_VectorParameter class attributes and methods
altarica_VectorParameter_isRequired: Property = Property(name="isRequired", type=BooleanType)
altarica_VectorParameter.attributes={altarica_VectorParameter_isRequired}

# altarica_NodeInstance class attributes and methods

# altarica_TransitionSpecification class attributes and methods

# altarica_Transition class attributes and methods

# altarica_Cardinality class attributes and methods

# altarica_EventRef class attributes and methods

# altarica_Switch class attributes and methods

# AbstractExpression class attributes and methods

# AbstractBooleanExpression class attributes and methods

# altarica_CaseExpression class attributes and methods

# altarica_NavigableVariable class attributes and methods
altarica_NavigableVariable_name: Property = Property(name="name", type=StringType)
altarica_NavigableVariable.attributes={altarica_NavigableVariable_name}

# altarica_VariableRef class attributes and methods

# Expression class attributes and methods

# altarica_IfThenElse class attributes and methods

# altarica_EObject class attributes and methods

# altarica_EString class attributes and methods
altarica_EString_value: Property = Property(name="value", type=StringType)
altarica_EString.attributes={altarica_EString_value}

# altarica_EInteger class attributes and methods
altarica_EInteger_value: Property = Property(name="value", type=IntegerType)
altarica_EInteger.attributes={altarica_EInteger_value}

# altarica_Addition class attributes and methods

# altarica_NonNavigableVariable class attributes and methods

# altarica_EBoolean class attributes and methods
altarica_EBoolean_value: Property = Property(name="value", type=StringType)
altarica_EBoolean.attributes={altarica_EBoolean_value}

# altarica_Multiplication class attributes and methods

# altarica_Division class attributes and methods

# altarica_Minus class attributes and methods

# altarica_Or class attributes and methods

# altarica_Equal class attributes and methods

# altarica_And class attributes and methods

# altarica_StrictLower class attributes and methods

# altarica_Lower class attributes and methods

# altarica_NotEqual class attributes and methods

# altarica_Upper class attributes and methods

# altarica_StrictUpper class attributes and methods

# altarica_NestedQualifiedEventRef class attributes and methods

# EventRef class attributes and methods

# altarica_NestedQualifiedVariableRef class attributes and methods

# VariableRef class attributes and methods

# altarica_Imply class attributes and methods

# Relationships
ownedDeclarations0: BinaryAssociation = BinaryAssociation(
    name="ownedDeclarations0",
    ends={
        Property(name="altarica_AbstractDeclaration", type=altarica_System, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_System", type=altarica_AbstractDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant1: BinaryAssociation = BinaryAssociation(
    name="constant1",
    ends={
        Property(name="altarica_Constant", type=altarica_ConstantDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_ConstantDefinition", type=altarica_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2: BinaryAssociation = BinaryAssociation(
    name="expression2",
    ends={
        Property(name="altarica_AbstractDefinitionConstant", type=altarica_ConstantDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_ConstantDefinition3", type=altarica_AbstractDefinitionConstant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain6: BinaryAssociation = BinaryAssociation(
    name="domain6",
    ends={
        Property(name="altarica_AbstractDomain", type=altarica_DomainConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_DomainConstant", type=altarica_AbstractDomain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain7: BinaryAssociation = BinaryAssociation(
    name="domain7",
    ends={
        Property(name="altarica_AbstractDomain8", type=altarica_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Domain", type=altarica_AbstractDomain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExpression4: BinaryAssociation = BinaryAssociation(
    name="ownedExpression4",
    ends={
        Property(name="altarica_Expression", type=altarica_AbstractDefinitionConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_AbstractDefinitionConstant5", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLiterals14: BinaryAssociation = BinaryAssociation(
    name="ownedLiterals14",
    ends={
        Property(name="altarica_Literal", type=altarica_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Enumeration", type=altarica_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lower9: BinaryAssociation = BinaryAssociation(
    name="lower9",
    ends={
        Property(name="altarica_Expression10", type=altarica_Range, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Range", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upper11: BinaryAssociation = BinaryAssociation(
    name="upper11",
    ends={
        Property(name="altarica_Expression13", type=altarica_Range, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Range12", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedInitStatements16: BinaryAssociation = BinaryAssociation(
    name="ownedInitStatements16",
    ends={
        Property(name="altarica_InitStatement", type=altarica_InitSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_InitSpecification", type=altarica_InitStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
affectation17: BinaryAssociation = BinaryAssociation(
    name="affectation17",
    ends={
        Property(name="altarica_Affectation", type=altarica_InitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_InitStatement18", type=altarica_Affectation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDirectives19: BinaryAssociation = BinaryAssociation(
    name="ownedDirectives19",
    ends={
        Property(name="altarica_ExternalDirective", type=altarica_ExternalSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_ExternalSpecification", type=altarica_ExternalDirective, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSpecifications15: BinaryAssociation = BinaryAssociation(
    name="ownedSpecifications15",
    ends={
        Property(name="altarica_AbstractSpecification", type=altarica_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Node", type=altarica_AbstractSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFlows21: BinaryAssociation = BinaryAssociation(
    name="ownedFlows21",
    ends={
        Property(name="altarica_Flow", type=altarica_FlowDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_FlowDeclaration22", type=altarica_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain23: BinaryAssociation = BinaryAssociation(
    name="domain23",
    ends={
        Property(name="altarica_AbstractTypeRef", type=altarica_FlowDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_FlowDeclaration24", type=altarica_AbstractTypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attribute25: BinaryAssociation = BinaryAssociation(
    name="attribute25",
    ends={
        Property(name="altarica_VariableAttribute", type=altarica_FlowDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_FlowDeclaration26", type=altarica_VariableAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDeclarations20: BinaryAssociation = BinaryAssociation(
    name="ownedDeclarations20",
    ends={
        Property(name="altarica_FlowDeclaration", type=altarica_FlowSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_FlowSpecification", type=altarica_FlowDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute30: BinaryAssociation = BinaryAssociation(
    name="attribute30",
    ends={
        Property(name="altarica_VariableAttribute32", type=altarica_EventDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_EventDeclaration31", type=altarica_VariableAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedPriority33: BinaryAssociation = BinaryAssociation(
    name="ownedPriority33",
    ends={
        Property(name="altarica_Priority", type=altarica_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Event34", type=altarica_Priority, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExpression35: BinaryAssociation = BinaryAssociation(
    name="ownedExpression35",
    ends={
        Property(name="altarica_AbstractExpression", type=altarica_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Priority36", type=altarica_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedStateDeclarations37: BinaryAssociation = BinaryAssociation(
    name="ownedStateDeclarations37",
    ends={
        Property(name="altarica_StateDeclaration", type=altarica_StateSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_StateSpecification", type=altarica_StateDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEventDeclarations27: BinaryAssociation = BinaryAssociation(
    name="ownedEventDeclarations27",
    ends={
        Property(name="altarica_EventDeclaration", type=altarica_EventSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_EventSpecification", type=altarica_EventDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEvents28: BinaryAssociation = BinaryAssociation(
    name="ownedEvents28",
    ends={
        Property(name="altarica_Event", type=altarica_EventDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_EventDeclaration29", type=altarica_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute43: BinaryAssociation = BinaryAssociation(
    name="attribute43",
    ends={
        Property(name="altarica_StateDeclaration44", type=altarica_VariableAttribute, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="altarica_VariableAttribute45", type=altarica_StateDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
reference46: BinaryAssociation = BinaryAssociation(
    name="reference46",
    ends={
        Property(name="altarica_Domain47", type=altarica_DomainRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_DomainRef", type=altarica_Domain, multiplicity=Multiplicity(0, 1))
    }
)
ownedNodeInstanceDeclarations48: BinaryAssociation = BinaryAssociation(
    name="ownedNodeInstanceDeclarations48",
    ends={
        Property(name="altarica_NodeInstanceDeclaration", type=altarica_NodeInstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NodeInstanceSpecification", type=altarica_NodeInstanceDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStates38: BinaryAssociation = BinaryAssociation(
    name="ownedStates38",
    ends={
        Property(name="altarica_State", type=altarica_StateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_StateDeclaration39", type=altarica_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain40: BinaryAssociation = BinaryAssociation(
    name="domain40",
    ends={
        Property(name="altarica_AbstractTypeRef42", type=altarica_StateDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_StateDeclaration41", type=altarica_AbstractTypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAsserts54: BinaryAssociation = BinaryAssociation(
    name="ownedAsserts54",
    ends={
        Property(name="altarica_Assert", type=altarica_AssertSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_AssertSpecification", type=altarica_Assert, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpressions55: BinaryAssociation = BinaryAssociation(
    name="ownedExpressions55",
    ends={
        Property(name="altarica_AbstractBooleanExpression", type=altarica_Assert, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Assert56", type=altarica_AbstractBooleanExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVectors57: BinaryAssociation = BinaryAssociation(
    name="ownedVectors57",
    ends={
        Property(name="altarica_Vector", type=altarica_VectorSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_VectorSpecification", type=altarica_Vector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameters58: BinaryAssociation = BinaryAssociation(
    name="ownedParameters58",
    ends={
        Property(name="altarica_VectorParameter", type=altarica_Vector, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Vector59", type=altarica_VectorParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedNodeInstances49: BinaryAssociation = BinaryAssociation(
    name="ownedNodeInstances49",
    ends={
        Property(name="altarica_NodeInstance", type=altarica_NodeInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NodeInstanceDeclaration50", type=altarica_NodeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeType51: BinaryAssociation = BinaryAssociation(
    name="nodeType51",
    ends={
        Property(name="altarica_Node53", type=altarica_NodeInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NodeInstanceDeclaration52", type=altarica_Node, multiplicity=Multiplicity(0, 1))
    }
)
expression64: BinaryAssociation = BinaryAssociation(
    name="expression64",
    ends={
        Property(name="altarica_AbstractExpression66", type=altarica_Cardinality, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Cardinality65", type=altarica_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTransitionTransitions67: BinaryAssociation = BinaryAssociation(
    name="ownedTransitionTransitions67",
    ends={
        Property(name="altarica_Transition", type=altarica_TransitionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_TransitionSpecification", type=altarica_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExpresion68: BinaryAssociation = BinaryAssociation(
    name="ownedExpresion68",
    ends={
        Property(name="altarica_AbstractExpression70", type=altarica_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Transition69", type=altarica_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event71: BinaryAssociation = BinaryAssociation(
    name="event71",
    ends={
        Property(name="altarica_Event73", type=altarica_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Transition72", type=altarica_Event, multiplicity=Multiplicity(0, 1))
    }
)
cardinality60: BinaryAssociation = BinaryAssociation(
    name="cardinality60",
    ends={
        Property(name="altarica_Cardinality", type=altarica_Vector, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Vector61", type=altarica_Cardinality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventParameter62: BinaryAssociation = BinaryAssociation(
    name="eventParameter62",
    ends={
        Property(name="altarica_EventRef", type=altarica_VectorParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_VectorParameter63", type=altarica_EventRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedCases83: BinaryAssociation = BinaryAssociation(
    name="ownedCases83",
    ends={
        Property(name="altarica_CaseExpression", type=altarica_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Switch", type=altarica_CaseExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default84: BinaryAssociation = BinaryAssociation(
    name="default84",
    ends={
        Property(name="altarica_Expression86", type=altarica_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Switch85", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition87: BinaryAssociation = BinaryAssociation(
    name="condition87",
    ends={
        Property(name="altarica_Expression89", type=altarica_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_CaseExpression88", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body90: BinaryAssociation = BinaryAssociation(
    name="body90",
    ends={
        Property(name="altarica_Expression92", type=altarica_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_CaseExpression91", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAffectations74: BinaryAssociation = BinaryAssociation(
    name="ownedAffectations74",
    ends={
        Property(name="altarica_Affectation76", type=altarica_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Transition75", type=altarica_Affectation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state77: BinaryAssociation = BinaryAssociation(
    name="state77",
    ends={
        Property(name="altarica_State79", type=altarica_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Affectation78", type=altarica_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedExpression80: BinaryAssociation = BinaryAssociation(
    name="ownedExpression80",
    ends={
        Property(name="altarica_AbstractExpression82", type=altarica_Affectation, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Affectation81", type=altarica_AbstractExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then95: BinaryAssociation = BinaryAssociation(
    name="then95",
    ends={
        Property(name="altarica_IfThenElse96", type=altarica_EObject, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="altarica_EObject", type=altarica_IfThenElse, multiplicity=Multiplicity(1, 1))
    }
)
else97: BinaryAssociation = BinaryAssociation(
    name="else97",
    ends={
        Property(name="altarica_EObject99", type=altarica_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_IfThenElse98", type=altarica_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand101: BinaryAssociation = BinaryAssociation(
    name="operand101",
    ends={
        Property(name="altarica_Expression102", type=altarica_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Expression100", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable103: BinaryAssociation = BinaryAssociation(
    name="variable103",
    ends={
        Property(name="altarica_NavigableVariable", type=altarica_EventRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_EventRef104", type=altarica_NavigableVariable, multiplicity=Multiplicity(0, 1))
    }
)
condition93: BinaryAssociation = BinaryAssociation(
    name="condition93",
    ends={
        Property(name="altarica_Expression94", type=altarica_IfThenElse, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_IfThenElse", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand107: BinaryAssociation = BinaryAssociation(
    name="leftOperand107",
    ends={
        Property(name="altarica_Expression108", type=altarica_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Addition", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand109: BinaryAssociation = BinaryAssociation(
    name="rightOperand109",
    ends={
        Property(name="altarica_Expression111", type=altarica_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Addition110", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable105: BinaryAssociation = BinaryAssociation(
    name="variable105",
    ends={
        Property(name="altarica_NavigableVariable106", type=altarica_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_VariableRef", type=altarica_NavigableVariable, multiplicity=Multiplicity(0, 1))
    }
)
leftOperand117: BinaryAssociation = BinaryAssociation(
    name="leftOperand117",
    ends={
        Property(name="altarica_Expression118", type=altarica_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Multiplication", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand119: BinaryAssociation = BinaryAssociation(
    name="rightOperand119",
    ends={
        Property(name="altarica_Expression121", type=altarica_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Multiplication120", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand122: BinaryAssociation = BinaryAssociation(
    name="leftOperand122",
    ends={
        Property(name="altarica_Expression123", type=altarica_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Division", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand124: BinaryAssociation = BinaryAssociation(
    name="rightOperand124",
    ends={
        Property(name="altarica_Expression126", type=altarica_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Division125", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand112: BinaryAssociation = BinaryAssociation(
    name="leftOperand112",
    ends={
        Property(name="altarica_Expression113", type=altarica_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Minus", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand114: BinaryAssociation = BinaryAssociation(
    name="rightOperand114",
    ends={
        Property(name="altarica_Expression116", type=altarica_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Minus115", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand132: BinaryAssociation = BinaryAssociation(
    name="leftOperand132",
    ends={
        Property(name="altarica_Expression133", type=altarica_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Or", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand134: BinaryAssociation = BinaryAssociation(
    name="rightOperand134",
    ends={
        Property(name="altarica_Expression136", type=altarica_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Or135", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand137: BinaryAssociation = BinaryAssociation(
    name="leftOperand137",
    ends={
        Property(name="altarica_Expression138", type=altarica_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Equal", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand127: BinaryAssociation = BinaryAssociation(
    name="leftOperand127",
    ends={
        Property(name="altarica_Expression128", type=altarica_And, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_And", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand129: BinaryAssociation = BinaryAssociation(
    name="rightOperand129",
    ends={
        Property(name="altarica_Expression131", type=altarica_And, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_And130", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand144: BinaryAssociation = BinaryAssociation(
    name="rightOperand144",
    ends={
        Property(name="altarica_Expression146", type=altarica_NotEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NotEqual145", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand147: BinaryAssociation = BinaryAssociation(
    name="leftOperand147",
    ends={
        Property(name="altarica_Expression148", type=altarica_StrictLower, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_StrictLower", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand149: BinaryAssociation = BinaryAssociation(
    name="rightOperand149",
    ends={
        Property(name="altarica_Expression151", type=altarica_StrictLower, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_StrictLower150", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand152: BinaryAssociation = BinaryAssociation(
    name="leftOperand152",
    ends={
        Property(name="altarica_Expression153", type=altarica_Lower, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Lower", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand139: BinaryAssociation = BinaryAssociation(
    name="rightOperand139",
    ends={
        Property(name="altarica_Expression141", type=altarica_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Equal140", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand142: BinaryAssociation = BinaryAssociation(
    name="leftOperand142",
    ends={
        Property(name="altarica_Expression143", type=altarica_NotEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NotEqual", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand157: BinaryAssociation = BinaryAssociation(
    name="leftOperand157",
    ends={
        Property(name="altarica_StrictUpper", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="altarica_Expression158", type=altarica_StrictUpper, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand159: BinaryAssociation = BinaryAssociation(
    name="rightOperand159",
    ends={
        Property(name="altarica_Expression161", type=altarica_StrictUpper, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_StrictUpper160", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand162: BinaryAssociation = BinaryAssociation(
    name="leftOperand162",
    ends={
        Property(name="altarica_Expression163", type=altarica_Upper, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Upper", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand164: BinaryAssociation = BinaryAssociation(
    name="rightOperand164",
    ends={
        Property(name="altarica_Expression166", type=altarica_Upper, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Upper165", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand154: BinaryAssociation = BinaryAssociation(
    name="rightOperand154",
    ends={
        Property(name="altarica_Expression156", type=altarica_Lower, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Lower155", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target172: BinaryAssociation = BinaryAssociation(
    name="target172",
    ends={
        Property(name="altarica_EventRef173", type=altarica_NestedQualifiedEventRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NestedQualifiedEventRef", type=altarica_EventRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedVariable174: BinaryAssociation = BinaryAssociation(
    name="nestedVariable174",
    ends={
        Property(name="altarica_NavigableVariable176", type=altarica_NestedQualifiedEventRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NestedQualifiedEventRef175", type=altarica_NavigableVariable, multiplicity=Multiplicity(0, 1))
    }
)
target177: BinaryAssociation = BinaryAssociation(
    name="target177",
    ends={
        Property(name="altarica_VariableRef178", type=altarica_NestedQualifiedVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NestedQualifiedVariableRef", type=altarica_VariableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedVariable179: BinaryAssociation = BinaryAssociation(
    name="nestedVariable179",
    ends={
        Property(name="altarica_NavigableVariable181", type=altarica_NestedQualifiedVariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_NestedQualifiedVariableRef180", type=altarica_NavigableVariable, multiplicity=Multiplicity(0, 1))
    }
)
leftOperand167: BinaryAssociation = BinaryAssociation(
    name="leftOperand167",
    ends={
        Property(name="altarica_Expression168", type=altarica_Imply, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Imply", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand169: BinaryAssociation = BinaryAssociation(
    name="rightOperand169",
    ends={
        Property(name="altarica_Expression171", type=altarica_Imply, multiplicity=Multiplicity(1, 1)),
        Property(name="altarica_Imply170", type=altarica_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_altarica_ConstantDefinition_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=altarica_ConstantDefinition)
gen_altarica_ExpressionConstant_AbstractDefinitionConstant = Generalization(general=AbstractDefinitionConstant, specific=altarica_ExpressionConstant)
gen_altarica_DomainConstant_AbstractDefinitionConstant = Generalization(general=AbstractDefinitionConstant, specific=altarica_DomainConstant)
gen_altarica_Domain_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=altarica_Domain)
gen_altarica_AbstractDomain_AbstractTypeRef = Generalization(general=AbstractTypeRef, specific=altarica_AbstractDomain)
gen_altarica_Range_AbstractDomain = Generalization(general=AbstractDomain, specific=altarica_Range)
gen_altarica_Constant_NonNavigableVariable = Generalization(general=NonNavigableVariable, specific=altarica_Constant)
gen_altarica_PrimitiveType_AbstractDomain = Generalization(general=AbstractDomain, specific=altarica_PrimitiveType)
gen_altarica_Literal_NonNavigableVariable = Generalization(general=NonNavigableVariable, specific=altarica_Literal)
gen_altarica_Node_AbstractDeclaration = Generalization(general=AbstractDeclaration, specific=altarica_Node)
gen_altarica_Enumeration_AbstractDomain = Generalization(general=AbstractDomain, specific=altarica_Enumeration)
gen_altarica_InitSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_InitSpecification)
gen_altarica_ExternalSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_ExternalSpecification)
gen_altarica_Flow_NonNavigableVariable = Generalization(general=NonNavigableVariable, specific=altarica_Flow)
gen_altarica_FlowSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_FlowSpecification)
gen_altarica_Event_NavigableVariable = Generalization(general=NavigableVariable, specific=altarica_Event)
gen_altarica_StateSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_StateSpecification)
gen_altarica_EventSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_EventSpecification)
gen_altarica_State_NonNavigableVariable = Generalization(general=NonNavigableVariable, specific=altarica_State)
gen_altarica_DomainRef_AbstractTypeRef = Generalization(general=AbstractTypeRef, specific=altarica_DomainRef)
gen_altarica_NodeInstanceSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_NodeInstanceSpecification)
gen_altarica_AssertSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_AssertSpecification)
gen_altarica_VectorSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_VectorSpecification)
gen_altarica_NodeInstance_NavigableVariable = Generalization(general=NavigableVariable, specific=altarica_NodeInstance)
gen_altarica_TransitionSpecification_AbstractSpecification = Generalization(general=AbstractSpecification, specific=altarica_TransitionSpecification)
gen_altarica_Switch_AbstractExpression = Generalization(general=AbstractExpression, specific=altarica_Switch)
gen_altarica_Switch_AbstractBooleanExpression = Generalization(general=AbstractBooleanExpression, specific=altarica_Switch)
gen_altarica_Expression_AbstractExpression = Generalization(general=AbstractExpression, specific=altarica_Expression)
gen_altarica_Expression_AbstractBooleanExpression = Generalization(general=AbstractBooleanExpression, specific=altarica_Expression)
gen_altarica_VariableRef_Expression = Generalization(general=Expression, specific=altarica_VariableRef)
gen_altarica_IfThenElse_AbstractExpression = Generalization(general=AbstractExpression, specific=altarica_IfThenElse)
gen_altarica_IfThenElse_AbstractBooleanExpression = Generalization(general=AbstractBooleanExpression, specific=altarica_IfThenElse)
gen_altarica_EString_Expression = Generalization(general=Expression, specific=altarica_EString)
gen_altarica_EInteger_Expression = Generalization(general=Expression, specific=altarica_EInteger)
gen_altarica_Addition_Expression = Generalization(general=Expression, specific=altarica_Addition)
gen_altarica_NonNavigableVariable_NavigableVariable = Generalization(general=NavigableVariable, specific=altarica_NonNavigableVariable)
gen_altarica_EBoolean_Expression = Generalization(general=Expression, specific=altarica_EBoolean)
gen_altarica_Multiplication_Expression = Generalization(general=Expression, specific=altarica_Multiplication)
gen_altarica_Division_Expression = Generalization(general=Expression, specific=altarica_Division)
gen_altarica_Minus_Expression = Generalization(general=Expression, specific=altarica_Minus)
gen_altarica_Or_Expression = Generalization(general=Expression, specific=altarica_Or)
gen_altarica_Equal_Expression = Generalization(general=Expression, specific=altarica_Equal)
gen_altarica_And_Expression = Generalization(general=Expression, specific=altarica_And)
gen_altarica_StrictLower_Expression = Generalization(general=Expression, specific=altarica_StrictLower)
gen_altarica_Lower_Expression = Generalization(general=Expression, specific=altarica_Lower)
gen_altarica_NotEqual_Expression = Generalization(general=Expression, specific=altarica_NotEqual)
gen_altarica_Upper_Expression = Generalization(general=Expression, specific=altarica_Upper)
gen_altarica_StrictUpper_Expression = Generalization(general=Expression, specific=altarica_StrictUpper)
gen_altarica_NestedQualifiedEventRef_EventRef = Generalization(general=EventRef, specific=altarica_NestedQualifiedEventRef)
gen_altarica_NestedQualifiedVariableRef_VariableRef = Generalization(general=VariableRef, specific=altarica_NestedQualifiedVariableRef)
gen_altarica_Imply_Expression = Generalization(general=Expression, specific=altarica_Imply)

# Domain Model
domain_model = DomainModel(
    name="altarica",
    types={altarica_System, altarica_AbstractDeclaration, altarica_ConstantDefinition, AbstractDeclaration, altarica_Constant, altarica_AbstractDefinitionConstant, altarica_DomainConstant, altarica_AbstractDomain, altarica_Domain, AbstractTypeRef, altarica_Range, AbstractDomain, NonNavigableVariable, altarica_Expression, altarica_ExpressionConstant, AbstractDefinitionConstant, altarica_PrimitiveType, altarica_Node, altarica_Enumeration, altarica_Literal, altarica_VariableAttribute, altarica_InitSpecification, AbstractSpecification, altarica_InitStatement, altarica_Affectation, altarica_ExternalSpecification, altarica_ExternalDirective, altarica_AbstractSpecification, altarica_Flow, altarica_AbstractTypeRef, altarica_FlowSpecification, altarica_FlowDeclaration, NavigableVariable, altarica_Priority, altarica_AbstractExpression, altarica_StateSpecification, altarica_StateDeclaration, altarica_EventSpecification, altarica_EventDeclaration, altarica_Event, altarica_DomainRef, altarica_NodeInstanceSpecification, altarica_NodeInstanceDeclaration, altarica_State, altarica_AssertSpecification, altarica_Assert, altarica_AbstractBooleanExpression, altarica_VectorSpecification, altarica_Vector, altarica_VectorParameter, altarica_NodeInstance, altarica_TransitionSpecification, altarica_Transition, altarica_Cardinality, altarica_EventRef, altarica_Switch, AbstractExpression, AbstractBooleanExpression, altarica_CaseExpression, altarica_NavigableVariable, altarica_VariableRef, Expression, altarica_IfThenElse, altarica_EObject, altarica_EString, altarica_EInteger, altarica_Addition, altarica_NonNavigableVariable, altarica_EBoolean, altarica_Multiplication, altarica_Division, altarica_Minus, altarica_Or, altarica_Equal, altarica_And, altarica_StrictLower, altarica_Lower, altarica_NotEqual, altarica_Upper, altarica_StrictUpper, altarica_NestedQualifiedEventRef, EventRef, altarica_NestedQualifiedVariableRef, VariableRef, altarica_Imply, PrimitiveTypeKind, FlowKind},
    associations={ownedDeclarations0, constant1, expression2, domain6, domain7, ownedExpression4, ownedLiterals14, lower9, upper11, ownedInitStatements16, affectation17, ownedDirectives19, ownedSpecifications15, ownedFlows21, domain23, attribute25, ownedDeclarations20, attribute30, ownedPriority33, ownedExpression35, ownedStateDeclarations37, ownedEventDeclarations27, ownedEvents28, attribute43, reference46, ownedNodeInstanceDeclarations48, ownedStates38, domain40, ownedAsserts54, ownedExpressions55, ownedVectors57, ownedParameters58, ownedNodeInstances49, nodeType51, expression64, ownedTransitionTransitions67, ownedExpresion68, event71, cardinality60, eventParameter62, ownedCases83, default84, condition87, body90, ownedAffectations74, state77, ownedExpression80, then95, else97, operand101, variable103, condition93, leftOperand107, rightOperand109, variable105, leftOperand117, rightOperand119, leftOperand122, rightOperand124, leftOperand112, rightOperand114, leftOperand132, rightOperand134, leftOperand137, leftOperand127, rightOperand129, rightOperand144, leftOperand147, rightOperand149, leftOperand152, rightOperand139, leftOperand142, leftOperand157, rightOperand159, leftOperand162, rightOperand164, rightOperand154, target172, nestedVariable174, target177, nestedVariable179, leftOperand167, rightOperand169},
    generalizations={gen_altarica_ConstantDefinition_AbstractDeclaration, gen_altarica_ExpressionConstant_AbstractDefinitionConstant, gen_altarica_DomainConstant_AbstractDefinitionConstant, gen_altarica_Domain_AbstractDeclaration, gen_altarica_AbstractDomain_AbstractTypeRef, gen_altarica_Range_AbstractDomain, gen_altarica_Constant_NonNavigableVariable, gen_altarica_PrimitiveType_AbstractDomain, gen_altarica_Literal_NonNavigableVariable, gen_altarica_Node_AbstractDeclaration, gen_altarica_Enumeration_AbstractDomain, gen_altarica_InitSpecification_AbstractSpecification, gen_altarica_ExternalSpecification_AbstractSpecification, gen_altarica_Flow_NonNavigableVariable, gen_altarica_FlowSpecification_AbstractSpecification, gen_altarica_Event_NavigableVariable, gen_altarica_StateSpecification_AbstractSpecification, gen_altarica_EventSpecification_AbstractSpecification, gen_altarica_State_NonNavigableVariable, gen_altarica_DomainRef_AbstractTypeRef, gen_altarica_NodeInstanceSpecification_AbstractSpecification, gen_altarica_AssertSpecification_AbstractSpecification, gen_altarica_VectorSpecification_AbstractSpecification, gen_altarica_NodeInstance_NavigableVariable, gen_altarica_TransitionSpecification_AbstractSpecification, gen_altarica_Switch_AbstractExpression, gen_altarica_Switch_AbstractBooleanExpression, gen_altarica_Expression_AbstractExpression, gen_altarica_Expression_AbstractBooleanExpression, gen_altarica_VariableRef_Expression, gen_altarica_IfThenElse_AbstractExpression, gen_altarica_IfThenElse_AbstractBooleanExpression, gen_altarica_EString_Expression, gen_altarica_EInteger_Expression, gen_altarica_Addition_Expression, gen_altarica_NonNavigableVariable_NavigableVariable, gen_altarica_EBoolean_Expression, gen_altarica_Multiplication_Expression, gen_altarica_Division_Expression, gen_altarica_Minus_Expression, gen_altarica_Or_Expression, gen_altarica_Equal_Expression, gen_altarica_And_Expression, gen_altarica_StrictLower_Expression, gen_altarica_Lower_Expression, gen_altarica_NotEqual_Expression, gen_altarica_Upper_Expression, gen_altarica_StrictUpper_Expression, gen_altarica_NestedQualifiedEventRef_EventRef, gen_altarica_NestedQualifiedVariableRef_VariableRef, gen_altarica_Imply_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)