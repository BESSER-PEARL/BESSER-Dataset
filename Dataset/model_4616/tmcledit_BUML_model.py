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
TopicId: Enumeration = Enumeration(
    name="TopicId",
    literals={
            EnumerationLiteral(name="SUBJECT_LOCATOR"),
			EnumerationLiteral(name="SUBJECT_IDENTIFIER"),
			EnumerationLiteral(name="ITEM_IDENTIFIER"),
			EnumerationLiteral(name="IDENTIFIER")
    }
)

EdgeType: Enumeration = Enumeration(
    name="EdgeType",
    literals={
            EnumerationLiteral(name="IS_ATYPE"),
			EnumerationLiteral(name="AKO_TYPE"),
			EnumerationLiteral(name="ROLE_CONSTRAINT_TYPE")
    }
)

KindOfTopicType: Enumeration = Enumeration(
    name="KindOfTopicType",
    literals={
            EnumerationLiteral(name="TopicType"),
			EnumerationLiteral(name="OccurrenceType"),
			EnumerationLiteral(name="NameType"),
			EnumerationLiteral(name="RoleType"),
			EnumerationLiteral(name="AssociationType"),
			EnumerationLiteral(name="ScopeType"),
			EnumerationLiteral(name="NoType")
    }
)

# Classes
TMCLConstruct = Class(name="TMCLConstruct")
model_OccurrenceTypeConstraint = Class(name="model::OccurrenceTypeConstraint")
model_NameTypeConstraint = Class(name="model::NameTypeConstraint")
model_SubjectIdentifierConstraint = Class(name="model::SubjectIdentifierConstraint")
model_SubjectLocatorConstraint = Class(name="model::SubjectLocatorConstraint")
model_TopicReifiesConstraint = Class(name="model::TopicReifiesConstraint")
model_ItemIdentifierConstraint = Class(name="model::ItemIdentifierConstraint")
model_TopicType = Class(name="model::TopicType")
model_AssociationTypeConstraint = Class(name="model::AssociationTypeConstraint")
model_MappingElement = Class(name="model::MappingElement")
AbstractRegExpConstraint = Class(name="AbstractRegExpConstraint")
AbstractTypedConstraint = Class(name="AbstractTypedConstraint")
OnoObject = Class(name="OnoObject")
model_Node = Class(name="model::Node")
model_TypeNode = Class(name="model::TypeNode")
Node = Class(name="Node")
model_AbstractRegExpConstraint = Class(name="model::AbstractRegExpConstraint", is_abstract=True)
AbstractConstraint = Class(name="AbstractConstraint")
AbstractTypedCardinalityConstraint = Class(name="AbstractTypedCardinalityConstraint")
model_RolePlayerConstraint = Class(name="model::RolePlayerConstraint")
AbstractCardinalityConstraint = Class(name="AbstractCardinalityConstraint")
model_RoleConstraint = Class(name="model::RoleConstraint")
model_TopicMapSchema = Class(name="model::TopicMapSchema")
model_Diagram = Class(name="model::Diagram")
model_Comment = Class(name="model::Comment")
model_File = Class(name="model::File")
model_Bendpoint = Class(name="model::Bendpoint")
model_Edge = Class(name="model::Edge")
model_LabelPos = Class(name="model::LabelPos")
model_AssociationNode = Class(name="model::AssociationNode")
model_AssociationType = Class(name="model::AssociationType")
ScopedTopicType = Class(name="ScopedTopicType")
ScopedReifiableTopicType = Class(name="ScopedReifiableTopicType")
model_RoleCombinationConstraint = Class(name="model::RoleCombinationConstraint")
model_OccurrenceType = Class(name="model::OccurrenceType")
AbstractRegExpTopicType = Class(name="AbstractRegExpTopicType")
AbstractUniqueValueTopicType = Class(name="AbstractUniqueValueTopicType")
model_RoleType = Class(name="model::RoleType")
model_ScopeConstraint = Class(name="model::ScopeConstraint")
model_AbstractCardinalityConstraint = Class(name="model::AbstractCardinalityConstraint", is_abstract=True)
model_AbstractTypedConstraint = Class(name="model::AbstractTypedConstraint", is_abstract=True)
model_ScopedTopicType = Class(name="model::ScopedTopicType", is_abstract=True)
TopicType = Class(name="TopicType")
ReifiableTopicType = Class(name="ReifiableTopicType")
model_AbstractRegExpTopicType = Class(name="model::AbstractRegExpTopicType", is_abstract=True)
model_AbstractConstraint = Class(name="model::AbstractConstraint", is_abstract=True)
model_DomainDiagram = Class(name="model::DomainDiagram")
Diagram = Class(name="Diagram")
model_OnoObject = Class(name="model::OnoObject", is_abstract=True)
model_AbstractUniqueValueTopicType = Class(name="model::AbstractUniqueValueTopicType")
model_NameType = Class(name="model::NameType")
model_AbstractTypedCardinalityConstraint = Class(name="model::AbstractTypedCardinalityConstraint")
model_TMCLConstruct = Class(name="model::TMCLConstruct")
model_Annotation = Class(name="model::Annotation")
model_ReifierConstraint = Class(name="model::ReifierConstraint")
model_ReifiableTopicType = Class(name="model::ReifiableTopicType")
model_ScopedReifiableTopicType = Class(name="model::ScopedReifiableTopicType")

# TMCLConstruct class attributes and methods

# model_OccurrenceTypeConstraint class attributes and methods

# model_NameTypeConstraint class attributes and methods

# model_SubjectIdentifierConstraint class attributes and methods

# model_SubjectLocatorConstraint class attributes and methods

# model_TopicReifiesConstraint class attributes and methods

# model_ItemIdentifierConstraint class attributes and methods

# model_TopicType class attributes and methods
model_TopicType_identifiers: Property = Property(name="identifiers", type=StringType)
model_TopicType_idType: Property = Property(name="idType", type=StringType)
model_TopicType_abstract: Property = Property(name="abstract", type=BooleanType)
model_TopicType_kind: Property = Property(name="kind", type=StringType)
model_TopicType_name: Property = Property(name="name", type=StringType)
model_TopicType_locators: Property = Property(name="locators", type=StringType)
model_TopicType.attributes={model_TopicType_abstract, model_TopicType_name, model_TopicType_kind, model_TopicType_idType, model_TopicType_locators, model_TopicType_identifiers}

# model_AssociationTypeConstraint class attributes and methods

# model_MappingElement class attributes and methods
model_MappingElement_key: Property = Property(name="key", type=StringType)
model_MappingElement_value: Property = Property(name="value", type=StringType)
model_MappingElement.attributes={model_MappingElement_value, model_MappingElement_key}

# AbstractRegExpConstraint class attributes and methods

# AbstractTypedConstraint class attributes and methods

# OnoObject class attributes and methods

# model_Node class attributes and methods
model_Node_posX: Property = Property(name="posX", type=IntegerType)
model_Node_posY: Property = Property(name="posY", type=IntegerType)
model_Node.attributes={model_Node_posX, model_Node_posY}

# model_TypeNode class attributes and methods
model_TypeNode_image: Property = Property(name="image", type=StringType)
model_TypeNode.attributes={model_TypeNode_image}

# Node class attributes and methods

# model_AbstractRegExpConstraint class attributes and methods
model_AbstractRegExpConstraint_regexp: Property = Property(name="regexp", type=StringType)
model_AbstractRegExpConstraint.attributes={model_AbstractRegExpConstraint_regexp}

# AbstractConstraint class attributes and methods

# AbstractTypedCardinalityConstraint class attributes and methods

# model_RolePlayerConstraint class attributes and methods

# AbstractCardinalityConstraint class attributes and methods

# model_RoleConstraint class attributes and methods

# model_TopicMapSchema class attributes and methods
model_TopicMapSchema_includes: Property = Property(name="includes", type=StringType)
model_TopicMapSchema_baseLocator: Property = Property(name="baseLocator", type=StringType)
model_TopicMapSchema_name: Property = Property(name="name", type=StringType)
model_TopicMapSchema_version: Property = Property(name="version", type=StringType)
model_TopicMapSchema_schemaResource: Property = Property(name="schemaResource", type=StringType)
model_TopicMapSchema.attributes={model_TopicMapSchema_includes, model_TopicMapSchema_schemaResource, model_TopicMapSchema_name, model_TopicMapSchema_version, model_TopicMapSchema_baseLocator}

# model_Diagram class attributes and methods
model_Diagram_name: Property = Property(name="name", type=StringType)
model_Diagram.attributes={model_Diagram_name}

# model_Comment class attributes and methods
model_Comment_content: Property = Property(name="content", type=StringType)
model_Comment_width: Property = Property(name="width", type=IntegerType)
model_Comment_height: Property = Property(name="height", type=IntegerType)
model_Comment.attributes={model_Comment_content, model_Comment_width, model_Comment_height}

# model_File class attributes and methods
model_File_filename: Property = Property(name="filename", type=StringType)
model_File_dirty: Property = Property(name="dirty", type=BooleanType)
model_File_notes: Property = Property(name="notes", type=StringType)
model_File.attributes={model_File_notes, model_File_dirty, model_File_filename}

# model_Bendpoint class attributes and methods
model_Bendpoint_posX: Property = Property(name="posX", type=IntegerType)
model_Bendpoint_posY: Property = Property(name="posY", type=IntegerType)
model_Bendpoint.attributes={model_Bendpoint_posY, model_Bendpoint_posX}

# model_Edge class attributes and methods
model_Edge_type: Property = Property(name="type", type=StringType)
model_Edge.attributes={model_Edge_type}

# model_LabelPos class attributes and methods
model_LabelPos_posX: Property = Property(name="posX", type=IntegerType)
model_LabelPos_posY: Property = Property(name="posY", type=IntegerType)
model_LabelPos.attributes={model_LabelPos_posX, model_LabelPos_posY}

# model_AssociationNode class attributes and methods

# model_AssociationType class attributes and methods

# ScopedTopicType class attributes and methods

# ScopedReifiableTopicType class attributes and methods

# model_RoleCombinationConstraint class attributes and methods

# model_OccurrenceType class attributes and methods
model_OccurrenceType_dataType: Property = Property(name="dataType", type=StringType)
model_OccurrenceType.attributes={model_OccurrenceType_dataType}

# AbstractRegExpTopicType class attributes and methods

# AbstractUniqueValueTopicType class attributes and methods

# model_RoleType class attributes and methods

# model_ScopeConstraint class attributes and methods

# model_AbstractCardinalityConstraint class attributes and methods
model_AbstractCardinalityConstraint_cardMin: Property = Property(name="cardMin", type=StringType)
model_AbstractCardinalityConstraint_cardMax: Property = Property(name="cardMax", type=StringType)
model_AbstractCardinalityConstraint.attributes={model_AbstractCardinalityConstraint_cardMin, model_AbstractCardinalityConstraint_cardMax}

# model_AbstractTypedConstraint class attributes and methods

# model_ScopedTopicType class attributes and methods

# TopicType class attributes and methods

# ReifiableTopicType class attributes and methods

# model_AbstractRegExpTopicType class attributes and methods
model_AbstractRegExpTopicType_regExp: Property = Property(name="regExp", type=StringType)
model_AbstractRegExpTopicType.attributes={model_AbstractRegExpTopicType_regExp}

# model_AbstractConstraint class attributes and methods

# model_DomainDiagram class attributes and methods

# Diagram class attributes and methods

# model_OnoObject class attributes and methods
model_OnoObject_id: Property = Property(name="id", type=IntegerType)
model_OnoObject.attributes={model_OnoObject_id}

# model_AbstractUniqueValueTopicType class attributes and methods
model_AbstractUniqueValueTopicType_unique: Property = Property(name="unique", type=BooleanType)
model_AbstractUniqueValueTopicType.attributes={model_AbstractUniqueValueTopicType_unique}

# model_NameType class attributes and methods

# model_AbstractTypedCardinalityConstraint class attributes and methods

# model_TMCLConstruct class attributes and methods
model_TMCLConstruct_see_also: Property = Property(name="see_also", type=StringType)
model_TMCLConstruct_comment: Property = Property(name="comment", type=StringType)
model_TMCLConstruct_description: Property = Property(name="description", type=StringType)
model_TMCLConstruct.attributes={model_TMCLConstruct_comment, model_TMCLConstruct_description, model_TMCLConstruct_see_also}

# model_Annotation class attributes and methods
model_Annotation_key: Property = Property(name="key", type=StringType)
model_Annotation_value: Property = Property(name="value", type=StringType)
model_Annotation.attributes={model_Annotation_value, model_Annotation_key}

# model_ReifierConstraint class attributes and methods

# model_ReifiableTopicType class attributes and methods

# model_ScopedReifiableTopicType class attributes and methods

# Relationships
isa1: BinaryAssociation = BinaryAssociation(
    name="isa1",
    ends={
        Property(name="model_TopicType", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType0", type=model_TopicType, multiplicity=Multiplicity(0, 9999))
    }
)
ako3: BinaryAssociation = BinaryAssociation(
    name="ako3",
    ends={
        Property(name="model_TopicType4", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType2", type=model_TopicType, multiplicity=Multiplicity(0, 9999))
    }
)
occurrenceConstraints5: BinaryAssociation = BinaryAssociation(
    name="occurrenceConstraints5",
    ends={
        Property(name="model_OccurrenceTypeConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType6", type=model_OccurrenceTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nameConstraints7: BinaryAssociation = BinaryAssociation(
    name="nameConstraints7",
    ends={
        Property(name="model_NameTypeConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType8", type=model_NameTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subjectIdentifierConstraints9: BinaryAssociation = BinaryAssociation(
    name="subjectIdentifierConstraints9",
    ends={
        Property(name="model_SubjectIdentifierConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType10", type=model_SubjectIdentifierConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subjectLocatorConstraints11: BinaryAssociation = BinaryAssociation(
    name="subjectLocatorConstraints11",
    ends={
        Property(name="model_SubjectLocatorConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType12", type=model_SubjectLocatorConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overlap14: BinaryAssociation = BinaryAssociation(
    name="overlap14",
    ends={
        Property(name="model_TopicType15", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType13", type=model_TopicType, multiplicity=Multiplicity(0, 9999))
    }
)
topicReifiesConstraints16: BinaryAssociation = BinaryAssociation(
    name="topicReifiesConstraints16",
    ends={
        Property(name="model_TopicReifiesConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType17", type=model_TopicReifiesConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itemIdentifierConstraints18: BinaryAssociation = BinaryAssociation(
    name="itemIdentifierConstraints18",
    ends={
        Property(name="model_ItemIdentifierConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicType19", type=model_ItemIdentifierConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topicTypes24: BinaryAssociation = BinaryAssociation(
    name="topicTypes24",
    ends={
        Property(name="model_TopicMapSchema", type=model_TopicType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="model_TopicType25", type=model_TopicMapSchema, multiplicity=Multiplicity(1, 1))
    }
)
associationTypeConstraints26: BinaryAssociation = BinaryAssociation(
    name="associationTypeConstraints26",
    ends={
        Property(name="model_AssociationTypeConstraint", type=model_TopicMapSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicMapSchema27", type=model_AssociationTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings28: BinaryAssociation = BinaryAssociation(
    name="mappings28",
    ends={
        Property(name="model_MappingElement", type=model_TopicMapSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TopicMapSchema29", type=model_MappingElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
playerConstraints30: BinaryAssociation = BinaryAssociation(
    name="playerConstraints30",
    ends={
        Property(name="model_RolePlayerConstraint32", type=model_AssociationTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AssociationTypeConstraint31", type=model_RolePlayerConstraint, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
topicType33: BinaryAssociation = BinaryAssociation(
    name="topicType33",
    ends={
        Property(name="model_TopicType34", type=model_TypeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TypeNode", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
player20: BinaryAssociation = BinaryAssociation(
    name="player20",
    ends={
        Property(name="model_TopicType21", type=model_RolePlayerConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RolePlayerConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
role22: BinaryAssociation = BinaryAssociation(
    name="role22",
    ends={
        Property(name="model_RoleConstraint", type=model_RolePlayerConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RolePlayerConstraint23", type=model_RoleConstraint, multiplicity=Multiplicity(1, 1))
    }
)
edges48: BinaryAssociation = BinaryAssociation(
    name="edges48",
    ends={
        Property(name="model_Edge49", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram", type=model_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes50: BinaryAssociation = BinaryAssociation(
    name="nodes50",
    ends={
        Property(name="model_Node52", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram51", type=model_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments53: BinaryAssociation = BinaryAssociation(
    name="comments53",
    ends={
        Property(name="model_Comment", type=model_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Diagram54", type=model_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams55: BinaryAssociation = BinaryAssociation(
    name="diagrams55",
    ends={
        Property(name="model_Diagram56", type=model_File, multiplicity=Multiplicity(1, 1)),
        Property(name="model_File", type=model_Diagram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topicMapSchema57: BinaryAssociation = BinaryAssociation(
    name="topicMapSchema57",
    ends={
        Property(name="model_TopicMapSchema59", type=model_File, multiplicity=Multiplicity(1, 1)),
        Property(name="model_File58", type=model_TopicMapSchema, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bendpoints35: BinaryAssociation = BinaryAssociation(
    name="bendpoints35",
    ends={
        Property(name="model_Bendpoint", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge", type=model_Bendpoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source36: BinaryAssociation = BinaryAssociation(
    name="source36",
    ends={
        Property(name="model_Node", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge37", type=model_Node, multiplicity=Multiplicity(1, 1))
    }
)
target38: BinaryAssociation = BinaryAssociation(
    name="target38",
    ends={
        Property(name="model_Node40", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge39", type=model_Node, multiplicity=Multiplicity(1, 1))
    }
)
roleConstraint41: BinaryAssociation = BinaryAssociation(
    name="roleConstraint41",
    ends={
        Property(name="model_RolePlayerConstraint43", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge42", type=model_RolePlayerConstraint, multiplicity=Multiplicity(0, 1))
    }
)
labelPositions44: BinaryAssociation = BinaryAssociation(
    name="labelPositions44",
    ends={
        Property(name="model_LabelPos", type=model_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Edge45", type=model_LabelPos, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
scope62: BinaryAssociation = BinaryAssociation(
    name="scope62",
    ends={
        Property(name="model_ScopeConstraint", type=model_ScopedTopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ScopedTopicType", type=model_ScopeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationConstraint46: BinaryAssociation = BinaryAssociation(
    name="associationConstraint46",
    ends={
        Property(name="model_AssociationTypeConstraint47", type=model_AssociationNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AssociationNode", type=model_AssociationTypeConstraint, multiplicity=Multiplicity(1, 1))
    }
)
roles63: BinaryAssociation = BinaryAssociation(
    name="roles63",
    ends={
        Property(name="model_RoleConstraint64", type=model_AssociationType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AssociationType", type=model_RoleConstraint, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
roleCombinations65: BinaryAssociation = BinaryAssociation(
    name="roleCombinations65",
    ends={
        Property(name="model_RoleCombinationConstraint", type=model_AssociationType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AssociationType66", type=model_RoleCombinationConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
player67: BinaryAssociation = BinaryAssociation(
    name="player67",
    ends={
        Property(name="model_TopicType69", type=model_RoleCombinationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoleCombinationConstraint68", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
otherPlayer70: BinaryAssociation = BinaryAssociation(
    name="otherPlayer70",
    ends={
        Property(name="model_TopicType72", type=model_RoleCombinationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoleCombinationConstraint71", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
otherRole73: BinaryAssociation = BinaryAssociation(
    name="otherRole73",
    ends={
        Property(name="model_TopicType75", type=model_RoleCombinationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoleCombinationConstraint74", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
type60: BinaryAssociation = BinaryAssociation(
    name="type60",
    ends={
        Property(name="model_TopicType61", type=model_AbstractTypedConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractTypedConstraint", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
role76: BinaryAssociation = BinaryAssociation(
    name="role76",
    ends={
        Property(name="model_TopicType78", type=model_RoleCombinationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_RoleCombinationConstraint77", type=model_TopicType, multiplicity=Multiplicity(1, 1))
    }
)
annotations79: BinaryAssociation = BinaryAssociation(
    name="annotations79",
    ends={
        Property(name="model_Annotation", type=model_TMCLConstruct, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TMCLConstruct", type=model_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reifierConstraint80: BinaryAssociation = BinaryAssociation(
    name="reifierConstraint80",
    ends={
        Property(name="model_ReifierConstraint", type=model_ReifiableTopicType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ReifiableTopicType", type=model_ReifierConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_TopicType_TMCLConstruct = Generalization(general=TMCLConstruct, specific=model_TopicType)
gen_model_SubjectLocatorConstraint_AbstractRegExpConstraint = Generalization(general=AbstractRegExpConstraint, specific=model_SubjectLocatorConstraint)
gen_model_SubjectLocatorConstraint_AbstractCardinalityConstraint = Generalization(general=AbstractCardinalityConstraint, specific=model_SubjectLocatorConstraint)
gen_model_SubjectIdentifierConstraint_AbstractRegExpConstraint = Generalization(general=AbstractRegExpConstraint, specific=model_SubjectIdentifierConstraint)
gen_model_SubjectIdentifierConstraint_AbstractCardinalityConstraint = Generalization(general=AbstractCardinalityConstraint, specific=model_SubjectIdentifierConstraint)
gen_model_AssociationTypeConstraint_AbstractTypedConstraint = Generalization(general=AbstractTypedConstraint, specific=model_AssociationTypeConstraint)
gen_model_MappingElement_OnoObject = Generalization(general=OnoObject, specific=model_MappingElement)
gen_model_Node_OnoObject = Generalization(general=OnoObject, specific=model_Node)
gen_model_TypeNode_Node = Generalization(general=Node, specific=model_TypeNode)
gen_model_AbstractRegExpConstraint_AbstractConstraint = Generalization(general=AbstractConstraint, specific=model_AbstractRegExpConstraint)
gen_model_OccurrenceTypeConstraint_AbstractTypedCardinalityConstraint = Generalization(general=AbstractTypedCardinalityConstraint, specific=model_OccurrenceTypeConstraint)
gen_model_NameTypeConstraint_AbstractTypedCardinalityConstraint = Generalization(general=AbstractTypedCardinalityConstraint, specific=model_NameTypeConstraint)
gen_model_RolePlayerConstraint_AbstractCardinalityConstraint = Generalization(general=AbstractCardinalityConstraint, specific=model_RolePlayerConstraint)
gen_model_TopicMapSchema_TMCLConstruct = Generalization(general=TMCLConstruct, specific=model_TopicMapSchema)
gen_model_Diagram_OnoObject = Generalization(general=OnoObject, specific=model_Diagram)
gen_model_File_OnoObject = Generalization(general=OnoObject, specific=model_File)
gen_model_Bendpoint_OnoObject = Generalization(general=OnoObject, specific=model_Bendpoint)
gen_model_Edge_OnoObject = Generalization(general=OnoObject, specific=model_Edge)
gen_model_AssociationNode_Node = Generalization(general=Node, specific=model_AssociationNode)
gen_model_AssociationType_ScopedTopicType = Generalization(general=ScopedTopicType, specific=model_AssociationType)
gen_model_AssociationType_ScopedReifiableTopicType = Generalization(general=ScopedReifiableTopicType, specific=model_AssociationType)
gen_model_OccurrenceType_ScopedTopicType = Generalization(general=ScopedTopicType, specific=model_OccurrenceType)
gen_model_OccurrenceType_ScopedReifiableTopicType = Generalization(general=ScopedReifiableTopicType, specific=model_OccurrenceType)
gen_model_OccurrenceType_AbstractRegExpTopicType = Generalization(general=AbstractRegExpTopicType, specific=model_OccurrenceType)
gen_model_OccurrenceType_AbstractUniqueValueTopicType = Generalization(general=AbstractUniqueValueTopicType, specific=model_OccurrenceType)
gen_model_RoleConstraint_AbstractTypedCardinalityConstraint = Generalization(general=AbstractTypedCardinalityConstraint, specific=model_RoleConstraint)
gen_model_RoleType_TopicType = Generalization(general=TopicType, specific=model_RoleType)
gen_model_RoleCombinationConstraint_AbstractConstraint = Generalization(general=AbstractConstraint, specific=model_RoleCombinationConstraint)
gen_model_ScopeConstraint_AbstractTypedCardinalityConstraint = Generalization(general=AbstractTypedCardinalityConstraint, specific=model_ScopeConstraint)
gen_model_AbstractCardinalityConstraint_AbstractConstraint = Generalization(general=AbstractConstraint, specific=model_AbstractCardinalityConstraint)
gen_model_LabelPos_OnoObject = Generalization(general=OnoObject, specific=model_LabelPos)
gen_model_AbstractTypedConstraint_AbstractConstraint = Generalization(general=AbstractConstraint, specific=model_AbstractTypedConstraint)
gen_model_ScopedTopicType_TopicType = Generalization(general=TopicType, specific=model_ScopedTopicType)
gen_model_ScopedReifiableTopicType_ReifiableTopicType = Generalization(general=ReifiableTopicType, specific=model_ScopedReifiableTopicType)
gen_model_Annotation_OnoObject = Generalization(general=OnoObject, specific=model_Annotation)
gen_model_AbstractRegExpTopicType_TopicType = Generalization(general=TopicType, specific=model_AbstractRegExpTopicType)
gen_model_AbstractConstraint_TMCLConstruct = Generalization(general=TMCLConstruct, specific=model_AbstractConstraint)
gen_model_TopicReifiesConstraint_AbstractTypedCardinalityConstraint = Generalization(general=AbstractTypedCardinalityConstraint, specific=model_TopicReifiesConstraint)
gen_model_DomainDiagram_Diagram = Generalization(general=Diagram, specific=model_DomainDiagram)
gen_model_AbstractUniqueValueTopicType_TopicType = Generalization(general=TopicType, specific=model_AbstractUniqueValueTopicType)
gen_model_ItemIdentifierConstraint_AbstractRegExpConstraint = Generalization(general=AbstractRegExpConstraint, specific=model_ItemIdentifierConstraint)
gen_model_ItemIdentifierConstraint_AbstractCardinalityConstraint = Generalization(general=AbstractCardinalityConstraint, specific=model_ItemIdentifierConstraint)
gen_model_NameType_ScopedTopicType = Generalization(general=ScopedTopicType, specific=model_NameType)
gen_model_NameType_ScopedReifiableTopicType = Generalization(general=ScopedReifiableTopicType, specific=model_NameType)
gen_model_NameType_AbstractRegExpTopicType = Generalization(general=AbstractRegExpTopicType, specific=model_NameType)
gen_model_NameType_AbstractUniqueValueTopicType = Generalization(general=AbstractUniqueValueTopicType, specific=model_NameType)
gen_model_AbstractTypedCardinalityConstraint_AbstractCardinalityConstraint = Generalization(general=AbstractCardinalityConstraint, specific=model_AbstractTypedCardinalityConstraint)
gen_model_AbstractTypedCardinalityConstraint_AbstractTypedConstraint = Generalization(general=AbstractTypedConstraint, specific=model_AbstractTypedCardinalityConstraint)
gen_model_Comment_Node = Generalization(general=Node, specific=model_Comment)
gen_model_TMCLConstruct_OnoObject = Generalization(general=OnoObject, specific=model_TMCLConstruct)
gen_model_ReifierConstraint_AbstractTypedCardinalityConstraint = Generalization(general=AbstractTypedCardinalityConstraint, specific=model_ReifierConstraint)
gen_model_ReifiableTopicType_TopicType = Generalization(general=TopicType, specific=model_ReifiableTopicType)
gen_model_ScopedReifiableTopicType_ScopedTopicType = Generalization(general=ScopedTopicType, specific=model_ScopedReifiableTopicType)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={TMCLConstruct, model_OccurrenceTypeConstraint, model_NameTypeConstraint, model_SubjectIdentifierConstraint, model_SubjectLocatorConstraint, model_TopicReifiesConstraint, model_ItemIdentifierConstraint, model_TopicType, model_AssociationTypeConstraint, model_MappingElement, AbstractRegExpConstraint, AbstractTypedConstraint, OnoObject, model_Node, model_TypeNode, Node, model_AbstractRegExpConstraint, AbstractConstraint, AbstractTypedCardinalityConstraint, model_RolePlayerConstraint, AbstractCardinalityConstraint, model_RoleConstraint, model_TopicMapSchema, model_Diagram, model_Comment, model_File, model_Bendpoint, model_Edge, model_LabelPos, model_AssociationNode, model_AssociationType, ScopedTopicType, ScopedReifiableTopicType, model_RoleCombinationConstraint, model_OccurrenceType, AbstractRegExpTopicType, AbstractUniqueValueTopicType, model_RoleType, model_ScopeConstraint, model_AbstractCardinalityConstraint, model_AbstractTypedConstraint, model_ScopedTopicType, TopicType, ReifiableTopicType, model_AbstractRegExpTopicType, model_AbstractConstraint, model_DomainDiagram, Diagram, model_OnoObject, model_AbstractUniqueValueTopicType, model_NameType, model_AbstractTypedCardinalityConstraint, model_TMCLConstruct, model_Annotation, model_ReifierConstraint, model_ReifiableTopicType, model_ScopedReifiableTopicType, TopicId, EdgeType, KindOfTopicType},
    associations={isa1, ako3, occurrenceConstraints5, nameConstraints7, subjectIdentifierConstraints9, subjectLocatorConstraints11, overlap14, topicReifiesConstraints16, itemIdentifierConstraints18, topicTypes24, associationTypeConstraints26, mappings28, playerConstraints30, topicType33, player20, role22, edges48, nodes50, comments53, diagrams55, topicMapSchema57, bendpoints35, source36, target38, roleConstraint41, labelPositions44, scope62, associationConstraint46, roles63, roleCombinations65, player67, otherPlayer70, otherRole73, type60, role76, annotations79, reifierConstraint80},
    generalizations={gen_model_TopicType_TMCLConstruct, gen_model_SubjectLocatorConstraint_AbstractRegExpConstraint, gen_model_SubjectLocatorConstraint_AbstractCardinalityConstraint, gen_model_SubjectIdentifierConstraint_AbstractRegExpConstraint, gen_model_SubjectIdentifierConstraint_AbstractCardinalityConstraint, gen_model_AssociationTypeConstraint_AbstractTypedConstraint, gen_model_MappingElement_OnoObject, gen_model_Node_OnoObject, gen_model_TypeNode_Node, gen_model_AbstractRegExpConstraint_AbstractConstraint, gen_model_OccurrenceTypeConstraint_AbstractTypedCardinalityConstraint, gen_model_NameTypeConstraint_AbstractTypedCardinalityConstraint, gen_model_RolePlayerConstraint_AbstractCardinalityConstraint, gen_model_TopicMapSchema_TMCLConstruct, gen_model_Diagram_OnoObject, gen_model_File_OnoObject, gen_model_Bendpoint_OnoObject, gen_model_Edge_OnoObject, gen_model_AssociationNode_Node, gen_model_AssociationType_ScopedTopicType, gen_model_AssociationType_ScopedReifiableTopicType, gen_model_OccurrenceType_ScopedTopicType, gen_model_OccurrenceType_ScopedReifiableTopicType, gen_model_OccurrenceType_AbstractRegExpTopicType, gen_model_OccurrenceType_AbstractUniqueValueTopicType, gen_model_RoleConstraint_AbstractTypedCardinalityConstraint, gen_model_RoleType_TopicType, gen_model_RoleCombinationConstraint_AbstractConstraint, gen_model_ScopeConstraint_AbstractTypedCardinalityConstraint, gen_model_AbstractCardinalityConstraint_AbstractConstraint, gen_model_LabelPos_OnoObject, gen_model_AbstractTypedConstraint_AbstractConstraint, gen_model_ScopedTopicType_TopicType, gen_model_ScopedReifiableTopicType_ReifiableTopicType, gen_model_Annotation_OnoObject, gen_model_AbstractRegExpTopicType_TopicType, gen_model_AbstractConstraint_TMCLConstruct, gen_model_TopicReifiesConstraint_AbstractTypedCardinalityConstraint, gen_model_DomainDiagram_Diagram, gen_model_AbstractUniqueValueTopicType_TopicType, gen_model_ItemIdentifierConstraint_AbstractRegExpConstraint, gen_model_ItemIdentifierConstraint_AbstractCardinalityConstraint, gen_model_NameType_ScopedTopicType, gen_model_NameType_ScopedReifiableTopicType, gen_model_NameType_AbstractRegExpTopicType, gen_model_NameType_AbstractUniqueValueTopicType, gen_model_AbstractTypedCardinalityConstraint_AbstractCardinalityConstraint, gen_model_AbstractTypedCardinalityConstraint_AbstractTypedConstraint, gen_model_Comment_Node, gen_model_TMCLConstruct_OnoObject, gen_model_ReifierConstraint_AbstractTypedCardinalityConstraint, gen_model_ReifiableTopicType_TopicType, gen_model_ScopedReifiableTopicType_ScopedTopicType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)