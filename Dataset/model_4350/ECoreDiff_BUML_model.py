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
ecoreDiff_EStringToStringMapEntry = Class(name="ecoreDiff::EStringToStringMapEntry")
ecoreDiff_EModelElement = Class(name="ecoreDiff::EModelElement", is_abstract=True)
ecoreDiff_EObject = Class(name="ecoreDiff::EObject")
ecoreDiff_EClass = Class(name="ecoreDiff::EClass")
EClassifier = Class(name="EClassifier")
ecoreDiff_EAnnotation = Class(name="ecoreDiff::EAnnotation")
EModelElement = Class(name="EModelElement")
ecoreDiff_EGenericType = Class(name="ecoreDiff::EGenericType")
ecoreDiff_EClassifier = Class(name="ecoreDiff::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecoreDiff_EOperation = Class(name="ecoreDiff::EOperation")
ecoreDiff_EAttribute = Class(name="ecoreDiff::EAttribute")
ecoreDiff_EStructuralFeature = Class(name="ecoreDiff::EStructuralFeature", is_abstract=True)
ecoreDiff_EReference = Class(name="ecoreDiff::EReference")
ecoreDiff_EPackage = Class(name="ecoreDiff::EPackage")
ecoreDiff_ETypeParameter = Class(name="ecoreDiff::ETypeParameter")
ecoreDiff_ENamedElement = Class(name="ecoreDiff::ENamedElement", is_abstract=True)
ecoreDiff_EFactory = Class(name="ecoreDiff::EFactory")
ecoreDiff_EClassifier_Wildcard = Class(name="ecoreDiff::EClassifier::Wildcard")
ETypedElement = Class(name="ETypedElement")
ecoreDiff_EParameter = Class(name="ecoreDiff::EParameter")
ecoreDiff_EDataType = Class(name="ecoreDiff::EDataType")
EObject = Class(name="EObject")
EStructuralFeature = Class(name="EStructuralFeature")
ecoreDiff_ETypedElement = Class(name="ecoreDiff::ETypedElement", is_abstract=True)
ecoreDiff_EEnum = Class(name="ecoreDiff::EEnum")
EDataType = Class(name="EDataType")
ecoreDiff_EEnumLiteral = Class(name="ecoreDiff::EEnumLiteral")
ecoreDiff_EStructuralFeature_Wildcard = Class(name="ecoreDiff::EStructuralFeature::Wildcard")
DifferenceElement = Class(name="DifferenceElement")
ecoreDiff_DifferenceModel = Class(name="ecoreDiff::DifferenceModel")
ecoreDiff_AddedEObject = Class(name="ecoreDiff::AddedEObject")
ecoreDiff_DeletedEObject = Class(name="ecoreDiff::DeletedEObject")
ecoreDiff_ChangedEObject = Class(name="ecoreDiff::ChangedEObject")
ecoreDiff_AddedEClass = Class(name="ecoreDiff::AddedEClass")
EClass = Class(name="EClass")
ecoreDiff_DeletedEClass = Class(name="ecoreDiff::DeletedEClass")
ecoreDiff_ChangedEClass = Class(name="ecoreDiff::ChangedEClass")
ecoreDiff_AddedEClassifier = Class(name="ecoreDiff::AddedEClassifier")
ecoreDiff_DeletedEClassifier = Class(name="ecoreDiff::DeletedEClassifier")
ecoreDiff_ChangedEClassifier = Class(name="ecoreDiff::ChangedEClassifier")
ecoreDiff_DifferenceElement = Class(name="ecoreDiff::DifferenceElement")
ecoreDiff_AddedEAnnotation = Class(name="ecoreDiff::AddedEAnnotation")
EAnnotation = Class(name="EAnnotation")
ecoreDiff_DeletedEAnnotation = Class(name="ecoreDiff::DeletedEAnnotation")
ecoreDiff_ChangedEAnnotation = Class(name="ecoreDiff::ChangedEAnnotation")
ecoreDiff_AddedEStringToStringMapEntry = Class(name="ecoreDiff::AddedEStringToStringMapEntry")
EStringToStringMapEntry = Class(name="EStringToStringMapEntry")
ecoreDiff_DeletedEStringToStringMapEntry = Class(name="ecoreDiff::DeletedEStringToStringMapEntry")
ecoreDiff_ChangedEStringToStringMapEntry = Class(name="ecoreDiff::ChangedEStringToStringMapEntry")
ecoreDiff_AddedEFactory = Class(name="ecoreDiff::AddedEFactory")
EFactory = Class(name="EFactory")
ecoreDiff_DeletedEFactory = Class(name="ecoreDiff::DeletedEFactory")
ecoreDiff_ChangedEFactory = Class(name="ecoreDiff::ChangedEFactory")
ecoreDiff_AddedEDataType = Class(name="ecoreDiff::AddedEDataType")
ecoreDiff_DeletedEDataType = Class(name="ecoreDiff::DeletedEDataType")
ecoreDiff_ChangedEDataType = Class(name="ecoreDiff::ChangedEDataType")
ecoreDiff_AddedETypeParameter = Class(name="ecoreDiff::AddedETypeParameter")
ETypeParameter = Class(name="ETypeParameter")
ecoreDiff_DeletedETypeParameter = Class(name="ecoreDiff::DeletedETypeParameter")
ecoreDiff_ChangedETypeParameter = Class(name="ecoreDiff::ChangedETypeParameter")
ecoreDiff_AddedENamedElement = Class(name="ecoreDiff::AddedENamedElement")
ecoreDiff_DeletedENamedElement = Class(name="ecoreDiff::DeletedENamedElement")
ecoreDiff_ChangedENamedElement = Class(name="ecoreDiff::ChangedENamedElement")
ecoreDiff_AddedEPackage = Class(name="ecoreDiff::AddedEPackage")
EPackage = Class(name="EPackage")
ecoreDiff_DeletedEPackage = Class(name="ecoreDiff::DeletedEPackage")
ecoreDiff_ChangedEPackage = Class(name="ecoreDiff::ChangedEPackage")
ecoreDiff_ChangedEOperation = Class(name="ecoreDiff::ChangedEOperation")
ecoreDiff_AddedETypedElement = Class(name="ecoreDiff::AddedETypedElement")
ecoreDiff_DeletedETypedElement = Class(name="ecoreDiff::DeletedETypedElement")
ecoreDiff_ChangedETypedElement = Class(name="ecoreDiff::ChangedETypedElement")
ecoreDiff_AddedEParameter = Class(name="ecoreDiff::AddedEParameter")
EParameter = Class(name="EParameter")
ecoreDiff_DeletedEParameter = Class(name="ecoreDiff::DeletedEParameter")
ecoreDiff_ChangedEParameter = Class(name="ecoreDiff::ChangedEParameter")
ecoreDiff_AddedEAttribute = Class(name="ecoreDiff::AddedEAttribute")
EAttribute = Class(name="EAttribute")
ecoreDiff_DeletedEAttribute = Class(name="ecoreDiff::DeletedEAttribute")
ecoreDiff_AddedEGenericType = Class(name="ecoreDiff::AddedEGenericType")
EGenericType = Class(name="EGenericType")
ecoreDiff_DeletedEGenericType = Class(name="ecoreDiff::DeletedEGenericType")
ecoreDiff_ChangedEGenericType = Class(name="ecoreDiff::ChangedEGenericType")
ecoreDiff_AddedEClassifier_Wildcard = Class(name="ecoreDiff::AddedEClassifier::Wildcard")
EClassifier_Wildcard = Class(name="EClassifier::Wildcard")
ecoreDiff_DeletedEClassifier_Wildcard = Class(name="ecoreDiff::DeletedEClassifier::Wildcard")
ecoreDiff_ChangedEClassifier_Wildcard = Class(name="ecoreDiff::ChangedEClassifier::Wildcard")
ecoreDiff_AddedEOperation = Class(name="ecoreDiff::AddedEOperation")
EOperation = Class(name="EOperation")
ecoreDiff_DeletedEOperation = Class(name="ecoreDiff::DeletedEOperation")
ecoreDiff_ChangedEStructuralFeature_Wildcard = Class(name="ecoreDiff::ChangedEStructuralFeature::Wildcard")
ecoreDiff_AddedEReference = Class(name="ecoreDiff::AddedEReference")
EReference = Class(name="EReference")
ecoreDiff_DeletedEReference = Class(name="ecoreDiff::DeletedEReference")
ecoreDiff_ChangedEReference = Class(name="ecoreDiff::ChangedEReference")
ecoreDiff_AddedEEnum = Class(name="ecoreDiff::AddedEEnum")
EEnum = Class(name="EEnum")
ecoreDiff_DeletedEEnum = Class(name="ecoreDiff::DeletedEEnum")
ecoreDiff_ChangedEEnum = Class(name="ecoreDiff::ChangedEEnum")
ecoreDiff_AddedEEnumLiteral = Class(name="ecoreDiff::AddedEEnumLiteral")
EEnumLiteral = Class(name="EEnumLiteral")
ecoreDiff_DeletedEEnumLiteral = Class(name="ecoreDiff::DeletedEEnumLiteral")
ecoreDiff_ChangedEAttribute = Class(name="ecoreDiff::ChangedEAttribute")
ecoreDiff_AddedEStructuralFeature = Class(name="ecoreDiff::AddedEStructuralFeature")
ecoreDiff_DeletedEStructuralFeature = Class(name="ecoreDiff::DeletedEStructuralFeature")
ecoreDiff_ChangedEStructuralFeature = Class(name="ecoreDiff::ChangedEStructuralFeature")
ecoreDiff_AddedEStructuralFeature_Wildcard = Class(name="ecoreDiff::AddedEStructuralFeature::Wildcard")
EStructuralFeature_Wildcard = Class(name="EStructuralFeature::Wildcard")
ecoreDiff_DeletedEStructuralFeature_Wildcard = Class(name="ecoreDiff::DeletedEStructuralFeature::Wildcard")
ecoreDiff_ChangedEEnumLiteral = Class(name="ecoreDiff::ChangedEEnumLiteral")
ecoreDiff_AddedEModelElement = Class(name="ecoreDiff::AddedEModelElement")
ecoreDiff_DeletedEModelElement = Class(name="ecoreDiff::DeletedEModelElement")
ecoreDiff_ChangedEModelElement = Class(name="ecoreDiff::ChangedEModelElement")

# ecoreDiff_EStringToStringMapEntry class attributes and methods
ecoreDiff_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecoreDiff_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecoreDiff_EStringToStringMapEntry.attributes={ecoreDiff_EStringToStringMapEntry_key, ecoreDiff_EStringToStringMapEntry_value}

# ecoreDiff_EModelElement class attributes and methods

# ecoreDiff_EObject class attributes and methods

# ecoreDiff_EClass class attributes and methods
ecoreDiff_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecoreDiff_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecoreDiff_EClass.attributes={ecoreDiff_EClass_interface, ecoreDiff_EClass_abstract}

# EClassifier class attributes and methods

# ecoreDiff_EAnnotation class attributes and methods
ecoreDiff_EAnnotation_source: Property = Property(name="source", type=StringType)
ecoreDiff_EAnnotation.attributes={ecoreDiff_EAnnotation_source}

# EModelElement class attributes and methods

# ecoreDiff_EGenericType class attributes and methods

# ecoreDiff_EClassifier class attributes and methods
ecoreDiff_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecoreDiff_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecoreDiff_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecoreDiff_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecoreDiff_EClassifier.attributes={ecoreDiff_EClassifier_instanceClassName, ecoreDiff_EClassifier_defaultValue, ecoreDiff_EClassifier_instanceClass, ecoreDiff_EClassifier_instanceTypeName}

# ENamedElement class attributes and methods

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
ecoreDiff_EStructuralFeature.attributes={ecoreDiff_EStructuralFeature_changeable, ecoreDiff_EStructuralFeature_defaultValueLiteral, ecoreDiff_EStructuralFeature_defaultValue, ecoreDiff_EStructuralFeature_unsettable, ecoreDiff_EStructuralFeature_transient, ecoreDiff_EStructuralFeature_derived, ecoreDiff_EStructuralFeature_volatile}

# ecoreDiff_EReference class attributes and methods
ecoreDiff_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecoreDiff_EReference_container: Property = Property(name="container", type=BooleanType)
ecoreDiff_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecoreDiff_EReference.attributes={ecoreDiff_EReference_container, ecoreDiff_EReference_containment, ecoreDiff_EReference_resolveProxies}

# ecoreDiff_EPackage class attributes and methods
ecoreDiff_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecoreDiff_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecoreDiff_EPackage.attributes={ecoreDiff_EPackage_nsPrefix, ecoreDiff_EPackage_nsURI}

# ecoreDiff_ETypeParameter class attributes and methods

# ecoreDiff_ENamedElement class attributes and methods
ecoreDiff_ENamedElement_name: Property = Property(name="name", type=StringType)
ecoreDiff_ENamedElement.attributes={ecoreDiff_ENamedElement_name}

# ecoreDiff_EFactory class attributes and methods

# ecoreDiff_EClassifier_Wildcard class attributes and methods

# ETypedElement class attributes and methods

# ecoreDiff_EParameter class attributes and methods

# ecoreDiff_EDataType class attributes and methods
ecoreDiff_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecoreDiff_EDataType.attributes={ecoreDiff_EDataType_serializable}

# EObject class attributes and methods

# EStructuralFeature class attributes and methods

# ecoreDiff_ETypedElement class attributes and methods
ecoreDiff_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecoreDiff_ETypedElement_required: Property = Property(name="required", type=StringType)
ecoreDiff_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecoreDiff_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecoreDiff_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecoreDiff_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecoreDiff_ETypedElement.attributes={ecoreDiff_ETypedElement_upperBound, ecoreDiff_ETypedElement_ordered, ecoreDiff_ETypedElement_required, ecoreDiff_ETypedElement_unique, ecoreDiff_ETypedElement_many, ecoreDiff_ETypedElement_lowerBound}

# ecoreDiff_EEnum class attributes and methods

# EDataType class attributes and methods

# ecoreDiff_EEnumLiteral class attributes and methods
ecoreDiff_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecoreDiff_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecoreDiff_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecoreDiff_EEnumLiteral.attributes={ecoreDiff_EEnumLiteral_value, ecoreDiff_EEnumLiteral_instance, ecoreDiff_EEnumLiteral_literal}

# ecoreDiff_EStructuralFeature_Wildcard class attributes and methods

# DifferenceElement class attributes and methods

# ecoreDiff_DifferenceModel class attributes and methods

# ecoreDiff_AddedEObject class attributes and methods

# ecoreDiff_DeletedEObject class attributes and methods

# ecoreDiff_ChangedEObject class attributes and methods

# ecoreDiff_AddedEClass class attributes and methods

# EClass class attributes and methods

# ecoreDiff_DeletedEClass class attributes and methods

# ecoreDiff_ChangedEClass class attributes and methods

# ecoreDiff_AddedEClassifier class attributes and methods

# ecoreDiff_DeletedEClassifier class attributes and methods

# ecoreDiff_ChangedEClassifier class attributes and methods

# ecoreDiff_DifferenceElement class attributes and methods

# ecoreDiff_AddedEAnnotation class attributes and methods

# EAnnotation class attributes and methods

# ecoreDiff_DeletedEAnnotation class attributes and methods

# ecoreDiff_ChangedEAnnotation class attributes and methods

# ecoreDiff_AddedEStringToStringMapEntry class attributes and methods

# EStringToStringMapEntry class attributes and methods

# ecoreDiff_DeletedEStringToStringMapEntry class attributes and methods

# ecoreDiff_ChangedEStringToStringMapEntry class attributes and methods

# ecoreDiff_AddedEFactory class attributes and methods

# EFactory class attributes and methods

# ecoreDiff_DeletedEFactory class attributes and methods

# ecoreDiff_ChangedEFactory class attributes and methods

# ecoreDiff_AddedEDataType class attributes and methods

# ecoreDiff_DeletedEDataType class attributes and methods

# ecoreDiff_ChangedEDataType class attributes and methods

# ecoreDiff_AddedETypeParameter class attributes and methods

# ETypeParameter class attributes and methods

# ecoreDiff_DeletedETypeParameter class attributes and methods

# ecoreDiff_ChangedETypeParameter class attributes and methods

# ecoreDiff_AddedENamedElement class attributes and methods

# ecoreDiff_DeletedENamedElement class attributes and methods

# ecoreDiff_ChangedENamedElement class attributes and methods

# ecoreDiff_AddedEPackage class attributes and methods

# EPackage class attributes and methods

# ecoreDiff_DeletedEPackage class attributes and methods

# ecoreDiff_ChangedEPackage class attributes and methods

# ecoreDiff_ChangedEOperation class attributes and methods

# ecoreDiff_AddedETypedElement class attributes and methods

# ecoreDiff_DeletedETypedElement class attributes and methods

# ecoreDiff_ChangedETypedElement class attributes and methods

# ecoreDiff_AddedEParameter class attributes and methods

# EParameter class attributes and methods

# ecoreDiff_DeletedEParameter class attributes and methods

# ecoreDiff_ChangedEParameter class attributes and methods

# ecoreDiff_AddedEAttribute class attributes and methods

# EAttribute class attributes and methods

# ecoreDiff_DeletedEAttribute class attributes and methods

# ecoreDiff_AddedEGenericType class attributes and methods

# EGenericType class attributes and methods

# ecoreDiff_DeletedEGenericType class attributes and methods

# ecoreDiff_ChangedEGenericType class attributes and methods

# ecoreDiff_AddedEClassifier_Wildcard class attributes and methods

# EClassifier_Wildcard class attributes and methods

# ecoreDiff_DeletedEClassifier_Wildcard class attributes and methods

# ecoreDiff_ChangedEClassifier_Wildcard class attributes and methods

# ecoreDiff_AddedEOperation class attributes and methods

# EOperation class attributes and methods

# ecoreDiff_DeletedEOperation class attributes and methods

# ecoreDiff_ChangedEStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_AddedEReference class attributes and methods

# EReference class attributes and methods

# ecoreDiff_DeletedEReference class attributes and methods

# ecoreDiff_ChangedEReference class attributes and methods

# ecoreDiff_AddedEEnum class attributes and methods

# EEnum class attributes and methods

# ecoreDiff_DeletedEEnum class attributes and methods

# ecoreDiff_ChangedEEnum class attributes and methods

# ecoreDiff_AddedEEnumLiteral class attributes and methods

# EEnumLiteral class attributes and methods

# ecoreDiff_DeletedEEnumLiteral class attributes and methods

# ecoreDiff_ChangedEAttribute class attributes and methods

# ecoreDiff_AddedEStructuralFeature class attributes and methods

# ecoreDiff_DeletedEStructuralFeature class attributes and methods

# ecoreDiff_ChangedEStructuralFeature class attributes and methods

# ecoreDiff_AddedEStructuralFeature_Wildcard class attributes and methods

# EStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_DeletedEStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_ChangedEEnumLiteral class attributes and methods

# ecoreDiff_AddedEModelElement class attributes and methods

# ecoreDiff_DeletedEModelElement class attributes and methods

# ecoreDiff_ChangedEModelElement class attributes and methods

# Relationships
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
        Property(name="2", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="ecoreDiff_EObject", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAnnotation4", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="ecoreDiff_EObject7", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAnnotation6", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="ecoreDiff_EClass", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass8", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations29: BinaryAssociation = BinaryAssociation(
    name="eAllOperations29",
    ends={
        Property(name="ecoreDiff_EOperation", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass30", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures31: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures31",
    ends={
        Property(name="ecoreDiff_EStructuralFeature", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass32", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes34: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes34",
    ends={
        Property(name="ecoreDiff_EClass35", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass33", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute36: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute36",
    ends={
        Property(name="ecoreDiff_EAttribute38", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass37", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes39",
    ends={
        Property(name="ecoreDiff_EGenericType", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass40", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes41: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes41",
    ends={
        Property(name="ecoreDiff_EGenericType43", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass42", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="12", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="11", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes13: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes13",
    ends={
        Property(name="ecoreDiff_EAttribute", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass14", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eStructuralFeatures15: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures15",
    ends={
        Property(name="17", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllReferences18: BinaryAssociation = BinaryAssociation(
    name="eAllReferences18",
    ends={
        Property(name="ecoreDiff_EReference", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass19", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences20: BinaryAssociation = BinaryAssociation(
    name="eReferences20",
    ends={
        Property(name="ecoreDiff_EReference22", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass21", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes23: BinaryAssociation = BinaryAssociation(
    name="eAttributes23",
    ends={
        Property(name="ecoreDiff_EAttribute25", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass24", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments26: BinaryAssociation = BinaryAssociation(
    name="eAllContainments26",
    ends={
        Property(name="ecoreDiff_EReference28", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass27", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperPackage56: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage56",
    ends={
        Property(name="58", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="57", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
ePackage44: BinaryAssociation = BinaryAssociation(
    name="ePackage44",
    ends={
        Property(name="46", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="45", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters47: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters47",
    ends={
        Property(name="ecoreDiff_ETypeParameter", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClassifier", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance48: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance48",
    ends={
        Property(name="50", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="49", type=ecoreDiff_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eSubpackages52: BinaryAssociation = BinaryAssociation(
    name="eSubpackages52",
    ends={
        Property(name="54", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="53", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound69: BinaryAssociation = BinaryAssociation(
    name="eUpperBound69",
    ends={
        Property(name="ecoreDiff_EGenericType70", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType68", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments72: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments72",
    ends={
        Property(name="ecoreDiff_EGenericType73", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType71", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType74: BinaryAssociation = BinaryAssociation(
    name="eRawType74",
    ends={
        Property(name="ecoreDiff_EClassifier76", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType75", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound78: BinaryAssociation = BinaryAssociation(
    name="eLowerBound78",
    ends={
        Property(name="ecoreDiff_EGenericType79", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType77", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter80: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter80",
    ends={
        Property(name="ecoreDiff_ETypeParameter82", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType81", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier83: BinaryAssociation = BinaryAssociation(
    name="eClassifier83",
    ends={
        Property(name="ecoreDiff_EClassifier85", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType84", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters86: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters86",
    ends={
        Property(name="ecoreDiff_ETypeParameter88", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation87", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters89: BinaryAssociation = BinaryAssociation(
    name="eParameters89",
    ends={
        Property(name="91", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="90", type=ecoreDiff_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions92: BinaryAssociation = BinaryAssociation(
    name="eExceptions92",
    ends={
        Property(name="ecoreDiff_EClassifier94", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation93", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eClassifiers59: BinaryAssociation = BinaryAssociation(
    name="eClassifiers59",
    ends={
        Property(name="61", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="60", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage62: BinaryAssociation = BinaryAssociation(
    name="ePackage62",
    ends={
        Property(name="64", type=ecoreDiff_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="63", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eBounds65: BinaryAssociation = BinaryAssociation(
    name="eBounds65",
    ends={
        Property(name="ecoreDiff_EGenericType67", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypeParameter66", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericType101: BinaryAssociation = BinaryAssociation(
    name="eGenericType101",
    ends={
        Property(name="ecoreDiff_EGenericType102", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypedElement", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eOperation103: BinaryAssociation = BinaryAssociation(
    name="eOperation103",
    ends={
        Property(name="105", type=ecoreDiff_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="104", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eAttributeType106: BinaryAssociation = BinaryAssociation(
    name="eAttributeType106",
    ends={
        Property(name="ecoreDiff_EDataType", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAttribute107", type=ecoreDiff_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eGenericExceptions95: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions95",
    ends={
        Property(name="ecoreDiff_EGenericType97", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation96", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass98: BinaryAssociation = BinaryAssociation(
    name="eContainingClass98",
    ends={
        Property(name="100", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="99", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite112: BinaryAssociation = BinaryAssociation(
    name="eOpposite112",
    ends={
        Property(name="ecoreDiff_EReference111", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 1)),
        Property(name="ecoreDiff_EReference113", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1))
    }
)
eReferenceType114: BinaryAssociation = BinaryAssociation(
    name="eReferenceType114",
    ends={
        Property(name="ecoreDiff_EClass116", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference115", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys117: BinaryAssociation = BinaryAssociation(
    name="eKeys117",
    ends={
        Property(name="ecoreDiff_EAttribute119", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference118", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eLiterals120: BinaryAssociation = BinaryAssociation(
    name="eLiterals120",
    ends={
        Property(name="122", type=ecoreDiff_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="121", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum123: BinaryAssociation = BinaryAssociation(
    name="eEnum123",
    ends={
        Property(name="125", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="124", type=ecoreDiff_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass108: BinaryAssociation = BinaryAssociation(
    name="eContainingClass108",
    ends={
        Property(name="110", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="109", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations126: BinaryAssociation = BinaryAssociation(
    name="eAnnotations126",
    ends={
        Property(name="128", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="127", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updatedElement132: BinaryAssociation = BinaryAssociation(
    name="updatedElement132",
    ends={
        Property(name="ecoreDiff_ChangedEStringToStringMapEntry", type=ecoreDiff_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999)),
        Property(name="ecoreDiff_EStringToStringMapEntry133", type=ecoreDiff_ChangedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1))
    }
)
updatedElement134: BinaryAssociation = BinaryAssociation(
    name="updatedElement134",
    ends={
        Property(name="ecoreDiff_EObject135", type=ecoreDiff_ChangedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEObject", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement136: BinaryAssociation = BinaryAssociation(
    name="updatedElement136",
    ends={
        Property(name="ecoreDiff_EClass137", type=ecoreDiff_ChangedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClass", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement138: BinaryAssociation = BinaryAssociation(
    name="updatedElement138",
    ends={
        Property(name="ecoreDiff_EClassifier139", type=ecoreDiff_ChangedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
differenceElements129: BinaryAssociation = BinaryAssociation(
    name="differenceElements129",
    ends={
        Property(name="ecoreDiff_DifferenceElement", type=ecoreDiff_DifferenceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DifferenceModel", type=ecoreDiff_DifferenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updatedElement130: BinaryAssociation = BinaryAssociation(
    name="updatedElement130",
    ends={
        Property(name="ecoreDiff_EAnnotation131", type=ecoreDiff_ChangedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAnnotation", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement142: BinaryAssociation = BinaryAssociation(
    name="updatedElement142",
    ends={
        Property(name="ecoreDiff_EFactory", type=ecoreDiff_ChangedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEFactory", type=ecoreDiff_EFactory, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement143: BinaryAssociation = BinaryAssociation(
    name="updatedElement143",
    ends={
        Property(name="ecoreDiff_EDataType144", type=ecoreDiff_ChangedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEDataType", type=ecoreDiff_EDataType, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement145: BinaryAssociation = BinaryAssociation(
    name="updatedElement145",
    ends={
        Property(name="ecoreDiff_ETypeParameter146", type=ecoreDiff_ChangedETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypeParameter", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement140: BinaryAssociation = BinaryAssociation(
    name="updatedElement140",
    ends={
        Property(name="ecoreDiff_ENamedElement", type=ecoreDiff_ChangedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedENamedElement", type=ecoreDiff_ENamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement141: BinaryAssociation = BinaryAssociation(
    name="updatedElement141",
    ends={
        Property(name="ecoreDiff_EPackage", type=ecoreDiff_ChangedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEPackage", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement150: BinaryAssociation = BinaryAssociation(
    name="updatedElement150",
    ends={
        Property(name="ecoreDiff_EOperation151", type=ecoreDiff_ChangedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEOperation", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement152: BinaryAssociation = BinaryAssociation(
    name="updatedElement152",
    ends={
        Property(name="ecoreDiff_ETypedElement153", type=ecoreDiff_ChangedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypedElement", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement154: BinaryAssociation = BinaryAssociation(
    name="updatedElement154",
    ends={
        Property(name="ecoreDiff_EParameter", type=ecoreDiff_ChangedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEParameter", type=ecoreDiff_EParameter, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement147: BinaryAssociation = BinaryAssociation(
    name="updatedElement147",
    ends={
        Property(name="ecoreDiff_EGenericType148", type=ecoreDiff_ChangedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEGenericType", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement149: BinaryAssociation = BinaryAssociation(
    name="updatedElement149",
    ends={
        Property(name="ecoreDiff_EClassifier_Wildcard", type=ecoreDiff_ChangedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier_Wildcard", type=ecoreDiff_EClassifier_Wildcard, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement159: BinaryAssociation = BinaryAssociation(
    name="updatedElement159",
    ends={
        Property(name="ecoreDiff_EStructuralFeature_Wildcard", type=ecoreDiff_ChangedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature_Wildcard", type=ecoreDiff_EStructuralFeature_Wildcard, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement160: BinaryAssociation = BinaryAssociation(
    name="updatedElement160",
    ends={
        Property(name="ecoreDiff_EReference161", type=ecoreDiff_ChangedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEReference", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement162: BinaryAssociation = BinaryAssociation(
    name="updatedElement162",
    ends={
        Property(name="ecoreDiff_EEnum", type=ecoreDiff_ChangedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnum", type=ecoreDiff_EEnum, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement155: BinaryAssociation = BinaryAssociation(
    name="updatedElement155",
    ends={
        Property(name="ecoreDiff_EAttribute156", type=ecoreDiff_ChangedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAttribute", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement157: BinaryAssociation = BinaryAssociation(
    name="updatedElement157",
    ends={
        Property(name="ecoreDiff_EStructuralFeature158", type=ecoreDiff_ChangedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement163: BinaryAssociation = BinaryAssociation(
    name="updatedElement163",
    ends={
        Property(name="ecoreDiff_EEnumLiteral", type=ecoreDiff_ChangedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnumLiteral", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement164: BinaryAssociation = BinaryAssociation(
    name="updatedElement164",
    ends={
        Property(name="ecoreDiff_EModelElement", type=ecoreDiff_ChangedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEModelElement", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ecoreDiff_EClass_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_EClass)
gen_ecoreDiff_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_EAnnotation)
gen_ecoreDiff_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EClassifier)
gen_ecoreDiff_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_ENamedElement)
gen_ecoreDiff_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EPackage)
gen_ecoreDiff_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EOperation)
gen_ecoreDiff_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_EFactory)
gen_ecoreDiff_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_EDataType)
gen_ecoreDiff_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ETypeParameter)
gen_ecoreDiff_EGenericType_EObject = Generalization(general=EObject, specific=ecoreDiff_EGenericType)
gen_ecoreDiff_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EParameter)
gen_ecoreDiff_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_EAttribute)
gen_ecoreDiff_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EStructuralFeature)
gen_ecoreDiff_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ETypedElement)
gen_ecoreDiff_EEnum_EDataType = Generalization(general=EDataType, specific=ecoreDiff_EEnum)
gen_ecoreDiff_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EEnumLiteral)
gen_ecoreDiff_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_EReference)
gen_ecoreDiff_EModelElement_EObject = Generalization(general=EObject, specific=ecoreDiff_EModelElement)
gen_ecoreDiff_EModelElement_DifferenceElement = Generalization(general=DifferenceElement, specific=ecoreDiff_EModelElement)
gen_ecoreDiff_AddedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_AddedEObject)
gen_ecoreDiff_DeletedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_DeletedEObject)
gen_ecoreDiff_ChangedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_ChangedEObject)
gen_ecoreDiff_AddedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_AddedEClass)
gen_ecoreDiff_DeletedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_DeletedEClass)
gen_ecoreDiff_ChangedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_ChangedEClass)
gen_ecoreDiff_AddedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_AddedEClassifier)
gen_ecoreDiff_DeletedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_DeletedEClassifier)
gen_ecoreDiff_ChangedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_ChangedEClassifier)
gen_ecoreDiff_AddedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_AddedEAnnotation)
gen_ecoreDiff_DeletedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_DeletedEAnnotation)
gen_ecoreDiff_ChangedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_ChangedEAnnotation)
gen_ecoreDiff_AddedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_AddedEStringToStringMapEntry)
gen_ecoreDiff_DeletedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_DeletedEStringToStringMapEntry)
gen_ecoreDiff_ChangedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_ChangedEStringToStringMapEntry)
gen_ecoreDiff_AddedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_AddedEFactory)
gen_ecoreDiff_DeletedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_DeletedEFactory)
gen_ecoreDiff_ChangedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_ChangedEFactory)
gen_ecoreDiff_AddedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_AddedEDataType)
gen_ecoreDiff_DeletedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_DeletedEDataType)
gen_ecoreDiff_ChangedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_ChangedEDataType)
gen_ecoreDiff_AddedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_AddedETypeParameter)
gen_ecoreDiff_DeletedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_DeletedETypeParameter)
gen_ecoreDiff_ChangedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_ChangedETypeParameter)
gen_ecoreDiff_AddedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_AddedENamedElement)
gen_ecoreDiff_DeletedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_DeletedENamedElement)
gen_ecoreDiff_ChangedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ChangedENamedElement)
gen_ecoreDiff_AddedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_AddedEPackage)
gen_ecoreDiff_DeletedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_DeletedEPackage)
gen_ecoreDiff_ChangedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_ChangedEPackage)
gen_ecoreDiff_ChangedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_ChangedEOperation)
gen_ecoreDiff_AddedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_AddedETypedElement)
gen_ecoreDiff_DeletedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_DeletedETypedElement)
gen_ecoreDiff_ChangedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_ChangedETypedElement)
gen_ecoreDiff_AddedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_AddedEParameter)
gen_ecoreDiff_DeletedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_DeletedEParameter)
gen_ecoreDiff_ChangedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_ChangedEParameter)
gen_ecoreDiff_AddedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_AddedEAttribute)
gen_ecoreDiff_DeletedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_DeletedEAttribute)
gen_ecoreDiff_AddedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_AddedEGenericType)
gen_ecoreDiff_DeletedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_DeletedEGenericType)
gen_ecoreDiff_ChangedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_ChangedEGenericType)
gen_ecoreDiff_AddedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_AddedEClassifier_Wildcard)
gen_ecoreDiff_DeletedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_DeletedEClassifier_Wildcard)
gen_ecoreDiff_ChangedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_ChangedEClassifier_Wildcard)
gen_ecoreDiff_AddedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_AddedEOperation)
gen_ecoreDiff_DeletedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_DeletedEOperation)
gen_ecoreDiff_ChangedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_ChangedEStructuralFeature_Wildcard)
gen_ecoreDiff_AddedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_AddedEReference)
gen_ecoreDiff_DeletedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_DeletedEReference)
gen_ecoreDiff_ChangedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_ChangedEReference)
gen_ecoreDiff_AddedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_AddedEEnum)
gen_ecoreDiff_DeletedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_DeletedEEnum)
gen_ecoreDiff_ChangedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_ChangedEEnum)
gen_ecoreDiff_AddedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_AddedEEnumLiteral)
gen_ecoreDiff_DeletedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_DeletedEEnumLiteral)
gen_ecoreDiff_ChangedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_ChangedEAttribute)
gen_ecoreDiff_AddedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_AddedEStructuralFeature)
gen_ecoreDiff_DeletedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_DeletedEStructuralFeature)
gen_ecoreDiff_ChangedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_ChangedEStructuralFeature)
gen_ecoreDiff_AddedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_AddedEStructuralFeature_Wildcard)
gen_ecoreDiff_DeletedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_DeletedEStructuralFeature_Wildcard)
gen_ecoreDiff_ChangedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_ChangedEEnumLiteral)
gen_ecoreDiff_AddedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_AddedEModelElement)
gen_ecoreDiff_DeletedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_DeletedEModelElement)
gen_ecoreDiff_ChangedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_ChangedEModelElement)

# Domain Model
domain_model = DomainModel(
    name="ecoreDiff",
    types={ecoreDiff_EStringToStringMapEntry, ecoreDiff_EModelElement, ecoreDiff_EObject, ecoreDiff_EClass, EClassifier, ecoreDiff_EAnnotation, EModelElement, ecoreDiff_EGenericType, ecoreDiff_EClassifier, ENamedElement, ecoreDiff_EOperation, ecoreDiff_EAttribute, ecoreDiff_EStructuralFeature, ecoreDiff_EReference, ecoreDiff_EPackage, ecoreDiff_ETypeParameter, ecoreDiff_ENamedElement, ecoreDiff_EFactory, ecoreDiff_EClassifier_Wildcard, ETypedElement, ecoreDiff_EParameter, ecoreDiff_EDataType, EObject, EStructuralFeature, ecoreDiff_ETypedElement, ecoreDiff_EEnum, EDataType, ecoreDiff_EEnumLiteral, ecoreDiff_EStructuralFeature_Wildcard, DifferenceElement, ecoreDiff_DifferenceModel, ecoreDiff_AddedEObject, ecoreDiff_DeletedEObject, ecoreDiff_ChangedEObject, ecoreDiff_AddedEClass, EClass, ecoreDiff_DeletedEClass, ecoreDiff_ChangedEClass, ecoreDiff_AddedEClassifier, ecoreDiff_DeletedEClassifier, ecoreDiff_ChangedEClassifier, ecoreDiff_DifferenceElement, ecoreDiff_AddedEAnnotation, EAnnotation, ecoreDiff_DeletedEAnnotation, ecoreDiff_ChangedEAnnotation, ecoreDiff_AddedEStringToStringMapEntry, EStringToStringMapEntry, ecoreDiff_DeletedEStringToStringMapEntry, ecoreDiff_ChangedEStringToStringMapEntry, ecoreDiff_AddedEFactory, EFactory, ecoreDiff_DeletedEFactory, ecoreDiff_ChangedEFactory, ecoreDiff_AddedEDataType, ecoreDiff_DeletedEDataType, ecoreDiff_ChangedEDataType, ecoreDiff_AddedETypeParameter, ETypeParameter, ecoreDiff_DeletedETypeParameter, ecoreDiff_ChangedETypeParameter, ecoreDiff_AddedENamedElement, ecoreDiff_DeletedENamedElement, ecoreDiff_ChangedENamedElement, ecoreDiff_AddedEPackage, EPackage, ecoreDiff_DeletedEPackage, ecoreDiff_ChangedEPackage, ecoreDiff_ChangedEOperation, ecoreDiff_AddedETypedElement, ecoreDiff_DeletedETypedElement, ecoreDiff_ChangedETypedElement, ecoreDiff_AddedEParameter, EParameter, ecoreDiff_DeletedEParameter, ecoreDiff_ChangedEParameter, ecoreDiff_AddedEAttribute, EAttribute, ecoreDiff_DeletedEAttribute, ecoreDiff_AddedEGenericType, EGenericType, ecoreDiff_DeletedEGenericType, ecoreDiff_ChangedEGenericType, ecoreDiff_AddedEClassifier_Wildcard, EClassifier_Wildcard, ecoreDiff_DeletedEClassifier_Wildcard, ecoreDiff_ChangedEClassifier_Wildcard, ecoreDiff_AddedEOperation, EOperation, ecoreDiff_DeletedEOperation, ecoreDiff_ChangedEStructuralFeature_Wildcard, ecoreDiff_AddedEReference, EReference, ecoreDiff_DeletedEReference, ecoreDiff_ChangedEReference, ecoreDiff_AddedEEnum, EEnum, ecoreDiff_DeletedEEnum, ecoreDiff_ChangedEEnum, ecoreDiff_AddedEEnumLiteral, EEnumLiteral, ecoreDiff_DeletedEEnumLiteral, ecoreDiff_ChangedEAttribute, ecoreDiff_AddedEStructuralFeature, ecoreDiff_DeletedEStructuralFeature, ecoreDiff_ChangedEStructuralFeature, ecoreDiff_AddedEStructuralFeature_Wildcard, EStructuralFeature_Wildcard, ecoreDiff_DeletedEStructuralFeature_Wildcard, ecoreDiff_ChangedEEnumLiteral, ecoreDiff_AddedEModelElement, ecoreDiff_DeletedEModelElement, ecoreDiff_ChangedEModelElement},
    associations={details0, eModelElement1, contents3, references5, eSuperTypes9, eAllOperations29, eAllStructuralFeatures31, eAllSuperTypes34, eIDAttribute36, eGenericSuperTypes39, eAllGenericSuperTypes41, eOperations10, eAllAttributes13, eStructuralFeatures15, eAllReferences18, eReferences20, eAttributes23, eAllContainments26, eSuperPackage56, ePackage44, eTypeParameters47, eFactoryInstance48, eSubpackages52, eUpperBound69, eTypeArguments72, eRawType74, eLowerBound78, eTypeParameter80, eClassifier83, eTypeParameters86, eParameters89, eExceptions92, eClassifiers59, ePackage62, eBounds65, eGenericType101, eOperation103, eAttributeType106, eGenericExceptions95, eContainingClass98, eOpposite112, eReferenceType114, eKeys117, eLiterals120, eEnum123, eContainingClass108, eAnnotations126, updatedElement132, updatedElement134, updatedElement136, updatedElement138, differenceElements129, updatedElement130, updatedElement142, updatedElement143, updatedElement145, updatedElement140, updatedElement141, updatedElement150, updatedElement152, updatedElement154, updatedElement147, updatedElement149, updatedElement159, updatedElement160, updatedElement162, updatedElement155, updatedElement157, updatedElement163, updatedElement164},
    generalizations={gen_ecoreDiff_EClass_EClassifier, gen_ecoreDiff_EAnnotation_EModelElement, gen_ecoreDiff_EClassifier_ENamedElement, gen_ecoreDiff_ENamedElement_EModelElement, gen_ecoreDiff_EPackage_ENamedElement, gen_ecoreDiff_EOperation_ETypedElement, gen_ecoreDiff_EFactory_EModelElement, gen_ecoreDiff_EDataType_EClassifier, gen_ecoreDiff_ETypeParameter_ENamedElement, gen_ecoreDiff_EGenericType_EObject, gen_ecoreDiff_EParameter_ETypedElement, gen_ecoreDiff_EAttribute_EStructuralFeature, gen_ecoreDiff_EStructuralFeature_ETypedElement, gen_ecoreDiff_ETypedElement_ENamedElement, gen_ecoreDiff_EEnum_EDataType, gen_ecoreDiff_EEnumLiteral_ENamedElement, gen_ecoreDiff_EReference_EStructuralFeature, gen_ecoreDiff_EModelElement_EObject, gen_ecoreDiff_EModelElement_DifferenceElement, gen_ecoreDiff_AddedEObject_EObject, gen_ecoreDiff_DeletedEObject_EObject, gen_ecoreDiff_ChangedEObject_EObject, gen_ecoreDiff_AddedEClass_EClass, gen_ecoreDiff_DeletedEClass_EClass, gen_ecoreDiff_ChangedEClass_EClass, gen_ecoreDiff_AddedEClassifier_EClassifier, gen_ecoreDiff_DeletedEClassifier_EClassifier, gen_ecoreDiff_ChangedEClassifier_EClassifier, gen_ecoreDiff_AddedEAnnotation_EAnnotation, gen_ecoreDiff_DeletedEAnnotation_EAnnotation, gen_ecoreDiff_ChangedEAnnotation_EAnnotation, gen_ecoreDiff_AddedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_DeletedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_ChangedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_AddedEFactory_EFactory, gen_ecoreDiff_DeletedEFactory_EFactory, gen_ecoreDiff_ChangedEFactory_EFactory, gen_ecoreDiff_AddedEDataType_EDataType, gen_ecoreDiff_DeletedEDataType_EDataType, gen_ecoreDiff_ChangedEDataType_EDataType, gen_ecoreDiff_AddedETypeParameter_ETypeParameter, gen_ecoreDiff_DeletedETypeParameter_ETypeParameter, gen_ecoreDiff_ChangedETypeParameter_ETypeParameter, gen_ecoreDiff_AddedENamedElement_ENamedElement, gen_ecoreDiff_DeletedENamedElement_ENamedElement, gen_ecoreDiff_ChangedENamedElement_ENamedElement, gen_ecoreDiff_AddedEPackage_EPackage, gen_ecoreDiff_DeletedEPackage_EPackage, gen_ecoreDiff_ChangedEPackage_EPackage, gen_ecoreDiff_ChangedEOperation_EOperation, gen_ecoreDiff_AddedETypedElement_ETypedElement, gen_ecoreDiff_DeletedETypedElement_ETypedElement, gen_ecoreDiff_ChangedETypedElement_ETypedElement, gen_ecoreDiff_AddedEParameter_EParameter, gen_ecoreDiff_DeletedEParameter_EParameter, gen_ecoreDiff_ChangedEParameter_EParameter, gen_ecoreDiff_AddedEAttribute_EAttribute, gen_ecoreDiff_DeletedEAttribute_EAttribute, gen_ecoreDiff_AddedEGenericType_EGenericType, gen_ecoreDiff_DeletedEGenericType_EGenericType, gen_ecoreDiff_ChangedEGenericType_EGenericType, gen_ecoreDiff_AddedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_DeletedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_ChangedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_AddedEOperation_EOperation, gen_ecoreDiff_DeletedEOperation_EOperation, gen_ecoreDiff_ChangedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_AddedEReference_EReference, gen_ecoreDiff_DeletedEReference_EReference, gen_ecoreDiff_ChangedEReference_EReference, gen_ecoreDiff_AddedEEnum_EEnum, gen_ecoreDiff_DeletedEEnum_EEnum, gen_ecoreDiff_ChangedEEnum_EEnum, gen_ecoreDiff_AddedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_DeletedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_ChangedEAttribute_EAttribute, gen_ecoreDiff_AddedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_DeletedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_ChangedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_AddedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_DeletedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_ChangedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_AddedEModelElement_EModelElement, gen_ecoreDiff_DeletedEModelElement_EModelElement, gen_ecoreDiff_ChangedEModelElement_EModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)