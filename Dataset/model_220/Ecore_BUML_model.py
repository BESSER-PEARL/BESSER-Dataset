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
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EObject = Class(name="ecore::EObject")
ecore_EAttribute = Class(name="ecore::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EReference = Class(name="ecore::EReference")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EPackage = Class(name="ecore::EPackage")
EObject = Class(name="EObject")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_EParameter = Class(name="ecore::EParameter")
ETypedElement = Class(name="ETypedElement")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_key, ecore_EStringToStringMapEntry_value}

# ecore_EObject class attributes and methods
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={})
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=EObject)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='resolve'), Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='feature'), Parameter(name='newValue')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject.methods={ecore_EObject_m_eGet, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eIsSet, ecore_EObject_m_eClass, ecore_EObject_m_eContainer, ecore_EObject_m_eResource, ecore_EObject_m_eContents, ecore_EObject_m_eAllContents, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eGet, ecore_EObject_m_eSet, ecore_EObject_m_eUnset, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eIsProxy}

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# EStructuralFeature class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass.attributes={ecore_EClass_interface, ecore_EClass_abstract}
ecore_EClass.methods={ecore_EClass_m_getFeatureCount, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getFeatureID}

# EClassifier class attributes and methods

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_resolveProxies, ecore_EReference_container, ecore_EReference_containment}

# ecore_EOperation class attributes and methods

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_transient}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureID}

# ecore_EGenericType class attributes and methods

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceTypeName, ecore_EClassifier_instanceClass}
ecore_EClassifier.methods={ecore_EClassifier_m_isInstance, ecore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# ecore_ETypeParameter class attributes and methods

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteralByLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsURI}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# EObject class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_instance, ecore_EEnumLiteral_value, ecore_EEnumLiteral_literal}

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='eDataType'), Parameter(name='instanceValue')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_convertToString, ecore_EFactory_m_createFromString, ecore_EFactory_m_create}

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EParameter class attributes and methods

# ETypedElement class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement.attributes={ecore_ETypedElement_lowerBound, ecore_ETypedElement_ordered, ecore_ETypedElement_unique, ecore_ETypedElement_required, ecore_ETypedElement_upperBound, ecore_ETypedElement_many}

# Relationships
eModelElement6: BinaryAssociation = BinaryAssociation(
    name="eModelElement6",
    ends={
        Property(name="EModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
details0: BinaryAssociation = BinaryAssociation(
    name="details0",
    ends={
        Property(name="ecore_EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents1: BinaryAssociation = BinaryAssociation(
    name="contents1",
    ends={
        Property(name="ecore_EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation2", type=ecore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references3: BinaryAssociation = BinaryAssociation(
    name="references3",
    ends={
        Property(name="ecore_EObject5", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation4", type=ecore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributeType7: BinaryAssociation = BinaryAssociation(
    name="eAttributeType7",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eAllAttributes12: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes12",
    ends={
        Property(name="ecore_EAttribute14", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass13", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments15: BinaryAssociation = BinaryAssociation(
    name="eAllContainments15",
    ends={
        Property(name="ecore_EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass16", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations8: BinaryAssociation = BinaryAssociation(
    name="eOperations8",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eStructuralFeatures9: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures9",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass10", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes11: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes11",
    ends={
        Property(name="ecore_EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllSuperTypes28: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes28",
    ends={
        Property(name="ecore_EClass29", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass27", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eAllGenericSuperTypes17: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes17",
    ends={
        Property(name="ecore_EGenericType19", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass18", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations20: BinaryAssociation = BinaryAssociation(
    name="eAllOperations20",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass21", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences22: BinaryAssociation = BinaryAssociation(
    name="eAllReferences22",
    ends={
        Property(name="ecore_EReference24", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass23", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures25: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures25",
    ends={
        Property(name="ecore_EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes30: BinaryAssociation = BinaryAssociation(
    name="eAttributes30",
    ends={
        Property(name="ecore_EAttribute32", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass31", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute33: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute33",
    ends={
        Property(name="ecore_EAttribute35", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass34", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eReferences36: BinaryAssociation = BinaryAssociation(
    name="eReferences36",
    ends={
        Property(name="ecore_EReference38", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass37", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes40: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes40",
    ends={
        Property(name="ecore_EClass41", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass39", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eTypeParameters42: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters42",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage43: BinaryAssociation = BinaryAssociation(
    name="ePackage43",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage47", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eLiterals44: BinaryAssociation = BinaryAssociation(
    name="eLiterals44",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum45: BinaryAssociation = BinaryAssociation(
    name="eEnum45",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eUpperBound49: BinaryAssociation = BinaryAssociation(
    name="eUpperBound49",
    ends={
        Property(name="ecore_EGenericType50", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType48", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments52: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments52",
    ends={
        Property(name="ecore_EGenericType53", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType51", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLowerBound55: BinaryAssociation = BinaryAssociation(
    name="eLowerBound55",
    ends={
        Property(name="ecore_EGenericType56", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType54", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eClassifier57: BinaryAssociation = BinaryAssociation(
    name="eClassifier57",
    ends={
        Property(name="ecore_EClassifier59", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType58", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eRawType60: BinaryAssociation = BinaryAssociation(
    name="eRawType60",
    ends={
        Property(name="ecore_EClassifier62", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType61", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eTypeParameter63: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter63",
    ends={
        Property(name="ecore_ETypeParameter65", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType64", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations66: BinaryAssociation = BinaryAssociation(
    name="eAnnotations66",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeParameters67: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters67",
    ends={
        Property(name="ecore_ETypeParameter69", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation68", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters70: BinaryAssociation = BinaryAssociation(
    name="eParameters70",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass77: BinaryAssociation = BinaryAssociation(
    name="eContainingClass77",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eGenericExceptions71: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions71",
    ends={
        Property(name="ecore_EGenericType73", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation72", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions74: BinaryAssociation = BinaryAssociation(
    name="eExceptions74",
    ends={
        Property(name="ecore_EClassifier76", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation75", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eClassifiers78: BinaryAssociation = BinaryAssociation(
    name="eClassifiers78",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages80: BinaryAssociation = BinaryAssociation(
    name="eSubpackages80",
    ends={
        Property(name="EPackage81", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance82: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance82",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage83", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eKeys89: BinaryAssociation = BinaryAssociation(
    name="eKeys89",
    ends={
        Property(name="ecore_EAttribute91", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference90", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperPackage85: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage85",
    ends={
        Property(name="EPackage86", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation87: BinaryAssociation = BinaryAssociation(
    name="eOperation87",
    ends={
        Property(name="EOperation88", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite93: BinaryAssociation = BinaryAssociation(
    name="eOpposite93",
    ends={
        Property(name="ecore_EReference94", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference92", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType95: BinaryAssociation = BinaryAssociation(
    name="eReferenceType95",
    ends={
        Property(name="ecore_EClass97", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference96", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eContainingClass98: BinaryAssociation = BinaryAssociation(
    name="eContainingClass98",
    ends={
        Property(name="EClass99", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType100: BinaryAssociation = BinaryAssociation(
    name="eGenericType100",
    ends={
        Property(name="ecore_EGenericType101", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eType102: BinaryAssociation = BinaryAssociation(
    name="eType102",
    ends={
        Property(name="ecore_EClassifier104", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement103", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds105: BinaryAssociation = BinaryAssociation(
    name="eBounds105",
    ends={
        Property(name="ecore_EGenericType107", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter106", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EGenericType_EObject = Generalization(general=EObject, specific=ecore_EGenericType)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_EModelElement_EObject = Generalization(general=EObject, specific=ecore_EModelElement)
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
    types={ecore_EModelElement, ecore_EAnnotation, EModelElement, ecore_EStringToStringMapEntry, ecore_EObject, ecore_EAttribute, EStructuralFeature, ecore_EDataType, ecore_EClass, EClassifier, ecore_EReference, ecore_EOperation, ecore_EStructuralFeature, ecore_EGenericType, ecore_EClassifier, ENamedElement, ecore_ETypeParameter, ecore_EEnum, EDataType, ecore_EPackage, EObject, ecore_EEnumLiteral, ecore_EFactory, ecore_ENamedElement, ecore_EParameter, ETypedElement, ecore_ETypedElement},
    associations={eModelElement6, details0, contents1, references3, eAttributeType7, eAllAttributes12, eAllContainments15, eOperations8, eStructuralFeatures9, eGenericSuperTypes11, eAllSuperTypes28, eAllGenericSuperTypes17, eAllOperations20, eAllReferences22, eAllStructuralFeatures25, eAttributes30, eIDAttribute33, eReferences36, eSuperTypes40, eTypeParameters42, ePackage43, ePackage46, eLiterals44, eEnum45, eUpperBound49, eTypeArguments52, eLowerBound55, eClassifier57, eRawType60, eTypeParameter63, eAnnotations66, eTypeParameters67, eParameters70, eContainingClass77, eGenericExceptions71, eExceptions74, eClassifiers78, eSubpackages80, eFactoryInstance82, eKeys89, eSuperPackage85, eOperation87, eOpposite93, eReferenceType95, eContainingClass98, eGenericType100, eType102, eBounds105},
    generalizations={gen_ecore_EAnnotation_EModelElement, gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EClass_EClassifier, gen_ecore_EClassifier_ENamedElement, gen_ecore_EEnum_EDataType, gen_ecore_EDataType_EClassifier, gen_ecore_EGenericType_EObject, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_EModelElement_EObject, gen_ecore_ENamedElement_EModelElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)