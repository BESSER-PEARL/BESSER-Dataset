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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

# Classes
cmof_ReflectiveSequence = Class(name="cmof::ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
cmof_ReflectiveCollection = Class(name="cmof::ReflectiveCollection")
Object = Class(name="Object")
cmof_Object = Class(name="cmof::Object")
cmof_Property = Class(name="cmof::Property")
StructuralFeature = Class(name="StructuralFeature")
cmof_Class = Class(name="cmof::Class")
cmof_DataType = Class(name="cmof::DataType")
cmof_Association = Class(name="cmof::Association")
cmof_ValueSpecification = Class(name="cmof::ValueSpecification", is_abstract=True)
cmof_StructuralFeature = Class(name="cmof::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
TypedElement = Class(name="TypedElement")
cmof_Feature = Class(name="cmof::Feature", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
cmof_Classifier = Class(name="cmof::Classifier", is_abstract=True)
cmof_RedefinableElement = Class(name="cmof::RedefinableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
cmof_NamedElement = Class(name="cmof::NamedElement", is_abstract=True)
Element = Class(name="Element")
cmof_Namespace = Class(name="cmof::Namespace", is_abstract=True)
cmof_Element = Class(name="cmof::Element", is_abstract=True)
cmof_Comment = Class(name="cmof::Comment")
Classifier = Class(name="Classifier")
cmof_Operation = Class(name="cmof::Operation")
Namespace = Class(name="Namespace")
Type = Class(name="Type")
cmof_Generalization = Class(name="cmof::Generalization")
cmof_Type = Class(name="cmof::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
cmof_Package = Class(name="cmof::Package")
cmof_PackageableElement = Class(name="cmof::PackageableElement", is_abstract=True)
cmof_PackageMerge = Class(name="cmof::PackageMerge")
cmof_ElementImport = Class(name="cmof::ElementImport")
cmof_Constraint = Class(name="cmof::Constraint")
cmof_PackageImport = Class(name="cmof::PackageImport")
DirectedRelationship = Class(name="DirectedRelationship")
cmof_DirectedRelationship = Class(name="cmof::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
cmof_Relationship = Class(name="cmof::Relationship", is_abstract=True)
cmof_TypedElement = Class(name="cmof::TypedElement", is_abstract=True)
BehavioralFeature = Class(name="BehavioralFeature")
cmof_BehavioralFeature = Class(name="cmof::BehavioralFeature", is_abstract=True)
cmof_MultiplicityElement = Class(name="cmof::MultiplicityElement", is_abstract=True)
cmof_Parameter = Class(name="cmof::Parameter")
cmof_Argument = Class(name="cmof::Argument")
cmof_Enumeration = Class(name="cmof::Enumeration")
DataType = Class(name="DataType")
cmof_EnumerationLiteral = Class(name="cmof::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
cmof_InstanceSpecification = Class(name="cmof::InstanceSpecification")
cmof_Slot = Class(name="cmof::Slot")
LiteralSpecification = Class(name="LiteralSpecification")
cmof_Expression = Class(name="cmof::Expression")
ValueSpecification = Class(name="ValueSpecification")
cmof_InstanceValue = Class(name="cmof::InstanceValue")
cmof_LiteralBoolean = Class(name="cmof::LiteralBoolean")
cmof_LiteralReal = Class(name="cmof::LiteralReal")
cmof_LiteralSpecification = Class(name="cmof::LiteralSpecification", is_abstract=True)
cmof_LiteralInteger = Class(name="cmof::LiteralInteger")
cmof_LiteralNull = Class(name="cmof::LiteralNull")
cmof_LiteralUnlimitedNatural = Class(name="cmof::LiteralUnlimitedNatural")
cmof_LiteralString = Class(name="cmof::LiteralString")
cmof_OpaqueExpression = Class(name="cmof::OpaqueExpression")
cmof_PrimitiveType = Class(name="cmof::PrimitiveType")
cmof_URIExtent = Class(name="cmof::URIExtent")
Extent = Class(name="Extent")
cmof_Extent = Class(name="cmof::Extent")
cmof_Factory = Class(name="cmof::Factory")
cmof_Link = Class(name="cmof::Link")
cmof_Tag = Class(name="cmof::Tag")
cmof_Exception = Class(name="cmof::Exception")

# cmof_ReflectiveSequence class attributes and methods
cmof_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='object'), Parameter(name='index')})
cmof_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='index')}, type=StringType)
cmof_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='index')}, type=StringType)
cmof_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='index'), Parameter(name='object')}, type=StringType)
cmof_ReflectiveSequence.methods={cmof_ReflectiveSequence_m_get, cmof_ReflectiveSequence_m_remove, cmof_ReflectiveSequence_m_add, cmof_ReflectiveSequence_m_set}

# ReflectiveCollection class attributes and methods

# cmof_ReflectiveCollection class attributes and methods
cmof_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='object')}, type=StringType)
cmof_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='objects')}, type=StringType)
cmof_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
cmof_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='object')}, type=StringType)
cmof_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
cmof_ReflectiveCollection.methods={cmof_ReflectiveCollection_m_addAll, cmof_ReflectiveCollection_m_size, cmof_ReflectiveCollection_m_remove, cmof_ReflectiveCollection_m_add, cmof_ReflectiveCollection_m_clear}

# Object class attributes and methods

# cmof_Object class attributes and methods
cmof_Object_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=Object)
cmof_Object_m_equals: Method = Method(name="equals", parameters={Parameter(name='element')}, type=StringType)
cmof_Object_m_set: Method = Method(name="set", parameters={Parameter(name='value'), Parameter(name='property')})
cmof_Object_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=StringType)
cmof_Object_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')})
cmof_Object_m_invoke: Method = Method(name="invoke", parameters={Parameter(name='op'), Parameter(name='arguments')}, type=Object)
cmof_Object.methods={cmof_Object_m_get, cmof_Object_m_invoke, cmof_Object_m_set, cmof_Object_m_unset, cmof_Object_m_equals, cmof_Object_m_isSet}

# cmof_Property class attributes and methods
cmof_Property_aggregation: Property = Property(name="aggregation", type=StringType)
cmof_Property_default: Property = Property(name="default", type=StringType)
cmof_Property_isComposite: Property = Property(name="isComposite", type=StringType)
cmof_Property_isDerived: Property = Property(name="isDerived", type=StringType)
cmof_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
cmof_Property_isID: Property = Property(name="isID", type=StringType)
cmof_Property_m_multiplicity_of_composite: Method = Method(name="multiplicity_of_composite", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Property_m_subsetting_context_conforms: Method = Method(name="subsetting_context_conforms", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_derived_union_is_read_only: Method = Method(name="derived_union_is_read_only", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Property_m_redefined_property_inherited: Method = Method(name="redefined_property_inherited", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_subsetted_property_names: Method = Method(name="subsetted_property_names", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_derived_union_is_derived: Method = Method(name="derived_union_is_derived", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Property_m_subsetting_rules: Method = Method(name="subsetting_rules", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_default: Method = Method(name="default", parameters={}, type=StringType)
cmof_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={Parameter(name='p')}, type=StringType)
cmof_Property_m_isComposite: Method = Method(name="isComposite", parameters={}, type=StringType)
cmof_Property_m_isNavigable: Method = Method(name="isNavigable", parameters={}, type=StringType)
cmof_Property_m_opposite: Method = Method(name="opposite", parameters={}, type=StringType)
cmof_Property_m_subsettingContext: Method = Method(name="subsettingContext", parameters={}, type=StringType)
cmof_Property.attributes={cmof_Property_isDerivedUnion, cmof_Property_default, cmof_Property_isID, cmof_Property_isComposite, cmof_Property_isDerived, cmof_Property_aggregation}
cmof_Property.methods={cmof_Property_m_isAttribute, cmof_Property_m_multiplicity_of_composite, cmof_Property_m_derived_union_is_read_only, cmof_Property_m_opposite, cmof_Property_m_isComposite, cmof_Property_m_subsetted_property_names, cmof_Property_m_isNavigable, cmof_Property_m_subsetting_context_conforms, cmof_Property_m_subsettingContext, cmof_Property_m_subsetting_rules, cmof_Property_m_default, cmof_Property_m_redefined_property_inherited, cmof_Property_m_derived_union_is_derived}

# StructuralFeature class attributes and methods

# cmof_Class class attributes and methods
cmof_Class_m_superClass: Method = Method(name="superClass", parameters={}, type=StringType)
cmof_Class.methods={cmof_Class_m_superClass}

# cmof_DataType class attributes and methods

# cmof_Association class attributes and methods
cmof_Association_isDerived: Property = Property(name="isDerived", type=StringType)
cmof_Association_m_specialized_end_types: Method = Method(name="specialized_end_types", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Association_m_binary_associations: Method = Method(name="binary_associations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Association_m_specialized_end_number: Method = Method(name="specialized_end_number", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Association_m_association_ends: Method = Method(name="association_ends", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Association_m_endType: Method = Method(name="endType", parameters={}, type=Type)
cmof_Association.attributes={cmof_Association_isDerived}
cmof_Association.methods={cmof_Association_m_specialized_end_number, cmof_Association_m_association_ends, cmof_Association_m_endType, cmof_Association_m_binary_associations, cmof_Association_m_specialized_end_types}

# cmof_ValueSpecification class attributes and methods
cmof_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=StringType)
cmof_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=StringType)
cmof_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=StringType)
cmof_ValueSpecification_m_realValue: Method = Method(name="realValue", parameters={}, type=StringType)
cmof_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
cmof_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=StringType)
cmof_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=StringType)
cmof_ValueSpecification.methods={cmof_ValueSpecification_m_isNull, cmof_ValueSpecification_m_stringValue, cmof_ValueSpecification_m_realValue, cmof_ValueSpecification_m_unlimitedValue, cmof_ValueSpecification_m_booleanValue, cmof_ValueSpecification_m_isComputable, cmof_ValueSpecification_m_integerValue}

# cmof_StructuralFeature class attributes and methods
cmof_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
cmof_StructuralFeature.attributes={cmof_StructuralFeature_isReadOnly}

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# TypedElement class attributes and methods

# cmof_Feature class attributes and methods
cmof_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
cmof_Feature.attributes={cmof_Feature_isStatic}

# RedefinableElement class attributes and methods

# cmof_Classifier class attributes and methods
cmof_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
cmof_Classifier_isFinalSpecialization: Property = Property(name="isFinalSpecialization", type=StringType)
cmof_Classifier_m_non_final_parents: Method = Method(name="non_final_parents", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Classifier_m_specialize_type: Method = Method(name="specialize_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Classifier_m_no_cycles_in_generalization: Method = Method(name="no_cycles_in_generalization", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=Feature)
cmof_Classifier_m_allParents: Method = Method(name="allParents", parameters={}, type=Classifier)
cmof_Classifier_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
cmof_Classifier_m_general: Method = Method(name="general", parameters={}, type=Classifier)
cmof_Classifier_m_hasVisibilityOf: Method = Method(name="hasVisibilityOf", parameters={Parameter(name='n')}, type=StringType)
cmof_Classifier_m_inherit: Method = Method(name="inherit", parameters={Parameter(name='inhs')}, type=NamedElement)
cmof_Classifier_m_inheritableMembers: Method = Method(name="inheritableMembers", parameters={Parameter(name='c')}, type=NamedElement)
cmof_Classifier_m_inheritedMember: Method = Method(name="inheritedMember", parameters={}, type=NamedElement)
cmof_Classifier_m_maySpecializeType: Method = Method(name="maySpecializeType", parameters={Parameter(name='c')}, type=StringType)
cmof_Classifier_m_parents: Method = Method(name="parents", parameters={}, type=Classifier)
cmof_Classifier.attributes={cmof_Classifier_isFinalSpecialization, cmof_Classifier_isAbstract}
cmof_Classifier.methods={cmof_Classifier_m_general, cmof_Classifier_m_inherit, cmof_Classifier_m_maySpecializeType, cmof_Classifier_m_inheritedMember, cmof_Classifier_m_hasVisibilityOf, cmof_Classifier_m_allParents, cmof_Classifier_m_parents, cmof_Classifier_m_no_cycles_in_generalization, cmof_Classifier_m_inheritableMembers, cmof_Classifier_m_allFeatures, cmof_Classifier_m_conformsTo, cmof_Classifier_m_non_final_parents, cmof_Classifier_m_specialize_type}

# cmof_RedefinableElement class attributes and methods
cmof_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
cmof_RedefinableElement_m_redefinition_consistent: Method = Method(name="redefinition_consistent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_RedefinableElement_m_non_leaf_redefinition: Method = Method(name="non_leaf_redefinition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_RedefinableElement_m_redefinition_context_valid: Method = Method(name="redefinition_context_valid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_RedefinableElement_m_isConsistentWith: Method = Method(name="isConsistentWith", parameters={Parameter(name='redefinee')}, type=StringType)
cmof_RedefinableElement_m_isRedefinitionContextValid: Method = Method(name="isRedefinitionContextValid", parameters={Parameter(name='redefined')}, type=StringType)
cmof_RedefinableElement.attributes={cmof_RedefinableElement_isLeaf}
cmof_RedefinableElement.methods={cmof_RedefinableElement_m_non_leaf_redefinition, cmof_RedefinableElement_m_isRedefinitionContextValid, cmof_RedefinableElement_m_isConsistentWith, cmof_RedefinableElement_m_redefinition_consistent, cmof_RedefinableElement_m_redefinition_context_valid}

# NamedElement class attributes and methods

# cmof_NamedElement class attributes and methods
cmof_NamedElement_name: Property = Property(name="name", type=StringType)
cmof_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
cmof_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
cmof_NamedElement_m_visibility_needs_ownership: Method = Method(name="visibility_needs_ownership", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_NamedElement_m_has_no_qualified_name: Method = Method(name="has_no_qualified_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_NamedElement_m_has_qualified_name: Method = Method(name="has_qualified_name", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=StringType)
cmof_NamedElement_m_isDistinguishableFrom: Method = Method(name="isDistinguishableFrom", parameters={Parameter(name='ns'), Parameter(name='n')}, type=StringType)
cmof_NamedElement_m_qualifiedName: Method = Method(name="qualifiedName", parameters={}, type=StringType)
cmof_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
cmof_NamedElement.attributes={cmof_NamedElement_qualifiedName, cmof_NamedElement_name, cmof_NamedElement_visibility}
cmof_NamedElement.methods={cmof_NamedElement_m_has_no_qualified_name, cmof_NamedElement_m_qualifiedName, cmof_NamedElement_m_allNamespaces, cmof_NamedElement_m_separator, cmof_NamedElement_m_isDistinguishableFrom, cmof_NamedElement_m_has_qualified_name, cmof_NamedElement_m_visibility_needs_ownership}

# Element class attributes and methods

# cmof_Namespace class attributes and methods
cmof_Namespace_m_excludeCollisions: Method = Method(name="excludeCollisions", parameters={Parameter(name='imps')}, type=PackageableElement)
cmof_Namespace_m_getNamesOfMember: Method = Method(name="getNamesOfMember", parameters={Parameter(name='element')}, type=StringType)
cmof_Namespace_m_importMembers: Method = Method(name="importMembers", parameters={Parameter(name='imps')}, type=PackageableElement)
cmof_Namespace_m_importedMember: Method = Method(name="importedMember", parameters={}, type=PackageableElement)
cmof_Namespace_m_membersAreDistinguishable: Method = Method(name="membersAreDistinguishable", parameters={}, type=StringType)
cmof_Namespace_m_members_distinguishable: Method = Method(name="members_distinguishable", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Namespace.methods={cmof_Namespace_m_membersAreDistinguishable, cmof_Namespace_m_excludeCollisions, cmof_Namespace_m_importedMember, cmof_Namespace_m_members_distinguishable, cmof_Namespace_m_getNamesOfMember, cmof_Namespace_m_importMembers}

# cmof_Element class attributes and methods
cmof_Element_m_has_owner: Method = Method(name="has_owner", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Element_m_not_own_self: Method = Method(name="not_own_self", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
cmof_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=StringType)
cmof_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
cmof_Element_m_container: Method = Method(name="container", parameters={}, type=Element)
cmof_Element_m_isInstanceOfType: Method = Method(name="isInstanceOfType", parameters={Parameter(name='type'), Parameter(name='includesSubtypes')}, type=StringType)
cmof_Element_m_delete: Method = Method(name="delete", parameters={})
cmof_Element.methods={cmof_Element_m_container, cmof_Element_m_mustBeOwned, cmof_Element_m_getMetaClass, cmof_Element_m_allOwnedElements, cmof_Element_m_delete, cmof_Element_m_isInstanceOfType, cmof_Element_m_has_owner, cmof_Element_m_not_own_self}

# cmof_Comment class attributes and methods
cmof_Comment_body: Property = Property(name="body", type=StringType)
cmof_Comment.attributes={cmof_Comment_body}

# Classifier class attributes and methods

# cmof_Operation class attributes and methods
cmof_Operation_isOrdered: Property = Property(name="isOrdered", type=StringType)
cmof_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
cmof_Operation_isUnique: Property = Property(name="isUnique", type=StringType)
cmof_Operation_lower: Property = Property(name="lower", type=StringType)
cmof_Operation_upper: Property = Property(name="upper", type=StringType)
cmof_Operation_m_only_body_for_query: Method = Method(name="only_body_for_query", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Operation_m_at_most_one_return: Method = Method(name="at_most_one_return", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Operation_m_isOrdered: Method = Method(name="isOrdered", parameters={}, type=StringType)
cmof_Operation_m_isUnique: Method = Method(name="isUnique", parameters={}, type=StringType)
cmof_Operation_m_lower: Method = Method(name="lower", parameters={}, type=StringType)
cmof_Operation_m_returnResult: Method = Method(name="returnResult", parameters={}, type=StringType)
cmof_Operation_m_type: Method = Method(name="type", parameters={}, type=Type)
cmof_Operation_m_upper: Method = Method(name="upper", parameters={}, type=StringType)
cmof_Operation.attributes={cmof_Operation_isOrdered, cmof_Operation_isQuery, cmof_Operation_upper, cmof_Operation_isUnique, cmof_Operation_lower}
cmof_Operation.methods={cmof_Operation_m_isUnique, cmof_Operation_m_isOrdered, cmof_Operation_m_returnResult, cmof_Operation_m_lower, cmof_Operation_m_at_most_one_return, cmof_Operation_m_type, cmof_Operation_m_upper, cmof_Operation_m_only_body_for_query}

# Namespace class attributes and methods

# Type class attributes and methods

# cmof_Generalization class attributes and methods
cmof_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
cmof_Generalization.attributes={cmof_Generalization_isSubstitutable}

# cmof_Type class attributes and methods
cmof_Type_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
cmof_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
cmof_Type.methods={cmof_Type_m_conformsTo, cmof_Type_m_isInstance}

# PackageableElement class attributes and methods

# cmof_Package class attributes and methods
cmof_Package_URI: Property = Property(name="URI", type=StringType)
cmof_Package_m_elements_public_or_private: Method = Method(name="elements_public_or_private", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Package_m_makesVisible: Method = Method(name="makesVisible", parameters={Parameter(name='el')}, type=StringType)
cmof_Package_m_nestedPackage: Method = Method(name="nestedPackage", parameters={}, type=StringType)
cmof_Package_m_ownedType: Method = Method(name="ownedType", parameters={}, type=Type)
cmof_Package_m_visibleMembers: Method = Method(name="visibleMembers", parameters={}, type=PackageableElement)
cmof_Package.attributes={cmof_Package_URI}
cmof_Package.methods={cmof_Package_m_elements_public_or_private, cmof_Package_m_visibleMembers, cmof_Package_m_makesVisible, cmof_Package_m_ownedType, cmof_Package_m_nestedPackage}

# cmof_PackageableElement class attributes and methods

# cmof_PackageMerge class attributes and methods

# cmof_ElementImport class attributes and methods
cmof_ElementImport_alias: Property = Property(name="alias", type=StringType)
cmof_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
cmof_ElementImport_m_visibility_public_or_private: Method = Method(name="visibility_public_or_private", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_ElementImport_m_imported_element_is_public: Method = Method(name="imported_element_is_public", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_ElementImport_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
cmof_ElementImport.attributes={cmof_ElementImport_alias, cmof_ElementImport_visibility}
cmof_ElementImport.methods={cmof_ElementImport_m_visibility_public_or_private, cmof_ElementImport_m_imported_element_is_public, cmof_ElementImport_m_getName}

# cmof_Constraint class attributes and methods
cmof_Constraint_m_value_specification_boolean: Method = Method(name="value_specification_boolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Constraint_m_boolean_value: Method = Method(name="boolean_value", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Constraint_m_not_apply_to_self: Method = Method(name="not_apply_to_self", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Constraint_m_no_side_effects: Method = Method(name="no_side_effects", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Constraint.methods={cmof_Constraint_m_boolean_value, cmof_Constraint_m_no_side_effects, cmof_Constraint_m_not_apply_to_self, cmof_Constraint_m_value_specification_boolean}

# cmof_PackageImport class attributes and methods
cmof_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
cmof_PackageImport_m_public_or_private: Method = Method(name="public_or_private", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_PackageImport.attributes={cmof_PackageImport_visibility}
cmof_PackageImport.methods={cmof_PackageImport_m_public_or_private}

# DirectedRelationship class attributes and methods

# cmof_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# cmof_Relationship class attributes and methods

# cmof_TypedElement class attributes and methods

# BehavioralFeature class attributes and methods

# cmof_BehavioralFeature class attributes and methods

# cmof_MultiplicityElement class attributes and methods
cmof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
cmof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
cmof_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
cmof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
cmof_MultiplicityElement_m_lower_ge_0: Method = Method(name="lower_ge_0", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_MultiplicityElement_m_value_specification_no_side_effects: Method = Method(name="value_specification_no_side_effects", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_MultiplicityElement_m_upper_ge_lower: Method = Method(name="upper_ge_lower", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_MultiplicityElement_m_value_specification_constant: Method = Method(name="value_specification_constant", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_MultiplicityElement_m_includesCardinality: Method = Method(name="includesCardinality", parameters={Parameter(name='C')}, type=StringType)
cmof_MultiplicityElement_m_includesMultiplicity: Method = Method(name="includesMultiplicity", parameters={Parameter(name='M')}, type=StringType)
cmof_MultiplicityElement_m_isMultivalued: Method = Method(name="isMultivalued", parameters={}, type=StringType)
cmof_MultiplicityElement_m_lower: Method = Method(name="lower", parameters={}, type=StringType)
cmof_MultiplicityElement_m_lowerBound: Method = Method(name="lowerBound", parameters={}, type=StringType)
cmof_MultiplicityElement_m_upper: Method = Method(name="upper", parameters={}, type=StringType)
cmof_MultiplicityElement_m_upperBound: Method = Method(name="upperBound", parameters={}, type=StringType)
cmof_MultiplicityElement.attributes={cmof_MultiplicityElement_isUnique, cmof_MultiplicityElement_lower, cmof_MultiplicityElement_isOrdered, cmof_MultiplicityElement_upper}
cmof_MultiplicityElement.methods={cmof_MultiplicityElement_m_value_specification_constant, cmof_MultiplicityElement_m_lower, cmof_MultiplicityElement_m_upper_ge_lower, cmof_MultiplicityElement_m_lowerBound, cmof_MultiplicityElement_m_includesMultiplicity, cmof_MultiplicityElement_m_upperBound, cmof_MultiplicityElement_m_value_specification_no_side_effects, cmof_MultiplicityElement_m_lower_ge_0, cmof_MultiplicityElement_m_isMultivalued, cmof_MultiplicityElement_m_upper, cmof_MultiplicityElement_m_includesCardinality}

# cmof_Parameter class attributes and methods
cmof_Parameter_default: Property = Property(name="default", type=StringType)
cmof_Parameter_direction: Property = Property(name="direction", type=StringType)
cmof_Parameter_m_default: Method = Method(name="default", parameters={}, type=StringType)
cmof_Parameter.attributes={cmof_Parameter_direction, cmof_Parameter_default}
cmof_Parameter.methods={cmof_Parameter_m_default}

# cmof_Argument class attributes and methods
cmof_Argument_name: Property = Property(name="name", type=StringType)
cmof_Argument.attributes={cmof_Argument_name}

# cmof_Enumeration class attributes and methods

# DataType class attributes and methods

# cmof_EnumerationLiteral class attributes and methods
cmof_EnumerationLiteral_m_classifier_equals_owning_enumeration: Method = Method(name="classifier_equals_owning_enumeration", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_EnumerationLiteral_m_classifier: Method = Method(name="classifier", parameters={}, type=StringType)
cmof_EnumerationLiteral.methods={cmof_EnumerationLiteral_m_classifier_equals_owning_enumeration, cmof_EnumerationLiteral_m_classifier}

# InstanceSpecification class attributes and methods

# cmof_InstanceSpecification class attributes and methods
cmof_InstanceSpecification_m_defining_feature: Method = Method(name="defining_feature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_InstanceSpecification_m_structural_feature: Method = Method(name="structural_feature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_InstanceSpecification.methods={cmof_InstanceSpecification_m_defining_feature, cmof_InstanceSpecification_m_structural_feature}

# cmof_Slot class attributes and methods

# LiteralSpecification class attributes and methods

# cmof_Expression class attributes and methods
cmof_Expression_symbol: Property = Property(name="symbol", type=StringType)
cmof_Expression.attributes={cmof_Expression_symbol}

# ValueSpecification class attributes and methods

# cmof_InstanceValue class attributes and methods

# cmof_LiteralBoolean class attributes and methods
cmof_LiteralBoolean_value: Property = Property(name="value", type=StringType)
cmof_LiteralBoolean.attributes={cmof_LiteralBoolean_value}

# cmof_LiteralReal class attributes and methods
cmof_LiteralReal_value: Property = Property(name="value", type=StringType)
cmof_LiteralReal.attributes={cmof_LiteralReal_value}

# cmof_LiteralSpecification class attributes and methods

# cmof_LiteralInteger class attributes and methods
cmof_LiteralInteger_value: Property = Property(name="value", type=StringType)
cmof_LiteralInteger.attributes={cmof_LiteralInteger_value}

# cmof_LiteralNull class attributes and methods

# cmof_LiteralUnlimitedNatural class attributes and methods
cmof_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
cmof_LiteralUnlimitedNatural.attributes={cmof_LiteralUnlimitedNatural_value}

# cmof_LiteralString class attributes and methods
cmof_LiteralString_value: Property = Property(name="value", type=StringType)
cmof_LiteralString.attributes={cmof_LiteralString_value}

# cmof_OpaqueExpression class attributes and methods
cmof_OpaqueExpression_body: Property = Property(name="body", type=StringType)
cmof_OpaqueExpression_language: Property = Property(name="language", type=StringType)
cmof_OpaqueExpression_m_isNonNegative: Method = Method(name="isNonNegative", parameters={}, type=StringType)
cmof_OpaqueExpression_m_isPositive: Method = Method(name="isPositive", parameters={}, type=StringType)
cmof_OpaqueExpression_m_value: Method = Method(name="value", parameters={}, type=StringType)
cmof_OpaqueExpression_m_language_body_size: Method = Method(name="language_body_size", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_OpaqueExpression_m_isIntegral: Method = Method(name="isIntegral", parameters={}, type=StringType)
cmof_OpaqueExpression.attributes={cmof_OpaqueExpression_language, cmof_OpaqueExpression_body}
cmof_OpaqueExpression.methods={cmof_OpaqueExpression_m_isIntegral, cmof_OpaqueExpression_m_isNonNegative, cmof_OpaqueExpression_m_isPositive, cmof_OpaqueExpression_m_value, cmof_OpaqueExpression_m_language_body_size}

# cmof_PrimitiveType class attributes and methods

# cmof_URIExtent class attributes and methods
cmof_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
cmof_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='object')}, type=StringType)
cmof_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='uri')}, type=Element)
cmof_URIExtent.methods={cmof_URIExtent_m_element, cmof_URIExtent_m_uri, cmof_URIExtent_m_contextURI}

# Extent class attributes and methods

# cmof_Extent class attributes and methods
cmof_Extent_m_elementsOfType: Method = Method(name="elementsOfType", parameters={Parameter(name='includesSubtypes'), Parameter(name='type')}, type=Element)
cmof_Extent_m_linksOfType: Method = Method(name="linksOfType", parameters={Parameter(name='type')}, type=StringType)
cmof_Extent_m_linkedElements: Method = Method(name="linkedElements", parameters={Parameter(name='end1ToEnd2Direction'), Parameter(name='association'), Parameter(name='endElement')}, type=Element)
cmof_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
cmof_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
cmof_Extent_m_linkExists: Method = Method(name="linkExists", parameters={Parameter(name='firstElement'), Parameter(name='association'), Parameter(name='secondElement')}, type=StringType)
cmof_Extent.methods={cmof_Extent_m_linkedElements, cmof_Extent_m_useContainment, cmof_Extent_m_linksOfType, cmof_Extent_m_elementsOfType, cmof_Extent_m_elements, cmof_Extent_m_linkExists}

# cmof_Factory class attributes and methods
cmof_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='dataType'), Parameter(name='string')}, type=Object)
cmof_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='object'), Parameter(name='dataType')}, type=StringType)
cmof_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=Element)
cmof_Factory_m_createElement: Method = Method(name="createElement", parameters={Parameter(name='class'), Parameter(name='arguments')}, type=Element)
cmof_Factory_m_createLink: Method = Method(name="createLink", parameters={Parameter(name='secondElement'), Parameter(name='firstElement'), Parameter(name='association')}, type=StringType)
cmof_Factory.methods={cmof_Factory_m_createLink, cmof_Factory_m_createFromString, cmof_Factory_m_convertToString, cmof_Factory_m_createElement, cmof_Factory_m_create}

# cmof_Link class attributes and methods
cmof_Link_m_equals: Method = Method(name="equals", parameters={Parameter(name='otherLink')}, type=StringType)
cmof_Link_m_delete: Method = Method(name="delete", parameters={})
cmof_Link.methods={cmof_Link_m_equals, cmof_Link_m_delete}

# cmof_Tag class attributes and methods
cmof_Tag_name: Property = Property(name="name", type=StringType)
cmof_Tag_value: Property = Property(name="value", type=StringType)
cmof_Tag.attributes={cmof_Tag_value, cmof_Tag_name}

# cmof_Exception class attributes and methods
cmof_Exception_description: Property = Property(name="description", type=StringType)
cmof_Exception.attributes={cmof_Exception_description}

# Relationships
class0: BinaryAssociation = BinaryAssociation(
    name="class0",
    ends={
        Property(name="Class", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=cmof_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype1: BinaryAssociation = BinaryAssociation(
    name="datatype1",
    ends={
        Property(name="DataType", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute2", type=cmof_DataType, multiplicity=Multiplicity(0, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Association", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=cmof_Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation4: BinaryAssociation = BinaryAssociation(
    name="owningAssociation4",
    ends={
        Property(name="Association5", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=cmof_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue6: BinaryAssociation = BinaryAssociation(
    name="defaultValue6",
    ends={
        Property(name="cmof_ValueSpecification", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite8: BinaryAssociation = BinaryAssociation(
    name="opposite8",
    ends={
        Property(name="cmof_Property9", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property7", type=cmof_Property, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty11: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty11",
    ends={
        Property(name="cmof_Property12", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property10", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty14: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty14",
    ends={
        Property(name="cmof_Property15", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property13", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier16: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier16",
    ends={
        Property(name="Classifier", type=cmof_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement18: BinaryAssociation = BinaryAssociation(
    name="redefinedElement18",
    ends={
        Property(name="cmof_RedefinableElement", type=cmof_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_RedefinableElement17", type=cmof_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext19: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext19",
    ends={
        Property(name="cmof_Classifier", type=cmof_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_RedefinableElement20", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
namespace21: BinaryAssociation = BinaryAssociation(
    name="namespace21",
    ends={
        Property(name="Namespace", type=cmof_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=cmof_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment22: BinaryAssociation = BinaryAssociation(
    name="ownedComment22",
    ends={
        Property(name="cmof_Comment", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Element", type=cmof_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement24: BinaryAssociation = BinaryAssociation(
    name="ownedElement24",
    ends={
        Property(name="Element", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner26: BinaryAssociation = BinaryAssociation(
    name="owner26",
    ends={
        Property(name="Element27", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=cmof_Element, multiplicity=Multiplicity(0, 1))
    }
)
metaclass28: BinaryAssociation = BinaryAssociation(
    name="metaclass28",
    ends={
        Property(name="cmof_Class", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Element29", type=cmof_Class, multiplicity=Multiplicity(1, 1))
    }
)
annotatedElement30: BinaryAssociation = BinaryAssociation(
    name="annotatedElement30",
    ends={
        Property(name="cmof_Element32", type=cmof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Comment31", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier33: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier33",
    ends={
        Property(name="cmof_Classifier35", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Class34", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute36: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute36",
    ends={
        Property(name="Property", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=cmof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation37: BinaryAssociation = BinaryAssociation(
    name="ownedOperation37",
    ends={
        Property(name="Operation", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class38", type=cmof_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass40: BinaryAssociation = BinaryAssociation(
    name="superClass40",
    ends={
        Property(name="cmof_Class41", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Class39", type=cmof_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attribute42: BinaryAssociation = BinaryAssociation(
    name="attribute42",
    ends={
        Property(name="cmof_Property44", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier43", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
feature45: BinaryAssociation = BinaryAssociation(
    name="feature45",
    ends={
        Property(name="Feature", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=cmof_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
general47: BinaryAssociation = BinaryAssociation(
    name="general47",
    ends={
        Property(name="cmof_Classifier48", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier46", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization49: BinaryAssociation = BinaryAssociation(
    name="generalization49",
    ends={
        Property(name="Generalization", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=cmof_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritedMember50: BinaryAssociation = BinaryAssociation(
    name="inheritedMember50",
    ends={
        Property(name="cmof_NamedElement", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier51", type=cmof_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier53: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier53",
    ends={
        Property(name="cmof_Classifier54", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier52", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
package55: BinaryAssociation = BinaryAssociation(
    name="package55",
    ends={
        Property(name="Package", type=cmof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType.1", type=cmof_Package, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage57: BinaryAssociation = BinaryAssociation(
    name="nestedPackage57",
    ends={
        Property(name="Package58", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=cmof_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage60: BinaryAssociation = BinaryAssociation(
    name="nestingPackage60",
    ends={
        Property(name="Package61", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage.1", type=cmof_Package, multiplicity=Multiplicity(0, 1))
    }
)
packageMerge62: BinaryAssociation = BinaryAssociation(
    name="packageMerge62",
    ends={
        Property(name="PackageMerge", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=cmof_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement63: BinaryAssociation = BinaryAssociation(
    name="packagedElement63",
    ends={
        Property(name="cmof_PackageableElement", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Package", type=cmof_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType64: BinaryAssociation = BinaryAssociation(
    name="ownedType64",
    ends={
        Property(name="Type", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=cmof_Type, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport65: BinaryAssociation = BinaryAssociation(
    name="elementImport65",
    ends={
        Property(name="ElementImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=cmof_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember66: BinaryAssociation = BinaryAssociation(
    name="importedMember66",
    ends={
        Property(name="cmof_PackageableElement67", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Namespace", type=cmof_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member68: BinaryAssociation = BinaryAssociation(
    name="member68",
    ends={
        Property(name="cmof_NamedElement70", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Namespace69", type=cmof_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember71: BinaryAssociation = BinaryAssociation(
    name="ownedMember71",
    ends={
        Property(name="NamedElement", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=cmof_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRule72: BinaryAssociation = BinaryAssociation(
    name="ownedRule72",
    ends={
        Property(name="Constraint", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport73: BinaryAssociation = BinaryAssociation(
    name="packageImport73",
    ends={
        Property(name="PackageImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace74", type=cmof_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement75: BinaryAssociation = BinaryAssociation(
    name="importedElement75",
    ends={
        Property(name="cmof_PackageableElement76", type=cmof_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_ElementImport", type=cmof_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace77: BinaryAssociation = BinaryAssociation(
    name="importingNamespace77",
    ends={
        Property(name="Namespace78", type=cmof_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
source79: BinaryAssociation = BinaryAssociation(
    name="source79",
    ends={
        Property(name="cmof_Element80", type=cmof_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_DirectedRelationship", type=cmof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target81: BinaryAssociation = BinaryAssociation(
    name="target81",
    ends={
        Property(name="cmof_Element83", type=cmof_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_DirectedRelationship82", type=cmof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement84: BinaryAssociation = BinaryAssociation(
    name="relatedElement84",
    ends={
        Property(name="cmof_Element85", type=cmof_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Relationship", type=cmof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
constrainedElement86: BinaryAssociation = BinaryAssociation(
    name="constrainedElement86",
    ends={
        Property(name="cmof_Element87", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Constraint", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification88: BinaryAssociation = BinaryAssociation(
    name="specification88",
    ends={
        Property(name="cmof_ValueSpecification90", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Constraint89", type=cmof_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context91: BinaryAssociation = BinaryAssociation(
    name="context91",
    ends={
        Property(name="Namespace92", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=cmof_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
type93: BinaryAssociation = BinaryAssociation(
    name="type93",
    ends={
        Property(name="cmof_Type", type=cmof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_TypedElement", type=cmof_Type, multiplicity=Multiplicity(0, 1))
    }
)
importedPackage94: BinaryAssociation = BinaryAssociation(
    name="importedPackage94",
    ends={
        Property(name="cmof_Package95", type=cmof_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_PackageImport", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace96: BinaryAssociation = BinaryAssociation(
    name="importingNamespace96",
    ends={
        Property(name="Namespace97", type=cmof_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage98: BinaryAssociation = BinaryAssociation(
    name="mergedPackage98",
    ends={
        Property(name="cmof_Package99", type=cmof_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_PackageMerge", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage100: BinaryAssociation = BinaryAssociation(
    name="receivingPackage100",
    ends={
        Property(name="Package101", type=cmof_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
general102: BinaryAssociation = BinaryAssociation(
    name="general102",
    ends={
        Property(name="cmof_Classifier103", type=cmof_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Generalization", type=cmof_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific104: BinaryAssociation = BinaryAssociation(
    name="specific104",
    ends={
        Property(name="Classifier105", type=cmof_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=cmof_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
bodyCondition106: BinaryAssociation = BinaryAssociation(
    name="bodyCondition106",
    ends={
        Property(name="cmof_Constraint107", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation", type=cmof_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
datatype108: BinaryAssociation = BinaryAssociation(
    name="datatype108",
    ends={
        Property(name="DataType109", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=cmof_DataType, multiplicity=Multiplicity(0, 1))
    }
)
postcondition110: BinaryAssociation = BinaryAssociation(
    name="postcondition110",
    ends={
        Property(name="cmof_Constraint112", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation111", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
precondition113: BinaryAssociation = BinaryAssociation(
    name="precondition113",
    ends={
        Property(name="cmof_Constraint115", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation114", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation117: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation117",
    ends={
        Property(name="cmof_Operation118", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation116", type=cmof_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
type119: BinaryAssociation = BinaryAssociation(
    name="type119",
    ends={
        Property(name="cmof_Type121", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation120", type=cmof_Type, multiplicity=Multiplicity(0, 1))
    }
)
class122: BinaryAssociation = BinaryAssociation(
    name="class122",
    ends={
        Property(name="Class124", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation123", type=cmof_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter125: BinaryAssociation = BinaryAssociation(
    name="ownedParameter125",
    ends={
        Property(name="cmof_BehavioralFeature", type=cmof_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="cmof_Parameter", type=cmof_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
raisedException126: BinaryAssociation = BinaryAssociation(
    name="raisedException126",
    ends={
        Property(name="cmof_Type128", type=cmof_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_BehavioralFeature127", type=cmof_Type, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue129: BinaryAssociation = BinaryAssociation(
    name="defaultValue129",
    ends={
        Property(name="cmof_ValueSpecification131", type=cmof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Parameter130", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation132: BinaryAssociation = BinaryAssociation(
    name="operation132",
    ends={
        Property(name="cmof_Operation134", type=cmof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Parameter133", type=cmof_Operation, multiplicity=Multiplicity(0, 1))
    }
)
lowerValue135: BinaryAssociation = BinaryAssociation(
    name="lowerValue135",
    ends={
        Property(name="cmof_ValueSpecification136", type=cmof_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_MultiplicityElement", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperValue137: BinaryAssociation = BinaryAssociation(
    name="upperValue137",
    ends={
        Property(name="cmof_ValueSpecification139", type=cmof_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_MultiplicityElement138", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAttribute140: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute140",
    ends={
        Property(name="Property141", type=cmof_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=cmof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation142: BinaryAssociation = BinaryAssociation(
    name="ownedOperation142",
    ends={
        Property(name="Operation144", type=cmof_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype143", type=cmof_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedEnd150: BinaryAssociation = BinaryAssociation(
    name="ownedEnd150",
    ends={
        Property(name="Property151", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=cmof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd152: BinaryAssociation = BinaryAssociation(
    name="memberEnd152",
    ends={
        Property(name="Property153", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=cmof_Property, multiplicity=Multiplicity(2, 9999))
    }
)
endType145: BinaryAssociation = BinaryAssociation(
    name="endType145",
    ends={
        Property(name="cmof_Type146", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Association", type=cmof_Type, multiplicity=Multiplicity(1, 9999))
    }
)
navigableOwnedEnd147: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd147",
    ends={
        Property(name="cmof_Property149", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Association148", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
value154: BinaryAssociation = BinaryAssociation(
    name="value154",
    ends={
        Property(name="cmof_Object", type=cmof_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Argument", type=cmof_Object, multiplicity=Multiplicity(1, 1))
    }
)
ownedLiteral155: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral155",
    ends={
        Property(name="EnumerationLiteral", type=cmof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=cmof_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier157: BinaryAssociation = BinaryAssociation(
    name="classifier157",
    ends={
        Property(name="cmof_Classifier158", type=cmof_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_InstanceSpecification", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
enumeration156: BinaryAssociation = BinaryAssociation(
    name="enumeration156",
    ends={
        Property(name="Enumeration", type=cmof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=cmof_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
value164: BinaryAssociation = BinaryAssociation(
    name="value164",
    ends={
        Property(name="cmof_ValueSpecification166", type=cmof_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Slot165", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance167: BinaryAssociation = BinaryAssociation(
    name="owningInstance167",
    ends={
        Property(name="InstanceSpecification", type=cmof_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=cmof_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot159: BinaryAssociation = BinaryAssociation(
    name="slot159",
    ends={
        Property(name="Slot", type=cmof_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=cmof_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification160: BinaryAssociation = BinaryAssociation(
    name="specification160",
    ends={
        Property(name="cmof_ValueSpecification162", type=cmof_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_InstanceSpecification161", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingFeature163: BinaryAssociation = BinaryAssociation(
    name="definingFeature163",
    ends={
        Property(name="cmof_StructuralFeature", type=cmof_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Slot", type=cmof_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
operand168: BinaryAssociation = BinaryAssociation(
    name="operand168",
    ends={
        Property(name="cmof_ValueSpecification169", type=cmof_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Expression", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instance170: BinaryAssociation = BinaryAssociation(
    name="instance170",
    ends={
        Property(name="cmof_InstanceSpecification171", type=cmof_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_InstanceValue", type=cmof_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
association177: BinaryAssociation = BinaryAssociation(
    name="association177",
    ends={
        Property(name="cmof_Association179", type=cmof_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Link178", type=cmof_Association, multiplicity=Multiplicity(1, 1))
    }
)
firstElement172: BinaryAssociation = BinaryAssociation(
    name="firstElement172",
    ends={
        Property(name="cmof_Element173", type=cmof_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Link", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
secondElement174: BinaryAssociation = BinaryAssociation(
    name="secondElement174",
    ends={
        Property(name="cmof_Element176", type=cmof_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Link175", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
elementInError184: BinaryAssociation = BinaryAssociation(
    name="elementInError184",
    ends={
        Property(name="cmof_Element186", type=cmof_Exception, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Exception185", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
element187: BinaryAssociation = BinaryAssociation(
    name="element187",
    ends={
        Property(name="cmof_Element188", type=cmof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Tag", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
package180: BinaryAssociation = BinaryAssociation(
    name="package180",
    ends={
        Property(name="cmof_Package181", type=cmof_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Factory", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
objectInError182: BinaryAssociation = BinaryAssociation(
    name="objectInError182",
    ends={
        Property(name="cmof_Element183", type=cmof_Exception, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Exception", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
tagOwner189: BinaryAssociation = BinaryAssociation(
    name="tagOwner189",
    ends={
        Property(name="cmof_Element191", type=cmof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Tag190", type=cmof_Element, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_cmof_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=cmof_ReflectiveSequence)
gen_cmof_ReflectiveCollection_Object = Generalization(general=Object, specific=cmof_ReflectiveCollection)
gen_cmof_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=cmof_Property)
gen_cmof_StructuralFeature_Feature = Generalization(general=Feature, specific=cmof_StructuralFeature)
gen_cmof_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=cmof_StructuralFeature)
gen_cmof_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=cmof_StructuralFeature)
gen_cmof_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=cmof_Feature)
gen_cmof_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=cmof_RedefinableElement)
gen_cmof_NamedElement_Element = Generalization(general=Element, specific=cmof_NamedElement)
gen_cmof_Element_Object = Generalization(general=Object, specific=cmof_Element)
gen_cmof_Comment_Element = Generalization(general=Element, specific=cmof_Comment)
gen_cmof_Class_Classifier = Generalization(general=Classifier, specific=cmof_Class)
gen_cmof_Classifier_Namespace = Generalization(general=Namespace, specific=cmof_Classifier)
gen_cmof_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=cmof_Classifier)
gen_cmof_Classifier_Type = Generalization(general=Type, specific=cmof_Classifier)
gen_cmof_Type_PackageableElement = Generalization(general=PackageableElement, specific=cmof_Type)
gen_cmof_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=cmof_PackageableElement)
gen_cmof_Package_Namespace = Generalization(general=Namespace, specific=cmof_Package)
gen_cmof_Package_PackageableElement = Generalization(general=PackageableElement, specific=cmof_Package)
gen_cmof_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_ElementImport)
gen_cmof_Namespace_NamedElement = Generalization(general=NamedElement, specific=cmof_Namespace)
gen_cmof_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=cmof_DirectedRelationship)
gen_cmof_Relationship_Element = Generalization(general=Element, specific=cmof_Relationship)
gen_cmof_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=cmof_Constraint)
gen_cmof_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=cmof_ValueSpecification)
gen_cmof_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=cmof_ValueSpecification)
gen_cmof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=cmof_TypedElement)
gen_cmof_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_PackageImport)
gen_cmof_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_Generalization)
gen_cmof_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=cmof_Operation)
gen_cmof_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_PackageMerge)
gen_cmof_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=cmof_BehavioralFeature)
gen_cmof_BehavioralFeature_Feature = Generalization(general=Feature, specific=cmof_BehavioralFeature)
gen_cmof_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=cmof_Parameter)
gen_cmof_Parameter_TypedElement = Generalization(general=TypedElement, specific=cmof_Parameter)
gen_cmof_MultiplicityElement_Element = Generalization(general=Element, specific=cmof_MultiplicityElement)
gen_cmof_DataType_Classifier = Generalization(general=Classifier, specific=cmof_DataType)
gen_cmof_Association_Classifier = Generalization(general=Classifier, specific=cmof_Association)
gen_cmof_Association_Relationship = Generalization(general=Relationship, specific=cmof_Association)
gen_cmof_Enumeration_DataType = Generalization(general=DataType, specific=cmof_Enumeration)
gen_cmof_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=cmof_EnumerationLiteral)
gen_cmof_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=cmof_InstanceSpecification)
gen_cmof_Slot_Element = Generalization(general=Element, specific=cmof_Slot)
gen_cmof_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=cmof_LiteralBoolean)
gen_cmof_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=cmof_Expression)
gen_cmof_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=cmof_InstanceValue)
gen_cmof_LiteralReal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=cmof_LiteralReal)
gen_cmof_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=cmof_LiteralSpecification)
gen_cmof_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=cmof_LiteralInteger)
gen_cmof_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=cmof_LiteralNull)
gen_cmof_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=cmof_LiteralUnlimitedNatural)
gen_cmof_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=cmof_LiteralString)
gen_cmof_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=cmof_OpaqueExpression)
gen_cmof_PrimitiveType_DataType = Generalization(general=DataType, specific=cmof_PrimitiveType)
gen_cmof_URIExtent_Extent = Generalization(general=Extent, specific=cmof_URIExtent)
gen_cmof_Extent_Object = Generalization(general=Object, specific=cmof_Extent)
gen_cmof_Factory_Element = Generalization(general=Element, specific=cmof_Factory)
gen_cmof_Link_Object = Generalization(general=Object, specific=cmof_Link)
gen_cmof_Tag_Element = Generalization(general=Element, specific=cmof_Tag)

# Domain Model
domain_model = DomainModel(
    name="cmof",
    types={cmof_ReflectiveSequence, ReflectiveCollection, cmof_ReflectiveCollection, Object, cmof_Object, cmof_Property, StructuralFeature, cmof_Class, cmof_DataType, cmof_Association, cmof_ValueSpecification, cmof_StructuralFeature, Feature, MultiplicityElement, TypedElement, cmof_Feature, RedefinableElement, cmof_Classifier, cmof_RedefinableElement, NamedElement, cmof_NamedElement, Element, cmof_Namespace, cmof_Element, cmof_Comment, Classifier, cmof_Operation, Namespace, Type, cmof_Generalization, cmof_Type, PackageableElement, cmof_Package, cmof_PackageableElement, cmof_PackageMerge, cmof_ElementImport, cmof_Constraint, cmof_PackageImport, DirectedRelationship, cmof_DirectedRelationship, Relationship, cmof_Relationship, cmof_TypedElement, BehavioralFeature, cmof_BehavioralFeature, cmof_MultiplicityElement, cmof_Parameter, cmof_Argument, cmof_Enumeration, DataType, cmof_EnumerationLiteral, InstanceSpecification, cmof_InstanceSpecification, cmof_Slot, LiteralSpecification, cmof_Expression, ValueSpecification, cmof_InstanceValue, cmof_LiteralBoolean, cmof_LiteralReal, cmof_LiteralSpecification, cmof_LiteralInteger, cmof_LiteralNull, cmof_LiteralUnlimitedNatural, cmof_LiteralString, cmof_OpaqueExpression, cmof_PrimitiveType, cmof_URIExtent, Extent, cmof_Extent, cmof_Factory, cmof_Link, cmof_Tag, cmof_Exception, VisibilityKind, ParameterDirectionKind, AggregationKind},
    associations={class0, datatype1, association3, owningAssociation4, defaultValue6, opposite8, redefinedProperty11, subsettedProperty14, featuringClassifier16, redefinedElement18, redefinitionContext19, namespace21, ownedComment22, ownedElement24, owner26, metaclass28, annotatedElement30, nestedClassifier33, ownedAttribute36, ownedOperation37, superClass40, attribute42, feature45, general47, generalization49, inheritedMember50, redefinedClassifier53, package55, nestedPackage57, nestingPackage60, packageMerge62, packagedElement63, ownedType64, elementImport65, importedMember66, member68, ownedMember71, ownedRule72, packageImport73, importedElement75, importingNamespace77, source79, target81, relatedElement84, constrainedElement86, specification88, context91, type93, importedPackage94, importingNamespace96, mergedPackage98, receivingPackage100, general102, specific104, bodyCondition106, datatype108, postcondition110, precondition113, redefinedOperation117, type119, class122, ownedParameter125, raisedException126, defaultValue129, operation132, lowerValue135, upperValue137, ownedAttribute140, ownedOperation142, ownedEnd150, memberEnd152, endType145, navigableOwnedEnd147, value154, ownedLiteral155, classifier157, enumeration156, value164, owningInstance167, slot159, specification160, definingFeature163, operand168, instance170, association177, firstElement172, secondElement174, elementInError184, element187, package180, objectInError182, tagOwner189},
    generalizations={gen_cmof_ReflectiveSequence_ReflectiveCollection, gen_cmof_ReflectiveCollection_Object, gen_cmof_Property_StructuralFeature, gen_cmof_StructuralFeature_Feature, gen_cmof_StructuralFeature_MultiplicityElement, gen_cmof_StructuralFeature_TypedElement, gen_cmof_Feature_RedefinableElement, gen_cmof_RedefinableElement_NamedElement, gen_cmof_NamedElement_Element, gen_cmof_Element_Object, gen_cmof_Comment_Element, gen_cmof_Class_Classifier, gen_cmof_Classifier_Namespace, gen_cmof_Classifier_RedefinableElement, gen_cmof_Classifier_Type, gen_cmof_Type_PackageableElement, gen_cmof_PackageableElement_NamedElement, gen_cmof_Package_Namespace, gen_cmof_Package_PackageableElement, gen_cmof_ElementImport_DirectedRelationship, gen_cmof_Namespace_NamedElement, gen_cmof_DirectedRelationship_Relationship, gen_cmof_Relationship_Element, gen_cmof_Constraint_PackageableElement, gen_cmof_ValueSpecification_TypedElement, gen_cmof_ValueSpecification_PackageableElement, gen_cmof_TypedElement_NamedElement, gen_cmof_PackageImport_DirectedRelationship, gen_cmof_Generalization_DirectedRelationship, gen_cmof_Operation_BehavioralFeature, gen_cmof_PackageMerge_DirectedRelationship, gen_cmof_BehavioralFeature_Namespace, gen_cmof_BehavioralFeature_Feature, gen_cmof_Parameter_MultiplicityElement, gen_cmof_Parameter_TypedElement, gen_cmof_MultiplicityElement_Element, gen_cmof_DataType_Classifier, gen_cmof_Association_Classifier, gen_cmof_Association_Relationship, gen_cmof_Enumeration_DataType, gen_cmof_EnumerationLiteral_InstanceSpecification, gen_cmof_InstanceSpecification_PackageableElement, gen_cmof_Slot_Element, gen_cmof_LiteralBoolean_LiteralSpecification, gen_cmof_Expression_ValueSpecification, gen_cmof_InstanceValue_ValueSpecification, gen_cmof_LiteralReal_LiteralSpecification, gen_cmof_LiteralSpecification_ValueSpecification, gen_cmof_LiteralInteger_LiteralSpecification, gen_cmof_LiteralNull_LiteralSpecification, gen_cmof_LiteralUnlimitedNatural_LiteralSpecification, gen_cmof_LiteralString_LiteralSpecification, gen_cmof_OpaqueExpression_ValueSpecification, gen_cmof_PrimitiveType_DataType, gen_cmof_URIExtent_Extent, gen_cmof_Extent_Object, gen_cmof_Factory_Element, gen_cmof_Link_Object, gen_cmof_Tag_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)