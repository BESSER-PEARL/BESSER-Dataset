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
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EObject = Class(name="ecore::EObject")
EObject = Class(name="EObject")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EAttribute = Class(name="ecore::EAttribute")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EReference = Class(name="ecore::EReference")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_EPackage = Class(name="ecore::EPackage")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EClassifier_Wildcard = Class(name="ecore::EClassifier::Wildcard")
ETypedElement = Class(name="ETypedElement")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)
ecore_EStructuralFeature_Wildcard = Class(name="ecore::EStructuralFeature::Wildcard")
EStructuralFeature = Class(name="EStructuralFeature")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=StringType)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=StringType)
ecore_EClass.attributes={ecore_EClass_interface, ecore_EClass_abstract}
ecore_EClass.methods={ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getFeatureID, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getFeatureCount}

# EClassifier class attributes and methods

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_value, ecore_EStringToStringMapEntry_key}

# ecore_EObject class attributes and methods
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=EObject)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=StringType)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={}, type=StringType)
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={}, type=StringType)
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
ecore_EObject.methods={ecore_EObject_m_eAllContents, ecore_EObject_m_eResource, ecore_EObject_m_eClass, ecore_EObject_m_eGet, ecore_EObject_m_eUnset, ecore_EObject_m_eIsProxy, ecore_EObject_m_eIsSet, ecore_EObject_m_eGet, ecore_EObject_m_eContainer, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eContents, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eSet, ecore_EObject_m_eContainmentFeature}

# EObject class attributes and methods

# ecore_EOperation class attributes and methods

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={}, type=StringType)
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_transient, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_derived}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureID}

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_container, ecore_EReference_resolveProxies, ecore_EReference_containment}

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceTypeName, ecore_EClassifier_instanceClass}
ecore_EClassifier.methods={ecore_EClassifier_m_isInstance, ecore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# ecore_EGenericType class attributes and methods

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsURI, ecore_EPackage_nsPrefix}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_ETypeParameter class attributes and methods

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=EObject)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='eDataType'), Parameter(name='literalValue')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_convertToString, ecore_EFactory_m_create, ecore_EFactory_m_createFromString}

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EClassifier_Wildcard class attributes and methods

# ETypedElement class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement.attributes={ecore_ETypedElement_lowerBound, ecore_ETypedElement_upperBound, ecore_ETypedElement_ordered, ecore_ETypedElement_many, ecore_ETypedElement_unique, ecore_ETypedElement_required}

# ecore_EStructuralFeature_Wildcard class attributes and methods

# EStructuralFeature class attributes and methods

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
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_instance, ecore_EEnumLiteral_literal, ecore_EEnumLiteral_value}

# Relationships
eModelElement0: BinaryAssociation = BinaryAssociation(
    name="eModelElement0",
    ends={
        Property(name="EModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="ecore_EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents2: BinaryAssociation = BinaryAssociation(
    name="contents2",
    ends={
        Property(name="ecore_EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation3", type=ecore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references4: BinaryAssociation = BinaryAssociation(
    name="references4",
    ends={
        Property(name="ecore_EObject6", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation5", type=ecore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAnnotations7: BinaryAssociation = BinaryAssociation(
    name="eAnnotations7",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="ecore_EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass8", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes11: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes11",
    ends={
        Property(name="ecore_EAttribute", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass12", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eStructuralFeatures13: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures13",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass14", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllReferences15: BinaryAssociation = BinaryAssociation(
    name="eAllReferences15",
    ends={
        Property(name="ecore_EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass16", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllGenericSuperTypes38: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes38",
    ends={
        Property(name="ecore_EGenericType40", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass39", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences17: BinaryAssociation = BinaryAssociation(
    name="eReferences17",
    ends={
        Property(name="ecore_EReference19", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass18", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes20: BinaryAssociation = BinaryAssociation(
    name="eAttributes20",
    ends={
        Property(name="ecore_EAttribute22", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass21", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments23: BinaryAssociation = BinaryAssociation(
    name="eAllContainments23",
    ends={
        Property(name="ecore_EReference25", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass24", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations26: BinaryAssociation = BinaryAssociation(
    name="eAllOperations26",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass27", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures28: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures28",
    ends={
        Property(name="ecore_EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass29", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes31: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes31",
    ends={
        Property(name="ecore_EClass32", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass30", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute33: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute33",
    ends={
        Property(name="ecore_EAttribute35", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass34", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eGenericSuperTypes36: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes36",
    ends={
        Property(name="ecore_EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass37", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeParameters42: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters42",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage41: BinaryAssociation = BinaryAssociation(
    name="ePackage41",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eSuperPackage48: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage48",
    ends={
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1)),
        Property(name="EPackage49", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers50: BinaryAssociation = BinaryAssociation(
    name="eClassifiers50",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage51", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance43: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance43",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eSubpackages45: BinaryAssociation = BinaryAssociation(
    name="eSubpackages45",
    ends={
        Property(name="EPackage46", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eBounds54: BinaryAssociation = BinaryAssociation(
    name="eBounds54",
    ends={
        Property(name="ecore_EGenericType56", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter55", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage52: BinaryAssociation = BinaryAssociation(
    name="ePackage52",
    ends={
        Property(name="EPackage53", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eClassifier72: BinaryAssociation = BinaryAssociation(
    name="eClassifier72",
    ends={
        Property(name="ecore_EClassifier74", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType73", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eUpperBound58: BinaryAssociation = BinaryAssociation(
    name="eUpperBound58",
    ends={
        Property(name="ecore_EGenericType59", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType57", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments61: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments61",
    ends={
        Property(name="ecore_EGenericType62", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType60", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType63: BinaryAssociation = BinaryAssociation(
    name="eRawType63",
    ends={
        Property(name="ecore_EClassifier65", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType64", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound67: BinaryAssociation = BinaryAssociation(
    name="eLowerBound67",
    ends={
        Property(name="ecore_EGenericType68", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType66", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter69: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter69",
    ends={
        Property(name="ecore_ETypeParameter71", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType70", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eGenericExceptions82: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions82",
    ends={
        Property(name="ecore_EGenericType84", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation83", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass85: BinaryAssociation = BinaryAssociation(
    name="eContainingClass85",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters75: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters75",
    ends={
        Property(name="ecore_ETypeParameter77", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation76", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters78: BinaryAssociation = BinaryAssociation(
    name="eParameters78",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions79: BinaryAssociation = BinaryAssociation(
    name="eExceptions79",
    ends={
        Property(name="ecore_EClassifier81", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation80", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericType88: BinaryAssociation = BinaryAssociation(
    name="eGenericType88",
    ends={
        Property(name="ecore_EGenericType90", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement89", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eOperation91: BinaryAssociation = BinaryAssociation(
    name="eOperation91",
    ends={
        Property(name="EOperation92", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eType86: BinaryAssociation = BinaryAssociation(
    name="eType86",
    ends={
        Property(name="ecore_EClassifier87", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eAttributeType93: BinaryAssociation = BinaryAssociation(
    name="eAttributeType93",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute94", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eContainingClass95: BinaryAssociation = BinaryAssociation(
    name="eContainingClass95",
    ends={
        Property(name="EClass96", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite98: BinaryAssociation = BinaryAssociation(
    name="eOpposite98",
    ends={
        Property(name="ecore_EReference99", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference97", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType100: BinaryAssociation = BinaryAssociation(
    name="eReferenceType100",
    ends={
        Property(name="ecore_EClass102", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference101", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys103: BinaryAssociation = BinaryAssociation(
    name="eKeys103",
    ends={
        Property(name="ecore_EAttribute105", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference104", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
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
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EModelElement_EObject = Generalization(general=EObject, specific=ecore_EModelElement)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)
gen_ecore_EGenericType_EObject = Generalization(general=EObject, specific=ecore_EGenericType)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAnnotation, EModelElement, ecore_EModelElement, ecore_EClass, EClassifier, ecore_EStringToStringMapEntry, ecore_EObject, EObject, ecore_EOperation, ecore_EAttribute, ecore_EStructuralFeature, ecore_EReference, ecore_EClassifier, ENamedElement, ecore_EGenericType, ecore_ENamedElement, ecore_EPackage, ecore_ETypeParameter, ecore_EFactory, ecore_EDataType, ecore_EClassifier_Wildcard, ETypedElement, ecore_EParameter, ecore_ETypedElement, ecore_EStructuralFeature_Wildcard, EStructuralFeature, ecore_EEnum, EDataType, ecore_EEnumLiteral},
    associations={eModelElement0, details1, contents2, references4, eAnnotations7, eSuperTypes9, eOperations10, eAllAttributes11, eStructuralFeatures13, eAllReferences15, eAllGenericSuperTypes38, eReferences17, eAttributes20, eAllContainments23, eAllOperations26, eAllStructuralFeatures28, eAllSuperTypes31, eIDAttribute33, eGenericSuperTypes36, eTypeParameters42, ePackage41, eSuperPackage48, eClassifiers50, eFactoryInstance43, eSubpackages45, eBounds54, ePackage52, eClassifier72, eUpperBound58, eTypeArguments61, eRawType63, eLowerBound67, eTypeParameter69, eGenericExceptions82, eContainingClass85, eTypeParameters75, eParameters78, eExceptions79, eGenericType88, eOperation91, eType86, eAttributeType93, eContainingClass95, eOpposite98, eReferenceType100, eKeys103, eLiterals106, eEnum107},
    generalizations={gen_ecore_EAnnotation_EModelElement, gen_ecore_EClass_EClassifier, gen_ecore_EModelElement_EObject, gen_ecore_EClassifier_ENamedElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EFactory_EModelElement, gen_ecore_EPackage_ENamedElement, gen_ecore_ETypeParameter_ENamedElement, gen_ecore_EGenericType_EObject, gen_ecore_EDataType_EClassifier, gen_ecore_EOperation_ETypedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_EEnum_EDataType, gen_ecore_EReference_EStructuralFeature, gen_ecore_EEnumLiteral_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)