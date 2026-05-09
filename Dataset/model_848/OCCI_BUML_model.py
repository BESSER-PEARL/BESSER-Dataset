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
NumericTypeEnum: Enumeration = Enumeration(
    name="NumericTypeEnum",
    literals={
            EnumerationLiteral(name="Byte"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Long"),
			EnumerationLiteral(name="Short"),
			EnumerationLiteral(name="BigDecimal")
    }
)

# Classes
occi_Attribute = Class(name="occi_Attribute")
occi_Constraint = Class(name="occi_Constraint")
occi_AnnotatedElement = Class(name="occi_AnnotatedElement", is_abstract=True)
occi_Annotation = Class(name="occi_Annotation")
occi_Category = Class(name="occi_Category", is_abstract=True)
AnnotatedElement = Class(name="AnnotatedElement")
occi_Transition = Class(name="occi_Transition")
occi_Type = Class(name="occi_Type", is_abstract=True)
Category = Class(name="Category")
occi_Action = Class(name="occi_Action")
occi_FSM = Class(name="occi_FSM")
occi_State = Class(name="occi_State")
occi_EnumerationLiteral = Class(name="occi_EnumerationLiteral")
occi_Mixin = Class(name="occi_Mixin")
occi_DataType = Class(name="occi_DataType", is_abstract=True)
occi_Kind = Class(name="occi_Kind")
Type = Class(name="Type")
occi_AttributeState = Class(name="occi_AttributeState")
occi_MixinBase = Class(name="occi_MixinBase")
occi_Entity = Class(name="occi_Entity", is_abstract=True)
occi_Link = Class(name="occi_Link")
occi_Extension = Class(name="occi_Extension")
occi_Resource = Class(name="occi_Resource")
Entity = Class(name="Entity")
occi_BasicType = Class(name="occi_BasicType", is_abstract=True)
DataType = Class(name="DataType")
occi_StringType = Class(name="occi_StringType")
BasicType = Class(name="BasicType")
occi_EObjectType = Class(name="occi_EObjectType")
occi_BooleanType = Class(name="occi_BooleanType")
occi_NumericType = Class(name="occi_NumericType")
occi_EnumerationType = Class(name="occi_EnumerationType")
occi_Configuration = Class(name="occi_Configuration")
Attribute = Class(name="Attribute")
occi_ArrayType = Class(name="occi_ArrayType")
occi_RecordType = Class(name="occi_RecordType")
occi_RecordField = Class(name="occi_RecordField")

# occi_Attribute class attributes and methods
occi_Attribute_name: Property = Property(name="name", type=StringType)
occi_Attribute_mutable: Property = Property(name="mutable", type=StringType)
occi_Attribute_required: Property = Property(name="required", type=StringType)
occi_Attribute_default: Property = Property(name="default", type=StringType)
occi_Attribute_description: Property = Property(name="description", type=StringType)
occi_Attribute.attributes={occi_Attribute_name, occi_Attribute_required, occi_Attribute_default, occi_Attribute_description, occi_Attribute_mutable}

# occi_Constraint class attributes and methods
occi_Constraint_name: Property = Property(name="name", type=StringType)
occi_Constraint_description: Property = Property(name="description", type=StringType)
occi_Constraint_body: Property = Property(name="body", type=StringType)
occi_Constraint.attributes={occi_Constraint_body, occi_Constraint_name, occi_Constraint_description}

# occi_AnnotatedElement class attributes and methods

# occi_Annotation class attributes and methods
occi_Annotation_key: Property = Property(name="key", type=StringType)
occi_Annotation_value: Property = Property(name="value", type=StringType)
occi_Annotation.attributes={occi_Annotation_value, occi_Annotation_key}

# occi_Category class attributes and methods
occi_Category_title: Property = Property(name="title", type=StringType)
occi_Category_description: Property = Property(name="description", type=StringType)
occi_Category_name: Property = Property(name="name", type=StringType)
occi_Category_term: Property = Property(name="term", type=StringType)
occi_Category_scheme: Property = Property(name="scheme", type=StringType)
occi_Category.attributes={occi_Category_term, occi_Category_scheme, occi_Category_title, occi_Category_name, occi_Category_description}

# AnnotatedElement class attributes and methods

# occi_Transition class attributes and methods

# occi_Type class attributes and methods

# Category class attributes and methods

# occi_Action class attributes and methods

# occi_FSM class attributes and methods

# occi_State class attributes and methods
occi_State_initial: Property = Property(name="initial", type=StringType)
occi_State_final: Property = Property(name="final", type=StringType)
occi_State.attributes={occi_State_initial, occi_State_final}

# occi_EnumerationLiteral class attributes and methods
occi_EnumerationLiteral_name: Property = Property(name="name", type=StringType)
occi_EnumerationLiteral_documentation: Property = Property(name="documentation", type=StringType)
occi_EnumerationLiteral.attributes={occi_EnumerationLiteral_documentation, occi_EnumerationLiteral_name}

# occi_Mixin class attributes and methods

# occi_DataType class attributes and methods
occi_DataType_name: Property = Property(name="name", type=StringType)
occi_DataType_documentation: Property = Property(name="documentation", type=StringType)
occi_DataType.attributes={occi_DataType_name, occi_DataType_documentation}

# occi_Kind class attributes and methods
occi_Kind_m_occiIsKindOf: Method = Method(name="occiIsKindOf", parameters={Parameter(name='occi_kind', type=StringType)}, type=StringType)
occi_Kind.methods={occi_Kind_m_occiIsKindOf}

# Type class attributes and methods

# occi_AttributeState class attributes and methods
occi_AttributeState_name: Property = Property(name="name", type=StringType)
occi_AttributeState_value: Property = Property(name="value", type=StringType)
occi_AttributeState.attributes={occi_AttributeState_value, occi_AttributeState_name}

# occi_MixinBase class attributes and methods

# occi_Entity class attributes and methods
occi_Entity_id: Property = Property(name="id", type=StringType)
occi_Entity_title: Property = Property(name="title", type=StringType)
occi_Entity_location: Property = Property(name="location", type=StringType)
occi_Entity_m_occiCreate: Method = Method(name="occiCreate", parameters={})
occi_Entity_m_occiRetrieve: Method = Method(name="occiRetrieve", parameters={})
occi_Entity_m_occiUpdate: Method = Method(name="occiUpdate", parameters={})
occi_Entity_m_occiDelete: Method = Method(name="occiDelete", parameters={})
occi_Entity.attributes={occi_Entity_id, occi_Entity_title, occi_Entity_location}
occi_Entity.methods={occi_Entity_m_occiUpdate, occi_Entity_m_occiCreate, occi_Entity_m_occiDelete, occi_Entity_m_occiRetrieve}

# occi_Link class attributes and methods
occi_Link_m_LinkTargetInvariant: Method = Method(name="LinkTargetInvariant", parameters={Parameter(name='occi_linkInstanceKind', type=StringType), Parameter(name='occi_resourcekind', type=StringType)}, type=StringType)
occi_Link_m_LinkSourceInvariant: Method = Method(name="LinkSourceInvariant", parameters={Parameter(name='occi_linkInstanceKind', type=StringType), Parameter(name='occi_resourcekind', type=StringType)}, type=StringType)
occi_Link.methods={occi_Link_m_LinkTargetInvariant, occi_Link_m_LinkSourceInvariant}

# occi_Extension class attributes and methods
occi_Extension_name: Property = Property(name="name", type=StringType)
occi_Extension_scheme: Property = Property(name="scheme", type=StringType)
occi_Extension_description: Property = Property(name="description", type=StringType)
occi_Extension_specification: Property = Property(name="specification", type=StringType)
occi_Extension.attributes={occi_Extension_scheme, occi_Extension_specification, occi_Extension_name, occi_Extension_description}

# occi_Resource class attributes and methods
occi_Resource_summary: Property = Property(name="summary", type=StringType)
occi_Resource.attributes={occi_Resource_summary}

# Entity class attributes and methods

# occi_BasicType class attributes and methods

# DataType class attributes and methods

# occi_StringType class attributes and methods
occi_StringType_pattern: Property = Property(name="pattern", type=StringType)
occi_StringType_length: Property = Property(name="length", type=StringType)
occi_StringType_minLength: Property = Property(name="minLength", type=StringType)
occi_StringType_maxLength: Property = Property(name="maxLength", type=StringType)
occi_StringType.attributes={occi_StringType_length, occi_StringType_minLength, occi_StringType_maxLength, occi_StringType_pattern}

# BasicType class attributes and methods

# occi_EObjectType class attributes and methods
occi_EObjectType_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
occi_EObjectType.attributes={occi_EObjectType_instanceClassName}

# occi_BooleanType class attributes and methods

# occi_NumericType class attributes and methods
occi_NumericType_type: Property = Property(name="type", type=StringType)
occi_NumericType_totalDigits: Property = Property(name="totalDigits", type=StringType)
occi_NumericType_minExclusive: Property = Property(name="minExclusive", type=StringType)
occi_NumericType_maxExclusive: Property = Property(name="maxExclusive", type=StringType)
occi_NumericType_minInclusive: Property = Property(name="minInclusive", type=StringType)
occi_NumericType_maxInclusive: Property = Property(name="maxInclusive", type=StringType)
occi_NumericType.attributes={occi_NumericType_type, occi_NumericType_minExclusive, occi_NumericType_minInclusive, occi_NumericType_maxInclusive, occi_NumericType_maxExclusive, occi_NumericType_totalDigits}

# occi_EnumerationType class attributes and methods

# occi_Configuration class attributes and methods
occi_Configuration_location: Property = Property(name="location", type=StringType)
occi_Configuration_description: Property = Property(name="description", type=StringType)
occi_Configuration.attributes={occi_Configuration_description, occi_Configuration_location}

# Attribute class attributes and methods

# occi_ArrayType class attributes and methods

# occi_RecordType class attributes and methods

# occi_RecordField class attributes and methods

# Relationships
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="occi_Attribute", type=occi_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Category", type=occi_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="occi_Annotation", type=occi_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_AnnotatedElement", type=occi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransition13: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition13",
    ends={
        Property(name="Transition", type=occi_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=occi_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="State15", type=occi_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=occi_State, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="occi_State17", type=occi_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Transition", type=occi_State, multiplicity=Multiplicity(1, 1))
    }
)
action18: BinaryAssociation = BinaryAssociation(
    name="action18",
    ends={
        Property(name="occi_Action20", type=occi_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Transition19", type=occi_Action, multiplicity=Multiplicity(0, 1))
    }
)
actions2: BinaryAssociation = BinaryAssociation(
    name="actions2",
    ends={
        Property(name="occi_Action", type=occi_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Type", type=occi_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="occi_Constraint", type=occi_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Type4", type=occi_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fsm5: BinaryAssociation = BinaryAssociation(
    name="fsm5",
    ends={
        Property(name="occi_FSM", type=occi_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Type6", type=occi_FSM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedState7: BinaryAssociation = BinaryAssociation(
    name="ownedState7",
    ends={
        Property(name="State", type=occi_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=occi_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute8: BinaryAssociation = BinaryAssociation(
    name="attribute8",
    ends={
        Property(name="occi_Attribute10", type=occi_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_FSM9", type=occi_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
literal11: BinaryAssociation = BinaryAssociation(
    name="literal11",
    ends={
        Property(name="occi_EnumerationLiteral", type=occi_State, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_State", type=occi_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
owningFSM12: BinaryAssociation = BinaryAssociation(
    name="owningFSM12",
    ends={
        Property(name="FSM", type=occi_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=occi_FSM, multiplicity=Multiplicity(1, 1))
    }
)
depends34: BinaryAssociation = BinaryAssociation(
    name="depends34",
    ends={
        Property(name="occi_Mixin", type=occi_Mixin, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Mixin33", type=occi_Mixin, multiplicity=Multiplicity(0, 9999))
    }
)
applies35: BinaryAssociation = BinaryAssociation(
    name="applies35",
    ends={
        Property(name="occi_Kind37", type=occi_Mixin, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Mixin36", type=occi_Kind, multiplicity=Multiplicity(0, 9999))
    }
)
entities38: BinaryAssociation = BinaryAssociation(
    name="entities38",
    ends={
        Property(name="occi_Entity40", type=occi_Mixin, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Mixin39", type=occi_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
kind41: BinaryAssociation = BinaryAssociation(
    name="kind41",
    ends={
        Property(name="occi_Kind43", type=occi_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Entity42", type=occi_Kind, multiplicity=Multiplicity(1, 1))
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="occi_DataType", type=occi_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Attribute22", type=occi_DataType, multiplicity=Multiplicity(0, 1))
    }
)
attributes44: BinaryAssociation = BinaryAssociation(
    name="attributes44",
    ends={
        Property(name="occi_AttributeState", type=occi_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Entity45", type=occi_AttributeState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mixins46: BinaryAssociation = BinaryAssociation(
    name="mixins46",
    ends={
        Property(name="occi_Mixin48", type=occi_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Entity47", type=occi_Mixin, multiplicity=Multiplicity(0, 9999))
    }
)
parts49: BinaryAssociation = BinaryAssociation(
    name="parts49",
    ends={
        Property(name="MixinBase", type=occi_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=occi_MixinBase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent24: BinaryAssociation = BinaryAssociation(
    name="parent24",
    ends={
        Property(name="occi_Kind", type=occi_Kind, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Kind23", type=occi_Kind, multiplicity=Multiplicity(0, 1))
    }
)
mixin50: BinaryAssociation = BinaryAssociation(
    name="mixin50",
    ends={
        Property(name="occi_Mixin51", type=occi_MixinBase, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_MixinBase", type=occi_Mixin, multiplicity=Multiplicity(1, 1))
    }
)
entity52: BinaryAssociation = BinaryAssociation(
    name="entity52",
    ends={
        Property(name="Entity", type=occi_MixinBase, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=occi_Entity, multiplicity=Multiplicity(1, 1))
    }
)
entities25: BinaryAssociation = BinaryAssociation(
    name="entities25",
    ends={
        Property(name="occi_Entity", type=occi_Kind, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Kind26", type=occi_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
source28: BinaryAssociation = BinaryAssociation(
    name="source28",
    ends={
        Property(name="occi_Kind29", type=occi_Kind, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Kind27", type=occi_Kind, multiplicity=Multiplicity(0, 9999))
    }
)
target31: BinaryAssociation = BinaryAssociation(
    name="target31",
    ends={
        Property(name="occi_Kind32", type=occi_Kind, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Kind30", type=occi_Kind, multiplicity=Multiplicity(0, 9999))
    }
)
links56: BinaryAssociation = BinaryAssociation(
    name="links56",
    ends={
        Property(name="Link", type=occi_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="source57", type=occi_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rlinks58: BinaryAssociation = BinaryAssociation(
    name="rlinks58",
    ends={
        Property(name="Link59", type=occi_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=occi_Link, multiplicity=Multiplicity(0, 9999))
    }
)
source60: BinaryAssociation = BinaryAssociation(
    name="source60",
    ends={
        Property(name="Resource", type=occi_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="links", type=occi_Resource, multiplicity=Multiplicity(1, 1))
    }
)
target61: BinaryAssociation = BinaryAssociation(
    name="target61",
    ends={
        Property(name="Resource62", type=occi_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="rlinks", type=occi_Resource, multiplicity=Multiplicity(1, 1))
    }
)
import_64: BinaryAssociation = BinaryAssociation(
    name="import_64",
    ends={
        Property(name="occi_Extension", type=occi_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Extension63", type=occi_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
kinds65: BinaryAssociation = BinaryAssociation(
    name="kinds65",
    ends={
        Property(name="occi_Kind67", type=occi_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Extension66", type=occi_Kind, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mixins68: BinaryAssociation = BinaryAssociation(
    name="mixins68",
    ends={
        Property(name="occi_Mixin70", type=occi_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Extension69", type=occi_Mixin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types71: BinaryAssociation = BinaryAssociation(
    name="types71",
    ends={
        Property(name="occi_DataType73", type=occi_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Extension72", type=occi_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes53: BinaryAssociation = BinaryAssociation(
    name="attributes53",
    ends={
        Property(name="occi_AttributeState55", type=occi_MixinBase, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_MixinBase54", type=occi_AttributeState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
use74: BinaryAssociation = BinaryAssociation(
    name="use74",
    ends={
        Property(name="occi_Extension75", type=occi_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Configuration", type=occi_Extension, multiplicity=Multiplicity(0, 9999))
    }
)
resources76: BinaryAssociation = BinaryAssociation(
    name="resources76",
    ends={
        Property(name="occi_Resource", type=occi_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Configuration77", type=occi_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mixins78: BinaryAssociation = BinaryAssociation(
    name="mixins78",
    ends={
        Property(name="occi_Mixin80", type=occi_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_Configuration79", type=occi_Mixin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals81: BinaryAssociation = BinaryAssociation(
    name="literals81",
    ends={
        Property(name="EnumerationLiteral", type=occi_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="enumerationType", type=occi_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
recordFields83: BinaryAssociation = BinaryAssociation(
    name="recordFields83",
    ends={
        Property(name="occi_RecordField", type=occi_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_RecordType", type=occi_RecordField, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type84: BinaryAssociation = BinaryAssociation(
    name="type84",
    ends={
        Property(name="occi_DataType85", type=occi_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="occi_ArrayType", type=occi_DataType, multiplicity=Multiplicity(1, 1))
    }
)
enumerationType82: BinaryAssociation = BinaryAssociation(
    name="enumerationType82",
    ends={
        Property(name="EnumerationType", type=occi_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=occi_EnumerationType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_occi_Category_AnnotatedElement = Generalization(general=AnnotatedElement, specific=occi_Category)
gen_occi_Type_Category = Generalization(general=Category, specific=occi_Type)
gen_occi_Mixin_Type = Generalization(general=Type, specific=occi_Mixin)
gen_occi_Attribute_AnnotatedElement = Generalization(general=AnnotatedElement, specific=occi_Attribute)
gen_occi_Kind_Type = Generalization(general=Type, specific=occi_Kind)
gen_occi_Action_Category = Generalization(general=Category, specific=occi_Action)
gen_occi_Link_Entity = Generalization(general=Entity, specific=occi_Link)
gen_occi_Resource_Entity = Generalization(general=Entity, specific=occi_Resource)
gen_occi_BasicType_DataType = Generalization(general=DataType, specific=occi_BasicType)
gen_occi_StringType_BasicType = Generalization(general=BasicType, specific=occi_StringType)
gen_occi_EObjectType_BasicType = Generalization(general=BasicType, specific=occi_EObjectType)
gen_occi_BooleanType_BasicType = Generalization(general=BasicType, specific=occi_BooleanType)
gen_occi_NumericType_BasicType = Generalization(general=BasicType, specific=occi_NumericType)
gen_occi_EnumerationType_DataType = Generalization(general=DataType, specific=occi_EnumerationType)
gen_occi_RecordField_Attribute = Generalization(general=Attribute, specific=occi_RecordField)
gen_occi_ArrayType_DataType = Generalization(general=DataType, specific=occi_ArrayType)
gen_occi_RecordType_DataType = Generalization(general=DataType, specific=occi_RecordType)

# Domain Model
domain_model = DomainModel(
    name="occi",
    types={occi_Attribute, occi_Constraint, occi_AnnotatedElement, occi_Annotation, occi_Category, AnnotatedElement, occi_Transition, occi_Type, Category, occi_Action, occi_FSM, occi_State, occi_EnumerationLiteral, occi_Mixin, occi_DataType, occi_Kind, Type, occi_AttributeState, occi_MixinBase, occi_Entity, occi_Link, occi_Extension, occi_Resource, Entity, occi_BasicType, DataType, occi_StringType, BasicType, occi_EObjectType, occi_BooleanType, occi_NumericType, occi_EnumerationType, occi_Configuration, Attribute, occi_ArrayType, occi_RecordType, occi_RecordField, NumericTypeEnum},
    associations={attributes1, annotations0, outgoingTransition13, source14, target16, action18, actions2, constraints3, fsm5, ownedState7, attribute8, literal11, owningFSM12, depends34, applies35, entities38, kind41, type21, attributes44, mixins46, parts49, parent24, mixin50, entity52, entities25, source28, target31, links56, rlinks58, source60, target61, import_64, kinds65, mixins68, types71, attributes53, use74, resources76, mixins78, literals81, recordFields83, type84, enumerationType82},
    generalizations={gen_occi_Category_AnnotatedElement, gen_occi_Type_Category, gen_occi_Mixin_Type, gen_occi_Attribute_AnnotatedElement, gen_occi_Kind_Type, gen_occi_Action_Category, gen_occi_Link_Entity, gen_occi_Resource_Entity, gen_occi_BasicType_DataType, gen_occi_StringType_BasicType, gen_occi_EObjectType_BasicType, gen_occi_BooleanType_BasicType, gen_occi_NumericType_BasicType, gen_occi_EnumerationType_DataType, gen_occi_RecordField_Attribute, gen_occi_ArrayType_DataType, gen_occi_RecordType_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)