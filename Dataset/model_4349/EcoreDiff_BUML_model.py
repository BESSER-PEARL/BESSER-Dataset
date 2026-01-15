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

# Classes
ecoreDiff_EAnnotation = Class(name="ecoreDiff::EAnnotation")
EModelElement = Class(name="EModelElement")
ecoreDiff_EStringToStringMapEntry = Class(name="ecoreDiff::EStringToStringMapEntry")
ecoreDiff_EModelElement = Class(name="ecoreDiff::EModelElement", is_abstract=True)
ecoreDiff_EObject = Class(name="ecoreDiff::EObject")
ecoreDiff_EClass = Class(name="ecoreDiff::EClass")
EClassifier = Class(name="EClassifier")
ecoreDiff_EOperation = Class(name="ecoreDiff::EOperation")
ecoreDiff_EAttribute = Class(name="ecoreDiff::EAttribute")
ecoreDiff_EStructuralFeature = Class(name="ecoreDiff::EStructuralFeature", is_abstract=True)
ecoreDiff_EReference = Class(name="ecoreDiff::EReference")
ecoreDiff_EGenericType = Class(name="ecoreDiff::EGenericType")
ecoreDiff_EClassifier = Class(name="ecoreDiff::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecoreDiff_EPackage = Class(name="ecoreDiff::EPackage")
ecoreDiff_ETypeParameter = Class(name="ecoreDiff::ETypeParameter")
ecoreDiff_ENamedElement = Class(name="ecoreDiff::ENamedElement", is_abstract=True)
ecoreDiff_EFactory = Class(name="ecoreDiff::EFactory")
ecoreDiff_EClassifier_Wildcard = Class(name="ecoreDiff::EClassifier::Wildcard")
ecoreDiff_EDataType = Class(name="ecoreDiff::EDataType")
ETypedElement = Class(name="ETypedElement")
EObject = Class(name="EObject")
ecoreDiff_ETypedElement = Class(name="ecoreDiff::ETypedElement", is_abstract=True)
ecoreDiff_EParameter = Class(name="ecoreDiff::EParameter")
ecoreDiff_EStructuralFeature_Wildcard = Class(name="ecoreDiff::EStructuralFeature::Wildcard")
EStructuralFeature = Class(name="EStructuralFeature")
ecoreDiff_EEnum = Class(name="ecoreDiff::EEnum")
EDataType = Class(name="EDataType")
ecoreDiff_EEnumLiteral = Class(name="ecoreDiff::EEnumLiteral")
DifferenceElement = Class(name="DifferenceElement")
ecoreDiff_DifferenceModel = Class(name="ecoreDiff::DifferenceModel")
ecoreDiff_DifferenceElement = Class(name="ecoreDiff::DifferenceElement")
ecoreDiff_AddedEAnnotation = Class(name="ecoreDiff::AddedEAnnotation")
EAnnotation = Class(name="EAnnotation")
ecoreDiff_DeletedEAnnotation = Class(name="ecoreDiff::DeletedEAnnotation")
ecoreDiff_ChangedEAnnotation = Class(name="ecoreDiff::ChangedEAnnotation")
ecoreDiff_AddedEClass = Class(name="ecoreDiff::AddedEClass")
EClass = Class(name="EClass")
ecoreDiff_DeletedEClass = Class(name="ecoreDiff::DeletedEClass")
ecoreDiff_ChangedEClass = Class(name="ecoreDiff::ChangedEClass")
ecoreDiff_AddedEClassifier = Class(name="ecoreDiff::AddedEClassifier")
ecoreDiff_DeletedEClassifier = Class(name="ecoreDiff::DeletedEClassifier")
ecoreDiff_ChangedEClassifier = Class(name="ecoreDiff::ChangedEClassifier")
ecoreDiff_AddedEStringToStringMapEntry = Class(name="ecoreDiff::AddedEStringToStringMapEntry")
EStringToStringMapEntry = Class(name="EStringToStringMapEntry")
ecoreDiff_DeletedEStringToStringMapEntry = Class(name="ecoreDiff::DeletedEStringToStringMapEntry")
ecoreDiff_ChangedEStringToStringMapEntry = Class(name="ecoreDiff::ChangedEStringToStringMapEntry")
ecoreDiff_AddedEObject = Class(name="ecoreDiff::AddedEObject")
ecoreDiff_DeletedEObject = Class(name="ecoreDiff::DeletedEObject")
ecoreDiff_ChangedEObject = Class(name="ecoreDiff::ChangedEObject")
ecoreDiff_AddedEFactory = Class(name="ecoreDiff::AddedEFactory")
EFactory = Class(name="EFactory")
ecoreDiff_DeletedEFactory = Class(name="ecoreDiff::DeletedEFactory")
ecoreDiff_ChangedEFactory = Class(name="ecoreDiff::ChangedEFactory")
ecoreDiff_AddedEDataType = Class(name="ecoreDiff::AddedEDataType")
ecoreDiff_DeletedEDataType = Class(name="ecoreDiff::DeletedEDataType")
ecoreDiff_ChangedEDataType = Class(name="ecoreDiff::ChangedEDataType")
ecoreDiff_AddedENamedElement = Class(name="ecoreDiff::AddedENamedElement")
ecoreDiff_DeletedENamedElement = Class(name="ecoreDiff::DeletedENamedElement")
ecoreDiff_ChangedENamedElement = Class(name="ecoreDiff::ChangedENamedElement")
ecoreDiff_AddedEPackage = Class(name="ecoreDiff::AddedEPackage")
EPackage = Class(name="EPackage")
ecoreDiff_DeletedEPackage = Class(name="ecoreDiff::DeletedEPackage")
ecoreDiff_ChangedEPackage = Class(name="ecoreDiff::ChangedEPackage")
ecoreDiff_AddedEClassifier_Wildcard = Class(name="ecoreDiff::AddedEClassifier::Wildcard")
EClassifier_Wildcard = Class(name="EClassifier::Wildcard")
ecoreDiff_DeletedEClassifier_Wildcard = Class(name="ecoreDiff::DeletedEClassifier::Wildcard")
ecoreDiff_ChangedEClassifier_Wildcard = Class(name="ecoreDiff::ChangedEClassifier::Wildcard")
ecoreDiff_AddedEOperation = Class(name="ecoreDiff::AddedEOperation")
EOperation = Class(name="EOperation")
ecoreDiff_DeletedEOperation = Class(name="ecoreDiff::DeletedEOperation")
ecoreDiff_AddedETypeParameter = Class(name="ecoreDiff::AddedETypeParameter")
ETypeParameter = Class(name="ETypeParameter")
ecoreDiff_DeletedETypeParameter = Class(name="ecoreDiff::DeletedETypeParameter")
ecoreDiff_ChangedETypeParameter = Class(name="ecoreDiff::ChangedETypeParameter")
ecoreDiff_AddedEGenericType = Class(name="ecoreDiff::AddedEGenericType")
EGenericType = Class(name="EGenericType")
ecoreDiff_DeletedEGenericType = Class(name="ecoreDiff::DeletedEGenericType")
ecoreDiff_ChangedEGenericType = Class(name="ecoreDiff::ChangedEGenericType")
ecoreDiff_ChangedEParameter = Class(name="ecoreDiff::ChangedEParameter")
ecoreDiff_AddedEAttribute = Class(name="ecoreDiff::AddedEAttribute")
EAttribute = Class(name="EAttribute")
ecoreDiff_DeletedEAttribute = Class(name="ecoreDiff::DeletedEAttribute")
ecoreDiff_ChangedEAttribute = Class(name="ecoreDiff::ChangedEAttribute")
ecoreDiff_AddedEStructuralFeature = Class(name="ecoreDiff::AddedEStructuralFeature")
ecoreDiff_DeletedEStructuralFeature = Class(name="ecoreDiff::DeletedEStructuralFeature")
ecoreDiff_ChangedEOperation = Class(name="ecoreDiff::ChangedEOperation")
ecoreDiff_AddedETypedElement = Class(name="ecoreDiff::AddedETypedElement")
ecoreDiff_DeletedETypedElement = Class(name="ecoreDiff::DeletedETypedElement")
ecoreDiff_ChangedETypedElement = Class(name="ecoreDiff::ChangedETypedElement")
ecoreDiff_AddedEParameter = Class(name="ecoreDiff::AddedEParameter")
EParameter = Class(name="EParameter")
ecoreDiff_DeletedEParameter = Class(name="ecoreDiff::DeletedEParameter")
ecoreDiff_DeletedEReference = Class(name="ecoreDiff::DeletedEReference")
ecoreDiff_ChangedEReference = Class(name="ecoreDiff::ChangedEReference")
ecoreDiff_AddedEEnum = Class(name="ecoreDiff::AddedEEnum")
EEnum = Class(name="EEnum")
ecoreDiff_DeletedEEnum = Class(name="ecoreDiff::DeletedEEnum")
ecoreDiff_ChangedEEnum = Class(name="ecoreDiff::ChangedEEnum")
ecoreDiff_ChangedEStructuralFeature = Class(name="ecoreDiff::ChangedEStructuralFeature")
ecoreDiff_AddedEStructuralFeature_Wildcard = Class(name="ecoreDiff::AddedEStructuralFeature::Wildcard")
EStructuralFeature_Wildcard = Class(name="EStructuralFeature::Wildcard")
ecoreDiff_DeletedEStructuralFeature_Wildcard = Class(name="ecoreDiff::DeletedEStructuralFeature::Wildcard")
ecoreDiff_ChangedEStructuralFeature_Wildcard = Class(name="ecoreDiff::ChangedEStructuralFeature::Wildcard")
ecoreDiff_AddedEReference = Class(name="ecoreDiff::AddedEReference")
EReference = Class(name="EReference")
ecoreDiff_AddedEEnumLiteral = Class(name="ecoreDiff::AddedEEnumLiteral")
EEnumLiteral = Class(name="EEnumLiteral")
ecoreDiff_DeletedEEnumLiteral = Class(name="ecoreDiff::DeletedEEnumLiteral")
ecoreDiff_ChangedEEnumLiteral = Class(name="ecoreDiff::ChangedEEnumLiteral")
ecoreDiff_AddedEModelElement = Class(name="ecoreDiff::AddedEModelElement")
ecoreDiff_DeletedEModelElement = Class(name="ecoreDiff::DeletedEModelElement")
ecoreDiff_ChangedEModelElement = Class(name="ecoreDiff::ChangedEModelElement")

# ecoreDiff_EAnnotation class attributes and methods
ecoreDiff_EAnnotation_source: Property = Property(name="source", type=StringType)
ecoreDiff_EAnnotation.attributes={ecoreDiff_EAnnotation_source}

# EModelElement class attributes and methods

# ecoreDiff_EStringToStringMapEntry class attributes and methods
ecoreDiff_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecoreDiff_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecoreDiff_EStringToStringMapEntry.attributes={ecoreDiff_EStringToStringMapEntry_key, ecoreDiff_EStringToStringMapEntry_value}

# ecoreDiff_EModelElement class attributes and methods

# ecoreDiff_EObject class attributes and methods

# ecoreDiff_EClass class attributes and methods
ecoreDiff_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecoreDiff_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecoreDiff_EClass.attributes={ecoreDiff_EClass_abstract, ecoreDiff_EClass_interface}

# EClassifier class attributes and methods

# ecoreDiff_EOperation class attributes and methods

# ecoreDiff_EAttribute class attributes and methods
ecoreDiff_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecoreDiff_EAttribute.attributes={ecoreDiff_EAttribute_iD}

# ecoreDiff_EStructuralFeature class attributes and methods
ecoreDiff_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecoreDiff_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecoreDiff_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecoreDiff_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecoreDiff_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecoreDiff_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecoreDiff_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecoreDiff_EStructuralFeature.attributes={ecoreDiff_EStructuralFeature_unsettable, ecoreDiff_EStructuralFeature_defaultValue, ecoreDiff_EStructuralFeature_defaultValueLiteral, ecoreDiff_EStructuralFeature_transient, ecoreDiff_EStructuralFeature_changeable, ecoreDiff_EStructuralFeature_volatile, ecoreDiff_EStructuralFeature_derived}

# ecoreDiff_EReference class attributes and methods
ecoreDiff_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecoreDiff_EReference_container: Property = Property(name="container", type=BooleanType)
ecoreDiff_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecoreDiff_EReference.attributes={ecoreDiff_EReference_containment, ecoreDiff_EReference_resolveProxies, ecoreDiff_EReference_container}

# ecoreDiff_EGenericType class attributes and methods

# ecoreDiff_EClassifier class attributes and methods
ecoreDiff_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecoreDiff_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecoreDiff_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecoreDiff_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecoreDiff_EClassifier.attributes={ecoreDiff_EClassifier_defaultValue, ecoreDiff_EClassifier_instanceClass, ecoreDiff_EClassifier_instanceTypeName, ecoreDiff_EClassifier_instanceClassName}

# ENamedElement class attributes and methods

# ecoreDiff_EPackage class attributes and methods
ecoreDiff_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecoreDiff_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecoreDiff_EPackage.attributes={ecoreDiff_EPackage_nsURI, ecoreDiff_EPackage_nsPrefix}

# ecoreDiff_ETypeParameter class attributes and methods

# ecoreDiff_ENamedElement class attributes and methods
ecoreDiff_ENamedElement_name: Property = Property(name="name", type=StringType)
ecoreDiff_ENamedElement.attributes={ecoreDiff_ENamedElement_name}

# ecoreDiff_EFactory class attributes and methods

# ecoreDiff_EClassifier_Wildcard class attributes and methods

# ecoreDiff_EDataType class attributes and methods
ecoreDiff_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecoreDiff_EDataType.attributes={ecoreDiff_EDataType_serializable}

# ETypedElement class attributes and methods

# EObject class attributes and methods

# ecoreDiff_ETypedElement class attributes and methods
ecoreDiff_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecoreDiff_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecoreDiff_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecoreDiff_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecoreDiff_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecoreDiff_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecoreDiff_ETypedElement.attributes={ecoreDiff_ETypedElement_required, ecoreDiff_ETypedElement_ordered, ecoreDiff_ETypedElement_upperBound, ecoreDiff_ETypedElement_many, ecoreDiff_ETypedElement_unique, ecoreDiff_ETypedElement_lowerBound}

# ecoreDiff_EParameter class attributes and methods

# ecoreDiff_EStructuralFeature_Wildcard class attributes and methods

# EStructuralFeature class attributes and methods

# ecoreDiff_EEnum class attributes and methods

# EDataType class attributes and methods

# ecoreDiff_EEnumLiteral class attributes and methods
ecoreDiff_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecoreDiff_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecoreDiff_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecoreDiff_EEnumLiteral.attributes={ecoreDiff_EEnumLiteral_instance, ecoreDiff_EEnumLiteral_value, ecoreDiff_EEnumLiteral_literal}

# DifferenceElement class attributes and methods

# ecoreDiff_DifferenceModel class attributes and methods

# ecoreDiff_DifferenceElement class attributes and methods

# ecoreDiff_AddedEAnnotation class attributes and methods

# EAnnotation class attributes and methods

# ecoreDiff_DeletedEAnnotation class attributes and methods

# ecoreDiff_ChangedEAnnotation class attributes and methods

# ecoreDiff_AddedEClass class attributes and methods

# EClass class attributes and methods

# ecoreDiff_DeletedEClass class attributes and methods

# ecoreDiff_ChangedEClass class attributes and methods

# ecoreDiff_AddedEClassifier class attributes and methods

# ecoreDiff_DeletedEClassifier class attributes and methods

# ecoreDiff_ChangedEClassifier class attributes and methods

# ecoreDiff_AddedEStringToStringMapEntry class attributes and methods

# EStringToStringMapEntry class attributes and methods

# ecoreDiff_DeletedEStringToStringMapEntry class attributes and methods

# ecoreDiff_ChangedEStringToStringMapEntry class attributes and methods

# ecoreDiff_AddedEObject class attributes and methods

# ecoreDiff_DeletedEObject class attributes and methods

# ecoreDiff_ChangedEObject class attributes and methods

# ecoreDiff_AddedEFactory class attributes and methods

# EFactory class attributes and methods

# ecoreDiff_DeletedEFactory class attributes and methods

# ecoreDiff_ChangedEFactory class attributes and methods

# ecoreDiff_AddedEDataType class attributes and methods

# ecoreDiff_DeletedEDataType class attributes and methods

# ecoreDiff_ChangedEDataType class attributes and methods

# ecoreDiff_AddedENamedElement class attributes and methods

# ecoreDiff_DeletedENamedElement class attributes and methods

# ecoreDiff_ChangedENamedElement class attributes and methods

# ecoreDiff_AddedEPackage class attributes and methods

# EPackage class attributes and methods

# ecoreDiff_DeletedEPackage class attributes and methods

# ecoreDiff_ChangedEPackage class attributes and methods

# ecoreDiff_AddedEClassifier_Wildcard class attributes and methods

# EClassifier_Wildcard class attributes and methods

# ecoreDiff_DeletedEClassifier_Wildcard class attributes and methods

# ecoreDiff_ChangedEClassifier_Wildcard class attributes and methods

# ecoreDiff_AddedEOperation class attributes and methods

# EOperation class attributes and methods

# ecoreDiff_DeletedEOperation class attributes and methods

# ecoreDiff_AddedETypeParameter class attributes and methods

# ETypeParameter class attributes and methods

# ecoreDiff_DeletedETypeParameter class attributes and methods

# ecoreDiff_ChangedETypeParameter class attributes and methods

# ecoreDiff_AddedEGenericType class attributes and methods

# EGenericType class attributes and methods

# ecoreDiff_DeletedEGenericType class attributes and methods

# ecoreDiff_ChangedEGenericType class attributes and methods

# ecoreDiff_ChangedEParameter class attributes and methods

# ecoreDiff_AddedEAttribute class attributes and methods

# EAttribute class attributes and methods

# ecoreDiff_DeletedEAttribute class attributes and methods

# ecoreDiff_ChangedEAttribute class attributes and methods

# ecoreDiff_AddedEStructuralFeature class attributes and methods

# ecoreDiff_DeletedEStructuralFeature class attributes and methods

# ecoreDiff_ChangedEOperation class attributes and methods

# ecoreDiff_AddedETypedElement class attributes and methods

# ecoreDiff_DeletedETypedElement class attributes and methods

# ecoreDiff_ChangedETypedElement class attributes and methods

# ecoreDiff_AddedEParameter class attributes and methods

# EParameter class attributes and methods

# ecoreDiff_DeletedEParameter class attributes and methods

# ecoreDiff_DeletedEReference class attributes and methods

# ecoreDiff_ChangedEReference class attributes and methods

# ecoreDiff_AddedEEnum class attributes and methods

# EEnum class attributes and methods

# ecoreDiff_DeletedEEnum class attributes and methods

# ecoreDiff_ChangedEEnum class attributes and methods

# ecoreDiff_ChangedEStructuralFeature class attributes and methods

# ecoreDiff_AddedEStructuralFeature_Wildcard class attributes and methods

# EStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_DeletedEStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_ChangedEStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_AddedEReference class attributes and methods

# EReference class attributes and methods

# ecoreDiff_AddedEEnumLiteral class attributes and methods

# EEnumLiteral class attributes and methods

# ecoreDiff_DeletedEEnumLiteral class attributes and methods

# ecoreDiff_ChangedEEnumLiteral class attributes and methods

# ecoreDiff_AddedEModelElement class attributes and methods

# ecoreDiff_DeletedEModelElement class attributes and methods

# ecoreDiff_ChangedEModelElement class attributes and methods

# Relationships
eSuperTypes8: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes8",
    ends={
        Property(name="ecoreDiff_EClass7", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 9999)),
        Property(name="ecoreDiff_EClass", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1))
    }
)
details0: BinaryAssociation = BinaryAssociation(
    name="details0",
    ends={
        Property(name="ecoreDiff_EStringToStringMapEntry", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAnnotation", type=ecoreDiff_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement1: BinaryAssociation = BinaryAssociation(
    name="eModelElement1",
    ends={
        Property(name="EModelElement", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents2: BinaryAssociation = BinaryAssociation(
    name="contents2",
    ends={
        Property(name="ecoreDiff_EObject", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAnnotation3", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references4: BinaryAssociation = BinaryAssociation(
    name="references4",
    ends={
        Property(name="ecoreDiff_EObject6", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAnnotation5", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="ecoreDiff_EReference24", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass23", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="ecoreDiff_EOperation", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass26", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations9: BinaryAssociation = BinaryAssociation(
    name="eOperations9",
    ends={
        Property(name="EOperation", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes10: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes10",
    ends={
        Property(name="ecoreDiff_EAttribute", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass11", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eStructuralFeatures12: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures12",
    ends={
        Property(name="EStructuralFeature", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass13", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="ecoreDiff_EReference", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass15", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="ecoreDiff_EReference18", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass17", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="ecoreDiff_EAttribute21", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass20", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="ecoreDiff_EStructuralFeature", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass28", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="ecoreDiff_EClass31", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass29", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="ecoreDiff_EAttribute34", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass33", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eGenericSuperTypes35: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes35",
    ends={
        Property(name="ecoreDiff_EGenericType", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass36", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes37",
    ends={
        Property(name="ecoreDiff_EGenericType39", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass38", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eFactoryInstance42: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance42",
    ends={
        Property(name="ePackage", type=ecoreDiff_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="EFactory", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eSubpackages44: BinaryAssociation = BinaryAssociation(
    name="eSubpackages44",
    ends={
        Property(name="EPackage45", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage47: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage47",
    ends={
        Property(name="EPackage48", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eClassifiers49: BinaryAssociation = BinaryAssociation(
    name="eClassifiers49",
    ends={
        Property(name="EClassifier", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage50", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage40: BinaryAssociation = BinaryAssociation(
    name="ePackage40",
    ends={
        Property(name="EPackage", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters41: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters41",
    ends={
        Property(name="ecoreDiff_ETypeParameter", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClassifier", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage51: BinaryAssociation = BinaryAssociation(
    name="ePackage51",
    ends={
        Property(name="EPackage52", type=ecoreDiff_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eBounds53: BinaryAssociation = BinaryAssociation(
    name="eBounds53",
    ends={
        Property(name="ecoreDiff_EGenericType55", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypeParameter54", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound57: BinaryAssociation = BinaryAssociation(
    name="eUpperBound57",
    ends={
        Property(name="ecoreDiff_EGenericType58", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType56", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments60: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments60",
    ends={
        Property(name="ecoreDiff_EGenericType61", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType59", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType62: BinaryAssociation = BinaryAssociation(
    name="eRawType62",
    ends={
        Property(name="ecoreDiff_EClassifier64", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType63", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound66: BinaryAssociation = BinaryAssociation(
    name="eLowerBound66",
    ends={
        Property(name="ecoreDiff_EGenericType67", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType65", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter68: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter68",
    ends={
        Property(name="ecoreDiff_ETypeParameter70", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType69", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier71: BinaryAssociation = BinaryAssociation(
    name="eClassifier71",
    ends={
        Property(name="ecoreDiff_EClassifier73", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType72", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eType85: BinaryAssociation = BinaryAssociation(
    name="eType85",
    ends={
        Property(name="ecoreDiff_EObject86", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType87: BinaryAssociation = BinaryAssociation(
    name="eGenericType87",
    ends={
        Property(name="ecoreDiff_EGenericType89", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypedElement88", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameters74: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters74",
    ends={
        Property(name="ecoreDiff_ETypeParameter76", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation75", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters77: BinaryAssociation = BinaryAssociation(
    name="eParameters77",
    ends={
        Property(name="EParameter", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecoreDiff_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions78: BinaryAssociation = BinaryAssociation(
    name="eExceptions78",
    ends={
        Property(name="ecoreDiff_EClassifier80", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation79", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions81: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions81",
    ends={
        Property(name="ecoreDiff_EGenericType83", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation82", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass84: BinaryAssociation = BinaryAssociation(
    name="eContainingClass84",
    ends={
        Property(name="EClass", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOperation90: BinaryAssociation = BinaryAssociation(
    name="eOperation90",
    ends={
        Property(name="EOperation91", type=ecoreDiff_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eAttributeType92: BinaryAssociation = BinaryAssociation(
    name="eAttributeType92",
    ends={
        Property(name="ecoreDiff_EDataType", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAttribute93", type=ecoreDiff_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eOpposite97: BinaryAssociation = BinaryAssociation(
    name="eOpposite97",
    ends={
        Property(name="ecoreDiff_EReference98", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference96", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType99: BinaryAssociation = BinaryAssociation(
    name="eReferenceType99",
    ends={
        Property(name="ecoreDiff_EClass101", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference100", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eContainingClass94: BinaryAssociation = BinaryAssociation(
    name="eContainingClass94",
    ends={
        Property(name="EClass95", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eKeys102: BinaryAssociation = BinaryAssociation(
    name="eKeys102",
    ends={
        Property(name="ecoreDiff_EAttribute104", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference103", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eLiterals105: BinaryAssociation = BinaryAssociation(
    name="eLiterals105",
    ends={
        Property(name="EEnumLiteral", type=ecoreDiff_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum106: BinaryAssociation = BinaryAssociation(
    name="eEnum106",
    ends={
        Property(name="EEnum", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecoreDiff_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations107: BinaryAssociation = BinaryAssociation(
    name="eAnnotations107",
    ends={
        Property(name="EAnnotation", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
differenceElements108: BinaryAssociation = BinaryAssociation(
    name="differenceElements108",
    ends={
        Property(name="ecoreDiff_DifferenceElement", type=ecoreDiff_DifferenceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DifferenceModel", type=ecoreDiff_DifferenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationElement109: BinaryAssociation = BinaryAssociation(
    name="applicationElement109",
    ends={
        Property(name="ecoreDiff_EObject110", type=ecoreDiff_DeletedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEAnnotation", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement111: BinaryAssociation = BinaryAssociation(
    name="updatedElement111",
    ends={
        Property(name="ecoreDiff_EAnnotation112", type=ecoreDiff_ChangedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAnnotation", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement130: BinaryAssociation = BinaryAssociation(
    name="applicationElement130",
    ends={
        Property(name="ecoreDiff_EObject131", type=ecoreDiff_DeletedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEClass", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement132: BinaryAssociation = BinaryAssociation(
    name="updatedElement132",
    ends={
        Property(name="ecoreDiff_EClass133", type=ecoreDiff_ChangedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClass", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement134: BinaryAssociation = BinaryAssociation(
    name="applicationElement134",
    ends={
        Property(name="ecoreDiff_EObject136", type=ecoreDiff_ChangedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClass135", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement137: BinaryAssociation = BinaryAssociation(
    name="applicationElement137",
    ends={
        Property(name="ecoreDiff_EObject138", type=ecoreDiff_DeletedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEClassifier", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement139: BinaryAssociation = BinaryAssociation(
    name="updatedElement139",
    ends={
        Property(name="ecoreDiff_EClassifier140", type=ecoreDiff_ChangedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement113: BinaryAssociation = BinaryAssociation(
    name="applicationElement113",
    ends={
        Property(name="ecoreDiff_EObject115", type=ecoreDiff_ChangedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAnnotation114", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement116: BinaryAssociation = BinaryAssociation(
    name="applicationElement116",
    ends={
        Property(name="ecoreDiff_EObject117", type=ecoreDiff_DeletedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEStringToStringMapEntry", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement118: BinaryAssociation = BinaryAssociation(
    name="updatedElement118",
    ends={
        Property(name="ecoreDiff_EStringToStringMapEntry119", type=ecoreDiff_ChangedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStringToStringMapEntry", type=ecoreDiff_EStringToStringMapEntry, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement120: BinaryAssociation = BinaryAssociation(
    name="applicationElement120",
    ends={
        Property(name="ecoreDiff_EObject122", type=ecoreDiff_ChangedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStringToStringMapEntry121", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement123: BinaryAssociation = BinaryAssociation(
    name="applicationElement123",
    ends={
        Property(name="ecoreDiff_EObject124", type=ecoreDiff_DeletedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEObject", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement125: BinaryAssociation = BinaryAssociation(
    name="updatedElement125",
    ends={
        Property(name="ecoreDiff_EObject126", type=ecoreDiff_ChangedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEObject", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement127: BinaryAssociation = BinaryAssociation(
    name="applicationElement127",
    ends={
        Property(name="ecoreDiff_EObject129", type=ecoreDiff_ChangedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEObject128", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement153: BinaryAssociation = BinaryAssociation(
    name="applicationElement153",
    ends={
        Property(name="ecoreDiff_EObject155", type=ecoreDiff_ChangedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEPackage154", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement156: BinaryAssociation = BinaryAssociation(
    name="applicationElement156",
    ends={
        Property(name="ecoreDiff_EObject157", type=ecoreDiff_DeletedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEFactory", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement158: BinaryAssociation = BinaryAssociation(
    name="updatedElement158",
    ends={
        Property(name="ecoreDiff_EFactory", type=ecoreDiff_ChangedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEFactory", type=ecoreDiff_EFactory, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement159: BinaryAssociation = BinaryAssociation(
    name="applicationElement159",
    ends={
        Property(name="ecoreDiff_EObject161", type=ecoreDiff_ChangedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEFactory160", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement162: BinaryAssociation = BinaryAssociation(
    name="applicationElement162",
    ends={
        Property(name="ecoreDiff_EObject163", type=ecoreDiff_DeletedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEDataType", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement141: BinaryAssociation = BinaryAssociation(
    name="applicationElement141",
    ends={
        Property(name="ecoreDiff_EObject143", type=ecoreDiff_ChangedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier142", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement144: BinaryAssociation = BinaryAssociation(
    name="applicationElement144",
    ends={
        Property(name="ecoreDiff_EObject145", type=ecoreDiff_DeletedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedENamedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement146: BinaryAssociation = BinaryAssociation(
    name="updatedElement146",
    ends={
        Property(name="ecoreDiff_ENamedElement", type=ecoreDiff_ChangedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedENamedElement", type=ecoreDiff_ENamedElement, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement147: BinaryAssociation = BinaryAssociation(
    name="applicationElement147",
    ends={
        Property(name="ecoreDiff_EObject149", type=ecoreDiff_ChangedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedENamedElement148", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement150: BinaryAssociation = BinaryAssociation(
    name="applicationElement150",
    ends={
        Property(name="ecoreDiff_EObject151", type=ecoreDiff_DeletedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEPackage", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement152: BinaryAssociation = BinaryAssociation(
    name="updatedElement152",
    ends={
        Property(name="ecoreDiff_EPackage", type=ecoreDiff_ChangedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEPackage", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement178: BinaryAssociation = BinaryAssociation(
    name="updatedElement178",
    ends={
        Property(name="ecoreDiff_EGenericType179", type=ecoreDiff_ChangedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEGenericType", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement180: BinaryAssociation = BinaryAssociation(
    name="applicationElement180",
    ends={
        Property(name="ecoreDiff_EObject182", type=ecoreDiff_ChangedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEGenericType181", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement183: BinaryAssociation = BinaryAssociation(
    name="applicationElement183",
    ends={
        Property(name="ecoreDiff_EObject184", type=ecoreDiff_DeletedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEClassifier_Wildcard", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement185: BinaryAssociation = BinaryAssociation(
    name="updatedElement185",
    ends={
        Property(name="ecoreDiff_EClassifier_Wildcard", type=ecoreDiff_ChangedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier_Wildcard", type=ecoreDiff_EClassifier_Wildcard, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement186: BinaryAssociation = BinaryAssociation(
    name="applicationElement186",
    ends={
        Property(name="ecoreDiff_EObject188", type=ecoreDiff_ChangedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier_Wildcard187", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement189: BinaryAssociation = BinaryAssociation(
    name="applicationElement189",
    ends={
        Property(name="ecoreDiff_EObject190", type=ecoreDiff_DeletedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEOperation", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement164: BinaryAssociation = BinaryAssociation(
    name="updatedElement164",
    ends={
        Property(name="ecoreDiff_EDataType165", type=ecoreDiff_ChangedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEDataType", type=ecoreDiff_EDataType, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement166: BinaryAssociation = BinaryAssociation(
    name="applicationElement166",
    ends={
        Property(name="ecoreDiff_EObject168", type=ecoreDiff_ChangedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEDataType167", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement169: BinaryAssociation = BinaryAssociation(
    name="applicationElement169",
    ends={
        Property(name="ecoreDiff_EObject170", type=ecoreDiff_DeletedETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedETypeParameter", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement171: BinaryAssociation = BinaryAssociation(
    name="updatedElement171",
    ends={
        Property(name="ecoreDiff_ETypeParameter172", type=ecoreDiff_ChangedETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypeParameter", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement173: BinaryAssociation = BinaryAssociation(
    name="applicationElement173",
    ends={
        Property(name="ecoreDiff_EObject175", type=ecoreDiff_ChangedETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypeParameter174", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement176: BinaryAssociation = BinaryAssociation(
    name="applicationElement176",
    ends={
        Property(name="ecoreDiff_EObject177", type=ecoreDiff_DeletedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEGenericType", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement205: BinaryAssociation = BinaryAssociation(
    name="updatedElement205",
    ends={
        Property(name="ecoreDiff_EParameter", type=ecoreDiff_ChangedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEParameter", type=ecoreDiff_EParameter, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement206: BinaryAssociation = BinaryAssociation(
    name="applicationElement206",
    ends={
        Property(name="ecoreDiff_EObject208", type=ecoreDiff_ChangedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEParameter207", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement209: BinaryAssociation = BinaryAssociation(
    name="applicationElement209",
    ends={
        Property(name="ecoreDiff_EObject210", type=ecoreDiff_DeletedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEAttribute", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement211: BinaryAssociation = BinaryAssociation(
    name="updatedElement211",
    ends={
        Property(name="ecoreDiff_EAttribute212", type=ecoreDiff_ChangedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAttribute", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement213: BinaryAssociation = BinaryAssociation(
    name="applicationElement213",
    ends={
        Property(name="ecoreDiff_EObject215", type=ecoreDiff_ChangedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAttribute214", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement191: BinaryAssociation = BinaryAssociation(
    name="updatedElement191",
    ends={
        Property(name="ecoreDiff_EOperation192", type=ecoreDiff_ChangedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEOperation", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement193: BinaryAssociation = BinaryAssociation(
    name="applicationElement193",
    ends={
        Property(name="ecoreDiff_EObject195", type=ecoreDiff_ChangedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEOperation194", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement196: BinaryAssociation = BinaryAssociation(
    name="applicationElement196",
    ends={
        Property(name="ecoreDiff_EObject197", type=ecoreDiff_DeletedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedETypedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement198: BinaryAssociation = BinaryAssociation(
    name="updatedElement198",
    ends={
        Property(name="ecoreDiff_ETypedElement199", type=ecoreDiff_ChangedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypedElement", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement200: BinaryAssociation = BinaryAssociation(
    name="applicationElement200",
    ends={
        Property(name="ecoreDiff_EObject202", type=ecoreDiff_ChangedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypedElement201", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement203: BinaryAssociation = BinaryAssociation(
    name="applicationElement203",
    ends={
        Property(name="ecoreDiff_EObject204", type=ecoreDiff_DeletedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEParameter", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement229: BinaryAssociation = BinaryAssociation(
    name="applicationElement229",
    ends={
        Property(name="ecoreDiff_EObject230", type=ecoreDiff_DeletedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEReference", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement231: BinaryAssociation = BinaryAssociation(
    name="updatedElement231",
    ends={
        Property(name="ecoreDiff_EReference232", type=ecoreDiff_ChangedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEReference", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement233: BinaryAssociation = BinaryAssociation(
    name="applicationElement233",
    ends={
        Property(name="ecoreDiff_EObject235", type=ecoreDiff_ChangedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEReference234", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement236: BinaryAssociation = BinaryAssociation(
    name="applicationElement236",
    ends={
        Property(name="ecoreDiff_EObject237", type=ecoreDiff_DeletedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEEnum", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement238: BinaryAssociation = BinaryAssociation(
    name="updatedElement238",
    ends={
        Property(name="ecoreDiff_EEnum", type=ecoreDiff_ChangedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnum", type=ecoreDiff_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement216: BinaryAssociation = BinaryAssociation(
    name="applicationElement216",
    ends={
        Property(name="ecoreDiff_EObject217", type=ecoreDiff_DeletedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEStructuralFeature", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement218: BinaryAssociation = BinaryAssociation(
    name="updatedElement218",
    ends={
        Property(name="ecoreDiff_EStructuralFeature219", type=ecoreDiff_ChangedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement220: BinaryAssociation = BinaryAssociation(
    name="applicationElement220",
    ends={
        Property(name="ecoreDiff_EObject222", type=ecoreDiff_ChangedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature221", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement223: BinaryAssociation = BinaryAssociation(
    name="applicationElement223",
    ends={
        Property(name="ecoreDiff_EObject224", type=ecoreDiff_DeletedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEStructuralFeature_Wildcard", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement225: BinaryAssociation = BinaryAssociation(
    name="updatedElement225",
    ends={
        Property(name="ecoreDiff_EStructuralFeature_Wildcard", type=ecoreDiff_ChangedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature_Wildcard", type=ecoreDiff_EStructuralFeature_Wildcard, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement226: BinaryAssociation = BinaryAssociation(
    name="applicationElement226",
    ends={
        Property(name="ecoreDiff_EObject228", type=ecoreDiff_ChangedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature_Wildcard227", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement250: BinaryAssociation = BinaryAssociation(
    name="updatedElement250",
    ends={
        Property(name="ecoreDiff_ChangedEModelElement", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(0, 1)),
        Property(name="ecoreDiff_EModelElement", type=ecoreDiff_ChangedEModelElement, multiplicity=Multiplicity(1, 1))
    }
)
applicationElement251: BinaryAssociation = BinaryAssociation(
    name="applicationElement251",
    ends={
        Property(name="ecoreDiff_EObject253", type=ecoreDiff_ChangedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEModelElement252", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement239: BinaryAssociation = BinaryAssociation(
    name="applicationElement239",
    ends={
        Property(name="ecoreDiff_EObject241", type=ecoreDiff_ChangedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnum240", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement242: BinaryAssociation = BinaryAssociation(
    name="applicationElement242",
    ends={
        Property(name="ecoreDiff_EObject243", type=ecoreDiff_DeletedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEEnumLiteral", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement244: BinaryAssociation = BinaryAssociation(
    name="updatedElement244",
    ends={
        Property(name="ecoreDiff_EEnumLiteral", type=ecoreDiff_ChangedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnumLiteral", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement245: BinaryAssociation = BinaryAssociation(
    name="applicationElement245",
    ends={
        Property(name="ecoreDiff_EObject247", type=ecoreDiff_ChangedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnumLiteral246", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement248: BinaryAssociation = BinaryAssociation(
    name="applicationElement248",
    ends={
        Property(name="ecoreDiff_EObject249", type=ecoreDiff_DeletedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEModelElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecoreDiff_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_EAnnotation)
gen_ecoreDiff_EClass_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_EClass)
gen_ecoreDiff_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EClassifier)
gen_ecoreDiff_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_ENamedElement)
gen_ecoreDiff_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EPackage)
gen_ecoreDiff_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_EFactory)
gen_ecoreDiff_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_EDataType)
gen_ecoreDiff_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EOperation)
gen_ecoreDiff_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ETypeParameter)
gen_ecoreDiff_EGenericType_EObject = Generalization(general=EObject, specific=ecoreDiff_EGenericType)
gen_ecoreDiff_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ETypedElement)
gen_ecoreDiff_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EParameter)
gen_ecoreDiff_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_EReference)
gen_ecoreDiff_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_EAttribute)
gen_ecoreDiff_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EStructuralFeature)
gen_ecoreDiff_EEnum_EDataType = Generalization(general=EDataType, specific=ecoreDiff_EEnum)
gen_ecoreDiff_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EEnumLiteral)
gen_ecoreDiff_EModelElement_EObject = Generalization(general=EObject, specific=ecoreDiff_EModelElement)
gen_ecoreDiff_EModelElement_DifferenceElement = Generalization(general=DifferenceElement, specific=ecoreDiff_EModelElement)
gen_ecoreDiff_AddedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_AddedEAnnotation)
gen_ecoreDiff_DeletedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_DeletedEAnnotation)
gen_ecoreDiff_ChangedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_ChangedEAnnotation)
gen_ecoreDiff_AddedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_AddedEClass)
gen_ecoreDiff_DeletedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_DeletedEClass)
gen_ecoreDiff_ChangedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_ChangedEClass)
gen_ecoreDiff_AddedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_AddedEClassifier)
gen_ecoreDiff_DeletedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_DeletedEClassifier)
gen_ecoreDiff_ChangedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_ChangedEClassifier)
gen_ecoreDiff_AddedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_AddedEStringToStringMapEntry)
gen_ecoreDiff_DeletedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_DeletedEStringToStringMapEntry)
gen_ecoreDiff_ChangedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_ChangedEStringToStringMapEntry)
gen_ecoreDiff_AddedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_AddedEObject)
gen_ecoreDiff_DeletedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_DeletedEObject)
gen_ecoreDiff_ChangedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_ChangedEObject)
gen_ecoreDiff_AddedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_AddedEFactory)
gen_ecoreDiff_DeletedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_DeletedEFactory)
gen_ecoreDiff_ChangedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_ChangedEFactory)
gen_ecoreDiff_AddedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_AddedEDataType)
gen_ecoreDiff_DeletedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_DeletedEDataType)
gen_ecoreDiff_ChangedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_ChangedEDataType)
gen_ecoreDiff_AddedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_AddedENamedElement)
gen_ecoreDiff_DeletedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_DeletedENamedElement)
gen_ecoreDiff_ChangedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ChangedENamedElement)
gen_ecoreDiff_AddedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_AddedEPackage)
gen_ecoreDiff_DeletedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_DeletedEPackage)
gen_ecoreDiff_ChangedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_ChangedEPackage)
gen_ecoreDiff_AddedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_AddedEClassifier_Wildcard)
gen_ecoreDiff_DeletedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_DeletedEClassifier_Wildcard)
gen_ecoreDiff_ChangedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_ChangedEClassifier_Wildcard)
gen_ecoreDiff_AddedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_AddedEOperation)
gen_ecoreDiff_DeletedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_DeletedEOperation)
gen_ecoreDiff_AddedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_AddedETypeParameter)
gen_ecoreDiff_DeletedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_DeletedETypeParameter)
gen_ecoreDiff_ChangedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_ChangedETypeParameter)
gen_ecoreDiff_AddedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_AddedEGenericType)
gen_ecoreDiff_DeletedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_DeletedEGenericType)
gen_ecoreDiff_ChangedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_ChangedEGenericType)
gen_ecoreDiff_ChangedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_ChangedEParameter)
gen_ecoreDiff_AddedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_AddedEAttribute)
gen_ecoreDiff_DeletedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_DeletedEAttribute)
gen_ecoreDiff_ChangedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_ChangedEAttribute)
gen_ecoreDiff_AddedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_AddedEStructuralFeature)
gen_ecoreDiff_DeletedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_DeletedEStructuralFeature)
gen_ecoreDiff_ChangedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_ChangedEOperation)
gen_ecoreDiff_AddedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_AddedETypedElement)
gen_ecoreDiff_DeletedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_DeletedETypedElement)
gen_ecoreDiff_ChangedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_ChangedETypedElement)
gen_ecoreDiff_AddedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_AddedEParameter)
gen_ecoreDiff_DeletedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_DeletedEParameter)
gen_ecoreDiff_DeletedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_DeletedEReference)
gen_ecoreDiff_ChangedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_ChangedEReference)
gen_ecoreDiff_AddedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_AddedEEnum)
gen_ecoreDiff_DeletedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_DeletedEEnum)
gen_ecoreDiff_ChangedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_ChangedEEnum)
gen_ecoreDiff_ChangedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_ChangedEStructuralFeature)
gen_ecoreDiff_AddedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_AddedEStructuralFeature_Wildcard)
gen_ecoreDiff_DeletedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_DeletedEStructuralFeature_Wildcard)
gen_ecoreDiff_ChangedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_ChangedEStructuralFeature_Wildcard)
gen_ecoreDiff_AddedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_AddedEReference)
gen_ecoreDiff_AddedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_AddedEEnumLiteral)
gen_ecoreDiff_DeletedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_DeletedEEnumLiteral)
gen_ecoreDiff_ChangedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_ChangedEEnumLiteral)
gen_ecoreDiff_AddedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_AddedEModelElement)
gen_ecoreDiff_DeletedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_DeletedEModelElement)
gen_ecoreDiff_ChangedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_ChangedEModelElement)

# Domain Model
domain_model = DomainModel(
    name="ecoreDiff",
    types={ecoreDiff_EAnnotation, EModelElement, ecoreDiff_EStringToStringMapEntry, ecoreDiff_EModelElement, ecoreDiff_EObject, ecoreDiff_EClass, EClassifier, ecoreDiff_EOperation, ecoreDiff_EAttribute, ecoreDiff_EStructuralFeature, ecoreDiff_EReference, ecoreDiff_EGenericType, ecoreDiff_EClassifier, ENamedElement, ecoreDiff_EPackage, ecoreDiff_ETypeParameter, ecoreDiff_ENamedElement, ecoreDiff_EFactory, ecoreDiff_EClassifier_Wildcard, ecoreDiff_EDataType, ETypedElement, EObject, ecoreDiff_ETypedElement, ecoreDiff_EParameter, ecoreDiff_EStructuralFeature_Wildcard, EStructuralFeature, ecoreDiff_EEnum, EDataType, ecoreDiff_EEnumLiteral, DifferenceElement, ecoreDiff_DifferenceModel, ecoreDiff_DifferenceElement, ecoreDiff_AddedEAnnotation, EAnnotation, ecoreDiff_DeletedEAnnotation, ecoreDiff_ChangedEAnnotation, ecoreDiff_AddedEClass, EClass, ecoreDiff_DeletedEClass, ecoreDiff_ChangedEClass, ecoreDiff_AddedEClassifier, ecoreDiff_DeletedEClassifier, ecoreDiff_ChangedEClassifier, ecoreDiff_AddedEStringToStringMapEntry, EStringToStringMapEntry, ecoreDiff_DeletedEStringToStringMapEntry, ecoreDiff_ChangedEStringToStringMapEntry, ecoreDiff_AddedEObject, ecoreDiff_DeletedEObject, ecoreDiff_ChangedEObject, ecoreDiff_AddedEFactory, EFactory, ecoreDiff_DeletedEFactory, ecoreDiff_ChangedEFactory, ecoreDiff_AddedEDataType, ecoreDiff_DeletedEDataType, ecoreDiff_ChangedEDataType, ecoreDiff_AddedENamedElement, ecoreDiff_DeletedENamedElement, ecoreDiff_ChangedENamedElement, ecoreDiff_AddedEPackage, EPackage, ecoreDiff_DeletedEPackage, ecoreDiff_ChangedEPackage, ecoreDiff_AddedEClassifier_Wildcard, EClassifier_Wildcard, ecoreDiff_DeletedEClassifier_Wildcard, ecoreDiff_ChangedEClassifier_Wildcard, ecoreDiff_AddedEOperation, EOperation, ecoreDiff_DeletedEOperation, ecoreDiff_AddedETypeParameter, ETypeParameter, ecoreDiff_DeletedETypeParameter, ecoreDiff_ChangedETypeParameter, ecoreDiff_AddedEGenericType, EGenericType, ecoreDiff_DeletedEGenericType, ecoreDiff_ChangedEGenericType, ecoreDiff_ChangedEParameter, ecoreDiff_AddedEAttribute, EAttribute, ecoreDiff_DeletedEAttribute, ecoreDiff_ChangedEAttribute, ecoreDiff_AddedEStructuralFeature, ecoreDiff_DeletedEStructuralFeature, ecoreDiff_ChangedEOperation, ecoreDiff_AddedETypedElement, ecoreDiff_DeletedETypedElement, ecoreDiff_ChangedETypedElement, ecoreDiff_AddedEParameter, EParameter, ecoreDiff_DeletedEParameter, ecoreDiff_DeletedEReference, ecoreDiff_ChangedEReference, ecoreDiff_AddedEEnum, EEnum, ecoreDiff_DeletedEEnum, ecoreDiff_ChangedEEnum, ecoreDiff_ChangedEStructuralFeature, ecoreDiff_AddedEStructuralFeature_Wildcard, EStructuralFeature_Wildcard, ecoreDiff_DeletedEStructuralFeature_Wildcard, ecoreDiff_ChangedEStructuralFeature_Wildcard, ecoreDiff_AddedEReference, EReference, ecoreDiff_AddedEEnumLiteral, EEnumLiteral, ecoreDiff_DeletedEEnumLiteral, ecoreDiff_ChangedEEnumLiteral, ecoreDiff_AddedEModelElement, ecoreDiff_DeletedEModelElement, ecoreDiff_ChangedEModelElement},
    associations={eSuperTypes8, details0, eModelElement1, contents2, references4, eAllContainments22, eAllOperations25, eOperations9, eAllAttributes10, eStructuralFeatures12, eAllReferences14, eReferences16, eAttributes19, eAllStructuralFeatures27, eAllSuperTypes30, eIDAttribute32, eGenericSuperTypes35, eAllGenericSuperTypes37, eFactoryInstance42, eSubpackages44, eSuperPackage47, eClassifiers49, ePackage40, eTypeParameters41, ePackage51, eBounds53, eUpperBound57, eTypeArguments60, eRawType62, eLowerBound66, eTypeParameter68, eClassifier71, eType85, eGenericType87, eTypeParameters74, eParameters77, eExceptions78, eGenericExceptions81, eContainingClass84, eOperation90, eAttributeType92, eOpposite97, eReferenceType99, eContainingClass94, eKeys102, eLiterals105, eEnum106, eAnnotations107, differenceElements108, applicationElement109, updatedElement111, applicationElement130, updatedElement132, applicationElement134, applicationElement137, updatedElement139, applicationElement113, applicationElement116, updatedElement118, applicationElement120, applicationElement123, updatedElement125, applicationElement127, applicationElement153, applicationElement156, updatedElement158, applicationElement159, applicationElement162, applicationElement141, applicationElement144, updatedElement146, applicationElement147, applicationElement150, updatedElement152, updatedElement178, applicationElement180, applicationElement183, updatedElement185, applicationElement186, applicationElement189, updatedElement164, applicationElement166, applicationElement169, updatedElement171, applicationElement173, applicationElement176, updatedElement205, applicationElement206, applicationElement209, updatedElement211, applicationElement213, updatedElement191, applicationElement193, applicationElement196, updatedElement198, applicationElement200, applicationElement203, applicationElement229, updatedElement231, applicationElement233, applicationElement236, updatedElement238, applicationElement216, updatedElement218, applicationElement220, applicationElement223, updatedElement225, applicationElement226, updatedElement250, applicationElement251, applicationElement239, applicationElement242, updatedElement244, applicationElement245, applicationElement248},
    generalizations={gen_ecoreDiff_EAnnotation_EModelElement, gen_ecoreDiff_EClass_EClassifier, gen_ecoreDiff_EClassifier_ENamedElement, gen_ecoreDiff_ENamedElement_EModelElement, gen_ecoreDiff_EPackage_ENamedElement, gen_ecoreDiff_EFactory_EModelElement, gen_ecoreDiff_EDataType_EClassifier, gen_ecoreDiff_EOperation_ETypedElement, gen_ecoreDiff_ETypeParameter_ENamedElement, gen_ecoreDiff_EGenericType_EObject, gen_ecoreDiff_ETypedElement_ENamedElement, gen_ecoreDiff_EParameter_ETypedElement, gen_ecoreDiff_EReference_EStructuralFeature, gen_ecoreDiff_EAttribute_EStructuralFeature, gen_ecoreDiff_EStructuralFeature_ETypedElement, gen_ecoreDiff_EEnum_EDataType, gen_ecoreDiff_EEnumLiteral_ENamedElement, gen_ecoreDiff_EModelElement_EObject, gen_ecoreDiff_EModelElement_DifferenceElement, gen_ecoreDiff_AddedEAnnotation_EAnnotation, gen_ecoreDiff_DeletedEAnnotation_EAnnotation, gen_ecoreDiff_ChangedEAnnotation_EAnnotation, gen_ecoreDiff_AddedEClass_EClass, gen_ecoreDiff_DeletedEClass_EClass, gen_ecoreDiff_ChangedEClass_EClass, gen_ecoreDiff_AddedEClassifier_EClassifier, gen_ecoreDiff_DeletedEClassifier_EClassifier, gen_ecoreDiff_ChangedEClassifier_EClassifier, gen_ecoreDiff_AddedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_DeletedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_ChangedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_AddedEObject_EObject, gen_ecoreDiff_DeletedEObject_EObject, gen_ecoreDiff_ChangedEObject_EObject, gen_ecoreDiff_AddedEFactory_EFactory, gen_ecoreDiff_DeletedEFactory_EFactory, gen_ecoreDiff_ChangedEFactory_EFactory, gen_ecoreDiff_AddedEDataType_EDataType, gen_ecoreDiff_DeletedEDataType_EDataType, gen_ecoreDiff_ChangedEDataType_EDataType, gen_ecoreDiff_AddedENamedElement_ENamedElement, gen_ecoreDiff_DeletedENamedElement_ENamedElement, gen_ecoreDiff_ChangedENamedElement_ENamedElement, gen_ecoreDiff_AddedEPackage_EPackage, gen_ecoreDiff_DeletedEPackage_EPackage, gen_ecoreDiff_ChangedEPackage_EPackage, gen_ecoreDiff_AddedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_DeletedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_ChangedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_AddedEOperation_EOperation, gen_ecoreDiff_DeletedEOperation_EOperation, gen_ecoreDiff_AddedETypeParameter_ETypeParameter, gen_ecoreDiff_DeletedETypeParameter_ETypeParameter, gen_ecoreDiff_ChangedETypeParameter_ETypeParameter, gen_ecoreDiff_AddedEGenericType_EGenericType, gen_ecoreDiff_DeletedEGenericType_EGenericType, gen_ecoreDiff_ChangedEGenericType_EGenericType, gen_ecoreDiff_ChangedEParameter_EParameter, gen_ecoreDiff_AddedEAttribute_EAttribute, gen_ecoreDiff_DeletedEAttribute_EAttribute, gen_ecoreDiff_ChangedEAttribute_EAttribute, gen_ecoreDiff_AddedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_DeletedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_ChangedEOperation_EOperation, gen_ecoreDiff_AddedETypedElement_ETypedElement, gen_ecoreDiff_DeletedETypedElement_ETypedElement, gen_ecoreDiff_ChangedETypedElement_ETypedElement, gen_ecoreDiff_AddedEParameter_EParameter, gen_ecoreDiff_DeletedEParameter_EParameter, gen_ecoreDiff_DeletedEReference_EReference, gen_ecoreDiff_ChangedEReference_EReference, gen_ecoreDiff_AddedEEnum_EEnum, gen_ecoreDiff_DeletedEEnum_EEnum, gen_ecoreDiff_ChangedEEnum_EEnum, gen_ecoreDiff_ChangedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_AddedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_DeletedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_ChangedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_AddedEReference_EReference, gen_ecoreDiff_AddedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_DeletedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_ChangedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_AddedEModelElement_EModelElement, gen_ecoreDiff_DeletedEModelElement_EModelElement, gen_ecoreDiff_ChangedEModelElement_EModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)