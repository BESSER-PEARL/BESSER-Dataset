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
ecore_EAttribute = Class(name="ecore::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
ecore_EClass = Class(name="ecore::EClass")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
EModelElement = Class(name="EModelElement")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
EObject = Class(name="EObject")
ecore_EAnnotation = Class(name="ecore::EAnnotation")
ecore_EObject = Class(name="ecore::EObject")
ecore_EOperation = Class(name="ecore::EOperation")
EClassifier = Class(name="EClassifier")
ecore_EReference = Class(name="ecore::EReference")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")

# ecore_EAttribute class attributes and methods
ecore_EAttribute_id: Property = Property(name="id", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_id}

# EStructuralFeature class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_m_getFeatureId: Method = Method(name="getFeatureId", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_derived, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_transient, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_unsettable}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureId}

# ETypedElement class attributes and methods

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureId')}, type=EStructuralFeature)
ecore_EClass_m_getFeatureId: Method = Method(name="getFeatureId", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecore_EClass.attributes={ecore_EClass_abstract, ecore_EClass_interface}
ecore_EClass.methods={ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getFeatureId, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getFeatureCount, ecore_EClass_m_getEStructuralFeature}

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement.attributes={ecore_ETypedElement_upperBound, ecore_ETypedElement_required, ecore_ETypedElement_unique, ecore_ETypedElement_many, ecore_ETypedElement_lowerBound, ecore_ETypedElement_ordered}

# ENamedElement class attributes and methods

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierId: Method = Method(name="getClassifierId", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceTypeName, ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceClass, ecore_EClassifier_defaultValue}
ecore_EClassifier.methods={ecore_EClassifier_m_isInstance, ecore_EClassifier_m_getClassifierId}

# ecore_EGenericType class attributes and methods

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# EModelElement class attributes and methods

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# EObject class attributes and methods

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# ecore_EObject class attributes and methods
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=EObject)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={})
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='feature'), Parameter(name='newValue')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject.methods={ecore_EObject_m_eGet, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eAllContents, ecore_EObject_m_eUnset, ecore_EObject_m_eIsSet, ecore_EObject_m_eContainer, ecore_EObject_m_eIsProxy, ecore_EObject_m_eResource, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eContents, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eClass, ecore_EObject_m_eGet, ecore_EObject_m_eSet}

# ecore_EOperation class attributes and methods

# EClassifier class attributes and methods

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_containment, ecore_EReference_container, ecore_EReference_resolveProxies}

# ecore_EPackage class attributes and methods
ecore_EPackage_nsUri: Property = Property(name="nsUri", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsUri}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_ETypeParameter class attributes and methods

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=EObject)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_convertToString, ecore_EFactory_m_create, ecore_EFactory_m_createFromString}

# ecore_EParameter class attributes and methods

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_value, ecore_EStringToStringMapEntry_key}

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteralByLiteral}

# EDataType class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_value, ecore_EEnumLiteral_literal, ecore_EEnumLiteral_instance}

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eContainingClass1: BinaryAssociation = BinaryAssociation(
    name="eContainingClass1",
    ends={
        Property(name="EClass", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType2: BinaryAssociation = BinaryAssociation(
    name="eType2",
    ends={
        Property(name="ecore_EClassifier", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType3: BinaryAssociation = BinaryAssociation(
    name="eGenericType3",
    ends={
        Property(name="ecore_EGenericType", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement4", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eAnnotations5: BinaryAssociation = BinaryAssociation(
    name="eAnnotations5",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eOperations8: BinaryAssociation = BinaryAssociation(
    name="eOperations8",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperTypes7: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes7",
    ends={
        Property(name="ecore_EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass6", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes28: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes28",
    ends={
        Property(name="ecore_EClass29", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass27", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eAllAttributes9: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes9",
    ends={
        Property(name="ecore_EAttribute11", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass10", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences12: BinaryAssociation = BinaryAssociation(
    name="eAllReferences12",
    ends={
        Property(name="ecore_EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass13", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences14: BinaryAssociation = BinaryAssociation(
    name="eReferences14",
    ends={
        Property(name="ecore_EReference16", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass15", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes17: BinaryAssociation = BinaryAssociation(
    name="eAttributes17",
    ends={
        Property(name="ecore_EAttribute19", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass18", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments20: BinaryAssociation = BinaryAssociation(
    name="eAllContainments20",
    ends={
        Property(name="ecore_EReference22", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass21", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations23: BinaryAssociation = BinaryAssociation(
    name="eAllOperations23",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass24", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures25: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures25",
    ends={
        Property(name="ecore_EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eidAttribute30: BinaryAssociation = BinaryAssociation(
    name="eidAttribute30",
    ends={
        Property(name="ecore_EAttribute32", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass31", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures33: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures33",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass34", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes35: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes35",
    ends={
        Property(name="ecore_EGenericType37", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass36", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes38: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes38",
    ends={
        Property(name="ecore_EGenericType40", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass39", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eSubpackages46: BinaryAssociation = BinaryAssociation(
    name="eSubpackages46",
    ends={
        Property(name="EPackage47", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage41: BinaryAssociation = BinaryAssociation(
    name="ePackage41",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters42: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters42",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier43", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance44: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance44",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eSuperPackage49: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage49",
    ends={
        Property(name="EPackage50", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eClassifiers51: BinaryAssociation = BinaryAssociation(
    name="eClassifiers51",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage52", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage53: BinaryAssociation = BinaryAssociation(
    name="ePackage53",
    ends={
        Property(name="EPackage54", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eTypeParameters76: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters76",
    ends={
        Property(name="ecore_ETypeParameter78", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation77", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eBounds55: BinaryAssociation = BinaryAssociation(
    name="eBounds55",
    ends={
        Property(name="ecore_EGenericType57", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter56", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound59: BinaryAssociation = BinaryAssociation(
    name="eUpperBound59",
    ends={
        Property(name="ecore_EGenericType60", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType58", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments62: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments62",
    ends={
        Property(name="ecore_EGenericType63", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType61", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType64: BinaryAssociation = BinaryAssociation(
    name="eRawType64",
    ends={
        Property(name="ecore_EClassifier66", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType65", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound68: BinaryAssociation = BinaryAssociation(
    name="eLowerBound68",
    ends={
        Property(name="ecore_EGenericType69", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType67", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter70: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter70",
    ends={
        Property(name="ecore_ETypeParameter72", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType71", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier73: BinaryAssociation = BinaryAssociation(
    name="eClassifier73",
    ends={
        Property(name="ecore_EClassifier75", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType74", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eParameters79: BinaryAssociation = BinaryAssociation(
    name="eParameters79",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions80: BinaryAssociation = BinaryAssociation(
    name="eExceptions80",
    ends={
        Property(name="ecore_EClassifier82", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation81", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions83: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions83",
    ends={
        Property(name="ecore_EGenericType85", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation84", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass86: BinaryAssociation = BinaryAssociation(
    name="eContainingClass86",
    ends={
        Property(name="EClass87", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOperation88: BinaryAssociation = BinaryAssociation(
    name="eOperation88",
    ends={
        Property(name="EOperation89", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite91: BinaryAssociation = BinaryAssociation(
    name="eOpposite91",
    ends={
        Property(name="ecore_EReference92", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference90", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType93: BinaryAssociation = BinaryAssociation(
    name="eReferenceType93",
    ends={
        Property(name="ecore_EClass95", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference94", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys96: BinaryAssociation = BinaryAssociation(
    name="eKeys96",
    ends={
        Property(name="ecore_EAttribute98", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference97", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
details99: BinaryAssociation = BinaryAssociation(
    name="details99",
    ends={
        Property(name="ecore_EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents100: BinaryAssociation = BinaryAssociation(
    name="contents100",
    ends={
        Property(name="ecore_EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation101", type=ecore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references102: BinaryAssociation = BinaryAssociation(
    name="references102",
    ends={
        Property(name="ecore_EObject104", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation103", type=ecore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eModelElement105: BinaryAssociation = BinaryAssociation(
    name="eModelElement105",
    ends={
        Property(name="EModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
eLiterals106: BinaryAssociation = BinaryAssociation(
    name="eLiterals106",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum107: BinaryAssociation = BinaryAssociation(
    name="eEnum107",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EModelElement_EObject = Generalization(general=EObject, specific=ecore_EModelElement)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EGenericType_EObject = Generalization(general=EObject, specific=ecore_EGenericType)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAttribute, EStructuralFeature, ecore_EDataType, ecore_EStructuralFeature, ETypedElement, ecore_EClass, ecore_ETypedElement, ENamedElement, ecore_EClassifier, ecore_EGenericType, ecore_ENamedElement, EModelElement, ecore_EModelElement, EObject, ecore_EAnnotation, ecore_EObject, ecore_EOperation, EClassifier, ecore_EReference, ecore_EPackage, ecore_ETypeParameter, ecore_EFactory, ecore_EParameter, ecore_EStringToStringMapEntry, ecore_EEnum, EDataType, ecore_EEnumLiteral},
    associations={eAttributeType0, eContainingClass1, eType2, eGenericType3, eAnnotations5, eOperations8, eSuperTypes7, eAllSuperTypes28, eAllAttributes9, eAllReferences12, eReferences14, eAttributes17, eAllContainments20, eAllOperations23, eAllStructuralFeatures25, eidAttribute30, eStructuralFeatures33, eGenericSuperTypes35, eAllGenericSuperTypes38, eSubpackages46, ePackage41, eTypeParameters42, eFactoryInstance44, eSuperPackage49, eClassifiers51, ePackage53, eTypeParameters76, eBounds55, eUpperBound59, eTypeArguments62, eRawType64, eLowerBound68, eTypeParameter70, eClassifier73, eParameters79, eExceptions80, eGenericExceptions83, eContainingClass86, eOperation88, eOpposite91, eReferenceType93, eKeys96, details99, contents100, references102, eModelElement105, eLiterals106, eEnum107},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EModelElement_EObject, gen_ecore_EClass_EClassifier, gen_ecore_EClassifier_ENamedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_ETypeParameter_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EDataType_EClassifier, gen_ecore_EGenericType_EObject, gen_ecore_EReference_EStructuralFeature, gen_ecore_EParameter_ETypedElement, gen_ecore_EAnnotation_EModelElement, gen_ecore_EEnum_EDataType, gen_ecore_EEnumLiteral_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)