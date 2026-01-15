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

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

# Classes
cmof_Classifier = Class(name="cmof::Classifier", is_abstract=True)
Namespace = Class(name="Namespace")
Type = Class(name="Type")
cmof_NamedElement = Class(name="cmof::NamedElement", is_abstract=True)
cmof_Feature = Class(name="cmof::Feature", is_abstract=True)
cmof_Property = Class(name="cmof::Property")
cmof_Namespace = Class(name="cmof::Namespace", is_abstract=True)
NamedElement = Class(name="NamedElement")
cmof_PackageImport = Class(name="cmof::PackageImport")
cmof_Constraint = Class(name="cmof::Constraint")
cmof_PackageableElement = Class(name="cmof::PackageableElement", is_abstract=True)
cmof_ElementImport = Class(name="cmof::ElementImport")
Element = Class(name="Element")
cmof_Element = Class(name="cmof::Element", is_abstract=True)
cmof_Comment = Class(name="cmof::Comment")
cmof_Operation = Class(name="cmof::Operation")
cmof_Class = Class(name="cmof::Class")
Classifier = Class(name="Classifier")
StructuralFeature = Class(name="StructuralFeature")
MultiplicityElement = Class(name="MultiplicityElement")
cmof_DataType = Class(name="cmof::DataType")
cmof_Association = Class(name="cmof::Association")
TypedElement = Class(name="TypedElement")
RedefinableElement = Class(name="RedefinableElement")
cmof_StructuralFeature = Class(name="cmof::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
cmof_RedefinableElement = Class(name="cmof::RedefinableElement", is_abstract=True)
cmof_TypedElement = Class(name="cmof::TypedElement", is_abstract=True)
cmof_Type = Class(name="cmof::Type", is_abstract=True)
PackageableElement = Class(name="PackageableElement")
cmof_Package = Class(name="cmof::Package")
cmof_PackageMerge = Class(name="cmof::PackageMerge")
DirectedRelationship = Class(name="DirectedRelationship")
cmof_DirectedRelationship = Class(name="cmof::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
cmof_Relationship = Class(name="cmof::Relationship", is_abstract=True)
cmof_MultiplicityElement = Class(name="cmof::MultiplicityElement", is_abstract=True)
BehavioralFeature = Class(name="BehavioralFeature")
cmof_BehavioralFeature = Class(name="cmof::BehavioralFeature", is_abstract=True)
cmof_Parameter = Class(name="cmof::Parameter")
cmof_ValueSpecification = Class(name="cmof::ValueSpecification", is_abstract=True)
cmof_Argument = Class(name="cmof::Argument")
cmof_OpaqueExpression = Class(name="cmof::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
cmof_PrimitiveType = Class(name="cmof::PrimitiveType")
cmof_Expression = Class(name="cmof::Expression")
cmof_Enumeration = Class(name="cmof::Enumeration")
DataType = Class(name="DataType")
cmof_EnumerationLiteral = Class(name="cmof::EnumerationLiteral")
cmof_Exception = Class(name="cmof::Exception")
cmof_Factory = Class(name="cmof::Factory")
cmof_Link = Class(name="cmof::Link")
cmof_Tag = Class(name="cmof::Tag")

# cmof_Classifier class attributes and methods
cmof_Classifier_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=BooleanType)
cmof_Classifier_m_no_cycles_in_generalization: Method = Method(name="no_cycles_in_generalization", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Classifier_m_specialize_type: Method = Method(name="specialize_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Classifier_m_hasVisibilityOf: Method = Method(name="hasVisibilityOf", parameters={Parameter(name='n')}, type=BooleanType)
cmof_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=StringType)
cmof_Classifier_m_getGenerals: Method = Method(name="getGenerals", parameters={}, type=StringType)
cmof_Classifier_m_parents: Method = Method(name="parents", parameters={}, type=StringType)
cmof_Classifier_m_getInheritedMembers: Method = Method(name="getInheritedMembers", parameters={}, type=StringType)
cmof_Classifier_m_allParents: Method = Method(name="allParents", parameters={}, type=StringType)
cmof_Classifier_m_inheritableMembers: Method = Method(name="inheritableMembers", parameters={Parameter(name='c')}, type=StringType)
cmof_Classifier_m_inherit: Method = Method(name="inherit", parameters={Parameter(name='inhs')}, type=StringType)
cmof_Classifier_m_maySpecializeType: Method = Method(name="maySpecializeType", parameters={Parameter(name='c')}, type=BooleanType)
cmof_Classifier.methods={cmof_Classifier_m_allFeatures, cmof_Classifier_m_inherit, cmof_Classifier_m_getInheritedMembers, cmof_Classifier_m_getGenerals, cmof_Classifier_m_conformsTo, cmof_Classifier_m_no_cycles_in_generalization, cmof_Classifier_m_parents, cmof_Classifier_m_allParents, cmof_Classifier_m_inheritableMembers, cmof_Classifier_m_maySpecializeType, cmof_Classifier_m_hasVisibilityOf, cmof_Classifier_m_specialize_type}

# Namespace class attributes and methods

# Type class attributes and methods

# cmof_NamedElement class attributes and methods
cmof_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
cmof_NamedElement_name: Property = Property(name="name", type=StringType)
cmof_NamedElement_m_visibility_needs_ownership: Method = Method(name="visibility_needs_ownership", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=Namespace)
cmof_NamedElement_m_no_name: Method = Method(name="no_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_NamedElement_m_qualified_name: Method = Method(name="qualified_name", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_NamedElement_m_isDistinguishableFrom: Method = Method(name="isDistinguishableFrom", parameters={Parameter(name='n'), Parameter(name='ns')}, type=BooleanType)
cmof_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
cmof_NamedElement_m_qualifiedName: Method = Method(name="qualifiedName", parameters={}, type=StringType)
cmof_NamedElement.attributes={cmof_NamedElement_name, cmof_NamedElement_visibility}
cmof_NamedElement.methods={cmof_NamedElement_m_separator, cmof_NamedElement_m_visibility_needs_ownership, cmof_NamedElement_m_allNamespaces, cmof_NamedElement_m_qualified_name, cmof_NamedElement_m_qualifiedName, cmof_NamedElement_m_no_name, cmof_NamedElement_m_isDistinguishableFrom}

# cmof_Feature class attributes and methods

# cmof_Property class attributes and methods
cmof_Property_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
cmof_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
cmof_Property_default: Property = Property(name="default", type=StringType)
cmof_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
cmof_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
cmof_Property_isID: Property = Property(name="isID", type=BooleanType)
cmof_Property_m_navigable_property_redefinition: Method = Method(name="navigable_property_redefinition", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Property_m_subsetting_rules: Method = Method(name="subsetting_rules", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_multiplicity_of_composite: Method = Method(name="multiplicity_of_composite", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Property_m_subsetting_context: Method = Method(name="subsetting_context", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_subsettingContext: Method = Method(name="subsettingContext", parameters={}, type=Classifier)
cmof_Property_m_isNavigable: Method = Method(name="isNavigable", parameters={}, type=BooleanType)
cmof_Property_m_navigable_readonly: Method = Method(name="navigable_readonly", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Property_m_derived_union_is_derived: Method = Method(name="derived_union_is_derived", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Property_m_getOpposite: Method = Method(name="getOpposite", parameters={}, type=StringType)
cmof_Property.attributes={cmof_Property_isID, cmof_Property_isDerivedUnion, cmof_Property_isReadOnly, cmof_Property_isComposite, cmof_Property_default, cmof_Property_isDerived}
cmof_Property.methods={cmof_Property_m_navigable_property_redefinition, cmof_Property_m_multiplicity_of_composite, cmof_Property_m_subsettingContext, cmof_Property_m_subsetting_context, cmof_Property_m_getOpposite, cmof_Property_m_isNavigable, cmof_Property_m_navigable_readonly, cmof_Property_m_derived_union_is_derived, cmof_Property_m_subsetting_rules}

# cmof_Namespace class attributes and methods
cmof_Namespace_m_importMembers: Method = Method(name="importMembers", parameters={Parameter(name='imps')}, type=StringType)
cmof_Namespace_m_members_are_distinguishable: Method = Method(name="members_are_distinguishable", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Namespace_m_getImportedMembers: Method = Method(name="getImportedMembers", parameters={}, type=StringType)
cmof_Namespace_m_getNamesOfMember: Method = Method(name="getNamesOfMember", parameters={Parameter(name='element')}, type=StringType)
cmof_Namespace_m_excludeCollisions: Method = Method(name="excludeCollisions", parameters={Parameter(name='imps')}, type=StringType)
cmof_Namespace_m_membersAreDistinguishable: Method = Method(name="membersAreDistinguishable", parameters={}, type=BooleanType)
cmof_Namespace.methods={cmof_Namespace_m_members_are_distinguishable, cmof_Namespace_m_getImportedMembers, cmof_Namespace_m_getNamesOfMember, cmof_Namespace_m_membersAreDistinguishable, cmof_Namespace_m_importMembers, cmof_Namespace_m_excludeCollisions}

# NamedElement class attributes and methods

# cmof_PackageImport class attributes and methods
cmof_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
cmof_PackageImport_m_public_or_private: Method = Method(name="public_or_private", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_PackageImport.attributes={cmof_PackageImport_visibility}
cmof_PackageImport.methods={cmof_PackageImport_m_public_or_private}

# cmof_Constraint class attributes and methods
cmof_Constraint_m_value_specification_boolean: Method = Method(name="value_specification_boolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Constraint_m_not_apply_to_self: Method = Method(name="not_apply_to_self", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Constraint.methods={cmof_Constraint_m_not_apply_to_self, cmof_Constraint_m_value_specification_boolean}

# cmof_PackageableElement class attributes and methods

# cmof_ElementImport class attributes and methods
cmof_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
cmof_ElementImport_alias: Property = Property(name="alias", type=StringType)
cmof_ElementImport_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
cmof_ElementImport_m_visibility_public_or_private: Method = Method(name="visibility_public_or_private", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_ElementImport_m_imported_element_is_public: Method = Method(name="imported_element_is_public", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_ElementImport.attributes={cmof_ElementImport_visibility, cmof_ElementImport_alias}
cmof_ElementImport.methods={cmof_ElementImport_m_getName, cmof_ElementImport_m_imported_element_is_public, cmof_ElementImport_m_visibility_public_or_private}

# Element class attributes and methods

# cmof_Element class attributes and methods
cmof_Element_m_not_own_self: Method = Method(name="not_own_self", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=BooleanType)
cmof_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')}, type=StringType)
cmof_Element_m_has_owner: Method = Method(name="has_owner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
cmof_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=BooleanType)
cmof_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
cmof_Element_m_container: Method = Method(name="container", parameters={}, type=Element)
cmof_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='otherElement')}, type=BooleanType)
cmof_Element_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=StringType)
cmof_Element_m_set: Method = Method(name="set", parameters={Parameter(name='value'), Parameter(name='property')}, type=StringType)
cmof_Element_m_delete: Method = Method(name="delete", parameters={}, type=StringType)
cmof_Element_m_invoke: Method = Method(name="invoke", parameters={Parameter(name='arguments'), Parameter(name='op')}, type=StringType)
cmof_Element_m_isInstanceOfType: Method = Method(name="isInstanceOfType", parameters={Parameter(name='type'), Parameter(name='includeSubtypes')}, type=BooleanType)
cmof_Element_m_verify: Method = Method(name="verify", parameters={Parameter(name='deepVerify')}, type=StringType)
cmof_Element.methods={cmof_Element_m_unset, cmof_Element_m_equals, cmof_Element_m_delete, cmof_Element_m_container, cmof_Element_m_verify, cmof_Element_m_invoke, cmof_Element_m_set, cmof_Element_m_allOwnedElements, cmof_Element_m_get, cmof_Element_m_not_own_self, cmof_Element_m_isSet, cmof_Element_m_isInstanceOfType, cmof_Element_m_mustBeOwned, cmof_Element_m_has_owner, cmof_Element_m_getMetaClass}

# cmof_Comment class attributes and methods
cmof_Comment_body: Property = Property(name="body", type=StringType)
cmof_Comment.attributes={cmof_Comment_body}

# cmof_Operation class attributes and methods
cmof_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
cmof_Operation_m_returnResult: Method = Method(name="returnResult", parameters={}, type=StringType)
cmof_Operation_m_only_body_for_query: Method = Method(name="only_body_for_query", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Operation_m_at_most_one_return: Method = Method(name="at_most_one_return", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Operation_m_isOrdered: Method = Method(name="isOrdered", parameters={}, type=BooleanType)
cmof_Operation_m_isUnique: Method = Method(name="isUnique", parameters={}, type=BooleanType)
cmof_Operation_m_getType: Method = Method(name="getType", parameters={}, type=Type)
cmof_Operation.attributes={cmof_Operation_isQuery}
cmof_Operation.methods={cmof_Operation_m_isOrdered, cmof_Operation_m_only_body_for_query, cmof_Operation_m_getType, cmof_Operation_m_isUnique, cmof_Operation_m_returnResult, cmof_Operation_m_at_most_one_return}

# cmof_Class class attributes and methods
cmof_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
cmof_Class.attributes={cmof_Class_isAbstract}

# Classifier class attributes and methods

# StructuralFeature class attributes and methods

# MultiplicityElement class attributes and methods

# cmof_DataType class attributes and methods

# cmof_Association class attributes and methods
cmof_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
cmof_Association_m_association_ends: Method = Method(name="association_ends", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_Association.attributes={cmof_Association_isDerived}
cmof_Association.methods={cmof_Association_m_association_ends}

# TypedElement class attributes and methods

# RedefinableElement class attributes and methods

# cmof_StructuralFeature class attributes and methods

# Feature class attributes and methods

# cmof_RedefinableElement class attributes and methods
cmof_RedefinableElement_m_isRedefinitionContextValid: Method = Method(name="isRedefinitionContextValid", parameters={Parameter(name='redefinable')}, type=BooleanType)
cmof_RedefinableElement_m_redefinition_context_valid: Method = Method(name="redefinition_context_valid", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_RedefinableElement_m_redefinition_consistent: Method = Method(name="redefinition_consistent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_RedefinableElement_m_isConsistentWith: Method = Method(name="isConsistentWith", parameters={Parameter(name='redefinee')}, type=BooleanType)
cmof_RedefinableElement.methods={cmof_RedefinableElement_m_isRedefinitionContextValid, cmof_RedefinableElement_m_isConsistentWith, cmof_RedefinableElement_m_redefinition_context_valid, cmof_RedefinableElement_m_redefinition_consistent}

# cmof_TypedElement class attributes and methods

# cmof_Type class attributes and methods
cmof_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
cmof_Type_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=BooleanType)
cmof_Type.methods={cmof_Type_m_conformsTo, cmof_Type_m_isInstance}

# PackageableElement class attributes and methods

# cmof_Package class attributes and methods
cmof_Package_uRI: Property = Property(name="uRI", type=StringType)
cmof_Package_m_makesVisible: Method = Method(name="makesVisible", parameters={Parameter(name='el')}, type=BooleanType)
cmof_Package_m_elements_public_or_private: Method = Method(name="elements_public_or_private", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_Package_m_visibleMembers: Method = Method(name="visibleMembers", parameters={}, type=PackageableElement)
cmof_Package.attributes={cmof_Package_uRI}
cmof_Package.methods={cmof_Package_m_makesVisible, cmof_Package_m_elements_public_or_private, cmof_Package_m_visibleMembers}

# cmof_PackageMerge class attributes and methods

# DirectedRelationship class attributes and methods

# cmof_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# cmof_Relationship class attributes and methods

# cmof_MultiplicityElement class attributes and methods
cmof_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
cmof_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
cmof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
cmof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
cmof_MultiplicityElement_m_lowerBound: Method = Method(name="lowerBound", parameters={}, type=IntegerType)
cmof_MultiplicityElement_m_upper_gt_0: Method = Method(name="upper_gt_0", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
cmof_MultiplicityElement_m_lower_ge_0: Method = Method(name="lower_ge_0", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_MultiplicityElement_m_upper_ge_lower: Method = Method(name="upper_ge_lower", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
cmof_MultiplicityElement_m_upperBound: Method = Method(name="upperBound", parameters={}, type=IntegerType)
cmof_MultiplicityElement_m_isMultivalued: Method = Method(name="isMultivalued", parameters={}, type=BooleanType)
cmof_MultiplicityElement_m_includesCardinality: Method = Method(name="includesCardinality", parameters={Parameter(name='C')}, type=BooleanType)
cmof_MultiplicityElement_m_includesMultiplicity: Method = Method(name="includesMultiplicity", parameters={Parameter(name='M')}, type=BooleanType)
cmof_MultiplicityElement.attributes={cmof_MultiplicityElement_upper, cmof_MultiplicityElement_isUnique, cmof_MultiplicityElement_isOrdered, cmof_MultiplicityElement_lower}
cmof_MultiplicityElement.methods={cmof_MultiplicityElement_m_lower_ge_0, cmof_MultiplicityElement_m_isMultivalued, cmof_MultiplicityElement_m_upper_gt_0, cmof_MultiplicityElement_m_includesCardinality, cmof_MultiplicityElement_m_upperBound, cmof_MultiplicityElement_m_lowerBound, cmof_MultiplicityElement_m_includesMultiplicity, cmof_MultiplicityElement_m_upper_ge_lower}

# BehavioralFeature class attributes and methods

# cmof_BehavioralFeature class attributes and methods

# cmof_Parameter class attributes and methods
cmof_Parameter_direction: Property = Property(name="direction", type=StringType)
cmof_Parameter_default: Property = Property(name="default", type=StringType)
cmof_Parameter.attributes={cmof_Parameter_default, cmof_Parameter_direction}

# cmof_ValueSpecification class attributes and methods
cmof_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=IntegerType)
cmof_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=BooleanType)
cmof_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
cmof_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=IntegerType)
cmof_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=BooleanType)
cmof_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=BooleanType)
cmof_ValueSpecification.methods={cmof_ValueSpecification_m_integerValue, cmof_ValueSpecification_m_stringValue, cmof_ValueSpecification_m_isNull, cmof_ValueSpecification_m_isComputable, cmof_ValueSpecification_m_booleanValue, cmof_ValueSpecification_m_unlimitedValue}

# cmof_Argument class attributes and methods
cmof_Argument_name: Property = Property(name="name", type=StringType)
cmof_Argument_value: Property = Property(name="value", type=StringType)
cmof_Argument.attributes={cmof_Argument_value, cmof_Argument_name}

# cmof_OpaqueExpression class attributes and methods
cmof_OpaqueExpression_body: Property = Property(name="body", type=StringType)
cmof_OpaqueExpression_language: Property = Property(name="language", type=StringType)
cmof_OpaqueExpression.attributes={cmof_OpaqueExpression_language, cmof_OpaqueExpression_body}

# ValueSpecification class attributes and methods

# cmof_PrimitiveType class attributes and methods

# cmof_Expression class attributes and methods

# cmof_Enumeration class attributes and methods

# DataType class attributes and methods

# cmof_EnumerationLiteral class attributes and methods

# cmof_Exception class attributes and methods
cmof_Exception_description: Property = Property(name="description", type=StringType)
cmof_Exception.attributes={cmof_Exception_description}

# cmof_Factory class attributes and methods
cmof_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='string'), Parameter(name='dataType')}, type=StringType)
cmof_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='object'), Parameter(name='dataType')}, type=StringType)
cmof_Factory_m_createElement: Method = Method(name="createElement", parameters={Parameter(name='arguments'), Parameter(name='aClass')}, type=Element)
cmof_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=Element)
cmof_Factory_m_createLink: Method = Method(name="createLink", parameters={Parameter(name='secondElement'), Parameter(name='firstElement'), Parameter(name='association')}, type=StringType)
cmof_Factory.methods={cmof_Factory_m_createElement, cmof_Factory_m_createFromString, cmof_Factory_m_createLink, cmof_Factory_m_convertToString, cmof_Factory_m_create}

# cmof_Link class attributes and methods
cmof_Link_m_equals: Method = Method(name="equals", parameters={Parameter(name='otherLink')}, type=BooleanType)
cmof_Link_m_delete: Method = Method(name="delete", parameters={}, type=StringType)
cmof_Link.methods={cmof_Link_m_delete, cmof_Link_m_equals}

# cmof_Tag class attributes and methods
cmof_Tag_name: Property = Property(name="name", type=StringType)
cmof_Tag_value: Property = Property(name="value", type=StringType)
cmof_Tag.attributes={cmof_Tag_name, cmof_Tag_value}

# Relationships
general3: BinaryAssociation = BinaryAssociation(
    name="general3",
    ends={
        Property(name="cmof_Classifier4", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier2", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember5: BinaryAssociation = BinaryAssociation(
    name="inheritedMember5",
    ends={
        Property(name="cmof_NamedElement", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier6", type=cmof_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature0: BinaryAssociation = BinaryAssociation(
    name="feature0",
    ends={
        Property(name="Feature", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=cmof_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="cmof_Property", type=cmof_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Classifier", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
packageImport10: BinaryAssociation = BinaryAssociation(
    name="packageImport10",
    ends={
        Property(name="PackageImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace11", type=cmof_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule7: BinaryAssociation = BinaryAssociation(
    name="ownedRule7",
    ends={
        Property(name="Constraint", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedMember8: BinaryAssociation = BinaryAssociation(
    name="importedMember8",
    ends={
        Property(name="cmof_PackageableElement", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Namespace", type=cmof_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport9: BinaryAssociation = BinaryAssociation(
    name="elementImport9",
    ends={
        Property(name="ElementImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=cmof_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member12: BinaryAssociation = BinaryAssociation(
    name="member12",
    ends={
        Property(name="cmof_NamedElement14", type=cmof_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Namespace13", type=cmof_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement16: BinaryAssociation = BinaryAssociation(
    name="ownedElement16",
    ends={
        Property(name="Element", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner18: BinaryAssociation = BinaryAssociation(
    name="owner18",
    ends={
        Property(name="Element19", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=cmof_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment20: BinaryAssociation = BinaryAssociation(
    name="ownedComment20",
    ends={
        Property(name="cmof_Comment", type=cmof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Element", type=cmof_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation25: BinaryAssociation = BinaryAssociation(
    name="ownedOperation25",
    ends={
        Property(name="Operation", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class26", type=cmof_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass28: BinaryAssociation = BinaryAssociation(
    name="superClass28",
    ends={
        Property(name="cmof_Class", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Class27", type=cmof_Class, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement21: BinaryAssociation = BinaryAssociation(
    name="annotatedElement21",
    ends={
        Property(name="cmof_Element23", type=cmof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Comment22", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute24: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute24",
    ends={
        Property(name="Property", type=cmof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=cmof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype38: BinaryAssociation = BinaryAssociation(
    name="datatype38",
    ends={
        Property(name="DataType", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=cmof_DataType, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation29: BinaryAssociation = BinaryAssociation(
    name="owningAssociation29",
    ends={
        Property(name="Association", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=cmof_Association, multiplicity=Multiplicity(0, 1))
    }
)
association30: BinaryAssociation = BinaryAssociation(
    name="association30",
    ends={
        Property(name="Association31", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=cmof_Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty33: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty33",
    ends={
        Property(name="cmof_Property34", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property32", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty36: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty36",
    ends={
        Property(name="cmof_Property37", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property35", type=cmof_Property, multiplicity=Multiplicity(0, 9999))
    }
)
opposite40: BinaryAssociation = BinaryAssociation(
    name="opposite40",
    ends={
        Property(name="cmof_Property41", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Property39", type=cmof_Property, multiplicity=Multiplicity(0, 1))
    }
)
class42: BinaryAssociation = BinaryAssociation(
    name="class42",
    ends={
        Property(name="Class", type=cmof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute43", type=cmof_Class, multiplicity=Multiplicity(0, 1))
    }
)
featuringClassifier44: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier44",
    ends={
        Property(name="Classifier", type=cmof_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext45: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext45",
    ends={
        Property(name="cmof_Classifier46", type=cmof_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_RedefinableElement", type=cmof_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement48: BinaryAssociation = BinaryAssociation(
    name="redefinedElement48",
    ends={
        Property(name="cmof_RedefinableElement49", type=cmof_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_RedefinableElement47", type=cmof_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="cmof_Type", type=cmof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_TypedElement", type=cmof_Type, multiplicity=Multiplicity(0, 1))
    }
)
package51: BinaryAssociation = BinaryAssociation(
    name="package51",
    ends={
        Property(name="Package", type=cmof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=cmof_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedMember52: BinaryAssociation = BinaryAssociation(
    name="ownedMember52",
    ends={
        Property(name="cmof_PackageableElement53", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Package", type=cmof_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType61: BinaryAssociation = BinaryAssociation(
    name="ownedType61",
    ends={
        Property(name="Type", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=cmof_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge54: BinaryAssociation = BinaryAssociation(
    name="packageMerge54",
    ends={
        Property(name="PackageMerge", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=cmof_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage56: BinaryAssociation = BinaryAssociation(
    name="nestedPackage56",
    ends={
        Property(name="Package57", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=cmof_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestingPackage59: BinaryAssociation = BinaryAssociation(
    name="nestingPackage59",
    ends={
        Property(name="Package60", type=cmof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=cmof_Package, multiplicity=Multiplicity(0, 1))
    }
)
target68: BinaryAssociation = BinaryAssociation(
    name="target68",
    ends={
        Property(name="cmof_Element70", type=cmof_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_DirectedRelationship69", type=cmof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
mergedPackage62: BinaryAssociation = BinaryAssociation(
    name="mergedPackage62",
    ends={
        Property(name="cmof_Package63", type=cmof_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_PackageMerge", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage64: BinaryAssociation = BinaryAssociation(
    name="receivingPackage64",
    ends={
        Property(name="Package65", type=cmof_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
source66: BinaryAssociation = BinaryAssociation(
    name="source66",
    ends={
        Property(name="cmof_Element67", type=cmof_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_DirectedRelationship", type=cmof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement71: BinaryAssociation = BinaryAssociation(
    name="relatedElement71",
    ends={
        Property(name="cmof_Element72", type=cmof_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Relationship", type=cmof_Element, multiplicity=Multiplicity(1, 9999))
    }
)
navigableOwnedEnd77: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd77",
    ends={
        Property(name="cmof_Association78", type=cmof_Property, multiplicity=Multiplicity(0, 9999)),
        Property(name="cmof_Property79", type=cmof_Association, multiplicity=Multiplicity(1, 1))
    }
)
ownedEnd80: BinaryAssociation = BinaryAssociation(
    name="ownedEnd80",
    ends={
        Property(name="Property81", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=cmof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endType73: BinaryAssociation = BinaryAssociation(
    name="endType73",
    ends={
        Property(name="cmof_Type74", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Association", type=cmof_Type, multiplicity=Multiplicity(1, 9999))
    }
)
memberEnd75: BinaryAssociation = BinaryAssociation(
    name="memberEnd75",
    ends={
        Property(name="Property76", type=cmof_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=cmof_Property, multiplicity=Multiplicity(2, 9999))
    }
)
ownedOperation82: BinaryAssociation = BinaryAssociation(
    name="ownedOperation82",
    ends={
        Property(name="Operation83", type=cmof_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=cmof_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute84: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute84",
    ends={
        Property(name="Property86", type=cmof_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype85", type=cmof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatype99: BinaryAssociation = BinaryAssociation(
    name="datatype99",
    ends={
        Property(name="ownedOperation100", type=cmof_DataType, multiplicity=Multiplicity(0, 1)),
        Property(name="DataType101", type=cmof_Operation, multiplicity=Multiplicity(1, 1))
    }
)
redefinedOperation88: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation88",
    ends={
        Property(name="cmof_Operation", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation87", type=cmof_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
precondition89: BinaryAssociation = BinaryAssociation(
    name="precondition89",
    ends={
        Property(name="cmof_Constraint", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation90", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
postcondition91: BinaryAssociation = BinaryAssociation(
    name="postcondition91",
    ends={
        Property(name="cmof_Constraint93", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation92", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
bodyCondition94: BinaryAssociation = BinaryAssociation(
    name="bodyCondition94",
    ends={
        Property(name="cmof_Constraint96", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Operation95", type=cmof_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
class97: BinaryAssociation = BinaryAssociation(
    name="class97",
    ends={
        Property(name="Class98", type=cmof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=cmof_Class, multiplicity=Multiplicity(0, 1))
    }
)
operation106: BinaryAssociation = BinaryAssociation(
    name="operation106",
    ends={
        Property(name="cmof_Operation108", type=cmof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Parameter107", type=cmof_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter102: BinaryAssociation = BinaryAssociation(
    name="ownedParameter102",
    ends={
        Property(name="cmof_Parameter", type=cmof_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_BehavioralFeature", type=cmof_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException103: BinaryAssociation = BinaryAssociation(
    name="raisedException103",
    ends={
        Property(name="cmof_Type105", type=cmof_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_BehavioralFeature104", type=cmof_Type, multiplicity=Multiplicity(0, 9999))
    }
)
context109: BinaryAssociation = BinaryAssociation(
    name="context109",
    ends={
        Property(name="cmof_Namespace111", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Constraint110", type=cmof_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement112: BinaryAssociation = BinaryAssociation(
    name="constrainedElement112",
    ends={
        Property(name="cmof_Element114", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Constraint113", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification115: BinaryAssociation = BinaryAssociation(
    name="specification115",
    ends={
        Property(name="cmof_ValueSpecification", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Constraint116", type=cmof_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namespace117: BinaryAssociation = BinaryAssociation(
    name="namespace117",
    ends={
        Property(name="Namespace", type=cmof_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=cmof_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
importedElement118: BinaryAssociation = BinaryAssociation(
    name="importedElement118",
    ends={
        Property(name="cmof_PackageableElement119", type=cmof_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_ElementImport", type=cmof_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace120: BinaryAssociation = BinaryAssociation(
    name="importingNamespace120",
    ends={
        Property(name="Namespace121", type=cmof_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage122: BinaryAssociation = BinaryAssociation(
    name="importedPackage122",
    ends={
        Property(name="cmof_Package123", type=cmof_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_PackageImport", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace124: BinaryAssociation = BinaryAssociation(
    name="importingNamespace124",
    ends={
        Property(name="Namespace125", type=cmof_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=cmof_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
enumeration129: BinaryAssociation = BinaryAssociation(
    name="enumeration129",
    ends={
        Property(name="Enumeration", type=cmof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=cmof_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
operand126: BinaryAssociation = BinaryAssociation(
    name="operand126",
    ends={
        Property(name="cmof_ValueSpecification127", type=cmof_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Expression", type=cmof_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral128: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral128",
    ends={
        Property(name="EnumerationLiteral", type=cmof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=cmof_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectInError130: BinaryAssociation = BinaryAssociation(
    name="objectInError130",
    ends={
        Property(name="cmof_Element131", type=cmof_Exception, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Exception", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
elementInError132: BinaryAssociation = BinaryAssociation(
    name="elementInError132",
    ends={
        Property(name="cmof_Element134", type=cmof_Exception, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Exception133", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
package135: BinaryAssociation = BinaryAssociation(
    name="package135",
    ends={
        Property(name="cmof_Package136", type=cmof_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Factory", type=cmof_Package, multiplicity=Multiplicity(1, 1))
    }
)
element145: BinaryAssociation = BinaryAssociation(
    name="element145",
    ends={
        Property(name="cmof_Element146", type=cmof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Tag", type=cmof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
secondElement137: BinaryAssociation = BinaryAssociation(
    name="secondElement137",
    ends={
        Property(name="cmof_Element138", type=cmof_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Link", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
firstElement139: BinaryAssociation = BinaryAssociation(
    name="firstElement139",
    ends={
        Property(name="cmof_Element141", type=cmof_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Link140", type=cmof_Element, multiplicity=Multiplicity(1, 1))
    }
)
association142: BinaryAssociation = BinaryAssociation(
    name="association142",
    ends={
        Property(name="cmof_Association144", type=cmof_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="cmof_Link143", type=cmof_Association, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_cmof_Classifier_Namespace = Generalization(general=Namespace, specific=cmof_Classifier)
gen_cmof_Classifier_Type = Generalization(general=Type, specific=cmof_Classifier)
gen_cmof_Namespace_NamedElement = Generalization(general=NamedElement, specific=cmof_Namespace)
gen_cmof_NamedElement_Element = Generalization(general=Element, specific=cmof_NamedElement)
gen_cmof_Comment_Element = Generalization(general=Element, specific=cmof_Comment)
gen_cmof_Class_Classifier = Generalization(general=Classifier, specific=cmof_Class)
gen_cmof_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=cmof_Property)
gen_cmof_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=cmof_Property)
gen_cmof_StructuralFeature_Feature = Generalization(general=Feature, specific=cmof_StructuralFeature)
gen_cmof_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=cmof_StructuralFeature)
gen_cmof_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=cmof_StructuralFeature)
gen_cmof_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=cmof_Feature)
gen_cmof_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=cmof_RedefinableElement)
gen_cmof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=cmof_TypedElement)
gen_cmof_Type_PackageableElement = Generalization(general=PackageableElement, specific=cmof_Type)
gen_cmof_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=cmof_PackageableElement)
gen_cmof_Package_Namespace = Generalization(general=Namespace, specific=cmof_Package)
gen_cmof_Package_PackageableElement = Generalization(general=PackageableElement, specific=cmof_Package)
gen_cmof_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_PackageMerge)
gen_cmof_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=cmof_DirectedRelationship)
gen_cmof_Relationship_Element = Generalization(general=Element, specific=cmof_Relationship)
gen_cmof_MultiplicityElement_Element = Generalization(general=Element, specific=cmof_MultiplicityElement)
gen_cmof_Association_Classifier = Generalization(general=Classifier, specific=cmof_Association)
gen_cmof_Association_Relationship = Generalization(general=Relationship, specific=cmof_Association)
gen_cmof_DataType_Classifier = Generalization(general=Classifier, specific=cmof_DataType)
gen_cmof_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=cmof_Operation)
gen_cmof_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=cmof_Operation)
gen_cmof_Operation_TypedElement = Generalization(general=TypedElement, specific=cmof_Operation)
gen_cmof_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=cmof_BehavioralFeature)
gen_cmof_BehavioralFeature_Feature = Generalization(general=Feature, specific=cmof_BehavioralFeature)
gen_cmof_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=cmof_Parameter)
gen_cmof_Parameter_TypedElement = Generalization(general=TypedElement, specific=cmof_Parameter)
gen_cmof_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=cmof_Constraint)
gen_cmof_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=cmof_ValueSpecification)
gen_cmof_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=cmof_ValueSpecification)
gen_cmof_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_ElementImport)
gen_cmof_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=cmof_OpaqueExpression)
gen_cmof_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=cmof_PackageImport)
gen_cmof_PrimitiveType_DataType = Generalization(general=DataType, specific=cmof_PrimitiveType)
gen_cmof_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=cmof_Expression)
gen_cmof_Enumeration_DataType = Generalization(general=DataType, specific=cmof_Enumeration)
gen_cmof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=cmof_EnumerationLiteral)
gen_cmof_Factory_Element = Generalization(general=Element, specific=cmof_Factory)
gen_cmof_Tag_Element = Generalization(general=Element, specific=cmof_Tag)

# Domain Model
domain_model = DomainModel(
    name="cmof",
    types={cmof_Classifier, Namespace, Type, cmof_NamedElement, cmof_Feature, cmof_Property, cmof_Namespace, NamedElement, cmof_PackageImport, cmof_Constraint, cmof_PackageableElement, cmof_ElementImport, Element, cmof_Element, cmof_Comment, cmof_Operation, cmof_Class, Classifier, StructuralFeature, MultiplicityElement, cmof_DataType, cmof_Association, TypedElement, RedefinableElement, cmof_StructuralFeature, Feature, cmof_RedefinableElement, cmof_TypedElement, cmof_Type, PackageableElement, cmof_Package, cmof_PackageMerge, DirectedRelationship, cmof_DirectedRelationship, Relationship, cmof_Relationship, cmof_MultiplicityElement, BehavioralFeature, cmof_BehavioralFeature, cmof_Parameter, cmof_ValueSpecification, cmof_Argument, cmof_OpaqueExpression, ValueSpecification, cmof_PrimitiveType, cmof_Expression, cmof_Enumeration, DataType, cmof_EnumerationLiteral, cmof_Exception, cmof_Factory, cmof_Link, cmof_Tag, ParameterDirectionKind, VisibilityKind},
    associations={general3, inheritedMember5, feature0, attribute1, packageImport10, ownedRule7, importedMember8, elementImport9, member12, ownedElement16, owner18, ownedComment20, ownedOperation25, superClass28, annotatedElement21, ownedAttribute24, datatype38, owningAssociation29, association30, redefinedProperty33, subsettedProperty36, opposite40, class42, featuringClassifier44, redefinitionContext45, redefinedElement48, type50, package51, ownedMember52, ownedType61, packageMerge54, nestedPackage56, nestingPackage59, target68, mergedPackage62, receivingPackage64, source66, relatedElement71, navigableOwnedEnd77, ownedEnd80, endType73, memberEnd75, ownedOperation82, ownedAttribute84, datatype99, redefinedOperation88, precondition89, postcondition91, bodyCondition94, class97, operation106, ownedParameter102, raisedException103, context109, constrainedElement112, specification115, namespace117, importedElement118, importingNamespace120, importedPackage122, importingNamespace124, enumeration129, operand126, ownedLiteral128, objectInError130, elementInError132, package135, element145, secondElement137, firstElement139, association142},
    generalizations={gen_cmof_Classifier_Namespace, gen_cmof_Classifier_Type, gen_cmof_Namespace_NamedElement, gen_cmof_NamedElement_Element, gen_cmof_Comment_Element, gen_cmof_Class_Classifier, gen_cmof_Property_StructuralFeature, gen_cmof_Property_MultiplicityElement, gen_cmof_StructuralFeature_Feature, gen_cmof_StructuralFeature_MultiplicityElement, gen_cmof_StructuralFeature_TypedElement, gen_cmof_Feature_RedefinableElement, gen_cmof_RedefinableElement_NamedElement, gen_cmof_TypedElement_NamedElement, gen_cmof_Type_PackageableElement, gen_cmof_PackageableElement_NamedElement, gen_cmof_Package_Namespace, gen_cmof_Package_PackageableElement, gen_cmof_PackageMerge_DirectedRelationship, gen_cmof_DirectedRelationship_Relationship, gen_cmof_Relationship_Element, gen_cmof_MultiplicityElement_Element, gen_cmof_Association_Classifier, gen_cmof_Association_Relationship, gen_cmof_DataType_Classifier, gen_cmof_Operation_BehavioralFeature, gen_cmof_Operation_MultiplicityElement, gen_cmof_Operation_TypedElement, gen_cmof_BehavioralFeature_Namespace, gen_cmof_BehavioralFeature_Feature, gen_cmof_Parameter_MultiplicityElement, gen_cmof_Parameter_TypedElement, gen_cmof_Constraint_PackageableElement, gen_cmof_ValueSpecification_TypedElement, gen_cmof_ValueSpecification_PackageableElement, gen_cmof_ElementImport_DirectedRelationship, gen_cmof_OpaqueExpression_ValueSpecification, gen_cmof_PackageImport_DirectedRelationship, gen_cmof_PrimitiveType_DataType, gen_cmof_Expression_ValueSpecification, gen_cmof_Enumeration_DataType, gen_cmof_EnumerationLiteral_NamedElement, gen_cmof_Factory_Element, gen_cmof_Tag_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)