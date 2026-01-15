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
InstanceState: Enumeration = Enumeration(
    name="InstanceState",
    literals={
            EnumerationLiteral(name="OFF"),
			EnumerationLiteral(name="ON")
    }
)

PortRole: Enumeration = Enumeration(
    name="PortRole",
    literals={
            EnumerationLiteral(name="client"),
			EnumerationLiteral(name="server")
    }
)

# Classes
art_NamedElement = Class(name="art::NamedElement", is_abstract=True)
art_ModelElement = Class(name="art::ModelElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
art_System = Class(name="art::System")
ModelElement = Class(name="ModelElement")
Node = Class(name="Node")
Service = Class(name="Service")
ComponentType = Class(name="ComponentType")
art_DataType = Class(name="art::DataType")
Group = Class(name="Group")
art_TypedElement = Class(name="art::TypedElement", is_abstract=True)
art_CardinalityElement = Class(name="art::CardinalityElement", is_abstract=True)
art_instance_ComponentInstance = Class(name="art::instance::ComponentInstance", is_abstract=True)
CompositeInstance = Class(name="CompositeInstance")
AttributeInstance = Class(name="AttributeInstance")
TransmissionBinding = Class(name="TransmissionBinding")
ComponentImplementation = Class(name="ComponentImplementation")
InstanceGroup = Class(name="InstanceGroup")
art_instance_PrimitiveInstance = Class(name="art::instance::PrimitiveInstance")
ComponentInstance = Class(name="ComponentInstance")
art_instance_CompositeInstance = Class(name="art::instance::CompositeInstance")
DelegationBinding = Class(name="DelegationBinding")
art_instance_Binding = Class(name="art::instance::Binding", is_abstract=True)
art_instance_TransmissionBinding = Class(name="art::instance::TransmissionBinding")
Binding = Class(name="Binding")
AbstractPort = Class(name="AbstractPort")
art_instance_DelegationBinding = Class(name="art::instance::DelegationBinding")
art_instance_AttributeInstance = Class(name="art::instance::AttributeInstance", is_abstract=True)
art_instance_DictionaryValuedAttribute = Class(name="art::instance::DictionaryValuedAttribute")
Entry = Class(name="Entry")
Dictionary = Class(name="Dictionary")
art_instance_Entry = Class(name="art::instance::Entry", is_abstract=True)
art_instance_DefaultEntry = Class(name="art::instance::DefaultEntry")
DictionaryDefaultValue = Class(name="DictionaryDefaultValue")
art_instance_OtherEntry = Class(name="art::instance::OtherEntry")
art_type_ComponentType = Class(name="art::type::ComponentType", is_abstract=True)
Attribute = Class(name="Attribute")
TypeGroup = Class(name="TypeGroup")
TypeImplementation = Class(name="TypeImplementation")
art_type_PrimitiveType = Class(name="art::type::PrimitiveType")
art_type_CompositeType = Class(name="art::type::CompositeType")
art_type_Service = Class(name="art::type::Service", is_abstract=True)
Operation = Class(name="Operation")
art_type_Operation = Class(name="art::type::Operation")
Parameter_ = Class(name="Parameter")
art_type_Parameter = Class(name="art::type::Parameter")
TypedElement = Class(name="TypedElement")
art_type_FunctionalService = Class(name="art::type::FunctionalService")
art_instance_ValuedAttribute = Class(name="art::instance::ValuedAttribute")
art_type_ControlService = Class(name="art::type::ControlService")
art_type_AbstractPort = Class(name="art::type::AbstractPort", is_abstract=True)
BasicAttribute = Class(name="BasicAttribute")
art_group_TypeGroup = Class(name="art::group::TypeGroup")
art_type_Port = Class(name="art::type::Port")
CardinalityElement = Class(name="CardinalityElement")
type_AbstractPort = Class(name="type::AbstractPort")
art_type_PortCollection = Class(name="art::type::PortCollection")
PortId = Class(name="PortId")
art_type_PortId = Class(name="art::type::PortId")
art_type_Attribute = Class(name="art::type::Attribute", is_abstract=True)
art_type_BasicAttribute = Class(name="art::type::BasicAttribute")
art_type_Dictionary = Class(name="art::type::Dictionary")
type_art_DataType = Class(name="type::art::DataType")
art_type_DictionaryDefaultValue = Class(name="art::type::DictionaryDefaultValue")
art_implem_ComponentImplementation = Class(name="art::implem::ComponentImplementation", is_abstract=True)
art_implem_FractalComponent = Class(name="art::implem::FractalComponent")
art_implem_OSGiComponent = Class(name="art::implem::OSGiComponent")
art_implem_TypeImplementation = Class(name="art::implem::TypeImplementation", is_abstract=True)
art_implem_OSGiType = Class(name="art::implem::OSGiType")
art_group_Group = Class(name="art::group::Group", is_abstract=True)
art_group_InstanceGroup = Class(name="art::group::InstanceGroup")
art_distrib_Node = Class(name="art::distrib::Node")

# art_NamedElement class attributes and methods
art_NamedElement_name: Property = Property(name="name", type=StringType)
art_NamedElement.attributes={art_NamedElement_name}

# art_ModelElement class attributes and methods

# NamedElement class attributes and methods

# art_System class attributes and methods

# ModelElement class attributes and methods

# Node class attributes and methods

# Service class attributes and methods

# ComponentType class attributes and methods

# art_DataType class attributes and methods

# Group class attributes and methods

# art_TypedElement class attributes and methods

# art_CardinalityElement class attributes and methods
art_CardinalityElement_lower: Property = Property(name="lower", type=StringType)
art_CardinalityElement_upper: Property = Property(name="upper", type=StringType)
art_CardinalityElement.attributes={art_CardinalityElement_lower, art_CardinalityElement_upper}

# art_instance_ComponentInstance class attributes and methods
art_instance_ComponentInstance_state: Property = Property(name="state", type=StringType)
art_instance_ComponentInstance.attributes={art_instance_ComponentInstance_state}

# CompositeInstance class attributes and methods

# AttributeInstance class attributes and methods

# TransmissionBinding class attributes and methods

# ComponentImplementation class attributes and methods

# InstanceGroup class attributes and methods

# art_instance_PrimitiveInstance class attributes and methods

# ComponentInstance class attributes and methods

# art_instance_CompositeInstance class attributes and methods

# DelegationBinding class attributes and methods

# art_instance_Binding class attributes and methods
art_instance_Binding_id: Property = Property(name="id", type=StringType)
art_instance_Binding.attributes={art_instance_Binding_id}

# art_instance_TransmissionBinding class attributes and methods

# Binding class attributes and methods

# AbstractPort class attributes and methods

# art_instance_DelegationBinding class attributes and methods

# art_instance_AttributeInstance class attributes and methods

# art_instance_DictionaryValuedAttribute class attributes and methods

# Entry class attributes and methods

# Dictionary class attributes and methods

# art_instance_Entry class attributes and methods
art_instance_Entry_value: Property = Property(name="value", type=StringType)
art_instance_Entry.attributes={art_instance_Entry_value}

# art_instance_DefaultEntry class attributes and methods

# DictionaryDefaultValue class attributes and methods

# art_instance_OtherEntry class attributes and methods
art_instance_OtherEntry_key: Property = Property(name="key", type=StringType)
art_instance_OtherEntry.attributes={art_instance_OtherEntry_key}

# art_type_ComponentType class attributes and methods

# Attribute class attributes and methods

# TypeGroup class attributes and methods

# TypeImplementation class attributes and methods

# art_type_PrimitiveType class attributes and methods

# art_type_CompositeType class attributes and methods

# art_type_Service class attributes and methods

# Operation class attributes and methods

# art_type_Operation class attributes and methods

# Parameter class attributes and methods

# art_type_Parameter class attributes and methods

# TypedElement class attributes and methods

# art_type_FunctionalService class attributes and methods

# art_instance_ValuedAttribute class attributes and methods
art_instance_ValuedAttribute_value: Property = Property(name="value", type=StringType)
art_instance_ValuedAttribute.attributes={art_instance_ValuedAttribute_value}

# art_type_ControlService class attributes and methods

# art_type_AbstractPort class attributes and methods
art_type_AbstractPort_role: Property = Property(name="role", type=StringType)
art_type_AbstractPort_protocol: Property = Property(name="protocol", type=StringType)
art_type_AbstractPort_uri: Property = Property(name="uri", type=StringType)
art_type_AbstractPort.attributes={art_type_AbstractPort_protocol, art_type_AbstractPort_uri, art_type_AbstractPort_role}

# BasicAttribute class attributes and methods

# art_group_TypeGroup class attributes and methods

# art_type_Port class attributes and methods

# CardinalityElement class attributes and methods

# type_AbstractPort class attributes and methods

# art_type_PortCollection class attributes and methods

# PortId class attributes and methods

# art_type_PortId class attributes and methods

# art_type_Attribute class attributes and methods

# art_type_BasicAttribute class attributes and methods
art_type_BasicAttribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
art_type_BasicAttribute.attributes={art_type_BasicAttribute_defaultValue}

# art_type_Dictionary class attributes and methods

# type_art_DataType class attributes and methods

# art_type_DictionaryDefaultValue class attributes and methods
art_type_DictionaryDefaultValue_key: Property = Property(name="key", type=StringType)
art_type_DictionaryDefaultValue_value: Property = Property(name="value", type=StringType)
art_type_DictionaryDefaultValue.attributes={art_type_DictionaryDefaultValue_key, art_type_DictionaryDefaultValue_value}

# art_implem_ComponentImplementation class attributes and methods

# art_implem_FractalComponent class attributes and methods
art_implem_FractalComponent_controllerDesc: Property = Property(name="controllerDesc", type=StringType)
art_implem_FractalComponent_contentDesc: Property = Property(name="contentDesc", type=StringType)
art_implem_FractalComponent.attributes={art_implem_FractalComponent_contentDesc, art_implem_FractalComponent_controllerDesc}

# art_implem_OSGiComponent class attributes and methods
art_implem_OSGiComponent_implementingClass: Property = Property(name="implementingClass", type=StringType)
art_implem_OSGiComponent.attributes={art_implem_OSGiComponent_implementingClass}

# art_implem_TypeImplementation class attributes and methods

# art_implem_OSGiType class attributes and methods
art_implem_OSGiType_generateInstanceBundle: Property = Property(name="generateInstanceBundle", type=StringType)
art_implem_OSGiType.attributes={art_implem_OSGiType_generateInstanceBundle}

# art_group_Group class attributes and methods

# art_group_InstanceGroup class attributes and methods

# art_distrib_Node class attributes and methods
art_distrib_Node_uri: Property = Property(name="uri", type=StringType)
art_distrib_Node.attributes={art_distrib_Node_uri}

# Relationships
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="ComponentType12", type=art_instance_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_ComponentInstance", type=ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=art_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_System", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services1: BinaryAssociation = BinaryAssociation(
    name="services1",
    ends={
        Property(name="Service", type=art_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_System2", type=Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types3: BinaryAssociation = BinaryAssociation(
    name="types3",
    ends={
        Property(name="ComponentType", type=art_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_System4", type=ComponentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes5: BinaryAssociation = BinaryAssociation(
    name="dataTypes5",
    ends={
        Property(name="art_DataType", type=art_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_System6", type=art_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups7: BinaryAssociation = BinaryAssociation(
    name="groups7",
    ends={
        Property(name="Group", type=art_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_System8", type=Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="art_DataType10", type=art_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="art_TypedElement", type=art_DataType, multiplicity=Multiplicity(1, 1))
    }
)
superComponent13: BinaryAssociation = BinaryAssociation(
    name="superComponent13",
    ends={
        Property(name="instance", type=art_instance_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="CompositeInstance", type=CompositeInstance, multiplicity=Multiplicity(0, 1))
    }
)
attribute14: BinaryAssociation = BinaryAssociation(
    name="attribute14",
    ends={
        Property(name="AttributeInstance", type=art_instance_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_ComponentInstance15", type=AttributeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binding16: BinaryAssociation = BinaryAssociation(
    name="binding16",
    ends={
        Property(name="TransmissionBinding", type=art_instance_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_ComponentInstance17", type=TransmissionBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implem18: BinaryAssociation = BinaryAssociation(
    name="implem18",
    ends={
        Property(name="ComponentImplementation", type=art_instance_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_ComponentInstance19", type=ComponentImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groups20: BinaryAssociation = BinaryAssociation(
    name="groups20",
    ends={
        Property(name="group", type=art_instance_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="InstanceGroup", type=InstanceGroup, multiplicity=Multiplicity(0, 9999))
    }
)
subComponent21: BinaryAssociation = BinaryAssociation(
    name="subComponent21",
    ends={
        Property(name="instance22", type=art_instance_CompositeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentInstance", type=ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegation23: BinaryAssociation = BinaryAssociation(
    name="delegation23",
    ends={
        Property(name="DelegationBinding", type=art_instance_CompositeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_CompositeInstance", type=DelegationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serverInstance24: BinaryAssociation = BinaryAssociation(
    name="serverInstance24",
    ends={
        Property(name="ComponentInstance25", type=art_instance_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_Binding", type=ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
client26: BinaryAssociation = BinaryAssociation(
    name="client26",
    ends={
        Property(name="AbstractPort", type=art_instance_TransmissionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_TransmissionBinding", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
server27: BinaryAssociation = BinaryAssociation(
    name="server27",
    ends={
        Property(name="AbstractPort29", type=art_instance_TransmissionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_TransmissionBinding28", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="AbstractPort31", type=art_instance_DelegationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_DelegationBinding", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
exported32: BinaryAssociation = BinaryAssociation(
    name="exported32",
    ends={
        Property(name="AbstractPort34", type=art_instance_DelegationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_DelegationBinding33", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
attribute35: BinaryAssociation = BinaryAssociation(
    name="attribute35",
    ends={
        Property(name="BasicAttribute", type=art_instance_ValuedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_ValuedAttribute", type=BasicAttribute, multiplicity=Multiplicity(1, 1))
    }
)
service53: BinaryAssociation = BinaryAssociation(
    name="service53",
    ends={
        Property(name="Service54", type=art_type_AbstractPort, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_AbstractPort", type=Service, multiplicity=Multiplicity(1, 1))
    }
)
entries36: BinaryAssociation = BinaryAssociation(
    name="entries36",
    ends={
        Property(name="Entry", type=art_instance_DictionaryValuedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_DictionaryValuedAttribute", type=Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute37: BinaryAssociation = BinaryAssociation(
    name="attribute37",
    ends={
        Property(name="Dictionary", type=art_instance_DictionaryValuedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_DictionaryValuedAttribute38", type=Dictionary, multiplicity=Multiplicity(1, 1))
    }
)
key39: BinaryAssociation = BinaryAssociation(
    name="key39",
    ends={
        Property(name="DictionaryDefaultValue", type=art_instance_DefaultEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="art_instance_DefaultEntry", type=DictionaryDefaultValue, multiplicity=Multiplicity(1, 1))
    }
)
port40: BinaryAssociation = BinaryAssociation(
    name="port40",
    ends={
        Property(name="AbstractPort41", type=art_type_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_ComponentType", type=AbstractPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute42: BinaryAssociation = BinaryAssociation(
    name="attribute42",
    ends={
        Property(name="Attribute", type=art_type_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_ComponentType43", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups44: BinaryAssociation = BinaryAssociation(
    name="groups44",
    ends={
        Property(name="group45", type=art_type_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGroup", type=TypeGroup, multiplicity=Multiplicity(0, 9999))
    }
)
implem46: BinaryAssociation = BinaryAssociation(
    name="implem46",
    ends={
        Property(name="TypeImplementation", type=art_type_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_ComponentType47", type=TypeImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation48: BinaryAssociation = BinaryAssociation(
    name="operation48",
    ends={
        Property(name="Operation", type=art_type_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_Service", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input49: BinaryAssociation = BinaryAssociation(
    name="input49",
    ends={
        Property(name="Parameter", type=art_type_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output50: BinaryAssociation = BinaryAssociation(
    name="output50",
    ends={
        Property(name="Parameter52", type=art_type_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_Operation51", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ids55: BinaryAssociation = BinaryAssociation(
    name="ids55",
    ends={
        Property(name="PortId", type=art_type_PortCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_PortCollection", type=PortId, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
valueType56: BinaryAssociation = BinaryAssociation(
    name="valueType56",
    ends={
        Property(name="type_art_DataType", type=art_type_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_Dictionary", type=type_art_DataType, multiplicity=Multiplicity(1, 1))
    }
)
keys57: BinaryAssociation = BinaryAssociation(
    name="keys57",
    ends={
        Property(name="DictionaryDefaultValue59", type=art_type_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="art_type_Dictionary58", type=DictionaryDefaultValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types60: BinaryAssociation = BinaryAssociation(
    name="types60",
    ends={
        Property(name="type", type=art_group_TypeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentType61", type=ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
subGroups62: BinaryAssociation = BinaryAssociation(
    name="subGroups62",
    ends={
        Property(name="TypeGroup63", type=art_group_TypeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="art_group_TypeGroup", type=TypeGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances64: BinaryAssociation = BinaryAssociation(
    name="instances64",
    ends={
        Property(name="instance66", type=art_group_InstanceGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentInstance65", type=ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
subGroups67: BinaryAssociation = BinaryAssociation(
    name="subGroups67",
    ends={
        Property(name="InstanceGroup68", type=art_group_InstanceGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="art_group_InstanceGroup", type=InstanceGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components69: BinaryAssociation = BinaryAssociation(
    name="components69",
    ends={
        Property(name="ComponentInstance70", type=art_distrib_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="art_distrib_Node", type=ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_art_ModelElement_NamedElement = Generalization(general=NamedElement, specific=art_ModelElement)
gen_art_System_ModelElement = Generalization(general=ModelElement, specific=art_System)
gen_art_DataType_ModelElement = Generalization(general=ModelElement, specific=art_DataType)
gen_art_TypedElement_ModelElement = Generalization(general=ModelElement, specific=art_TypedElement)
gen_art_CardinalityElement_ModelElement = Generalization(general=ModelElement, specific=art_CardinalityElement)
gen_art_instance_ComponentInstance_ModelElement = Generalization(general=ModelElement, specific=art_instance_ComponentInstance)
gen_art_instance_PrimitiveInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=art_instance_PrimitiveInstance)
gen_art_instance_CompositeInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=art_instance_CompositeInstance)
gen_art_instance_TransmissionBinding_Binding = Generalization(general=Binding, specific=art_instance_TransmissionBinding)
gen_art_instance_DelegationBinding_Binding = Generalization(general=Binding, specific=art_instance_DelegationBinding)
gen_art_instance_DictionaryValuedAttribute_AttributeInstance = Generalization(general=AttributeInstance, specific=art_instance_DictionaryValuedAttribute)
gen_art_instance_DefaultEntry_Entry = Generalization(general=Entry, specific=art_instance_DefaultEntry)
gen_art_instance_OtherEntry_Entry = Generalization(general=Entry, specific=art_instance_OtherEntry)
gen_art_type_ComponentType_ModelElement = Generalization(general=ModelElement, specific=art_type_ComponentType)
gen_art_type_PrimitiveType_ComponentType = Generalization(general=ComponentType, specific=art_type_PrimitiveType)
gen_art_type_CompositeType_ComponentType = Generalization(general=ComponentType, specific=art_type_CompositeType)
gen_art_type_Service_ModelElement = Generalization(general=ModelElement, specific=art_type_Service)
gen_art_type_Operation_ModelElement = Generalization(general=ModelElement, specific=art_type_Operation)
gen_art_type_Parameter_TypedElement = Generalization(general=TypedElement, specific=art_type_Parameter)
gen_art_type_FunctionalService_Service = Generalization(general=Service, specific=art_type_FunctionalService)
gen_art_instance_ValuedAttribute_AttributeInstance = Generalization(general=AttributeInstance, specific=art_instance_ValuedAttribute)
gen_art_type_ControlService_Service = Generalization(general=Service, specific=art_type_ControlService)
gen_art_type_AbstractPort_NamedElement = Generalization(general=NamedElement, specific=art_type_AbstractPort)
gen_art_group_TypeGroup_Group = Generalization(general=Group, specific=art_group_TypeGroup)
gen_art_type_Port_CardinalityElement = Generalization(general=CardinalityElement, specific=art_type_Port)
gen_art_type_Port_type_AbstractPort = Generalization(general=type_AbstractPort, specific=art_type_Port)
gen_art_type_PortCollection_AbstractPort = Generalization(general=AbstractPort, specific=art_type_PortCollection)
gen_art_type_PortId_NamedElement = Generalization(general=NamedElement, specific=art_type_PortId)
gen_art_type_Attribute_TypedElement = Generalization(general=TypedElement, specific=art_type_Attribute)
gen_art_type_BasicAttribute_Attribute = Generalization(general=Attribute, specific=art_type_BasicAttribute)
gen_art_type_Dictionary_Attribute = Generalization(general=Attribute, specific=art_type_Dictionary)
gen_art_implem_FractalComponent_ComponentImplementation = Generalization(general=ComponentImplementation, specific=art_implem_FractalComponent)
gen_art_implem_OSGiComponent_ComponentImplementation = Generalization(general=ComponentImplementation, specific=art_implem_OSGiComponent)
gen_art_implem_OSGiType_TypeImplementation = Generalization(general=TypeImplementation, specific=art_implem_OSGiType)
gen_art_group_Group_NamedElement = Generalization(general=NamedElement, specific=art_group_Group)
gen_art_group_InstanceGroup_Group = Generalization(general=Group, specific=art_group_InstanceGroup)
gen_art_distrib_Node_NamedElement = Generalization(general=NamedElement, specific=art_distrib_Node)

# Domain Model
domain_model = DomainModel(
    name="art",
    types={art_NamedElement, art_ModelElement, NamedElement, art_System, ModelElement, Node, Service, ComponentType, art_DataType, Group, art_TypedElement, art_CardinalityElement, art_instance_ComponentInstance, CompositeInstance, AttributeInstance, TransmissionBinding, ComponentImplementation, InstanceGroup, art_instance_PrimitiveInstance, ComponentInstance, art_instance_CompositeInstance, DelegationBinding, art_instance_Binding, art_instance_TransmissionBinding, Binding, AbstractPort, art_instance_DelegationBinding, art_instance_AttributeInstance, art_instance_DictionaryValuedAttribute, Entry, Dictionary, art_instance_Entry, art_instance_DefaultEntry, DictionaryDefaultValue, art_instance_OtherEntry, art_type_ComponentType, Attribute, TypeGroup, TypeImplementation, art_type_PrimitiveType, art_type_CompositeType, art_type_Service, Operation, art_type_Operation, Parameter_, art_type_Parameter, TypedElement, art_type_FunctionalService, art_instance_ValuedAttribute, art_type_ControlService, art_type_AbstractPort, BasicAttribute, art_group_TypeGroup, art_type_Port, CardinalityElement, type_AbstractPort, art_type_PortCollection, PortId, art_type_PortId, art_type_Attribute, art_type_BasicAttribute, art_type_Dictionary, type_art_DataType, art_type_DictionaryDefaultValue, art_implem_ComponentImplementation, art_implem_FractalComponent, art_implem_OSGiComponent, art_implem_TypeImplementation, art_implem_OSGiType, art_group_Group, art_group_InstanceGroup, art_distrib_Node, InstanceState, PortRole},
    associations={type11, nodes0, services1, types3, dataTypes5, groups7, type9, superComponent13, attribute14, binding16, implem18, groups20, subComponent21, delegation23, serverInstance24, client26, server27, source30, exported32, attribute35, service53, entries36, attribute37, key39, port40, attribute42, groups44, implem46, operation48, input49, output50, ids55, valueType56, keys57, types60, subGroups62, instances64, subGroups67, components69},
    generalizations={gen_art_ModelElement_NamedElement, gen_art_System_ModelElement, gen_art_DataType_ModelElement, gen_art_TypedElement_ModelElement, gen_art_CardinalityElement_ModelElement, gen_art_instance_ComponentInstance_ModelElement, gen_art_instance_PrimitiveInstance_ComponentInstance, gen_art_instance_CompositeInstance_ComponentInstance, gen_art_instance_TransmissionBinding_Binding, gen_art_instance_DelegationBinding_Binding, gen_art_instance_DictionaryValuedAttribute_AttributeInstance, gen_art_instance_DefaultEntry_Entry, gen_art_instance_OtherEntry_Entry, gen_art_type_ComponentType_ModelElement, gen_art_type_PrimitiveType_ComponentType, gen_art_type_CompositeType_ComponentType, gen_art_type_Service_ModelElement, gen_art_type_Operation_ModelElement, gen_art_type_Parameter_TypedElement, gen_art_type_FunctionalService_Service, gen_art_instance_ValuedAttribute_AttributeInstance, gen_art_type_ControlService_Service, gen_art_type_AbstractPort_NamedElement, gen_art_group_TypeGroup_Group, gen_art_type_Port_CardinalityElement, gen_art_type_Port_type_AbstractPort, gen_art_type_PortCollection_AbstractPort, gen_art_type_PortId_NamedElement, gen_art_type_Attribute_TypedElement, gen_art_type_BasicAttribute_Attribute, gen_art_type_Dictionary_Attribute, gen_art_implem_FractalComponent_ComponentImplementation, gen_art_implem_OSGiComponent_ComponentImplementation, gen_art_implem_OSGiType_TypeImplementation, gen_art_group_Group_NamedElement, gen_art_group_InstanceGroup_Group, gen_art_distrib_Node_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)