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
SomeKind: Enumeration = Enumeration(
    name="SomeKind",
    literals={
            EnumerationLiteral(name="one"),
			EnumerationLiteral(name="Two"),
			EnumerationLiteral(name="Three")
    }
)

# Classes
sample_ETypes = Class(name="sample::ETypes")
sample_TypeMap = Class(name="sample::TypeMap")
sample_TypeMapReference = Class(name="sample::TypeMapReference")
sample_StringMap = Class(name="sample::StringMap")
sample_DataTypeMap = Class(name="sample::DataTypeMap")
sample_Type = Class(name="sample::Type")
sample_Value = Class(name="sample::Value")
sample_PrimaryObject = Class(name="sample::PrimaryObject")
sample_TargetObject = Class(name="sample::TargetObject")
sample_Tree = Class(name="sample::Tree")
sample_Node = Class(name="sample::Node", is_abstract=True)
sample_Comment = Class(name="sample::Comment")
sample_PhysicalNode = Class(name="sample::PhysicalNode")
Node = Class(name="Node")
sample_RemoteNode = Class(name="sample::RemoteNode")
PhysicalNode = Class(name="PhysicalNode")
sample_LocalNode = Class(name="sample::LocalNode")
sample_VirtualNode = Class(name="sample::VirtualNode")

# sample_ETypes class attributes and methods
sample_ETypes_uris: Property = Property(name="uris", type=StringType)
sample_ETypes.attributes={sample_ETypes_uris}

# sample_TypeMap class attributes and methods

# sample_TypeMapReference class attributes and methods

# sample_StringMap class attributes and methods
sample_StringMap_value: Property = Property(name="value", type=StringType)
sample_StringMap_key: Property = Property(name="key", type=StringType)
sample_StringMap.attributes={sample_StringMap_key, sample_StringMap_value}

# sample_DataTypeMap class attributes and methods
sample_DataTypeMap_key: Property = Property(name="key", type=StringType)
sample_DataTypeMap_value: Property = Property(name="value", type=StringType)
sample_DataTypeMap.attributes={sample_DataTypeMap_key, sample_DataTypeMap_value}

# sample_Type class attributes and methods
sample_Type_name: Property = Property(name="name", type=StringType)
sample_Type.attributes={sample_Type_name}

# sample_Value class attributes and methods
sample_Value_value: Property = Property(name="value", type=IntegerType)
sample_Value.attributes={sample_Value_value}

# sample_PrimaryObject class attributes and methods
sample_PrimaryObject_name: Property = Property(name="name", type=StringType)
sample_PrimaryObject_kind: Property = Property(name="kind", type=StringType)
sample_PrimaryObject_unsettableAttribute: Property = Property(name="unsettableAttribute", type=StringType)
sample_PrimaryObject_id: Property = Property(name="id", type=StringType)
sample_PrimaryObject_unsettableAttributeWithDefault: Property = Property(name="unsettableAttributeWithDefault", type=StringType)
sample_PrimaryObject_featureMapReferenceCollection: Property = Property(name="featureMapReferenceCollection", type=StringType)
sample_PrimaryObject_featureMapAttributeCollection: Property = Property(name="featureMapAttributeCollection", type=StringType)
sample_PrimaryObject_featureMapAttributeType1: Property = Property(name="featureMapAttributeType1", type=StringType)
sample_PrimaryObject_featureMapAttributeType2: Property = Property(name="featureMapAttributeType2", type=StringType)
sample_PrimaryObject.attributes={sample_PrimaryObject_featureMapReferenceCollection, sample_PrimaryObject_unsettableAttributeWithDefault, sample_PrimaryObject_featureMapAttributeType1, sample_PrimaryObject_unsettableAttribute, sample_PrimaryObject_id, sample_PrimaryObject_kind, sample_PrimaryObject_featureMapAttributeType2, sample_PrimaryObject_featureMapAttributeCollection, sample_PrimaryObject_name}

# sample_TargetObject class attributes and methods
sample_TargetObject_name: Property = Property(name="name", type=StringType)
sample_TargetObject_singleAttribute: Property = Property(name="singleAttribute", type=StringType)
sample_TargetObject_manyAttributes: Property = Property(name="manyAttributes", type=StringType)
sample_TargetObject.attributes={sample_TargetObject_manyAttributes, sample_TargetObject_singleAttribute, sample_TargetObject_name}

# sample_Tree class attributes and methods
sample_Tree_name: Property = Property(name="name", type=StringType)
sample_Tree.attributes={sample_Tree_name}

# sample_Node class attributes and methods
sample_Node_label: Property = Property(name="label", type=StringType)
sample_Node.attributes={sample_Node_label}

# sample_Comment class attributes and methods
sample_Comment_content: Property = Property(name="content", type=StringType)
sample_Comment.attributes={sample_Comment_content}

# sample_PhysicalNode class attributes and methods

# Node class attributes and methods

# sample_RemoteNode class attributes and methods

# PhysicalNode class attributes and methods

# sample_LocalNode class attributes and methods

# sample_VirtualNode class attributes and methods

# Relationships
values0: BinaryAssociation = BinaryAssociation(
    name="values0",
    ends={
        Property(name="sample_TypeMap", type=sample_ETypes, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_ETypes", type=sample_TypeMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valuesWithReferences1: BinaryAssociation = BinaryAssociation(
    name="valuesWithReferences1",
    ends={
        Property(name="sample_TypeMapReference", type=sample_ETypes, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_ETypes2", type=sample_TypeMapReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stringValues3: BinaryAssociation = BinaryAssociation(
    name="stringValues3",
    ends={
        Property(name="sample_StringMap", type=sample_ETypes, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_ETypes4", type=sample_StringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypeValues5: BinaryAssociation = BinaryAssociation(
    name="dataTypeValues5",
    ends={
        Property(name="sample_DataTypeMap", type=sample_ETypes, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_ETypes6", type=sample_DataTypeMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key7: BinaryAssociation = BinaryAssociation(
    name="key7",
    ends={
        Property(name="sample_Type", type=sample_TypeMap, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_TypeMap8", type=sample_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="sample_Value", type=sample_TypeMap, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_TypeMap10", type=sample_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key11: BinaryAssociation = BinaryAssociation(
    name="key11",
    ends={
        Property(name="sample_PrimaryObject", type=sample_TypeMapReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_TypeMapReference12", type=sample_PrimaryObject, multiplicity=Multiplicity(0, 1))
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="sample_TargetObject", type=sample_TypeMapReference, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_TypeMapReference14", type=sample_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
featureMapReferenceType233: BinaryAssociation = BinaryAssociation(
    name="featureMapReferenceType233",
    ends={
        Property(name="sample_TargetObject35", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject34", type=sample_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unsettableReference15: BinaryAssociation = BinaryAssociation(
    name="unsettableReference15",
    ends={
        Property(name="sample_TargetObject17", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject16", type=sample_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
singleReference18: BinaryAssociation = BinaryAssociation(
    name="singleReference18",
    ends={
        Property(name="sample_TargetObject20", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject19", type=sample_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
manyReferences21: BinaryAssociation = BinaryAssociation(
    name="manyReferences21",
    ends={
        Property(name="sample_TargetObject23", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject22", type=sample_TargetObject, multiplicity=Multiplicity(0, 9999))
    }
)
singleContainmentReference24: BinaryAssociation = BinaryAssociation(
    name="singleContainmentReference24",
    ends={
        Property(name="sample_TargetObject26", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject25", type=sample_TargetObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
manyContainmentReferences27: BinaryAssociation = BinaryAssociation(
    name="manyContainmentReferences27",
    ends={
        Property(name="sample_TargetObject29", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject28", type=sample_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureMapReferenceType130: BinaryAssociation = BinaryAssociation(
    name="featureMapReferenceType130",
    ends={
        Property(name="sample_TargetObject32", type=sample_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_PrimaryObject31", type=sample_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleReference36: BinaryAssociation = BinaryAssociation(
    name="singleReference36",
    ends={
        Property(name="sample_PrimaryObject38", type=sample_TargetObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_TargetObject37", type=sample_PrimaryObject, multiplicity=Multiplicity(0, 1))
    }
)
manyReferences39: BinaryAssociation = BinaryAssociation(
    name="manyReferences39",
    ends={
        Property(name="sample_PrimaryObject41", type=sample_TargetObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_TargetObject40", type=sample_PrimaryObject, multiplicity=Multiplicity(0, 9999))
    }
)
parentProxy61: BinaryAssociation = BinaryAssociation(
    name="parentProxy61",
    ends={
        Property(name="childrenProxies", type=sample_Node, multiplicity=Multiplicity(0, 1)),
        Property(name="Node62", type=sample_Node, multiplicity=Multiplicity(1, 1))
    }
)
tree63: BinaryAssociation = BinaryAssociation(
    name="tree63",
    ends={
        Property(name="Tree64", type=sample_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=sample_Tree, multiplicity=Multiplicity(0, 1))
    }
)
nodes42: BinaryAssociation = BinaryAssociation(
    name="nodes42",
    ends={
        Property(name="Node", type=sample_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="tree", type=sample_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent44: BinaryAssociation = BinaryAssociation(
    name="parent44",
    ends={
        Property(name="Tree", type=sample_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=sample_Tree, multiplicity=Multiplicity(0, 1))
    }
)
children46: BinaryAssociation = BinaryAssociation(
    name="children46",
    ends={
        Property(name="Tree47", type=sample_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=sample_Tree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manyReference48: BinaryAssociation = BinaryAssociation(
    name="manyReference48",
    ends={
        Property(name="sample_Comment", type=sample_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Tree", type=sample_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
children50: BinaryAssociation = BinaryAssociation(
    name="children50",
    ends={
        Property(name="Node52", type=sample_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parent51", type=sample_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenProxies54: BinaryAssociation = BinaryAssociation(
    name="childrenProxies54",
    ends={
        Property(name="Node55", type=sample_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parentProxy", type=sample_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent57: BinaryAssociation = BinaryAssociation(
    name="parent57",
    ends={
        Property(name="Node59", type=sample_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="children58", type=sample_Node, multiplicity=Multiplicity(0, 1))
    }
)
manyContainmentReference65: BinaryAssociation = BinaryAssociation(
    name="manyContainmentReference65",
    ends={
        Property(name="sample_Comment66", type=sample_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Node", type=sample_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_sample_PhysicalNode_Node = Generalization(general=Node, specific=sample_PhysicalNode)
gen_sample_RemoteNode_PhysicalNode = Generalization(general=PhysicalNode, specific=sample_RemoteNode)
gen_sample_LocalNode_PhysicalNode = Generalization(general=PhysicalNode, specific=sample_LocalNode)
gen_sample_VirtualNode_Node = Generalization(general=Node, specific=sample_VirtualNode)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_ETypes, sample_TypeMap, sample_TypeMapReference, sample_StringMap, sample_DataTypeMap, sample_Type, sample_Value, sample_PrimaryObject, sample_TargetObject, sample_Tree, sample_Node, sample_Comment, sample_PhysicalNode, Node, sample_RemoteNode, PhysicalNode, sample_LocalNode, sample_VirtualNode, SomeKind},
    associations={values0, valuesWithReferences1, stringValues3, dataTypeValues5, key7, value9, key11, value13, featureMapReferenceType233, unsettableReference15, singleReference18, manyReferences21, singleContainmentReference24, manyContainmentReferences27, featureMapReferenceType130, singleReference36, manyReferences39, parentProxy61, tree63, nodes42, parent44, children46, manyReference48, children50, childrenProxies54, parent57, manyContainmentReference65},
    generalizations={gen_sample_PhysicalNode_Node, gen_sample_RemoteNode_PhysicalNode, gen_sample_LocalNode_PhysicalNode, gen_sample_VirtualNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)