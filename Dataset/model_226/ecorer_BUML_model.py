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
ecorer_EDataType = Class(name="ecorer::EDataType")
ecorer_EAnnotation = Class(name="ecorer::EAnnotation")
EModelElement = Class(name="EModelElement")
ecorer_EStringToStringMapEntry = Class(name="ecorer::EStringToStringMapEntry")
ecorer_EModelElement = Class(name="ecorer::EModelElement", is_abstract=True)
ecorer_EObject = Class(name="ecorer::EObject")
ecorer_EAttribute = Class(name="ecorer::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
ecorer_EClass = Class(name="ecorer::EClass")
EClassifier = Class(name="EClassifier")
ecorer_EOperation = Class(name="ecorer::EOperation")
ecorer_EReference = Class(name="ecorer::EReference")
ecorer_EStructuralFeature = Class(name="ecorer::EStructuralFeature", is_abstract=True)
ecorer_EGenericType = Class(name="ecorer::EGenericType")
ecorer_EPackage = Class(name="ecorer::EPackage")
ecorer_EClassifier = Class(name="ecorer::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecorer_EEnum = Class(name="ecorer::EEnum")
EDataType = Class(name="EDataType")
ecorer_EEnumLiteral = Class(name="ecorer::EEnumLiteral")
ecorer_ETypeParameter = Class(name="ecorer::ETypeParameter")
ecorer_ENamedElement = Class(name="ecorer::ENamedElement", is_abstract=True)
ecorer_EFactory = Class(name="ecorer::EFactory")
ecorer_EParameter = Class(name="ecorer::EParameter")
ETypedElement = Class(name="ETypedElement")
ecorer_ETypedElement = Class(name="ecorer::ETypedElement", is_abstract=True)

# ecorer_EDataType class attributes and methods
ecorer_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecorer_EDataType.attributes={ecorer_EDataType_serializable}

# ecorer_EAnnotation class attributes and methods
ecorer_EAnnotation_source: Property = Property(name="source", type=StringType)
ecorer_EAnnotation.attributes={ecorer_EAnnotation_source}

# EModelElement class attributes and methods

# ecorer_EStringToStringMapEntry class attributes and methods
ecorer_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecorer_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecorer_EStringToStringMapEntry.attributes={ecorer_EStringToStringMapEntry_key, ecorer_EStringToStringMapEntry_value}

# ecorer_EModelElement class attributes and methods
ecorer_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecorer_EModelElement.methods={ecorer_EModelElement_m_getEAnnotation}

# ecorer_EObject class attributes and methods
ecorer_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecorer_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecorer_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecorer_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecorer_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
ecorer_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecorer_EObject_m_eContents: Method = Method(name="eContents", parameters={})
ecorer_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
ecorer_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
ecorer_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecorer_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecorer_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='feature'), Parameter(name='newValue')})
ecorer_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='arguments'), Parameter(name='operation')}, type=StringType)
ecorer_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecorer_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecorer_EObject.methods={ecorer_EObject_m_eContents, ecorer_EObject_m_eInvoke, ecorer_EObject_m_eClass, ecorer_EObject_m_eContainmentFeature, ecorer_EObject_m_eAllContents, ecorer_EObject_m_eCrossReferences, ecorer_EObject_m_eResource, ecorer_EObject_m_eContainer, ecorer_EObject_m_eGet, ecorer_EObject_m_eSet, ecorer_EObject_m_eContainingFeature, ecorer_EObject_m_eIsSet, ecorer_EObject_m_eUnset, ecorer_EObject_m_eIsProxy, ecorer_EObject_m_eGet}

# ecorer_EAttribute class attributes and methods
ecorer_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecorer_EAttribute.attributes={ecorer_EAttribute_iD}

# EStructuralFeature class attributes and methods

# ecorer_EClass class attributes and methods
ecorer_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecorer_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecorer_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecorer_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecorer_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecorer_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecorer_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecorer_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=IntegerType)
ecorer_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
ecorer_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=IntegerType)
ecorer_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
ecorer_EClass.attributes={ecorer_EClass_abstract, ecorer_EClass_interface}
ecorer_EClass.methods={ecorer_EClass_m_getFeatureCount, ecorer_EClass_m_getEOperation, ecorer_EClass_m_getOverride, ecorer_EClass_m_getOperationID, ecorer_EClass_m_getEStructuralFeature, ecorer_EClass_m_getEStructuralFeature, ecorer_EClass_m_isSuperTypeOf, ecorer_EClass_m_getOperationCount, ecorer_EClass_m_getFeatureID}

# EClassifier class attributes and methods

# ecorer_EOperation class attributes and methods
ecorer_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=BooleanType)
ecorer_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=IntegerType)
ecorer_EOperation.methods={ecorer_EOperation_m_getOperationID, ecorer_EOperation_m_isOverrideOf}

# ecorer_EReference class attributes and methods
ecorer_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecorer_EReference_container: Property = Property(name="container", type=BooleanType)
ecorer_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecorer_EReference.attributes={ecorer_EReference_containment, ecorer_EReference_container, ecorer_EReference_resolveProxies}

# ecorer_EStructuralFeature class attributes and methods
ecorer_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecorer_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecorer_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecorer_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecorer_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecorer_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecorer_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecorer_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecorer_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecorer_EStructuralFeature.attributes={ecorer_EStructuralFeature_transient, ecorer_EStructuralFeature_unsettable, ecorer_EStructuralFeature_volatile, ecorer_EStructuralFeature_derived, ecorer_EStructuralFeature_defaultValue, ecorer_EStructuralFeature_defaultValueLiteral, ecorer_EStructuralFeature_changeable}
ecorer_EStructuralFeature.methods={ecorer_EStructuralFeature_m_getContainerClass, ecorer_EStructuralFeature_m_getFeatureID}

# ecorer_EGenericType class attributes and methods

# ecorer_EPackage class attributes and methods
ecorer_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecorer_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecorer_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecorer_EPackage.attributes={ecorer_EPackage_nsURI, ecorer_EPackage_nsPrefix}
ecorer_EPackage.methods={ecorer_EPackage_m_getEClassifier}

# ecorer_EClassifier class attributes and methods
ecorer_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecorer_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecorer_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecorer_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecorer_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecorer_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecorer_EClassifier.attributes={ecorer_EClassifier_instanceTypeName, ecorer_EClassifier_defaultValue, ecorer_EClassifier_instanceClass, ecorer_EClassifier_instanceClassName}
ecorer_EClassifier.methods={ecorer_EClassifier_m_getClassifierID, ecorer_EClassifier_m_isInstance}

# ENamedElement class attributes and methods

# ecorer_EEnum class attributes and methods
ecorer_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecorer_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecorer_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecorer_EEnum.methods={ecorer_EEnum_m_getEEnumLiteral, ecorer_EEnum_m_getEEnumLiteralByLiteral, ecorer_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# ecorer_EEnumLiteral class attributes and methods
ecorer_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecorer_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecorer_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecorer_EEnumLiteral.attributes={ecorer_EEnumLiteral_instance, ecorer_EEnumLiteral_value, ecorer_EEnumLiteral_literal}

# ecorer_ETypeParameter class attributes and methods

# ecorer_ENamedElement class attributes and methods
ecorer_ENamedElement_name: Property = Property(name="name", type=StringType)
ecorer_ENamedElement.attributes={ecorer_ENamedElement_name}

# ecorer_EFactory class attributes and methods
ecorer_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecorer_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='eDataType'), Parameter(name='instanceValue')}, type=StringType)
ecorer_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecorer_EFactory.methods={ecorer_EFactory_m_convertToString, ecorer_EFactory_m_createFromString, ecorer_EFactory_m_create}

# ecorer_EParameter class attributes and methods

# ETypedElement class attributes and methods

# ecorer_ETypedElement class attributes and methods
ecorer_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecorer_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecorer_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecorer_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecorer_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecorer_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecorer_ETypedElement.attributes={ecorer_ETypedElement_unique, ecorer_ETypedElement_many, ecorer_ETypedElement_upperBound, ecorer_ETypedElement_required, ecorer_ETypedElement_lowerBound, ecorer_ETypedElement_ordered}

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecorer_EDataType", type=ecorer_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EAttribute", type=ecorer_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="ecorer_EStringToStringMapEntry", type=ecorer_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EAnnotation", type=ecorer_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="EModelElement", type=ecorer_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecorer_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="ecorer_EObject", type=ecorer_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EAnnotation4", type=ecorer_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="ecorer_EObject7", type=ecorer_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EAnnotation6", type=ecorer_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="EOperation", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecorer_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes11: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes11",
    ends={
        Property(name="ecorer_EAttribute13", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass12", type=ecorer_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="ecorer_EReference", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass15", type=ecorer_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="ecorer_EReference18", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass17", type=ecorer_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="ecorer_EAttribute21", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass20", type=ecorer_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="ecorer_EClass", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass8", type=ecorer_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="ecorer_EStructuralFeature", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass28", type=ecorer_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="ecorer_EClass31", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass29", type=ecorer_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="ecorer_EAttribute34", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass33", type=ecorer_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="EStructuralFeature", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass36", type=ecorer_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes37",
    ends={
        Property(name="ecorer_EGenericType", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass38", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="ecorer_EReference24", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass23", type=ecorer_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="ecorer_EOperation", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass26", type=ecorer_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage42: BinaryAssociation = BinaryAssociation(
    name="ePackage42",
    ends={
        Property(name="EPackage", type=ecorer_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecorer_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eAllGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes39",
    ends={
        Property(name="ecorer_EGenericType41", type=ecorer_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClass40", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eLiterals44: BinaryAssociation = BinaryAssociation(
    name="eLiterals44",
    ends={
        Property(name="EEnumLiteral", type=ecorer_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecorer_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeParameters43: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters43",
    ends={
        Property(name="ecorer_ETypeParameter", type=ecorer_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EClassifier", type=ecorer_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage47", type=ecorer_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecorer_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations48: BinaryAssociation = BinaryAssociation(
    name="eAnnotations48",
    ends={
        Property(name="EAnnotation", type=ecorer_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecorer_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum45: BinaryAssociation = BinaryAssociation(
    name="eEnum45",
    ends={
        Property(name="EEnum", type=ecorer_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecorer_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass49: BinaryAssociation = BinaryAssociation(
    name="eContainingClass49",
    ends={
        Property(name="EClass", type=ecorer_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecorer_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters50: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters50",
    ends={
        Property(name="ecorer_ETypeParameter52", type=ecorer_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EOperation51", type=ecorer_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters53: BinaryAssociation = BinaryAssociation(
    name="eParameters53",
    ends={
        Property(name="EParameter", type=ecorer_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecorer_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions54: BinaryAssociation = BinaryAssociation(
    name="eExceptions54",
    ends={
        Property(name="ecorer_EClassifier56", type=ecorer_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EOperation55", type=ecorer_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions57: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions57",
    ends={
        Property(name="ecorer_EGenericType59", type=ecorer_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EOperation58", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance60: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance60",
    ends={
        Property(name="EFactory", type=ecorer_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecorer_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eSuperPackage67: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage67",
    ends={
        Property(name="EPackage68", type=ecorer_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecorer_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation69: BinaryAssociation = BinaryAssociation(
    name="eOperation69",
    ends={
        Property(name="EOperation70", type=ecorer_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecorer_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite72: BinaryAssociation = BinaryAssociation(
    name="eOpposite72",
    ends={
        Property(name="ecorer_EReference73", type=ecorer_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EReference71", type=ecorer_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eClassifiers61: BinaryAssociation = BinaryAssociation(
    name="eClassifiers61",
    ends={
        Property(name="EClassifier", type=ecorer_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage62", type=ecorer_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages64: BinaryAssociation = BinaryAssociation(
    name="eSubpackages64",
    ends={
        Property(name="EPackage65", type=ecorer_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecorer_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass80: BinaryAssociation = BinaryAssociation(
    name="eContainingClass80",
    ends={
        Property(name="EClass81", type=ecorer_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecorer_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType74: BinaryAssociation = BinaryAssociation(
    name="eReferenceType74",
    ends={
        Property(name="ecorer_EClass76", type=ecorer_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EReference75", type=ecorer_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys77: BinaryAssociation = BinaryAssociation(
    name="eKeys77",
    ends={
        Property(name="ecorer_EAttribute79", type=ecorer_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EReference78", type=ecorer_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eType82: BinaryAssociation = BinaryAssociation(
    name="eType82",
    ends={
        Property(name="ecorer_EClassifier83", type=ecorer_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_ETypedElement", type=ecorer_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType84: BinaryAssociation = BinaryAssociation(
    name="eGenericType84",
    ends={
        Property(name="ecorer_EGenericType86", type=ecorer_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_ETypedElement85", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eUpperBound88: BinaryAssociation = BinaryAssociation(
    name="eUpperBound88",
    ends={
        Property(name="ecorer_EGenericType89", type=ecorer_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EGenericType87", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments91: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments91",
    ends={
        Property(name="ecorer_EGenericType92", type=ecorer_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EGenericType90", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType93: BinaryAssociation = BinaryAssociation(
    name="eRawType93",
    ends={
        Property(name="ecorer_EClassifier95", type=ecorer_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EGenericType94", type=ecorer_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound97: BinaryAssociation = BinaryAssociation(
    name="eLowerBound97",
    ends={
        Property(name="ecorer_EGenericType98", type=ecorer_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EGenericType96", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eClassifier102: BinaryAssociation = BinaryAssociation(
    name="eClassifier102",
    ends={
        Property(name="ecorer_EClassifier104", type=ecorer_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EGenericType103", type=ecorer_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds105: BinaryAssociation = BinaryAssociation(
    name="eBounds105",
    ends={
        Property(name="ecorer_EGenericType107", type=ecorer_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_ETypeParameter106", type=ecorer_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeParameter99: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter99",
    ends={
        Property(name="ecorer_ETypeParameter101", type=ecorer_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecorer_EGenericType100", type=ecorer_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecorer_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecorer_EAnnotation)
gen_ecorer_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecorer_EAttribute)
gen_ecorer_EClass_EClassifier = Generalization(general=EClassifier, specific=ecorer_EClass)
gen_ecorer_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecorer_EClassifier)
gen_ecorer_EEnum_EDataType = Generalization(general=EDataType, specific=ecorer_EEnum)
gen_ecorer_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecorer_EEnumLiteral)
gen_ecorer_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecorer_EDataType)
gen_ecorer_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecorer_ENamedElement)
gen_ecorer_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecorer_EFactory)
gen_ecorer_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecorer_EOperation)
gen_ecorer_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecorer_EPackage)
gen_ecorer_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecorer_EParameter)
gen_ecorer_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecorer_EReference)
gen_ecorer_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecorer_ETypedElement)
gen_ecorer_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecorer_EStructuralFeature)
gen_ecorer_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecorer_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecorer",
    types={ecorer_EDataType, ecorer_EAnnotation, EModelElement, ecorer_EStringToStringMapEntry, ecorer_EModelElement, ecorer_EObject, ecorer_EAttribute, EStructuralFeature, ecorer_EClass, EClassifier, ecorer_EOperation, ecorer_EReference, ecorer_EStructuralFeature, ecorer_EGenericType, ecorer_EPackage, ecorer_EClassifier, ENamedElement, ecorer_EEnum, EDataType, ecorer_EEnumLiteral, ecorer_ETypeParameter, ecorer_ENamedElement, ecorer_EFactory, ecorer_EParameter, ETypedElement, ecorer_ETypedElement},
    associations={eAttributeType0, details1, eModelElement2, contents3, references5, eOperations10, eAllAttributes11, eAllReferences14, eReferences16, eAttributes19, eSuperTypes9, eAllStructuralFeatures27, eAllSuperTypes30, eIDAttribute32, eStructuralFeatures35, eGenericSuperTypes37, eAllContainments22, eAllOperations25, ePackage42, eAllGenericSuperTypes39, eLiterals44, eTypeParameters43, ePackage46, eAnnotations48, eEnum45, eContainingClass49, eTypeParameters50, eParameters53, eExceptions54, eGenericExceptions57, eFactoryInstance60, eSuperPackage67, eOperation69, eOpposite72, eClassifiers61, eSubpackages64, eContainingClass80, eReferenceType74, eKeys77, eType82, eGenericType84, eUpperBound88, eTypeArguments91, eRawType93, eLowerBound97, eClassifier102, eBounds105, eTypeParameter99},
    generalizations={gen_ecorer_EAnnotation_EModelElement, gen_ecorer_EAttribute_EStructuralFeature, gen_ecorer_EClass_EClassifier, gen_ecorer_EClassifier_ENamedElement, gen_ecorer_EEnum_EDataType, gen_ecorer_EEnumLiteral_ENamedElement, gen_ecorer_EDataType_EClassifier, gen_ecorer_ENamedElement_EModelElement, gen_ecorer_EFactory_EModelElement, gen_ecorer_EOperation_ETypedElement, gen_ecorer_EPackage_ENamedElement, gen_ecorer_EParameter_ETypedElement, gen_ecorer_EReference_EStructuralFeature, gen_ecorer_ETypedElement_ENamedElement, gen_ecorer_EStructuralFeature_ETypedElement, gen_ecorer_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)