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
ecoreDiff_EObject = Class(name="ecoreDiff::EObject")
ecoreDiff_EClass = Class(name="ecoreDiff::EClass")
EClassifier = Class(name="EClassifier")
ecoreDiff_EOperation = Class(name="ecoreDiff::EOperation")
ecoreDiff_EStructuralFeature = Class(name="ecoreDiff::EStructuralFeature", is_abstract=True)
ecoreDiff_EGenericType = Class(name="ecoreDiff::EGenericType")
ecoreDiff_EAnnotation = Class(name="ecoreDiff::EAnnotation")
EModelElement = Class(name="EModelElement")
ecoreDiff_EStringToStringMapEntry = Class(name="ecoreDiff::EStringToStringMapEntry")
ecoreDiff_EModelElement = Class(name="ecoreDiff::EModelElement", is_abstract=True)
ecoreDiff_ENamedElement = Class(name="ecoreDiff::ENamedElement", is_abstract=True)
ecoreDiff_EPackage = Class(name="ecoreDiff::EPackage")
ecoreDiff_EFactory = Class(name="ecoreDiff::EFactory")
ecoreDiff_EDataType = Class(name="ecoreDiff::EDataType")
ecoreDiff_EClassifier = Class(name="ecoreDiff::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecoreDiff_ETypeParameter = Class(name="ecoreDiff::ETypeParameter")
ecoreDiff_EClassifier_Wildcard = Class(name="ecoreDiff::EClassifier::Wildcard")
ETypedElement = Class(name="ETypedElement")
ecoreDiff_EParameter = Class(name="ecoreDiff::EParameter")
ecoreDiff_ETypedElement = Class(name="ecoreDiff::ETypedElement", is_abstract=True)
EObject = Class(name="EObject")
ecoreDiff_EStructuralFeature_Wildcard = Class(name="ecoreDiff::EStructuralFeature::Wildcard")
ecoreDiff_EReference = Class(name="ecoreDiff::EReference")
ecoreDiff_EAttribute = Class(name="ecoreDiff::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
ecoreDiff_EEnum = Class(name="ecoreDiff::EEnum")
EDataType = Class(name="EDataType")
ecoreDiff_EEnumLiteral = Class(name="ecoreDiff::EEnumLiteral")
ecoreDiff_AddedEAnnotation = Class(name="ecoreDiff::AddedEAnnotation")
EAnnotation = Class(name="EAnnotation")
ecoreDiff_DeletedEAnnotation = Class(name="ecoreDiff::DeletedEAnnotation")
DifferenceElement = Class(name="DifferenceElement")
ecoreDiff_DifferenceModel = Class(name="ecoreDiff::DifferenceModel")
ecoreDiff_DifferenceElement = Class(name="ecoreDiff::DifferenceElement")
ecoreDiff_AddedEObject = Class(name="ecoreDiff::AddedEObject")
ecoreDiff_DeletedEObject = Class(name="ecoreDiff::DeletedEObject")
ecoreDiff_ChangedEObject = Class(name="ecoreDiff::ChangedEObject")
ecoreDiff_ChangedEAnnotation = Class(name="ecoreDiff::ChangedEAnnotation")
ecoreDiff_AddedEStringToStringMapEntry = Class(name="ecoreDiff::AddedEStringToStringMapEntry")
EStringToStringMapEntry = Class(name="EStringToStringMapEntry")
ecoreDiff_DeletedEStringToStringMapEntry = Class(name="ecoreDiff::DeletedEStringToStringMapEntry")
ecoreDiff_ChangedEStringToStringMapEntry = Class(name="ecoreDiff::ChangedEStringToStringMapEntry")
ecoreDiff_AddedEClassifier = Class(name="ecoreDiff::AddedEClassifier")
ecoreDiff_DeletedEClassifier = Class(name="ecoreDiff::DeletedEClassifier")
ecoreDiff_ChangedEClassifier = Class(name="ecoreDiff::ChangedEClassifier")
ecoreDiff_AddedENamedElement = Class(name="ecoreDiff::AddedENamedElement")
ecoreDiff_DeletedENamedElement = Class(name="ecoreDiff::DeletedENamedElement")
ecoreDiff_AddedEClass = Class(name="ecoreDiff::AddedEClass")
EClass = Class(name="EClass")
ecoreDiff_DeletedEClass = Class(name="ecoreDiff::DeletedEClass")
ecoreDiff_ChangedEClass = Class(name="ecoreDiff::ChangedEClass")
ecoreDiff_AddedEFactory = Class(name="ecoreDiff::AddedEFactory")
EFactory = Class(name="EFactory")
ecoreDiff_DeletedEFactory = Class(name="ecoreDiff::DeletedEFactory")
ecoreDiff_ChangedEFactory = Class(name="ecoreDiff::ChangedEFactory")
ecoreDiff_AddedEDataType = Class(name="ecoreDiff::AddedEDataType")
ecoreDiff_DeletedEDataType = Class(name="ecoreDiff::DeletedEDataType")
ecoreDiff_ChangedEDataType = Class(name="ecoreDiff::ChangedEDataType")
ecoreDiff_ChangedENamedElement = Class(name="ecoreDiff::ChangedENamedElement")
ecoreDiff_AddedEPackage = Class(name="ecoreDiff::AddedEPackage")
EPackage = Class(name="EPackage")
ecoreDiff_DeletedEPackage = Class(name="ecoreDiff::DeletedEPackage")
ecoreDiff_ChangedEPackage = Class(name="ecoreDiff::ChangedEPackage")
ecoreDiff_AddedEGenericType = Class(name="ecoreDiff::AddedEGenericType")
EGenericType = Class(name="EGenericType")
ecoreDiff_DeletedEGenericType = Class(name="ecoreDiff::DeletedEGenericType")
ecoreDiff_ChangedEGenericType = Class(name="ecoreDiff::ChangedEGenericType")
ecoreDiff_AddedEClassifier_Wildcard = Class(name="ecoreDiff::AddedEClassifier::Wildcard")
EClassifier_Wildcard = Class(name="EClassifier::Wildcard")
ecoreDiff_DeletedEClassifier_Wildcard = Class(name="ecoreDiff::DeletedEClassifier::Wildcard")
ecoreDiff_AddedETypeParameter = Class(name="ecoreDiff::AddedETypeParameter")
ETypeParameter = Class(name="ETypeParameter")
ecoreDiff_DeletedETypeParameter = Class(name="ecoreDiff::DeletedETypeParameter")
ecoreDiff_ChangedETypeParameter = Class(name="ecoreDiff::ChangedETypeParameter")
ecoreDiff_DeletedEOperation = Class(name="ecoreDiff::DeletedEOperation")
ecoreDiff_ChangedEOperation = Class(name="ecoreDiff::ChangedEOperation")
ecoreDiff_AddedETypedElement = Class(name="ecoreDiff::AddedETypedElement")
ecoreDiff_DeletedETypedElement = Class(name="ecoreDiff::DeletedETypedElement")
ecoreDiff_ChangedEClassifier_Wildcard = Class(name="ecoreDiff::ChangedEClassifier::Wildcard")
ecoreDiff_AddedEOperation = Class(name="ecoreDiff::AddedEOperation")
EOperation = Class(name="EOperation")
ecoreDiff_DeletedEParameter = Class(name="ecoreDiff::DeletedEParameter")
ecoreDiff_ChangedEParameter = Class(name="ecoreDiff::ChangedEParameter")
ecoreDiff_AddedEAttribute = Class(name="ecoreDiff::AddedEAttribute")
EAttribute = Class(name="EAttribute")
ecoreDiff_DeletedEAttribute = Class(name="ecoreDiff::DeletedEAttribute")
ecoreDiff_ChangedETypedElement = Class(name="ecoreDiff::ChangedETypedElement")
ecoreDiff_AddedEParameter = Class(name="ecoreDiff::AddedEParameter")
EParameter = Class(name="EParameter")
ecoreDiff_ChangedEStructuralFeature = Class(name="ecoreDiff::ChangedEStructuralFeature")
ecoreDiff_AddedEStructuralFeature_Wildcard = Class(name="ecoreDiff::AddedEStructuralFeature::Wildcard")
EStructuralFeature_Wildcard = Class(name="EStructuralFeature::Wildcard")
ecoreDiff_DeletedEStructuralFeature_Wildcard = Class(name="ecoreDiff::DeletedEStructuralFeature::Wildcard")
ecoreDiff_ChangedEAttribute = Class(name="ecoreDiff::ChangedEAttribute")
ecoreDiff_AddedEStructuralFeature = Class(name="ecoreDiff::AddedEStructuralFeature")
ecoreDiff_DeletedEStructuralFeature = Class(name="ecoreDiff::DeletedEStructuralFeature")
ecoreDiff_DeletedEReference = Class(name="ecoreDiff::DeletedEReference")
ecoreDiff_ChangedEReference = Class(name="ecoreDiff::ChangedEReference")
ecoreDiff_ChangedEStructuralFeature_Wildcard = Class(name="ecoreDiff::ChangedEStructuralFeature::Wildcard")
ecoreDiff_AddedEReference = Class(name="ecoreDiff::AddedEReference")
EReference = Class(name="EReference")
ecoreDiff_ChangedEEnum = Class(name="ecoreDiff::ChangedEEnum")
ecoreDiff_AddedEEnumLiteral = Class(name="ecoreDiff::AddedEEnumLiteral")
EEnumLiteral = Class(name="EEnumLiteral")
ecoreDiff_AddedEEnum = Class(name="ecoreDiff::AddedEEnum")
EEnum = Class(name="EEnum")
ecoreDiff_DeletedEEnum = Class(name="ecoreDiff::DeletedEEnum")
ecoreDiff_AddedEModelElement = Class(name="ecoreDiff::AddedEModelElement")
ecoreDiff_DeletedEModelElement = Class(name="ecoreDiff::DeletedEModelElement")
ecoreDiff_ChangedEModelElement = Class(name="ecoreDiff::ChangedEModelElement")
ecoreDiff_DeletedEEnumLiteral = Class(name="ecoreDiff::DeletedEEnumLiteral")
ecoreDiff_ChangedEEnumLiteral = Class(name="ecoreDiff::ChangedEEnumLiteral")

# ecoreDiff_EObject class attributes and methods

# ecoreDiff_EClass class attributes and methods
ecoreDiff_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecoreDiff_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecoreDiff_EClass.attributes={ecoreDiff_EClass_abstract, ecoreDiff_EClass_interface}

# EClassifier class attributes and methods

# ecoreDiff_EOperation class attributes and methods

# ecoreDiff_EStructuralFeature class attributes and methods
ecoreDiff_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecoreDiff_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecoreDiff_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecoreDiff_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecoreDiff_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecoreDiff_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecoreDiff_EStructuralFeature.attributes={ecoreDiff_EStructuralFeature_unsettable, ecoreDiff_EStructuralFeature_transient, ecoreDiff_EStructuralFeature_defaultValueLiteral, ecoreDiff_EStructuralFeature_volatile, ecoreDiff_EStructuralFeature_changeable, ecoreDiff_EStructuralFeature_derived}

# ecoreDiff_EGenericType class attributes and methods

# ecoreDiff_EAnnotation class attributes and methods
ecoreDiff_EAnnotation_source: Property = Property(name="source", type=StringType)
ecoreDiff_EAnnotation.attributes={ecoreDiff_EAnnotation_source}

# EModelElement class attributes and methods

# ecoreDiff_EStringToStringMapEntry class attributes and methods
ecoreDiff_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecoreDiff_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecoreDiff_EStringToStringMapEntry.attributes={ecoreDiff_EStringToStringMapEntry_key, ecoreDiff_EStringToStringMapEntry_value}

# ecoreDiff_EModelElement class attributes and methods

# ecoreDiff_ENamedElement class attributes and methods
ecoreDiff_ENamedElement_name: Property = Property(name="name", type=StringType)
ecoreDiff_ENamedElement.attributes={ecoreDiff_ENamedElement_name}

# ecoreDiff_EPackage class attributes and methods
ecoreDiff_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecoreDiff_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecoreDiff_EPackage.attributes={ecoreDiff_EPackage_nsURI, ecoreDiff_EPackage_nsPrefix}

# ecoreDiff_EFactory class attributes and methods

# ecoreDiff_EDataType class attributes and methods
ecoreDiff_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecoreDiff_EDataType.attributes={ecoreDiff_EDataType_serializable}

# ecoreDiff_EClassifier class attributes and methods
ecoreDiff_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecoreDiff_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecoreDiff_EClassifier.attributes={ecoreDiff_EClassifier_instanceTypeName, ecoreDiff_EClassifier_instanceClassName}

# ENamedElement class attributes and methods

# ecoreDiff_ETypeParameter class attributes and methods

# ecoreDiff_EClassifier_Wildcard class attributes and methods

# ETypedElement class attributes and methods

# ecoreDiff_EParameter class attributes and methods

# ecoreDiff_ETypedElement class attributes and methods
ecoreDiff_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecoreDiff_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecoreDiff_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecoreDiff_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecoreDiff_ETypedElement.attributes={ecoreDiff_ETypedElement_lowerBound, ecoreDiff_ETypedElement_ordered, ecoreDiff_ETypedElement_upperBound, ecoreDiff_ETypedElement_unique}

# EObject class attributes and methods

# ecoreDiff_EStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_EReference class attributes and methods
ecoreDiff_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecoreDiff_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecoreDiff_EReference.attributes={ecoreDiff_EReference_containment, ecoreDiff_EReference_resolveProxies}

# ecoreDiff_EAttribute class attributes and methods
ecoreDiff_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecoreDiff_EAttribute.attributes={ecoreDiff_EAttribute_iD}

# EStructuralFeature class attributes and methods

# ecoreDiff_EEnum class attributes and methods

# EDataType class attributes and methods

# ecoreDiff_EEnumLiteral class attributes and methods
ecoreDiff_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecoreDiff_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecoreDiff_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecoreDiff_EEnumLiteral.attributes={ecoreDiff_EEnumLiteral_instance, ecoreDiff_EEnumLiteral_literal, ecoreDiff_EEnumLiteral_value}

# ecoreDiff_AddedEAnnotation class attributes and methods

# EAnnotation class attributes and methods

# ecoreDiff_DeletedEAnnotation class attributes and methods

# DifferenceElement class attributes and methods

# ecoreDiff_DifferenceModel class attributes and methods

# ecoreDiff_DifferenceElement class attributes and methods

# ecoreDiff_AddedEObject class attributes and methods

# ecoreDiff_DeletedEObject class attributes and methods

# ecoreDiff_ChangedEObject class attributes and methods

# ecoreDiff_ChangedEAnnotation class attributes and methods

# ecoreDiff_AddedEStringToStringMapEntry class attributes and methods

# EStringToStringMapEntry class attributes and methods

# ecoreDiff_DeletedEStringToStringMapEntry class attributes and methods

# ecoreDiff_ChangedEStringToStringMapEntry class attributes and methods

# ecoreDiff_AddedEClassifier class attributes and methods

# ecoreDiff_DeletedEClassifier class attributes and methods

# ecoreDiff_ChangedEClassifier class attributes and methods

# ecoreDiff_AddedENamedElement class attributes and methods

# ecoreDiff_DeletedENamedElement class attributes and methods

# ecoreDiff_AddedEClass class attributes and methods

# EClass class attributes and methods

# ecoreDiff_DeletedEClass class attributes and methods

# ecoreDiff_ChangedEClass class attributes and methods

# ecoreDiff_AddedEFactory class attributes and methods

# EFactory class attributes and methods

# ecoreDiff_DeletedEFactory class attributes and methods

# ecoreDiff_ChangedEFactory class attributes and methods

# ecoreDiff_AddedEDataType class attributes and methods

# ecoreDiff_DeletedEDataType class attributes and methods

# ecoreDiff_ChangedEDataType class attributes and methods

# ecoreDiff_ChangedENamedElement class attributes and methods

# ecoreDiff_AddedEPackage class attributes and methods

# EPackage class attributes and methods

# ecoreDiff_DeletedEPackage class attributes and methods

# ecoreDiff_ChangedEPackage class attributes and methods

# ecoreDiff_AddedEGenericType class attributes and methods

# EGenericType class attributes and methods

# ecoreDiff_DeletedEGenericType class attributes and methods

# ecoreDiff_ChangedEGenericType class attributes and methods

# ecoreDiff_AddedEClassifier_Wildcard class attributes and methods

# EClassifier_Wildcard class attributes and methods

# ecoreDiff_DeletedEClassifier_Wildcard class attributes and methods

# ecoreDiff_AddedETypeParameter class attributes and methods

# ETypeParameter class attributes and methods

# ecoreDiff_DeletedETypeParameter class attributes and methods

# ecoreDiff_ChangedETypeParameter class attributes and methods

# ecoreDiff_DeletedEOperation class attributes and methods

# ecoreDiff_ChangedEOperation class attributes and methods

# ecoreDiff_AddedETypedElement class attributes and methods

# ecoreDiff_DeletedETypedElement class attributes and methods

# ecoreDiff_ChangedEClassifier_Wildcard class attributes and methods

# ecoreDiff_AddedEOperation class attributes and methods

# EOperation class attributes and methods

# ecoreDiff_DeletedEParameter class attributes and methods

# ecoreDiff_ChangedEParameter class attributes and methods

# ecoreDiff_AddedEAttribute class attributes and methods

# EAttribute class attributes and methods

# ecoreDiff_DeletedEAttribute class attributes and methods

# ecoreDiff_ChangedETypedElement class attributes and methods

# ecoreDiff_AddedEParameter class attributes and methods

# EParameter class attributes and methods

# ecoreDiff_ChangedEStructuralFeature class attributes and methods

# ecoreDiff_AddedEStructuralFeature_Wildcard class attributes and methods

# EStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_DeletedEStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_ChangedEAttribute class attributes and methods

# ecoreDiff_AddedEStructuralFeature class attributes and methods

# ecoreDiff_DeletedEStructuralFeature class attributes and methods

# ecoreDiff_DeletedEReference class attributes and methods

# ecoreDiff_ChangedEReference class attributes and methods

# ecoreDiff_ChangedEStructuralFeature_Wildcard class attributes and methods

# ecoreDiff_AddedEReference class attributes and methods

# EReference class attributes and methods

# ecoreDiff_ChangedEEnum class attributes and methods

# ecoreDiff_AddedEEnumLiteral class attributes and methods

# EEnumLiteral class attributes and methods

# ecoreDiff_AddedEEnum class attributes and methods

# EEnum class attributes and methods

# ecoreDiff_DeletedEEnum class attributes and methods

# ecoreDiff_AddedEModelElement class attributes and methods

# ecoreDiff_DeletedEModelElement class attributes and methods

# ecoreDiff_ChangedEModelElement class attributes and methods

# ecoreDiff_DeletedEEnumLiteral class attributes and methods

# ecoreDiff_ChangedEEnumLiteral class attributes and methods

# Relationships
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
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="ecoreDiff_EOperation", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass11", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eStructuralFeatures12: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures12",
    ends={
        Property(name="ecoreDiff_EStructuralFeature", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass13", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="ecoreDiff_EModelElement", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EAnnotation2", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
eFactoryInstance20: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance20",
    ends={
        Property(name="ecoreDiff_EFactory", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EPackage", type=ecoreDiff_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eSubpackages22: BinaryAssociation = BinaryAssociation(
    name="eSubpackages22",
    ends={
        Property(name="ecoreDiff_EPackage23", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EPackage21", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage25: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage25",
    ends={
        Property(name="ecoreDiff_EPackage26", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EPackage24", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eClassifiers27: BinaryAssociation = BinaryAssociation(
    name="eClassifiers27",
    ends={
        Property(name="ecoreDiff_EClassifier29", type=ecoreDiff_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EPackage28", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage30: BinaryAssociation = BinaryAssociation(
    name="ePackage30",
    ends={
        Property(name="ecoreDiff_EObject32", type=ecoreDiff_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EFactory31", type=ecoreDiff_EObject, multiplicity=Multiplicity(1, 1))
    }
)
eGenericSuperTypes14: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes14",
    ends={
        Property(name="ecoreDiff_EGenericType", type=ecoreDiff_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClass15", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage16: BinaryAssociation = BinaryAssociation(
    name="ePackage16",
    ends={
        Property(name="ecoreDiff_EObject17", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClassifier", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters18: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters18",
    ends={
        Property(name="ecoreDiff_ETypeParameter", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EClassifier19", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeParameters51: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters51",
    ends={
        Property(name="ecoreDiff_ETypeParameter53", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation52", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters54: BinaryAssociation = BinaryAssociation(
    name="eParameters54",
    ends={
        Property(name="ecoreDiff_EParameter", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation55", type=ecoreDiff_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions56: BinaryAssociation = BinaryAssociation(
    name="eExceptions56",
    ends={
        Property(name="ecoreDiff_EClassifier58", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation57", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions59: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions59",
    ends={
        Property(name="ecoreDiff_EGenericType61", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation60", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass62: BinaryAssociation = BinaryAssociation(
    name="eContainingClass62",
    ends={
        Property(name="ecoreDiff_EObject64", type=ecoreDiff_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EOperation63", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eBounds33: BinaryAssociation = BinaryAssociation(
    name="eBounds33",
    ends={
        Property(name="ecoreDiff_EGenericType35", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypeParameter34", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound37: BinaryAssociation = BinaryAssociation(
    name="eUpperBound37",
    ends={
        Property(name="ecoreDiff_EGenericType38", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType36", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments40: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments40",
    ends={
        Property(name="ecoreDiff_EGenericType41", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType39", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLowerBound43: BinaryAssociation = BinaryAssociation(
    name="eLowerBound43",
    ends={
        Property(name="ecoreDiff_EGenericType44", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType42", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter45: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter45",
    ends={
        Property(name="ecoreDiff_ETypeParameter47", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType46", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier48: BinaryAssociation = BinaryAssociation(
    name="eClassifier48",
    ends={
        Property(name="ecoreDiff_EClassifier50", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EGenericType49", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass73: BinaryAssociation = BinaryAssociation(
    name="eContainingClass73",
    ends={
        Property(name="ecoreDiff_EObject75", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EStructuralFeature74", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite77: BinaryAssociation = BinaryAssociation(
    name="eOpposite77",
    ends={
        Property(name="ecoreDiff_EReference", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference76", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eKeys78: BinaryAssociation = BinaryAssociation(
    name="eKeys78",
    ends={
        Property(name="ecoreDiff_EAttribute", type=ecoreDiff_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EReference79", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eType65: BinaryAssociation = BinaryAssociation(
    name="eType65",
    ends={
        Property(name="ecoreDiff_EObject66", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType67: BinaryAssociation = BinaryAssociation(
    name="eGenericType67",
    ends={
        Property(name="ecoreDiff_EGenericType69", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ETypedElement68", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eOperation70: BinaryAssociation = BinaryAssociation(
    name="eOperation70",
    ends={
        Property(name="ecoreDiff_EOperation72", type=ecoreDiff_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EParameter71", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eLiterals80: BinaryAssociation = BinaryAssociation(
    name="eLiterals80",
    ends={
        Property(name="ecoreDiff_EEnumLiteral", type=ecoreDiff_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EEnum", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum81: BinaryAssociation = BinaryAssociation(
    name="eEnum81",
    ends={
        Property(name="ecoreDiff_EEnum83", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EEnumLiteral82", type=ecoreDiff_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement88: BinaryAssociation = BinaryAssociation(
    name="applicationElement88",
    ends={
        Property(name="ecoreDiff_EObject89", type=ecoreDiff_AddedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEAnnotation", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations84: BinaryAssociation = BinaryAssociation(
    name="eAnnotations84",
    ends={
        Property(name="ecoreDiff_EAnnotation86", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_EModelElement85", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
updatedElement101: BinaryAssociation = BinaryAssociation(
    name="updatedElement101",
    ends={
        Property(name="ecoreDiff_EStringToStringMapEntry102", type=ecoreDiff_ChangedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStringToStringMapEntry", type=ecoreDiff_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999))
    }
)
differenceElements87: BinaryAssociation = BinaryAssociation(
    name="differenceElements87",
    ends={
        Property(name="ecoreDiff_DifferenceElement", type=ecoreDiff_DifferenceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DifferenceModel", type=ecoreDiff_DifferenceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
applicationElement103: BinaryAssociation = BinaryAssociation(
    name="applicationElement103",
    ends={
        Property(name="ecoreDiff_EObject105", type=ecoreDiff_ChangedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStringToStringMapEntry104", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement106: BinaryAssociation = BinaryAssociation(
    name="applicationElement106",
    ends={
        Property(name="ecoreDiff_EObject107", type=ecoreDiff_AddedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEObject", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement108: BinaryAssociation = BinaryAssociation(
    name="applicationElement108",
    ends={
        Property(name="ecoreDiff_EObject109", type=ecoreDiff_DeletedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEObject", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement110: BinaryAssociation = BinaryAssociation(
    name="updatedElement110",
    ends={
        Property(name="ecoreDiff_EObject111", type=ecoreDiff_ChangedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEObject", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement90: BinaryAssociation = BinaryAssociation(
    name="applicationElement90",
    ends={
        Property(name="ecoreDiff_EObject91", type=ecoreDiff_DeletedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEAnnotation", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement92: BinaryAssociation = BinaryAssociation(
    name="updatedElement92",
    ends={
        Property(name="ecoreDiff_EAnnotation93", type=ecoreDiff_ChangedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAnnotation", type=ecoreDiff_EAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement94: BinaryAssociation = BinaryAssociation(
    name="applicationElement94",
    ends={
        Property(name="ecoreDiff_EObject96", type=ecoreDiff_ChangedEAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAnnotation95", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement97: BinaryAssociation = BinaryAssociation(
    name="applicationElement97",
    ends={
        Property(name="ecoreDiff_EObject98", type=ecoreDiff_AddedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEStringToStringMapEntry", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement99: BinaryAssociation = BinaryAssociation(
    name="applicationElement99",
    ends={
        Property(name="ecoreDiff_EObject100", type=ecoreDiff_DeletedEStringToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEStringToStringMapEntry", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement121: BinaryAssociation = BinaryAssociation(
    name="applicationElement121",
    ends={
        Property(name="ecoreDiff_EObject123", type=ecoreDiff_ChangedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClass122", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement124: BinaryAssociation = BinaryAssociation(
    name="applicationElement124",
    ends={
        Property(name="ecoreDiff_EObject125", type=ecoreDiff_AddedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEClassifier", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement126: BinaryAssociation = BinaryAssociation(
    name="applicationElement126",
    ends={
        Property(name="ecoreDiff_EObject127", type=ecoreDiff_DeletedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEClassifier", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement128: BinaryAssociation = BinaryAssociation(
    name="updatedElement128",
    ends={
        Property(name="ecoreDiff_EClassifier129", type=ecoreDiff_ChangedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier", type=ecoreDiff_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement130: BinaryAssociation = BinaryAssociation(
    name="applicationElement130",
    ends={
        Property(name="ecoreDiff_EObject132", type=ecoreDiff_ChangedEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier131", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement133: BinaryAssociation = BinaryAssociation(
    name="applicationElement133",
    ends={
        Property(name="ecoreDiff_EObject134", type=ecoreDiff_AddedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedENamedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement135: BinaryAssociation = BinaryAssociation(
    name="applicationElement135",
    ends={
        Property(name="ecoreDiff_EObject136", type=ecoreDiff_DeletedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedENamedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement112: BinaryAssociation = BinaryAssociation(
    name="applicationElement112",
    ends={
        Property(name="ecoreDiff_EObject114", type=ecoreDiff_ChangedEObject, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEObject113", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement115: BinaryAssociation = BinaryAssociation(
    name="applicationElement115",
    ends={
        Property(name="ecoreDiff_EObject116", type=ecoreDiff_AddedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEClass", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement117: BinaryAssociation = BinaryAssociation(
    name="applicationElement117",
    ends={
        Property(name="ecoreDiff_EObject118", type=ecoreDiff_DeletedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEClass", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement119: BinaryAssociation = BinaryAssociation(
    name="updatedElement119",
    ends={
        Property(name="ecoreDiff_EClass120", type=ecoreDiff_ChangedEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClass", type=ecoreDiff_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement150: BinaryAssociation = BinaryAssociation(
    name="applicationElement150",
    ends={
        Property(name="ecoreDiff_EObject151", type=ecoreDiff_AddedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEFactory", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement152: BinaryAssociation = BinaryAssociation(
    name="applicationElement152",
    ends={
        Property(name="ecoreDiff_EObject153", type=ecoreDiff_DeletedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEFactory", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement154: BinaryAssociation = BinaryAssociation(
    name="updatedElement154",
    ends={
        Property(name="ecoreDiff_EFactory155", type=ecoreDiff_ChangedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEFactory", type=ecoreDiff_EFactory, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement156: BinaryAssociation = BinaryAssociation(
    name="applicationElement156",
    ends={
        Property(name="ecoreDiff_EObject158", type=ecoreDiff_ChangedEFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEFactory157", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement159: BinaryAssociation = BinaryAssociation(
    name="applicationElement159",
    ends={
        Property(name="ecoreDiff_EObject160", type=ecoreDiff_AddedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEDataType", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement161: BinaryAssociation = BinaryAssociation(
    name="applicationElement161",
    ends={
        Property(name="ecoreDiff_EObject162", type=ecoreDiff_DeletedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEDataType", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement137: BinaryAssociation = BinaryAssociation(
    name="updatedElement137",
    ends={
        Property(name="ecoreDiff_ENamedElement", type=ecoreDiff_ChangedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedENamedElement", type=ecoreDiff_ENamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement138: BinaryAssociation = BinaryAssociation(
    name="applicationElement138",
    ends={
        Property(name="ecoreDiff_EObject140", type=ecoreDiff_ChangedENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedENamedElement139", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement141: BinaryAssociation = BinaryAssociation(
    name="applicationElement141",
    ends={
        Property(name="ecoreDiff_EObject142", type=ecoreDiff_AddedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEPackage", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement143: BinaryAssociation = BinaryAssociation(
    name="applicationElement143",
    ends={
        Property(name="ecoreDiff_EObject144", type=ecoreDiff_DeletedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEPackage", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement145: BinaryAssociation = BinaryAssociation(
    name="updatedElement145",
    ends={
        Property(name="ecoreDiff_EPackage146", type=ecoreDiff_ChangedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEPackage", type=ecoreDiff_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement147: BinaryAssociation = BinaryAssociation(
    name="applicationElement147",
    ends={
        Property(name="ecoreDiff_EObject149", type=ecoreDiff_ChangedEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEPackage148", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement176: BinaryAssociation = BinaryAssociation(
    name="applicationElement176",
    ends={
        Property(name="ecoreDiff_EObject177", type=ecoreDiff_AddedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEGenericType", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement178: BinaryAssociation = BinaryAssociation(
    name="applicationElement178",
    ends={
        Property(name="ecoreDiff_EObject179", type=ecoreDiff_DeletedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEGenericType", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement180: BinaryAssociation = BinaryAssociation(
    name="updatedElement180",
    ends={
        Property(name="ecoreDiff_EGenericType181", type=ecoreDiff_ChangedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEGenericType", type=ecoreDiff_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement182: BinaryAssociation = BinaryAssociation(
    name="applicationElement182",
    ends={
        Property(name="ecoreDiff_EObject184", type=ecoreDiff_ChangedEGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEGenericType183", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement185: BinaryAssociation = BinaryAssociation(
    name="applicationElement185",
    ends={
        Property(name="ecoreDiff_EObject186", type=ecoreDiff_AddedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEClassifier_Wildcard", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement163: BinaryAssociation = BinaryAssociation(
    name="updatedElement163",
    ends={
        Property(name="ecoreDiff_EDataType", type=ecoreDiff_ChangedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEDataType", type=ecoreDiff_EDataType, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement164: BinaryAssociation = BinaryAssociation(
    name="applicationElement164",
    ends={
        Property(name="ecoreDiff_EObject166", type=ecoreDiff_ChangedEDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEDataType165", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement167: BinaryAssociation = BinaryAssociation(
    name="applicationElement167",
    ends={
        Property(name="ecoreDiff_EObject168", type=ecoreDiff_AddedETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedETypeParameter", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
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
        Property(name="ecoreDiff_ChangedETypeParameter", type=ecoreDiff_ETypeParameter, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement173: BinaryAssociation = BinaryAssociation(
    name="applicationElement173",
    ends={
        Property(name="ecoreDiff_EObject175", type=ecoreDiff_ChangedETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypeParameter174", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement195: BinaryAssociation = BinaryAssociation(
    name="applicationElement195",
    ends={
        Property(name="ecoreDiff_EObject196", type=ecoreDiff_DeletedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEOperation", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement197: BinaryAssociation = BinaryAssociation(
    name="updatedElement197",
    ends={
        Property(name="ecoreDiff_EOperation198", type=ecoreDiff_ChangedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEOperation", type=ecoreDiff_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement199: BinaryAssociation = BinaryAssociation(
    name="applicationElement199",
    ends={
        Property(name="ecoreDiff_EObject201", type=ecoreDiff_ChangedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEOperation200", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement202: BinaryAssociation = BinaryAssociation(
    name="applicationElement202",
    ends={
        Property(name="ecoreDiff_EObject203", type=ecoreDiff_AddedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedETypedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement204: BinaryAssociation = BinaryAssociation(
    name="applicationElement204",
    ends={
        Property(name="ecoreDiff_EObject205", type=ecoreDiff_DeletedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedETypedElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement187: BinaryAssociation = BinaryAssociation(
    name="applicationElement187",
    ends={
        Property(name="ecoreDiff_EObject188", type=ecoreDiff_DeletedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEClassifier_Wildcard", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement189: BinaryAssociation = BinaryAssociation(
    name="updatedElement189",
    ends={
        Property(name="ecoreDiff_EClassifier_Wildcard", type=ecoreDiff_ChangedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier_Wildcard", type=ecoreDiff_EClassifier_Wildcard, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement190: BinaryAssociation = BinaryAssociation(
    name="applicationElement190",
    ends={
        Property(name="ecoreDiff_EObject192", type=ecoreDiff_ChangedEClassifier_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEClassifier_Wildcard191", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement193: BinaryAssociation = BinaryAssociation(
    name="applicationElement193",
    ends={
        Property(name="ecoreDiff_EObject194", type=ecoreDiff_AddedEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEOperation", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement213: BinaryAssociation = BinaryAssociation(
    name="applicationElement213",
    ends={
        Property(name="ecoreDiff_EObject214", type=ecoreDiff_DeletedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEParameter", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement215: BinaryAssociation = BinaryAssociation(
    name="updatedElement215",
    ends={
        Property(name="ecoreDiff_EParameter216", type=ecoreDiff_ChangedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEParameter", type=ecoreDiff_EParameter, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement217: BinaryAssociation = BinaryAssociation(
    name="applicationElement217",
    ends={
        Property(name="ecoreDiff_EObject219", type=ecoreDiff_ChangedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEParameter218", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement220: BinaryAssociation = BinaryAssociation(
    name="applicationElement220",
    ends={
        Property(name="ecoreDiff_EObject221", type=ecoreDiff_AddedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEAttribute", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement222: BinaryAssociation = BinaryAssociation(
    name="applicationElement222",
    ends={
        Property(name="ecoreDiff_EObject223", type=ecoreDiff_DeletedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEAttribute", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement206: BinaryAssociation = BinaryAssociation(
    name="updatedElement206",
    ends={
        Property(name="ecoreDiff_ETypedElement207", type=ecoreDiff_ChangedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypedElement", type=ecoreDiff_ETypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement208: BinaryAssociation = BinaryAssociation(
    name="applicationElement208",
    ends={
        Property(name="ecoreDiff_EObject210", type=ecoreDiff_ChangedETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedETypedElement209", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement211: BinaryAssociation = BinaryAssociation(
    name="applicationElement211",
    ends={
        Property(name="ecoreDiff_EObject212", type=ecoreDiff_AddedEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEParameter", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement233: BinaryAssociation = BinaryAssociation(
    name="updatedElement233",
    ends={
        Property(name="ecoreDiff_EStructuralFeature234", type=ecoreDiff_ChangedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature", type=ecoreDiff_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement235: BinaryAssociation = BinaryAssociation(
    name="applicationElement235",
    ends={
        Property(name="ecoreDiff_EObject237", type=ecoreDiff_ChangedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature236", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement238: BinaryAssociation = BinaryAssociation(
    name="applicationElement238",
    ends={
        Property(name="ecoreDiff_EObject239", type=ecoreDiff_AddedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEStructuralFeature_Wildcard", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement240: BinaryAssociation = BinaryAssociation(
    name="applicationElement240",
    ends={
        Property(name="ecoreDiff_EObject241", type=ecoreDiff_DeletedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEStructuralFeature_Wildcard", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement224: BinaryAssociation = BinaryAssociation(
    name="updatedElement224",
    ends={
        Property(name="ecoreDiff_EAttribute225", type=ecoreDiff_ChangedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAttribute", type=ecoreDiff_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement226: BinaryAssociation = BinaryAssociation(
    name="applicationElement226",
    ends={
        Property(name="ecoreDiff_EObject228", type=ecoreDiff_ChangedEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEAttribute227", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement229: BinaryAssociation = BinaryAssociation(
    name="applicationElement229",
    ends={
        Property(name="ecoreDiff_EObject230", type=ecoreDiff_AddedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEStructuralFeature", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement231: BinaryAssociation = BinaryAssociation(
    name="applicationElement231",
    ends={
        Property(name="ecoreDiff_EObject232", type=ecoreDiff_DeletedEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEStructuralFeature", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement248: BinaryAssociation = BinaryAssociation(
    name="applicationElement248",
    ends={
        Property(name="ecoreDiff_EObject249", type=ecoreDiff_DeletedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEReference", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement250: BinaryAssociation = BinaryAssociation(
    name="updatedElement250",
    ends={
        Property(name="ecoreDiff_EReference251", type=ecoreDiff_ChangedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEReference", type=ecoreDiff_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
updatedElement242: BinaryAssociation = BinaryAssociation(
    name="updatedElement242",
    ends={
        Property(name="ecoreDiff_EStructuralFeature_Wildcard", type=ecoreDiff_ChangedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature_Wildcard", type=ecoreDiff_EStructuralFeature_Wildcard, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement243: BinaryAssociation = BinaryAssociation(
    name="applicationElement243",
    ends={
        Property(name="ecoreDiff_EObject245", type=ecoreDiff_ChangedEStructuralFeature_Wildcard, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEStructuralFeature_Wildcard244", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement246: BinaryAssociation = BinaryAssociation(
    name="applicationElement246",
    ends={
        Property(name="ecoreDiff_EObject247", type=ecoreDiff_AddedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEReference", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement259: BinaryAssociation = BinaryAssociation(
    name="updatedElement259",
    ends={
        Property(name="ecoreDiff_EEnum260", type=ecoreDiff_ChangedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnum", type=ecoreDiff_EEnum, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement261: BinaryAssociation = BinaryAssociation(
    name="applicationElement261",
    ends={
        Property(name="ecoreDiff_EObject263", type=ecoreDiff_ChangedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnum262", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement252: BinaryAssociation = BinaryAssociation(
    name="applicationElement252",
    ends={
        Property(name="ecoreDiff_EObject254", type=ecoreDiff_ChangedEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEReference253", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement255: BinaryAssociation = BinaryAssociation(
    name="applicationElement255",
    ends={
        Property(name="ecoreDiff_EObject256", type=ecoreDiff_AddedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEEnum", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement257: BinaryAssociation = BinaryAssociation(
    name="applicationElement257",
    ends={
        Property(name="ecoreDiff_EObject258", type=ecoreDiff_DeletedEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEEnum", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement268: BinaryAssociation = BinaryAssociation(
    name="updatedElement268",
    ends={
        Property(name="ecoreDiff_EEnumLiteral269", type=ecoreDiff_ChangedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnumLiteral", type=ecoreDiff_EEnumLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement270: BinaryAssociation = BinaryAssociation(
    name="applicationElement270",
    ends={
        Property(name="ecoreDiff_EObject272", type=ecoreDiff_ChangedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEEnumLiteral271", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement273: BinaryAssociation = BinaryAssociation(
    name="applicationElement273",
    ends={
        Property(name="ecoreDiff_EObject274", type=ecoreDiff_DeletedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEModelElement", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
updatedElement275: BinaryAssociation = BinaryAssociation(
    name="updatedElement275",
    ends={
        Property(name="ecoreDiff_EModelElement276", type=ecoreDiff_ChangedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEModelElement", type=ecoreDiff_EModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
applicationElement264: BinaryAssociation = BinaryAssociation(
    name="applicationElement264",
    ends={
        Property(name="ecoreDiff_EObject265", type=ecoreDiff_AddedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_AddedEEnumLiteral", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement266: BinaryAssociation = BinaryAssociation(
    name="applicationElement266",
    ends={
        Property(name="ecoreDiff_EObject267", type=ecoreDiff_DeletedEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_DeletedEEnumLiteral", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)
applicationElement277: BinaryAssociation = BinaryAssociation(
    name="applicationElement277",
    ends={
        Property(name="ecoreDiff_EObject279", type=ecoreDiff_ChangedEModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreDiff_ChangedEModelElement278", type=ecoreDiff_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecoreDiff_EClass_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_EClass)
gen_ecoreDiff_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_EAnnotation)
gen_ecoreDiff_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_ENamedElement)
gen_ecoreDiff_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EPackage)
gen_ecoreDiff_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_EFactory)
gen_ecoreDiff_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_EDataType)
gen_ecoreDiff_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ETypeParameter)
gen_ecoreDiff_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EClassifier)
gen_ecoreDiff_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EOperation)
gen_ecoreDiff_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ETypedElement)
gen_ecoreDiff_EGenericType_EObject = Generalization(general=EObject, specific=ecoreDiff_EGenericType)
gen_ecoreDiff_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EStructuralFeature)
gen_ecoreDiff_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_EReference)
gen_ecoreDiff_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_EParameter)
gen_ecoreDiff_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_EAttribute)
gen_ecoreDiff_EEnum_EDataType = Generalization(general=EDataType, specific=ecoreDiff_EEnum)
gen_ecoreDiff_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_EEnumLiteral)
gen_ecoreDiff_AddedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_AddedEAnnotation)
gen_ecoreDiff_DeletedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_DeletedEAnnotation)
gen_ecoreDiff_EModelElement_DifferenceElement = Generalization(general=DifferenceElement, specific=ecoreDiff_EModelElement)
gen_ecoreDiff_EModelElement_EObject = Generalization(general=EObject, specific=ecoreDiff_EModelElement)
gen_ecoreDiff_AddedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_AddedEObject)
gen_ecoreDiff_DeletedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_DeletedEObject)
gen_ecoreDiff_ChangedEObject_EObject = Generalization(general=EObject, specific=ecoreDiff_ChangedEObject)
gen_ecoreDiff_ChangedEAnnotation_EAnnotation = Generalization(general=EAnnotation, specific=ecoreDiff_ChangedEAnnotation)
gen_ecoreDiff_AddedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_AddedEStringToStringMapEntry)
gen_ecoreDiff_DeletedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_DeletedEStringToStringMapEntry)
gen_ecoreDiff_ChangedEStringToStringMapEntry_EStringToStringMapEntry = Generalization(general=EStringToStringMapEntry, specific=ecoreDiff_ChangedEStringToStringMapEntry)
gen_ecoreDiff_AddedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_AddedEClassifier)
gen_ecoreDiff_DeletedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_DeletedEClassifier)
gen_ecoreDiff_ChangedEClassifier_EClassifier = Generalization(general=EClassifier, specific=ecoreDiff_ChangedEClassifier)
gen_ecoreDiff_AddedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_AddedENamedElement)
gen_ecoreDiff_DeletedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_DeletedENamedElement)
gen_ecoreDiff_AddedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_AddedEClass)
gen_ecoreDiff_DeletedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_DeletedEClass)
gen_ecoreDiff_ChangedEClass_EClass = Generalization(general=EClass, specific=ecoreDiff_ChangedEClass)
gen_ecoreDiff_AddedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_AddedEFactory)
gen_ecoreDiff_DeletedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_DeletedEFactory)
gen_ecoreDiff_ChangedEFactory_EFactory = Generalization(general=EFactory, specific=ecoreDiff_ChangedEFactory)
gen_ecoreDiff_AddedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_AddedEDataType)
gen_ecoreDiff_DeletedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_DeletedEDataType)
gen_ecoreDiff_ChangedEDataType_EDataType = Generalization(general=EDataType, specific=ecoreDiff_ChangedEDataType)
gen_ecoreDiff_ChangedENamedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreDiff_ChangedENamedElement)
gen_ecoreDiff_AddedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_AddedEPackage)
gen_ecoreDiff_DeletedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_DeletedEPackage)
gen_ecoreDiff_ChangedEPackage_EPackage = Generalization(general=EPackage, specific=ecoreDiff_ChangedEPackage)
gen_ecoreDiff_AddedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_AddedEGenericType)
gen_ecoreDiff_DeletedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_DeletedEGenericType)
gen_ecoreDiff_ChangedEGenericType_EGenericType = Generalization(general=EGenericType, specific=ecoreDiff_ChangedEGenericType)
gen_ecoreDiff_AddedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_AddedEClassifier_Wildcard)
gen_ecoreDiff_DeletedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_DeletedEClassifier_Wildcard)
gen_ecoreDiff_AddedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_AddedETypeParameter)
gen_ecoreDiff_DeletedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_DeletedETypeParameter)
gen_ecoreDiff_ChangedETypeParameter_ETypeParameter = Generalization(general=ETypeParameter, specific=ecoreDiff_ChangedETypeParameter)
gen_ecoreDiff_DeletedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_DeletedEOperation)
gen_ecoreDiff_ChangedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_ChangedEOperation)
gen_ecoreDiff_AddedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_AddedETypedElement)
gen_ecoreDiff_DeletedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_DeletedETypedElement)
gen_ecoreDiff_ChangedEClassifier_Wildcard_EClassifier_Wildcard = Generalization(general=EClassifier_Wildcard, specific=ecoreDiff_ChangedEClassifier_Wildcard)
gen_ecoreDiff_AddedEOperation_EOperation = Generalization(general=EOperation, specific=ecoreDiff_AddedEOperation)
gen_ecoreDiff_DeletedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_DeletedEParameter)
gen_ecoreDiff_ChangedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_ChangedEParameter)
gen_ecoreDiff_AddedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_AddedEAttribute)
gen_ecoreDiff_DeletedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_DeletedEAttribute)
gen_ecoreDiff_ChangedETypedElement_ETypedElement = Generalization(general=ETypedElement, specific=ecoreDiff_ChangedETypedElement)
gen_ecoreDiff_AddedEParameter_EParameter = Generalization(general=EParameter, specific=ecoreDiff_AddedEParameter)
gen_ecoreDiff_ChangedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_ChangedEStructuralFeature)
gen_ecoreDiff_AddedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_AddedEStructuralFeature_Wildcard)
gen_ecoreDiff_DeletedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_DeletedEStructuralFeature_Wildcard)
gen_ecoreDiff_ChangedEAttribute_EAttribute = Generalization(general=EAttribute, specific=ecoreDiff_ChangedEAttribute)
gen_ecoreDiff_AddedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_AddedEStructuralFeature)
gen_ecoreDiff_DeletedEStructuralFeature_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreDiff_DeletedEStructuralFeature)
gen_ecoreDiff_DeletedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_DeletedEReference)
gen_ecoreDiff_ChangedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_ChangedEReference)
gen_ecoreDiff_ChangedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard = Generalization(general=EStructuralFeature_Wildcard, specific=ecoreDiff_ChangedEStructuralFeature_Wildcard)
gen_ecoreDiff_AddedEReference_EReference = Generalization(general=EReference, specific=ecoreDiff_AddedEReference)
gen_ecoreDiff_ChangedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_ChangedEEnum)
gen_ecoreDiff_AddedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_AddedEEnumLiteral)
gen_ecoreDiff_AddedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_AddedEEnum)
gen_ecoreDiff_DeletedEEnum_EEnum = Generalization(general=EEnum, specific=ecoreDiff_DeletedEEnum)
gen_ecoreDiff_AddedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_AddedEModelElement)
gen_ecoreDiff_DeletedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_DeletedEModelElement)
gen_ecoreDiff_ChangedEModelElement_EModelElement = Generalization(general=EModelElement, specific=ecoreDiff_ChangedEModelElement)
gen_ecoreDiff_DeletedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_DeletedEEnumLiteral)
gen_ecoreDiff_ChangedEEnumLiteral_EEnumLiteral = Generalization(general=EEnumLiteral, specific=ecoreDiff_ChangedEEnumLiteral)

# Domain Model
domain_model = DomainModel(
    name="ecoreDiff",
    types={ecoreDiff_EObject, ecoreDiff_EClass, EClassifier, ecoreDiff_EOperation, ecoreDiff_EStructuralFeature, ecoreDiff_EGenericType, ecoreDiff_EAnnotation, EModelElement, ecoreDiff_EStringToStringMapEntry, ecoreDiff_EModelElement, ecoreDiff_ENamedElement, ecoreDiff_EPackage, ecoreDiff_EFactory, ecoreDiff_EDataType, ecoreDiff_EClassifier, ENamedElement, ecoreDiff_ETypeParameter, ecoreDiff_EClassifier_Wildcard, ETypedElement, ecoreDiff_EParameter, ecoreDiff_ETypedElement, EObject, ecoreDiff_EStructuralFeature_Wildcard, ecoreDiff_EReference, ecoreDiff_EAttribute, EStructuralFeature, ecoreDiff_EEnum, EDataType, ecoreDiff_EEnumLiteral, ecoreDiff_AddedEAnnotation, EAnnotation, ecoreDiff_DeletedEAnnotation, DifferenceElement, ecoreDiff_DifferenceModel, ecoreDiff_DifferenceElement, ecoreDiff_AddedEObject, ecoreDiff_DeletedEObject, ecoreDiff_ChangedEObject, ecoreDiff_ChangedEAnnotation, ecoreDiff_AddedEStringToStringMapEntry, EStringToStringMapEntry, ecoreDiff_DeletedEStringToStringMapEntry, ecoreDiff_ChangedEStringToStringMapEntry, ecoreDiff_AddedEClassifier, ecoreDiff_DeletedEClassifier, ecoreDiff_ChangedEClassifier, ecoreDiff_AddedENamedElement, ecoreDiff_DeletedENamedElement, ecoreDiff_AddedEClass, EClass, ecoreDiff_DeletedEClass, ecoreDiff_ChangedEClass, ecoreDiff_AddedEFactory, EFactory, ecoreDiff_DeletedEFactory, ecoreDiff_ChangedEFactory, ecoreDiff_AddedEDataType, ecoreDiff_DeletedEDataType, ecoreDiff_ChangedEDataType, ecoreDiff_ChangedENamedElement, ecoreDiff_AddedEPackage, EPackage, ecoreDiff_DeletedEPackage, ecoreDiff_ChangedEPackage, ecoreDiff_AddedEGenericType, EGenericType, ecoreDiff_DeletedEGenericType, ecoreDiff_ChangedEGenericType, ecoreDiff_AddedEClassifier_Wildcard, EClassifier_Wildcard, ecoreDiff_DeletedEClassifier_Wildcard, ecoreDiff_AddedETypeParameter, ETypeParameter, ecoreDiff_DeletedETypeParameter, ecoreDiff_ChangedETypeParameter, ecoreDiff_DeletedEOperation, ecoreDiff_ChangedEOperation, ecoreDiff_AddedETypedElement, ecoreDiff_DeletedETypedElement, ecoreDiff_ChangedEClassifier_Wildcard, ecoreDiff_AddedEOperation, EOperation, ecoreDiff_DeletedEParameter, ecoreDiff_ChangedEParameter, ecoreDiff_AddedEAttribute, EAttribute, ecoreDiff_DeletedEAttribute, ecoreDiff_ChangedETypedElement, ecoreDiff_AddedEParameter, EParameter, ecoreDiff_ChangedEStructuralFeature, ecoreDiff_AddedEStructuralFeature_Wildcard, EStructuralFeature_Wildcard, ecoreDiff_DeletedEStructuralFeature_Wildcard, ecoreDiff_ChangedEAttribute, ecoreDiff_AddedEStructuralFeature, ecoreDiff_DeletedEStructuralFeature, ecoreDiff_DeletedEReference, ecoreDiff_ChangedEReference, ecoreDiff_ChangedEStructuralFeature_Wildcard, ecoreDiff_AddedEReference, EReference, ecoreDiff_ChangedEEnum, ecoreDiff_AddedEEnumLiteral, EEnumLiteral, ecoreDiff_AddedEEnum, EEnum, ecoreDiff_DeletedEEnum, ecoreDiff_AddedEModelElement, ecoreDiff_DeletedEModelElement, ecoreDiff_ChangedEModelElement, ecoreDiff_DeletedEEnumLiteral, ecoreDiff_ChangedEEnumLiteral},
    associations={contents3, references5, eSuperTypes9, eOperations10, eStructuralFeatures12, details0, eModelElement1, eFactoryInstance20, eSubpackages22, eSuperPackage25, eClassifiers27, ePackage30, eGenericSuperTypes14, ePackage16, eTypeParameters18, eTypeParameters51, eParameters54, eExceptions56, eGenericExceptions59, eContainingClass62, eBounds33, eUpperBound37, eTypeArguments40, eLowerBound43, eTypeParameter45, eClassifier48, eContainingClass73, eOpposite77, eKeys78, eType65, eGenericType67, eOperation70, eLiterals80, eEnum81, applicationElement88, eAnnotations84, updatedElement101, differenceElements87, applicationElement103, applicationElement106, applicationElement108, updatedElement110, applicationElement90, updatedElement92, applicationElement94, applicationElement97, applicationElement99, applicationElement121, applicationElement124, applicationElement126, updatedElement128, applicationElement130, applicationElement133, applicationElement135, applicationElement112, applicationElement115, applicationElement117, updatedElement119, applicationElement150, applicationElement152, updatedElement154, applicationElement156, applicationElement159, applicationElement161, updatedElement137, applicationElement138, applicationElement141, applicationElement143, updatedElement145, applicationElement147, applicationElement176, applicationElement178, updatedElement180, applicationElement182, applicationElement185, updatedElement163, applicationElement164, applicationElement167, applicationElement169, updatedElement171, applicationElement173, applicationElement195, updatedElement197, applicationElement199, applicationElement202, applicationElement204, applicationElement187, updatedElement189, applicationElement190, applicationElement193, applicationElement213, updatedElement215, applicationElement217, applicationElement220, applicationElement222, updatedElement206, applicationElement208, applicationElement211, updatedElement233, applicationElement235, applicationElement238, applicationElement240, updatedElement224, applicationElement226, applicationElement229, applicationElement231, applicationElement248, updatedElement250, updatedElement242, applicationElement243, applicationElement246, updatedElement259, applicationElement261, applicationElement252, applicationElement255, applicationElement257, updatedElement268, applicationElement270, applicationElement273, updatedElement275, applicationElement264, applicationElement266, applicationElement277},
    generalizations={gen_ecoreDiff_EClass_EClassifier, gen_ecoreDiff_EAnnotation_EModelElement, gen_ecoreDiff_ENamedElement_EModelElement, gen_ecoreDiff_EPackage_ENamedElement, gen_ecoreDiff_EFactory_EModelElement, gen_ecoreDiff_EDataType_EClassifier, gen_ecoreDiff_ETypeParameter_ENamedElement, gen_ecoreDiff_EClassifier_ENamedElement, gen_ecoreDiff_EOperation_ETypedElement, gen_ecoreDiff_ETypedElement_ENamedElement, gen_ecoreDiff_EGenericType_EObject, gen_ecoreDiff_EStructuralFeature_ETypedElement, gen_ecoreDiff_EReference_EStructuralFeature, gen_ecoreDiff_EParameter_ETypedElement, gen_ecoreDiff_EAttribute_EStructuralFeature, gen_ecoreDiff_EEnum_EDataType, gen_ecoreDiff_EEnumLiteral_ENamedElement, gen_ecoreDiff_AddedEAnnotation_EAnnotation, gen_ecoreDiff_DeletedEAnnotation_EAnnotation, gen_ecoreDiff_EModelElement_DifferenceElement, gen_ecoreDiff_EModelElement_EObject, gen_ecoreDiff_AddedEObject_EObject, gen_ecoreDiff_DeletedEObject_EObject, gen_ecoreDiff_ChangedEObject_EObject, gen_ecoreDiff_ChangedEAnnotation_EAnnotation, gen_ecoreDiff_AddedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_DeletedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_ChangedEStringToStringMapEntry_EStringToStringMapEntry, gen_ecoreDiff_AddedEClassifier_EClassifier, gen_ecoreDiff_DeletedEClassifier_EClassifier, gen_ecoreDiff_ChangedEClassifier_EClassifier, gen_ecoreDiff_AddedENamedElement_ENamedElement, gen_ecoreDiff_DeletedENamedElement_ENamedElement, gen_ecoreDiff_AddedEClass_EClass, gen_ecoreDiff_DeletedEClass_EClass, gen_ecoreDiff_ChangedEClass_EClass, gen_ecoreDiff_AddedEFactory_EFactory, gen_ecoreDiff_DeletedEFactory_EFactory, gen_ecoreDiff_ChangedEFactory_EFactory, gen_ecoreDiff_AddedEDataType_EDataType, gen_ecoreDiff_DeletedEDataType_EDataType, gen_ecoreDiff_ChangedEDataType_EDataType, gen_ecoreDiff_ChangedENamedElement_ENamedElement, gen_ecoreDiff_AddedEPackage_EPackage, gen_ecoreDiff_DeletedEPackage_EPackage, gen_ecoreDiff_ChangedEPackage_EPackage, gen_ecoreDiff_AddedEGenericType_EGenericType, gen_ecoreDiff_DeletedEGenericType_EGenericType, gen_ecoreDiff_ChangedEGenericType_EGenericType, gen_ecoreDiff_AddedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_DeletedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_AddedETypeParameter_ETypeParameter, gen_ecoreDiff_DeletedETypeParameter_ETypeParameter, gen_ecoreDiff_ChangedETypeParameter_ETypeParameter, gen_ecoreDiff_DeletedEOperation_EOperation, gen_ecoreDiff_ChangedEOperation_EOperation, gen_ecoreDiff_AddedETypedElement_ETypedElement, gen_ecoreDiff_DeletedETypedElement_ETypedElement, gen_ecoreDiff_ChangedEClassifier_Wildcard_EClassifier_Wildcard, gen_ecoreDiff_AddedEOperation_EOperation, gen_ecoreDiff_DeletedEParameter_EParameter, gen_ecoreDiff_ChangedEParameter_EParameter, gen_ecoreDiff_AddedEAttribute_EAttribute, gen_ecoreDiff_DeletedEAttribute_EAttribute, gen_ecoreDiff_ChangedETypedElement_ETypedElement, gen_ecoreDiff_AddedEParameter_EParameter, gen_ecoreDiff_ChangedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_AddedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_DeletedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_ChangedEAttribute_EAttribute, gen_ecoreDiff_AddedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_DeletedEStructuralFeature_EStructuralFeature, gen_ecoreDiff_DeletedEReference_EReference, gen_ecoreDiff_ChangedEReference_EReference, gen_ecoreDiff_ChangedEStructuralFeature_Wildcard_EStructuralFeature_Wildcard, gen_ecoreDiff_AddedEReference_EReference, gen_ecoreDiff_ChangedEEnum_EEnum, gen_ecoreDiff_AddedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_AddedEEnum_EEnum, gen_ecoreDiff_DeletedEEnum_EEnum, gen_ecoreDiff_AddedEModelElement_EModelElement, gen_ecoreDiff_DeletedEModelElement_EModelElement, gen_ecoreDiff_ChangedEModelElement_EModelElement, gen_ecoreDiff_DeletedEEnumLiteral_EEnumLiteral, gen_ecoreDiff_ChangedEEnumLiteral_EEnumLiteral},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)