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

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

# Classes
RefUML_Comment = Class(name="RefUML::Comment")
Element = Class(name="Element")
RefUML_Element = Class(name="RefUML::Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
RefUML_Package = Class(name="RefUML::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
RefUML_Type = Class(name="RefUML::Type", is_abstract=True)
RefUML_PackageMerge = Class(name="RefUML::PackageMerge")
NamedElement = Class(name="NamedElement")
RefUML_NamedElement = Class(name="RefUML::NamedElement", is_abstract=True)
RefUML_PackageableElement = Class(name="RefUML::PackageableElement", is_abstract=True)
RefUML_Dependency = Class(name="RefUML::Dependency")
RefUML_Namespace = Class(name="RefUML::Namespace", is_abstract=True)
RefUML_DirectedRelationship = Class(name="RefUML::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
RefUML_StringExpression = Class(name="RefUML::StringExpression")
DirectedRelationship = Class(name="DirectedRelationship")
RefUML_Relationship = Class(name="RefUML::Relationship", is_abstract=True)
RefUML_ElementImport = Class(name="RefUML::ElementImport")
RefUML_PackageImport = Class(name="RefUML::PackageImport")
RefUML_Constraintx = Class(name="RefUML::Constraintx")
RefUML_ValueSpecification = Class(name="RefUML::ValueSpecification", is_abstract=True)
RefUML_TypedElement = Class(name="RefUML::TypedElement", is_abstract=True)
TypedElement = Class(name="TypedElement")
RefUML_Association = Class(name="RefUML::Association")
Classifier = Class(name="Classifier")
RefUML_Property = Class(name="RefUML::Property")
RefUML_Classifier = Class(name="RefUML::Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
RefUML_Generalization = Class(name="RefUML::Generalization")
RefUML_GeneralizationSet = Class(name="RefUML::GeneralizationSet")
RefUML_Feature = Class(name="RefUML::Feature", is_abstract=True)
RefUML_RedefinableElement = Class(name="RefUML::RedefinableElement", is_abstract=True)
RefUML_OpaqueExpression = Class(name="RefUML::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
RefUML_MultiplicityElement = Class(name="RefUML::MultiplicityElement", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
RefUML_Class = Class(name="RefUML::Class")
RefUML_DataType = Class(name="RefUML::DataType")
RefUML_Model = Class(name="RefUML::Model")
Package = Class(name="Package")
RefUML_StructuralFeature = Class(name="RefUML::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
Expression = Class(name="Expression")
MultiplicityElement = Class(name="MultiplicityElement")
RefUML_Expression = Class(name="RefUML::Expression")
RefUML_Slot = Class(name="RefUML::Slot")
RefUML_Enumeration = Class(name="RefUML::Enumeration")
DataType = Class(name="DataType")
RefUML_EnumerationLiteral = Class(name="RefUML::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
RefUML_InstanceSpecification = Class(name="RefUML::InstanceSpecification")
RefUML_PrimitiveType = Class(name="RefUML::PrimitiveType")
RefUML_LiteralSpecification = Class(name="RefUML::LiteralSpecification", is_abstract=True)
RefUML_LiteralInteger = Class(name="RefUML::LiteralInteger")
LiteralSpecification = Class(name="LiteralSpecification")
RefUML_LiteralString = Class(name="RefUML::LiteralString")
RefUML_LiteralNull = Class(name="RefUML::LiteralNull")
RefUML_LiteralBoolean = Class(name="RefUML::LiteralBoolean")
RefUML_InstanceValue = Class(name="RefUML::InstanceValue")
RefUML_LiteralUnlimitedNatural = Class(name="RefUML::LiteralUnlimitedNatural")

# RefUML_Comment class attributes and methods
RefUML_Comment_body: Property = Property(name="body", type=StringType)
RefUML_Comment.attributes={RefUML_Comment_body}

# Element class attributes and methods

# RefUML_Element class attributes and methods
RefUML_Element_m_destroy: Method = Method(name="destroy", parameters={})
RefUML_Element_m_hasKeyword: Method = Method(name="hasKeyword", parameters={Parameter(name='keyword')}, type=StringType)
RefUML_Element_m_getKeywords: Method = Method(name="getKeywords", parameters={}, type=StringType)
RefUML_Element_m_getModel: Method = Method(name="getModel", parameters={}, type=StringType)
RefUML_Element_m_getApplicableStereotype: Method = Method(name="getApplicableStereotype", parameters={Parameter(name='qualifiedName')})
RefUML_Element_m_getStereotypeApplications: Method = Method(name="getStereotypeApplications", parameters={}, type=StringType)
RefUML_Element_m_getRequiredStereotype: Method = Method(name="getRequiredStereotype", parameters={Parameter(name='qualifiedName')})
RefUML_Element_m_getAppliedStereotype: Method = Method(name="getAppliedStereotype", parameters={Parameter(name='qualifiedName')})
RefUML_Element_m_addKeyword: Method = Method(name="addKeyword", parameters={Parameter(name='keyword')}, type=StringType)
RefUML_Element_m_removeKeyword: Method = Method(name="removeKeyword", parameters={Parameter(name='keyword')}, type=StringType)
RefUML_Element_m_getNearestPackage: Method = Method(name="getNearestPackage", parameters={}, type=StringType)
RefUML_Element_m_getSourceDirectedRelationships: Method = Method(name="getSourceDirectedRelationships", parameters={}, type=StringType)
RefUML_Element_m_getSourceDirectedRelationships: Method = Method(name="getSourceDirectedRelationships", parameters={Parameter(name='eClass')}, type=StringType)
RefUML_Element_m_getTargetDirectedRelationships: Method = Method(name="getTargetDirectedRelationships", parameters={}, type=StringType)
RefUML_Element_m_getTargetDirectedRelationships: Method = Method(name="getTargetDirectedRelationships", parameters={Parameter(name='eClass')}, type=StringType)
RefUML_Element_m_createEAnnotation: Method = Method(name="createEAnnotation", parameters={Parameter(name='source')}, type=StringType)
RefUML_Element_m_getRelationships: Method = Method(name="getRelationships", parameters={}, type=StringType)
RefUML_Element_m_getRelationships: Method = Method(name="getRelationships", parameters={Parameter(name='eClass')}, type=StringType)
RefUML_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
RefUML_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=StringType)
RefUML_Element.methods={RefUML_Element_m_addKeyword, RefUML_Element_m_mustBeOwned, RefUML_Element_m_removeKeyword, RefUML_Element_m_getRequiredStereotype, RefUML_Element_m_getSourceDirectedRelationships, RefUML_Element_m_getAppliedStereotype, RefUML_Element_m_getApplicableStereotype, RefUML_Element_m_getStereotypeApplications, RefUML_Element_m_getRelationships, RefUML_Element_m_getSourceDirectedRelationships, RefUML_Element_m_allOwnedElements, RefUML_Element_m_getRelationships, RefUML_Element_m_destroy, RefUML_Element_m_createEAnnotation, RefUML_Element_m_getKeywords, RefUML_Element_m_hasKeyword, RefUML_Element_m_getTargetDirectedRelationships, RefUML_Element_m_getTargetDirectedRelationships, RefUML_Element_m_getModel, RefUML_Element_m_getNearestPackage}

# EModelElement class attributes and methods

# RefUML_Package class attributes and methods
RefUML_Package_m_createOwnedEnumeration: Method = Method(name="createOwnedEnumeration", parameters={Parameter(name='name')}, type=StringType)
RefUML_Package_m_createOwnedPrimitiveType: Method = Method(name="createOwnedPrimitiveType", parameters={Parameter(name='name')}, type=StringType)
RefUML_Package_m_createOwnedInterface: Method = Method(name="createOwnedInterface", parameters={Parameter(name='name')})
RefUML_Package_m_getAppliedProfile: Method = Method(name="getAppliedProfile", parameters={Parameter(name='qualifiedName')})
RefUML_Package_m_createOwnedClass: Method = Method(name="createOwnedClass", parameters={Parameter(name='name'), Parameter(name='isAbstract')}, type=StringType)
RefUML_Package_m_visibleMembers: Method = Method(name="visibleMembers", parameters={}, type=PackageableElement)
RefUML_Package_m_makesVisible: Method = Method(name="makesVisible", parameters={Parameter(name='el')}, type=StringType)
RefUML_Package_m_getAppliedProfile: Method = Method(name="getAppliedProfile", parameters={Parameter(name='qualifiedName'), Parameter(name='recurse')})
RefUML_Package_m_isModelLibrary: Method = Method(name="isModelLibrary", parameters={}, type=StringType)
RefUML_Package.methods={RefUML_Package_m_makesVisible, RefUML_Package_m_createOwnedClass, RefUML_Package_m_createOwnedInterface, RefUML_Package_m_getAppliedProfile, RefUML_Package_m_isModelLibrary, RefUML_Package_m_getAppliedProfile, RefUML_Package_m_createOwnedEnumeration, RefUML_Package_m_createOwnedPrimitiveType, RefUML_Package_m_visibleMembers}

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# RefUML_Type class attributes and methods
RefUML_Type_m_createAssociation: Method = Method(name="createAssociation", parameters={Parameter(name='end2Aggregation'), Parameter(name='end1Upper'), Parameter(name='end1Lower'), Parameter(name='end2Upper'), Parameter(name='end1IsNavigable'), Parameter(name='end2IsNavigable'), Parameter(name='end1Type'), Parameter(name='end2Lower'), Parameter(name='end1Name'), Parameter(name='end1Aggregation'), Parameter(name='end2Name')}, type=StringType)
RefUML_Type_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
RefUML_Type_m_getAssociations: Method = Method(name="getAssociations", parameters={}, type=StringType)
RefUML_Type.methods={RefUML_Type_m_getAssociations, RefUML_Type_m_conformsTo, RefUML_Type_m_createAssociation}

# RefUML_PackageMerge class attributes and methods

# NamedElement class attributes and methods

# RefUML_NamedElement class attributes and methods
RefUML_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
RefUML_NamedElement_name: Property = Property(name="name", type=StringType)
RefUML_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
RefUML_NamedElement_m_createUsage: Method = Method(name="createUsage", parameters={Parameter(name='supplier')})
RefUML_NamedElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
RefUML_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=Namespace)
RefUML_NamedElement_m_isDistinguishableFrom: Method = Method(name="isDistinguishableFrom", parameters={Parameter(name='ns'), Parameter(name='n')}, type=StringType)
RefUML_NamedElement_m_createDependency: Method = Method(name="createDependency", parameters={Parameter(name='supplier')}, type=StringType)
RefUML_NamedElement_m_getLabel: Method = Method(name="getLabel", parameters={}, type=StringType)
RefUML_NamedElement_m_getLabel: Method = Method(name="getLabel", parameters={Parameter(name='localize')}, type=StringType)
RefUML_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
RefUML_NamedElement_m_allOwningPackages: Method = Method(name="allOwningPackages", parameters={}, type=StringType)
RefUML_NamedElement.attributes={RefUML_NamedElement_visibility, RefUML_NamedElement_name, RefUML_NamedElement_qualifiedName}
RefUML_NamedElement.methods={RefUML_NamedElement_m_getQualifiedName, RefUML_NamedElement_m_getLabel, RefUML_NamedElement_m_createUsage, RefUML_NamedElement_m_createDependency, RefUML_NamedElement_m_isDistinguishableFrom, RefUML_NamedElement_m_allOwningPackages, RefUML_NamedElement_m_allNamespaces, RefUML_NamedElement_m_getLabel, RefUML_NamedElement_m_separator}

# RefUML_PackageableElement class attributes and methods

# RefUML_Dependency class attributes and methods

# RefUML_Namespace class attributes and methods
RefUML_Namespace_m_createElementImport: Method = Method(name="createElementImport", parameters={Parameter(name='visibility'), Parameter(name='element')}, type=StringType)
RefUML_Namespace_m_createPackageImport: Method = Method(name="createPackageImport", parameters={Parameter(name='visibility'), Parameter(name='package_')}, type=StringType)
RefUML_Namespace_m_getImportedMembers: Method = Method(name="getImportedMembers", parameters={}, type=PackageableElement)
RefUML_Namespace_m_getNamesOfMember: Method = Method(name="getNamesOfMember", parameters={Parameter(name='element')}, type=StringType)
RefUML_Namespace_m_membersAreDistinguishable: Method = Method(name="membersAreDistinguishable", parameters={}, type=StringType)
RefUML_Namespace_m_importMembers: Method = Method(name="importMembers", parameters={Parameter(name='imps')}, type=PackageableElement)
RefUML_Namespace_m_excludeCollisions: Method = Method(name="excludeCollisions", parameters={Parameter(name='imps')}, type=PackageableElement)
RefUML_Namespace_m_getImportedElements: Method = Method(name="getImportedElements", parameters={}, type=PackageableElement)
RefUML_Namespace_m_getImportedPackages: Method = Method(name="getImportedPackages", parameters={}, type=StringType)
RefUML_Namespace.methods={RefUML_Namespace_m_getNamesOfMember, RefUML_Namespace_m_membersAreDistinguishable, RefUML_Namespace_m_excludeCollisions, RefUML_Namespace_m_getImportedMembers, RefUML_Namespace_m_getImportedPackages, RefUML_Namespace_m_createPackageImport, RefUML_Namespace_m_getImportedElements, RefUML_Namespace_m_createElementImport, RefUML_Namespace_m_importMembers}

# RefUML_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# RefUML_StringExpression class attributes and methods

# DirectedRelationship class attributes and methods

# RefUML_Relationship class attributes and methods

# RefUML_ElementImport class attributes and methods
RefUML_ElementImport_alias: Property = Property(name="alias", type=StringType)
RefUML_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
RefUML_ElementImport_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
RefUML_ElementImport.attributes={RefUML_ElementImport_alias, RefUML_ElementImport_visibility}
RefUML_ElementImport.methods={RefUML_ElementImport_m_getName}

# RefUML_PackageImport class attributes and methods
RefUML_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
RefUML_PackageImport.attributes={RefUML_PackageImport_visibility}

# RefUML_Constraintx class attributes and methods

# RefUML_ValueSpecification class attributes and methods
RefUML_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=StringType)
RefUML_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
RefUML_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=StringType)
RefUML_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=StringType)
RefUML_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=StringType)
RefUML_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=StringType)
RefUML_ValueSpecification.methods={RefUML_ValueSpecification_m_booleanValue, RefUML_ValueSpecification_m_unlimitedValue, RefUML_ValueSpecification_m_isComputable, RefUML_ValueSpecification_m_stringValue, RefUML_ValueSpecification_m_isNull, RefUML_ValueSpecification_m_integerValue}

# RefUML_TypedElement class attributes and methods

# TypedElement class attributes and methods

# RefUML_Association class attributes and methods
RefUML_Association_isDerived: Property = Property(name="isDerived", type=StringType)
RefUML_Association_m_isBinary: Method = Method(name="isBinary", parameters={}, type=StringType)
RefUML_Association_m_getEndTypes: Method = Method(name="getEndTypes", parameters={}, type=StringType)
RefUML_Association.attributes={RefUML_Association_isDerived}
RefUML_Association.methods={RefUML_Association_m_isBinary, RefUML_Association_m_getEndTypes}

# Classifier class attributes and methods

# RefUML_Property class attributes and methods
RefUML_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
RefUML_Property_default: Property = Property(name="default", type=StringType)
RefUML_Property_aggregation: Property = Property(name="aggregation", type=StringType)
RefUML_Property_isComposite: Property = Property(name="isComposite", type=StringType)
RefUML_Property_isDerived: Property = Property(name="isDerived", type=StringType)
RefUML_Property_m_getDefault: Method = Method(name="getDefault", parameters={}, type=StringType)
RefUML_Property_m_isSetDefault: Method = Method(name="isSetDefault", parameters={}, type=StringType)
RefUML_Property_m_setDefault: Method = Method(name="setDefault", parameters={Parameter(name='newDefault')})
RefUML_Property_m_setIsComposite: Method = Method(name="setIsComposite", parameters={Parameter(name='newIsComposite')})
RefUML_Property_m_getOtherEnd: Method = Method(name="getOtherEnd", parameters={}, type=StringType)
RefUML_Property_m_setBooleanDefaultValue: Method = Method(name="setBooleanDefaultValue", parameters={Parameter(name='value')})
RefUML_Property_m_setIntegerDefaultValue: Method = Method(name="setIntegerDefaultValue", parameters={Parameter(name='value')})
RefUML_Property_m_setStringDefaultValue: Method = Method(name="setStringDefaultValue", parameters={Parameter(name='value')})
RefUML_Property_m_setOpposite: Method = Method(name="setOpposite", parameters={Parameter(name='newOpposite')})
RefUML_Property_m_unsetDefault: Method = Method(name="unsetDefault", parameters={})
RefUML_Property_m_setIsNavigable: Method = Method(name="setIsNavigable", parameters={Parameter(name='isNavigable')})
RefUML_Property_m_getOpposite: Method = Method(name="getOpposite", parameters={}, type=StringType)
RefUML_Property_m_isComposite: Method = Method(name="isComposite", parameters={}, type=StringType)
RefUML_Property_m_subsettingContext: Method = Method(name="subsettingContext", parameters={}, type=Type)
RefUML_Property_m_isNavigable: Method = Method(name="isNavigable", parameters={}, type=StringType)
RefUML_Property_m_setUnlimitedNaturalDefaultValue: Method = Method(name="setUnlimitedNaturalDefaultValue", parameters={Parameter(name='value')})
RefUML_Property_m_setNullDefaultValue: Method = Method(name="setNullDefaultValue", parameters={})
RefUML_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={Parameter(name='p')}, type=StringType)
RefUML_Property.attributes={RefUML_Property_isDerived, RefUML_Property_aggregation, RefUML_Property_isComposite, RefUML_Property_isDerivedUnion, RefUML_Property_default}
RefUML_Property.methods={RefUML_Property_m_setNullDefaultValue, RefUML_Property_m_isNavigable, RefUML_Property_m_getOpposite, RefUML_Property_m_subsettingContext, RefUML_Property_m_isAttribute, RefUML_Property_m_setStringDefaultValue, RefUML_Property_m_setIntegerDefaultValue, RefUML_Property_m_setBooleanDefaultValue, RefUML_Property_m_getDefault, RefUML_Property_m_unsetDefault, RefUML_Property_m_setIsNavigable, RefUML_Property_m_isSetDefault, RefUML_Property_m_setUnlimitedNaturalDefaultValue, RefUML_Property_m_setOpposite, RefUML_Property_m_setIsComposite, RefUML_Property_m_isComposite, RefUML_Property_m_setDefault, RefUML_Property_m_getOtherEnd}

# RefUML_Classifier class attributes and methods
RefUML_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
RefUML_Classifier_m_getGenerals: Method = Method(name="getGenerals", parameters={}, type=Classifier)
RefUML_Classifier_m_getInheritedMembers: Method = Method(name="getInheritedMembers", parameters={}, type=NamedElement)
RefUML_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=StringType)
RefUML_Classifier_m_parents: Method = Method(name="parents", parameters={}, type=Classifier)
RefUML_Classifier_m_inheritableMembers: Method = Method(name="inheritableMembers", parameters={Parameter(name='c')}, type=NamedElement)
RefUML_Classifier_m_getAllAttributes: Method = Method(name="getAllAttributes", parameters={}, type=StringType)
RefUML_Classifier_m_maySpecializeType: Method = Method(name="maySpecializeType", parameters={Parameter(name='c')}, type=StringType)
RefUML_Classifier_m_allParents: Method = Method(name="allParents", parameters={}, type=Classifier)
RefUML_Classifier_m_hasKindAncestor: Method = Method(name="hasKindAncestor", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasQuantityAncestor: Method = Method(name="hasQuantityAncestor", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasVisibilityOf: Method = Method(name="hasVisibilityOf", parameters={Parameter(name='n')}, type=StringType)
RefUML_Classifier_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
RefUML_Classifier_m_inherit: Method = Method(name="inherit", parameters={Parameter(name='inhs')}, type=NamedElement)
RefUML_Classifier_m_hasQuantityInstances: Method = Method(name="hasQuantityInstances", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasCollectiveInstances: Method = Method(name="hasCollectiveInstances", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasCollectiveAncestor: Method = Method(name="hasCollectiveAncestor", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasKindOffspring: Method = Method(name="hasKindOffspring", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasQuantityOffspring: Method = Method(name="hasQuantityOffspring", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasCollectiveOffspring: Method = Method(name="hasCollectiveOffspring", parameters={}, type=BooleanType)
RefUML_Classifier_m_hasFunctionalComplexInstances: Method = Method(name="hasFunctionalComplexInstances", parameters={}, type=BooleanType)
RefUML_Classifier.attributes={RefUML_Classifier_isAbstract}
RefUML_Classifier.methods={RefUML_Classifier_m_hasQuantityInstances, RefUML_Classifier_m_hasFunctionalComplexInstances, RefUML_Classifier_m_inheritableMembers, RefUML_Classifier_m_hasCollectiveAncestor, RefUML_Classifier_m_hasQuantityAncestor, RefUML_Classifier_m_hasCollectiveInstances, RefUML_Classifier_m_parents, RefUML_Classifier_m_hasQuantityOffspring, RefUML_Classifier_m_getAllAttributes, RefUML_Classifier_m_hasKindOffspring, RefUML_Classifier_m_hasVisibilityOf, RefUML_Classifier_m_getGenerals, RefUML_Classifier_m_conformsTo, RefUML_Classifier_m_maySpecializeType, RefUML_Classifier_m_hasCollectiveOffspring, RefUML_Classifier_m_allParents, RefUML_Classifier_m_inherit, RefUML_Classifier_m_hasKindAncestor, RefUML_Classifier_m_getInheritedMembers, RefUML_Classifier_m_allFeatures}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# RefUML_Generalization class attributes and methods
RefUML_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
RefUML_Generalization.attributes={RefUML_Generalization_isSubstitutable}

# RefUML_GeneralizationSet class attributes and methods
RefUML_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=StringType)
RefUML_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=StringType)
RefUML_GeneralizationSet.attributes={RefUML_GeneralizationSet_isDisjoint, RefUML_GeneralizationSet_isCovering}

# RefUML_Feature class attributes and methods
RefUML_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
RefUML_Feature.attributes={RefUML_Feature_isStatic}

# RefUML_RedefinableElement class attributes and methods
RefUML_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
RefUML_RedefinableElement_m_isConsistentWith: Method = Method(name="isConsistentWith", parameters={Parameter(name='redefinee')}, type=StringType)
RefUML_RedefinableElement_m_isRedefinitionContextValid: Method = Method(name="isRedefinitionContextValid", parameters={Parameter(name='redefined')}, type=StringType)
RefUML_RedefinableElement.attributes={RefUML_RedefinableElement_isLeaf}
RefUML_RedefinableElement.methods={RefUML_RedefinableElement_m_isRedefinitionContextValid, RefUML_RedefinableElement_m_isConsistentWith}

# RefUML_OpaqueExpression class attributes and methods
RefUML_OpaqueExpression_language: Property = Property(name="language", type=StringType)
RefUML_OpaqueExpression_body: Property = Property(name="body", type=StringType)
RefUML_OpaqueExpression_m_getResult: Method = Method(name="getResult", parameters={})
RefUML_OpaqueExpression_m_value: Method = Method(name="value", parameters={}, type=StringType)
RefUML_OpaqueExpression_m_isIntegral: Method = Method(name="isIntegral", parameters={}, type=StringType)
RefUML_OpaqueExpression_m_isPositive: Method = Method(name="isPositive", parameters={}, type=StringType)
RefUML_OpaqueExpression_m_isNonNegative: Method = Method(name="isNonNegative", parameters={}, type=StringType)
RefUML_OpaqueExpression.attributes={RefUML_OpaqueExpression_body, RefUML_OpaqueExpression_language}
RefUML_OpaqueExpression.methods={RefUML_OpaqueExpression_m_isPositive, RefUML_OpaqueExpression_m_isIntegral, RefUML_OpaqueExpression_m_isNonNegative, RefUML_OpaqueExpression_m_value, RefUML_OpaqueExpression_m_getResult}

# ValueSpecification class attributes and methods

# RefUML_MultiplicityElement class attributes and methods
RefUML_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
RefUML_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
RefUML_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
RefUML_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
RefUML_MultiplicityElement_m_setLower: Method = Method(name="setLower", parameters={Parameter(name='newLower')})
RefUML_MultiplicityElement_m_setUpper: Method = Method(name="setUpper", parameters={Parameter(name='newUpper')})
RefUML_MultiplicityElement_m_includesCardinality: Method = Method(name="includesCardinality", parameters={Parameter(name='C')}, type=StringType)
RefUML_MultiplicityElement_m_includesMultiplicity: Method = Method(name="includesMultiplicity", parameters={Parameter(name='M')}, type=StringType)
RefUML_MultiplicityElement_m_lowerBound: Method = Method(name="lowerBound", parameters={}, type=StringType)
RefUML_MultiplicityElement_m_upperBound: Method = Method(name="upperBound", parameters={}, type=StringType)
RefUML_MultiplicityElement_m_getLower: Method = Method(name="getLower", parameters={}, type=StringType)
RefUML_MultiplicityElement_m_getUpper: Method = Method(name="getUpper", parameters={}, type=StringType)
RefUML_MultiplicityElement_m_isMultivalued: Method = Method(name="isMultivalued", parameters={}, type=StringType)
RefUML_MultiplicityElement_m_compatibleWith: Method = Method(name="compatibleWith", parameters={Parameter(name='other')}, type=StringType)
RefUML_MultiplicityElement_m_is: Method = Method(name="is", parameters={Parameter(name='lowerbound'), Parameter(name='upperbound')}, type=StringType)
RefUML_MultiplicityElement.attributes={RefUML_MultiplicityElement_lower, RefUML_MultiplicityElement_isOrdered, RefUML_MultiplicityElement_isUnique, RefUML_MultiplicityElement_upper}
RefUML_MultiplicityElement.methods={RefUML_MultiplicityElement_m_setLower, RefUML_MultiplicityElement_m_getLower, RefUML_MultiplicityElement_m_upperBound, RefUML_MultiplicityElement_m_isMultivalued, RefUML_MultiplicityElement_m_compatibleWith, RefUML_MultiplicityElement_m_is, RefUML_MultiplicityElement_m_includesCardinality, RefUML_MultiplicityElement_m_lowerBound, RefUML_MultiplicityElement_m_getUpper, RefUML_MultiplicityElement_m_includesMultiplicity, RefUML_MultiplicityElement_m_setUpper}

# StructuralFeature class attributes and methods

# RefUML_Class class attributes and methods
RefUML_Class_isActive: Property = Property(name="isActive", type=StringType)
RefUML_Class_m_isMetaclass: Method = Method(name="isMetaclass", parameters={}, type=StringType)
RefUML_Class_m_createOwnedOperation: Method = Method(name="createOwnedOperation", parameters={Parameter(name='parameterNames'), Parameter(name='returnType'), Parameter(name='name'), Parameter(name='parameterTypes')})
RefUML_Class.attributes={RefUML_Class_isActive}
RefUML_Class.methods={RefUML_Class_m_isMetaclass, RefUML_Class_m_createOwnedOperation}

# RefUML_DataType class attributes and methods
RefUML_DataType_m_createOwnedOperation: Method = Method(name="createOwnedOperation", parameters={Parameter(name='parameterTypes'), Parameter(name='name'), Parameter(name='returnType'), Parameter(name='parameterNames')})
RefUML_DataType_m_createOwnedAttribute: Method = Method(name="createOwnedAttribute", parameters={Parameter(name='type'), Parameter(name='name'), Parameter(name='lower'), Parameter(name='upper')}, type=StringType)
RefUML_DataType.methods={RefUML_DataType_m_createOwnedOperation, RefUML_DataType_m_createOwnedAttribute}

# RefUML_Model class attributes and methods
RefUML_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
RefUML_Model_m_isMetamodel: Method = Method(name="isMetamodel", parameters={}, type=StringType)
RefUML_Model.attributes={RefUML_Model_viewpoint}
RefUML_Model.methods={RefUML_Model_m_isMetamodel}

# Package class attributes and methods

# RefUML_StructuralFeature class attributes and methods
RefUML_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
RefUML_StructuralFeature.attributes={RefUML_StructuralFeature_isReadOnly}

# Feature class attributes and methods

# Expression class attributes and methods

# MultiplicityElement class attributes and methods

# RefUML_Expression class attributes and methods
RefUML_Expression_symbol: Property = Property(name="symbol", type=StringType)
RefUML_Expression.attributes={RefUML_Expression_symbol}

# RefUML_Slot class attributes and methods

# RefUML_Enumeration class attributes and methods

# DataType class attributes and methods

# RefUML_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# RefUML_InstanceSpecification class attributes and methods

# RefUML_PrimitiveType class attributes and methods

# RefUML_LiteralSpecification class attributes and methods

# RefUML_LiteralInteger class attributes and methods
RefUML_LiteralInteger_value: Property = Property(name="value", type=StringType)
RefUML_LiteralInteger.attributes={RefUML_LiteralInteger_value}

# LiteralSpecification class attributes and methods

# RefUML_LiteralString class attributes and methods
RefUML_LiteralString_value: Property = Property(name="value", type=StringType)
RefUML_LiteralString.attributes={RefUML_LiteralString_value}

# RefUML_LiteralNull class attributes and methods

# RefUML_LiteralBoolean class attributes and methods
RefUML_LiteralBoolean_value: Property = Property(name="value", type=StringType)
RefUML_LiteralBoolean.attributes={RefUML_LiteralBoolean_value}

# RefUML_InstanceValue class attributes and methods

# RefUML_LiteralUnlimitedNatural class attributes and methods
RefUML_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
RefUML_LiteralUnlimitedNatural.attributes={RefUML_LiteralUnlimitedNatural_value}

# Relationships
annotatedElement0: BinaryAssociation = BinaryAssociation(
    name="annotatedElement0",
    ends={
        Property(name="RefUML_Element", type=RefUML_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Comment", type=RefUML_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Element5", type=RefUML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=RefUML_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="RefUML_Comment8", type=RefUML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Element7", type=RefUML_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement2: BinaryAssociation = BinaryAssociation(
    name="ownedElement2",
    ends={
        Property(name="Element", type=RefUML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RefUML_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType9: BinaryAssociation = BinaryAssociation(
    name="ownedType9",
    ends={
        Property(name="Type", type=RefUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=RefUML_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge10: BinaryAssociation = BinaryAssociation(
    name="packageMerge10",
    ends={
        Property(name="PackageMerge", type=RefUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=RefUML_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage15: BinaryAssociation = BinaryAssociation(
    name="nestingPackage15",
    ends={
        Property(name="Package16", type=RefUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=RefUML_Package, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement11: BinaryAssociation = BinaryAssociation(
    name="packagedElement11",
    ends={
        Property(name="RefUML_PackageableElement", type=RefUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Package", type=RefUML_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage13: BinaryAssociation = BinaryAssociation(
    name="nestedPackage13",
    ends={
        Property(name="Package", type=RefUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=RefUML_Package, multiplicity=Multiplicity(0, 9999))
    }
)
clientDependency17: BinaryAssociation = BinaryAssociation(
    name="clientDependency17",
    ends={
        Property(name="Dependency", type=RefUML_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=RefUML_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
namespace18: BinaryAssociation = BinaryAssociation(
    name="namespace18",
    ends={
        Property(name="Namespace", type=RefUML_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=RefUML_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
supplier20: BinaryAssociation = BinaryAssociation(
    name="supplier20",
    ends={
        Property(name="RefUML_NamedElement21", type=RefUML_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Dependency", type=RefUML_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client22: BinaryAssociation = BinaryAssociation(
    name="client22",
    ends={
        Property(name="NamedElement", type=RefUML_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=RefUML_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="RefUML_Element24", type=RefUML_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_DirectedRelationship", type=RefUML_Element, multiplicity=Multiplicity(1, 9999))
    }
)
nameExpression19: BinaryAssociation = BinaryAssociation(
    name="nameExpression19",
    ends={
        Property(name="RefUML_StringExpression", type=RefUML_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_NamedElement", type=RefUML_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relatedElement28: BinaryAssociation = BinaryAssociation(
    name="relatedElement28",
    ends={
        Property(name="RefUML_Element29", type=RefUML_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Relationship", type=RefUML_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="RefUML_Element27", type=RefUML_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_DirectedRelationship26", type=RefUML_Element, multiplicity=Multiplicity(1, 9999))
    }
)
member34: BinaryAssociation = BinaryAssociation(
    name="member34",
    ends={
        Property(name="RefUML_NamedElement35", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Namespace", type=RefUML_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember36: BinaryAssociation = BinaryAssociation(
    name="importedMember36",
    ends={
        Property(name="RefUML_PackageableElement38", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Namespace37", type=RefUML_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember39: BinaryAssociation = BinaryAssociation(
    name="ownedMember39",
    ends={
        Property(name="NamedElement40", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=RefUML_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
elementImport30: BinaryAssociation = BinaryAssociation(
    name="elementImport30",
    ends={
        Property(name="ElementImport", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=RefUML_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport31: BinaryAssociation = BinaryAssociation(
    name="packageImport31",
    ends={
        Property(name="PackageImport", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace32", type=RefUML_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule33: BinaryAssociation = BinaryAssociation(
    name="ownedRule33",
    ends={
        Property(name="Constraintx", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=RefUML_Constraintx, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement41: BinaryAssociation = BinaryAssociation(
    name="importedElement41",
    ends={
        Property(name="RefUML_PackageableElement42", type=RefUML_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_ElementImport", type=RefUML_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace43: BinaryAssociation = BinaryAssociation(
    name="importingNamespace43",
    ends={
        Property(name="Namespace44", type=RefUML_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElement49: BinaryAssociation = BinaryAssociation(
    name="constrainedElement49",
    ends={
        Property(name="RefUML_Element50", type=RefUML_Constraintx, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Constraintx", type=RefUML_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification51: BinaryAssociation = BinaryAssociation(
    name="specification51",
    ends={
        Property(name="RefUML_ValueSpecification", type=RefUML_Constraintx, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Constraintx52", type=RefUML_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context53: BinaryAssociation = BinaryAssociation(
    name="context53",
    ends={
        Property(name="Namespace54", type=RefUML_Constraintx, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=RefUML_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
importedPackage45: BinaryAssociation = BinaryAssociation(
    name="importedPackage45",
    ends={
        Property(name="RefUML_Package46", type=RefUML_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_PackageImport", type=RefUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace47: BinaryAssociation = BinaryAssociation(
    name="importingNamespace47",
    ends={
        Property(name="Namespace48", type=RefUML_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=RefUML_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="RefUML_Type", type=RefUML_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_TypedElement", type=RefUML_Type, multiplicity=Multiplicity(0, 1))
    }
)
package56: BinaryAssociation = BinaryAssociation(
    name="package56",
    ends={
        Property(name="Package57", type=RefUML_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=RefUML_Package, multiplicity=Multiplicity(0, 1))
    }
)
endType61: BinaryAssociation = BinaryAssociation(
    name="endType61",
    ends={
        Property(name="RefUML_Type62", type=RefUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Association", type=RefUML_Type, multiplicity=Multiplicity(1, 9999))
    }
)
navigableOwnedEnd63: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd63",
    ends={
        Property(name="RefUML_Property", type=RefUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Association64", type=RefUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd58: BinaryAssociation = BinaryAssociation(
    name="ownedEnd58",
    ends={
        Property(name="Property", type=RefUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=RefUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd59: BinaryAssociation = BinaryAssociation(
    name="memberEnd59",
    ends={
        Property(name="Property60", type=RefUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=RefUML_Property, multiplicity=Multiplicity(2, 9999))
    }
)
generalization65: BinaryAssociation = BinaryAssociation(
    name="generalization65",
    ends={
        Property(name="Generalization", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=RefUML_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritedMember68: BinaryAssociation = BinaryAssociation(
    name="inheritedMember68",
    ends={
        Property(name="RefUML_NamedElement69", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Classifier", type=RefUML_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier71: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier71",
    ends={
        Property(name="RefUML_Classifier72", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Classifier70", type=RefUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general74: BinaryAssociation = BinaryAssociation(
    name="general74",
    ends={
        Property(name="RefUML_Classifier75", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Classifier73", type=RefUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
powertypeExtent66: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent66",
    ends={
        Property(name="GeneralizationSet", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=RefUML_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
feature67: BinaryAssociation = BinaryAssociation(
    name="feature67",
    ends={
        Property(name="Feature", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=RefUML_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement80: BinaryAssociation = BinaryAssociation(
    name="redefinedElement80",
    ends={
        Property(name="RefUML_RedefinableElement", type=RefUML_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_RedefinableElement79", type=RefUML_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute76: BinaryAssociation = BinaryAssociation(
    name="attribute76",
    ends={
        Property(name="RefUML_Property78", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Classifier77", type=RefUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general84: BinaryAssociation = BinaryAssociation(
    name="general84",
    ends={
        Property(name="RefUML_Classifier85", type=RefUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Generalization", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet86: BinaryAssociation = BinaryAssociation(
    name="generalizationSet86",
    ends={
        Property(name="GeneralizationSet87", type=RefUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=RefUML_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext81: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext81",
    ends={
        Property(name="RefUML_Classifier83", type=RefUML_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_RedefinableElement82", type=RefUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
powertype90: BinaryAssociation = BinaryAssociation(
    name="powertype90",
    ends={
        Property(name="Classifier91", type=RefUML_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=RefUML_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization92: BinaryAssociation = BinaryAssociation(
    name="generalization92",
    ends={
        Property(name="Generalization93", type=RefUML_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=RefUML_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
specific88: BinaryAssociation = BinaryAssociation(
    name="specific88",
    ends={
        Property(name="Classifier", type=RefUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization89", type=RefUML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
featuringClassifier94: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier94",
    ends={
        Property(name="Classifier95", type=RefUML_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=RefUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
upperValue96: BinaryAssociation = BinaryAssociation(
    name="upperValue96",
    ends={
        Property(name="RefUML_ValueSpecification97", type=RefUML_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_MultiplicityElement", type=RefUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue98: BinaryAssociation = BinaryAssociation(
    name="lowerValue98",
    ends={
        Property(name="RefUML_ValueSpecification100", type=RefUML_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_MultiplicityElement99", type=RefUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class101: BinaryAssociation = BinaryAssociation(
    name="class101",
    ends={
        Property(name="Class", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=RefUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty105: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty105",
    ends={
        Property(name="RefUML_Property106", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Property104", type=RefUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
datatype102: BinaryAssociation = BinaryAssociation(
    name="datatype102",
    ends={
        Property(name="DataType", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute103", type=RefUML_DataType, multiplicity=Multiplicity(0, 1))
    }
)
opposite112: BinaryAssociation = BinaryAssociation(
    name="opposite112",
    ends={
        Property(name="RefUML_Property113", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Property111", type=RefUML_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty115: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty115",
    ends={
        Property(name="RefUML_Property116", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Property114", type=RefUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
association117: BinaryAssociation = BinaryAssociation(
    name="association117",
    ends={
        Property(name="Association118", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=RefUML_Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation107: BinaryAssociation = BinaryAssociation(
    name="owningAssociation107",
    ends={
        Property(name="Association", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=RefUML_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue108: BinaryAssociation = BinaryAssociation(
    name="defaultValue108",
    ends={
        Property(name="RefUML_ValueSpecification110", type=RefUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Property109", type=RefUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedClassifier119: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier119",
    ends={
        Property(name="RefUML_Classifier120", type=RefUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Class", type=RefUML_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass122: BinaryAssociation = BinaryAssociation(
    name="superClass122",
    ends={
        Property(name="RefUML_Class123", type=RefUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Class121", type=RefUML_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute124: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute124",
    ends={
        Property(name="Property125", type=RefUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=RefUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute126: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute126",
    ends={
        Property(name="Property127", type=RefUML_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=RefUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mergedPackage135: BinaryAssociation = BinaryAssociation(
    name="mergedPackage135",
    ends={
        Property(name="RefUML_Package136", type=RefUML_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_PackageMerge", type=RefUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage137: BinaryAssociation = BinaryAssociation(
    name="receivingPackage137",
    ends={
        Property(name="Package138", type=RefUML_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=RefUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
subExpression129: BinaryAssociation = BinaryAssociation(
    name="subExpression129",
    ends={
        Property(name="StringExpression", type=RefUML_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="owningExpression", type=RefUML_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningExpression131: BinaryAssociation = BinaryAssociation(
    name="owningExpression131",
    ends={
        Property(name="StringExpression132", type=RefUML_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="subExpression", type=RefUML_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand133: BinaryAssociation = BinaryAssociation(
    name="operand133",
    ends={
        Property(name="RefUML_ValueSpecification134", type=RefUML_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Expression", type=RefUML_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slot143: BinaryAssociation = BinaryAssociation(
    name="slot143",
    ends={
        Property(name="Slot", type=RefUML_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=RefUML_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral139: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral139",
    ends={
        Property(name="EnumerationLiteral", type=RefUML_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=RefUML_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration140: BinaryAssociation = BinaryAssociation(
    name="enumeration140",
    ends={
        Property(name="Enumeration", type=RefUML_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=RefUML_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
classifier141: BinaryAssociation = BinaryAssociation(
    name="classifier141",
    ends={
        Property(name="RefUML_Classifier142", type=RefUML_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_InstanceSpecification", type=RefUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
specification144: BinaryAssociation = BinaryAssociation(
    name="specification144",
    ends={
        Property(name="RefUML_ValueSpecification146", type=RefUML_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_InstanceSpecification145", type=RefUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingFeature147: BinaryAssociation = BinaryAssociation(
    name="definingFeature147",
    ends={
        Property(name="RefUML_StructuralFeature", type=RefUML_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Slot", type=RefUML_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value148: BinaryAssociation = BinaryAssociation(
    name="value148",
    ends={
        Property(name="RefUML_ValueSpecification150", type=RefUML_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_Slot149", type=RefUML_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance151: BinaryAssociation = BinaryAssociation(
    name="owningInstance151",
    ends={
        Property(name="InstanceSpecification", type=RefUML_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=RefUML_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
instance152: BinaryAssociation = BinaryAssociation(
    name="instance152",
    ends={
        Property(name="RefUML_InstanceSpecification153", type=RefUML_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="RefUML_InstanceValue", type=RefUML_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_RefUML_Comment_Element = Generalization(general=Element, specific=RefUML_Comment)
gen_RefUML_Element_EModelElement = Generalization(general=EModelElement, specific=RefUML_Element)
gen_RefUML_Package_Namespace = Generalization(general=Namespace, specific=RefUML_Package)
gen_RefUML_Package_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_Package)
gen_RefUML_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=RefUML_PackageableElement)
gen_RefUML_NamedElement_Element = Generalization(general=Element, specific=RefUML_NamedElement)
gen_RefUML_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=RefUML_DirectedRelationship)
gen_RefUML_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_Dependency)
gen_RefUML_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefUML_Dependency)
gen_RefUML_Namespace_NamedElement = Generalization(general=NamedElement, specific=RefUML_Namespace)
gen_RefUML_Relationship_Element = Generalization(general=Element, specific=RefUML_Relationship)
gen_RefUML_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefUML_PackageImport)
gen_RefUML_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefUML_ElementImport)
gen_RefUML_Constraintx_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_Constraintx)
gen_RefUML_TypedElement_NamedElement = Generalization(general=NamedElement, specific=RefUML_TypedElement)
gen_RefUML_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_ValueSpecification)
gen_RefUML_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=RefUML_ValueSpecification)
gen_RefUML_Type_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_Type)
gen_RefUML_Association_Classifier = Generalization(general=Classifier, specific=RefUML_Association)
gen_RefUML_Association_Relationship = Generalization(general=Relationship, specific=RefUML_Association)
gen_RefUML_Classifier_Namespace = Generalization(general=Namespace, specific=RefUML_Classifier)
gen_RefUML_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=RefUML_Classifier)
gen_RefUML_Classifier_Type = Generalization(general=Type, specific=RefUML_Classifier)
gen_RefUML_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=RefUML_RedefinableElement)
gen_RefUML_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefUML_Generalization)
gen_RefUML_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=RefUML_Feature)
gen_RefUML_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_GeneralizationSet)
gen_RefUML_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=RefUML_OpaqueExpression)
gen_RefUML_MultiplicityElement_Element = Generalization(general=Element, specific=RefUML_MultiplicityElement)
gen_RefUML_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=RefUML_Property)
gen_RefUML_Class_Classifier = Generalization(general=Classifier, specific=RefUML_Class)
gen_RefUML_Model_Package = Generalization(general=Package, specific=RefUML_Model)
gen_RefUML_DataType_Classifier = Generalization(general=Classifier, specific=RefUML_DataType)
gen_RefUML_StructuralFeature_Feature = Generalization(general=Feature, specific=RefUML_StructuralFeature)
gen_RefUML_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=RefUML_StructuralFeature)
gen_RefUML_StringExpression_Expression = Generalization(general=Expression, specific=RefUML_StringExpression)
gen_RefUML_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=RefUML_StructuralFeature)
gen_RefUML_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=RefUML_Expression)
gen_RefUML_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefUML_PackageMerge)
gen_RefUML_Enumeration_DataType = Generalization(general=DataType, specific=RefUML_Enumeration)
gen_RefUML_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=RefUML_EnumerationLiteral)
gen_RefUML_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=RefUML_InstanceSpecification)
gen_RefUML_PrimitiveType_DataType = Generalization(general=DataType, specific=RefUML_PrimitiveType)
gen_RefUML_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=RefUML_LiteralSpecification)
gen_RefUML_Slot_Element = Generalization(general=Element, specific=RefUML_Slot)
gen_RefUML_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefUML_LiteralInteger)
gen_RefUML_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefUML_LiteralString)
gen_RefUML_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefUML_LiteralNull)
gen_RefUML_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefUML_LiteralBoolean)
gen_RefUML_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=RefUML_InstanceValue)
gen_RefUML_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefUML_LiteralUnlimitedNatural)

# Domain Model
domain_model = DomainModel(
    name="RefUML",
    types={RefUML_Comment, Element, RefUML_Element, EModelElement, RefUML_Package, Namespace, PackageableElement, RefUML_Type, RefUML_PackageMerge, NamedElement, RefUML_NamedElement, RefUML_PackageableElement, RefUML_Dependency, RefUML_Namespace, RefUML_DirectedRelationship, Relationship, RefUML_StringExpression, DirectedRelationship, RefUML_Relationship, RefUML_ElementImport, RefUML_PackageImport, RefUML_Constraintx, RefUML_ValueSpecification, RefUML_TypedElement, TypedElement, RefUML_Association, Classifier, RefUML_Property, RefUML_Classifier, RedefinableElement, Type, RefUML_Generalization, RefUML_GeneralizationSet, RefUML_Feature, RefUML_RedefinableElement, RefUML_OpaqueExpression, ValueSpecification, RefUML_MultiplicityElement, StructuralFeature, RefUML_Class, RefUML_DataType, RefUML_Model, Package, RefUML_StructuralFeature, Feature, Expression, MultiplicityElement, RefUML_Expression, RefUML_Slot, RefUML_Enumeration, DataType, RefUML_EnumerationLiteral, InstanceSpecification, RefUML_InstanceSpecification, RefUML_PrimitiveType, RefUML_LiteralSpecification, RefUML_LiteralInteger, LiteralSpecification, RefUML_LiteralString, RefUML_LiteralNull, RefUML_LiteralBoolean, RefUML_InstanceValue, RefUML_LiteralUnlimitedNatural, VisibilityKind, AggregationKind},
    associations={annotatedElement0, owner4, ownedComment6, ownedElement2, ownedType9, packageMerge10, nestingPackage15, packagedElement11, nestedPackage13, clientDependency17, namespace18, supplier20, client22, source23, nameExpression19, relatedElement28, target25, member34, importedMember36, ownedMember39, elementImport30, packageImport31, ownedRule33, importedElement41, importingNamespace43, constrainedElement49, specification51, context53, importedPackage45, importingNamespace47, type55, package56, endType61, navigableOwnedEnd63, ownedEnd58, memberEnd59, generalization65, inheritedMember68, redefinedClassifier71, general74, powertypeExtent66, feature67, redefinedElement80, attribute76, general84, generalizationSet86, redefinitionContext81, powertype90, generalization92, specific88, featuringClassifier94, upperValue96, lowerValue98, class101, redefinedProperty105, datatype102, opposite112, subsettedProperty115, association117, owningAssociation107, defaultValue108, nestedClassifier119, superClass122, ownedAttribute124, ownedAttribute126, mergedPackage135, receivingPackage137, subExpression129, owningExpression131, operand133, slot143, ownedLiteral139, enumeration140, classifier141, specification144, definingFeature147, value148, owningInstance151, instance152},
    generalizations={gen_RefUML_Comment_Element, gen_RefUML_Element_EModelElement, gen_RefUML_Package_Namespace, gen_RefUML_Package_PackageableElement, gen_RefUML_PackageableElement_NamedElement, gen_RefUML_NamedElement_Element, gen_RefUML_DirectedRelationship_Relationship, gen_RefUML_Dependency_PackageableElement, gen_RefUML_Dependency_DirectedRelationship, gen_RefUML_Namespace_NamedElement, gen_RefUML_Relationship_Element, gen_RefUML_PackageImport_DirectedRelationship, gen_RefUML_ElementImport_DirectedRelationship, gen_RefUML_Constraintx_PackageableElement, gen_RefUML_TypedElement_NamedElement, gen_RefUML_ValueSpecification_PackageableElement, gen_RefUML_ValueSpecification_TypedElement, gen_RefUML_Type_PackageableElement, gen_RefUML_Association_Classifier, gen_RefUML_Association_Relationship, gen_RefUML_Classifier_Namespace, gen_RefUML_Classifier_RedefinableElement, gen_RefUML_Classifier_Type, gen_RefUML_RedefinableElement_NamedElement, gen_RefUML_Generalization_DirectedRelationship, gen_RefUML_Feature_RedefinableElement, gen_RefUML_GeneralizationSet_PackageableElement, gen_RefUML_OpaqueExpression_ValueSpecification, gen_RefUML_MultiplicityElement_Element, gen_RefUML_Property_StructuralFeature, gen_RefUML_Class_Classifier, gen_RefUML_Model_Package, gen_RefUML_DataType_Classifier, gen_RefUML_StructuralFeature_Feature, gen_RefUML_StructuralFeature_TypedElement, gen_RefUML_StringExpression_Expression, gen_RefUML_StructuralFeature_MultiplicityElement, gen_RefUML_Expression_ValueSpecification, gen_RefUML_PackageMerge_DirectedRelationship, gen_RefUML_Enumeration_DataType, gen_RefUML_EnumerationLiteral_InstanceSpecification, gen_RefUML_InstanceSpecification_PackageableElement, gen_RefUML_PrimitiveType_DataType, gen_RefUML_LiteralSpecification_ValueSpecification, gen_RefUML_Slot_Element, gen_RefUML_LiteralInteger_LiteralSpecification, gen_RefUML_LiteralString_LiteralSpecification, gen_RefUML_LiteralNull_LiteralSpecification, gen_RefUML_LiteralBoolean_LiteralSpecification, gen_RefUML_InstanceValue_ValueSpecification, gen_RefUML_LiteralUnlimitedNatural_LiteralSpecification},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)