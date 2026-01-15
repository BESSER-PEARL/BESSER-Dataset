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
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
EStructuralFeature = Class(name="EStructuralFeature")
EDataType = Class(name="EDataType")
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
EStringToStringMapEntry = Class(name="EStringToStringMapEntry")
EObject = Class(name="EObject")
EClass = Class(name="EClass")
EOperation = Class(name="EOperation")
EAttribute = Class(name="EAttribute")
EReference = Class(name="EReference")
EGenericType = Class(name="EGenericType")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
EPackage = Class(name="EPackage")
ETypeParameter = Class(name="ETypeParameter")
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EEnum = Class(name="ecore::EEnum")
EEnumLiteral = Class(name="EEnumLiteral")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
EEnum = Class(name="EEnum")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
EAnnotation = Class(name="EAnnotation")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_EOperation = Class(name="ecore::EOperation")
ETypedElement = Class(name="ETypedElement")
ecore_EObject = Class(name="ecore::EObject")
EParameter = Class(name="EParameter")
ecore_EPackage = Class(name="ecore::EPackage")
EFactory = Class(name="EFactory")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_EReference = Class(name="ecore::EReference")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=StringType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=StringType)
ecore_EClass_interface: Property = Property(name="interface", type=StringType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=StringType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=StringType)
ecore_EClass_m_getFeatureType: Method = Method(name="getFeatureType", parameters={Parameter(name='feature')}, type=StringType)
ecore_EClass_m_op_getEStructuralFeature: Method = Method(name="op_getEStructuralFeature", parameters={Parameter(name='featureID')}, type=StringType)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=StringType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=StringType)
ecore_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=StringType)
ecore_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
ecore_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=StringType)
ecore_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
ecore_EClass.attributes={ecore_EClass_abstract, ecore_EClass_interface}
ecore_EClass.methods={ecore_EClass_m_getOperationCount, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getOperationID, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getOverride, ecore_EClass_m_getFeatureType, ecore_EClass_m_getFeatureID, ecore_EClass_m_getEOperation, ecore_EClass_m_getFeatureCount, ecore_EClass_m_op_getEStructuralFeature}

# EClassifier class attributes and methods

# EStructuralFeature class attributes and methods

# EDataType class attributes and methods

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# EStringToStringMapEntry class attributes and methods

# EObject class attributes and methods

# EClass class attributes and methods

# EOperation class attributes and methods

# EAttribute class attributes and methods

# EReference class attributes and methods

# EGenericType class attributes and methods

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=StringType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceTypeName, ecore_EClassifier_instanceClass, ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClassName}
ecore_EClassifier.methods={ecore_EClassifier_m_isInstance, ecore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# EPackage class attributes and methods

# ETypeParameter class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=StringType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EEnum class attributes and methods
ecore_EEnum_m_op_getEEnumLiteral: Method = Method(name="op_getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_op_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteralByLiteral, ecore_EEnum_m_getEEnumLiteral}

# EEnumLiteral class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=StringType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_literal, ecore_EEnumLiteral_instance, ecore_EEnumLiteral_value}

# EEnum class attributes and methods

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='eDataType'), Parameter(name='instanceValue')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_convertToString, ecore_EFactory_m_createFromString, ecore_EFactory_m_create}

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# EAnnotation class attributes and methods

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EOperation class attributes and methods
ecore_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=StringType)
ecore_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=StringType)
ecore_EOperation.methods={ecore_EOperation_m_isOverrideOf, ecore_EOperation_m_getOperationID}

# ETypedElement class attributes and methods

# ecore_EObject class attributes and methods
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=StringType)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={}, type=StringType)
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={}, type=StringType)
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={}, type=StringType)
ecore_EObject_m_op_eGet: Method = Method(name="op_eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='operation'), Parameter(name='arguments')}, type=StringType)
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=StringType)
ecore_EObject.methods={ecore_EObject_m_eIsProxy, ecore_EObject_m_eContainer, ecore_EObject_m_eIsSet, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eAllContents, ecore_EObject_m_eUnset, ecore_EObject_m_eContents, ecore_EObject_m_eResource, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eSet, ecore_EObject_m_eInvoke, ecore_EObject_m_eGet, ecore_EObject_m_eClass, ecore_EObject_m_op_eGet, ecore_EObject_m_eContainmentFeature}

# EParameter class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=StringType)
ecore_EPackage.attributes={ecore_EPackage_nsURI, ecore_EPackage_nsPrefix}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# EFactory class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=StringType)
ecore_EReference_container: Property = Property(name="container", type=StringType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=StringType)
ecore_EReference.attributes={ecore_EReference_containment, ecore_EReference_container, ecore_EReference_resolveProxies}

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=StringType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=StringType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=StringType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=StringType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=StringType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=StringType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={}, type=StringType)
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_transient, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_volatile}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureID}

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=StringType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=StringType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=StringType)
ecore_ETypedElement_many: Property = Property(name="many", type=StringType)
ecore_ETypedElement_required: Property = Property(name="required", type=StringType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=StringType)
ecore_ETypedElement.attributes={ecore_ETypedElement_unique, ecore_ETypedElement_many, ecore_ETypedElement_upperBound, ecore_ETypedElement_ordered, ecore_ETypedElement_lowerBound, ecore_ETypedElement_required}

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_key, ecore_EStringToStringMapEntry_value}

# ecore_EGenericType class attributes and methods
ecore_EGenericType_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
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
        Property(name="#", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation4", type=EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="EObject7", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation6", type=EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes8: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes8",
    ends={
        Property(name="EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass", type=EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="EAttribute21", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass20", type=EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="EReference24", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass23", type=EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations9: BinaryAssociation = BinaryAssociation(
    name="eOperations9",
    ends={
        Property(name="#11", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="110", type=EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes12: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes12",
    ends={
        Property(name="EAttribute", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass13", type=EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass15", type=EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="EReference18", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass17", type=EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="EAttribute34", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass33", type=EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="#37", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="136", type=EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes38: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes38",
    ends={
        Property(name="EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass39", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes40: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes40",
    ends={
        Property(name="EGenericType42", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass41", type=EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass28", type=EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes29: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes29",
    ends={
        Property(name="EClass31", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass30", type=EClass, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage43: BinaryAssociation = BinaryAssociation(
    name="ePackage43",
    ends={
        Property(name="#45", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="144", type=EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters46: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters46",
    ends={
        Property(name="ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLiterals47: BinaryAssociation = BinaryAssociation(
    name="eLiterals47",
    ends={
        Property(name="#49", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="148", type=EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum50: BinaryAssociation = BinaryAssociation(
    name="eEnum50",
    ends={
        Property(name="#52", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="151", type=EEnum, multiplicity=Multiplicity(0, 1))
    }
)
ePackage53: BinaryAssociation = BinaryAssociation(
    name="ePackage53",
    ends={
        Property(name="#55", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="154", type=EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations56: BinaryAssociation = BinaryAssociation(
    name="eAnnotations56",
    ends={
        Property(name="#58", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="157", type=EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters64: BinaryAssociation = BinaryAssociation(
    name="eParameters64",
    ends={
        Property(name="#66", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="165", type=EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions67: BinaryAssociation = BinaryAssociation(
    name="eExceptions67",
    ends={
        Property(name="EClassifier", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation68", type=EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions69: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions69",
    ends={
        Property(name="EGenericType71", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation70", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance72: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance72",
    ends={
        Property(name="#74", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="173", type=EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers75: BinaryAssociation = BinaryAssociation(
    name="eClassifiers75",
    ends={
        Property(name="#77", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="176", type=EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages78: BinaryAssociation = BinaryAssociation(
    name="eSubpackages78",
    ends={
        Property(name="#80", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="179", type=EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage81: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage81",
    ends={
        Property(name="#83", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="182", type=EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation84: BinaryAssociation = BinaryAssociation(
    name="eOperation84",
    ends={
        Property(name="#86", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="185", type=EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass59: BinaryAssociation = BinaryAssociation(
    name="eContainingClass59",
    ends={
        Property(name="#61", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="160", type=EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters62: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters62",
    ends={
        Property(name="ETypeParameter63", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation", type=ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eOpposite87: BinaryAssociation = BinaryAssociation(
    name="eOpposite87",
    ends={
        Property(name="EReference88", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference", type=EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType89: BinaryAssociation = BinaryAssociation(
    name="eReferenceType89",
    ends={
        Property(name="EClass91", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference90", type=EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys92: BinaryAssociation = BinaryAssociation(
    name="eKeys92",
    ends={
        Property(name="EAttribute94", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference93", type=EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eContainingClass95: BinaryAssociation = BinaryAssociation(
    name="eContainingClass95",
    ends={
        Property(name="#97", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="196", type=EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType98: BinaryAssociation = BinaryAssociation(
    name="eType98",
    ends={
        Property(name="EClassifier99", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eUpperBound103: BinaryAssociation = BinaryAssociation(
    name="eUpperBound103",
    ends={
        Property(name="EGenericType104", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType", type=EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments105: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments105",
    ends={
        Property(name="EGenericType107", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType106", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType108: BinaryAssociation = BinaryAssociation(
    name="eRawType108",
    ends={
        Property(name="EClassifier110", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType109", type=EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound111: BinaryAssociation = BinaryAssociation(
    name="eLowerBound111",
    ends={
        Property(name="EGenericType113", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType112", type=EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter114: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter114",
    ends={
        Property(name="ETypeParameter116", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType115", type=ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier117: BinaryAssociation = BinaryAssociation(
    name="eClassifier117",
    ends={
        Property(name="EClassifier119", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType118", type=EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType100: BinaryAssociation = BinaryAssociation(
    name="eGenericType100",
    ends={
        Property(name="EGenericType102", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement101", type=EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eBounds120: BinaryAssociation = BinaryAssociation(
    name="eBounds120",
    ends={
        Property(name="EGenericType121", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter", type=EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAttribute, ecore_EClass, EClassifier, EStructuralFeature, EDataType, ecore_EAnnotation, EModelElement, EStringToStringMapEntry, EObject, EClass, EOperation, EAttribute, EReference, EGenericType, ecore_EClassifier, ENamedElement, EPackage, ETypeParameter, ecore_EDataType, ecore_EEnum, EEnumLiteral, ecore_EEnumLiteral, EEnum, ecore_EFactory, ecore_EModelElement, EAnnotation, ecore_ENamedElement, ecore_EOperation, ETypedElement, ecore_EObject, EParameter, ecore_EPackage, EFactory, ecore_EParameter, ecore_EReference, ecore_EStructuralFeature, ecore_ETypedElement, ecore_EStringToStringMapEntry, ecore_EGenericType, ecore_ETypeParameter},
    associations={eAttributeType0, details1, eModelElement2, contents3, references5, eSuperTypes8, eAttributes19, eAllContainments22, eOperations9, eAllAttributes12, eAllReferences14, eReferences16, eIDAttribute32, eStructuralFeatures35, eGenericSuperTypes38, eAllGenericSuperTypes40, eAllOperations25, eAllStructuralFeatures27, eAllSuperTypes29, ePackage43, eTypeParameters46, eLiterals47, eEnum50, ePackage53, eAnnotations56, eParameters64, eExceptions67, eGenericExceptions69, eFactoryInstance72, eClassifiers75, eSubpackages78, eSuperPackage81, eOperation84, eContainingClass59, eTypeParameters62, eOpposite87, eReferenceType89, eKeys92, eContainingClass95, eType98, eUpperBound103, eTypeArguments105, eRawType108, eLowerBound111, eTypeParameter114, eClassifier117, eGenericType100, eBounds120},
    generalizations={gen_ecore_EClass_EClassifier, gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EAnnotation_EModelElement, gen_ecore_EClassifier_ENamedElement, gen_ecore_EDataType_EClassifier, gen_ecore_EEnum_EDataType, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)