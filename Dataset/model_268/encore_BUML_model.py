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
EStructuralFeature = Class(name="EStructuralFeature")
encore_EDataType = Class(name="encore::EDataType")
encore_EAnnotation = Class(name="encore::EAnnotation")
EModelElement = Class(name="EModelElement")
encore_EStringToStringMapEntry = Class(name="encore::EStringToStringMapEntry")
encore_EModelElement = Class(name="encore::EModelElement", is_abstract=True)
encore_EObject = Class(name="encore::EObject")
encore_EAttribute = Class(name="encore::EAttribute")
encore_EClass = Class(name="encore::EClass")
EClassifier = Class(name="EClassifier")
encore_EReference = Class(name="encore::EReference")
encore_EOperation = Class(name="encore::EOperation")
encore_EGenericType = Class(name="encore::EGenericType")
encore_EClassifier = Class(name="encore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
encore_EStructuralFeature = Class(name="encore::EStructuralFeature", is_abstract=True)
encore_EPackage = Class(name="encore::EPackage")
encore_ETypeParameter = Class(name="encore::ETypeParameter")
encore_EEnum = Class(name="encore::EEnum")
EDataType = Class(name="EDataType")
encore_EFactory = Class(name="encore::EFactory")
encore_EEnumLiteral = Class(name="encore::EEnumLiteral")
encore_ENamedElement = Class(name="encore::ENamedElement", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
encore_EParameter = Class(name="encore::EParameter")
encore_ETypedElement = Class(name="encore::ETypedElement", is_abstract=True)

# EStructuralFeature class attributes and methods

# encore_EDataType class attributes and methods
encore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
encore_EDataType.attributes={encore_EDataType_serializable}

# encore_EAnnotation class attributes and methods
encore_EAnnotation_source: Property = Property(name="source", type=StringType)
encore_EAnnotation.attributes={encore_EAnnotation_source}

# EModelElement class attributes and methods

# encore_EStringToStringMapEntry class attributes and methods
encore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
encore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
encore_EStringToStringMapEntry.attributes={encore_EStringToStringMapEntry_value, encore_EStringToStringMapEntry_key}

# encore_EModelElement class attributes and methods
encore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
encore_EModelElement.methods={encore_EModelElement_m_getEAnnotation}

# encore_EObject class attributes and methods
encore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
encore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
encore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
encore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
encore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
encore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
encore_EObject_m_eContents: Method = Method(name="eContents", parameters={})
encore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
encore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
encore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
encore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
encore_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='arguments'), Parameter(name='operation')}, type=StringType)
encore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
encore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
encore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='resolve'), Parameter(name='feature')}, type=StringType)
encore_EObject.methods={encore_EObject_m_eAllContents, encore_EObject_m_eInvoke, encore_EObject_m_eIsSet, encore_EObject_m_eCrossReferences, encore_EObject_m_eIsProxy, encore_EObject_m_eContainmentFeature, encore_EObject_m_eGet, encore_EObject_m_eGet, encore_EObject_m_eContainingFeature, encore_EObject_m_eSet, encore_EObject_m_eResource, encore_EObject_m_eContents, encore_EObject_m_eClass, encore_EObject_m_eContainer, encore_EObject_m_eUnset}

# encore_EAttribute class attributes and methods
encore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
encore_EAttribute.attributes={encore_EAttribute_iD}

# encore_EClass class attributes and methods
encore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
encore_EClass_interface: Property = Property(name="interface", type=BooleanType)
encore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
encore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
encore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
encore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
encore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
encore_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=IntegerType)
encore_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
encore_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=IntegerType)
encore_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
encore_EClass.attributes={encore_EClass_interface, encore_EClass_abstract}
encore_EClass.methods={encore_EClass_m_getFeatureCount, encore_EClass_m_getEOperation, encore_EClass_m_getEStructuralFeature, encore_EClass_m_getEStructuralFeature, encore_EClass_m_getOperationID, encore_EClass_m_getFeatureID, encore_EClass_m_getOverride, encore_EClass_m_getOperationCount, encore_EClass_m_isSuperTypeOf}

# EClassifier class attributes and methods

# encore_EReference class attributes and methods
encore_EReference_containment: Property = Property(name="containment", type=BooleanType)
encore_EReference_container: Property = Property(name="container", type=BooleanType)
encore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
encore_EReference.attributes={encore_EReference_container, encore_EReference_resolveProxies, encore_EReference_containment}

# encore_EOperation class attributes and methods
encore_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=IntegerType)
encore_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=BooleanType)
encore_EOperation.methods={encore_EOperation_m_getOperationID, encore_EOperation_m_isOverrideOf}

# encore_EGenericType class attributes and methods

# encore_EClassifier class attributes and methods
encore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
encore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
encore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
encore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
encore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
encore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
encore_EClassifier.attributes={encore_EClassifier_instanceClass, encore_EClassifier_instanceTypeName, encore_EClassifier_defaultValue, encore_EClassifier_instanceClassName}
encore_EClassifier.methods={encore_EClassifier_m_isInstance, encore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# encore_EStructuralFeature class attributes and methods
encore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
encore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
encore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
encore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
encore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
encore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
encore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
encore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
encore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
encore_EStructuralFeature.attributes={encore_EStructuralFeature_changeable, encore_EStructuralFeature_defaultValueLiteral, encore_EStructuralFeature_derived, encore_EStructuralFeature_transient, encore_EStructuralFeature_volatile, encore_EStructuralFeature_defaultValue, encore_EStructuralFeature_unsettable}
encore_EStructuralFeature.methods={encore_EStructuralFeature_m_getContainerClass, encore_EStructuralFeature_m_getFeatureID}

# encore_EPackage class attributes and methods
encore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
encore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
encore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
encore_EPackage.attributes={encore_EPackage_nsURI, encore_EPackage_nsPrefix}
encore_EPackage.methods={encore_EPackage_m_getEClassifier}

# encore_ETypeParameter class attributes and methods

# encore_EEnum class attributes and methods
encore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
encore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
encore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
encore_EEnum.methods={encore_EEnum_m_getEEnumLiteral, encore_EEnum_m_getEEnumLiteralByLiteral, encore_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# encore_EFactory class attributes and methods
encore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
encore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
encore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
encore_EFactory.methods={encore_EFactory_m_convertToString, encore_EFactory_m_create, encore_EFactory_m_createFromString}

# encore_EEnumLiteral class attributes and methods
encore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
encore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
encore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
encore_EEnumLiteral.attributes={encore_EEnumLiteral_literal, encore_EEnumLiteral_instance, encore_EEnumLiteral_value}

# encore_ENamedElement class attributes and methods
encore_ENamedElement_name: Property = Property(name="name", type=StringType)
encore_ENamedElement.attributes={encore_ENamedElement_name}

# ETypedElement class attributes and methods

# encore_EParameter class attributes and methods

# encore_ETypedElement class attributes and methods
encore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
encore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
encore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
encore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
encore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
encore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
encore_ETypedElement.attributes={encore_ETypedElement_unique, encore_ETypedElement_lowerBound, encore_ETypedElement_upperBound, encore_ETypedElement_required, encore_ETypedElement_ordered, encore_ETypedElement_many}

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="encore_EDataType", type=encore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EAttribute", type=encore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="encore_EStringToStringMapEntry", type=encore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EAnnotation", type=encore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="EModelElement", type=encore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=encore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="encore_EObject", type=encore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EAnnotation4", type=encore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="encore_EObject7", type=encore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EAnnotation6", type=encore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAllAttributes11: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes11",
    ends={
        Property(name="encore_EAttribute13", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass12", type=encore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="encore_EReference", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass15", type=encore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="encore_EReference18", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass17", type=encore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="encore_EAttribute21", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass20", type=encore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="encore_EReference24", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass23", type=encore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="encore_EOperation", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass26", type=encore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="encore_EClass", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass8", type=encore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="EOperation", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=encore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="encore_EAttribute34", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass33", type=encore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="EStructuralFeature", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass36", type=encore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes37",
    ends={
        Property(name="encore_EGenericType", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass38", type=encore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes39",
    ends={
        Property(name="encore_EGenericType41", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass40", type=encore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="encore_EStructuralFeature", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass28", type=encore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="encore_EClass31", type=encore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClass29", type=encore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage42: BinaryAssociation = BinaryAssociation(
    name="ePackage42",
    ends={
        Property(name="encore_EPackage", type=encore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClassifier", type=encore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters43: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters43",
    ends={
        Property(name="encore_ETypeParameter", type=encore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EClassifier44", type=encore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum46: BinaryAssociation = BinaryAssociation(
    name="eEnum46",
    ends={
        Property(name="EEnum", type=encore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=encore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
ePackage47: BinaryAssociation = BinaryAssociation(
    name="ePackage47",
    ends={
        Property(name="EPackage", type=encore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=encore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eLiterals45: BinaryAssociation = BinaryAssociation(
    name="eLiterals45",
    ends={
        Property(name="EEnumLiteral", type=encore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=encore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAnnotations48: BinaryAssociation = BinaryAssociation(
    name="eAnnotations48",
    ends={
        Property(name="EAnnotation", type=encore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=encore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters53: BinaryAssociation = BinaryAssociation(
    name="eParameters53",
    ends={
        Property(name="eOperation", type=encore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="EParameter", type=encore_EOperation, multiplicity=Multiplicity(1, 1))
    }
)
eExceptions54: BinaryAssociation = BinaryAssociation(
    name="eExceptions54",
    ends={
        Property(name="encore_EClassifier56", type=encore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EOperation55", type=encore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions57: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions57",
    ends={
        Property(name="encore_EGenericType59", type=encore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EOperation58", type=encore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass49: BinaryAssociation = BinaryAssociation(
    name="eContainingClass49",
    ends={
        Property(name="EClass", type=encore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=encore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters50: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters50",
    ends={
        Property(name="encore_ETypeParameter52", type=encore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EOperation51", type=encore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages65: BinaryAssociation = BinaryAssociation(
    name="eSubpackages65",
    ends={
        Property(name="encore_EPackage66", type=encore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EPackage64", type=encore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage68: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage68",
    ends={
        Property(name="encore_EPackage69", type=encore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EPackage67", type=encore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eFactoryInstance60: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance60",
    ends={
        Property(name="EFactory", type=encore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=encore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers61: BinaryAssociation = BinaryAssociation(
    name="eClassifiers61",
    ends={
        Property(name="encore_EClassifier63", type=encore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EPackage62", type=encore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eOpposite73: BinaryAssociation = BinaryAssociation(
    name="eOpposite73",
    ends={
        Property(name="encore_EReference74", type=encore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EReference72", type=encore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType75: BinaryAssociation = BinaryAssociation(
    name="eReferenceType75",
    ends={
        Property(name="encore_EClass77", type=encore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EReference76", type=encore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys78: BinaryAssociation = BinaryAssociation(
    name="eKeys78",
    ends={
        Property(name="encore_EAttribute80", type=encore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EReference79", type=encore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eContainingClass81: BinaryAssociation = BinaryAssociation(
    name="eContainingClass81",
    ends={
        Property(name="EClass82", type=encore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=encore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOperation70: BinaryAssociation = BinaryAssociation(
    name="eOperation70",
    ends={
        Property(name="EOperation71", type=encore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=encore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType85: BinaryAssociation = BinaryAssociation(
    name="eGenericType85",
    ends={
        Property(name="encore_EGenericType87", type=encore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_ETypedElement86", type=encore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eType83: BinaryAssociation = BinaryAssociation(
    name="eType83",
    ends={
        Property(name="encore_EClassifier84", type=encore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_ETypedElement", type=encore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eUpperBound89: BinaryAssociation = BinaryAssociation(
    name="eUpperBound89",
    ends={
        Property(name="encore_EGenericType90", type=encore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EGenericType88", type=encore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eLowerBound98: BinaryAssociation = BinaryAssociation(
    name="eLowerBound98",
    ends={
        Property(name="encore_EGenericType99", type=encore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EGenericType97", type=encore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter100: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter100",
    ends={
        Property(name="encore_ETypeParameter102", type=encore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EGenericType101", type=encore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier103: BinaryAssociation = BinaryAssociation(
    name="eClassifier103",
    ends={
        Property(name="encore_EClassifier105", type=encore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EGenericType104", type=encore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds106: BinaryAssociation = BinaryAssociation(
    name="eBounds106",
    ends={
        Property(name="encore_EGenericType108", type=encore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_ETypeParameter107", type=encore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeArguments92: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments92",
    ends={
        Property(name="encore_EGenericType93", type=encore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EGenericType91", type=encore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType94: BinaryAssociation = BinaryAssociation(
    name="eRawType94",
    ends={
        Property(name="encore_EClassifier96", type=encore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="encore_EGenericType95", type=encore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_encore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=encore_EAttribute)
gen_encore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=encore_EAnnotation)
gen_encore_EClass_EClassifier = Generalization(general=EClassifier, specific=encore_EClass)
gen_encore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=encore_EClassifier)
gen_encore_EDataType_EClassifier = Generalization(general=EClassifier, specific=encore_EDataType)
gen_encore_EEnum_EDataType = Generalization(general=EDataType, specific=encore_EEnum)
gen_encore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=encore_EEnumLiteral)
gen_encore_EFactory_EModelElement = Generalization(general=EModelElement, specific=encore_EFactory)
gen_encore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=encore_ENamedElement)
gen_encore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=encore_EOperation)
gen_encore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=encore_EPackage)
gen_encore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=encore_EParameter)
gen_encore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=encore_EStructuralFeature)
gen_encore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=encore_ETypedElement)
gen_encore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=encore_EReference)
gen_encore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=encore_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="encore",
    types={EStructuralFeature, encore_EDataType, encore_EAnnotation, EModelElement, encore_EStringToStringMapEntry, encore_EModelElement, encore_EObject, encore_EAttribute, encore_EClass, EClassifier, encore_EReference, encore_EOperation, encore_EGenericType, encore_EClassifier, ENamedElement, encore_EStructuralFeature, encore_EPackage, encore_ETypeParameter, encore_EEnum, EDataType, encore_EFactory, encore_EEnumLiteral, encore_ENamedElement, ETypedElement, encore_EParameter, encore_ETypedElement},
    associations={eAttributeType0, details1, eModelElement2, contents3, references5, eAllAttributes11, eAllReferences14, eReferences16, eAttributes19, eAllContainments22, eAllOperations25, eSuperTypes9, eOperations10, eIDAttribute32, eStructuralFeatures35, eGenericSuperTypes37, eAllGenericSuperTypes39, eAllStructuralFeatures27, eAllSuperTypes30, ePackage42, eTypeParameters43, eEnum46, ePackage47, eLiterals45, eAnnotations48, eParameters53, eExceptions54, eGenericExceptions57, eContainingClass49, eTypeParameters50, eSubpackages65, eSuperPackage68, eFactoryInstance60, eClassifiers61, eOpposite73, eReferenceType75, eKeys78, eContainingClass81, eOperation70, eGenericType85, eType83, eUpperBound89, eLowerBound98, eTypeParameter100, eClassifier103, eBounds106, eTypeArguments92, eRawType94},
    generalizations={gen_encore_EAttribute_EStructuralFeature, gen_encore_EAnnotation_EModelElement, gen_encore_EClass_EClassifier, gen_encore_EClassifier_ENamedElement, gen_encore_EDataType_EClassifier, gen_encore_EEnum_EDataType, gen_encore_EEnumLiteral_ENamedElement, gen_encore_EFactory_EModelElement, gen_encore_ENamedElement_EModelElement, gen_encore_EOperation_ETypedElement, gen_encore_EPackage_ENamedElement, gen_encore_EParameter_ETypedElement, gen_encore_EStructuralFeature_ETypedElement, gen_encore_ETypedElement_ENamedElement, gen_encore_EReference_EStructuralFeature, gen_encore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)