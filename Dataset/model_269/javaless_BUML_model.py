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
javaless_EAttribute = Class(name="javaless::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
javaless_EClass = Class(name="javaless::EClass")
EClassifier = Class(name="EClassifier")
javaless_EDataType = Class(name="javaless::EDataType")
javaless_EAnnotation = Class(name="javaless::EAnnotation")
EModelElement = Class(name="EModelElement")
javaless_EStringToStringMapEntry = Class(name="javaless::EStringToStringMapEntry")
javaless_EModelElement = Class(name="javaless::EModelElement", is_abstract=True)
javaless_EObject = Class(name="javaless::EObject")
javaless_EReference = Class(name="javaless::EReference")
javaless_EOperation = Class(name="javaless::EOperation")
javaless_EClassifier = Class(name="javaless::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
javaless_EStructuralFeature = Class(name="javaless::EStructuralFeature", is_abstract=True)
javaless_EPackage = Class(name="javaless::EPackage")
javaless_EEnum = Class(name="javaless::EEnum")
EDataType = Class(name="EDataType")
javaless_EEnumLiteral = Class(name="javaless::EEnumLiteral")
EObject = Class(name="EObject")
javaless_ENamedElement = Class(name="javaless::ENamedElement", is_abstract=True)
javaless_EFactory = Class(name="javaless::EFactory")
ETypedElement = Class(name="ETypedElement")
javaless_EParameter = Class(name="javaless::EParameter")
javaless_ETypedElement = Class(name="javaless::ETypedElement", is_abstract=True)

# javaless_EAttribute class attributes and methods
javaless_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
javaless_EAttribute.attributes={javaless_EAttribute_iD}

# EStructuralFeature class attributes and methods

# javaless_EClass class attributes and methods
javaless_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
javaless_EClass_interface: Property = Property(name="interface", type=BooleanType)
javaless_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
javaless_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
javaless_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
javaless_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
javaless_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
javaless_EClass.attributes={javaless_EClass_abstract, javaless_EClass_interface}
javaless_EClass.methods={javaless_EClass_m_getEStructuralFeature, javaless_EClass_m_isSuperTypeOf, javaless_EClass_m_getEStructuralFeature, javaless_EClass_m_getFeatureCount, javaless_EClass_m_getFeatureID}

# EClassifier class attributes and methods

# javaless_EDataType class attributes and methods
javaless_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
javaless_EDataType.attributes={javaless_EDataType_serializable}

# javaless_EAnnotation class attributes and methods
javaless_EAnnotation_source: Property = Property(name="source", type=StringType)
javaless_EAnnotation.attributes={javaless_EAnnotation_source}

# EModelElement class attributes and methods

# javaless_EStringToStringMapEntry class attributes and methods
javaless_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
javaless_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
javaless_EStringToStringMapEntry.attributes={javaless_EStringToStringMapEntry_value, javaless_EStringToStringMapEntry_key}

# javaless_EModelElement class attributes and methods
javaless_EModelElement_m_getEAnnotation: Method = Method(name="getEAnnotation", parameters={Parameter(name='source')}, type=StringType)
javaless_EModelElement.methods={javaless_EModelElement_m_getEAnnotation}

# javaless_EObject class attributes and methods
javaless_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
javaless_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
javaless_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
javaless_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
javaless_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
javaless_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=EObject)
javaless_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
javaless_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
javaless_EObject_m_eContents: Method = Method(name="eContents", parameters={}, type=StringType)
javaless_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={}, type=StringType)
javaless_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={}, type=StringType)
javaless_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
javaless_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
javaless_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
javaless_EObject.methods={javaless_EObject_m_eContainmentFeature, javaless_EObject_m_eCrossReferences, javaless_EObject_m_eContents, javaless_EObject_m_eAllContents, javaless_EObject_m_eSet, javaless_EObject_m_eResource, javaless_EObject_m_eIsSet, javaless_EObject_m_eIsProxy, javaless_EObject_m_eUnset, javaless_EObject_m_eGet, javaless_EObject_m_eContainingFeature, javaless_EObject_m_eClass, javaless_EObject_m_eContainer, javaless_EObject_m_eGet}

# javaless_EReference class attributes and methods
javaless_EReference_containment: Property = Property(name="containment", type=BooleanType)
javaless_EReference_container: Property = Property(name="container", type=BooleanType)
javaless_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
javaless_EReference.attributes={javaless_EReference_resolveProxies, javaless_EReference_containment, javaless_EReference_container}

# javaless_EOperation class attributes and methods

# javaless_EClassifier class attributes and methods
javaless_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
javaless_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
javaless_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
javaless_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
javaless_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
javaless_EClassifier.attributes={javaless_EClassifier_instanceClass, javaless_EClassifier_instanceClassName, javaless_EClassifier_defaultValue}
javaless_EClassifier.methods={javaless_EClassifier_m_isInstance, javaless_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# javaless_EStructuralFeature class attributes and methods
javaless_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
javaless_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
javaless_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
javaless_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
javaless_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
javaless_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
javaless_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
javaless_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
javaless_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={}, type=StringType)
javaless_EStructuralFeature.attributes={javaless_EStructuralFeature_defaultValueLiteral, javaless_EStructuralFeature_changeable, javaless_EStructuralFeature_defaultValue, javaless_EStructuralFeature_unsettable, javaless_EStructuralFeature_volatile, javaless_EStructuralFeature_transient, javaless_EStructuralFeature_derived}
javaless_EStructuralFeature.methods={javaless_EStructuralFeature_m_getFeatureID, javaless_EStructuralFeature_m_getContainerClass}

# javaless_EPackage class attributes and methods
javaless_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
javaless_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
javaless_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
javaless_EPackage.attributes={javaless_EPackage_nsURI, javaless_EPackage_nsPrefix}
javaless_EPackage.methods={javaless_EPackage_m_getEClassifier}

# javaless_EEnum class attributes and methods
javaless_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
javaless_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
javaless_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
javaless_EEnum.methods={javaless_EEnum_m_getEEnumLiteral, javaless_EEnum_m_getEEnumLiteralByLiteral, javaless_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# javaless_EEnumLiteral class attributes and methods
javaless_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
javaless_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
javaless_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
javaless_EEnumLiteral.attributes={javaless_EEnumLiteral_value, javaless_EEnumLiteral_literal, javaless_EEnumLiteral_instance}

# EObject class attributes and methods

# javaless_ENamedElement class attributes and methods
javaless_ENamedElement_name: Property = Property(name="name", type=StringType)
javaless_ENamedElement.attributes={javaless_ENamedElement_name}

# javaless_EFactory class attributes and methods
javaless_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
javaless_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='literalValue'), Parameter(name='eDataType')}, type=StringType)
javaless_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='instanceValue'), Parameter(name='eDataType')}, type=StringType)
javaless_EFactory.methods={javaless_EFactory_m_convertToString, javaless_EFactory_m_createFromString, javaless_EFactory_m_create}

# ETypedElement class attributes and methods

# javaless_EParameter class attributes and methods

# javaless_ETypedElement class attributes and methods
javaless_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
javaless_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
javaless_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
javaless_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
javaless_ETypedElement_many: Property = Property(name="many", type=BooleanType)
javaless_ETypedElement_required: Property = Property(name="required", type=BooleanType)
javaless_ETypedElement.attributes={javaless_ETypedElement_many, javaless_ETypedElement_required, javaless_ETypedElement_upperBound, javaless_ETypedElement_ordered, javaless_ETypedElement_unique, javaless_ETypedElement_lowerBound}

# Relationships
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="javaless_EObject", type=javaless_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EAnnotation4", type=javaless_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="javaless_EObject7", type=javaless_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EAnnotation6", type=javaless_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="javaless_EDataType", type=javaless_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EAttribute", type=javaless_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
details1: BinaryAssociation = BinaryAssociation(
    name="details1",
    ends={
        Property(name="javaless_EStringToStringMapEntry", type=javaless_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EAnnotation", type=javaless_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eModelElement2: BinaryAssociation = BinaryAssociation(
    name="eModelElement2",
    ends={
        Property(name="EModelElement", type=javaless_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=javaless_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
eAllReferences14: BinaryAssociation = BinaryAssociation(
    name="eAllReferences14",
    ends={
        Property(name="javaless_EReference", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass15", type=javaless_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences16: BinaryAssociation = BinaryAssociation(
    name="eReferences16",
    ends={
        Property(name="javaless_EReference18", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass17", type=javaless_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes19: BinaryAssociation = BinaryAssociation(
    name="eAttributes19",
    ends={
        Property(name="javaless_EAttribute21", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass20", type=javaless_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments22: BinaryAssociation = BinaryAssociation(
    name="eAllContainments22",
    ends={
        Property(name="javaless_EReference24", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass23", type=javaless_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes9: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes9",
    ends={
        Property(name="javaless_EClass", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass8", type=javaless_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations10: BinaryAssociation = BinaryAssociation(
    name="eOperations10",
    ends={
        Property(name="EOperation", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=javaless_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes11: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes11",
    ends={
        Property(name="javaless_EAttribute13", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass12", type=javaless_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="javaless_EAttribute34", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass33", type=javaless_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="EStructuralFeature", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass36", type=javaless_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="javaless_EOperation", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass26", type=javaless_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures27: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures27",
    ends={
        Property(name="javaless_EStructuralFeature", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass28", type=javaless_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes30: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes30",
    ends={
        Property(name="javaless_EClass31", type=javaless_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EClass29", type=javaless_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage37: BinaryAssociation = BinaryAssociation(
    name="ePackage37",
    ends={
        Property(name="EPackage", type=javaless_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=javaless_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eLiterals38: BinaryAssociation = BinaryAssociation(
    name="eLiterals38",
    ends={
        Property(name="EEnumLiteral", type=javaless_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=javaless_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage40: BinaryAssociation = BinaryAssociation(
    name="ePackage40",
    ends={
        Property(name="eFactoryInstance", type=javaless_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="EPackage41", type=javaless_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations42: BinaryAssociation = BinaryAssociation(
    name="eAnnotations42",
    ends={
        Property(name="EAnnotation", type=javaless_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=javaless_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum39: BinaryAssociation = BinaryAssociation(
    name="eEnum39",
    ends={
        Property(name="EEnum", type=javaless_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=javaless_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass43: BinaryAssociation = BinaryAssociation(
    name="eContainingClass43",
    ends={
        Property(name="EClass", type=javaless_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=javaless_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eParameters44: BinaryAssociation = BinaryAssociation(
    name="eParameters44",
    ends={
        Property(name="EParameter", type=javaless_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=javaless_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions45: BinaryAssociation = BinaryAssociation(
    name="eExceptions45",
    ends={
        Property(name="javaless_EClassifier", type=javaless_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EOperation46", type=javaless_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eClassifiers48: BinaryAssociation = BinaryAssociation(
    name="eClassifiers48",
    ends={
        Property(name="ePackage49", type=javaless_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="EClassifier", type=javaless_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eSubpackages51: BinaryAssociation = BinaryAssociation(
    name="eSubpackages51",
    ends={
        Property(name="EPackage52", type=javaless_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=javaless_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage54: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage54",
    ends={
        Property(name="EPackage55", type=javaless_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=javaless_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation56: BinaryAssociation = BinaryAssociation(
    name="eOperation56",
    ends={
        Property(name="EOperation57", type=javaless_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=javaless_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eFactoryInstance47: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance47",
    ends={
        Property(name="EFactory", type=javaless_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=javaless_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eContainingClass64: BinaryAssociation = BinaryAssociation(
    name="eContainingClass64",
    ends={
        Property(name="EClass65", type=javaless_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=javaless_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite59: BinaryAssociation = BinaryAssociation(
    name="eOpposite59",
    ends={
        Property(name="javaless_EReference60", type=javaless_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EReference58", type=javaless_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType61: BinaryAssociation = BinaryAssociation(
    name="eReferenceType61",
    ends={
        Property(name="javaless_EClass63", type=javaless_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_EReference62", type=javaless_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eType66: BinaryAssociation = BinaryAssociation(
    name="eType66",
    ends={
        Property(name="javaless_EClassifier67", type=javaless_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="javaless_ETypedElement", type=javaless_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_javaless_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=javaless_EAttribute)
gen_javaless_EClass_EClassifier = Generalization(general=EClassifier, specific=javaless_EClass)
gen_javaless_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=javaless_EAnnotation)
gen_javaless_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=javaless_EClassifier)
gen_javaless_EDataType_EClassifier = Generalization(general=EClassifier, specific=javaless_EDataType)
gen_javaless_EEnum_EDataType = Generalization(general=EDataType, specific=javaless_EEnum)
gen_javaless_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=javaless_EEnumLiteral)
gen_javaless_EModelElement_EObject = Generalization(general=EObject, specific=javaless_EModelElement)
gen_javaless_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=javaless_ENamedElement)
gen_javaless_EFactory_EModelElement = Generalization(general=EModelElement, specific=javaless_EFactory)
gen_javaless_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=javaless_EOperation)
gen_javaless_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=javaless_EParameter)
gen_javaless_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=javaless_EReference)
gen_javaless_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=javaless_EPackage)
gen_javaless_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=javaless_ETypedElement)
gen_javaless_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=javaless_EStructuralFeature)

# Domain Model
domain_model = DomainModel(
    name="javaless",
    types={javaless_EAttribute, EStructuralFeature, javaless_EClass, EClassifier, javaless_EDataType, javaless_EAnnotation, EModelElement, javaless_EStringToStringMapEntry, javaless_EModelElement, javaless_EObject, javaless_EReference, javaless_EOperation, javaless_EClassifier, ENamedElement, javaless_EStructuralFeature, javaless_EPackage, javaless_EEnum, EDataType, javaless_EEnumLiteral, EObject, javaless_ENamedElement, javaless_EFactory, ETypedElement, javaless_EParameter, javaless_ETypedElement},
    associations={contents3, references5, eAttributeType0, details1, eModelElement2, eAllReferences14, eReferences16, eAttributes19, eAllContainments22, eSuperTypes9, eOperations10, eAllAttributes11, eIDAttribute32, eStructuralFeatures35, eAllOperations25, eAllStructuralFeatures27, eAllSuperTypes30, ePackage37, eLiterals38, ePackage40, eAnnotations42, eEnum39, eContainingClass43, eParameters44, eExceptions45, eClassifiers48, eSubpackages51, eSuperPackage54, eOperation56, eFactoryInstance47, eContainingClass64, eOpposite59, eReferenceType61, eType66},
    generalizations={gen_javaless_EAttribute_EStructuralFeature, gen_javaless_EClass_EClassifier, gen_javaless_EAnnotation_EModelElement, gen_javaless_EClassifier_ENamedElement, gen_javaless_EDataType_EClassifier, gen_javaless_EEnum_EDataType, gen_javaless_EEnumLiteral_ENamedElement, gen_javaless_EModelElement_EObject, gen_javaless_ENamedElement_EModelElement, gen_javaless_EFactory_EModelElement, gen_javaless_EOperation_ETypedElement, gen_javaless_EParameter_ETypedElement, gen_javaless_EReference_EStructuralFeature, gen_javaless_EPackage_ENamedElement, gen_javaless_ETypedElement_ENamedElement, gen_javaless_EStructuralFeature_ETypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)