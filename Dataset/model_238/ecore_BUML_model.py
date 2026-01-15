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
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
ecore_EAttribute = Class(name="ecore::EAttribute")
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
ecore_EObject = Class(name="ecore::EObject")
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EReference = Class(name="ecore::EReference")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_EParameter = Class(name="ecore::EParameter")
ETypedElement = Class(name="ETypedElement")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)

# EStructuralFeature class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_key, ecore_EStringToStringMapEntry_value}

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# ecore_EObject class attributes and methods
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={})
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='arguments'), Parameter(name='operation')}, type=StringType)
ecore_EObject.methods={ecore_EObject_m_eContainer, ecore_EObject_m_eClass, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eGet, ecore_EObject_m_eIsSet, ecore_EObject_m_eSet, ecore_EObject_m_eUnset, ecore_EObject_m_eContents, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eGet, ecore_EObject_m_eInvoke, ecore_EObject_m_eAllContents, ecore_EObject_m_eIsProxy, ecore_EObject_m_eResource}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
ecore_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=IntegerType)
ecore_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
ecore_EClass_m_getFeatureType: Method = Method(name="getFeatureType", parameters={Parameter(name='feature')}, type=StringType)
ecore_EClass.attributes={ecore_EClass_interface, ecore_EClass_abstract}
ecore_EClass.methods={ecore_EClass_m_getEOperation, ecore_EClass_m_getOperationID, ecore_EClass_m_getFeatureType, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getOverride, ecore_EClass_m_getOperationCount, ecore_EClass_m_getFeatureID, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getFeatureCount}

# EClassifier class attributes and methods

# ecore_EOperation class attributes and methods
ecore_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=IntegerType)
ecore_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=BooleanType)
ecore_EOperation.methods={ecore_EOperation_m_isOverrideOf, ecore_EOperation_m_getOperationID}

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_transient}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getFeatureID, ecore_EStructuralFeature_m_getContainerClass}

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_resolveProxies, ecore_EReference_container, ecore_EReference_containment}

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceClassName, ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClass, ecore_EClassifier_instanceTypeName}
ecore_EClassifier.methods={ecore_EClassifier_m_getClassifierID, ecore_EClassifier_m_isInstance}

# ENamedElement class attributes and methods

# ecore_EGenericType class attributes and methods
ecore_EGenericType_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EGenericType.methods={ecore_EGenericType_m_isInstance}

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteralByLiteral}

# EDataType class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsURI}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_ETypeParameter class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_literal, ecore_EEnumLiteral_instance, ecore_EEnumLiteral_value}

# ecore_EFactory class attributes and methods
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_createFromString, ecore_EFactory_m_create, ecore_EFactory_m_convertToString}

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EParameter class attributes and methods

# ETypedElement class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement.attributes={ecore_ETypedElement_ordered, ecore_ETypedElement_unique, ecore_ETypedElement_many, ecore_ETypedElement_lowerBound, ecore_ETypedElement_upperBound, ecore_ETypedElement_required}

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="ecore_EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="3", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=ecore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents4: BinaryAssociation = BinaryAssociation(
    name="contents4",
    ends={
        Property(name="ecore_EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation5", type=ecore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references6: BinaryAssociation = BinaryAssociation(
    name="references6",
    ends={
        Property(name="ecore_EObject8", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation7", type=ecore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes10: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes10",
    ends={
        Property(name="ecore_EClass9", type=ecore_EClass, multiplicity=Multiplicity(0, 9999)),
        Property(name="ecore_EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eOperations11: BinaryAssociation = BinaryAssociation(
    name="eOperations11",
    ends={
        Property(name="13", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllContainments25: BinaryAssociation = BinaryAssociation(
    name="eAllContainments25",
    ends={
        Property(name="ecore_EReference27", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations28: BinaryAssociation = BinaryAssociation(
    name="eAllOperations28",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass29", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllAttributes14: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes14",
    ends={
        Property(name="ecore_EAttribute16", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass15", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences17: BinaryAssociation = BinaryAssociation(
    name="eAllReferences17",
    ends={
        Property(name="ecore_EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass18", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences19: BinaryAssociation = BinaryAssociation(
    name="eReferences19",
    ends={
        Property(name="ecore_EReference21", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass20", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes22: BinaryAssociation = BinaryAssociation(
    name="eAttributes22",
    ends={
        Property(name="ecore_EAttribute24", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass23", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllGenericSuperTypes43: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes43",
    ends={
        Property(name="ecore_EGenericType45", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass44", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures30: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures30",
    ends={
        Property(name="ecore_EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass31", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes33: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes33",
    ends={
        Property(name="ecore_EClass34", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass32", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute35: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute35",
    ends={
        Property(name="ecore_EAttribute37", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass36", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures38: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures38",
    ends={
        Property(name="40", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="39", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes41: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes41",
    ends={
        Property(name="ecore_EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass42", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="48", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="47", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters49: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters49",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage56: BinaryAssociation = BinaryAssociation(
    name="ePackage56",
    ends={
        Property(name="58", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="57", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eLiterals50: BinaryAssociation = BinaryAssociation(
    name="eLiterals50",
    ends={
        Property(name="52", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="51", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum53: BinaryAssociation = BinaryAssociation(
    name="eEnum53",
    ends={
        Property(name="55", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="54", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations59: BinaryAssociation = BinaryAssociation(
    name="eAnnotations59",
    ends={
        Property(name="61", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="60", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass62: BinaryAssociation = BinaryAssociation(
    name="eContainingClass62",
    ends={
        Property(name="64", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="63", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters65: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters65",
    ends={
        Property(name="ecore_ETypeParameter67", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation66", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters68: BinaryAssociation = BinaryAssociation(
    name="eParameters68",
    ends={
        Property(name="70", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="69", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages84: BinaryAssociation = BinaryAssociation(
    name="eSubpackages84",
    ends={
        Property(name="86", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="85", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage88: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage88",
    ends={
        Property(name="90", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="89", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eExceptions71: BinaryAssociation = BinaryAssociation(
    name="eExceptions71",
    ends={
        Property(name="ecore_EClassifier73", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation72", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions74: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions74",
    ends={
        Property(name="ecore_EGenericType76", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation75", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance77: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance77",
    ends={
        Property(name="79", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="78", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers80: BinaryAssociation = BinaryAssociation(
    name="eClassifiers80",
    ends={
        Property(name="82", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="81", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eOperation91: BinaryAssociation = BinaryAssociation(
    name="eOperation91",
    ends={
        Property(name="93", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="92", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite95: BinaryAssociation = BinaryAssociation(
    name="eOpposite95",
    ends={
        Property(name="ecore_EReference96", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference94", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType97: BinaryAssociation = BinaryAssociation(
    name="eReferenceType97",
    ends={
        Property(name="ecore_EClass99", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference98", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys100: BinaryAssociation = BinaryAssociation(
    name="eKeys100",
    ends={
        Property(name="ecore_EAttribute102", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference101", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eType106: BinaryAssociation = BinaryAssociation(
    name="eType106",
    ends={
        Property(name="ecore_EClassifier107", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType108: BinaryAssociation = BinaryAssociation(
    name="eGenericType108",
    ends={
        Property(name="ecore_EGenericType110", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement109", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eContainingClass103: BinaryAssociation = BinaryAssociation(
    name="eContainingClass103",
    ends={
        Property(name="105", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="104", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier126: BinaryAssociation = BinaryAssociation(
    name="eClassifier126",
    ends={
        Property(name="ecore_EClassifier128", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType127", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds129: BinaryAssociation = BinaryAssociation(
    name="eBounds129",
    ends={
        Property(name="ecore_EGenericType131", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter130", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound112: BinaryAssociation = BinaryAssociation(
    name="eUpperBound112",
    ends={
        Property(name="ecore_EGenericType113", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType111", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments115: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments115",
    ends={
        Property(name="ecore_EGenericType116", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType114", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType117: BinaryAssociation = BinaryAssociation(
    name="eRawType117",
    ends={
        Property(name="ecore_EClassifier119", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType118", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound121: BinaryAssociation = BinaryAssociation(
    name="eLowerBound121",
    ends={
        Property(name="ecore_EGenericType122", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType120", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter123: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter123",
    ends={
        Property(name="ecore_ETypeParameter125", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType124", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={EStructuralFeature, ecore_EDataType, ecore_EAnnotation, EModelElement, ecore_EAttribute, ecore_EStringToStringMapEntry, ecore_EModelElement, ecore_EObject, ecore_EClass, EClassifier, ecore_EOperation, ecore_EStructuralFeature, ecore_EReference, ecore_EClassifier, ENamedElement, ecore_EGenericType, ecore_EEnum, EDataType, ecore_EPackage, ecore_ETypeParameter, ecore_EEnumLiteral, ecore_EFactory, ecore_ENamedElement, ecore_EParameter, ETypedElement, ecore_ETypedElement},
    associations={eAttributeType0, details1, eModelElement2, contents4, references6, eSuperTypes10, eOperations11, eAllContainments25, eAllOperations28, eAllAttributes14, eAllReferences17, eReferences19, eAttributes22, eAllGenericSuperTypes43, eAllStructuralFeatures30, eAllSuperTypes33, eIDAttribute35, eStructuralFeatures38, eGenericSuperTypes41, ePackage46, eTypeParameters49, ePackage56, eLiterals50, eEnum53, eAnnotations59, eContainingClass62, eTypeParameters65, eParameters68, eSubpackages84, eSuperPackage88, eExceptions71, eGenericExceptions74, eFactoryInstance77, eClassifiers80, eOperation91, eOpposite95, eReferenceType97, eKeys100, eType106, eGenericType108, eContainingClass103, eClassifier126, eBounds129, eUpperBound112, eTypeArguments115, eRawType117, eLowerBound121, eTypeParameter123},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EAnnotation_EModelElement, gen_ecore_EClass_EClassifier, gen_ecore_EClassifier_ENamedElement, gen_ecore_EEnum_EDataType, gen_ecore_EDataType_EClassifier, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_ETypedElement_ENamedElement, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)