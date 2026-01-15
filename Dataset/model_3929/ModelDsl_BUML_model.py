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
ValueType: Enumeration = Enumeration(
    name="ValueType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="INT_RANGE"),
			EnumerationLiteral(name="FORMAT_RANGE")
    }
)

# Classes
modelDsl_Entity = Class(name="modelDsl::Entity")
modelDsl_Parent = Class(name="modelDsl::Parent")
modelDsl_EntityElements = Class(name="modelDsl::EntityElements")
modelDsl_EntityGroup = Class(name="modelDsl::EntityGroup")
modelDsl_Child = Class(name="modelDsl::Child")
modelDsl_Property = Class(name="modelDsl::Property")
modelDsl_Reference = Class(name="modelDsl::Reference")
modelDsl_ReferenceList = Class(name="modelDsl::ReferenceList")
modelDsl_Model = Class(name="modelDsl::Model")
modelDsl_Import = Class(name="modelDsl::Import")
modelDsl_Element = Class(name="modelDsl::Element")
Annotated = Class(name="Annotated")
modelDsl_Type = Class(name="modelDsl::Type")
Element = Class(name="Element")
modelDsl_AnnotationGroup = Class(name="modelDsl::AnnotationGroup")
modelDsl_Package = Class(name="modelDsl::Package")
modelDsl_DataType = Class(name="modelDsl::DataType")
Type = Class(name="Type")
modelDsl_DataTypeField = Class(name="modelDsl::DataTypeField")
modelDsl_PatternType = Class(name="modelDsl::PatternType")
modelDsl_AnnotationInstance = Class(name="modelDsl::AnnotationInstance")
modelDsl_AnnotationProperty = Class(name="modelDsl::AnnotationProperty")
modelDsl_GroupType = Class(name="modelDsl::GroupType")
AnnotationValue = Class(name="AnnotationValue")
modelDsl_AnnotationValue = Class(name="modelDsl::AnnotationValue")
modelDsl_AnnotationHiddenProperty = Class(name="modelDsl::AnnotationHiddenProperty")
modelDsl_Container = Class(name="modelDsl::Container")
modelDsl_Field = Class(name="modelDsl::Field")
Container = Class(name="Container")
Field = Class(name="Field")
modelDsl_Annotation = Class(name="modelDsl::Annotation")
modelDsl_AnnoTypes = Class(name="modelDsl::AnnoTypes")
modelDsl_DoubleValue = Class(name="modelDsl::DoubleValue")
modelDsl_RangeValue = Class(name="modelDsl::RangeValue")
modelDsl_FormatRangeValue = Class(name="modelDsl::FormatRangeValue")
modelDsl_Value = Class(name="modelDsl::Value")
modelDsl_Annotated = Class(name="modelDsl::Annotated")
AnnoTypes = Class(name="AnnoTypes")
modelDsl_PackageType = Class(name="modelDsl::PackageType")
modelDsl_DataTypeType = Class(name="modelDsl::DataTypeType")
modelDsl_AnnotationType = Class(name="modelDsl::AnnotationType")
modelDsl_EntityType = Class(name="modelDsl::EntityType")
modelDsl_PropertyType = Class(name="modelDsl::PropertyType")
modelDsl_ReferenceType = Class(name="modelDsl::ReferenceType")
modelDsl_ReferenceListType = Class(name="modelDsl::ReferenceListType")
modelDsl_ParentType = Class(name="modelDsl::ParentType")
modelDsl_ChildType = Class(name="modelDsl::ChildType")
modelDsl_StringValue = Class(name="modelDsl::StringValue")
Value = Class(name="Value")
modelDsl_IntegerValue = Class(name="modelDsl::IntegerValue")

# modelDsl_Entity class attributes and methods

# modelDsl_Parent class attributes and methods

# modelDsl_EntityElements class attributes and methods

# modelDsl_EntityGroup class attributes and methods
modelDsl_EntityGroup_name: Property = Property(name="name", type=StringType)
modelDsl_EntityGroup.attributes={modelDsl_EntityGroup_name}

# modelDsl_Child class attributes and methods

# modelDsl_Property class attributes and methods
modelDsl_Property_optional: Property = Property(name="optional", type=BooleanType)
modelDsl_Property.attributes={modelDsl_Property_optional}

# modelDsl_Reference class attributes and methods
modelDsl_Reference_optional: Property = Property(name="optional", type=BooleanType)
modelDsl_Reference.attributes={modelDsl_Reference_optional}

# modelDsl_ReferenceList class attributes and methods

# modelDsl_Model class attributes and methods

# modelDsl_Import class attributes and methods
modelDsl_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
modelDsl_Import.attributes={modelDsl_Import_importedNamespace}

# modelDsl_Element class attributes and methods
modelDsl_Element_name: Property = Property(name="name", type=StringType)
modelDsl_Element.attributes={modelDsl_Element_name}

# Annotated class attributes and methods

# modelDsl_Type class attributes and methods

# Element class attributes and methods

# modelDsl_AnnotationGroup class attributes and methods

# modelDsl_Package class attributes and methods

# modelDsl_DataType class attributes and methods

# Type class attributes and methods

# modelDsl_DataTypeField class attributes and methods
modelDsl_DataTypeField_format: Property = Property(name="format", type=StringType)
modelDsl_DataTypeField.attributes={modelDsl_DataTypeField_format}

# modelDsl_PatternType class attributes and methods
modelDsl_PatternType_REGEX: Property = Property(name="REGEX", type=StringType)
modelDsl_PatternType_DATE: Property = Property(name="DATE", type=StringType)
modelDsl_PatternType_NUMBER: Property = Property(name="NUMBER", type=StringType)
modelDsl_PatternType.attributes={modelDsl_PatternType_DATE, modelDsl_PatternType_NUMBER, modelDsl_PatternType_REGEX}

# modelDsl_AnnotationInstance class attributes and methods

# modelDsl_AnnotationProperty class attributes and methods
modelDsl_AnnotationProperty_name: Property = Property(name="name", type=StringType)
modelDsl_AnnotationProperty_type: Property = Property(name="type", type=StringType)
modelDsl_AnnotationProperty_multi: Property = Property(name="multi", type=BooleanType)
modelDsl_AnnotationProperty.attributes={modelDsl_AnnotationProperty_type, modelDsl_AnnotationProperty_name, modelDsl_AnnotationProperty_multi}

# modelDsl_GroupType class attributes and methods
modelDsl_GroupType_name: Property = Property(name="name", type=StringType)
modelDsl_GroupType.attributes={modelDsl_GroupType_name}

# AnnotationValue class attributes and methods

# modelDsl_AnnotationValue class attributes and methods

# modelDsl_AnnotationHiddenProperty class attributes and methods

# modelDsl_Container class attributes and methods

# modelDsl_Field class attributes and methods
modelDsl_Field_name: Property = Property(name="name", type=StringType)
modelDsl_Field.attributes={modelDsl_Field_name}

# Container class attributes and methods

# Field class attributes and methods

# modelDsl_Annotation class attributes and methods

# modelDsl_AnnoTypes class attributes and methods
modelDsl_AnnoTypes_type: Property = Property(name="type", type=StringType)
modelDsl_AnnoTypes.attributes={modelDsl_AnnoTypes_type}

# modelDsl_DoubleValue class attributes and methods
modelDsl_DoubleValue_value: Property = Property(name="value", type=FloatType)
modelDsl_DoubleValue.attributes={modelDsl_DoubleValue_value}

# modelDsl_RangeValue class attributes and methods
modelDsl_RangeValue_from: Property = Property(name="from", type=IntegerType)
modelDsl_RangeValue_fromInf: Property = Property(name="fromInf", type=BooleanType)
modelDsl_RangeValue_to: Property = Property(name="to", type=IntegerType)
modelDsl_RangeValue_toInf: Property = Property(name="toInf", type=BooleanType)
modelDsl_RangeValue.attributes={modelDsl_RangeValue_fromInf, modelDsl_RangeValue_from, modelDsl_RangeValue_toInf, modelDsl_RangeValue_to}

# modelDsl_FormatRangeValue class attributes and methods
modelDsl_FormatRangeValue_from: Property = Property(name="from", type=StringType)
modelDsl_FormatRangeValue_to: Property = Property(name="to", type=StringType)
modelDsl_FormatRangeValue.attributes={modelDsl_FormatRangeValue_to, modelDsl_FormatRangeValue_from}

# modelDsl_Value class attributes and methods

# modelDsl_Annotated class attributes and methods

# AnnoTypes class attributes and methods

# modelDsl_PackageType class attributes and methods

# modelDsl_DataTypeType class attributes and methods

# modelDsl_AnnotationType class attributes and methods

# modelDsl_EntityType class attributes and methods

# modelDsl_PropertyType class attributes and methods

# modelDsl_ReferenceType class attributes and methods

# modelDsl_ReferenceListType class attributes and methods

# modelDsl_ParentType class attributes and methods

# modelDsl_ChildType class attributes and methods

# modelDsl_StringValue class attributes and methods
modelDsl_StringValue_value: Property = Property(name="value", type=StringType)
modelDsl_StringValue.attributes={modelDsl_StringValue_value}

# Value class attributes and methods

# modelDsl_IntegerValue class attributes and methods
modelDsl_IntegerValue_value: Property = Property(name="value", type=IntegerType)
modelDsl_IntegerValue.attributes={modelDsl_IntegerValue_value}

# Relationships
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="modelDsl_DataType14", type=modelDsl_DataTypeField, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DataTypeField13", type=modelDsl_DataType, multiplicity=Multiplicity(0, 1))
    }
)
parent15: BinaryAssociation = BinaryAssociation(
    name="parent15",
    ends={
        Property(name="modelDsl_Parent", type=modelDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Entity", type=modelDsl_Parent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements16: BinaryAssociation = BinaryAssociation(
    name="elements16",
    ends={
        Property(name="modelDsl_EntityElements", type=modelDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Entity17", type=modelDsl_EntityElements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groups18: BinaryAssociation = BinaryAssociation(
    name="groups18",
    ends={
        Property(name="modelDsl_EntityGroup", type=modelDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Entity19", type=modelDsl_EntityGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements20: BinaryAssociation = BinaryAssociation(
    name="elements20",
    ends={
        Property(name="modelDsl_EntityElements22", type=modelDsl_EntityGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_EntityGroup21", type=modelDsl_EntityElements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childs23: BinaryAssociation = BinaryAssociation(
    name="childs23",
    ends={
        Property(name="modelDsl_Child", type=modelDsl_EntityElements, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_EntityElements24", type=modelDsl_Child, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties25: BinaryAssociation = BinaryAssociation(
    name="properties25",
    ends={
        Property(name="modelDsl_Property", type=modelDsl_EntityElements, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_EntityElements26", type=modelDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references27: BinaryAssociation = BinaryAssociation(
    name="references27",
    ends={
        Property(name="modelDsl_Reference", type=modelDsl_EntityElements, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_EntityElements28", type=modelDsl_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceLists29: BinaryAssociation = BinaryAssociation(
    name="referenceLists29",
    ends={
        Property(name="modelDsl_ReferenceList", type=modelDsl_EntityElements, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_EntityElements30", type=modelDsl_ReferenceList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="modelDsl_Import", type=modelDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Model", type=modelDsl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="modelDsl_Element", type=modelDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Model2", type=modelDsl_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations3: BinaryAssociation = BinaryAssociation(
    name="annotations3",
    ends={
        Property(name="modelDsl_AnnotationGroup", type=modelDsl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Type", type=modelDsl_AnnotationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations4: BinaryAssociation = BinaryAssociation(
    name="annotations4",
    ends={
        Property(name="modelDsl_AnnotationGroup5", type=modelDsl_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Package", type=modelDsl_AnnotationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements6: BinaryAssociation = BinaryAssociation(
    name="elements6",
    ends={
        Property(name="modelDsl_Element8", type=modelDsl_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Package7", type=modelDsl_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formatedFields9: BinaryAssociation = BinaryAssociation(
    name="formatedFields9",
    ends={
        Property(name="modelDsl_DataTypeField", type=modelDsl_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DataType", type=modelDsl_DataTypeField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern10: BinaryAssociation = BinaryAssociation(
    name="pattern10",
    ends={
        Property(name="modelDsl_PatternType", type=modelDsl_DataTypeField, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_DataTypeField11", type=modelDsl_PatternType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types50: BinaryAssociation = BinaryAssociation(
    name="types50",
    ends={
        Property(name="modelDsl_AnnoTypes", type=modelDsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Annotation", type=modelDsl_AnnoTypes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instances51: BinaryAssociation = BinaryAssociation(
    name="instances51",
    ends={
        Property(name="modelDsl_AnnotationInstance", type=modelDsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Annotation52", type=modelDsl_AnnotationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mandatories53: BinaryAssociation = BinaryAssociation(
    name="mandatories53",
    ends={
        Property(name="modelDsl_AnnotationProperty", type=modelDsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Annotation54", type=modelDsl_AnnotationProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionals55: BinaryAssociation = BinaryAssociation(
    name="optionals55",
    ends={
        Property(name="modelDsl_AnnotationProperty57", type=modelDsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Annotation56", type=modelDsl_AnnotationProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group58: BinaryAssociation = BinaryAssociation(
    name="group58",
    ends={
        Property(name="modelDsl_GroupType", type=modelDsl_AnnotationProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationProperty59", type=modelDsl_GroupType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instances60: BinaryAssociation = BinaryAssociation(
    name="instances60",
    ends={
        Property(name="modelDsl_AnnotationInstance62", type=modelDsl_AnnotationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationGroup61", type=modelDsl_AnnotationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation63: BinaryAssociation = BinaryAssociation(
    name="annotation63",
    ends={
        Property(name="modelDsl_Annotation65", type=modelDsl_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationInstance64", type=modelDsl_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
values66: BinaryAssociation = BinaryAssociation(
    name="values66",
    ends={
        Property(name="modelDsl_AnnotationValue", type=modelDsl_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationInstance67", type=modelDsl_AnnotationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties68: BinaryAssociation = BinaryAssociation(
    name="properties68",
    ends={
        Property(name="modelDsl_AnnotationHiddenProperty", type=modelDsl_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationInstance69", type=modelDsl_AnnotationHiddenProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="modelDsl_Entity32", type=modelDsl_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Container", type=modelDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
annotations33: BinaryAssociation = BinaryAssociation(
    name="annotations33",
    ends={
        Property(name="modelDsl_AnnotationGroup35", type=modelDsl_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Container34", type=modelDsl_AnnotationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations36: BinaryAssociation = BinaryAssociation(
    name="annotations36",
    ends={
        Property(name="modelDsl_AnnotationGroup37", type=modelDsl_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Field", type=modelDsl_AnnotationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="modelDsl_Type40", type=modelDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Property39", type=modelDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
entity41: BinaryAssociation = BinaryAssociation(
    name="entity41",
    ends={
        Property(name="modelDsl_Entity43", type=modelDsl_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_Reference42", type=modelDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
reference44: BinaryAssociation = BinaryAssociation(
    name="reference44",
    ends={
        Property(name="modelDsl_Reference46", type=modelDsl_ReferenceList, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_ReferenceList45", type=modelDsl_Reference, multiplicity=Multiplicity(0, 1))
    }
)
entity47: BinaryAssociation = BinaryAssociation(
    name="entity47",
    ends={
        Property(name="modelDsl_Entity49", type=modelDsl_ReferenceList, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_ReferenceList48", type=modelDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
property70: BinaryAssociation = BinaryAssociation(
    name="property70",
    ends={
        Property(name="modelDsl_AnnotationProperty72", type=modelDsl_AnnotationHiddenProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationHiddenProperty71", type=modelDsl_AnnotationProperty, multiplicity=Multiplicity(0, 1))
    }
)
values73: BinaryAssociation = BinaryAssociation(
    name="values73",
    ends={
        Property(name="modelDsl_AnnotationValue75", type=modelDsl_AnnotationHiddenProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="modelDsl_AnnotationHiddenProperty74", type=modelDsl_AnnotationValue, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_modelDsl_Entity_Type = Generalization(general=Type, specific=modelDsl_Entity)
gen_modelDsl_Element_Annotated = Generalization(general=Annotated, specific=modelDsl_Element)
gen_modelDsl_Type_Element = Generalization(general=Element, specific=modelDsl_Type)
gen_modelDsl_Package_Element = Generalization(general=Element, specific=modelDsl_Package)
gen_modelDsl_DataType_Type = Generalization(general=Type, specific=modelDsl_DataType)
gen_modelDsl_AnnotationGroup_AnnotationValue = Generalization(general=AnnotationValue, specific=modelDsl_AnnotationGroup)
gen_modelDsl_AnnotationInstance_Annotated = Generalization(general=Annotated, specific=modelDsl_AnnotationInstance)
gen_modelDsl_Container_Annotated = Generalization(general=Annotated, specific=modelDsl_Container)
gen_modelDsl_Field_Annotated = Generalization(general=Annotated, specific=modelDsl_Field)
gen_modelDsl_Parent_Container = Generalization(general=Container, specific=modelDsl_Parent)
gen_modelDsl_Child_Container = Generalization(general=Container, specific=modelDsl_Child)
gen_modelDsl_Property_Field = Generalization(general=Field, specific=modelDsl_Property)
gen_modelDsl_Reference_Field = Generalization(general=Field, specific=modelDsl_Reference)
gen_modelDsl_ReferenceList_Field = Generalization(general=Field, specific=modelDsl_ReferenceList)
gen_modelDsl_Annotation_Element = Generalization(general=Element, specific=modelDsl_Annotation)
gen_modelDsl_IntegerValue_Value = Generalization(general=Value, specific=modelDsl_IntegerValue)
gen_modelDsl_DoubleValue_Value = Generalization(general=Value, specific=modelDsl_DoubleValue)
gen_modelDsl_RangeValue_Value = Generalization(general=Value, specific=modelDsl_RangeValue)
gen_modelDsl_FormatRangeValue_Value = Generalization(general=Value, specific=modelDsl_FormatRangeValue)
gen_modelDsl_Value_AnnotationValue = Generalization(general=AnnotationValue, specific=modelDsl_Value)
gen_modelDsl_GroupType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_GroupType)
gen_modelDsl_PackageType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_PackageType)
gen_modelDsl_DataTypeType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_DataTypeType)
gen_modelDsl_AnnotationType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_AnnotationType)
gen_modelDsl_EntityType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_EntityType)
gen_modelDsl_PropertyType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_PropertyType)
gen_modelDsl_ReferenceType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_ReferenceType)
gen_modelDsl_ReferenceListType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_ReferenceListType)
gen_modelDsl_ParentType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_ParentType)
gen_modelDsl_ChildType_AnnoTypes = Generalization(general=AnnoTypes, specific=modelDsl_ChildType)
gen_modelDsl_StringValue_Value = Generalization(general=Value, specific=modelDsl_StringValue)

# Domain Model
domain_model = DomainModel(
    name="modelDsl",
    types={modelDsl_Entity, modelDsl_Parent, modelDsl_EntityElements, modelDsl_EntityGroup, modelDsl_Child, modelDsl_Property, modelDsl_Reference, modelDsl_ReferenceList, modelDsl_Model, modelDsl_Import, modelDsl_Element, Annotated, modelDsl_Type, Element, modelDsl_AnnotationGroup, modelDsl_Package, modelDsl_DataType, Type, modelDsl_DataTypeField, modelDsl_PatternType, modelDsl_AnnotationInstance, modelDsl_AnnotationProperty, modelDsl_GroupType, AnnotationValue, modelDsl_AnnotationValue, modelDsl_AnnotationHiddenProperty, modelDsl_Container, modelDsl_Field, Container, Field, modelDsl_Annotation, modelDsl_AnnoTypes, modelDsl_DoubleValue, modelDsl_RangeValue, modelDsl_FormatRangeValue, modelDsl_Value, modelDsl_Annotated, AnnoTypes, modelDsl_PackageType, modelDsl_DataTypeType, modelDsl_AnnotationType, modelDsl_EntityType, modelDsl_PropertyType, modelDsl_ReferenceType, modelDsl_ReferenceListType, modelDsl_ParentType, modelDsl_ChildType, modelDsl_StringValue, Value, modelDsl_IntegerValue, ValueType},
    associations={type12, parent15, elements16, groups18, elements20, childs23, properties25, references27, referenceLists29, imports0, elements1, annotations3, annotations4, elements6, formatedFields9, pattern10, types50, instances51, mandatories53, optionals55, group58, instances60, annotation63, values66, properties68, type31, annotations33, annotations36, type38, entity41, reference44, entity47, property70, values73},
    generalizations={gen_modelDsl_Entity_Type, gen_modelDsl_Element_Annotated, gen_modelDsl_Type_Element, gen_modelDsl_Package_Element, gen_modelDsl_DataType_Type, gen_modelDsl_AnnotationGroup_AnnotationValue, gen_modelDsl_AnnotationInstance_Annotated, gen_modelDsl_Container_Annotated, gen_modelDsl_Field_Annotated, gen_modelDsl_Parent_Container, gen_modelDsl_Child_Container, gen_modelDsl_Property_Field, gen_modelDsl_Reference_Field, gen_modelDsl_ReferenceList_Field, gen_modelDsl_Annotation_Element, gen_modelDsl_IntegerValue_Value, gen_modelDsl_DoubleValue_Value, gen_modelDsl_RangeValue_Value, gen_modelDsl_FormatRangeValue_Value, gen_modelDsl_Value_AnnotationValue, gen_modelDsl_GroupType_AnnoTypes, gen_modelDsl_PackageType_AnnoTypes, gen_modelDsl_DataTypeType_AnnoTypes, gen_modelDsl_AnnotationType_AnnoTypes, gen_modelDsl_EntityType_AnnoTypes, gen_modelDsl_PropertyType_AnnoTypes, gen_modelDsl_ReferenceType_AnnoTypes, gen_modelDsl_ReferenceListType_AnnoTypes, gen_modelDsl_ParentType_AnnoTypes, gen_modelDsl_ChildType_AnnoTypes, gen_modelDsl_StringValue_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)