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
ecore_EAttribute = Class(name="ecore_EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
EDataType = Class(name="EDataType")
ecore_EAnnotation = Class(name="ecore_EAnnotation")
EModelElement = Class(name="EModelElement")
EStringToStringMapEntry = Class(name="EStringToStringMapEntry")
EObject = Class(name="EObject")
EClass = Class(name="EClass")
ecore_EClass = Class(name="ecore_EClass")
EClassifier = Class(name="EClassifier")
EOperation = Class(name="EOperation")
EAttribute = Class(name="EAttribute")
EReference = Class(name="EReference")
EPackage = Class(name="EPackage")
ETypeParameter = Class(name="ETypeParameter")
ecore_EDataType = Class(name="ecore_EDataType")
ecore_EEnum = Class(name="ecore_EEnum")
EGenericType = Class(name="EGenericType")
ecore_EClassifier = Class(name="ecore_EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EFactory = Class(name="ecore_EFactory")
ecore_EModelElement = Class(name="ecore_EModelElement", is_abstract=True)
EAnnotation = Class(name="EAnnotation")
ecore_ENamedElement = Class(name="ecore_ENamedElement", is_abstract=True)
ecore_EObject = Class(name="ecore_EObject")
EEnumLiteral = Class(name="EEnumLiteral")
ecore_EEnumLiteral = Class(name="ecore_EEnumLiteral")
EEnum = Class(name="EEnum")
ecore_EOperation = Class(name="ecore_EOperation")
ETypedElement = Class(name="ETypedElement")
EParameter = Class(name="EParameter")
ecore_EParameter = Class(name="ecore_EParameter")
ecore_EReference = Class(name="ecore_EReference")
ecore_EPackage = Class(name="ecore_EPackage")
EFactory = Class(name="EFactory")
ecore_ETypedElement = Class(name="ecore_ETypedElement", is_abstract=True)
ecore_EStructuralFeature = Class(name="ecore_EStructuralFeature", is_abstract=True)
ecore_EStringToStringMapEntry = Class(name="ecore_EStringToStringMapEntry")
ecore_EGenericType = Class(name="ecore_EGenericType")
ecore_ETypeParameter = Class(name="ecore_ETypeParameter")

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=StringType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# EStructuralFeature class attributes and methods

# EDataType class attributes and methods

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# EStringToStringMapEntry class attributes and methods

# EObject class attributes and methods

# EClass class attributes and methods

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=StringType)
ecore_EClass_interface: Property = Property(name="interface", type=StringType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='ecore_featureName', type=StringType)}, type=StringType)
ecore_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=StringType)
ecore_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='ecore_operationID', type=StringType)}, type=StringType)
ecore_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='ecore_operation', type=StringType)}, type=StringType)
ecore_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='ecore_operation', type=StringType)}, type=StringType)
ecore_EClass_m_getFeatureType: Method = Method(name="getFeatureType", parameters={Parameter(name='ecore_feature', type=StringType)}, type=StringType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='ecore_someClass', type=StringType)}, type=StringType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=StringType)
ecore_EClass_m_op_getEStructuralFeature: Method = Method(name="op_getEStructuralFeature", parameters={Parameter(name='ecore_featureID', type=StringType)}, type=StringType)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='ecore_feature', type=StringType)}, type=StringType)
ecore_EClass.attributes={ecore_EClass_interface, ecore_EClass_abstract}
ecore_EClass.methods={ecore_EClass_m_getFeatureType, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getFeatureID, ecore_EClass_m_getFeatureCount, ecore_EClass_m_getEOperation, ecore_EClass_m_getOperationID, ecore_EClass_m_getOperationCount, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getOverride, ecore_EClass_m_op_getEStructuralFeature}

# EClassifier class attributes and methods

# EOperation class attributes and methods

# EAttribute class attributes and methods

# EReference class attributes and methods

# EPackage class attributes and methods

# ETypeParameter class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=StringType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EEnum class attributes and methods
ecore_EEnum_m_op_getEEnumLiteral: Method = Method(name="op_getEEnumLiteral", parameters={Parameter(name='ecore_name', type=StringType)}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='ecore_value', type=StringType)}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='ecore_literal', type=StringType)}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_op_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteralByLiteral}

# EGenericType class attributes and methods

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='ecore_object', type=StringType)}, type=StringType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=StringType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceTypeName, ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClass}
ecore_EClassifier.methods={ecore_EClassifier_m_getClassifierID, ecore_EClassifier_m_isInstance}

# ENamedElement class attributes and methods

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='ecore_eClass', type=StringType)}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='ecore_literalValue', type=StringType), Parameter(name='ecore_eDataType', type=StringType)}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='ecore_instanceValue', type=StringType), Parameter(name='ecore_eDataType', type=StringType)}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_createFromString, ecore_EFactory_m_convertToString, ecore_EFactory_m_create}

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='ecore_source', type=StringType)}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# EAnnotation class attributes and methods

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EObject class attributes and methods
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='ecore_resolve', type=StringType), Parameter(name='ecore_feature', type=StringType)}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='ecore_newValue', type=StringType), Parameter(name='ecore_feature', type=StringType)})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='ecore_feature', type=StringType)}, type=StringType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='ecore_feature', type=StringType)})
ecore_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='ecore_arguments', type=StringType), Parameter(name='ecore_operation', type=StringType)}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=StringType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=StringType)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={}, type=StringType)
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={}, type=StringType)
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={}, type=StringType)
ecore_EObject_m_op_eGet: Method = Method(name="op_eGet", parameters={Parameter(name='ecore_feature', type=StringType)}, type=StringType)
ecore_EObject.methods={ecore_EObject_m_eResource, ecore_EObject_m_eClass, ecore_EObject_m_eGet, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eContents, ecore_EObject_m_eContainer, ecore_EObject_m_eSet, ecore_EObject_m_eIsSet, ecore_EObject_m_eUnset, ecore_EObject_m_op_eGet, ecore_EObject_m_eAllContents, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eInvoke, ecore_EObject_m_eIsProxy, ecore_EObject_m_eCrossReferences}

# EEnumLiteral class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=StringType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_instance, ecore_EEnumLiteral_value, ecore_EEnumLiteral_literal}

# EEnum class attributes and methods

# ecore_EOperation class attributes and methods
ecore_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=StringType)
ecore_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='ecore_someOperation', type=StringType)}, type=StringType)
ecore_EOperation.methods={ecore_EOperation_m_getOperationID, ecore_EOperation_m_isOverrideOf}

# ETypedElement class attributes and methods

# EParameter class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=StringType)
ecore_EReference_container: Property = Property(name="container", type=StringType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=StringType)
ecore_EReference.attributes={ecore_EReference_containment, ecore_EReference_resolveProxies, ecore_EReference_container}

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='ecore_name', type=StringType)}, type=StringType)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsURI}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# EFactory class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=StringType)
ecore_ETypedElement_required: Property = Property(name="required", type=StringType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=StringType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=StringType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=StringType)
ecore_ETypedElement_many: Property = Property(name="many", type=StringType)
ecore_ETypedElement.attributes={ecore_ETypedElement_upperBound, ecore_ETypedElement_required, ecore_ETypedElement_lowerBound, ecore_ETypedElement_unique, ecore_ETypedElement_many, ecore_ETypedElement_ordered}

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=StringType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=StringType)
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=StringType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=StringType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=StringType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=StringType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={}, type=StringType)
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_transient, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_unsettable}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getFeatureID, ecore_EStructuralFeature_m_getContainerClass}

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_value, ecore_EStringToStringMapEntry_key}

# ecore_EGenericType class attributes and methods
ecore_EGenericType_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='ecore_object', type=StringType)}, type=StringType)
ecore_EGenericType.methods={ecore_EGenericType_m_isInstance}

# ecore_ETypeParameter class attributes and methods

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=EDataType, multiplicity=Multiplicity(1, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="EModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation4", type=EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperTypes8: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes8",
    ends={
        Property(name="EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass", type=EClass, multiplicity=Multiplicity(0, 9999))
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="EObject7", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation6", type=EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments20: BinaryAssociation = BinaryAssociation(
    name="eAllContainments20",
    ends={
        Property(name="EReference22", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass21", type=EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations23: BinaryAssociation = BinaryAssociation(
    name="eAllOperations23",
    ends={
        Property(name="EOperation25", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass24", type=EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures26: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures26",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass27", type=EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes28: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes28",
    ends={
        Property(name="EClass30", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass29", type=EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute31: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute31",
    ends={
        Property(name="EAttribute33", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass32", type=EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eOperations9: BinaryAssociation = BinaryAssociation(
    name="eOperations9",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes10: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes10",
    ends={
        Property(name="EAttribute", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass11", type=EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences12: BinaryAssociation = BinaryAssociation(
    name="eAllReferences12",
    ends={
        Property(name="EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass13", type=EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences14: BinaryAssociation = BinaryAssociation(
    name="eReferences14",
    ends={
        Property(name="EReference16", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass15", type=EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes17: BinaryAssociation = BinaryAssociation(
    name="eAttributes17",
    ends={
        Property(name="EAttribute19", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass18", type=EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage42: BinaryAssociation = BinaryAssociation(
    name="ePackage42",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters43: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters43",
    ends={
        Property(name="ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eStructuralFeatures34: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures34",
    ends={
        Property(name="EStructuralFeature36", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass35", type=EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes37",
    ends={
        Property(name="EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass38", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes39",
    ends={
        Property(name="EGenericType41", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass40", type=EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage47", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations48: BinaryAssociation = BinaryAssociation(
    name="eAnnotations48",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLiterals44: BinaryAssociation = BinaryAssociation(
    name="eLiterals44",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum45: BinaryAssociation = BinaryAssociation(
    name="eEnum45",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass49: BinaryAssociation = BinaryAssociation(
    name="eContainingClass49",
    ends={
        Property(name="EClass50", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters51: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters51",
    ends={
        Property(name="ETypeParameter52", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation", type=ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters53: BinaryAssociation = BinaryAssociation(
    name="eParameters53",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage65: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage65",
    ends={
        Property(name="EPackage66", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation67: BinaryAssociation = BinaryAssociation(
    name="eOperation67",
    ends={
        Property(name="EOperation68", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite69: BinaryAssociation = BinaryAssociation(
    name="eOpposite69",
    ends={
        Property(name="EReference70", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference", type=EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType71: BinaryAssociation = BinaryAssociation(
    name="eReferenceType71",
    ends={
        Property(name="EClass73", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference72", type=EClass, multiplicity=Multiplicity(1, 1))
    }
)
eExceptions54: BinaryAssociation = BinaryAssociation(
    name="eExceptions54",
    ends={
        Property(name="EClassifier", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation55", type=EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions56: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions56",
    ends={
        Property(name="EGenericType58", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation57", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance59: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance59",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers60: BinaryAssociation = BinaryAssociation(
    name="eClassifiers60",
    ends={
        Property(name="EClassifier62", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage61", type=EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages63: BinaryAssociation = BinaryAssociation(
    name="eSubpackages63",
    ends={
        Property(name="EPackage64", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass77: BinaryAssociation = BinaryAssociation(
    name="eContainingClass77",
    ends={
        Property(name="EClass78", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=EClass, multiplicity=Multiplicity(0, 1))
    }
)
eKeys74: BinaryAssociation = BinaryAssociation(
    name="eKeys74",
    ends={
        Property(name="EAttribute76", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference75", type=EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eType79: BinaryAssociation = BinaryAssociation(
    name="eType79",
    ends={
        Property(name="EClassifier80", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType81: BinaryAssociation = BinaryAssociation(
    name="eGenericType81",
    ends={
        Property(name="EGenericType83", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement82", type=EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eBounds101: BinaryAssociation = BinaryAssociation(
    name="eBounds101",
    ends={
        Property(name="EGenericType102", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound84: BinaryAssociation = BinaryAssociation(
    name="eUpperBound84",
    ends={
        Property(name="EGenericType85", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType", type=EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments86: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments86",
    ends={
        Property(name="EGenericType88", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType87", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType89: BinaryAssociation = BinaryAssociation(
    name="eRawType89",
    ends={
        Property(name="EClassifier91", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType90", type=EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound92: BinaryAssociation = BinaryAssociation(
    name="eLowerBound92",
    ends={
        Property(name="EGenericType94", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType93", type=EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter95: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter95",
    ends={
        Property(name="ETypeParameter97", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType96", type=ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier98: BinaryAssociation = BinaryAssociation(
    name="eClassifier98",
    ends={
        Property(name="EClassifier100", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType99", type=EClassifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAttribute, EStructuralFeature, EDataType, ecore_EAnnotation, EModelElement, EStringToStringMapEntry, EObject, EClass, ecore_EClass, EClassifier, EOperation, EAttribute, EReference, EPackage, ETypeParameter, ecore_EDataType, ecore_EEnum, EGenericType, ecore_EClassifier, ENamedElement, ecore_EFactory, ecore_EModelElement, EAnnotation, ecore_ENamedElement, ecore_EObject, EEnumLiteral, ecore_EEnumLiteral, EEnum, ecore_EOperation, ETypedElement, EParameter, ecore_EParameter, ecore_EReference, ecore_EPackage, EFactory, ecore_ETypedElement, ecore_EStructuralFeature, ecore_EStringToStringMapEntry, ecore_EGenericType, ecore_ETypeParameter},
    associations={eAttributeType0, details1, eModelElement2, contents3, eSuperTypes8, references5, eAllContainments20, eAllOperations23, eAllStructuralFeatures26, eAllSuperTypes28, eIDAttribute31, eOperations9, eAllAttributes10, eAllReferences12, eReferences14, eAttributes17, ePackage42, eTypeParameters43, eStructuralFeatures34, eGenericSuperTypes37, eAllGenericSuperTypes39, ePackage46, eAnnotations48, eLiterals44, eEnum45, eContainingClass49, eTypeParameters51, eParameters53, eSuperPackage65, eOperation67, eOpposite69, eReferenceType71, eExceptions54, eGenericExceptions56, eFactoryInstance59, eClassifiers60, eSubpackages63, eContainingClass77, eKeys74, eType79, eGenericType81, eBounds101, eUpperBound84, eTypeArguments86, eRawType89, eLowerBound92, eTypeParameter95, eClassifier98},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EAnnotation_EModelElement, gen_ecore_EClass_EClassifier, gen_ecore_EDataType_EClassifier, gen_ecore_EEnum_EDataType, gen_ecore_EClassifier_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_EPackage_ENamedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)