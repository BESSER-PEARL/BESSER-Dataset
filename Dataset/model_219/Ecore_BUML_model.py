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
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
ecore_EObject = Class(name="ecore::EObject")
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EReference = Class(name="ecore::EReference")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EGenericType = Class(name="ecore::EGenericType")
ENamedElement = Class(name="ENamedElement")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_EFactory = Class(name="ecore::EFactory")
EObject = Class(name="EObject")
ETypedElement = Class(name="ETypedElement")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# EStructuralFeature class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

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
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='resolve'), Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject.methods={ecore_EObject_m_eGet, ecore_EObject_m_eGet, ecore_EObject_m_eSet, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eResource, ecore_EObject_m_eAllContents, ecore_EObject_m_eIsProxy, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eContents, ecore_EObject_m_eIsSet, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eUnset, ecore_EObject_m_eContainer, ecore_EObject_m_eClass}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecore_EClass.attributes={ecore_EClass_abstract, ecore_EClass_interface}
ecore_EClass.methods={ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getFeatureID, ecore_EClass_m_getFeatureCount}

# EClassifier class attributes and methods

# ecore_EOperation class attributes and methods

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_containment, ecore_EReference_resolveProxies, ecore_EReference_container}

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
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_transient, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_defaultValue}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getFeatureID, ecore_EStructuralFeature_m_getContainerClass}

# ecore_EGenericType class attributes and methods

# ENamedElement class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsURI}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_ETypeParameter class attributes and methods

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteralByLiteral}

# EDataType class attributes and methods

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceClass, ecore_EClassifier_defaultValue, ecore_EClassifier_instanceTypeName, ecore_EClassifier_instanceClassName}
ecore_EClassifier.methods={ecore_EClassifier_m_getClassifierID, ecore_EClassifier_m_isInstance}

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_value, ecore_EEnumLiteral_literal, ecore_EEnumLiteral_instance}

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='literalValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_convertToString, ecore_EFactory_m_create, ecore_EFactory_m_createFromString}

# EObject class attributes and methods

# ETypedElement class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement.attributes={ecore_ETypedElement_unique, ecore_ETypedElement_many, ecore_ETypedElement_ordered, ecore_ETypedElement_upperBound, ecore_ETypedElement_required, ecore_ETypedElement_lowerBound}

# Relationships
eModelElement1: BinaryAssociation = BinaryAssociation(
    name="eModelElement1",
    ends={
        Property(name="EModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents2: BinaryAssociation = BinaryAssociation(
    name="contents2",
    ends={
        Property(name="ecore_EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references3: BinaryAssociation = BinaryAssociation(
    name="references3",
    ends={
        Property(name="ecore_EObject5", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation4", type=ecore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eSuperTypes7: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes7",
    ends={
        Property(name="ecore_EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass6", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations8: BinaryAssociation = BinaryAssociation(
    name="eOperations8",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
eAllSuperTypes28: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes28",
    ends={
        Property(name="ecore_EClass29", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass27", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute30: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute30",
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
        Property(name="ecore_EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass36", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes37",
    ends={
        Property(name="ecore_EGenericType39", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass38", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttributeForTest40: BinaryAssociation = BinaryAssociation(
    name="eIDAttributeForTest40",
    ends={
        Property(name="ecore_EAttribute42", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass41", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eAllAttributesForTest43: BinaryAssociation = BinaryAssociation(
    name="eAllAttributesForTest43",
    ends={
        Property(name="ecore_EAttribute45", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass44", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters47: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters47",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLiterals48: BinaryAssociation = BinaryAssociation(
    name="eLiterals48",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum49: BinaryAssociation = BinaryAssociation(
    name="eEnum49",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
ePackage50: BinaryAssociation = BinaryAssociation(
    name="ePackage50",
    ends={
        Property(name="EPackage51", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eFactoryInstance64: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance64",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers65: BinaryAssociation = BinaryAssociation(
    name="eClassifiers65",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage66", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages68: BinaryAssociation = BinaryAssociation(
    name="eSubpackages68",
    ends={
        Property(name="EPackage69", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass53: BinaryAssociation = BinaryAssociation(
    name="eContainingClass53",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters54: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters54",
    ends={
        Property(name="ecore_ETypeParameter56", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation55", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters57: BinaryAssociation = BinaryAssociation(
    name="eParameters57",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions58: BinaryAssociation = BinaryAssociation(
    name="eExceptions58",
    ends={
        Property(name="ecore_EClassifier60", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation59", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions61: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions61",
    ends={
        Property(name="ecore_EGenericType63", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation62", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAnnotations52: BinaryAssociation = BinaryAssociation(
    name="eAnnotations52",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eKeys81: BinaryAssociation = BinaryAssociation(
    name="eKeys81",
    ends={
        Property(name="ecore_EAttribute83", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference82", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperPackage71: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage71",
    ends={
        Property(name="EPackage72", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation73: BinaryAssociation = BinaryAssociation(
    name="eOperation73",
    ends={
        Property(name="EOperation74", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite76: BinaryAssociation = BinaryAssociation(
    name="eOpposite76",
    ends={
        Property(name="ecore_EReference77", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference75", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType78: BinaryAssociation = BinaryAssociation(
    name="eReferenceType78",
    ends={
        Property(name="ecore_EClass80", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference79", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eType86: BinaryAssociation = BinaryAssociation(
    name="eType86",
    ends={
        Property(name="ecore_EClassifier87", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType88: BinaryAssociation = BinaryAssociation(
    name="eGenericType88",
    ends={
        Property(name="ecore_EGenericType90", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement89", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eContainingClass84: BinaryAssociation = BinaryAssociation(
    name="eContainingClass84",
    ends={
        Property(name="EClass85", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eUpperBound92: BinaryAssociation = BinaryAssociation(
    name="eUpperBound92",
    ends={
        Property(name="ecore_EGenericType93", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType91", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments95: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments95",
    ends={
        Property(name="ecore_EGenericType96", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType94", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType97: BinaryAssociation = BinaryAssociation(
    name="eRawType97",
    ends={
        Property(name="ecore_EClassifier99", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType98", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound101: BinaryAssociation = BinaryAssociation(
    name="eLowerBound101",
    ends={
        Property(name="ecore_EGenericType102", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType100", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter103: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter103",
    ends={
        Property(name="ecore_ETypeParameter105", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType104", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier106: BinaryAssociation = BinaryAssociation(
    name="eClassifier106",
    ends={
        Property(name="ecore_EClassifier108", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType107", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds109: BinaryAssociation = BinaryAssociation(
    name="eBounds109",
    ends={
        Property(name="ecore_EGenericType111", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter110", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_EModelElement_EObject = Generalization(general=EObject, specific=ecore_EModelElement)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_EGenericType_EObject = Generalization(general=EObject, specific=ecore_EGenericType)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAttribute, EStructuralFeature, ecore_EDataType, ecore_EAnnotation, EModelElement, ecore_EModelElement, ecore_EObject, ecore_EClass, EClassifier, ecore_EOperation, ecore_EReference, ecore_EStructuralFeature, ecore_EGenericType, ENamedElement, ecore_EPackage, ecore_ETypeParameter, ecore_EEnum, EDataType, ecore_EClassifier, ecore_EEnumLiteral, ecore_EFactory, EObject, ETypedElement, ecore_EParameter, ecore_ENamedElement, ecore_ETypedElement},
    associations={eModelElement1, contents2, references3, eAttributeType0, eSuperTypes7, eOperations8, eAllAttributes9, eAllReferences12, eReferences14, eAttributes17, eAllContainments20, eAllOperations23, eAllStructuralFeatures25, eAllSuperTypes28, eIDAttribute30, eStructuralFeatures33, eGenericSuperTypes35, eAllGenericSuperTypes37, eIDAttributeForTest40, eAllAttributesForTest43, ePackage46, eTypeParameters47, eLiterals48, eEnum49, ePackage50, eFactoryInstance64, eClassifiers65, eSubpackages68, eContainingClass53, eTypeParameters54, eParameters57, eExceptions58, eGenericExceptions61, eAnnotations52, eKeys81, eSuperPackage71, eOperation73, eOpposite76, eReferenceType78, eType86, eGenericType88, eContainingClass84, eUpperBound92, eTypeArguments95, eRawType97, eLowerBound101, eTypeParameter103, eClassifier106, eBounds109},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EAnnotation_EModelElement, gen_ecore_EClass_EClassifier, gen_ecore_EClassifier_ENamedElement, gen_ecore_EDataType_EClassifier, gen_ecore_EEnum_EDataType, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_EModelElement_EObject, gen_ecore_EOperation_ETypedElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EPackage_ENamedElement, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_ETypedElement_ENamedElement, gen_ecore_EGenericType_EObject, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)