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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

ReferenceType: Enumeration = Enumeration(
    name="ReferenceType",
    literals={
            EnumerationLiteral(name="Composition"),
			EnumerationLiteral(name="Aggregation"),
			EnumerationLiteral(name="Regular")
    }
)

MessageSort: Enumeration = Enumeration(
    name="MessageSort",
    literals={
            EnumerationLiteral(name="synchCall"),
			EnumerationLiteral(name="createMessage"),
			EnumerationLiteral(name="deleteMessage"),
			EnumerationLiteral(name="reply")
    }
)

InteractionOperatorKind: Enumeration = Enumeration(
    name="InteractionOperatorKind",
    literals={
            EnumerationLiteral(name="alt"),
			EnumerationLiteral(name="opt"),
			EnumerationLiteral(name="loop"),
			EnumerationLiteral(name="disruptable"),
			EnumerationLiteral(name="critical")
    }
)

InstantiationType: Enumeration = Enumeration(
    name="InstantiationType",
    literals={
            EnumerationLiteral(name="Depends"),
			EnumerationLiteral(name="Extends")
    }
)

# Classes
ram_MappableElement = Class(name="ram::MappableElement", is_abstract=True)
ram_AbstractMessageView = Class(name="ram::AbstractMessageView", is_abstract=True)
ram_Instantiation = Class(name="ram::Instantiation")
ram_Layout = Class(name="ram::Layout")
ram_Classifier = Class(name="ram::Classifier", is_abstract=True)
ram_Association = Class(name="ram::Association")
ram_Type = Class(name="ram::Type", is_abstract=True)
ram_Class = Class(name="ram::Class")
Classifier = Class(name="Classifier")
ram_Aspect = Class(name="ram::Aspect")
NamedElement = Class(name="NamedElement")
ram_StructuralView = Class(name="ram::StructuralView")
ram_NamedElement = Class(name="ram::NamedElement", is_abstract=True)
ram_Mapping = Class(name="ram::Mapping")
ram_AssociationEnd = Class(name="ram::AssociationEnd")
ram_Attribute = Class(name="ram::Attribute")
Property_ = Class(name="Property")
ram_Parameter = Class(name="ram::Parameter")
StructuralFeature = Class(name="StructuralFeature")
TemporaryProperty = Class(name="TemporaryProperty")
ram_PrimitiveType = Class(name="ram::PrimitiveType", is_abstract=True)
TypedElement = Class(name="TypedElement")
Type = Class(name="Type")
ImplementationClass = Class(name="ImplementationClass")
ram_Operation = Class(name="ram::Operation")
MappableElement = Class(name="MappableElement")
ram_RInt = Class(name="ram::RInt")
ram_RChar = Class(name="ram::RChar")
ram_RString = Class(name="ram::RString")
ram_RAny = Class(name="ram::RAny")
ram_REnum = Class(name="ram::REnum")
ram_REnumLiteral = Class(name="ram::REnumLiteral")
ram_ObjectType = Class(name="ram::ObjectType", is_abstract=True)
ram_RVoid = Class(name="ram::RVoid")
ram_RBoolean = Class(name="ram::RBoolean")
PrimitiveType = Class(name="PrimitiveType")
ram_Interaction = Class(name="ram::Interaction")
ram_MessageViewReference = Class(name="ram::MessageViewReference")
FragmentContainer = Class(name="FragmentContainer")
ram_AspectMessageView = Class(name="ram::AspectMessageView")
ram_MessageView = Class(name="ram::MessageView")
AbstractMessageView = Class(name="AbstractMessageView")
ram_Gate = Class(name="ram::Gate")
ram_TypedElement = Class(name="ram::TypedElement", is_abstract=True)
ram_Lifeline = Class(name="ram::Lifeline")
ram_Message = Class(name="ram::Message")
ram_Reference = Class(name="ram::Reference")
ram_MessageEnd = Class(name="ram::MessageEnd", is_abstract=True)
ram_TemporaryProperty = Class(name="ram::TemporaryProperty", is_abstract=True)
ram_InteractionFragment = Class(name="ram::InteractionFragment", is_abstract=True)
ram_ValueSpecification = Class(name="ram::ValueSpecification", is_abstract=True)
ram_StructuralFeature = Class(name="ram::StructuralFeature", is_abstract=True)
ram_ParameterValueMapping = Class(name="ram::ParameterValueMapping")
ram_FragmentContainer = Class(name="ram::FragmentContainer", is_abstract=True)
ram_CombinedFragment = Class(name="ram::CombinedFragment")
ram_MessageOccurrenceSpecification = Class(name="ram::MessageOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
MessageEnd = Class(name="MessageEnd")
ram_OccurrenceSpecification = Class(name="ram::OccurrenceSpecification")
InteractionFragment = Class(name="InteractionFragment")
ram_DestructionOccurrenceSpecification = Class(name="ram::DestructionOccurrenceSpecification")
MessageOccurrenceSpecification = Class(name="MessageOccurrenceSpecification")
ram_OriginalBehaviorExecution = Class(name="ram::OriginalBehaviorExecution")
ram_ExecutionStatement = Class(name="ram::ExecutionStatement")
ram_StructuralFeatureValue = Class(name="ram::StructuralFeatureValue")
ValueSpecification = Class(name="ValueSpecification")
ram_InteractionOperand = Class(name="ram::InteractionOperand")
ram_ParameterValue = Class(name="ram::ParameterValue")
ram_OpaqueExpression = Class(name="ram::OpaqueExpression")
ram_LiteralSpecification = Class(name="ram::LiteralSpecification", is_abstract=True)
ram_LiteralString = Class(name="ram::LiteralString")
LiteralSpecification = Class(name="LiteralSpecification")
ram_LiteralInteger = Class(name="ram::LiteralInteger")
ram_RCollection = Class(name="ram::RCollection", is_abstract=True)
ram_EObject = Class(name="ram::EObject")
ram_ElementMap = Class(name="ram::ElementMap")
ram_LayoutElement = Class(name="ram::LayoutElement")
ObjectType = Class(name="ObjectType")
ram_ImplementationClass = Class(name="ram::ImplementationClass")
ram_Property = Class(name="ram::Property", is_abstract=True)
ram_RSet = Class(name="ram::RSet")
RCollection = Class(name="RCollection")
ram_RList = Class(name="ram::RList")
ram_ContainerMap = Class(name="ram::ContainerMap")
ram_LiteralBoolean = Class(name="ram::LiteralBoolean")

# ram_MappableElement class attributes and methods

# ram_AbstractMessageView class attributes and methods

# ram_Instantiation class attributes and methods
ram_Instantiation_type: Property = Property(name="type", type=StringType)
ram_Instantiation.attributes={ram_Instantiation_type}

# ram_Layout class attributes and methods

# ram_Classifier class attributes and methods

# ram_Association class attributes and methods

# ram_Type class attributes and methods

# ram_Class class attributes and methods
ram_Class_partial: Property = Property(name="partial", type=BooleanType)
ram_Class_abstract: Property = Property(name="abstract", type=BooleanType)
ram_Class.attributes={ram_Class_partial, ram_Class_abstract}

# Classifier class attributes and methods

# ram_Aspect class attributes and methods

# NamedElement class attributes and methods

# ram_StructuralView class attributes and methods

# ram_NamedElement class attributes and methods
ram_NamedElement_name: Property = Property(name="name", type=StringType)
ram_NamedElement.attributes={ram_NamedElement_name}

# ram_Mapping class attributes and methods

# ram_AssociationEnd class attributes and methods
ram_AssociationEnd_navigable: Property = Property(name="navigable", type=BooleanType)
ram_AssociationEnd_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
ram_AssociationEnd.attributes={ram_AssociationEnd_navigable}
ram_AssociationEnd.methods={ram_AssociationEnd_m_getType}

# ram_Attribute class attributes and methods

# Property class attributes and methods

# ram_Parameter class attributes and methods

# StructuralFeature class attributes and methods

# TemporaryProperty class attributes and methods

# ram_PrimitiveType class attributes and methods

# TypedElement class attributes and methods

# Type class attributes and methods

# ImplementationClass class attributes and methods

# ram_Operation class attributes and methods
ram_Operation_abstract: Property = Property(name="abstract", type=BooleanType)
ram_Operation_visibility: Property = Property(name="visibility", type=StringType)
ram_Operation_static: Property = Property(name="static", type=BooleanType)
ram_Operation_partial: Property = Property(name="partial", type=BooleanType)
ram_Operation.attributes={ram_Operation_visibility, ram_Operation_static, ram_Operation_partial, ram_Operation_abstract}

# MappableElement class attributes and methods

# ram_RInt class attributes and methods
ram_RInt_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RInt_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RInt.methods={ram_RInt_m_getInstanceClassName, ram_RInt_m_getName}

# ram_RChar class attributes and methods
ram_RChar_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RChar_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RChar.methods={ram_RChar_m_getInstanceClassName, ram_RChar_m_getName}

# ram_RString class attributes and methods
ram_RString_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RString_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RString.methods={ram_RString_m_getName, ram_RString_m_getInstanceClassName}

# ram_RAny class attributes and methods
ram_RAny_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RAny.methods={ram_RAny_m_getName}

# ram_REnum class attributes and methods

# ram_REnumLiteral class attributes and methods

# ram_ObjectType class attributes and methods

# ram_RVoid class attributes and methods
ram_RVoid_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RVoid.methods={ram_RVoid_m_getName}

# ram_RBoolean class attributes and methods
ram_RBoolean_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RBoolean_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RBoolean.methods={ram_RBoolean_m_getName, ram_RBoolean_m_getInstanceClassName}

# PrimitiveType class attributes and methods

# ram_Interaction class attributes and methods

# ram_MessageViewReference class attributes and methods

# FragmentContainer class attributes and methods

# ram_AspectMessageView class attributes and methods

# ram_MessageView class attributes and methods

# AbstractMessageView class attributes and methods

# ram_Gate class attributes and methods

# ram_TypedElement class attributes and methods
ram_TypedElement_m_getType: Method = Method(name="getType", parameters={}, type=Type)
ram_TypedElement.methods={ram_TypedElement_m_getType}

# ram_Lifeline class attributes and methods

# ram_Message class attributes and methods
ram_Message_selfMessage: Property = Property(name="selfMessage", type=BooleanType)
ram_Message_messageSort: Property = Property(name="messageSort", type=StringType)
ram_Message.attributes={ram_Message_selfMessage, ram_Message_messageSort}

# ram_Reference class attributes and methods

# ram_MessageEnd class attributes and methods

# ram_TemporaryProperty class attributes and methods

# ram_InteractionFragment class attributes and methods

# ram_ValueSpecification class attributes and methods

# ram_StructuralFeature class attributes and methods
ram_StructuralFeature_static: Property = Property(name="static", type=BooleanType)
ram_StructuralFeature.attributes={ram_StructuralFeature_static}

# ram_ParameterValueMapping class attributes and methods

# ram_FragmentContainer class attributes and methods

# ram_CombinedFragment class attributes and methods
ram_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
ram_CombinedFragment.attributes={ram_CombinedFragment_interactionOperator}

# ram_MessageOccurrenceSpecification class attributes and methods

# OccurrenceSpecification class attributes and methods

# MessageEnd class attributes and methods

# ram_OccurrenceSpecification class attributes and methods

# InteractionFragment class attributes and methods

# ram_DestructionOccurrenceSpecification class attributes and methods

# MessageOccurrenceSpecification class attributes and methods

# ram_OriginalBehaviorExecution class attributes and methods

# ram_ExecutionStatement class attributes and methods

# ram_StructuralFeatureValue class attributes and methods

# ValueSpecification class attributes and methods

# ram_InteractionOperand class attributes and methods

# ram_ParameterValue class attributes and methods

# ram_OpaqueExpression class attributes and methods
ram_OpaqueExpression_body: Property = Property(name="body", type=StringType)
ram_OpaqueExpression_language: Property = Property(name="language", type=StringType)
ram_OpaqueExpression.attributes={ram_OpaqueExpression_body, ram_OpaqueExpression_language}

# ram_LiteralSpecification class attributes and methods

# ram_LiteralString class attributes and methods
ram_LiteralString_value: Property = Property(name="value", type=StringType)
ram_LiteralString.attributes={ram_LiteralString_value}

# LiteralSpecification class attributes and methods

# ram_LiteralInteger class attributes and methods
ram_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
ram_LiteralInteger.attributes={ram_LiteralInteger_value}

# ram_RCollection class attributes and methods
ram_RCollection_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RCollection.methods={ram_RCollection_m_getName}

# ram_EObject class attributes and methods

# ram_ElementMap class attributes and methods

# ram_LayoutElement class attributes and methods
ram_LayoutElement_x: Property = Property(name="x", type=FloatType)
ram_LayoutElement_y: Property = Property(name="y", type=FloatType)
ram_LayoutElement.attributes={ram_LayoutElement_x, ram_LayoutElement_y}

# ObjectType class attributes and methods

# ram_ImplementationClass class attributes and methods
ram_ImplementationClass_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ram_ImplementationClass.attributes={ram_ImplementationClass_instanceClassName}

# ram_Property class attributes and methods
ram_Property_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ram_Property_upperBound: Property = Property(name="upperBound", type=IntegerType)
ram_Property_referenceType: Property = Property(name="referenceType", type=StringType)
ram_Property.attributes={ram_Property_lowerBound, ram_Property_referenceType, ram_Property_upperBound}

# ram_RSet class attributes and methods

# RCollection class attributes and methods

# ram_RList class attributes and methods

# ram_ContainerMap class attributes and methods

# ram_LiteralBoolean class attributes and methods
ram_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
ram_LiteralBoolean.attributes={ram_LiteralBoolean_value}

# Relationships
mandatoryAspectParameters1: BinaryAssociation = BinaryAssociation(
    name="mandatoryAspectParameters1",
    ends={
        Property(name="ram_MappableElement", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect2", type=ram_MappableElement, multiplicity=Multiplicity(0, 9999))
    }
)
messageViews3: BinaryAssociation = BinaryAssociation(
    name="messageViews3",
    ends={
        Property(name="ram_AbstractMessageView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect4", type=ram_AbstractMessageView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiations5: BinaryAssociation = BinaryAssociation(
    name="instantiations5",
    ends={
        Property(name="ram_Instantiation", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect6", type=ram_Instantiation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout7: BinaryAssociation = BinaryAssociation(
    name="layout7",
    ends={
        Property(name="ram_Layout", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect8", type=ram_Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes9: BinaryAssociation = BinaryAssociation(
    name="classes9",
    ends={
        Property(name="ram_Classifier", type=ram_StructuralView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralView10", type=ram_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations11: BinaryAssociation = BinaryAssociation(
    name="associations11",
    ends={
        Property(name="ram_Association", type=ram_StructuralView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralView12", type=ram_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types13: BinaryAssociation = BinaryAssociation(
    name="types13",
    ends={
        Property(name="ram_Type", type=ram_StructuralView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralView14", type=ram_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralView0: BinaryAssociation = BinaryAssociation(
    name="structuralView0",
    ends={
        Property(name="ram_StructuralView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect", type=ram_StructuralView, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assoc20: BinaryAssociation = BinaryAssociation(
    name="assoc20",
    ends={
        Property(name="Association", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ends", type=ram_Association, multiplicity=Multiplicity(1, 1))
    }
)
myClass21: BinaryAssociation = BinaryAssociation(
    name="myClass21",
    ends={
        Property(name="Class", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnds", type=ram_Class, multiplicity=Multiplicity(1, 1))
    }
)
ends22: BinaryAssociation = BinaryAssociation(
    name="ends22",
    ends={
        Property(name="AssociationEnd23", type=ram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc", type=ram_AssociationEnd, multiplicity=Multiplicity(2, 2))
    }
)
mappings24: BinaryAssociation = BinaryAssociation(
    name="mappings24",
    ends={
        Property(name="ram_Mapping", type=ram_Instantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Instantiation25", type=ram_Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalAspect26: BinaryAssociation = BinaryAssociation(
    name="externalAspect26",
    ends={
        Property(name="ram_Aspect28", type=ram_Instantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Instantiation27", type=ram_Aspect, multiplicity=Multiplicity(1, 1))
    }
)
associationEnds15: BinaryAssociation = BinaryAssociation(
    name="associationEnds15",
    ends={
        Property(name="AssociationEnd", type=ram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="myClass", type=ram_AssociationEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes16: BinaryAssociation = BinaryAssociation(
    name="attributes16",
    ends={
        Property(name="ram_Attribute", type=ram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Class", type=ram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes17: BinaryAssociation = BinaryAssociation(
    name="superTypes17",
    ends={
        Property(name="ram_Classifier19", type=ram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Class18", type=ram_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
returnType35: BinaryAssociation = BinaryAssociation(
    name="returnType35",
    ends={
        Property(name="ram_Type36", type=ram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Operation", type=ram_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameters37: BinaryAssociation = BinaryAssociation(
    name="parameters37",
    ends={
        Property(name="ram_Parameter", type=ram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Operation38", type=ram_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="ram_PrimitiveType", type=ram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Attribute40", type=ram_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="ram_Type43", type=ram_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Parameter42", type=ram_Type, multiplicity=Multiplicity(1, 1))
    }
)
toElements29: BinaryAssociation = BinaryAssociation(
    name="toElements29",
    ends={
        Property(name="ram_MappableElement31", type=ram_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Mapping30", type=ram_MappableElement, multiplicity=Multiplicity(1, 9999))
    }
)
fromElement32: BinaryAssociation = BinaryAssociation(
    name="fromElement32",
    ends={
        Property(name="ram_MappableElement34", type=ram_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Mapping33", type=ram_MappableElement, multiplicity=Multiplicity(1, 1))
    }
)
literals44: BinaryAssociation = BinaryAssociation(
    name="literals44",
    ends={
        Property(name="REnumLiteral", type=ram_REnum, multiplicity=Multiplicity(1, 1)),
        Property(name="enum", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enum45: BinaryAssociation = BinaryAssociation(
    name="enum45",
    ends={
        Property(name="REnum", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=ram_REnum, multiplicity=Multiplicity(1, 1))
    }
)
specifies48: BinaryAssociation = BinaryAssociation(
    name="specifies48",
    ends={
        Property(name="ram_Operation49", type=ram_MessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageView", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
specification50: BinaryAssociation = BinaryAssociation(
    name="specification50",
    ends={
        Property(name="ram_Interaction", type=ram_MessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageView51", type=ram_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
references52: BinaryAssociation = BinaryAssociation(
    name="references52",
    ends={
        Property(name="ram_MessageView53", type=ram_MessageViewReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageViewReference", type=ram_MessageView, multiplicity=Multiplicity(1, 1))
    }
)
affectedBy46: BinaryAssociation = BinaryAssociation(
    name="affectedBy46",
    ends={
        Property(name="ram_AspectMessageView", type=ram_AbstractMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AbstractMessageView47", type=ram_AspectMessageView, multiplicity=Multiplicity(0, 9999))
    }
)
properties57: BinaryAssociation = BinaryAssociation(
    name="properties57",
    ends={
        Property(name="ram_Reference", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction58", type=ram_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGates59: BinaryAssociation = BinaryAssociation(
    name="formalGates59",
    ends={
        Property(name="ram_Gate", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction60", type=ram_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointcut61: BinaryAssociation = BinaryAssociation(
    name="pointcut61",
    ends={
        Property(name="ram_Operation63", type=ram_AspectMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AspectMessageView62", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
advice64: BinaryAssociation = BinaryAssociation(
    name="advice64",
    ends={
        Property(name="ram_Interaction66", type=ram_AspectMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AspectMessageView65", type=ram_Interaction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lifelines54: BinaryAssociation = BinaryAssociation(
    name="lifelines54",
    ends={
        Property(name="ram_Lifeline", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction55", type=ram_Lifeline, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
messages56: BinaryAssociation = BinaryAssociation(
    name="messages56",
    ends={
        Property(name="Message", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=ram_Message, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sendEvent72: BinaryAssociation = BinaryAssociation(
    name="sendEvent72",
    ends={
        Property(name="ram_MessageEnd", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1))
    }
)
receiveEvent73: BinaryAssociation = BinaryAssociation(
    name="receiveEvent73",
    ends={
        Property(name="ram_MessageEnd75", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message74", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1))
    }
)
signature76: BinaryAssociation = BinaryAssociation(
    name="signature76",
    ends={
        Property(name="ram_Operation78", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message77", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
represents67: BinaryAssociation = BinaryAssociation(
    name="represents67",
    ends={
        Property(name="ram_TypedElement", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Lifeline68", type=ram_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
localProperties69: BinaryAssociation = BinaryAssociation(
    name="localProperties69",
    ends={
        Property(name="ram_TemporaryProperty", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Lifeline70", type=ram_TemporaryProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coveredBy71: BinaryAssociation = BinaryAssociation(
    name="coveredBy71",
    ends={
        Property(name="InteractionFragment", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 9999))
    }
)
interaction83: BinaryAssociation = BinaryAssociation(
    name="interaction83",
    ends={
        Property(name="Interaction", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=ram_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
returns84: BinaryAssociation = BinaryAssociation(
    name="returns84",
    ends={
        Property(name="ram_ValueSpecification", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message85", type=ram_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message86: BinaryAssociation = BinaryAssociation(
    name="message86",
    ends={
        Property(name="ram_Message88", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageEnd87", type=ram_Message, multiplicity=Multiplicity(1, 1))
    }
)
assignTo79: BinaryAssociation = BinaryAssociation(
    name="assignTo79",
    ends={
        Property(name="ram_StructuralFeature", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message80", type=ram_StructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
arguments81: BinaryAssociation = BinaryAssociation(
    name="arguments81",
    ends={
        Property(name="ram_ParameterValueMapping", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message82", type=ram_ParameterValueMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
covered89: BinaryAssociation = BinaryAssociation(
    name="covered89",
    ends={
        Property(name="Lifeline", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=ram_Lifeline, multiplicity=Multiplicity(1, 9999))
    }
)
container90: BinaryAssociation = BinaryAssociation(
    name="container90",
    ends={
        Property(name="FragmentContainer", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=ram_FragmentContainer, multiplicity=Multiplicity(1, 1))
    }
)
operands91: BinaryAssociation = BinaryAssociation(
    name="operands91",
    ends={
        Property(name="ram_CombinedFragment", type=ram_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="ram_InteractionOperand", type=ram_CombinedFragment, multiplicity=Multiplicity(1, 1))
    }
)
specification92: BinaryAssociation = BinaryAssociation(
    name="specification92",
    ends={
        Property(name="ram_ValueSpecification93", type=ram_ExecutionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ExecutionStatement", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interactionConstraint94: BinaryAssociation = BinaryAssociation(
    name="interactionConstraint94",
    ends={
        Property(name="ram_ValueSpecification96", type=ram_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_InteractionOperand95", type=ram_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value97: BinaryAssociation = BinaryAssociation(
    name="value97",
    ends={
        Property(name="ram_StructuralFeature98", type=ram_StructuralFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralFeatureValue", type=ram_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value102: BinaryAssociation = BinaryAssociation(
    name="value102",
    ends={
        Property(name="ram_ValueSpecification104", type=ram_ParameterValueMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValueMapping103", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter105: BinaryAssociation = BinaryAssociation(
    name="parameter105",
    ends={
        Property(name="ram_Parameter106", type=ram_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValue", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
fragments107: BinaryAssociation = BinaryAssociation(
    name="fragments107",
    ends={
        Property(name="InteractionFragment108", type=ram_FragmentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter99: BinaryAssociation = BinaryAssociation(
    name="parameter99",
    ends={
        Property(name="ram_Parameter101", type=ram_ParameterValueMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValueMapping100", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
key112: BinaryAssociation = BinaryAssociation(
    name="key112",
    ends={
        Property(name="ram_EObject", type=ram_ContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ContainerMap113", type=ram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value114: BinaryAssociation = BinaryAssociation(
    name="value114",
    ends={
        Property(name="ram_ElementMap", type=ram_ContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ContainerMap115", type=ram_ElementMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
key116: BinaryAssociation = BinaryAssociation(
    name="key116",
    ends={
        Property(name="ram_EObject118", type=ram_ElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ElementMap117", type=ram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value119: BinaryAssociation = BinaryAssociation(
    name="value119",
    ends={
        Property(name="ram_LayoutElement", type=ram_ElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ElementMap120", type=ram_LayoutElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations121: BinaryAssociation = BinaryAssociation(
    name="operations121",
    ends={
        Property(name="ram_Operation123", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Classifier122", type=ram_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type124: BinaryAssociation = BinaryAssociation(
    name="type124",
    ends={
        Property(name="ram_ObjectType126", type=ram_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Reference125", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="ram_ObjectType", type=ram_RCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_RCollection", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
containers110: BinaryAssociation = BinaryAssociation(
    name="containers110",
    ends={
        Property(name="ram_ContainerMap", type=ram_Layout, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Layout111", type=ram_ContainerMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_ram_MappableElement_NamedElement = Generalization(general=NamedElement, specific=ram_MappableElement)
gen_ram_Class_Classifier = Generalization(general=Classifier, specific=ram_Class)
gen_ram_Aspect_NamedElement = Generalization(general=NamedElement, specific=ram_Aspect)
gen_ram_Association_NamedElement = Generalization(general=NamedElement, specific=ram_Association)
gen_ram_AssociationEnd_Property = Generalization(general=Property_, specific=ram_AssociationEnd)
gen_ram_Operation_MappableElement = Generalization(general=MappableElement, specific=ram_Operation)
gen_ram_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=ram_Attribute)
gen_ram_Attribute_TemporaryProperty = Generalization(general=TemporaryProperty, specific=ram_Attribute)
gen_ram_Type_NamedElement = Generalization(general=NamedElement, specific=ram_Type)
gen_ram_Parameter_TypedElement = Generalization(general=TypedElement, specific=ram_Parameter)
gen_ram_PrimitiveType_Type = Generalization(general=Type, specific=ram_PrimitiveType)
gen_ram_PrimitiveType_ImplementationClass = Generalization(general=ImplementationClass, specific=ram_PrimitiveType)
gen_ram_Operation_NamedElement = Generalization(general=NamedElement, specific=ram_Operation)
gen_ram_RInt_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RInt)
gen_ram_RChar_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RChar)
gen_ram_RString_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RString)
gen_ram_RAny_Type = Generalization(general=Type, specific=ram_RAny)
gen_ram_REnum_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_REnum)
gen_ram_REnumLiteral_NamedElement = Generalization(general=NamedElement, specific=ram_REnumLiteral)
gen_ram_ObjectType_Type = Generalization(general=Type, specific=ram_ObjectType)
gen_ram_ObjectType_MappableElement = Generalization(general=MappableElement, specific=ram_ObjectType)
gen_ram_RVoid_Type = Generalization(general=Type, specific=ram_RVoid)
gen_ram_RBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RBoolean)
gen_ram_MessageViewReference_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_MessageViewReference)
gen_ram_Interaction_FragmentContainer = Generalization(general=FragmentContainer, specific=ram_Interaction)
gen_ram_MessageView_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_MessageView)
gen_ram_AspectMessageView_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_AspectMessageView)
gen_ram_AspectMessageView_NamedElement = Generalization(general=NamedElement, specific=ram_AspectMessageView)
gen_ram_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_CombinedFragment)
gen_ram_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=ram_MessageOccurrenceSpecification)
gen_ram_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=ram_MessageOccurrenceSpecification)
gen_ram_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_OccurrenceSpecification)
gen_ram_DestructionOccurrenceSpecification_MessageOccurrenceSpecification = Generalization(general=MessageOccurrenceSpecification, specific=ram_DestructionOccurrenceSpecification)
gen_ram_OriginalBehaviorExecution_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_OriginalBehaviorExecution)
gen_ram_ExecutionStatement_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_ExecutionStatement)
gen_ram_InteractionOperand_FragmentContainer = Generalization(general=FragmentContainer, specific=ram_InteractionOperand)
gen_ram_StructuralFeatureValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_StructuralFeatureValue)
gen_ram_ParameterValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_ParameterValue)
gen_ram_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_OpaqueExpression)
gen_ram_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_LiteralSpecification)
gen_ram_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralString)
gen_ram_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralInteger)
gen_ram_RCollection_Type = Generalization(general=Type, specific=ram_RCollection)
gen_ram_RCollection_ImplementationClass = Generalization(general=ImplementationClass, specific=ram_RCollection)
gen_ram_Classifier_ObjectType = Generalization(general=ObjectType, specific=ram_Classifier)
gen_ram_ImplementationClass_Classifier = Generalization(general=Classifier, specific=ram_ImplementationClass)
gen_ram_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=ram_StructuralFeature)
gen_ram_Reference_Property = Generalization(general=Property_, specific=ram_Reference)
gen_ram_Reference_TemporaryProperty = Generalization(general=TemporaryProperty, specific=ram_Reference)
gen_ram_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=ram_Property)
gen_ram_RSet_RCollection = Generalization(general=RCollection, specific=ram_RSet)
gen_ram_RList_RCollection = Generalization(general=RCollection, specific=ram_RList)
gen_ram_Gate_NamedElement = Generalization(general=NamedElement, specific=ram_Gate)
gen_ram_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralBoolean)
gen_ram_TypedElement_NamedElement = Generalization(general=NamedElement, specific=ram_TypedElement)
gen_ram_Gate_MessageEnd = Generalization(general=MessageEnd, specific=ram_Gate)

# Domain Model
domain_model = DomainModel(
    name="ram",
    types={ram_MappableElement, ram_AbstractMessageView, ram_Instantiation, ram_Layout, ram_Classifier, ram_Association, ram_Type, ram_Class, Classifier, ram_Aspect, NamedElement, ram_StructuralView, ram_NamedElement, ram_Mapping, ram_AssociationEnd, ram_Attribute, Property_, ram_Parameter, StructuralFeature, TemporaryProperty, ram_PrimitiveType, TypedElement, Type, ImplementationClass, ram_Operation, MappableElement, ram_RInt, ram_RChar, ram_RString, ram_RAny, ram_REnum, ram_REnumLiteral, ram_ObjectType, ram_RVoid, ram_RBoolean, PrimitiveType, ram_Interaction, ram_MessageViewReference, FragmentContainer, ram_AspectMessageView, ram_MessageView, AbstractMessageView, ram_Gate, ram_TypedElement, ram_Lifeline, ram_Message, ram_Reference, ram_MessageEnd, ram_TemporaryProperty, ram_InteractionFragment, ram_ValueSpecification, ram_StructuralFeature, ram_ParameterValueMapping, ram_FragmentContainer, ram_CombinedFragment, ram_MessageOccurrenceSpecification, OccurrenceSpecification, MessageEnd, ram_OccurrenceSpecification, InteractionFragment, ram_DestructionOccurrenceSpecification, MessageOccurrenceSpecification, ram_OriginalBehaviorExecution, ram_ExecutionStatement, ram_StructuralFeatureValue, ValueSpecification, ram_InteractionOperand, ram_ParameterValue, ram_OpaqueExpression, ram_LiteralSpecification, ram_LiteralString, LiteralSpecification, ram_LiteralInteger, ram_RCollection, ram_EObject, ram_ElementMap, ram_LayoutElement, ObjectType, ram_ImplementationClass, ram_Property, ram_RSet, RCollection, ram_RList, ram_ContainerMap, ram_LiteralBoolean, Visibility, ReferenceType, MessageSort, InteractionOperatorKind, InstantiationType},
    associations={mandatoryAspectParameters1, messageViews3, instantiations5, layout7, classes9, associations11, types13, structuralView0, assoc20, myClass21, ends22, mappings24, externalAspect26, associationEnds15, attributes16, superTypes17, returnType35, parameters37, type39, type41, toElements29, fromElement32, literals44, enum45, specifies48, specification50, references52, affectedBy46, properties57, formalGates59, pointcut61, advice64, lifelines54, messages56, sendEvent72, receiveEvent73, signature76, represents67, localProperties69, coveredBy71, interaction83, returns84, message86, assignTo79, arguments81, covered89, container90, operands91, specification92, interactionConstraint94, value97, value102, parameter105, fragments107, parameter99, key112, value114, key116, value119, operations121, type124, type109, containers110},
    generalizations={gen_ram_MappableElement_NamedElement, gen_ram_Class_Classifier, gen_ram_Aspect_NamedElement, gen_ram_Association_NamedElement, gen_ram_AssociationEnd_Property, gen_ram_Operation_MappableElement, gen_ram_Attribute_StructuralFeature, gen_ram_Attribute_TemporaryProperty, gen_ram_Type_NamedElement, gen_ram_Parameter_TypedElement, gen_ram_PrimitiveType_Type, gen_ram_PrimitiveType_ImplementationClass, gen_ram_Operation_NamedElement, gen_ram_RInt_PrimitiveType, gen_ram_RChar_PrimitiveType, gen_ram_RString_PrimitiveType, gen_ram_RAny_Type, gen_ram_REnum_PrimitiveType, gen_ram_REnumLiteral_NamedElement, gen_ram_ObjectType_Type, gen_ram_ObjectType_MappableElement, gen_ram_RVoid_Type, gen_ram_RBoolean_PrimitiveType, gen_ram_MessageViewReference_AbstractMessageView, gen_ram_Interaction_FragmentContainer, gen_ram_MessageView_AbstractMessageView, gen_ram_AspectMessageView_AbstractMessageView, gen_ram_AspectMessageView_NamedElement, gen_ram_CombinedFragment_InteractionFragment, gen_ram_MessageOccurrenceSpecification_OccurrenceSpecification, gen_ram_MessageOccurrenceSpecification_MessageEnd, gen_ram_OccurrenceSpecification_InteractionFragment, gen_ram_DestructionOccurrenceSpecification_MessageOccurrenceSpecification, gen_ram_OriginalBehaviorExecution_InteractionFragment, gen_ram_ExecutionStatement_InteractionFragment, gen_ram_InteractionOperand_FragmentContainer, gen_ram_StructuralFeatureValue_ValueSpecification, gen_ram_ParameterValue_ValueSpecification, gen_ram_OpaqueExpression_ValueSpecification, gen_ram_LiteralSpecification_ValueSpecification, gen_ram_LiteralString_LiteralSpecification, gen_ram_LiteralInteger_LiteralSpecification, gen_ram_RCollection_Type, gen_ram_RCollection_ImplementationClass, gen_ram_Classifier_ObjectType, gen_ram_ImplementationClass_Classifier, gen_ram_StructuralFeature_TypedElement, gen_ram_Reference_Property, gen_ram_Reference_TemporaryProperty, gen_ram_Property_StructuralFeature, gen_ram_RSet_RCollection, gen_ram_RList_RCollection, gen_ram_Gate_NamedElement, gen_ram_LiteralBoolean_LiteralSpecification, gen_ram_TypedElement_NamedElement, gen_ram_Gate_MessageEnd},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)