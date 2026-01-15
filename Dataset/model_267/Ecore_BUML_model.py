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
ecoreO_EAnnotation = Class(name="ecoreO::EAnnotation")
EModelElement = Class(name="EModelElement")
ecoreO_EStringToStringMapEntry = Class(name="ecoreO::EStringToStringMapEntry")
ecoreO_EModelElement = Class(name="ecoreO::EModelElement", is_abstract=True)
ecoreO_EAttribute = Class(name="ecoreO::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
ecoreO_EDataType = Class(name="ecoreO::EDataType")
ecoreO_EObject = Class(name="ecoreO::EObject")
ecoreO_EClass = Class(name="ecoreO::EClass")
EClassifier = Class(name="EClassifier")
ecoreO_EOperation = Class(name="ecoreO::EOperation")
ecoreO_EReference = Class(name="ecoreO::EReference")
ecoreO_EGenericType = Class(name="ecoreO::EGenericType")
ecoreO_EStructuralFeature = Class(name="ecoreO::EStructuralFeature", is_abstract=True)
ecoreO_EPackage = Class(name="ecoreO::EPackage")
ecoreO_ETypeParameter = Class(name="ecoreO::ETypeParameter")
ecoreO_EClassifier = Class(name="ecoreO::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecoreO_EFactory = Class(name="ecoreO::EFactory")
ecoreO_EEnum = Class(name="ecoreO::EEnum")
EDataType = Class(name="EDataType")
ecoreO_EEnumLiteral = Class(name="ecoreO::EEnumLiteral")
ecoreO_ENamedElement = Class(name="ecoreO::ENamedElement", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
ecoreO_EParameter = Class(name="ecoreO::EParameter")
ecoreO_ETypedElement = Class(name="ecoreO::ETypedElement", is_abstract=True)

# ecoreO_EAnnotation class attributes and methods
ecoreO_EAnnotation_source: Property = Property(name="source", type=StringType)
ecoreO_EAnnotation.attributes={ecoreO_EAnnotation_source}

# EModelElement class attributes and methods

# ecoreO_EStringToStringMapEntry class attributes and methods
ecoreO_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecoreO_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecoreO_EStringToStringMapEntry.attributes={ecoreO_EStringToStringMapEntry_value, ecoreO_EStringToStringMapEntry_key}

# ecoreO_EModelElement class attributes and methods
ecoreO_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecoreO_EModelElement.methods={ecoreO_EModelElement_m_getEAnnotation}

# ecoreO_EAttribute class attributes and methods
ecoreO_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecoreO_EAttribute.attributes={ecoreO_EAttribute_iD}

# EStructuralFeature class attributes and methods

# ecoreO_EDataType class attributes and methods
ecoreO_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecoreO_EDataType.attributes={ecoreO_EDataType_serializable}

# ecoreO_EObject class attributes and methods
ecoreO_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecoreO_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecoreO_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecoreO_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecoreO_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
ecoreO_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecoreO_EObject_m_eContents: Method = Method(name="eContents", parameters={})
ecoreO_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
ecoreO_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='arguments'), Parameter(name='operation')}, type=StringType)
ecoreO_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
ecoreO_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecoreO_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecoreO_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='feature'), Parameter(name='newValue')})
ecoreO_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecoreO_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecoreO_EObject.methods={ecoreO_EObject_m_eAllContents, ecoreO_EObject_m_eGet, ecoreO_EObject_m_eIsSet, ecoreO_EObject_m_eInvoke, ecoreO_EObject_m_eContainingFeature, ecoreO_EObject_m_eCrossReferences, ecoreO_EObject_m_eUnset, ecoreO_EObject_m_eContainer, ecoreO_EObject_m_eResource, ecoreO_EObject_m_eIsProxy, ecoreO_EObject_m_eClass, ecoreO_EObject_m_eGet, ecoreO_EObject_m_eSet, ecoreO_EObject_m_eContents, ecoreO_EObject_m_eContainmentFeature}

# ecoreO_EClass class attributes and methods
ecoreO_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecoreO_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecoreO_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecoreO_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=IntegerType)
ecoreO_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
ecoreO_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=IntegerType)
ecoreO_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecoreO_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecoreO_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecoreO_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecoreO_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
ecoreO_EClass.attributes={ecoreO_EClass_abstract, ecoreO_EClass_interface}
ecoreO_EClass.methods={ecoreO_EClass_m_getOperationCount, ecoreO_EClass_m_getOperationID, ecoreO_EClass_m_getEStructuralFeature, ecoreO_EClass_m_getFeatureCount, ecoreO_EClass_m_isSuperTypeOf, ecoreO_EClass_m_getEOperation, ecoreO_EClass_m_getFeatureID, ecoreO_EClass_m_getEStructuralFeature, ecoreO_EClass_m_getOverride}

# EClassifier class attributes and methods

# ecoreO_EOperation class attributes and methods
ecoreO_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=IntegerType)
ecoreO_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=BooleanType)
ecoreO_EOperation.methods={ecoreO_EOperation_m_isOverrideOf, ecoreO_EOperation_m_getOperationID}

# ecoreO_EReference class attributes and methods
ecoreO_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecoreO_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecoreO_EReference_container: Property = Property(name="container", type=BooleanType)
ecoreO_EReference.attributes={ecoreO_EReference_resolveProxies, ecoreO_EReference_container, ecoreO_EReference_containment}

# ecoreO_EGenericType class attributes and methods

# ecoreO_EStructuralFeature class attributes and methods
ecoreO_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecoreO_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecoreO_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecoreO_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecoreO_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecoreO_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecoreO_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecoreO_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecoreO_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecoreO_EStructuralFeature.attributes={ecoreO_EStructuralFeature_defaultValueLiteral, ecoreO_EStructuralFeature_volatile, ecoreO_EStructuralFeature_unsettable, ecoreO_EStructuralFeature_transient, ecoreO_EStructuralFeature_defaultValue, ecoreO_EStructuralFeature_derived, ecoreO_EStructuralFeature_changeable}
ecoreO_EStructuralFeature.methods={ecoreO_EStructuralFeature_m_getContainerClass, ecoreO_EStructuralFeature_m_getFeatureID}

# ecoreO_EPackage class attributes and methods
ecoreO_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecoreO_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecoreO_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecoreO_EPackage.attributes={ecoreO_EPackage_nsPrefix, ecoreO_EPackage_nsURI}
ecoreO_EPackage.methods={ecoreO_EPackage_m_getEClassifier}

# ecoreO_ETypeParameter class attributes and methods

# ecoreO_EClassifier class attributes and methods
ecoreO_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecoreO_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecoreO_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecoreO_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecoreO_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecoreO_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecoreO_EClassifier.attributes={ecoreO_EClassifier_instanceClass, ecoreO_EClassifier_instanceClassName, ecoreO_EClassifier_defaultValue, ecoreO_EClassifier_instanceTypeName}
ecoreO_EClassifier.methods={ecoreO_EClassifier_m_getClassifierID, ecoreO_EClassifier_m_isInstance}

# ENamedElement class attributes and methods

# ecoreO_EFactory class attributes and methods
ecoreO_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecoreO_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecoreO_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
ecoreO_EFactory.methods={ecoreO_EFactory_m_create, ecoreO_EFactory_m_createFromString, ecoreO_EFactory_m_convertToString}

# ecoreO_EEnum class attributes and methods
ecoreO_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecoreO_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecoreO_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecoreO_EEnum.methods={ecoreO_EEnum_m_getEEnumLiteral, ecoreO_EEnum_m_getEEnumLiteralByLiteral, ecoreO_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# ecoreO_EEnumLiteral class attributes and methods
ecoreO_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecoreO_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecoreO_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecoreO_EEnumLiteral.attributes={ecoreO_EEnumLiteral_value, ecoreO_EEnumLiteral_instance, ecoreO_EEnumLiteral_literal}

# ecoreO_ENamedElement class attributes and methods
ecoreO_ENamedElement_name: Property = Property(name="name", type=StringType)
ecoreO_ENamedElement.attributes={ecoreO_ENamedElement_name}

# ETypedElement class attributes and methods

# ecoreO_EParameter class attributes and methods

# ecoreO_ETypedElement class attributes and methods
ecoreO_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecoreO_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecoreO_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecoreO_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecoreO_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecoreO_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecoreO_ETypedElement.attributes={ecoreO_ETypedElement_many, ecoreO_ETypedElement_unique, ecoreO_ETypedElement_ordered, ecoreO_ETypedElement_required, ecoreO_ETypedElement_upperBound, ecoreO_ETypedElement_lowerBound}

# Relationships
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="ecoreO_EStringToStringMapEntry", type=ecoreO_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EAnnotation", type=ecoreO_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="EModelElement", type=ecoreO_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecoreO_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecoreO_EDataType", type=ecoreO_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EAttribute", type=ecoreO_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="ecoreO_EObject", type=ecoreO_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EAnnotation4", type=ecoreO_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="ecoreO_EObject7", type=ecoreO_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EAnnotation6", type=ecoreO_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="ecoreO_EReference18", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass17", type=ecoreO_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="ecoreO_EAttribute21", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass20", type=ecoreO_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="ecoreO_EClass", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass8", type=ecoreO_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="EOperation", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecoreO_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes11: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes11",
    ends={
        Property(name="ecoreO_EAttribute13", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass12", type=ecoreO_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="ecoreO_EReference", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass15", type=ecoreO_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes37",
    ends={
        Property(name="ecoreO_EGenericType", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass38", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes39",
    ends={
        Property(name="ecoreO_EGenericType41", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass40", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="ecoreO_EReference24", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass23", type=ecoreO_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="ecoreO_EOperation", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass26", type=ecoreO_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="ecoreO_EStructuralFeature", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass28", type=ecoreO_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="ecoreO_EClass31", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass29", type=ecoreO_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="ecoreO_EAttribute34", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClass33", type=ecoreO_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="EStructuralFeature", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass36", type=ecoreO_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage42: BinaryAssociation = BinaryAssociation(
    name="ePackage42",
    ends={
        Property(name="EPackage", type=ecoreO_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecoreO_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters43: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters43",
    ends={
        Property(name="ecoreO_ETypeParameter", type=ecoreO_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EClassifier", type=ecoreO_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum45: BinaryAssociation = BinaryAssociation(
    name="eEnum45",
    ends={
        Property(name="EEnum", type=ecoreO_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecoreO_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eLiterals44: BinaryAssociation = BinaryAssociation(
    name="eLiterals44",
    ends={
        Property(name="EEnumLiteral", type=ecoreO_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecoreO_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage47", type=ecoreO_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecoreO_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations48: BinaryAssociation = BinaryAssociation(
    name="eAnnotations48",
    ends={
        Property(name="EAnnotation", type=ecoreO_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecoreO_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions54: BinaryAssociation = BinaryAssociation(
    name="eExceptions54",
    ends={
        Property(name="ecoreO_EClassifier56", type=ecoreO_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EOperation55", type=ecoreO_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions57: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions57",
    ends={
        Property(name="ecoreO_EGenericType59", type=ecoreO_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EOperation58", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass49: BinaryAssociation = BinaryAssociation(
    name="eContainingClass49",
    ends={
        Property(name="EClass", type=ecoreO_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecoreO_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters50: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters50",
    ends={
        Property(name="ecoreO_ETypeParameter52", type=ecoreO_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EOperation51", type=ecoreO_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters53: BinaryAssociation = BinaryAssociation(
    name="eParameters53",
    ends={
        Property(name="EParameter", type=ecoreO_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecoreO_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance60: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance60",
    ends={
        Property(name="EFactory", type=ecoreO_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecoreO_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eOpposite72: BinaryAssociation = BinaryAssociation(
    name="eOpposite72",
    ends={
        Property(name="ecoreO_EReference73", type=ecoreO_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EReference71", type=ecoreO_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType74: BinaryAssociation = BinaryAssociation(
    name="eReferenceType74",
    ends={
        Property(name="ecoreO_EClass76", type=ecoreO_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EReference75", type=ecoreO_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers61: BinaryAssociation = BinaryAssociation(
    name="eClassifiers61",
    ends={
        Property(name="EClassifier", type=ecoreO_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage62", type=ecoreO_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eKeys77: BinaryAssociation = BinaryAssociation(
    name="eKeys77",
    ends={
        Property(name="ecoreO_EAttribute79", type=ecoreO_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EReference78", type=ecoreO_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSubpackages64: BinaryAssociation = BinaryAssociation(
    name="eSubpackages64",
    ends={
        Property(name="EPackage65", type=ecoreO_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecoreO_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage67: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage67",
    ends={
        Property(name="EPackage68", type=ecoreO_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecoreO_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation69: BinaryAssociation = BinaryAssociation(
    name="eOperation69",
    ends={
        Property(name="EOperation70", type=ecoreO_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecoreO_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass80: BinaryAssociation = BinaryAssociation(
    name="eContainingClass80",
    ends={
        Property(name="EClass81", type=ecoreO_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecoreO_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType82: BinaryAssociation = BinaryAssociation(
    name="eType82",
    ends={
        Property(name="ecoreO_EClassifier83", type=ecoreO_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_ETypedElement", type=ecoreO_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType84: BinaryAssociation = BinaryAssociation(
    name="eGenericType84",
    ends={
        Property(name="ecoreO_EGenericType86", type=ecoreO_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_ETypedElement85", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eUpperBound88: BinaryAssociation = BinaryAssociation(
    name="eUpperBound88",
    ends={
        Property(name="ecoreO_EGenericType89", type=ecoreO_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EGenericType87", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments91: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments91",
    ends={
        Property(name="ecoreO_EGenericType92", type=ecoreO_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EGenericType90", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType93: BinaryAssociation = BinaryAssociation(
    name="eRawType93",
    ends={
        Property(name="ecoreO_EClassifier95", type=ecoreO_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EGenericType94", type=ecoreO_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eBounds105: BinaryAssociation = BinaryAssociation(
    name="eBounds105",
    ends={
        Property(name="ecoreO_ETypeParameter106", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ecoreO_EGenericType107", type=ecoreO_ETypeParameter, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound97: BinaryAssociation = BinaryAssociation(
    name="eLowerBound97",
    ends={
        Property(name="ecoreO_EGenericType98", type=ecoreO_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EGenericType96", type=ecoreO_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter99: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter99",
    ends={
        Property(name="ecoreO_ETypeParameter101", type=ecoreO_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EGenericType100", type=ecoreO_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier102: BinaryAssociation = BinaryAssociation(
    name="eClassifier102",
    ends={
        Property(name="ecoreO_EClassifier104", type=ecoreO_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreO_EGenericType103", type=ecoreO_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecoreO_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecoreO_EAnnotation)
gen_ecoreO_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreO_EAttribute)
gen_ecoreO_EClass_EClassifier = Generalization(general=EClassifier, specific=ecoreO_EClass)
gen_ecoreO_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecoreO_EDataType)
gen_ecoreO_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecoreO_EClassifier)
gen_ecoreO_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecoreO_EFactory)
gen_ecoreO_EEnum_EDataType = Generalization(general=EDataType, specific=ecoreO_EEnum)
gen_ecoreO_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecoreO_EEnumLiteral)
gen_ecoreO_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecoreO_ENamedElement)
gen_ecoreO_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecoreO_EOperation)
gen_ecoreO_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecoreO_EPackage)
gen_ecoreO_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecoreO_EStructuralFeature)
gen_ecoreO_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecoreO_EParameter)
gen_ecoreO_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecoreO_EReference)
gen_ecoreO_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecoreO_ETypedElement)
gen_ecoreO_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecoreO_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecoreO",
    types={ecoreO_EAnnotation, EModelElement, ecoreO_EStringToStringMapEntry, ecoreO_EModelElement, ecoreO_EAttribute, EStructuralFeature, ecoreO_EDataType, ecoreO_EObject, ecoreO_EClass, EClassifier, ecoreO_EOperation, ecoreO_EReference, ecoreO_EGenericType, ecoreO_EStructuralFeature, ecoreO_EPackage, ecoreO_ETypeParameter, ecoreO_EClassifier, ENamedElement, ecoreO_EFactory, ecoreO_EEnum, EDataType, ecoreO_EEnumLiteral, ecoreO_ENamedElement, ETypedElement, ecoreO_EParameter, ecoreO_ETypedElement},
    associations={details1, eModelElement2, eAttributeType0, contents3, references5, eReferences16, eAttributes19, eSuperTypes9, eOperations10, eAllAttributes11, eAllReferences14, eGenericSuperTypes37, eAllGenericSuperTypes39, eAllContainments22, eAllOperations25, eAllStructuralFeatures27, eAllSuperTypes30, eIDAttribute32, eStructuralFeatures35, ePackage42, eTypeParameters43, eEnum45, eLiterals44, ePackage46, eAnnotations48, eExceptions54, eGenericExceptions57, eContainingClass49, eTypeParameters50, eParameters53, eFactoryInstance60, eOpposite72, eReferenceType74, eClassifiers61, eKeys77, eSubpackages64, eSuperPackage67, eOperation69, eContainingClass80, eType82, eGenericType84, eUpperBound88, eTypeArguments91, eRawType93, eBounds105, eLowerBound97, eTypeParameter99, eClassifier102},
    generalizations={gen_ecoreO_EAnnotation_EModelElement, gen_ecoreO_EAttribute_EStructuralFeature, gen_ecoreO_EClass_EClassifier, gen_ecoreO_EDataType_EClassifier, gen_ecoreO_EClassifier_ENamedElement, gen_ecoreO_EFactory_EModelElement, gen_ecoreO_EEnum_EDataType, gen_ecoreO_EEnumLiteral_ENamedElement, gen_ecoreO_ENamedElement_EModelElement, gen_ecoreO_EOperation_ETypedElement, gen_ecoreO_EPackage_ENamedElement, gen_ecoreO_EStructuralFeature_ETypedElement, gen_ecoreO_EParameter_ETypedElement, gen_ecoreO_EReference_EStructuralFeature, gen_ecoreO_ETypedElement_ENamedElement, gen_ecoreO_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)