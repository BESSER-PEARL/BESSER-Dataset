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
ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="shallowHistory")
    }
)

TypeOfContext: Enumeration = Enumeration(
    name="TypeOfContext",
    literals={
            EnumerationLiteral(name="WIFI_STATUS"),
			EnumerationLiteral(name="BLUETOOTH_STATUS"),
			EnumerationLiteral(name="BATTERY_LEVEL"),
			EnumerationLiteral(name="CPU_LOAD"),
			EnumerationLiteral(name="MEMORY_LOAD"),
			EnumerationLiteral(name="AIRPLANE_MODE"),
			EnumerationLiteral(name="NETWORK_STATUS"),
			EnumerationLiteral(name="GPS_STATUS")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

TypeOfCondition: Enumeration = Enumeration(
    name="TypeOfCondition",
    literals={
            EnumerationLiteral(name="WHILE_EQUALS"),
			EnumerationLiteral(name="WHILE_LOWER"),
			EnumerationLiteral(name="WHILE_HIGHER"),
			EnumerationLiteral(name="WHEN_EQUALS"),
			EnumerationLiteral(name="IS_OFF"),
			EnumerationLiteral(name="IS_ON"),
			EnumerationLiteral(name="IS_EQUAL"),
			EnumerationLiteral(name="WHEN_HIGHER"),
			EnumerationLiteral(name="WHEN_LOWER"),
			EnumerationLiteral(name="IS_DIFFERENT")
    }
)

# Classes
SecCon_MultiplicityElement = Class(name="SecCon::MultiplicityElement", is_abstract=True)
Element = Class(name="Element")
SecCon_NamedElement = Class(name="SecCon::NamedElement", is_abstract=True)
SecCon_Attribute = Class(name="SecCon::Attribute")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
SecCon_Operation = Class(name="SecCon::Operation")
SecCon_Parameter = Class(name="SecCon::Parameter")
SecCon_Element = Class(name="SecCon::Element", is_abstract=True)
SecCon_Comment = Class(name="SecCon::Comment")
SecCon_TypedElement = Class(name="SecCon::TypedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
SecCon_Type = Class(name="SecCon::Type", is_abstract=True)
SecCon_DataType = Class(name="SecCon::DataType", is_abstract=True)
SecCon_PrimitiveType = Class(name="SecCon::PrimitiveType")
DataType = Class(name="DataType")
SecCon_Enumeration = Class(name="SecCon::Enumeration")
SecCon_EnumerationLiteral = Class(name="SecCon::EnumerationLiteral")
SecCon_Actor = Class(name="SecCon::Actor")
SecCon_UseCase = Class(name="SecCon::UseCase", is_abstract=True)
SecCon_Include = Class(name="SecCon::Include")
SecCon_Package = Class(name="SecCon::Package")
SecCon_Class = Class(name="SecCon::Class")
Type = Class(name="Type")
SecCon_CountermeasureUseCase = Class(name="SecCon::CountermeasureUseCase")
SecCon_RecoverUseCase = Class(name="SecCon::RecoverUseCase")
SecCon_PrevenctionUseCase = Class(name="SecCon::PrevenctionUseCase")
SecCon_DetectionUseCase = Class(name="SecCon::DetectionUseCase")
SecCon_Extend = Class(name="SecCon::Extend")
SecCon_UseCaseScenario = Class(name="SecCon::UseCaseScenario")
SecCon_ThreatUseCase = Class(name="SecCon::ThreatUseCase")
UseCase = Class(name="UseCase")
SecCon_AttackUseCase = Class(name="SecCon::AttackUseCase")
SecCon_VulnerabilityUseCase = Class(name="SecCon::VulnerabilityUseCase")
SecCon_Transition = Class(name="SecCon::Transition")
SecCon_State = Class(name="SecCon::State", is_abstract=True)
StateVertex = Class(name="StateVertex")
SecCon_StateOperation = Class(name="SecCon::StateOperation")
SecCon_FinalState = Class(name="SecCon::FinalState")
SecCon_ThreatenedState = Class(name="SecCon::ThreatenedState")
State = Class(name="State")
SecCon_AttackedState = Class(name="SecCon::AttackedState")
SecCon_VulnerableState = Class(name="SecCon::VulnerableState")
SecCon_ProtectedState = Class(name="SecCon::ProtectedState")
SecCon_InitialState = Class(name="SecCon::InitialState")
SecCon_StateMachineScenario = Class(name="SecCon::StateMachineScenario")
SecCon_StateVertex = Class(name="SecCon::StateVertex", is_abstract=True)
SecCon_Event = Class(name="SecCon::Event", is_abstract=True)
SecCon_ContextScenario = Class(name="SecCon::ContextScenario")
SecCon_Rule = Class(name="SecCon::Rule")
SecCon_ContextInformation = Class(name="SecCon::ContextInformation")
SecCon_Condition = Class(name="SecCon::Condition")
SecCon_Action = Class(name="SecCon::Action")
SecCon_CountermeasureEvent = Class(name="SecCon::CountermeasureEvent")
Event = Class(name="Event")
SecCon_ThreatEvent = Class(name="SecCon::ThreatEvent")
SecCon_AttackEvent = Class(name="SecCon::AttackEvent")
SecCon_Project = Class(name="SecCon::Project")

# SecCon_MultiplicityElement class attributes and methods
SecCon_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
SecCon_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
SecCon_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
SecCon_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
SecCon_MultiplicityElement.attributes={SecCon_MultiplicityElement_upper, SecCon_MultiplicityElement_isUnique, SecCon_MultiplicityElement_isOrdered, SecCon_MultiplicityElement_lower}

# Element class attributes and methods

# SecCon_NamedElement class attributes and methods
SecCon_NamedElement_name: Property = Property(name="name", type=StringType)
SecCon_NamedElement.attributes={SecCon_NamedElement_name}

# SecCon_Attribute class attributes and methods
SecCon_Attribute_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
SecCon_Attribute_default: Property = Property(name="default", type=StringType)
SecCon_Attribute_isComposite: Property = Property(name="isComposite", type=BooleanType)
SecCon_Attribute_isDerived: Property = Property(name="isDerived", type=BooleanType)
SecCon_Attribute_isID: Property = Property(name="isID", type=BooleanType)
SecCon_Attribute.attributes={SecCon_Attribute_isReadOnly, SecCon_Attribute_isID, SecCon_Attribute_default, SecCon_Attribute_isComposite, SecCon_Attribute_isDerived}

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# SecCon_Operation class attributes and methods
SecCon_Operation_body: Property = Property(name="body", type=StringType)
SecCon_Operation.attributes={SecCon_Operation_body}

# SecCon_Parameter class attributes and methods
SecCon_Parameter_default: Property = Property(name="default", type=StringType)
SecCon_Parameter_direction: Property = Property(name="direction", type=StringType)
SecCon_Parameter.attributes={SecCon_Parameter_default, SecCon_Parameter_direction}

# SecCon_Element class attributes and methods

# SecCon_Comment class attributes and methods
SecCon_Comment_body: Property = Property(name="body", type=StringType)
SecCon_Comment.attributes={SecCon_Comment_body}

# SecCon_TypedElement class attributes and methods

# NamedElement class attributes and methods

# SecCon_Type class attributes and methods

# SecCon_DataType class attributes and methods

# SecCon_PrimitiveType class attributes and methods

# DataType class attributes and methods

# SecCon_Enumeration class attributes and methods

# SecCon_EnumerationLiteral class attributes and methods

# SecCon_Actor class attributes and methods

# SecCon_UseCase class attributes and methods
SecCon_UseCase_description: Property = Property(name="description", type=StringType)
SecCon_UseCase_preCondition: Property = Property(name="preCondition", type=StringType)
SecCon_UseCase.attributes={SecCon_UseCase_preCondition, SecCon_UseCase_description}

# SecCon_Include class attributes and methods
SecCon_Include_name: Property = Property(name="name", type=StringType)
SecCon_Include.attributes={SecCon_Include_name}

# SecCon_Package class attributes and methods

# SecCon_Class class attributes and methods
SecCon_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
SecCon_Class.attributes={SecCon_Class_isAbstract}

# Type class attributes and methods

# SecCon_CountermeasureUseCase class attributes and methods

# SecCon_RecoverUseCase class attributes and methods

# SecCon_PrevenctionUseCase class attributes and methods

# SecCon_DetectionUseCase class attributes and methods

# SecCon_Extend class attributes and methods
SecCon_Extend_name: Property = Property(name="name", type=StringType)
SecCon_Extend_condition: Property = Property(name="condition", type=StringType)
SecCon_Extend.attributes={SecCon_Extend_name, SecCon_Extend_condition}

# SecCon_UseCaseScenario class attributes and methods
SecCon_UseCaseScenario_author: Property = Property(name="author", type=StringType)
SecCon_UseCaseScenario_version: Property = Property(name="version", type=StringType)
SecCon_UseCaseScenario.attributes={SecCon_UseCaseScenario_version, SecCon_UseCaseScenario_author}

# SecCon_ThreatUseCase class attributes and methods

# UseCase class attributes and methods

# SecCon_AttackUseCase class attributes and methods

# SecCon_VulnerabilityUseCase class attributes and methods

# SecCon_Transition class attributes and methods

# SecCon_State class attributes and methods

# StateVertex class attributes and methods

# SecCon_StateOperation class attributes and methods

# SecCon_FinalState class attributes and methods

# SecCon_ThreatenedState class attributes and methods

# State class attributes and methods

# SecCon_AttackedState class attributes and methods

# SecCon_VulnerableState class attributes and methods

# SecCon_ProtectedState class attributes and methods

# SecCon_InitialState class attributes and methods

# SecCon_StateMachineScenario class attributes and methods
SecCon_StateMachineScenario_author: Property = Property(name="author", type=StringType)
SecCon_StateMachineScenario_version: Property = Property(name="version", type=StringType)
SecCon_StateMachineScenario.attributes={SecCon_StateMachineScenario_version, SecCon_StateMachineScenario_author}

# SecCon_StateVertex class attributes and methods

# SecCon_Event class attributes and methods

# SecCon_ContextScenario class attributes and methods
SecCon_ContextScenario_name: Property = Property(name="name", type=StringType)
SecCon_ContextScenario.attributes={SecCon_ContextScenario_name}

# SecCon_Rule class attributes and methods
SecCon_Rule_name: Property = Property(name="name", type=StringType)
SecCon_Rule_operator: Property = Property(name="operator", type=StringType)
SecCon_Rule_logicValue: Property = Property(name="logicValue", type=BooleanType)
SecCon_Rule.attributes={SecCon_Rule_logicValue, SecCon_Rule_name, SecCon_Rule_operator}

# SecCon_ContextInformation class attributes and methods
SecCon_ContextInformation_name: Property = Property(name="name", type=StringType)
SecCon_ContextInformation_type: Property = Property(name="type", type=StringType)
SecCon_ContextInformation.attributes={SecCon_ContextInformation_type, SecCon_ContextInformation_name}

# SecCon_Condition class attributes and methods
SecCon_Condition_condition: Property = Property(name="condition", type=StringType)
SecCon_Condition_value: Property = Property(name="value", type=StringType)
SecCon_Condition_logicValue: Property = Property(name="logicValue", type=BooleanType)
SecCon_Condition.attributes={SecCon_Condition_logicValue, SecCon_Condition_value, SecCon_Condition_condition}

# SecCon_Action class attributes and methods
SecCon_Action_name: Property = Property(name="name", type=StringType)
SecCon_Action_parameter: Property = Property(name="parameter", type=StringType)
SecCon_Action.attributes={SecCon_Action_name, SecCon_Action_parameter}

# SecCon_CountermeasureEvent class attributes and methods

# Event class attributes and methods

# SecCon_ThreatEvent class attributes and methods

# SecCon_AttackEvent class attributes and methods

# SecCon_Project class attributes and methods

# Relationships
annotatedElement2: BinaryAssociation = BinaryAssociation(
    name="annotatedElement2",
    ends={
        Property(name="SecCon_Element4", type=SecCon_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Comment3", type=SecCon_Element, multiplicity=Multiplicity(0, 9999))
    }
)
opposite6: BinaryAssociation = BinaryAssociation(
    name="opposite6",
    ends={
        Property(name="SecCon_Attribute", type=SecCon_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Attribute5", type=SecCon_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
raisedException7: BinaryAssociation = BinaryAssociation(
    name="raisedException7",
    ends={
        Property(name="SecCon_Type8", type=SecCon_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Operation", type=SecCon_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter9: BinaryAssociation = BinaryAssociation(
    name="ownedParameter9",
    ends={
        Property(name="SecCon_Parameter", type=SecCon_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Operation10", type=SecCon_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement0: BinaryAssociation = BinaryAssociation(
    name="ownedElement0",
    ends={
        Property(name="SecCon_Comment", type=SecCon_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Element", type=SecCon_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="SecCon_Type", type=SecCon_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_TypedElement", type=SecCon_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral21: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral21",
    ends={
        Property(name="EnumerationLiteral", type=SecCon_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=SecCon_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration22: BinaryAssociation = BinaryAssociation(
    name="enumeration22",
    ends={
        Property(name="Enumeration", type=SecCon_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=SecCon_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
ownedType23: BinaryAssociation = BinaryAssociation(
    name="ownedType23",
    ends={
        Property(name="SecCon_Type25", type=SecCon_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Package24", type=SecCon_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage27: BinaryAssociation = BinaryAssociation(
    name="nestedPackage27",
    ends={
        Property(name="Package", type=SecCon_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=SecCon_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage29: BinaryAssociation = BinaryAssociation(
    name="nestingPackage29",
    ends={
        Property(name="Package30", type=SecCon_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=SecCon_Package, multiplicity=Multiplicity(0, 1))
    }
)
actor31: BinaryAssociation = BinaryAssociation(
    name="actor31",
    ends={
        Property(name="SecCon_Actor", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_UseCase", type=SecCon_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
includes32: BinaryAssociation = BinaryAssociation(
    name="includes32",
    ends={
        Property(name="Include", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="addition", type=SecCon_Include, multiplicity=Multiplicity(0, 9999))
    }
)
include33: BinaryAssociation = BinaryAssociation(
    name="include33",
    ends={
        Property(name="Include34", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=SecCon_Include, multiplicity=Multiplicity(0, 1))
    }
)
package11: BinaryAssociation = BinaryAssociation(
    name="package11",
    ends={
        Property(name="SecCon_Package", type=SecCon_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Type12", type=SecCon_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedOperation13: BinaryAssociation = BinaryAssociation(
    name="ownedOperation13",
    ends={
        Property(name="SecCon_Operation14", type=SecCon_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Class", type=SecCon_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass16: BinaryAssociation = BinaryAssociation(
    name="superclass16",
    ends={
        Property(name="SecCon_Class17", type=SecCon_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Class15", type=SecCon_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute18: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute18",
    ends={
        Property(name="SecCon_Attribute20", type=SecCon_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Class19", type=SecCon_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addition41: BinaryAssociation = BinaryAssociation(
    name="addition41",
    ends={
        Property(name="UseCase", type=SecCon_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="includes", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base42: BinaryAssociation = BinaryAssociation(
    name="base42",
    ends={
        Property(name="UseCase43", type=SecCon_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
scenario44: BinaryAssociation = BinaryAssociation(
    name="scenario44",
    ends={
        Property(name="SecCon_UseCaseScenario45", type=SecCon_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Include", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(0, 1))
    }
)
extension46: BinaryAssociation = BinaryAssociation(
    name="extension46",
    ends={
        Property(name="UseCase47", type=SecCon_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base48: BinaryAssociation = BinaryAssociation(
    name="base48",
    ends={
        Property(name="UseCase49", type=SecCon_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extends", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1))
    }
)
scenario50: BinaryAssociation = BinaryAssociation(
    name="scenario50",
    ends={
        Property(name="SecCon_UseCaseScenario51", type=SecCon_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Extend", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(0, 1))
    }
)
ownedUseCase52: BinaryAssociation = BinaryAssociation(
    name="ownedUseCase52",
    ends={
        Property(name="SecCon_UseCase54", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_UseCaseScenario53", type=SecCon_UseCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtend55: BinaryAssociation = BinaryAssociation(
    name="ownedExtend55",
    ends={
        Property(name="SecCon_Extend57", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_UseCaseScenario56", type=SecCon_Extend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInclude58: BinaryAssociation = BinaryAssociation(
    name="ownedInclude58",
    ends={
        Property(name="SecCon_Include60", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_UseCaseScenario59", type=SecCon_Include, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend35: BinaryAssociation = BinaryAssociation(
    name="extend35",
    ends={
        Property(name="Extend", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=SecCon_Extend, multiplicity=Multiplicity(0, 9999))
    }
)
extends36: BinaryAssociation = BinaryAssociation(
    name="extends36",
    ends={
        Property(name="Extend38", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base37", type=SecCon_Extend, multiplicity=Multiplicity(0, 9999))
    }
)
scenario39: BinaryAssociation = BinaryAssociation(
    name="scenario39",
    ends={
        Property(name="SecCon_UseCaseScenario", type=SecCon_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_UseCase40", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(0, 1))
    }
)
ownedTransition67: BinaryAssociation = BinaryAssociation(
    name="ownedTransition67",
    ends={
        Property(name="SecCon_Transition", type=SecCon_StateMachineScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_StateMachineScenario68", type=SecCon_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing69: BinaryAssociation = BinaryAssociation(
    name="outgoing69",
    ends={
        Property(name="SecCon_Transition71", type=SecCon_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_StateVertex70", type=SecCon_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming72: BinaryAssociation = BinaryAssociation(
    name="incoming72",
    ends={
        Property(name="SecCon_Transition74", type=SecCon_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_StateVertex73", type=SecCon_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownedStateOperation75: BinaryAssociation = BinaryAssociation(
    name="ownedStateOperation75",
    ends={
        Property(name="SecCon_StateOperation", type=SecCon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_State", type=SecCon_StateOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableEvent76: BinaryAssociation = BinaryAssociation(
    name="deferrableEvent76",
    ends={
        Property(name="SecCon_Event78", type=SecCon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_State77", type=SecCon_Event, multiplicity=Multiplicity(0, 9999))
    }
)
trigger79: BinaryAssociation = BinaryAssociation(
    name="trigger79",
    ends={
        Property(name="SecCon_Event81", type=SecCon_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Transition80", type=SecCon_Event, multiplicity=Multiplicity(0, 1))
    }
)
ownedActor61: BinaryAssociation = BinaryAssociation(
    name="ownedActor61",
    ends={
        Property(name="SecCon_Actor63", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_UseCaseScenario62", type=SecCon_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedState64: BinaryAssociation = BinaryAssociation(
    name="ownedState64",
    ends={
        Property(name="SecCon_StateVertex", type=SecCon_StateMachineScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_StateMachineScenario", type=SecCon_StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEvent65: BinaryAssociation = BinaryAssociation(
    name="ownedEvent65",
    ends={
        Property(name="SecCon_Event", type=SecCon_StateMachineScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_StateMachineScenario66", type=SecCon_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedUseCaseScenario84: BinaryAssociation = BinaryAssociation(
    name="ownedUseCaseScenario84",
    ends={
        Property(name="SecCon_Project85", type=SecCon_UseCaseScenario, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="SecCon_UseCaseScenario86", type=SecCon_Project, multiplicity=Multiplicity(1, 1))
    }
)
ownedStateMachineScenario87: BinaryAssociation = BinaryAssociation(
    name="ownedStateMachineScenario87",
    ends={
        Property(name="SecCon_StateMachineScenario89", type=SecCon_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Project88", type=SecCon_StateMachineScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedContextScenario90: BinaryAssociation = BinaryAssociation(
    name="ownedContextScenario90",
    ends={
        Property(name="SecCon_ContextScenario", type=SecCon_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Project91", type=SecCon_ContextScenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains92: BinaryAssociation = BinaryAssociation(
    name="contains92",
    ends={
        Property(name="SecCon_Rule", type=SecCon_ContextScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_ContextScenario93", type=SecCon_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isFormed94: BinaryAssociation = BinaryAssociation(
    name="isFormed94",
    ends={
        Property(name="SecCon_ContextInformation", type=SecCon_ContextScenario, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_ContextScenario95", type=SecCon_ContextInformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasCondition96: BinaryAssociation = BinaryAssociation(
    name="hasCondition96",
    ends={
        Property(name="SecCon_Condition", type=SecCon_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Rule97", type=SecCon_Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
hasAction98: BinaryAssociation = BinaryAssociation(
    name="hasAction98",
    ends={
        Property(name="SecCon_Action", type=SecCon_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Rule99", type=SecCon_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
hasContextInformation100: BinaryAssociation = BinaryAssociation(
    name="hasContextInformation100",
    ends={
        Property(name="SecCon_ContextInformation102", type=SecCon_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Condition101", type=SecCon_ContextInformation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedPackages82: BinaryAssociation = BinaryAssociation(
    name="ownedPackages82",
    ends={
        Property(name="SecCon_Package83", type=SecCon_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="SecCon_Project", type=SecCon_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SecCon_MultiplicityElement_Element = Generalization(general=Element, specific=SecCon_MultiplicityElement)
gen_SecCon_NamedElement_Element = Generalization(general=Element, specific=SecCon_NamedElement)
gen_SecCon_Attribute_TypedElement = Generalization(general=TypedElement, specific=SecCon_Attribute)
gen_SecCon_Attribute_MultiplicityElement = Generalization(general=MultiplicityElement, specific=SecCon_Attribute)
gen_SecCon_Operation_TypedElement = Generalization(general=TypedElement, specific=SecCon_Operation)
gen_SecCon_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=SecCon_Operation)
gen_SecCon_Parameter_TypedElement = Generalization(general=TypedElement, specific=SecCon_Parameter)
gen_SecCon_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=SecCon_Parameter)
gen_SecCon_Type_NamedElement = Generalization(general=NamedElement, specific=SecCon_Type)
gen_SecCon_TypedElement_NamedElement = Generalization(general=NamedElement, specific=SecCon_TypedElement)
gen_SecCon_DataType_Type = Generalization(general=Type, specific=SecCon_DataType)
gen_SecCon_PrimitiveType_DataType = Generalization(general=DataType, specific=SecCon_PrimitiveType)
gen_SecCon_Enumeration_DataType = Generalization(general=DataType, specific=SecCon_Enumeration)
gen_SecCon_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=SecCon_EnumerationLiteral)
gen_SecCon_Package_NamedElement = Generalization(general=NamedElement, specific=SecCon_Package)
gen_SecCon_Actor_NamedElement = Generalization(general=NamedElement, specific=SecCon_Actor)
gen_SecCon_UseCase_NamedElement = Generalization(general=NamedElement, specific=SecCon_UseCase)
gen_SecCon_Class_Type = Generalization(general=Type, specific=SecCon_Class)
gen_SecCon_CountermeasureUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_CountermeasureUseCase)
gen_SecCon_RecoverUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_RecoverUseCase)
gen_SecCon_PrevenctionUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_PrevenctionUseCase)
gen_SecCon_DetectionUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_DetectionUseCase)
gen_SecCon_UseCaseScenario_NamedElement = Generalization(general=NamedElement, specific=SecCon_UseCaseScenario)
gen_SecCon_ThreatUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_ThreatUseCase)
gen_SecCon_AttackUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_AttackUseCase)
gen_SecCon_VulnerabilityUseCase_UseCase = Generalization(general=UseCase, specific=SecCon_VulnerabilityUseCase)
gen_SecCon_StateVertex_NamedElement = Generalization(general=NamedElement, specific=SecCon_StateVertex)
gen_SecCon_State_StateVertex = Generalization(general=StateVertex, specific=SecCon_State)
gen_SecCon_StateOperation_NamedElement = Generalization(general=NamedElement, specific=SecCon_StateOperation)
gen_SecCon_FinalState_StateVertex = Generalization(general=StateVertex, specific=SecCon_FinalState)
gen_SecCon_ThreatenedState_State = Generalization(general=State, specific=SecCon_ThreatenedState)
gen_SecCon_AttackedState_State = Generalization(general=State, specific=SecCon_AttackedState)
gen_SecCon_VulnerableState_State = Generalization(general=State, specific=SecCon_VulnerableState)
gen_SecCon_ProtectedState_State = Generalization(general=State, specific=SecCon_ProtectedState)
gen_SecCon_Transition_NamedElement = Generalization(general=NamedElement, specific=SecCon_Transition)
gen_SecCon_Event_NamedElement = Generalization(general=NamedElement, specific=SecCon_Event)
gen_SecCon_InitialState_StateVertex = Generalization(general=StateVertex, specific=SecCon_InitialState)
gen_SecCon_StateMachineScenario_NamedElement = Generalization(general=NamedElement, specific=SecCon_StateMachineScenario)
gen_SecCon_CountermeasureEvent_Event = Generalization(general=Event, specific=SecCon_CountermeasureEvent)
gen_SecCon_ThreatEvent_Event = Generalization(general=Event, specific=SecCon_ThreatEvent)
gen_SecCon_AttackEvent_Event = Generalization(general=Event, specific=SecCon_AttackEvent)
gen_SecCon_Project_NamedElement = Generalization(general=NamedElement, specific=SecCon_Project)

# Domain Model
domain_model = DomainModel(
    name="SecCon",
    types={SecCon_MultiplicityElement, Element, SecCon_NamedElement, SecCon_Attribute, TypedElement, MultiplicityElement, SecCon_Operation, SecCon_Parameter, SecCon_Element, SecCon_Comment, SecCon_TypedElement, NamedElement, SecCon_Type, SecCon_DataType, SecCon_PrimitiveType, DataType, SecCon_Enumeration, SecCon_EnumerationLiteral, SecCon_Actor, SecCon_UseCase, SecCon_Include, SecCon_Package, SecCon_Class, Type, SecCon_CountermeasureUseCase, SecCon_RecoverUseCase, SecCon_PrevenctionUseCase, SecCon_DetectionUseCase, SecCon_Extend, SecCon_UseCaseScenario, SecCon_ThreatUseCase, UseCase, SecCon_AttackUseCase, SecCon_VulnerabilityUseCase, SecCon_Transition, SecCon_State, StateVertex, SecCon_StateOperation, SecCon_FinalState, SecCon_ThreatenedState, State, SecCon_AttackedState, SecCon_VulnerableState, SecCon_ProtectedState, SecCon_InitialState, SecCon_StateMachineScenario, SecCon_StateVertex, SecCon_Event, SecCon_ContextScenario, SecCon_Rule, SecCon_ContextInformation, SecCon_Condition, SecCon_Action, SecCon_CountermeasureEvent, Event, SecCon_ThreatEvent, SecCon_AttackEvent, SecCon_Project, ParameterDirectionKind, PseudostateKind, TypeOfContext, Operator, TypeOfCondition},
    associations={annotatedElement2, opposite6, raisedException7, ownedParameter9, ownedElement0, type1, ownedLiteral21, enumeration22, ownedType23, nestedPackage27, nestingPackage29, actor31, includes32, include33, package11, ownedOperation13, superclass16, ownedAttribute18, addition41, base42, scenario44, extension46, base48, scenario50, ownedUseCase52, ownedExtend55, ownedInclude58, extend35, extends36, scenario39, ownedTransition67, outgoing69, incoming72, ownedStateOperation75, deferrableEvent76, trigger79, ownedActor61, ownedState64, ownedEvent65, ownedUseCaseScenario84, ownedStateMachineScenario87, ownedContextScenario90, contains92, isFormed94, hasCondition96, hasAction98, hasContextInformation100, ownedPackages82},
    generalizations={gen_SecCon_MultiplicityElement_Element, gen_SecCon_NamedElement_Element, gen_SecCon_Attribute_TypedElement, gen_SecCon_Attribute_MultiplicityElement, gen_SecCon_Operation_TypedElement, gen_SecCon_Operation_MultiplicityElement, gen_SecCon_Parameter_TypedElement, gen_SecCon_Parameter_MultiplicityElement, gen_SecCon_Type_NamedElement, gen_SecCon_TypedElement_NamedElement, gen_SecCon_DataType_Type, gen_SecCon_PrimitiveType_DataType, gen_SecCon_Enumeration_DataType, gen_SecCon_EnumerationLiteral_NamedElement, gen_SecCon_Package_NamedElement, gen_SecCon_Actor_NamedElement, gen_SecCon_UseCase_NamedElement, gen_SecCon_Class_Type, gen_SecCon_CountermeasureUseCase_UseCase, gen_SecCon_RecoverUseCase_UseCase, gen_SecCon_PrevenctionUseCase_UseCase, gen_SecCon_DetectionUseCase_UseCase, gen_SecCon_UseCaseScenario_NamedElement, gen_SecCon_ThreatUseCase_UseCase, gen_SecCon_AttackUseCase_UseCase, gen_SecCon_VulnerabilityUseCase_UseCase, gen_SecCon_StateVertex_NamedElement, gen_SecCon_State_StateVertex, gen_SecCon_StateOperation_NamedElement, gen_SecCon_FinalState_StateVertex, gen_SecCon_ThreatenedState_State, gen_SecCon_AttackedState_State, gen_SecCon_VulnerableState_State, gen_SecCon_ProtectedState_State, gen_SecCon_Transition_NamedElement, gen_SecCon_Event_NamedElement, gen_SecCon_InitialState_StateVertex, gen_SecCon_StateMachineScenario_NamedElement, gen_SecCon_CountermeasureEvent_Event, gen_SecCon_ThreatEvent_Event, gen_SecCon_AttackEvent_Event, gen_SecCon_Project_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)