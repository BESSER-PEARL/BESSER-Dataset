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
ram_Aspect = Class(name="ram::Aspect")
NamedElement = Class(name="NamedElement")
ram_StructuralView = Class(name="ram::StructuralView")
ram_MappableElement = Class(name="ram::MappableElement", is_abstract=True)
ram_Classifier = Class(name="ram::Classifier", is_abstract=True)
ram_Association = Class(name="ram::Association")
ram_Type = Class(name="ram::Type", is_abstract=True)
ram_Class = Class(name="ram::Class")
Classifier = Class(name="Classifier")
ram_Attribute = Class(name="ram::Attribute")
ram_AssociationEnd = Class(name="ram::AssociationEnd")
Property_ = Class(name="Property")
ram_AbstractMessageView = Class(name="ram::AbstractMessageView", is_abstract=True)
ram_Instantiation = Class(name="ram::Instantiation")
ram_Layout = Class(name="ram::Layout")
ram_StateView = Class(name="ram::StateView")
ram_ClassifierMapping = Class(name="ram::ClassifierMapping")
ram_Mapping = Class(name="ram::Mapping", is_abstract=True)
ram_Operation = Class(name="ram::Operation")
MappableElement = Class(name="MappableElement")
ram_Parameter = Class(name="ram::Parameter")
ram_NamedElement = Class(name="ram::NamedElement", is_abstract=True)
ObjectType = Class(name="ObjectType")
ImplementationClass = Class(name="ImplementationClass")
ram_ObjectType = Class(name="ram::ObjectType", is_abstract=True)
Type = Class(name="Type")
ram_RVoid = Class(name="ram::RVoid")
ram_RBoolean = Class(name="ram::RBoolean")
PrimitiveType = Class(name="PrimitiveType")
ram_RInt = Class(name="ram::RInt")
ram_RChar = Class(name="ram::RChar")
StructuralFeature = Class(name="StructuralFeature")
TemporaryProperty = Class(name="TemporaryProperty")
ram_PrimitiveType = Class(name="ram::PrimitiveType", is_abstract=True)
TypedElement = Class(name="TypedElement")
ram_REnum = Class(name="ram::REnum")
ram_REnumLiteral = Class(name="ram::REnumLiteral")
ram_AspectMessageView = Class(name="ram::AspectMessageView")
ram_MessageView = Class(name="ram::MessageView")
AbstractMessageView = Class(name="AbstractMessageView")
ram_Interaction = Class(name="ram::Interaction")
ram_MessageViewReference = Class(name="ram::MessageViewReference")
FragmentContainer = Class(name="FragmentContainer")
ram_RString = Class(name="ram::RString")
ram_RAny = Class(name="ram::RAny")
ram_TypedElement = Class(name="ram::TypedElement", is_abstract=True)
ram_TemporaryProperty = Class(name="ram::TemporaryProperty", is_abstract=True)
ram_InteractionFragment = Class(name="ram::InteractionFragment", is_abstract=True)
ram_MessageEnd = Class(name="ram::MessageEnd", is_abstract=True)
ram_Lifeline = Class(name="ram::Lifeline")
ram_Message = Class(name="ram::Message")
ram_Reference = Class(name="ram::Reference")
ram_Gate = Class(name="ram::Gate")
ram_ValueSpecification = Class(name="ram::ValueSpecification", is_abstract=True)
ram_MessageOccurrenceSpecification = Class(name="ram::MessageOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
MessageEnd = Class(name="MessageEnd")
ram_OccurrenceSpecification = Class(name="ram::OccurrenceSpecification")
InteractionFragment = Class(name="InteractionFragment")
ram_DestructionOccurrenceSpecification = Class(name="ram::DestructionOccurrenceSpecification")
MessageOccurrenceSpecification = Class(name="MessageOccurrenceSpecification")
ram_FragmentContainer = Class(name="ram::FragmentContainer", is_abstract=True)
ram_CombinedFragment = Class(name="ram::CombinedFragment")
ram_StructuralFeature = Class(name="ram::StructuralFeature", is_abstract=True)
ram_ParameterValueMapping = Class(name="ram::ParameterValueMapping")
ram_StructuralFeatureValue = Class(name="ram::StructuralFeatureValue")
ValueSpecification = Class(name="ValueSpecification")
ram_InteractionOperand = Class(name="ram::InteractionOperand")
ram_OriginalBehaviorExecution = Class(name="ram::OriginalBehaviorExecution")
ram_ExecutionStatement = Class(name="ram::ExecutionStatement")
ram_OpaqueExpression = Class(name="ram::OpaqueExpression")
ram_LiteralSpecification = Class(name="ram::LiteralSpecification", is_abstract=True)
ram_LiteralString = Class(name="ram::LiteralString")
LiteralSpecification = Class(name="LiteralSpecification")
ram_LiteralInteger = Class(name="ram::LiteralInteger")
ram_RCollection = Class(name="ram::RCollection", is_abstract=True)
ram_RSet = Class(name="ram::RSet")
RCollection = Class(name="RCollection")
ram_RSequence = Class(name="ram::RSequence")
ram_ContainerMap = Class(name="ram::ContainerMap")
ram_ParameterValue = Class(name="ram::ParameterValue")
ram_TypeParameter = Class(name="ram::TypeParameter")
ram_ImplementationClass = Class(name="ram::ImplementationClass")
ram_Property = Class(name="ram::Property", is_abstract=True)
ram_EObject = Class(name="ram::EObject")
ram_ElementMap = Class(name="ram::ElementMap")
ram_LayoutElement = Class(name="ram::LayoutElement")
ram_AttributeMapping = Class(name="ram::AttributeMapping")
ram_ParameterMapping = Class(name="ram::ParameterMapping")
ram_StateMachine = Class(name="ram::StateMachine")
ram_LiteralBoolean = Class(name="ram::LiteralBoolean")
Mapping = Class(name="Mapping")
ram_OperationMapping = Class(name="ram::OperationMapping")
ram_Constraint = Class(name="ram::Constraint")
ram_RDouble = Class(name="ram::RDouble")
ram_RFloat = Class(name="ram::RFloat")
ram_TransitionSubstitution = Class(name="ram::TransitionSubstitution")
Substitution = Class(name="Substitution")
ram_State = Class(name="ram::State")
ram_Transition = Class(name="ram::Transition")
ram_Substitution = Class(name="ram::Substitution")
ram_RArray = Class(name="ram::RArray")
ram_RLong = Class(name="ram::RLong")

# ram_Aspect class attributes and methods

# NamedElement class attributes and methods

# ram_StructuralView class attributes and methods

# ram_MappableElement class attributes and methods

# ram_Classifier class attributes and methods

# ram_Association class attributes and methods

# ram_Type class attributes and methods

# ram_Class class attributes and methods
ram_Class_partial: Property = Property(name="partial", type=BooleanType)
ram_Class_abstract: Property = Property(name="abstract", type=BooleanType)
ram_Class.attributes={ram_Class_partial, ram_Class_abstract}

# Classifier class attributes and methods

# ram_Attribute class attributes and methods

# ram_AssociationEnd class attributes and methods
ram_AssociationEnd_navigable: Property = Property(name="navigable", type=BooleanType)
ram_AssociationEnd_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
ram_AssociationEnd.attributes={ram_AssociationEnd_navigable}
ram_AssociationEnd.methods={ram_AssociationEnd_m_getType}

# Property class attributes and methods

# ram_AbstractMessageView class attributes and methods

# ram_Instantiation class attributes and methods
ram_Instantiation_type: Property = Property(name="type", type=StringType)
ram_Instantiation.attributes={ram_Instantiation_type}

# ram_Layout class attributes and methods

# ram_StateView class attributes and methods

# ram_ClassifierMapping class attributes and methods

# ram_Mapping class attributes and methods
ram_Mapping_m_getFromElement: Method = Method(name="getFromElement", parameters={}, type=StringType)
ram_Mapping_m_getToElement: Method = Method(name="getToElement", parameters={}, type=StringType)
ram_Mapping.methods={ram_Mapping_m_getFromElement, ram_Mapping_m_getToElement}

# ram_Operation class attributes and methods
ram_Operation_abstract: Property = Property(name="abstract", type=BooleanType)
ram_Operation_visibility: Property = Property(name="visibility", type=StringType)
ram_Operation_static: Property = Property(name="static", type=BooleanType)
ram_Operation_partial: Property = Property(name="partial", type=BooleanType)
ram_Operation.attributes={ram_Operation_static, ram_Operation_partial, ram_Operation_visibility, ram_Operation_abstract}

# MappableElement class attributes and methods

# ram_Parameter class attributes and methods

# ram_NamedElement class attributes and methods
ram_NamedElement_name: Property = Property(name="name", type=StringType)
ram_NamedElement.attributes={ram_NamedElement_name}

# ObjectType class attributes and methods

# ImplementationClass class attributes and methods

# ram_ObjectType class attributes and methods

# Type class attributes and methods

# ram_RVoid class attributes and methods
ram_RVoid_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RVoid.methods={ram_RVoid_m_getName}

# ram_RBoolean class attributes and methods
ram_RBoolean_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RBoolean_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RBoolean.methods={ram_RBoolean_m_getInstanceClassName, ram_RBoolean_m_getName}

# PrimitiveType class attributes and methods

# ram_RInt class attributes and methods
ram_RInt_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RInt_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RInt.methods={ram_RInt_m_getName, ram_RInt_m_getInstanceClassName}

# ram_RChar class attributes and methods
ram_RChar_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RChar_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RChar.methods={ram_RChar_m_getInstanceClassName, ram_RChar_m_getName}

# StructuralFeature class attributes and methods

# TemporaryProperty class attributes and methods

# ram_PrimitiveType class attributes and methods

# TypedElement class attributes and methods

# ram_REnum class attributes and methods

# ram_REnumLiteral class attributes and methods

# ram_AspectMessageView class attributes and methods

# ram_MessageView class attributes and methods

# AbstractMessageView class attributes and methods

# ram_Interaction class attributes and methods

# ram_MessageViewReference class attributes and methods

# FragmentContainer class attributes and methods

# ram_RString class attributes and methods
ram_RString_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RString_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RString.methods={ram_RString_m_getInstanceClassName, ram_RString_m_getName}

# ram_RAny class attributes and methods
ram_RAny_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RAny.methods={ram_RAny_m_getName}

# ram_TypedElement class attributes and methods
ram_TypedElement_m_getType: Method = Method(name="getType", parameters={}, type=Type)
ram_TypedElement.methods={ram_TypedElement_m_getType}

# ram_TemporaryProperty class attributes and methods

# ram_InteractionFragment class attributes and methods

# ram_MessageEnd class attributes and methods

# ram_Lifeline class attributes and methods

# ram_Message class attributes and methods
ram_Message_selfMessage: Property = Property(name="selfMessage", type=BooleanType)
ram_Message_messageSort: Property = Property(name="messageSort", type=StringType)
ram_Message.attributes={ram_Message_selfMessage, ram_Message_messageSort}

# ram_Reference class attributes and methods

# ram_Gate class attributes and methods

# ram_ValueSpecification class attributes and methods

# ram_MessageOccurrenceSpecification class attributes and methods

# OccurrenceSpecification class attributes and methods

# MessageEnd class attributes and methods

# ram_OccurrenceSpecification class attributes and methods

# InteractionFragment class attributes and methods

# ram_DestructionOccurrenceSpecification class attributes and methods

# MessageOccurrenceSpecification class attributes and methods

# ram_FragmentContainer class attributes and methods

# ram_CombinedFragment class attributes and methods
ram_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
ram_CombinedFragment.attributes={ram_CombinedFragment_interactionOperator}

# ram_StructuralFeature class attributes and methods
ram_StructuralFeature_static: Property = Property(name="static", type=BooleanType)
ram_StructuralFeature.attributes={ram_StructuralFeature_static}

# ram_ParameterValueMapping class attributes and methods

# ram_StructuralFeatureValue class attributes and methods

# ValueSpecification class attributes and methods

# ram_InteractionOperand class attributes and methods

# ram_OriginalBehaviorExecution class attributes and methods

# ram_ExecutionStatement class attributes and methods

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

# ram_RSet class attributes and methods

# RCollection class attributes and methods

# ram_RSequence class attributes and methods

# ram_ContainerMap class attributes and methods

# ram_ParameterValue class attributes and methods

# ram_TypeParameter class attributes and methods

# ram_ImplementationClass class attributes and methods
ram_ImplementationClass_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ram_ImplementationClass_interface: Property = Property(name="interface", type=BooleanType)
ram_ImplementationClass.attributes={ram_ImplementationClass_instanceClassName, ram_ImplementationClass_interface}

# ram_Property class attributes and methods
ram_Property_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ram_Property_upperBound: Property = Property(name="upperBound", type=IntegerType)
ram_Property_referenceType: Property = Property(name="referenceType", type=StringType)
ram_Property.attributes={ram_Property_upperBound, ram_Property_lowerBound, ram_Property_referenceType}

# ram_EObject class attributes and methods

# ram_ElementMap class attributes and methods

# ram_LayoutElement class attributes and methods
ram_LayoutElement_y: Property = Property(name="y", type=FloatType)
ram_LayoutElement_x: Property = Property(name="x", type=FloatType)
ram_LayoutElement.attributes={ram_LayoutElement_x, ram_LayoutElement_y}

# ram_AttributeMapping class attributes and methods

# ram_ParameterMapping class attributes and methods

# ram_StateMachine class attributes and methods

# ram_LiteralBoolean class attributes and methods
ram_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
ram_LiteralBoolean.attributes={ram_LiteralBoolean_value}

# Mapping class attributes and methods

# ram_OperationMapping class attributes and methods

# ram_Constraint class attributes and methods

# ram_RDouble class attributes and methods
ram_RDouble_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RDouble_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RDouble.methods={ram_RDouble_m_getInstanceClassName, ram_RDouble_m_getName}

# ram_RFloat class attributes and methods
ram_RFloat_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RFloat_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RFloat.methods={ram_RFloat_m_getName, ram_RFloat_m_getInstanceClassName}

# ram_TransitionSubstitution class attributes and methods

# Substitution class attributes and methods

# ram_State class attributes and methods

# ram_Transition class attributes and methods

# ram_Substitution class attributes and methods

# ram_RArray class attributes and methods
ram_RArray_size: Property = Property(name="size", type=IntegerType)
ram_RArray_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RArray_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RArray.attributes={ram_RArray_size}
ram_RArray.methods={ram_RArray_m_getName, ram_RArray_m_getInstanceClassName}

# ram_RLong class attributes and methods
ram_RLong_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RLong_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RLong.methods={ram_RLong_m_getName, ram_RLong_m_getInstanceClassName}

# Relationships
structuralView0: BinaryAssociation = BinaryAssociation(
    name="structuralView0",
    ends={
        Property(name="ram_StructuralView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect", type=ram_StructuralView, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mandatoryAspectParameters1: BinaryAssociation = BinaryAssociation(
    name="mandatoryAspectParameters1",
    ends={
        Property(name="ram_MappableElement", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect2", type=ram_MappableElement, multiplicity=Multiplicity(0, 9999))
    }
)
classes11: BinaryAssociation = BinaryAssociation(
    name="classes11",
    ends={
        Property(name="ram_Classifier", type=ram_StructuralView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralView12", type=ram_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations13: BinaryAssociation = BinaryAssociation(
    name="associations13",
    ends={
        Property(name="ram_Association", type=ram_StructuralView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralView14", type=ram_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types15: BinaryAssociation = BinaryAssociation(
    name="types15",
    ends={
        Property(name="ram_Type", type=ram_StructuralView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralView16", type=ram_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes17: BinaryAssociation = BinaryAssociation(
    name="attributes17",
    ends={
        Property(name="ram_Attribute", type=ram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Class", type=ram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes18: BinaryAssociation = BinaryAssociation(
    name="superTypes18",
    ends={
        Property(name="ram_Classifier20", type=ram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Class19", type=ram_Classifier, multiplicity=Multiplicity(0, 9999))
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
stateViews9: BinaryAssociation = BinaryAssociation(
    name="stateViews9",
    ends={
        Property(name="ram_StateView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect10", type=ram_StateView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings24: BinaryAssociation = BinaryAssociation(
    name="mappings24",
    ends={
        Property(name="ram_ClassifierMapping", type=ram_Instantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Instantiation25", type=ram_ClassifierMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalAspect26: BinaryAssociation = BinaryAssociation(
    name="externalAspect26",
    ends={
        Property(name="ram_Aspect28", type=ram_Instantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Instantiation27", type=ram_Aspect, multiplicity=Multiplicity(1, 1))
    }
)
returnType29: BinaryAssociation = BinaryAssociation(
    name="returnType29",
    ends={
        Property(name="ram_Type30", type=ram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Operation", type=ram_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="ram_Parameter", type=ram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Operation32", type=ram_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assoc21: BinaryAssociation = BinaryAssociation(
    name="assoc21",
    ends={
        Property(name="Association", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ends", type=ram_Association, multiplicity=Multiplicity(1, 1))
    }
)
classifier22: BinaryAssociation = BinaryAssociation(
    name="classifier22",
    ends={
        Property(name="Classifier", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnds", type=ram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
ends23: BinaryAssociation = BinaryAssociation(
    name="ends23",
    ends={
        Property(name="AssociationEnd", type=ram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc", type=ram_AssociationEnd, multiplicity=Multiplicity(2, 2))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="ram_Parameter36", type=ram_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Type37", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="ram_PrimitiveType", type=ram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Attribute34", type=ram_PrimitiveType, multiplicity=Multiplicity(1, 1))
    }
)
literals38: BinaryAssociation = BinaryAssociation(
    name="literals38",
    ends={
        Property(name="REnumLiteral", type=ram_REnum, multiplicity=Multiplicity(1, 1)),
        Property(name="enum", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enum39: BinaryAssociation = BinaryAssociation(
    name="enum39",
    ends={
        Property(name="REnum", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=ram_REnum, multiplicity=Multiplicity(1, 1))
    }
)
affectedBy40: BinaryAssociation = BinaryAssociation(
    name="affectedBy40",
    ends={
        Property(name="ram_AspectMessageView", type=ram_AbstractMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AbstractMessageView41", type=ram_AspectMessageView, multiplicity=Multiplicity(0, 9999))
    }
)
specifies42: BinaryAssociation = BinaryAssociation(
    name="specifies42",
    ends={
        Property(name="ram_Operation43", type=ram_MessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageView", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
specification44: BinaryAssociation = BinaryAssociation(
    name="specification44",
    ends={
        Property(name="ram_Interaction", type=ram_MessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageView45", type=ram_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
references46: BinaryAssociation = BinaryAssociation(
    name="references46",
    ends={
        Property(name="ram_MessageView47", type=ram_MessageViewReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageViewReference", type=ram_MessageView, multiplicity=Multiplicity(1, 1))
    }
)
pointcut55: BinaryAssociation = BinaryAssociation(
    name="pointcut55",
    ends={
        Property(name="ram_Operation57", type=ram_AspectMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AspectMessageView56", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
advice58: BinaryAssociation = BinaryAssociation(
    name="advice58",
    ends={
        Property(name="ram_Interaction60", type=ram_AspectMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AspectMessageView59", type=ram_Interaction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
represents61: BinaryAssociation = BinaryAssociation(
    name="represents61",
    ends={
        Property(name="ram_TypedElement", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Lifeline62", type=ram_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
localProperties63: BinaryAssociation = BinaryAssociation(
    name="localProperties63",
    ends={
        Property(name="ram_TemporaryProperty", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Lifeline64", type=ram_TemporaryProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coveredBy65: BinaryAssociation = BinaryAssociation(
    name="coveredBy65",
    ends={
        Property(name="InteractionFragment", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 9999))
    }
)
sendEvent66: BinaryAssociation = BinaryAssociation(
    name="sendEvent66",
    ends={
        Property(name="ram_MessageEnd", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1))
    }
)
lifelines48: BinaryAssociation = BinaryAssociation(
    name="lifelines48",
    ends={
        Property(name="ram_Lifeline", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction49", type=ram_Lifeline, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
messages50: BinaryAssociation = BinaryAssociation(
    name="messages50",
    ends={
        Property(name="Message", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=ram_Message, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties51: BinaryAssociation = BinaryAssociation(
    name="properties51",
    ends={
        Property(name="ram_Reference", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction52", type=ram_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGates53: BinaryAssociation = BinaryAssociation(
    name="formalGates53",
    ends={
        Property(name="ram_Gate", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction54", type=ram_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returns78: BinaryAssociation = BinaryAssociation(
    name="returns78",
    ends={
        Property(name="ram_ValueSpecification", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message79", type=ram_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
message80: BinaryAssociation = BinaryAssociation(
    name="message80",
    ends={
        Property(name="ram_Message82", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageEnd81", type=ram_Message, multiplicity=Multiplicity(1, 1))
    }
)
covered83: BinaryAssociation = BinaryAssociation(
    name="covered83",
    ends={
        Property(name="Lifeline", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=ram_Lifeline, multiplicity=Multiplicity(1, 9999))
    }
)
container84: BinaryAssociation = BinaryAssociation(
    name="container84",
    ends={
        Property(name="FragmentContainer", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=ram_FragmentContainer, multiplicity=Multiplicity(1, 1))
    }
)
receiveEvent67: BinaryAssociation = BinaryAssociation(
    name="receiveEvent67",
    ends={
        Property(name="ram_MessageEnd69", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message68", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1))
    }
)
signature70: BinaryAssociation = BinaryAssociation(
    name="signature70",
    ends={
        Property(name="ram_Operation72", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message71", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
assignTo73: BinaryAssociation = BinaryAssociation(
    name="assignTo73",
    ends={
        Property(name="ram_StructuralFeature", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message74", type=ram_StructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
arguments75: BinaryAssociation = BinaryAssociation(
    name="arguments75",
    ends={
        Property(name="ram_ParameterValueMapping", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message76", type=ram_ParameterValueMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interaction77: BinaryAssociation = BinaryAssociation(
    name="interaction77",
    ends={
        Property(name="Interaction", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=ram_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
interactionConstraint88: BinaryAssociation = BinaryAssociation(
    name="interactionConstraint88",
    ends={
        Property(name="ram_ValueSpecification90", type=ram_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_InteractionOperand89", type=ram_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value91: BinaryAssociation = BinaryAssociation(
    name="value91",
    ends={
        Property(name="ram_StructuralFeature92", type=ram_StructuralFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralFeatureValue", type=ram_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
operands85: BinaryAssociation = BinaryAssociation(
    name="operands85",
    ends={
        Property(name="ram_InteractionOperand", type=ram_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_CombinedFragment", type=ram_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specification86: BinaryAssociation = BinaryAssociation(
    name="specification86",
    ends={
        Property(name="ram_ValueSpecification87", type=ram_ExecutionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ExecutionStatement", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter99: BinaryAssociation = BinaryAssociation(
    name="parameter99",
    ends={
        Property(name="ram_Parameter100", type=ram_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValue", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
fragments101: BinaryAssociation = BinaryAssociation(
    name="fragments101",
    ends={
        Property(name="InteractionFragment102", type=ram_FragmentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type103: BinaryAssociation = BinaryAssociation(
    name="type103",
    ends={
        Property(name="ram_ObjectType", type=ram_RCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_RCollection", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
containers104: BinaryAssociation = BinaryAssociation(
    name="containers104",
    ends={
        Property(name="ram_ContainerMap", type=ram_Layout, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Layout105", type=ram_ContainerMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameter93: BinaryAssociation = BinaryAssociation(
    name="parameter93",
    ends={
        Property(name="ram_Parameter95", type=ram_ParameterValueMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValueMapping94", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
value96: BinaryAssociation = BinaryAssociation(
    name="value96",
    ends={
        Property(name="ram_ValueSpecification98", type=ram_ParameterValueMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValueMapping97", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations115: BinaryAssociation = BinaryAssociation(
    name="operations115",
    ends={
        Property(name="ram_Operation117", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Classifier116", type=ram_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnds118: BinaryAssociation = BinaryAssociation(
    name="associationEnds118",
    ends={
        Property(name="AssociationEnd119", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=ram_AssociationEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters120: BinaryAssociation = BinaryAssociation(
    name="typeParameters120",
    ends={
        Property(name="ram_TypeParameter", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Classifier121", type=ram_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type122: BinaryAssociation = BinaryAssociation(
    name="type122",
    ends={
        Property(name="ram_ObjectType124", type=ram_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Reference123", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
key106: BinaryAssociation = BinaryAssociation(
    name="key106",
    ends={
        Property(name="ram_EObject", type=ram_ContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ContainerMap107", type=ram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value108: BinaryAssociation = BinaryAssociation(
    name="value108",
    ends={
        Property(name="ram_ElementMap", type=ram_ContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ContainerMap109", type=ram_ElementMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
key110: BinaryAssociation = BinaryAssociation(
    name="key110",
    ends={
        Property(name="ram_EObject112", type=ram_ElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ElementMap111", type=ram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value113: BinaryAssociation = BinaryAssociation(
    name="value113",
    ends={
        Property(name="ram_LayoutElement", type=ram_ElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ElementMap114", type=ram_LayoutElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeMappings127: BinaryAssociation = BinaryAssociation(
    name="attributeMappings127",
    ends={
        Property(name="ram_AttributeMapping", type=ram_ClassifierMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ClassifierMapping128", type=ram_AttributeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromElement129: BinaryAssociation = BinaryAssociation(
    name="fromElement129",
    ends={
        Property(name="ram_Classifier131", type=ram_ClassifierMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ClassifierMapping130", type=ram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
toElement132: BinaryAssociation = BinaryAssociation(
    name="toElement132",
    ends={
        Property(name="ram_Classifier134", type=ram_ClassifierMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ClassifierMapping133", type=ram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
fromElement135: BinaryAssociation = BinaryAssociation(
    name="fromElement135",
    ends={
        Property(name="ram_Attribute137", type=ram_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AttributeMapping136", type=ram_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
toElement138: BinaryAssociation = BinaryAssociation(
    name="toElement138",
    ends={
        Property(name="ram_Attribute140", type=ram_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AttributeMapping139", type=ram_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
parameterMappings141: BinaryAssociation = BinaryAssociation(
    name="parameterMappings141",
    ends={
        Property(name="ram_ParameterMapping", type=ram_OperationMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_OperationMapping142", type=ram_ParameterMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromElement143: BinaryAssociation = BinaryAssociation(
    name="fromElement143",
    ends={
        Property(name="ram_Operation145", type=ram_OperationMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_OperationMapping144", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
toElement146: BinaryAssociation = BinaryAssociation(
    name="toElement146",
    ends={
        Property(name="ram_Operation148", type=ram_OperationMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_OperationMapping147", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
fromElement149: BinaryAssociation = BinaryAssociation(
    name="fromElement149",
    ends={
        Property(name="ram_Parameter151", type=ram_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterMapping150", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
toElement152: BinaryAssociation = BinaryAssociation(
    name="toElement152",
    ends={
        Property(name="ram_Parameter154", type=ram_ParameterMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterMapping153", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
stateMachines155: BinaryAssociation = BinaryAssociation(
    name="stateMachines155",
    ends={
        Property(name="ram_StateMachine", type=ram_StateView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateView156", type=ram_StateMachine, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specifies157: BinaryAssociation = BinaryAssociation(
    name="specifies157",
    ends={
        Property(name="ram_Classifier159", type=ram_StateView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateView158", type=ram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
operationMappings125: BinaryAssociation = BinaryAssociation(
    name="operationMappings125",
    ends={
        Property(name="ram_OperationMapping", type=ram_ClassifierMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ClassifierMapping126", type=ram_OperationMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState169: BinaryAssociation = BinaryAssociation(
    name="endState169",
    ends={
        Property(name="State", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=ram_State, multiplicity=Multiplicity(1, 1))
    }
)
startState170: BinaryAssociation = BinaryAssociation(
    name="startState170",
    ends={
        Property(name="State171", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=ram_State, multiplicity=Multiplicity(1, 1))
    }
)
signature172: BinaryAssociation = BinaryAssociation(
    name="signature172",
    ends={
        Property(name="ram_Operation174", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Transition173", type=ram_Operation, multiplicity=Multiplicity(0, 1))
    }
)
guard175: BinaryAssociation = BinaryAssociation(
    name="guard175",
    ends={
        Property(name="ram_Constraint", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Transition176", type=ram_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomings177: BinaryAssociation = BinaryAssociation(
    name="incomings177",
    ends={
        Property(name="Transition", type=ram_State, multiplicity=Multiplicity(1, 1)),
        Property(name="endState", type=ram_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoings178: BinaryAssociation = BinaryAssociation(
    name="outgoings178",
    ends={
        Property(name="Transition179", type=ram_State, multiplicity=Multiplicity(1, 1)),
        Property(name="startState", type=ram_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
Specification180: BinaryAssociation = BinaryAssociation(
    name="Specification180",
    ends={
        Property(name="ram_ValueSpecification182", type=ram_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Constraint181", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start160: BinaryAssociation = BinaryAssociation(
    name="start160",
    ends={
        Property(name="ram_State", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine161", type=ram_State, multiplicity=Multiplicity(1, 1))
    }
)
states162: BinaryAssociation = BinaryAssociation(
    name="states162",
    ends={
        Property(name="ram_State164", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine163", type=ram_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions165: BinaryAssociation = BinaryAssociation(
    name="transitions165",
    ends={
        Property(name="ram_Transition", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine166", type=ram_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitutions167: BinaryAssociation = BinaryAssociation(
    name="substitutions167",
    ends={
        Property(name="ram_Substitution", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine168", type=ram_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type191: BinaryAssociation = BinaryAssociation(
    name="type191",
    ends={
        Property(name="ram_ObjectType192", type=ram_RArray, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_RArray", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
from183: BinaryAssociation = BinaryAssociation(
    name="from183",
    ends={
        Property(name="ram_Transition184", type=ram_TransitionSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TransitionSubstitution", type=ram_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to185: BinaryAssociation = BinaryAssociation(
    name="to185",
    ends={
        Property(name="ram_Transition187", type=ram_TransitionSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TransitionSubstitution186", type=ram_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
genericType188: BinaryAssociation = BinaryAssociation(
    name="genericType188",
    ends={
        Property(name="ram_ObjectType190", type=ram_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TypeParameter189", type=ram_ObjectType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ram_Aspect_NamedElement = Generalization(general=NamedElement, specific=ram_Aspect)
gen_ram_Class_Classifier = Generalization(general=Classifier, specific=ram_Class)
gen_ram_AssociationEnd_Property = Generalization(general=Property_, specific=ram_AssociationEnd)
gen_ram_MappableElement_NamedElement = Generalization(general=NamedElement, specific=ram_MappableElement)
gen_ram_Operation_NamedElement = Generalization(general=NamedElement, specific=ram_Operation)
gen_ram_Operation_MappableElement = Generalization(general=MappableElement, specific=ram_Operation)
gen_ram_Association_NamedElement = Generalization(general=NamedElement, specific=ram_Association)
gen_ram_PrimitiveType_ObjectType = Generalization(general=ObjectType, specific=ram_PrimitiveType)
gen_ram_PrimitiveType_ImplementationClass = Generalization(general=ImplementationClass, specific=ram_PrimitiveType)
gen_ram_ObjectType_Type = Generalization(general=Type, specific=ram_ObjectType)
gen_ram_ObjectType_MappableElement = Generalization(general=MappableElement, specific=ram_ObjectType)
gen_ram_RVoid_Type = Generalization(general=Type, specific=ram_RVoid)
gen_ram_RBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RBoolean)
gen_ram_RInt_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RInt)
gen_ram_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=ram_Attribute)
gen_ram_Attribute_TemporaryProperty = Generalization(general=TemporaryProperty, specific=ram_Attribute)
gen_ram_Attribute_MappableElement = Generalization(general=MappableElement, specific=ram_Attribute)
gen_ram_Type_NamedElement = Generalization(general=NamedElement, specific=ram_Type)
gen_ram_Parameter_TypedElement = Generalization(general=TypedElement, specific=ram_Parameter)
gen_ram_Parameter_MappableElement = Generalization(general=MappableElement, specific=ram_Parameter)
gen_ram_REnum_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_REnum)
gen_ram_REnumLiteral_NamedElement = Generalization(general=NamedElement, specific=ram_REnumLiteral)
gen_ram_MessageView_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_MessageView)
gen_ram_MessageViewReference_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_MessageViewReference)
gen_ram_RChar_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RChar)
gen_ram_RString_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RString)
gen_ram_RAny_Type = Generalization(general=Type, specific=ram_RAny)
gen_ram_Interaction_FragmentContainer = Generalization(general=FragmentContainer, specific=ram_Interaction)
gen_ram_AspectMessageView_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_AspectMessageView)
gen_ram_AspectMessageView_NamedElement = Generalization(general=NamedElement, specific=ram_AspectMessageView)
gen_ram_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=ram_MessageOccurrenceSpecification)
gen_ram_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=ram_MessageOccurrenceSpecification)
gen_ram_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_OccurrenceSpecification)
gen_ram_DestructionOccurrenceSpecification_MessageOccurrenceSpecification = Generalization(general=MessageOccurrenceSpecification, specific=ram_DestructionOccurrenceSpecification)
gen_ram_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_CombinedFragment)
gen_ram_InteractionOperand_FragmentContainer = Generalization(general=FragmentContainer, specific=ram_InteractionOperand)
gen_ram_StructuralFeatureValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_StructuralFeatureValue)
gen_ram_OriginalBehaviorExecution_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_OriginalBehaviorExecution)
gen_ram_ExecutionStatement_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_ExecutionStatement)
gen_ram_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_OpaqueExpression)
gen_ram_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_LiteralSpecification)
gen_ram_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralString)
gen_ram_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralInteger)
gen_ram_RCollection_Type = Generalization(general=Type, specific=ram_RCollection)
gen_ram_RCollection_ImplementationClass = Generalization(general=ImplementationClass, specific=ram_RCollection)
gen_ram_RSet_RCollection = Generalization(general=RCollection, specific=ram_RSet)
gen_ram_RSequence_RCollection = Generalization(general=RCollection, specific=ram_RSequence)
gen_ram_ParameterValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_ParameterValue)
gen_ram_Classifier_ObjectType = Generalization(general=ObjectType, specific=ram_Classifier)
gen_ram_ImplementationClass_Classifier = Generalization(general=Classifier, specific=ram_ImplementationClass)
gen_ram_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=ram_StructuralFeature)
gen_ram_Reference_Property = Generalization(general=Property_, specific=ram_Reference)
gen_ram_Reference_TemporaryProperty = Generalization(general=TemporaryProperty, specific=ram_Reference)
gen_ram_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=ram_Property)
gen_ram_AttributeMapping_Mapping = Generalization(general=Mapping, specific=ram_AttributeMapping)
gen_ram_OperationMapping_Mapping = Generalization(general=Mapping, specific=ram_OperationMapping)
gen_ram_ParameterMapping_Mapping = Generalization(general=Mapping, specific=ram_ParameterMapping)
gen_ram_StateView_NamedElement = Generalization(general=NamedElement, specific=ram_StateView)
gen_ram_TypedElement_NamedElement = Generalization(general=NamedElement, specific=ram_TypedElement)
gen_ram_Gate_MessageEnd = Generalization(general=MessageEnd, specific=ram_Gate)
gen_ram_Gate_NamedElement = Generalization(general=NamedElement, specific=ram_Gate)
gen_ram_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralBoolean)
gen_ram_ClassifierMapping_Mapping = Generalization(general=Mapping, specific=ram_ClassifierMapping)
gen_ram_State_NamedElement = Generalization(general=NamedElement, specific=ram_State)
gen_ram_RDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RDouble)
gen_ram_RFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RFloat)
gen_ram_TransitionSubstitution_Substitution = Generalization(general=Substitution, specific=ram_TransitionSubstitution)
gen_ram_Transition_NamedElement = Generalization(general=NamedElement, specific=ram_Transition)
gen_ram_RArray_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RArray)
gen_ram_TypeParameter_Type = Generalization(general=Type, specific=ram_TypeParameter)
gen_ram_RLong_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RLong)

# Domain Model
domain_model = DomainModel(
    name="ram",
    types={ram_Aspect, NamedElement, ram_StructuralView, ram_MappableElement, ram_Classifier, ram_Association, ram_Type, ram_Class, Classifier, ram_Attribute, ram_AssociationEnd, Property_, ram_AbstractMessageView, ram_Instantiation, ram_Layout, ram_StateView, ram_ClassifierMapping, ram_Mapping, ram_Operation, MappableElement, ram_Parameter, ram_NamedElement, ObjectType, ImplementationClass, ram_ObjectType, Type, ram_RVoid, ram_RBoolean, PrimitiveType, ram_RInt, ram_RChar, StructuralFeature, TemporaryProperty, ram_PrimitiveType, TypedElement, ram_REnum, ram_REnumLiteral, ram_AspectMessageView, ram_MessageView, AbstractMessageView, ram_Interaction, ram_MessageViewReference, FragmentContainer, ram_RString, ram_RAny, ram_TypedElement, ram_TemporaryProperty, ram_InteractionFragment, ram_MessageEnd, ram_Lifeline, ram_Message, ram_Reference, ram_Gate, ram_ValueSpecification, ram_MessageOccurrenceSpecification, OccurrenceSpecification, MessageEnd, ram_OccurrenceSpecification, InteractionFragment, ram_DestructionOccurrenceSpecification, MessageOccurrenceSpecification, ram_FragmentContainer, ram_CombinedFragment, ram_StructuralFeature, ram_ParameterValueMapping, ram_StructuralFeatureValue, ValueSpecification, ram_InteractionOperand, ram_OriginalBehaviorExecution, ram_ExecutionStatement, ram_OpaqueExpression, ram_LiteralSpecification, ram_LiteralString, LiteralSpecification, ram_LiteralInteger, ram_RCollection, ram_RSet, RCollection, ram_RSequence, ram_ContainerMap, ram_ParameterValue, ram_TypeParameter, ram_ImplementationClass, ram_Property, ram_EObject, ram_ElementMap, ram_LayoutElement, ram_AttributeMapping, ram_ParameterMapping, ram_StateMachine, ram_LiteralBoolean, Mapping, ram_OperationMapping, ram_Constraint, ram_RDouble, ram_RFloat, ram_TransitionSubstitution, Substitution, ram_State, ram_Transition, ram_Substitution, ram_RArray, ram_RLong, Visibility, ReferenceType, MessageSort, InteractionOperatorKind, InstantiationType},
    associations={structuralView0, mandatoryAspectParameters1, classes11, associations13, types15, attributes17, superTypes18, messageViews3, instantiations5, layout7, stateViews9, mappings24, externalAspect26, returnType29, parameters31, assoc21, classifier22, ends23, type35, type33, literals38, enum39, affectedBy40, specifies42, specification44, references46, pointcut55, advice58, represents61, localProperties63, coveredBy65, sendEvent66, lifelines48, messages50, properties51, formalGates53, returns78, message80, covered83, container84, receiveEvent67, signature70, assignTo73, arguments75, interaction77, interactionConstraint88, value91, operands85, specification86, parameter99, fragments101, type103, containers104, parameter93, value96, operations115, associationEnds118, typeParameters120, type122, key106, value108, key110, value113, attributeMappings127, fromElement129, toElement132, fromElement135, toElement138, parameterMappings141, fromElement143, toElement146, fromElement149, toElement152, stateMachines155, specifies157, operationMappings125, endState169, startState170, signature172, guard175, incomings177, outgoings178, Specification180, start160, states162, transitions165, substitutions167, type191, from183, to185, genericType188},
    generalizations={gen_ram_Aspect_NamedElement, gen_ram_Class_Classifier, gen_ram_AssociationEnd_Property, gen_ram_MappableElement_NamedElement, gen_ram_Operation_NamedElement, gen_ram_Operation_MappableElement, gen_ram_Association_NamedElement, gen_ram_PrimitiveType_ObjectType, gen_ram_PrimitiveType_ImplementationClass, gen_ram_ObjectType_Type, gen_ram_ObjectType_MappableElement, gen_ram_RVoid_Type, gen_ram_RBoolean_PrimitiveType, gen_ram_RInt_PrimitiveType, gen_ram_Attribute_StructuralFeature, gen_ram_Attribute_TemporaryProperty, gen_ram_Attribute_MappableElement, gen_ram_Type_NamedElement, gen_ram_Parameter_TypedElement, gen_ram_Parameter_MappableElement, gen_ram_REnum_PrimitiveType, gen_ram_REnumLiteral_NamedElement, gen_ram_MessageView_AbstractMessageView, gen_ram_MessageViewReference_AbstractMessageView, gen_ram_RChar_PrimitiveType, gen_ram_RString_PrimitiveType, gen_ram_RAny_Type, gen_ram_Interaction_FragmentContainer, gen_ram_AspectMessageView_AbstractMessageView, gen_ram_AspectMessageView_NamedElement, gen_ram_MessageOccurrenceSpecification_OccurrenceSpecification, gen_ram_MessageOccurrenceSpecification_MessageEnd, gen_ram_OccurrenceSpecification_InteractionFragment, gen_ram_DestructionOccurrenceSpecification_MessageOccurrenceSpecification, gen_ram_CombinedFragment_InteractionFragment, gen_ram_InteractionOperand_FragmentContainer, gen_ram_StructuralFeatureValue_ValueSpecification, gen_ram_OriginalBehaviorExecution_InteractionFragment, gen_ram_ExecutionStatement_InteractionFragment, gen_ram_OpaqueExpression_ValueSpecification, gen_ram_LiteralSpecification_ValueSpecification, gen_ram_LiteralString_LiteralSpecification, gen_ram_LiteralInteger_LiteralSpecification, gen_ram_RCollection_Type, gen_ram_RCollection_ImplementationClass, gen_ram_RSet_RCollection, gen_ram_RSequence_RCollection, gen_ram_ParameterValue_ValueSpecification, gen_ram_Classifier_ObjectType, gen_ram_ImplementationClass_Classifier, gen_ram_StructuralFeature_TypedElement, gen_ram_Reference_Property, gen_ram_Reference_TemporaryProperty, gen_ram_Property_StructuralFeature, gen_ram_AttributeMapping_Mapping, gen_ram_OperationMapping_Mapping, gen_ram_ParameterMapping_Mapping, gen_ram_StateView_NamedElement, gen_ram_TypedElement_NamedElement, gen_ram_Gate_MessageEnd, gen_ram_Gate_NamedElement, gen_ram_LiteralBoolean_LiteralSpecification, gen_ram_ClassifierMapping_Mapping, gen_ram_State_NamedElement, gen_ram_RDouble_PrimitiveType, gen_ram_RFloat_PrimitiveType, gen_ram_TransitionSubstitution_Substitution, gen_ram_Transition_NamedElement, gen_ram_RArray_PrimitiveType, gen_ram_TypeParameter_Type, gen_ram_RLong_PrimitiveType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)