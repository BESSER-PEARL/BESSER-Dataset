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
art_relaxed_ModelElement = Class(name="art_relaxed_ModelElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
art_relaxed_System = Class(name="art_relaxed_System")
ModelElement = Class(name="ModelElement")
Node = Class(name="Node")
Service = Class(name="Service")
ComponentType = Class(name="ComponentType")
art_relaxed_DataType = Class(name="art_relaxed_DataType")
Group = Class(name="Group")
art_relaxed_TypedElement = Class(name="art_relaxed_TypedElement", is_abstract=True)
art_relaxed_CardinalityElement = Class(name="art_relaxed_CardinalityElement", is_abstract=True)
art_relaxed_AspectModelElement = Class(name="art_relaxed_AspectModelElement", is_abstract=True)
art_relaxed_instance_relaxed_ComponentInstance = Class(name="art_relaxed_instance_relaxed_ComponentInstance", is_abstract=True)
CompositeInstance = Class(name="CompositeInstance")
art_relaxed_NamedElement = Class(name="art_relaxed_NamedElement", is_abstract=True)
AspectModelElement = Class(name="AspectModelElement")
DelegationBinding = Class(name="DelegationBinding")
art_relaxed_instance_relaxed_Binding = Class(name="art_relaxed_instance_relaxed_Binding", is_abstract=True)
art_relaxed_instance_relaxed_TransmissionBinding = Class(name="art_relaxed_instance_relaxed_TransmissionBinding")
Binding = Class(name="Binding")
AbstractPort = Class(name="AbstractPort")
art_relaxed_instance_relaxed_DelegationBinding = Class(name="art_relaxed_instance_relaxed_DelegationBinding")
art_relaxed_instance_relaxed_AttributeInstance = Class(name="art_relaxed_instance_relaxed_AttributeInstance", is_abstract=True)
art_relaxed_instance_relaxed_ValuedAttribute = Class(name="art_relaxed_instance_relaxed_ValuedAttribute")
BasicAttribute = Class(name="BasicAttribute")
art_relaxed_instance_relaxed_DictionaryValuedAttribute = Class(name="art_relaxed_instance_relaxed_DictionaryValuedAttribute")
Entry = Class(name="Entry")
Dictionary = Class(name="Dictionary")
AttributeInstance = Class(name="AttributeInstance")
TransmissionBinding = Class(name="TransmissionBinding")
ComponentImplementation = Class(name="ComponentImplementation")
InstanceGroup = Class(name="InstanceGroup")
art_relaxed_instance_relaxed_PrimitiveInstance = Class(name="art_relaxed_instance_relaxed_PrimitiveInstance")
ComponentInstance = Class(name="ComponentInstance")
art_relaxed_instance_relaxed_CompositeInstance = Class(name="art_relaxed_instance_relaxed_CompositeInstance")
Attribute = Class(name="Attribute")
TypeGroup = Class(name="TypeGroup")
TypeImplementation = Class(name="TypeImplementation")
art_relaxed_type_relaxed_PrimitiveType = Class(name="art_relaxed_type_relaxed_PrimitiveType")
art_relaxed_type_relaxed_CompositeType = Class(name="art_relaxed_type_relaxed_CompositeType")
art_relaxed_type_relaxed_Service = Class(name="art_relaxed_type_relaxed_Service", is_abstract=True)
Operation = Class(name="Operation")
art_relaxed_type_relaxed_Operation = Class(name="art_relaxed_type_relaxed_Operation")
Parameter_ = Class(name="Parameter")
art_relaxed_type_relaxed_Parameter = Class(name="art_relaxed_type_relaxed_Parameter")
TypedElement = Class(name="TypedElement")
art_relaxed_type_relaxed_FunctionalService = Class(name="art_relaxed_type_relaxed_FunctionalService")
art_relaxed_type_relaxed_ControlService = Class(name="art_relaxed_type_relaxed_ControlService")
art_relaxed_type_relaxed_AbstractPort = Class(name="art_relaxed_type_relaxed_AbstractPort", is_abstract=True)
art_relaxed_type_relaxed_Port = Class(name="art_relaxed_type_relaxed_Port")
CardinalityElement = Class(name="CardinalityElement")
type_relaxed_AbstractPort = Class(name="type_relaxed_AbstractPort")
art_relaxed_type_relaxed_PortCollection = Class(name="art_relaxed_type_relaxed_PortCollection")
PortId = Class(name="PortId")
art_relaxed_type_relaxed_PortId = Class(name="art_relaxed_type_relaxed_PortId")
art_relaxed_instance_relaxed_Entry = Class(name="art_relaxed_instance_relaxed_Entry", is_abstract=True)
art_relaxed_instance_relaxed_DefaultEntry = Class(name="art_relaxed_instance_relaxed_DefaultEntry")
DictionaryDefaultValue = Class(name="DictionaryDefaultValue")
art_relaxed_instance_relaxed_OtherEntry = Class(name="art_relaxed_instance_relaxed_OtherEntry")
art_relaxed_type_relaxed_ComponentType = Class(name="art_relaxed_type_relaxed_ComponentType", is_abstract=True)
art_relaxed_implem_relaxed_ComponentImplementation = Class(name="art_relaxed_implem_relaxed_ComponentImplementation", is_abstract=True)
art_relaxed_implem_relaxed_FractalComponent = Class(name="art_relaxed_implem_relaxed_FractalComponent")
art_relaxed_implem_relaxed_OSGiComponent = Class(name="art_relaxed_implem_relaxed_OSGiComponent")
art_relaxed_implem_relaxed_TypeImplementation = Class(name="art_relaxed_implem_relaxed_TypeImplementation", is_abstract=True)
art_relaxed_implem_relaxed_OSGiType = Class(name="art_relaxed_implem_relaxed_OSGiType")
art_relaxed_group_relaxed_Group = Class(name="art_relaxed_group_relaxed_Group", is_abstract=True)
art_relaxed_group_relaxed_TypeGroup = Class(name="art_relaxed_group_relaxed_TypeGroup")
art_relaxed_group_relaxed_InstanceGroup = Class(name="art_relaxed_group_relaxed_InstanceGroup")
art_relaxed_distrib_relaxed_Node = Class(name="art_relaxed_distrib_relaxed_Node")
art_relaxed_type_relaxed_Attribute = Class(name="art_relaxed_type_relaxed_Attribute", is_abstract=True)
art_relaxed_type_relaxed_BasicAttribute = Class(name="art_relaxed_type_relaxed_BasicAttribute")
art_relaxed_type_relaxed_Dictionary = Class(name="art_relaxed_type_relaxed_Dictionary")
type_relaxed_art_relaxed_DataType = Class(name="type_relaxed_art_relaxed_DataType")
art_relaxed_type_relaxed_DictionaryDefaultValue = Class(name="art_relaxed_type_relaxed_DictionaryDefaultValue")

# art_relaxed_ModelElement class attributes and methods

# NamedElement class attributes and methods

# art_relaxed_System class attributes and methods

# ModelElement class attributes and methods

# Node class attributes and methods

# Service class attributes and methods

# ComponentType class attributes and methods

# art_relaxed_DataType class attributes and methods

# Group class attributes and methods

# art_relaxed_TypedElement class attributes and methods

# art_relaxed_CardinalityElement class attributes and methods
art_relaxed_CardinalityElement_lower: Property = Property(name="lower", type=StringType)
art_relaxed_CardinalityElement_upper: Property = Property(name="upper", type=StringType)
art_relaxed_CardinalityElement.attributes={art_relaxed_CardinalityElement_upper, art_relaxed_CardinalityElement_lower}

# art_relaxed_AspectModelElement class attributes and methods
art_relaxed_AspectModelElement_pid: Property = Property(name="pid", type=StringType)
art_relaxed_AspectModelElement.attributes={art_relaxed_AspectModelElement_pid}

# art_relaxed_instance_relaxed_ComponentInstance class attributes and methods
art_relaxed_instance_relaxed_ComponentInstance_state: Property = Property(name="state", type=StringType)
art_relaxed_instance_relaxed_ComponentInstance.attributes={art_relaxed_instance_relaxed_ComponentInstance_state}

# CompositeInstance class attributes and methods

# art_relaxed_NamedElement class attributes and methods
art_relaxed_NamedElement_name: Property = Property(name="name", type=StringType)
art_relaxed_NamedElement.attributes={art_relaxed_NamedElement_name}

# AspectModelElement class attributes and methods

# DelegationBinding class attributes and methods

# art_relaxed_instance_relaxed_Binding class attributes and methods
art_relaxed_instance_relaxed_Binding_id: Property = Property(name="id", type=StringType)
art_relaxed_instance_relaxed_Binding.attributes={art_relaxed_instance_relaxed_Binding_id}

# art_relaxed_instance_relaxed_TransmissionBinding class attributes and methods

# Binding class attributes and methods

# AbstractPort class attributes and methods

# art_relaxed_instance_relaxed_DelegationBinding class attributes and methods

# art_relaxed_instance_relaxed_AttributeInstance class attributes and methods

# art_relaxed_instance_relaxed_ValuedAttribute class attributes and methods
art_relaxed_instance_relaxed_ValuedAttribute_value: Property = Property(name="value", type=StringType)
art_relaxed_instance_relaxed_ValuedAttribute.attributes={art_relaxed_instance_relaxed_ValuedAttribute_value}

# BasicAttribute class attributes and methods

# art_relaxed_instance_relaxed_DictionaryValuedAttribute class attributes and methods

# Entry class attributes and methods

# Dictionary class attributes and methods

# AttributeInstance class attributes and methods

# TransmissionBinding class attributes and methods

# ComponentImplementation class attributes and methods

# InstanceGroup class attributes and methods

# art_relaxed_instance_relaxed_PrimitiveInstance class attributes and methods

# ComponentInstance class attributes and methods

# art_relaxed_instance_relaxed_CompositeInstance class attributes and methods

# Attribute class attributes and methods

# TypeGroup class attributes and methods

# TypeImplementation class attributes and methods

# art_relaxed_type_relaxed_PrimitiveType class attributes and methods

# art_relaxed_type_relaxed_CompositeType class attributes and methods

# art_relaxed_type_relaxed_Service class attributes and methods

# Operation class attributes and methods

# art_relaxed_type_relaxed_Operation class attributes and methods

# Parameter class attributes and methods

# art_relaxed_type_relaxed_Parameter class attributes and methods

# TypedElement class attributes and methods

# art_relaxed_type_relaxed_FunctionalService class attributes and methods

# art_relaxed_type_relaxed_ControlService class attributes and methods

# art_relaxed_type_relaxed_AbstractPort class attributes and methods
art_relaxed_type_relaxed_AbstractPort_role: Property = Property(name="role", type=StringType)
art_relaxed_type_relaxed_AbstractPort_protocol: Property = Property(name="protocol", type=StringType)
art_relaxed_type_relaxed_AbstractPort_uri: Property = Property(name="uri", type=StringType)
art_relaxed_type_relaxed_AbstractPort.attributes={art_relaxed_type_relaxed_AbstractPort_protocol, art_relaxed_type_relaxed_AbstractPort_uri, art_relaxed_type_relaxed_AbstractPort_role}

# art_relaxed_type_relaxed_Port class attributes and methods

# CardinalityElement class attributes and methods

# type_relaxed_AbstractPort class attributes and methods

# art_relaxed_type_relaxed_PortCollection class attributes and methods

# PortId class attributes and methods

# art_relaxed_type_relaxed_PortId class attributes and methods

# art_relaxed_instance_relaxed_Entry class attributes and methods
art_relaxed_instance_relaxed_Entry_value: Property = Property(name="value", type=StringType)
art_relaxed_instance_relaxed_Entry.attributes={art_relaxed_instance_relaxed_Entry_value}

# art_relaxed_instance_relaxed_DefaultEntry class attributes and methods

# DictionaryDefaultValue class attributes and methods

# art_relaxed_instance_relaxed_OtherEntry class attributes and methods
art_relaxed_instance_relaxed_OtherEntry_key: Property = Property(name="key", type=StringType)
art_relaxed_instance_relaxed_OtherEntry.attributes={art_relaxed_instance_relaxed_OtherEntry_key}

# art_relaxed_type_relaxed_ComponentType class attributes and methods

# art_relaxed_implem_relaxed_ComponentImplementation class attributes and methods

# art_relaxed_implem_relaxed_FractalComponent class attributes and methods
art_relaxed_implem_relaxed_FractalComponent_controllerDesc: Property = Property(name="controllerDesc", type=StringType)
art_relaxed_implem_relaxed_FractalComponent_contentDesc: Property = Property(name="contentDesc", type=StringType)
art_relaxed_implem_relaxed_FractalComponent.attributes={art_relaxed_implem_relaxed_FractalComponent_contentDesc, art_relaxed_implem_relaxed_FractalComponent_controllerDesc}

# art_relaxed_implem_relaxed_OSGiComponent class attributes and methods
art_relaxed_implem_relaxed_OSGiComponent_implementingClass: Property = Property(name="implementingClass", type=StringType)
art_relaxed_implem_relaxed_OSGiComponent.attributes={art_relaxed_implem_relaxed_OSGiComponent_implementingClass}

# art_relaxed_implem_relaxed_TypeImplementation class attributes and methods

# art_relaxed_implem_relaxed_OSGiType class attributes and methods
art_relaxed_implem_relaxed_OSGiType_generateInstanceBundle: Property = Property(name="generateInstanceBundle", type=StringType)
art_relaxed_implem_relaxed_OSGiType.attributes={art_relaxed_implem_relaxed_OSGiType_generateInstanceBundle}

# art_relaxed_group_relaxed_Group class attributes and methods

# art_relaxed_group_relaxed_TypeGroup class attributes and methods

# art_relaxed_group_relaxed_InstanceGroup class attributes and methods

# art_relaxed_distrib_relaxed_Node class attributes and methods
art_relaxed_distrib_relaxed_Node_uri: Property = Property(name="uri", type=StringType)
art_relaxed_distrib_relaxed_Node.attributes={art_relaxed_distrib_relaxed_Node_uri}

# art_relaxed_type_relaxed_Attribute class attributes and methods

# art_relaxed_type_relaxed_BasicAttribute class attributes and methods
art_relaxed_type_relaxed_BasicAttribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
art_relaxed_type_relaxed_BasicAttribute.attributes={art_relaxed_type_relaxed_BasicAttribute_defaultValue}

# art_relaxed_type_relaxed_Dictionary class attributes and methods

# type_relaxed_art_relaxed_DataType class attributes and methods

# art_relaxed_type_relaxed_DictionaryDefaultValue class attributes and methods
art_relaxed_type_relaxed_DictionaryDefaultValue_key: Property = Property(name="key", type=StringType)
art_relaxed_type_relaxed_DictionaryDefaultValue_value: Property = Property(name="value", type=StringType)
art_relaxed_type_relaxed_DictionaryDefaultValue.attributes={art_relaxed_type_relaxed_DictionaryDefaultValue_value, art_relaxed_type_relaxed_DictionaryDefaultValue_key}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=art_relaxed_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_System", type=Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services1: BinaryAssociation = BinaryAssociation(
    name="services1",
    ends={
        Property(name="Service", type=art_relaxed_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_System2", type=Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types3: BinaryAssociation = BinaryAssociation(
    name="types3",
    ends={
        Property(name="ComponentType", type=art_relaxed_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_System4", type=ComponentType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes5: BinaryAssociation = BinaryAssociation(
    name="dataTypes5",
    ends={
        Property(name="art_relaxed_DataType", type=art_relaxed_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_System6", type=art_relaxed_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups7: BinaryAssociation = BinaryAssociation(
    name="groups7",
    ends={
        Property(name="Group", type=art_relaxed_System, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_System8", type=Group, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="art_relaxed_DataType10", type=art_relaxed_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_TypedElement", type=art_relaxed_DataType, multiplicity=Multiplicity(1, 1))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="ComponentType12", type=art_relaxed_instance_relaxed_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_ComponentInstance", type=ComponentType, multiplicity=Multiplicity(1, 1))
    }
)
superComponent13: BinaryAssociation = BinaryAssociation(
    name="superComponent13",
    ends={
        Property(name="CompositeInstance", type=art_relaxed_instance_relaxed_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="subComponent", type=CompositeInstance, multiplicity=Multiplicity(0, 1))
    }
)
subComponent21: BinaryAssociation = BinaryAssociation(
    name="subComponent21",
    ends={
        Property(name="ComponentInstance", type=art_relaxed_instance_relaxed_CompositeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="superComponent", type=ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegation22: BinaryAssociation = BinaryAssociation(
    name="delegation22",
    ends={
        Property(name="DelegationBinding", type=art_relaxed_instance_relaxed_CompositeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_CompositeInstance", type=DelegationBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serverInstance23: BinaryAssociation = BinaryAssociation(
    name="serverInstance23",
    ends={
        Property(name="ComponentInstance24", type=art_relaxed_instance_relaxed_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_Binding", type=ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
client25: BinaryAssociation = BinaryAssociation(
    name="client25",
    ends={
        Property(name="AbstractPort", type=art_relaxed_instance_relaxed_TransmissionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_TransmissionBinding", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
server26: BinaryAssociation = BinaryAssociation(
    name="server26",
    ends={
        Property(name="AbstractPort28", type=art_relaxed_instance_relaxed_TransmissionBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_TransmissionBinding27", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="AbstractPort30", type=art_relaxed_instance_relaxed_DelegationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_DelegationBinding", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
exported31: BinaryAssociation = BinaryAssociation(
    name="exported31",
    ends={
        Property(name="AbstractPort33", type=art_relaxed_instance_relaxed_DelegationBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_DelegationBinding32", type=AbstractPort, multiplicity=Multiplicity(1, 1))
    }
)
attribute34: BinaryAssociation = BinaryAssociation(
    name="attribute34",
    ends={
        Property(name="BasicAttribute", type=art_relaxed_instance_relaxed_ValuedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_ValuedAttribute", type=BasicAttribute, multiplicity=Multiplicity(1, 1))
    }
)
entries35: BinaryAssociation = BinaryAssociation(
    name="entries35",
    ends={
        Property(name="Entry", type=art_relaxed_instance_relaxed_DictionaryValuedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_DictionaryValuedAttribute", type=Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute36: BinaryAssociation = BinaryAssociation(
    name="attribute36",
    ends={
        Property(name="Dictionary", type=art_relaxed_instance_relaxed_DictionaryValuedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_DictionaryValuedAttribute37", type=Dictionary, multiplicity=Multiplicity(1, 1))
    }
)
attribute14: BinaryAssociation = BinaryAssociation(
    name="attribute14",
    ends={
        Property(name="AttributeInstance", type=art_relaxed_instance_relaxed_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_ComponentInstance15", type=AttributeInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
binding16: BinaryAssociation = BinaryAssociation(
    name="binding16",
    ends={
        Property(name="TransmissionBinding", type=art_relaxed_instance_relaxed_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_ComponentInstance17", type=TransmissionBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implem18: BinaryAssociation = BinaryAssociation(
    name="implem18",
    ends={
        Property(name="ComponentImplementation", type=art_relaxed_instance_relaxed_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_ComponentInstance19", type=ComponentImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groups20: BinaryAssociation = BinaryAssociation(
    name="groups20",
    ends={
        Property(name="InstanceGroup", type=art_relaxed_instance_relaxed_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=InstanceGroup, multiplicity=Multiplicity(0, 9999))
    }
)
port39: BinaryAssociation = BinaryAssociation(
    name="port39",
    ends={
        Property(name="AbstractPort40", type=art_relaxed_type_relaxed_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_ComponentType", type=AbstractPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute41: BinaryAssociation = BinaryAssociation(
    name="attribute41",
    ends={
        Property(name="Attribute", type=art_relaxed_type_relaxed_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_ComponentType42", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups43: BinaryAssociation = BinaryAssociation(
    name="groups43",
    ends={
        Property(name="TypeGroup", type=art_relaxed_type_relaxed_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=TypeGroup, multiplicity=Multiplicity(0, 9999))
    }
)
implem44: BinaryAssociation = BinaryAssociation(
    name="implem44",
    ends={
        Property(name="TypeImplementation", type=art_relaxed_type_relaxed_ComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_ComponentType45", type=TypeImplementation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation46: BinaryAssociation = BinaryAssociation(
    name="operation46",
    ends={
        Property(name="Operation", type=art_relaxed_type_relaxed_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_Service", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input47: BinaryAssociation = BinaryAssociation(
    name="input47",
    ends={
        Property(name="Parameter", type=art_relaxed_type_relaxed_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_Operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output48: BinaryAssociation = BinaryAssociation(
    name="output48",
    ends={
        Property(name="Parameter50", type=art_relaxed_type_relaxed_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_Operation49", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
service51: BinaryAssociation = BinaryAssociation(
    name="service51",
    ends={
        Property(name="Service52", type=art_relaxed_type_relaxed_AbstractPort, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_AbstractPort", type=Service, multiplicity=Multiplicity(1, 1))
    }
)
ids53: BinaryAssociation = BinaryAssociation(
    name="ids53",
    ends={
        Property(name="PortId", type=art_relaxed_type_relaxed_PortCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_PortCollection", type=PortId, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
key38: BinaryAssociation = BinaryAssociation(
    name="key38",
    ends={
        Property(name="DictionaryDefaultValue", type=art_relaxed_instance_relaxed_DefaultEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_instance_relaxed_DefaultEntry", type=DictionaryDefaultValue, multiplicity=Multiplicity(1, 1))
    }
)
types58: BinaryAssociation = BinaryAssociation(
    name="types58",
    ends={
        Property(name="ComponentType59", type=art_relaxed_group_relaxed_TypeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=ComponentType, multiplicity=Multiplicity(0, 9999))
    }
)
subGroups60: BinaryAssociation = BinaryAssociation(
    name="subGroups60",
    ends={
        Property(name="TypeGroup61", type=art_relaxed_group_relaxed_TypeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_group_relaxed_TypeGroup", type=TypeGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances62: BinaryAssociation = BinaryAssociation(
    name="instances62",
    ends={
        Property(name="ComponentInstance64", type=art_relaxed_group_relaxed_InstanceGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="groups63", type=ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
subGroups65: BinaryAssociation = BinaryAssociation(
    name="subGroups65",
    ends={
        Property(name="InstanceGroup66", type=art_relaxed_group_relaxed_InstanceGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_group_relaxed_InstanceGroup", type=InstanceGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components67: BinaryAssociation = BinaryAssociation(
    name="components67",
    ends={
        Property(name="ComponentInstance68", type=art_relaxed_distrib_relaxed_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_distrib_relaxed_Node", type=ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueType54: BinaryAssociation = BinaryAssociation(
    name="valueType54",
    ends={
        Property(name="type_relaxed_art_relaxed_DataType", type=art_relaxed_type_relaxed_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_Dictionary", type=type_relaxed_art_relaxed_DataType, multiplicity=Multiplicity(1, 1))
    }
)
keys55: BinaryAssociation = BinaryAssociation(
    name="keys55",
    ends={
        Property(name="DictionaryDefaultValue57", type=art_relaxed_type_relaxed_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="art_relaxed_type_relaxed_Dictionary56", type=DictionaryDefaultValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_art_relaxed_ModelElement_NamedElement = Generalization(general=NamedElement, specific=art_relaxed_ModelElement)
gen_art_relaxed_System_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_System)
gen_art_relaxed_DataType_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_DataType)
gen_art_relaxed_TypedElement_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_TypedElement)
gen_art_relaxed_CardinalityElement_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_CardinalityElement)
gen_art_relaxed_instance_relaxed_ComponentInstance_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_instance_relaxed_ComponentInstance)
gen_art_relaxed_NamedElement_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_NamedElement)
gen_art_relaxed_instance_relaxed_Binding_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_instance_relaxed_Binding)
gen_art_relaxed_instance_relaxed_TransmissionBinding_Binding = Generalization(general=Binding, specific=art_relaxed_instance_relaxed_TransmissionBinding)
gen_art_relaxed_instance_relaxed_DelegationBinding_Binding = Generalization(general=Binding, specific=art_relaxed_instance_relaxed_DelegationBinding)
gen_art_relaxed_instance_relaxed_AttributeInstance_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_instance_relaxed_AttributeInstance)
gen_art_relaxed_instance_relaxed_ValuedAttribute_AttributeInstance = Generalization(general=AttributeInstance, specific=art_relaxed_instance_relaxed_ValuedAttribute)
gen_art_relaxed_instance_relaxed_DictionaryValuedAttribute_AttributeInstance = Generalization(general=AttributeInstance, specific=art_relaxed_instance_relaxed_DictionaryValuedAttribute)
gen_art_relaxed_instance_relaxed_PrimitiveInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=art_relaxed_instance_relaxed_PrimitiveInstance)
gen_art_relaxed_instance_relaxed_CompositeInstance_ComponentInstance = Generalization(general=ComponentInstance, specific=art_relaxed_instance_relaxed_CompositeInstance)
gen_art_relaxed_type_relaxed_PrimitiveType_ComponentType = Generalization(general=ComponentType, specific=art_relaxed_type_relaxed_PrimitiveType)
gen_art_relaxed_type_relaxed_CompositeType_ComponentType = Generalization(general=ComponentType, specific=art_relaxed_type_relaxed_CompositeType)
gen_art_relaxed_type_relaxed_Service_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_type_relaxed_Service)
gen_art_relaxed_type_relaxed_Operation_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_type_relaxed_Operation)
gen_art_relaxed_type_relaxed_Parameter_TypedElement = Generalization(general=TypedElement, specific=art_relaxed_type_relaxed_Parameter)
gen_art_relaxed_type_relaxed_FunctionalService_Service = Generalization(general=Service, specific=art_relaxed_type_relaxed_FunctionalService)
gen_art_relaxed_type_relaxed_ControlService_Service = Generalization(general=Service, specific=art_relaxed_type_relaxed_ControlService)
gen_art_relaxed_type_relaxed_AbstractPort_NamedElement = Generalization(general=NamedElement, specific=art_relaxed_type_relaxed_AbstractPort)
gen_art_relaxed_type_relaxed_Port_CardinalityElement = Generalization(general=CardinalityElement, specific=art_relaxed_type_relaxed_Port)
gen_art_relaxed_type_relaxed_Port_type_relaxed_AbstractPort = Generalization(general=type_relaxed_AbstractPort, specific=art_relaxed_type_relaxed_Port)
gen_art_relaxed_type_relaxed_PortCollection_AbstractPort = Generalization(general=AbstractPort, specific=art_relaxed_type_relaxed_PortCollection)
gen_art_relaxed_instance_relaxed_Entry_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_instance_relaxed_Entry)
gen_art_relaxed_instance_relaxed_DefaultEntry_Entry = Generalization(general=Entry, specific=art_relaxed_instance_relaxed_DefaultEntry)
gen_art_relaxed_instance_relaxed_OtherEntry_Entry = Generalization(general=Entry, specific=art_relaxed_instance_relaxed_OtherEntry)
gen_art_relaxed_type_relaxed_ComponentType_ModelElement = Generalization(general=ModelElement, specific=art_relaxed_type_relaxed_ComponentType)
gen_art_relaxed_implem_relaxed_ComponentImplementation_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_implem_relaxed_ComponentImplementation)
gen_art_relaxed_implem_relaxed_FractalComponent_ComponentImplementation = Generalization(general=ComponentImplementation, specific=art_relaxed_implem_relaxed_FractalComponent)
gen_art_relaxed_implem_relaxed_OSGiComponent_ComponentImplementation = Generalization(general=ComponentImplementation, specific=art_relaxed_implem_relaxed_OSGiComponent)
gen_art_relaxed_implem_relaxed_TypeImplementation_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_implem_relaxed_TypeImplementation)
gen_art_relaxed_implem_relaxed_OSGiType_TypeImplementation = Generalization(general=TypeImplementation, specific=art_relaxed_implem_relaxed_OSGiType)
gen_art_relaxed_group_relaxed_Group_NamedElement = Generalization(general=NamedElement, specific=art_relaxed_group_relaxed_Group)
gen_art_relaxed_group_relaxed_TypeGroup_Group = Generalization(general=Group, specific=art_relaxed_group_relaxed_TypeGroup)
gen_art_relaxed_group_relaxed_InstanceGroup_Group = Generalization(general=Group, specific=art_relaxed_group_relaxed_InstanceGroup)
gen_art_relaxed_distrib_relaxed_Node_NamedElement = Generalization(general=NamedElement, specific=art_relaxed_distrib_relaxed_Node)
gen_art_relaxed_type_relaxed_PortId_NamedElement = Generalization(general=NamedElement, specific=art_relaxed_type_relaxed_PortId)
gen_art_relaxed_type_relaxed_Attribute_TypedElement = Generalization(general=TypedElement, specific=art_relaxed_type_relaxed_Attribute)
gen_art_relaxed_type_relaxed_BasicAttribute_Attribute = Generalization(general=Attribute, specific=art_relaxed_type_relaxed_BasicAttribute)
gen_art_relaxed_type_relaxed_Dictionary_Attribute = Generalization(general=Attribute, specific=art_relaxed_type_relaxed_Dictionary)
gen_art_relaxed_type_relaxed_DictionaryDefaultValue_AspectModelElement = Generalization(general=AspectModelElement, specific=art_relaxed_type_relaxed_DictionaryDefaultValue)

# Domain Model
domain_model = DomainModel(
    name="art_relaxed",
    types={art_relaxed_ModelElement, NamedElement, art_relaxed_System, ModelElement, Node, Service, ComponentType, art_relaxed_DataType, Group, art_relaxed_TypedElement, art_relaxed_CardinalityElement, art_relaxed_AspectModelElement, art_relaxed_instance_relaxed_ComponentInstance, CompositeInstance, art_relaxed_NamedElement, AspectModelElement, DelegationBinding, art_relaxed_instance_relaxed_Binding, art_relaxed_instance_relaxed_TransmissionBinding, Binding, AbstractPort, art_relaxed_instance_relaxed_DelegationBinding, art_relaxed_instance_relaxed_AttributeInstance, art_relaxed_instance_relaxed_ValuedAttribute, BasicAttribute, art_relaxed_instance_relaxed_DictionaryValuedAttribute, Entry, Dictionary, AttributeInstance, TransmissionBinding, ComponentImplementation, InstanceGroup, art_relaxed_instance_relaxed_PrimitiveInstance, ComponentInstance, art_relaxed_instance_relaxed_CompositeInstance, Attribute, TypeGroup, TypeImplementation, art_relaxed_type_relaxed_PrimitiveType, art_relaxed_type_relaxed_CompositeType, art_relaxed_type_relaxed_Service, Operation, art_relaxed_type_relaxed_Operation, Parameter_, art_relaxed_type_relaxed_Parameter, TypedElement, art_relaxed_type_relaxed_FunctionalService, art_relaxed_type_relaxed_ControlService, art_relaxed_type_relaxed_AbstractPort, art_relaxed_type_relaxed_Port, CardinalityElement, type_relaxed_AbstractPort, art_relaxed_type_relaxed_PortCollection, PortId, art_relaxed_type_relaxed_PortId, art_relaxed_instance_relaxed_Entry, art_relaxed_instance_relaxed_DefaultEntry, DictionaryDefaultValue, art_relaxed_instance_relaxed_OtherEntry, art_relaxed_type_relaxed_ComponentType, art_relaxed_implem_relaxed_ComponentImplementation, art_relaxed_implem_relaxed_FractalComponent, art_relaxed_implem_relaxed_OSGiComponent, art_relaxed_implem_relaxed_TypeImplementation, art_relaxed_implem_relaxed_OSGiType, art_relaxed_group_relaxed_Group, art_relaxed_group_relaxed_TypeGroup, art_relaxed_group_relaxed_InstanceGroup, art_relaxed_distrib_relaxed_Node, art_relaxed_type_relaxed_Attribute, art_relaxed_type_relaxed_BasicAttribute, art_relaxed_type_relaxed_Dictionary, type_relaxed_art_relaxed_DataType, art_relaxed_type_relaxed_DictionaryDefaultValue, InstanceState, PortRole},
    associations={nodes0, services1, types3, dataTypes5, groups7, type9, type11, superComponent13, subComponent21, delegation22, serverInstance23, client25, server26, source29, exported31, attribute34, entries35, attribute36, attribute14, binding16, implem18, groups20, port39, attribute41, groups43, implem44, operation46, input47, output48, service51, ids53, key38, types58, subGroups60, instances62, subGroups65, components67, valueType54, keys55},
    generalizations={gen_art_relaxed_ModelElement_NamedElement, gen_art_relaxed_System_ModelElement, gen_art_relaxed_DataType_ModelElement, gen_art_relaxed_TypedElement_ModelElement, gen_art_relaxed_CardinalityElement_ModelElement, gen_art_relaxed_instance_relaxed_ComponentInstance_ModelElement, gen_art_relaxed_NamedElement_AspectModelElement, gen_art_relaxed_instance_relaxed_Binding_AspectModelElement, gen_art_relaxed_instance_relaxed_TransmissionBinding_Binding, gen_art_relaxed_instance_relaxed_DelegationBinding_Binding, gen_art_relaxed_instance_relaxed_AttributeInstance_AspectModelElement, gen_art_relaxed_instance_relaxed_ValuedAttribute_AttributeInstance, gen_art_relaxed_instance_relaxed_DictionaryValuedAttribute_AttributeInstance, gen_art_relaxed_instance_relaxed_PrimitiveInstance_ComponentInstance, gen_art_relaxed_instance_relaxed_CompositeInstance_ComponentInstance, gen_art_relaxed_type_relaxed_PrimitiveType_ComponentType, gen_art_relaxed_type_relaxed_CompositeType_ComponentType, gen_art_relaxed_type_relaxed_Service_ModelElement, gen_art_relaxed_type_relaxed_Operation_ModelElement, gen_art_relaxed_type_relaxed_Parameter_TypedElement, gen_art_relaxed_type_relaxed_FunctionalService_Service, gen_art_relaxed_type_relaxed_ControlService_Service, gen_art_relaxed_type_relaxed_AbstractPort_NamedElement, gen_art_relaxed_type_relaxed_Port_CardinalityElement, gen_art_relaxed_type_relaxed_Port_type_relaxed_AbstractPort, gen_art_relaxed_type_relaxed_PortCollection_AbstractPort, gen_art_relaxed_instance_relaxed_Entry_AspectModelElement, gen_art_relaxed_instance_relaxed_DefaultEntry_Entry, gen_art_relaxed_instance_relaxed_OtherEntry_Entry, gen_art_relaxed_type_relaxed_ComponentType_ModelElement, gen_art_relaxed_implem_relaxed_ComponentImplementation_AspectModelElement, gen_art_relaxed_implem_relaxed_FractalComponent_ComponentImplementation, gen_art_relaxed_implem_relaxed_OSGiComponent_ComponentImplementation, gen_art_relaxed_implem_relaxed_TypeImplementation_AspectModelElement, gen_art_relaxed_implem_relaxed_OSGiType_TypeImplementation, gen_art_relaxed_group_relaxed_Group_NamedElement, gen_art_relaxed_group_relaxed_TypeGroup_Group, gen_art_relaxed_group_relaxed_InstanceGroup_Group, gen_art_relaxed_distrib_relaxed_Node_NamedElement, gen_art_relaxed_type_relaxed_PortId_NamedElement, gen_art_relaxed_type_relaxed_Attribute_TypedElement, gen_art_relaxed_type_relaxed_BasicAttribute_Attribute, gen_art_relaxed_type_relaxed_Dictionary_Attribute, gen_art_relaxed_type_relaxed_DictionaryDefaultValue_AspectModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)