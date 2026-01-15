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
RAMVisibilityType: Enumeration = Enumeration(
    name="RAMVisibilityType",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private"),
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

OperationType: Enumeration = Enumeration(
    name="OperationType",
    literals={
            EnumerationLiteral(name="Normal"),
			EnumerationLiteral(name="Constructor"),
			EnumerationLiteral(name="Destructor")
    }
)

# Classes
ram_Aspect = Class(name="ram::Aspect")
NamedElement = Class(name="NamedElement")
COREModel = Class(name="COREModel")
ram_StructuralView = Class(name="ram::StructuralView")
ram_AbstractMessageView = Class(name="ram::AbstractMessageView", is_abstract=True)
ram_Instantiation = Class(name="ram::Instantiation")
ram_Layout = Class(name="ram::Layout")
ram_StateView = Class(name="ram::StateView")
ram_WovenAspect = Class(name="ram::WovenAspect")
ram_MappableElement = Class(name="ram::MappableElement", is_abstract=True)
COREModelElement = Class(name="COREModelElement")
ram_Attribute = Class(name="ram::Attribute")
ram_AssociationEnd = Class(name="ram::AssociationEnd")
Property_ = Class(name="Property")
ram_COREModelReuse = Class(name="ram::COREModelReuse")
ram_NamedElement = Class(name="ram::NamedElement", is_abstract=True)
CORENamedElement = Class(name="CORENamedElement")
ram_Classifier = Class(name="ram::Classifier", is_abstract=True)
ram_Association = Class(name="ram::Association")
ram_Type = Class(name="ram::Type", is_abstract=True)
ram_Class = Class(name="ram::Class")
Classifier = Class(name="Classifier")
ram_Operation = Class(name="ram::Operation")
MappableElement = Class(name="MappableElement")
Traceable = Class(name="Traceable")
ram_Parameter = Class(name="ram::Parameter")
TypedElement = Class(name="TypedElement")
ram_PrimitiveType = Class(name="ram::PrimitiveType", is_abstract=True)
ObjectType = Class(name="ObjectType")
ImplementationClass = Class(name="ImplementationClass")
Type = Class(name="Type")
ram_RVoid = Class(name="ram::RVoid")
ram_RBoolean = Class(name="ram::RBoolean")
PrimitiveType = Class(name="PrimitiveType")
StructuralFeature = Class(name="StructuralFeature")
TemporaryProperty = Class(name="TemporaryProperty")
ram_ObjectType = Class(name="ram::ObjectType", is_abstract=True)
ram_RString = Class(name="ram::RString")
ram_RAny = Class(name="ram::RAny")
ram_REnum = Class(name="ram::REnum")
ram_REnumLiteral = Class(name="ram::REnumLiteral")
ram_AspectMessageView = Class(name="ram::AspectMessageView")
ram_MessageView = Class(name="ram::MessageView")
AbstractMessageView = Class(name="AbstractMessageView")
ram_RInt = Class(name="ram::RInt")
ram_RChar = Class(name="ram::RChar")
FragmentContainer = Class(name="FragmentContainer")
ram_Lifeline = Class(name="ram::Lifeline")
ram_Message = Class(name="ram::Message")
ram_Reference = Class(name="ram::Reference")
ram_Gate = Class(name="ram::Gate")
ram_TypedElement = Class(name="ram::TypedElement", is_abstract=True)
ram_InteractionFragment = Class(name="ram::InteractionFragment", is_abstract=True)
ram_Interaction = Class(name="ram::Interaction")
ram_MessageViewReference = Class(name="ram::MessageViewReference")
ram_StructuralFeature = Class(name="ram::StructuralFeature", is_abstract=True)
ram_ParameterValueMapping = Class(name="ram::ParameterValueMapping")
ram_ValueSpecification = Class(name="ram::ValueSpecification", is_abstract=True)
ram_TemporaryProperty = Class(name="ram::TemporaryProperty", is_abstract=True)
ram_MessageEnd = Class(name="ram::MessageEnd", is_abstract=True)
ram_CombinedFragment = Class(name="ram::CombinedFragment")
ram_InteractionOperand = Class(name="ram::InteractionOperand")
ram_OriginalBehaviorExecution = Class(name="ram::OriginalBehaviorExecution")
ram_ExecutionStatement = Class(name="ram::ExecutionStatement")
ram_StructuralFeatureValue = Class(name="ram::StructuralFeatureValue")
ValueSpecification = Class(name="ValueSpecification")
ram_MessageOccurrenceSpecification = Class(name="ram::MessageOccurrenceSpecification")
OccurrenceSpecification = Class(name="OccurrenceSpecification")
MessageEnd = Class(name="MessageEnd")
ram_OccurrenceSpecification = Class(name="ram::OccurrenceSpecification")
InteractionFragment = Class(name="InteractionFragment")
ram_DestructionOccurrenceSpecification = Class(name="ram::DestructionOccurrenceSpecification")
MessageOccurrenceSpecification = Class(name="MessageOccurrenceSpecification")
ram_FragmentContainer = Class(name="ram::FragmentContainer", is_abstract=True)
ram_RCollection = Class(name="ram::RCollection", is_abstract=True)
ram_RSet = Class(name="ram::RSet")
RCollection = Class(name="RCollection")
ram_RSequence = Class(name="ram::RSequence")
ram_ContainerMap = Class(name="ram::ContainerMap")
ram_EObject = Class(name="ram::EObject")
ram_ElementMap = Class(name="ram::ElementMap")
ram_NewLayoutElement = Class(name="ram::NewLayoutElement")
ram_ParameterValue = Class(name="ram::ParameterValue")
ram_OpaqueExpression = Class(name="ram::OpaqueExpression")
ram_LiteralSpecification = Class(name="ram::LiteralSpecification", is_abstract=True)
ram_LiteralString = Class(name="ram::LiteralString")
LiteralSpecification = Class(name="LiteralSpecification")
ram_LiteralInteger = Class(name="ram::LiteralInteger")
ram_ImplementationClass = Class(name="ram::ImplementationClass")
ram_Property = Class(name="ram::Property", is_abstract=True)
ram_LiteralBoolean = Class(name="ram::LiteralBoolean")
ram_ClassifierMapping = Class(name="ram::ClassifierMapping")
ram_OperationMapping = Class(name="ram::OperationMapping")
ram_TypeParameter = Class(name="ram::TypeParameter")
ram_StateMachine = Class(name="ram::StateMachine")
ram_CheckState = Class(name="ram::CheckState")
ram_Transition = Class(name="ram::Transition")
ram_Substitution = Class(name="ram::Substitution")
ram_Constraint = Class(name="ram::Constraint")
ram_AttributeMapping = Class(name="ram::AttributeMapping")
ram_ParameterMapping = Class(name="ram::ParameterMapping")
ram_RFloat = Class(name="ram::RFloat")
ram_TransitionSubstitution = Class(name="ram::TransitionSubstitution")
Substitution = Class(name="Substitution")
ram_RLong = Class(name="ram::RLong")
ram_RArray = Class(name="ram::RArray")
ram_RDouble = Class(name="ram::RDouble")
ram_Traceable = Class(name="ram::Traceable", is_abstract=True)
ram_TracingMap = Class(name="ram::TracingMap")
ram_LiteralNull = Class(name="ram::LiteralNull")
ram_EnumLiteralValue = Class(name="ram::EnumLiteralValue")
ram_AssignmentStatement = Class(name="ram::AssignmentStatement")
ram_RByte = Class(name="ram::RByte")
ram_LiteralChar = Class(name="ram::LiteralChar")
ram_LiteralDouble = Class(name="ram::LiteralDouble")
ram_LiteralLong = Class(name="ram::LiteralLong")
ram_LiteralFloat = Class(name="ram::LiteralFloat")
ram_LiteralByte = Class(name="ram::LiteralByte")

# ram_Aspect class attributes and methods

# NamedElement class attributes and methods

# COREModel class attributes and methods

# ram_StructuralView class attributes and methods

# ram_AbstractMessageView class attributes and methods

# ram_Instantiation class attributes and methods
ram_Instantiation_type: Property = Property(name="type", type=StringType)
ram_Instantiation.attributes={ram_Instantiation_type}

# ram_Layout class attributes and methods

# ram_StateView class attributes and methods

# ram_WovenAspect class attributes and methods

# ram_MappableElement class attributes and methods

# COREModelElement class attributes and methods

# ram_Attribute class attributes and methods

# ram_AssociationEnd class attributes and methods
ram_AssociationEnd_navigable: Property = Property(name="navigable", type=BooleanType)
ram_AssociationEnd_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
ram_AssociationEnd_m_getOppositeEnd: Method = Method(name="getOppositeEnd", parameters={}, type=StringType)
ram_AssociationEnd.attributes={ram_AssociationEnd_navigable}
ram_AssociationEnd.methods={ram_AssociationEnd_m_getType, ram_AssociationEnd_m_getOppositeEnd}

# Property class attributes and methods

# ram_COREModelReuse class attributes and methods

# ram_NamedElement class attributes and methods

# CORENamedElement class attributes and methods

# ram_Classifier class attributes and methods
ram_Classifier_dataType: Property = Property(name="dataType", type=BooleanType)
ram_Classifier.attributes={ram_Classifier_dataType}

# ram_Association class attributes and methods

# ram_Type class attributes and methods

# ram_Class class attributes and methods
ram_Class_abstract: Property = Property(name="abstract", type=BooleanType)
ram_Class.attributes={ram_Class_abstract}

# Classifier class attributes and methods

# ram_Operation class attributes and methods
ram_Operation_abstract: Property = Property(name="abstract", type=BooleanType)
ram_Operation_extendedVisibility: Property = Property(name="extendedVisibility", type=StringType)
ram_Operation_static: Property = Property(name="static", type=BooleanType)
ram_Operation_operationType: Property = Property(name="operationType", type=StringType)
ram_Operation.attributes={ram_Operation_static, ram_Operation_operationType, ram_Operation_abstract, ram_Operation_extendedVisibility}

# MappableElement class attributes and methods

# Traceable class attributes and methods

# ram_Parameter class attributes and methods

# TypedElement class attributes and methods

# ram_PrimitiveType class attributes and methods

# ObjectType class attributes and methods

# ImplementationClass class attributes and methods

# Type class attributes and methods

# ram_RVoid class attributes and methods
ram_RVoid_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RVoid.methods={ram_RVoid_m_getName}

# ram_RBoolean class attributes and methods
ram_RBoolean_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RBoolean_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RBoolean.methods={ram_RBoolean_m_getName, ram_RBoolean_m_getInstanceClassName}

# PrimitiveType class attributes and methods

# StructuralFeature class attributes and methods

# TemporaryProperty class attributes and methods

# ram_ObjectType class attributes and methods

# ram_RString class attributes and methods
ram_RString_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RString_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RString.methods={ram_RString_m_getName, ram_RString_m_getInstanceClassName}

# ram_RAny class attributes and methods
ram_RAny_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RAny.methods={ram_RAny_m_getName}

# ram_REnum class attributes and methods

# ram_REnumLiteral class attributes and methods

# ram_AspectMessageView class attributes and methods

# ram_MessageView class attributes and methods

# AbstractMessageView class attributes and methods

# ram_RInt class attributes and methods
ram_RInt_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RInt_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RInt.methods={ram_RInt_m_getName, ram_RInt_m_getInstanceClassName}

# ram_RChar class attributes and methods
ram_RChar_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RChar_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RChar.methods={ram_RChar_m_getInstanceClassName, ram_RChar_m_getName}

# FragmentContainer class attributes and methods

# ram_Lifeline class attributes and methods

# ram_Message class attributes and methods
ram_Message_messageSort: Property = Property(name="messageSort", type=StringType)
ram_Message_selfMessage: Property = Property(name="selfMessage", type=BooleanType)
ram_Message.attributes={ram_Message_messageSort, ram_Message_selfMessage}

# ram_Reference class attributes and methods

# ram_Gate class attributes and methods

# ram_TypedElement class attributes and methods
ram_TypedElement_m_getType: Method = Method(name="getType", parameters={}, type=Type)
ram_TypedElement.methods={ram_TypedElement_m_getType}

# ram_InteractionFragment class attributes and methods

# ram_Interaction class attributes and methods

# ram_MessageViewReference class attributes and methods

# ram_StructuralFeature class attributes and methods
ram_StructuralFeature_static: Property = Property(name="static", type=BooleanType)
ram_StructuralFeature.attributes={ram_StructuralFeature_static}

# ram_ParameterValueMapping class attributes and methods

# ram_ValueSpecification class attributes and methods

# ram_TemporaryProperty class attributes and methods

# ram_MessageEnd class attributes and methods

# ram_CombinedFragment class attributes and methods
ram_CombinedFragment_interactionOperator: Property = Property(name="interactionOperator", type=StringType)
ram_CombinedFragment.attributes={ram_CombinedFragment_interactionOperator}

# ram_InteractionOperand class attributes and methods

# ram_OriginalBehaviorExecution class attributes and methods

# ram_ExecutionStatement class attributes and methods

# ram_StructuralFeatureValue class attributes and methods

# ValueSpecification class attributes and methods

# ram_MessageOccurrenceSpecification class attributes and methods

# OccurrenceSpecification class attributes and methods

# MessageEnd class attributes and methods

# ram_OccurrenceSpecification class attributes and methods

# InteractionFragment class attributes and methods

# ram_DestructionOccurrenceSpecification class attributes and methods

# MessageOccurrenceSpecification class attributes and methods

# ram_FragmentContainer class attributes and methods

# ram_RCollection class attributes and methods
ram_RCollection_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RCollection.methods={ram_RCollection_m_getName}

# ram_RSet class attributes and methods

# RCollection class attributes and methods

# ram_RSequence class attributes and methods

# ram_ContainerMap class attributes and methods

# ram_EObject class attributes and methods

# ram_ElementMap class attributes and methods

# ram_NewLayoutElement class attributes and methods
ram_NewLayoutElement_x: Property = Property(name="x", type=FloatType)
ram_NewLayoutElement_y: Property = Property(name="y", type=FloatType)
ram_NewLayoutElement.attributes={ram_NewLayoutElement_x, ram_NewLayoutElement_y}

# ram_ParameterValue class attributes and methods

# ram_OpaqueExpression class attributes and methods
ram_OpaqueExpression_body: Property = Property(name="body", type=StringType)
ram_OpaqueExpression_language: Property = Property(name="language", type=StringType)
ram_OpaqueExpression.attributes={ram_OpaqueExpression_language, ram_OpaqueExpression_body}

# ram_LiteralSpecification class attributes and methods

# ram_LiteralString class attributes and methods
ram_LiteralString_value: Property = Property(name="value", type=StringType)
ram_LiteralString.attributes={ram_LiteralString_value}

# LiteralSpecification class attributes and methods

# ram_LiteralInteger class attributes and methods
ram_LiteralInteger_value: Property = Property(name="value", type=IntegerType)
ram_LiteralInteger.attributes={ram_LiteralInteger_value}

# ram_ImplementationClass class attributes and methods
ram_ImplementationClass_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ram_ImplementationClass_interface: Property = Property(name="interface", type=BooleanType)
ram_ImplementationClass.attributes={ram_ImplementationClass_instanceClassName, ram_ImplementationClass_interface}

# ram_Property class attributes and methods
ram_Property_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ram_Property_upperBound: Property = Property(name="upperBound", type=IntegerType)
ram_Property_referenceType: Property = Property(name="referenceType", type=StringType)
ram_Property.attributes={ram_Property_upperBound, ram_Property_referenceType, ram_Property_lowerBound}

# ram_LiteralBoolean class attributes and methods
ram_LiteralBoolean_value: Property = Property(name="value", type=BooleanType)
ram_LiteralBoolean.attributes={ram_LiteralBoolean_value}

# ram_ClassifierMapping class attributes and methods

# ram_OperationMapping class attributes and methods

# ram_TypeParameter class attributes and methods

# ram_StateMachine class attributes and methods

# ram_CheckState class attributes and methods

# ram_Transition class attributes and methods

# ram_Substitution class attributes and methods

# ram_Constraint class attributes and methods

# ram_AttributeMapping class attributes and methods

# ram_ParameterMapping class attributes and methods

# ram_RFloat class attributes and methods
ram_RFloat_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RFloat_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RFloat.methods={ram_RFloat_m_getName, ram_RFloat_m_getInstanceClassName}

# ram_TransitionSubstitution class attributes and methods

# Substitution class attributes and methods

# ram_RLong class attributes and methods
ram_RLong_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RLong_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RLong.methods={ram_RLong_m_getName, ram_RLong_m_getInstanceClassName}

# ram_RArray class attributes and methods
ram_RArray_size: Property = Property(name="size", type=IntegerType)
ram_RArray_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RArray_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RArray.attributes={ram_RArray_size}
ram_RArray.methods={ram_RArray_m_getInstanceClassName, ram_RArray_m_getName}

# ram_RDouble class attributes and methods
ram_RDouble_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RDouble_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RDouble.methods={ram_RDouble_m_getName, ram_RDouble_m_getInstanceClassName}

# ram_Traceable class attributes and methods

# ram_TracingMap class attributes and methods

# ram_LiteralNull class attributes and methods

# ram_EnumLiteralValue class attributes and methods

# ram_AssignmentStatement class attributes and methods

# ram_RByte class attributes and methods
ram_RByte_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
ram_RByte_m_getInstanceClassName: Method = Method(name="getInstanceClassName", parameters={}, type=StringType)
ram_RByte.methods={ram_RByte_m_getName, ram_RByte_m_getInstanceClassName}

# ram_LiteralChar class attributes and methods
ram_LiteralChar_value: Property = Property(name="value", type=StringType)
ram_LiteralChar.attributes={ram_LiteralChar_value}

# ram_LiteralDouble class attributes and methods
ram_LiteralDouble_value: Property = Property(name="value", type=FloatType)
ram_LiteralDouble.attributes={ram_LiteralDouble_value}

# ram_LiteralLong class attributes and methods
ram_LiteralLong_value: Property = Property(name="value", type=StringType)
ram_LiteralLong.attributes={ram_LiteralLong_value}

# ram_LiteralFloat class attributes and methods
ram_LiteralFloat_value: Property = Property(name="value", type=FloatType)
ram_LiteralFloat.attributes={ram_LiteralFloat_value}

# ram_LiteralByte class attributes and methods
ram_LiteralByte_value: Property = Property(name="value", type=StringType)
ram_LiteralByte.attributes={ram_LiteralByte_value}

# Relationships
structuralView0: BinaryAssociation = BinaryAssociation(
    name="structuralView0",
    ends={
        Property(name="ram_StructuralView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect", type=ram_StructuralView, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
messageViews1: BinaryAssociation = BinaryAssociation(
    name="messageViews1",
    ends={
        Property(name="ram_AbstractMessageView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect2", type=ram_AbstractMessageView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiations3: BinaryAssociation = BinaryAssociation(
    name="instantiations3",
    ends={
        Property(name="ram_Instantiation", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect4", type=ram_Instantiation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layout5: BinaryAssociation = BinaryAssociation(
    name="layout5",
    ends={
        Property(name="ram_Layout", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect6", type=ram_Layout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateViews7: BinaryAssociation = BinaryAssociation(
    name="stateViews7",
    ends={
        Property(name="ram_StateView", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect8", type=ram_StateView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wovenAspects9: BinaryAssociation = BinaryAssociation(
    name="wovenAspects9",
    ends={
        Property(name="ram_WovenAspect", type=ram_Aspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Aspect10", type=ram_WovenAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes17: BinaryAssociation = BinaryAssociation(
    name="attributes17",
    ends={
        Property(name="ram_Attribute", type=ram_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Class", type=ram_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assoc18: BinaryAssociation = BinaryAssociation(
    name="assoc18",
    ends={
        Property(name="Association", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ends", type=ram_Association, multiplicity=Multiplicity(1, 1))
    }
)
classifier19: BinaryAssociation = BinaryAssociation(
    name="classifier19",
    ends={
        Property(name="Classifier", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnds", type=ram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
featureSelection20: BinaryAssociation = BinaryAssociation(
    name="featureSelection20",
    ends={
        Property(name="ram_COREModelReuse", type=ram_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AssociationEnd", type=ram_COREModelReuse, multiplicity=Multiplicity(0, 1))
    }
)
ends21: BinaryAssociation = BinaryAssociation(
    name="ends21",
    ends={
        Property(name="AssociationEnd", type=ram_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="assoc", type=ram_AssociationEnd, multiplicity=Multiplicity(2, 2))
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
returnType22: BinaryAssociation = BinaryAssociation(
    name="returnType22",
    ends={
        Property(name="ram_Type23", type=ram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Operation", type=ram_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="ram_Parameter", type=ram_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Operation25", type=ram_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type28: BinaryAssociation = BinaryAssociation(
    name="type28",
    ends={
        Property(name="ram_Type30", type=ram_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Parameter29", type=ram_Type, multiplicity=Multiplicity(1, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="ram_ObjectType", type=ram_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Attribute27", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
literals31: BinaryAssociation = BinaryAssociation(
    name="literals31",
    ends={
        Property(name="REnumLiteral", type=ram_REnum, multiplicity=Multiplicity(1, 1)),
        Property(name="enum", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enum32: BinaryAssociation = BinaryAssociation(
    name="enum32",
    ends={
        Property(name="REnum", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=ram_REnum, multiplicity=Multiplicity(1, 1))
    }
)
affectedBy33: BinaryAssociation = BinaryAssociation(
    name="affectedBy33",
    ends={
        Property(name="ram_AspectMessageView", type=ram_AbstractMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AbstractMessageView34", type=ram_AspectMessageView, multiplicity=Multiplicity(0, 9999))
    }
)
references39: BinaryAssociation = BinaryAssociation(
    name="references39",
    ends={
        Property(name="ram_MessageView40", type=ram_MessageViewReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageViewReference", type=ram_MessageView, multiplicity=Multiplicity(1, 1))
    }
)
lifelines41: BinaryAssociation = BinaryAssociation(
    name="lifelines41",
    ends={
        Property(name="ram_Lifeline", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction42", type=ram_Lifeline, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
messages43: BinaryAssociation = BinaryAssociation(
    name="messages43",
    ends={
        Property(name="Message", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="interaction", type=ram_Message, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties44: BinaryAssociation = BinaryAssociation(
    name="properties44",
    ends={
        Property(name="ram_Reference", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction45", type=ram_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalGates46: BinaryAssociation = BinaryAssociation(
    name="formalGates46",
    ends={
        Property(name="ram_Gate", type=ram_Interaction, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Interaction47", type=ram_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pointcut48: BinaryAssociation = BinaryAssociation(
    name="pointcut48",
    ends={
        Property(name="ram_Operation50", type=ram_AspectMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AspectMessageView49", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
advice51: BinaryAssociation = BinaryAssociation(
    name="advice51",
    ends={
        Property(name="ram_Interaction53", type=ram_AspectMessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AspectMessageView52", type=ram_Interaction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
represents54: BinaryAssociation = BinaryAssociation(
    name="represents54",
    ends={
        Property(name="ram_TypedElement", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Lifeline55", type=ram_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
coveredBy56: BinaryAssociation = BinaryAssociation(
    name="coveredBy56",
    ends={
        Property(name="InteractionFragment", type=ram_Lifeline, multiplicity=Multiplicity(1, 1)),
        Property(name="covered", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 9999))
    }
)
specifies35: BinaryAssociation = BinaryAssociation(
    name="specifies35",
    ends={
        Property(name="ram_Operation36", type=ram_MessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageView", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
specification37: BinaryAssociation = BinaryAssociation(
    name="specification37",
    ends={
        Property(name="ram_Interaction", type=ram_MessageView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageView38", type=ram_Interaction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature61: BinaryAssociation = BinaryAssociation(
    name="signature61",
    ends={
        Property(name="ram_Operation63", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message62", type=ram_Operation, multiplicity=Multiplicity(1, 1))
    }
)
assignTo64: BinaryAssociation = BinaryAssociation(
    name="assignTo64",
    ends={
        Property(name="ram_StructuralFeature", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message65", type=ram_StructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
arguments66: BinaryAssociation = BinaryAssociation(
    name="arguments66",
    ends={
        Property(name="ram_ParameterValueMapping", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message67", type=ram_ParameterValueMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interaction68: BinaryAssociation = BinaryAssociation(
    name="interaction68",
    ends={
        Property(name="Interaction", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="messages", type=ram_Interaction, multiplicity=Multiplicity(1, 1))
    }
)
returns69: BinaryAssociation = BinaryAssociation(
    name="returns69",
    ends={
        Property(name="ram_ValueSpecification", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message70", type=ram_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localProperties71: BinaryAssociation = BinaryAssociation(
    name="localProperties71",
    ends={
        Property(name="ram_TemporaryProperty", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message72", type=ram_TemporaryProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message73: BinaryAssociation = BinaryAssociation(
    name="message73",
    ends={
        Property(name="ram_Message75", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_MessageEnd74", type=ram_Message, multiplicity=Multiplicity(1, 1))
    }
)
sendEvent57: BinaryAssociation = BinaryAssociation(
    name="sendEvent57",
    ends={
        Property(name="ram_MessageEnd", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1))
    }
)
receiveEvent58: BinaryAssociation = BinaryAssociation(
    name="receiveEvent58",
    ends={
        Property(name="ram_MessageEnd60", type=ram_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Message59", type=ram_MessageEnd, multiplicity=Multiplicity(1, 1))
    }
)
operands78: BinaryAssociation = BinaryAssociation(
    name="operands78",
    ends={
        Property(name="ram_InteractionOperand", type=ram_CombinedFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_CombinedFragment", type=ram_InteractionOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specification79: BinaryAssociation = BinaryAssociation(
    name="specification79",
    ends={
        Property(name="ram_ValueSpecification80", type=ram_ExecutionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ExecutionStatement", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interactionConstraint81: BinaryAssociation = BinaryAssociation(
    name="interactionConstraint81",
    ends={
        Property(name="ram_ValueSpecification83", type=ram_InteractionOperand, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_InteractionOperand82", type=ram_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="ram_StructuralFeature85", type=ram_StructuralFeatureValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StructuralFeatureValue", type=ram_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
parameter86: BinaryAssociation = BinaryAssociation(
    name="parameter86",
    ends={
        Property(name="ram_Parameter88", type=ram_ParameterValueMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValueMapping87", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
covered76: BinaryAssociation = BinaryAssociation(
    name="covered76",
    ends={
        Property(name="Lifeline", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="coveredBy", type=ram_Lifeline, multiplicity=Multiplicity(1, 9999))
    }
)
container77: BinaryAssociation = BinaryAssociation(
    name="container77",
    ends={
        Property(name="FragmentContainer", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=ram_FragmentContainer, multiplicity=Multiplicity(1, 1))
    }
)
fragments94: BinaryAssociation = BinaryAssociation(
    name="fragments94",
    ends={
        Property(name="InteractionFragment95", type=ram_FragmentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=ram_InteractionFragment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type96: BinaryAssociation = BinaryAssociation(
    name="type96",
    ends={
        Property(name="ram_ObjectType97", type=ram_RCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_RCollection", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
containers98: BinaryAssociation = BinaryAssociation(
    name="containers98",
    ends={
        Property(name="ram_ContainerMap", type=ram_Layout, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Layout99", type=ram_ContainerMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
key100: BinaryAssociation = BinaryAssociation(
    name="key100",
    ends={
        Property(name="ram_EObject", type=ram_ContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ContainerMap101", type=ram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value102: BinaryAssociation = BinaryAssociation(
    name="value102",
    ends={
        Property(name="ram_ElementMap", type=ram_ContainerMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ContainerMap103", type=ram_ElementMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
key104: BinaryAssociation = BinaryAssociation(
    name="key104",
    ends={
        Property(name="ram_EObject106", type=ram_ElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ElementMap105", type=ram_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value107: BinaryAssociation = BinaryAssociation(
    name="value107",
    ends={
        Property(name="ram_NewLayoutElement", type=ram_ElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ElementMap108", type=ram_NewLayoutElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="ram_ValueSpecification91", type=ram_ParameterValueMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValueMapping90", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter92: BinaryAssociation = BinaryAssociation(
    name="parameter92",
    ends={
        Property(name="ram_Parameter93", type=ram_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ParameterValue", type=ram_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="ram_ObjectType121", type=ram_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Reference120", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)
operationMappings122: BinaryAssociation = BinaryAssociation(
    name="operationMappings122",
    ends={
        Property(name="ram_OperationMapping", type=ram_ClassifierMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ClassifierMapping", type=ram_OperationMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations109: BinaryAssociation = BinaryAssociation(
    name="operations109",
    ends={
        Property(name="ram_Operation111", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Classifier110", type=ram_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnds112: BinaryAssociation = BinaryAssociation(
    name="associationEnds112",
    ends={
        Property(name="AssociationEnd113", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=ram_AssociationEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters114: BinaryAssociation = BinaryAssociation(
    name="typeParameters114",
    ends={
        Property(name="ram_TypeParameter", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Classifier115", type=ram_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superTypes117: BinaryAssociation = BinaryAssociation(
    name="superTypes117",
    ends={
        Property(name="ram_Classifier118", type=ram_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Classifier116", type=ram_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachines127: BinaryAssociation = BinaryAssociation(
    name="stateMachines127",
    ends={
        Property(name="ram_StateMachine", type=ram_StateView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateView128", type=ram_StateMachine, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specifies129: BinaryAssociation = BinaryAssociation(
    name="specifies129",
    ends={
        Property(name="ram_Classifier131", type=ram_StateView, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateView130", type=ram_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
start132: BinaryAssociation = BinaryAssociation(
    name="start132",
    ends={
        Property(name="ram_CheckState", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine133", type=ram_CheckState, multiplicity=Multiplicity(1, 1))
    }
)
states134: BinaryAssociation = BinaryAssociation(
    name="states134",
    ends={
        Property(name="ram_CheckState136", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine135", type=ram_CheckState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions137: BinaryAssociation = BinaryAssociation(
    name="transitions137",
    ends={
        Property(name="ram_Transition", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine138", type=ram_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitutions139: BinaryAssociation = BinaryAssociation(
    name="substitutions139",
    ends={
        Property(name="ram_Substitution", type=ram_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_StateMachine140", type=ram_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState141: BinaryAssociation = BinaryAssociation(
    name="endState141",
    ends={
        Property(name="CheckState", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=ram_CheckState, multiplicity=Multiplicity(1, 1))
    }
)
startState142: BinaryAssociation = BinaryAssociation(
    name="startState142",
    ends={
        Property(name="CheckState143", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=ram_CheckState, multiplicity=Multiplicity(1, 1))
    }
)
signature144: BinaryAssociation = BinaryAssociation(
    name="signature144",
    ends={
        Property(name="ram_Operation146", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Transition145", type=ram_Operation, multiplicity=Multiplicity(0, 1))
    }
)
guard147: BinaryAssociation = BinaryAssociation(
    name="guard147",
    ends={
        Property(name="ram_Constraint", type=ram_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Transition148", type=ram_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeMappings123: BinaryAssociation = BinaryAssociation(
    name="attributeMappings123",
    ends={
        Property(name="ram_AttributeMapping", type=ram_ClassifierMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_ClassifierMapping124", type=ram_AttributeMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterMappings125: BinaryAssociation = BinaryAssociation(
    name="parameterMappings125",
    ends={
        Property(name="ram_ParameterMapping", type=ram_OperationMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_OperationMapping126", type=ram_ParameterMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Specification152: BinaryAssociation = BinaryAssociation(
    name="Specification152",
    ends={
        Property(name="ram_ValueSpecification154", type=ram_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_Constraint153", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from155: BinaryAssociation = BinaryAssociation(
    name="from155",
    ends={
        Property(name="ram_Transition156", type=ram_TransitionSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TransitionSubstitution", type=ram_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to157: BinaryAssociation = BinaryAssociation(
    name="to157",
    ends={
        Property(name="ram_Transition159", type=ram_TransitionSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TransitionSubstitution158", type=ram_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
genericType160: BinaryAssociation = BinaryAssociation(
    name="genericType160",
    ends={
        Property(name="ram_ObjectType162", type=ram_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TypeParameter161", type=ram_ObjectType, multiplicity=Multiplicity(0, 1))
    }
)
incomings149: BinaryAssociation = BinaryAssociation(
    name="incomings149",
    ends={
        Property(name="Transition", type=ram_CheckState, multiplicity=Multiplicity(1, 1)),
        Property(name="endState", type=ram_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoings150: BinaryAssociation = BinaryAssociation(
    name="outgoings150",
    ends={
        Property(name="Transition151", type=ram_CheckState, multiplicity=Multiplicity(1, 1)),
        Property(name="startState", type=ram_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
comesFrom165: BinaryAssociation = BinaryAssociation(
    name="comesFrom165",
    ends={
        Property(name="ram_Aspect167", type=ram_WovenAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_WovenAspect166", type=ram_Aspect, multiplicity=Multiplicity(1, 1))
    }
)
children169: BinaryAssociation = BinaryAssociation(
    name="children169",
    ends={
        Property(name="ram_WovenAspect170", type=ram_WovenAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_WovenAspect168", type=ram_WovenAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wovenElements171: BinaryAssociation = BinaryAssociation(
    name="wovenElements171",
    ends={
        Property(name="ram_TracingMap", type=ram_WovenAspect, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_WovenAspect172", type=ram_TracingMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value173: BinaryAssociation = BinaryAssociation(
    name="value173",
    ends={
        Property(name="ram_REnumLiteral", type=ram_EnumLiteralValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_EnumLiteralValue", type=ram_REnumLiteral, multiplicity=Multiplicity(1, 1))
    }
)
assignTo174: BinaryAssociation = BinaryAssociation(
    name="assignTo174",
    ends={
        Property(name="ram_StructuralFeature175", type=ram_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AssignmentStatement", type=ram_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value176: BinaryAssociation = BinaryAssociation(
    name="value176",
    ends={
        Property(name="ram_ValueSpecification178", type=ram_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_AssignmentStatement177", type=ram_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key179: BinaryAssociation = BinaryAssociation(
    name="key179",
    ends={
        Property(name="ram_Traceable", type=ram_TracingMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TracingMap180", type=ram_Traceable, multiplicity=Multiplicity(1, 1))
    }
)
value181: BinaryAssociation = BinaryAssociation(
    name="value181",
    ends={
        Property(name="ram_Traceable183", type=ram_TracingMap, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_TracingMap182", type=ram_Traceable, multiplicity=Multiplicity(1, 1))
    }
)
type163: BinaryAssociation = BinaryAssociation(
    name="type163",
    ends={
        Property(name="ram_ObjectType164", type=ram_RArray, multiplicity=Multiplicity(1, 1)),
        Property(name="ram_RArray", type=ram_ObjectType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ram_Aspect_NamedElement = Generalization(general=NamedElement, specific=ram_Aspect)
gen_ram_Aspect_COREModel = Generalization(general=COREModel, specific=ram_Aspect)
gen_ram_MappableElement_NamedElement = Generalization(general=NamedElement, specific=ram_MappableElement)
gen_ram_AssociationEnd_Property = Generalization(general=Property_, specific=ram_AssociationEnd)
gen_ram_Association_NamedElement = Generalization(general=NamedElement, specific=ram_Association)
gen_ram_NamedElement_CORENamedElement = Generalization(general=CORENamedElement, specific=ram_NamedElement)
gen_ram_MappableElement_COREModelElement = Generalization(general=COREModelElement, specific=ram_MappableElement)
gen_ram_Class_Classifier = Generalization(general=Classifier, specific=ram_Class)
gen_ram_Operation_NamedElement = Generalization(general=NamedElement, specific=ram_Operation)
gen_ram_Operation_MappableElement = Generalization(general=MappableElement, specific=ram_Operation)
gen_ram_Operation_Traceable = Generalization(general=Traceable, specific=ram_Operation)
gen_ram_Type_NamedElement = Generalization(general=NamedElement, specific=ram_Type)
gen_ram_Parameter_TypedElement = Generalization(general=TypedElement, specific=ram_Parameter)
gen_ram_Parameter_MappableElement = Generalization(general=MappableElement, specific=ram_Parameter)
gen_ram_PrimitiveType_ObjectType = Generalization(general=ObjectType, specific=ram_PrimitiveType)
gen_ram_PrimitiveType_ImplementationClass = Generalization(general=ImplementationClass, specific=ram_PrimitiveType)
gen_ram_ObjectType_Type = Generalization(general=Type, specific=ram_ObjectType)
gen_ram_ObjectType_MappableElement = Generalization(general=MappableElement, specific=ram_ObjectType)
gen_ram_RVoid_Type = Generalization(general=Type, specific=ram_RVoid)
gen_ram_RBoolean_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RBoolean)
gen_ram_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=ram_Attribute)
gen_ram_Attribute_TemporaryProperty = Generalization(general=TemporaryProperty, specific=ram_Attribute)
gen_ram_Attribute_MappableElement = Generalization(general=MappableElement, specific=ram_Attribute)
gen_ram_Attribute_Traceable = Generalization(general=Traceable, specific=ram_Attribute)
gen_ram_RString_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RString)
gen_ram_RAny_Type = Generalization(general=Type, specific=ram_RAny)
gen_ram_REnum_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_REnum)
gen_ram_REnumLiteral_NamedElement = Generalization(general=NamedElement, specific=ram_REnumLiteral)
gen_ram_MessageView_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_MessageView)
gen_ram_RInt_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RInt)
gen_ram_RChar_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RChar)
gen_ram_Interaction_FragmentContainer = Generalization(general=FragmentContainer, specific=ram_Interaction)
gen_ram_AspectMessageView_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_AspectMessageView)
gen_ram_AspectMessageView_NamedElement = Generalization(general=NamedElement, specific=ram_AspectMessageView)
gen_ram_MessageViewReference_AbstractMessageView = Generalization(general=AbstractMessageView, specific=ram_MessageViewReference)
gen_ram_CombinedFragment_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_CombinedFragment)
gen_ram_OriginalBehaviorExecution_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_OriginalBehaviorExecution)
gen_ram_ExecutionStatement_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_ExecutionStatement)
gen_ram_InteractionOperand_FragmentContainer = Generalization(general=FragmentContainer, specific=ram_InteractionOperand)
gen_ram_StructuralFeatureValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_StructuralFeatureValue)
gen_ram_MessageOccurrenceSpecification_OccurrenceSpecification = Generalization(general=OccurrenceSpecification, specific=ram_MessageOccurrenceSpecification)
gen_ram_MessageOccurrenceSpecification_MessageEnd = Generalization(general=MessageEnd, specific=ram_MessageOccurrenceSpecification)
gen_ram_OccurrenceSpecification_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_OccurrenceSpecification)
gen_ram_DestructionOccurrenceSpecification_MessageOccurrenceSpecification = Generalization(general=MessageOccurrenceSpecification, specific=ram_DestructionOccurrenceSpecification)
gen_ram_RCollection_Type = Generalization(general=Type, specific=ram_RCollection)
gen_ram_RCollection_ImplementationClass = Generalization(general=ImplementationClass, specific=ram_RCollection)
gen_ram_RSet_RCollection = Generalization(general=RCollection, specific=ram_RSet)
gen_ram_RSequence_RCollection = Generalization(general=RCollection, specific=ram_RSequence)
gen_ram_ParameterValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_ParameterValue)
gen_ram_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_OpaqueExpression)
gen_ram_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_LiteralSpecification)
gen_ram_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralString)
gen_ram_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralInteger)
gen_ram_ImplementationClass_Classifier = Generalization(general=Classifier, specific=ram_ImplementationClass)
gen_ram_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=ram_StructuralFeature)
gen_ram_Reference_Property = Generalization(general=Property_, specific=ram_Reference)
gen_ram_Reference_TemporaryProperty = Generalization(general=TemporaryProperty, specific=ram_Reference)
gen_ram_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=ram_Property)
gen_ram_TypedElement_NamedElement = Generalization(general=NamedElement, specific=ram_TypedElement)
gen_ram_Gate_MessageEnd = Generalization(general=MessageEnd, specific=ram_Gate)
gen_ram_Gate_NamedElement = Generalization(general=NamedElement, specific=ram_Gate)
gen_ram_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralBoolean)
gen_ram_Classifier_ObjectType = Generalization(general=ObjectType, specific=ram_Classifier)
gen_ram_Classifier_Traceable = Generalization(general=Traceable, specific=ram_Classifier)
gen_ram_StateView_NamedElement = Generalization(general=NamedElement, specific=ram_StateView)
gen_ram_Transition_NamedElement = Generalization(general=NamedElement, specific=ram_Transition)
gen_ram_RFloat_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RFloat)
gen_ram_TransitionSubstitution_Substitution = Generalization(general=Substitution, specific=ram_TransitionSubstitution)
gen_ram_TypeParameter_Type = Generalization(general=Type, specific=ram_TypeParameter)
gen_ram_RLong_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RLong)
gen_ram_RArray_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RArray)
gen_ram_CheckState_NamedElement = Generalization(general=NamedElement, specific=ram_CheckState)
gen_ram_RDouble_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RDouble)
gen_ram_WovenAspect_NamedElement = Generalization(general=NamedElement, specific=ram_WovenAspect)
gen_ram_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralNull)
gen_ram_EnumLiteralValue_ValueSpecification = Generalization(general=ValueSpecification, specific=ram_EnumLiteralValue)
gen_ram_AssignmentStatement_InteractionFragment = Generalization(general=InteractionFragment, specific=ram_AssignmentStatement)
gen_ram_LiteralChar_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralChar)
gen_ram_LiteralDouble_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralDouble)
gen_ram_RByte_PrimitiveType = Generalization(general=PrimitiveType, specific=ram_RByte)
gen_ram_LiteralLong_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralLong)
gen_ram_LiteralFloat_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralFloat)
gen_ram_LiteralByte_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ram_LiteralByte)

# Domain Model
domain_model = DomainModel(
    name="ram",
    types={ram_Aspect, NamedElement, COREModel, ram_StructuralView, ram_AbstractMessageView, ram_Instantiation, ram_Layout, ram_StateView, ram_WovenAspect, ram_MappableElement, COREModelElement, ram_Attribute, ram_AssociationEnd, Property_, ram_COREModelReuse, ram_NamedElement, CORENamedElement, ram_Classifier, ram_Association, ram_Type, ram_Class, Classifier, ram_Operation, MappableElement, Traceable, ram_Parameter, TypedElement, ram_PrimitiveType, ObjectType, ImplementationClass, Type, ram_RVoid, ram_RBoolean, PrimitiveType, StructuralFeature, TemporaryProperty, ram_ObjectType, ram_RString, ram_RAny, ram_REnum, ram_REnumLiteral, ram_AspectMessageView, ram_MessageView, AbstractMessageView, ram_RInt, ram_RChar, FragmentContainer, ram_Lifeline, ram_Message, ram_Reference, ram_Gate, ram_TypedElement, ram_InteractionFragment, ram_Interaction, ram_MessageViewReference, ram_StructuralFeature, ram_ParameterValueMapping, ram_ValueSpecification, ram_TemporaryProperty, ram_MessageEnd, ram_CombinedFragment, ram_InteractionOperand, ram_OriginalBehaviorExecution, ram_ExecutionStatement, ram_StructuralFeatureValue, ValueSpecification, ram_MessageOccurrenceSpecification, OccurrenceSpecification, MessageEnd, ram_OccurrenceSpecification, InteractionFragment, ram_DestructionOccurrenceSpecification, MessageOccurrenceSpecification, ram_FragmentContainer, ram_RCollection, ram_RSet, RCollection, ram_RSequence, ram_ContainerMap, ram_EObject, ram_ElementMap, ram_NewLayoutElement, ram_ParameterValue, ram_OpaqueExpression, ram_LiteralSpecification, ram_LiteralString, LiteralSpecification, ram_LiteralInteger, ram_ImplementationClass, ram_Property, ram_LiteralBoolean, ram_ClassifierMapping, ram_OperationMapping, ram_TypeParameter, ram_StateMachine, ram_CheckState, ram_Transition, ram_Substitution, ram_Constraint, ram_AttributeMapping, ram_ParameterMapping, ram_RFloat, ram_TransitionSubstitution, Substitution, ram_RLong, ram_RArray, ram_RDouble, ram_Traceable, ram_TracingMap, ram_LiteralNull, ram_EnumLiteralValue, ram_AssignmentStatement, ram_RByte, ram_LiteralChar, ram_LiteralDouble, ram_LiteralLong, ram_LiteralFloat, ram_LiteralByte, RAMVisibilityType, ReferenceType, MessageSort, InteractionOperatorKind, InstantiationType, OperationType},
    associations={structuralView0, messageViews1, instantiations3, layout5, stateViews7, wovenAspects9, attributes17, assoc18, classifier19, featureSelection20, ends21, classes11, associations13, types15, returnType22, parameters24, type28, type26, literals31, enum32, affectedBy33, references39, lifelines41, messages43, properties44, formalGates46, pointcut48, advice51, represents54, coveredBy56, specifies35, specification37, signature61, assignTo64, arguments66, interaction68, returns69, localProperties71, message73, sendEvent57, receiveEvent58, operands78, specification79, interactionConstraint81, value84, parameter86, covered76, container77, fragments94, type96, containers98, key100, value102, key104, value107, value89, parameter92, type119, operationMappings122, operations109, associationEnds112, typeParameters114, superTypes117, stateMachines127, specifies129, start132, states134, transitions137, substitutions139, endState141, startState142, signature144, guard147, attributeMappings123, parameterMappings125, Specification152, from155, to157, genericType160, incomings149, outgoings150, comesFrom165, children169, wovenElements171, value173, assignTo174, value176, key179, value181, type163},
    generalizations={gen_ram_Aspect_NamedElement, gen_ram_Aspect_COREModel, gen_ram_MappableElement_NamedElement, gen_ram_AssociationEnd_Property, gen_ram_Association_NamedElement, gen_ram_NamedElement_CORENamedElement, gen_ram_MappableElement_COREModelElement, gen_ram_Class_Classifier, gen_ram_Operation_NamedElement, gen_ram_Operation_MappableElement, gen_ram_Operation_Traceable, gen_ram_Type_NamedElement, gen_ram_Parameter_TypedElement, gen_ram_Parameter_MappableElement, gen_ram_PrimitiveType_ObjectType, gen_ram_PrimitiveType_ImplementationClass, gen_ram_ObjectType_Type, gen_ram_ObjectType_MappableElement, gen_ram_RVoid_Type, gen_ram_RBoolean_PrimitiveType, gen_ram_Attribute_StructuralFeature, gen_ram_Attribute_TemporaryProperty, gen_ram_Attribute_MappableElement, gen_ram_Attribute_Traceable, gen_ram_RString_PrimitiveType, gen_ram_RAny_Type, gen_ram_REnum_PrimitiveType, gen_ram_REnumLiteral_NamedElement, gen_ram_MessageView_AbstractMessageView, gen_ram_RInt_PrimitiveType, gen_ram_RChar_PrimitiveType, gen_ram_Interaction_FragmentContainer, gen_ram_AspectMessageView_AbstractMessageView, gen_ram_AspectMessageView_NamedElement, gen_ram_MessageViewReference_AbstractMessageView, gen_ram_CombinedFragment_InteractionFragment, gen_ram_OriginalBehaviorExecution_InteractionFragment, gen_ram_ExecutionStatement_InteractionFragment, gen_ram_InteractionOperand_FragmentContainer, gen_ram_StructuralFeatureValue_ValueSpecification, gen_ram_MessageOccurrenceSpecification_OccurrenceSpecification, gen_ram_MessageOccurrenceSpecification_MessageEnd, gen_ram_OccurrenceSpecification_InteractionFragment, gen_ram_DestructionOccurrenceSpecification_MessageOccurrenceSpecification, gen_ram_RCollection_Type, gen_ram_RCollection_ImplementationClass, gen_ram_RSet_RCollection, gen_ram_RSequence_RCollection, gen_ram_ParameterValue_ValueSpecification, gen_ram_OpaqueExpression_ValueSpecification, gen_ram_LiteralSpecification_ValueSpecification, gen_ram_LiteralString_LiteralSpecification, gen_ram_LiteralInteger_LiteralSpecification, gen_ram_ImplementationClass_Classifier, gen_ram_StructuralFeature_TypedElement, gen_ram_Reference_Property, gen_ram_Reference_TemporaryProperty, gen_ram_Property_StructuralFeature, gen_ram_TypedElement_NamedElement, gen_ram_Gate_MessageEnd, gen_ram_Gate_NamedElement, gen_ram_LiteralBoolean_LiteralSpecification, gen_ram_Classifier_ObjectType, gen_ram_Classifier_Traceable, gen_ram_StateView_NamedElement, gen_ram_Transition_NamedElement, gen_ram_RFloat_PrimitiveType, gen_ram_TransitionSubstitution_Substitution, gen_ram_TypeParameter_Type, gen_ram_RLong_PrimitiveType, gen_ram_RArray_PrimitiveType, gen_ram_CheckState_NamedElement, gen_ram_RDouble_PrimitiveType, gen_ram_WovenAspect_NamedElement, gen_ram_LiteralNull_LiteralSpecification, gen_ram_EnumLiteralValue_ValueSpecification, gen_ram_AssignmentStatement_InteractionFragment, gen_ram_LiteralChar_LiteralSpecification, gen_ram_LiteralDouble_LiteralSpecification, gen_ram_RByte_PrimitiveType, gen_ram_LiteralLong_LiteralSpecification, gen_ram_LiteralFloat_LiteralSpecification, gen_ram_LiteralByte_LiteralSpecification},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)