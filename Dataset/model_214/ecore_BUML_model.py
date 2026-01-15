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
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
ecore_EObject = Class(name="ecore::EObject")
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EAttribute = Class(name="ecore::EAttribute")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EReference = Class(name="ecore::EReference")
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_EDataType = Class(name="ecore::EDataType")
EObject = Class(name="EObject")
ecore_EClassifier_Wildcard = Class(name="ecore::EClassifier::Wildcard")
ETypedElement = Class(name="ETypedElement")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)
EStructuralFeature = Class(name="EStructuralFeature")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_EStructuralFeature_Wildcard = Class(name="ecore::EStructuralFeature::Wildcard")

# ecore_EAnnotation class attributes and methods
ecore_EAnnotation_source: Property = Property(name="source", type=StringType)
ecore_EAnnotation.attributes={ecore_EAnnotation_source}

# EModelElement class attributes and methods

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_value, ecore_EStringToStringMapEntry_key}

# ecore_EModelElement class attributes and methods
ecore_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
ecore_EModelElement.methods={ecore_EModelElement_m_getEAnnotation}

# ecore_EObject class attributes and methods
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=StringType)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={}, type=StringType)
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={}, type=StringType)
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='feature'), Parameter(name='newValue')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject.methods={ecore_EObject_m_eGet, ecore_EObject_m_eContents, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eClass, ecore_EObject_m_eAllContents, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eResource, ecore_EObject_m_eGet, ecore_EObject_m_eIsSet, ecore_EObject_m_eSet, ecore_EObject_m_eContainer, ecore_EObject_m_eIsProxy, ecore_EObject_m_eUnset, ecore_EObject_m_eContainmentFeature}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=StringType)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=StringType)
ecore_EClass.attributes={ecore_EClass_interface, ecore_EClass_abstract}
ecore_EClass.methods={ecore_EClass_m_getFeatureID, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getFeatureCount, ecore_EClass_m_isSuperTypeOf}

# EClassifier class attributes and methods

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# ecore_EOperation class attributes and methods

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={}, type=StringType)
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_transient, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_derived}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureID}

# ecore_EReference class attributes and methods
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_resolveProxies, ecore_EReference_container, ecore_EReference_containment}

# ecore_EGenericType class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsURI}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_ETypeParameter class attributes and methods

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier.attributes={ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClass, ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceTypeName}
ecore_EClassifier.methods={ecore_EClassifier_m_getClassifierID, ecore_EClassifier_m_isInstance}

# ENamedElement class attributes and methods

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='literalValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='eDataType'), Parameter(name='instanceValue')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_create, ecore_EFactory_m_convertToString, ecore_EFactory_m_createFromString}

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# EObject class attributes and methods

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
ecore_ETypedElement.attributes={ecore_ETypedElement_many, ecore_ETypedElement_ordered, ecore_ETypedElement_lowerBound, ecore_ETypedElement_required, ecore_ETypedElement_upperBound, ecore_ETypedElement_unique}

# EStructuralFeature class attributes and methods

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteralByLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_literal, ecore_EEnumLiteral_value, ecore_EEnumLiteral_instance}

# ecore_EStructuralFeature_Wildcard class attributes and methods

# Relationships
details0: BinaryAssociation = BinaryAssociation(
    name="details0",
    ends={
        Property(name="ecore_EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
eAllAttributes10: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes10",
    ends={
        Property(name="ecore_EAttribute", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass11", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes8: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes8",
    ends={
        Property(name="ecore_EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass7", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations9: BinaryAssociation = BinaryAssociation(
    name="eOperations9",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="ecore_EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass28", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="ecore_EClass31", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass29", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eStructuralFeatures12: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures12",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass13", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="ecore_EAttribute34", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass33", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="ecore_EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass15", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="ecore_EReference18", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass17", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="ecore_EAttribute21", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass20", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="ecore_EReference24", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass23", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
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
ePackage40: BinaryAssociation = BinaryAssociation(
    name="ePackage40",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters41: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters41",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance42: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance42",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eSubpackages44: BinaryAssociation = BinaryAssociation(
    name="eSubpackages44",
    ends={
        Property(name="EPackage45", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage47: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage47",
    ends={
        Property(name="EPackage48", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
ePackage51: BinaryAssociation = BinaryAssociation(
    name="ePackage51",
    ends={
        Property(name="EPackage52", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers49: BinaryAssociation = BinaryAssociation(
    name="eClassifiers49",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage50", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eBounds53: BinaryAssociation = BinaryAssociation(
    name="eBounds53",
    ends={
        Property(name="ecore_EGenericType55", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter54", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eUpperBound57: BinaryAssociation = BinaryAssociation(
    name="eUpperBound57",
    ends={
        Property(name="ecore_EGenericType58", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType56", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments60: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments60",
    ends={
        Property(name="ecore_EGenericType61", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType59", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType62: BinaryAssociation = BinaryAssociation(
    name="eRawType62",
    ends={
        Property(name="ecore_EClassifier64", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType63", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound66: BinaryAssociation = BinaryAssociation(
    name="eLowerBound66",
    ends={
        Property(name="ecore_EGenericType67", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType65", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter68: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter68",
    ends={
        Property(name="ecore_ETypeParameter70", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType69", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier71: BinaryAssociation = BinaryAssociation(
    name="eClassifier71",
    ends={
        Property(name="ecore_EClassifier73", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType72", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters74: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters74",
    ends={
        Property(name="ecore_ETypeParameter76", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation75", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters77: BinaryAssociation = BinaryAssociation(
    name="eParameters77",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions78: BinaryAssociation = BinaryAssociation(
    name="eExceptions78",
    ends={
        Property(name="ecore_EClassifier80", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation79", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions81: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions81",
    ends={
        Property(name="ecore_EGenericType83", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation82", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass84: BinaryAssociation = BinaryAssociation(
    name="eContainingClass84",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOperation90: BinaryAssociation = BinaryAssociation(
    name="eOperation90",
    ends={
        Property(name="EOperation91", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eAttributeType92: BinaryAssociation = BinaryAssociation(
    name="eAttributeType92",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute93", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eType85: BinaryAssociation = BinaryAssociation(
    name="eType85",
    ends={
        Property(name="ecore_EClassifier86", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType87: BinaryAssociation = BinaryAssociation(
    name="eGenericType87",
    ends={
        Property(name="ecore_EGenericType89", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement88", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eOpposite97: BinaryAssociation = BinaryAssociation(
    name="eOpposite97",
    ends={
        Property(name="ecore_EReference98", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference96", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType99: BinaryAssociation = BinaryAssociation(
    name="eReferenceType99",
    ends={
        Property(name="ecore_EClass101", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference100", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys102: BinaryAssociation = BinaryAssociation(
    name="eKeys102",
    ends={
        Property(name="ecore_EAttribute104", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference103", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eLiterals105: BinaryAssociation = BinaryAssociation(
    name="eLiterals105",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass94: BinaryAssociation = BinaryAssociation(
    name="eContainingClass94",
    ends={
        Property(name="EClass95", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eEnum106: BinaryAssociation = BinaryAssociation(
    name="eEnum106",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations107: BinaryAssociation = BinaryAssociation(
    name="eAnnotations107",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)
gen_ecore_EGenericType_EObject = Generalization(general=EObject, specific=ecore_EGenericType)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EModelElement_EObject = Generalization(general=EObject, specific=ecore_EModelElement)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAnnotation, EModelElement, ecore_EStringToStringMapEntry, ecore_EModelElement, ecore_EObject, ecore_EClass, EClassifier, ecore_EAttribute, ecore_EOperation, ecore_EStructuralFeature, ecore_EReference, ecore_EGenericType, ecore_EPackage, ecore_ETypeParameter, ecore_EClassifier, ENamedElement, ecore_EFactory, ecore_ENamedElement, ecore_EDataType, EObject, ecore_EClassifier_Wildcard, ETypedElement, ecore_EParameter, ecore_ETypedElement, EStructuralFeature, ecore_EEnum, EDataType, ecore_EEnumLiteral, ecore_EStructuralFeature_Wildcard},
    associations={details0, eModelElement1, contents2, references4, eAllAttributes10, eSuperTypes8, eOperations9, eAllStructuralFeatures27, eAllSuperTypes30, eStructuralFeatures12, eIDAttribute32, eAllReferences14, eReferences16, eAttributes19, eAllContainments22, eAllOperations25, eGenericSuperTypes35, eAllGenericSuperTypes37, ePackage40, eTypeParameters41, eFactoryInstance42, eSubpackages44, eSuperPackage47, ePackage51, eClassifiers49, eBounds53, eUpperBound57, eTypeArguments60, eRawType62, eLowerBound66, eTypeParameter68, eClassifier71, eTypeParameters74, eParameters77, eExceptions78, eGenericExceptions81, eContainingClass84, eOperation90, eAttributeType92, eType85, eGenericType87, eOpposite97, eReferenceType99, eKeys102, eLiterals105, eContainingClass94, eEnum106, eAnnotations107},
    generalizations={gen_ecore_EAnnotation_EModelElement, gen_ecore_EClass_EClassifier, gen_ecore_EClassifier_ENamedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EFactory_EModelElement, gen_ecore_EDataType_EClassifier, gen_ecore_ETypeParameter_ENamedElement, gen_ecore_EGenericType_EObject, gen_ecore_EOperation_ETypedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EEnum_EDataType, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EModelElement_EObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)