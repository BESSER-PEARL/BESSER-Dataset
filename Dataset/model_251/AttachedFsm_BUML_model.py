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
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
ecore_EObject = Class(name="ecore::EObject")
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
FSM = Class(name="FSM")
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EReference = Class(name="ecore::EReference")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_FSM = Class(name="ecore::FSM")
ETypedElement = Class(name="ETypedElement")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)
ecore_State = Class(name="ecore::State")
ecore_Transition = Class(name="ecore::Transition")

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# EStructuralFeature class attributes and methods

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
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
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
ecore_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='operation'), Parameter(name='arguments')}, type=StringType)
ecore_EObject.methods={ecore_EObject_m_eGet, ecore_EObject_m_eIsSet, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eInvoke, ecore_EObject_m_eClass, ecore_EObject_m_eResource, ecore_EObject_m_eSet, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eAllContents, ecore_EObject_m_eContainer, ecore_EObject_m_eContents, ecore_EObject_m_eGet, ecore_EObject_m_eUnset, ecore_EObject_m_eIsProxy}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecore_EClass_m_getOperationCount: Method = Method(name="getOperationCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEOperation: Method = Method(name="getEOperation", parameters={Parameter(name='operationID')}, type=StringType)
ecore_EClass_m_getOperationID: Method = Method(name="getOperationID", parameters={Parameter(name='operation')}, type=IntegerType)
ecore_EClass_m_getOverride: Method = Method(name="getOverride", parameters={Parameter(name='operation')}, type=StringType)
ecore_EClass_m_getFeatureType: Method = Method(name="getFeatureType", parameters={Parameter(name='feature')}, type=StringType)
ecore_EClass.attributes={ecore_EClass_abstract, ecore_EClass_interface}
ecore_EClass.methods={ecore_EClass_m_getFeatureType, ecore_EClass_m_getFeatureID, ecore_EClass_m_getEOperation, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getOperationID, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getFeatureCount, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getOverride, ecore_EClass_m_getOperationCount}

# EClassifier class attributes and methods

# FSM class attributes and methods

# ecore_EDataType class attributes and methods
ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
ecore_EDataType.attributes={ecore_EDataType_serializable}

# ecore_EOperation class attributes and methods
ecore_EOperation_m_getOperationID: Method = Method(name="getOperationID", parameters={}, type=IntegerType)
ecore_EOperation_m_isOverrideOf: Method = Method(name="isOverrideOf", parameters={Parameter(name='someOperation')}, type=BooleanType)
ecore_EOperation.methods={ecore_EOperation_m_isOverrideOf, ecore_EOperation_m_getOperationID}

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_containment, ecore_EReference_resolveProxies, ecore_EReference_container}

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_transient, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_volatile}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureID}

# ecore_EGenericType class attributes and methods
ecore_EGenericType_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EGenericType.methods={ecore_EGenericType_m_isInstance}

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceClass, ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceTypeName, ecore_EClassifier_defaultValue}
ecore_EClassifier.methods={ecore_EClassifier_m_isInstance, ecore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsURI, ecore_EPackage_nsPrefix}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_ETypeParameter class attributes and methods

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteralByLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_instance, ecore_EEnumLiteral_value, ecore_EEnumLiteral_literal}

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='literalValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='eDataType'), Parameter(name='instanceValue')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_create, ecore_EFactory_m_convertToString, ecore_EFactory_m_createFromString}

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_FSM class attributes and methods

# ETypedElement class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement.attributes={ecore_ETypedElement_required, ecore_ETypedElement_ordered, ecore_ETypedElement_many, ecore_ETypedElement_upperBound, ecore_ETypedElement_unique, ecore_ETypedElement_lowerBound}

# ecore_State class attributes and methods
ecore_State_name: Property = Property(name="name", type=StringType)
ecore_State.attributes={ecore_State_name}

# ecore_Transition class attributes and methods
ecore_Transition_input: Property = Property(name="input", type=StringType)
ecore_Transition_output: Property = Property(name="output", type=StringType)
ecore_Transition.attributes={ecore_Transition_output, ecore_Transition_input}

# Relationships
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
        Property(name="EModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=ecore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
contents3: BinaryAssociation = BinaryAssociation(
    name="contents3",
    ends={
        Property(name="ecore_EObject", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation4", type=ecore_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references5: BinaryAssociation = BinaryAssociation(
    name="references5",
    ends={
        Property(name="ecore_EObject7", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation6", type=ecore_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
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
        Property(name="ecore_EAttribute13", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass12", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
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
eIDAttribute32: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute32",
    ends={
        Property(name="ecore_EAttribute34", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass33", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures35: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures35",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass36", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes37: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes37",
    ends={
        Property(name="ecore_EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass38", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes39: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes39",
    ends={
        Property(name="ecore_EGenericType41", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass40", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations25: BinaryAssociation = BinaryAssociation(
    name="eAllOperations25",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage42: BinaryAssociation = BinaryAssociation(
    name="ePackage42",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters43: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters43",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClassifier", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
ePackage46: BinaryAssociation = BinaryAssociation(
    name="ePackage46",
    ends={
        Property(name="EPackage47", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations48: BinaryAssociation = BinaryAssociation(
    name="eAnnotations48",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
myFSMs49: BinaryAssociation = BinaryAssociation(
    name="myFSMs49",
    ends={
        Property(name="ecore_FSM", type=ecore_ENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ENamedElement", type=ecore_FSM, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
eContainingClass50: BinaryAssociation = BinaryAssociation(
    name="eContainingClass50",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eParameters54: BinaryAssociation = BinaryAssociation(
    name="eParameters54",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions55: BinaryAssociation = BinaryAssociation(
    name="eExceptions55",
    ends={
        Property(name="ecore_EClassifier57", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation56", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eGenericExceptions58: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions58",
    ends={
        Property(name="ecore_EGenericType60", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation59", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eFactoryInstance61: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance61",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers62: BinaryAssociation = BinaryAssociation(
    name="eClassifiers62",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage63", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eTypeParameters51: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters51",
    ends={
        Property(name="ecore_ETypeParameter53", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation52", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage68: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage68",
    ends={
        Property(name="EPackage69", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation70: BinaryAssociation = BinaryAssociation(
    name="eOperation70",
    ends={
        Property(name="EOperation71", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite73: BinaryAssociation = BinaryAssociation(
    name="eOpposite73",
    ends={
        Property(name="ecore_EReference74", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference72", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType75: BinaryAssociation = BinaryAssociation(
    name="eReferenceType75",
    ends={
        Property(name="ecore_EClass77", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference76", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys78: BinaryAssociation = BinaryAssociation(
    name="eKeys78",
    ends={
        Property(name="ecore_EAttribute80", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference79", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eSubpackages65: BinaryAssociation = BinaryAssociation(
    name="eSubpackages65",
    ends={
        Property(name="EPackage66", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass81: BinaryAssociation = BinaryAssociation(
    name="eContainingClass81",
    ends={
        Property(name="EClass82", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType83: BinaryAssociation = BinaryAssociation(
    name="eType83",
    ends={
        Property(name="ecore_EClassifier84", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType85: BinaryAssociation = BinaryAssociation(
    name="eGenericType85",
    ends={
        Property(name="ecore_EGenericType87", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement86", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeArguments92: BinaryAssociation = BinaryAssociation(
    name="eTypeArguments92",
    ends={
        Property(name="ecore_EGenericType93", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType91", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eRawType94: BinaryAssociation = BinaryAssociation(
    name="eRawType94",
    ends={
        Property(name="ecore_EClassifier96", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType95", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound98: BinaryAssociation = BinaryAssociation(
    name="eLowerBound98",
    ends={
        Property(name="ecore_EGenericType99", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType97", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter100: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter100",
    ends={
        Property(name="ecore_ETypeParameter102", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType101", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier103: BinaryAssociation = BinaryAssociation(
    name="eClassifier103",
    ends={
        Property(name="ecore_EClassifier105", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType104", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eUpperBound89: BinaryAssociation = BinaryAssociation(
    name="eUpperBound89",
    ends={
        Property(name="ecore_EGenericType90", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType88", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedState109: BinaryAssociation = BinaryAssociation(
    name="ownedState109",
    ends={
        Property(name="State", type=ecore_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=ecore_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState110: BinaryAssociation = BinaryAssociation(
    name="initialState110",
    ends={
        Property(name="ecore_State", type=ecore_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_FSM111", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState112: BinaryAssociation = BinaryAssociation(
    name="finalState112",
    ends={
        Property(name="ecore_State114", type=ecore_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_FSM113", type=ecore_State, multiplicity=Multiplicity(1, 9999))
    }
)
owningFSM115: BinaryAssociation = BinaryAssociation(
    name="owningFSM115",
    ends={
        Property(name="FSM", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=ecore_FSM, multiplicity=Multiplicity(1, 1))
    }
)
eBounds106: BinaryAssociation = BinaryAssociation(
    name="eBounds106",
    ends={
        Property(name="ecore_EGenericType108", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter107", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransition116: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition116",
    ends={
        Property(name="Transition", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ecore_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition117: BinaryAssociation = BinaryAssociation(
    name="incomingTransition117",
    ends={
        Property(name="Transition118", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ecore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
myClasses119: BinaryAssociation = BinaryAssociation(
    name="myClasses119",
    ends={
        Property(name="ecore_EClass121", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_State120", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
source122: BinaryAssociation = BinaryAssociation(
    name="source122",
    ends={
        Property(name="State123", type=ecore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)
target124: BinaryAssociation = BinaryAssociation(
    name="target124",
    ends={
        Property(name="State125", type=ecore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EClass_FSM = Generalization(general=FSM, specific=ecore_EClass)
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
    types={ecore_EAttribute, EStructuralFeature, ecore_EAnnotation, EModelElement, ecore_EStringToStringMapEntry, ecore_EModelElement, ecore_EObject, ecore_EClass, EClassifier, FSM, ecore_EDataType, ecore_EOperation, ecore_EReference, ecore_EStructuralFeature, ecore_EGenericType, ecore_EClassifier, ENamedElement, ecore_EPackage, ecore_ETypeParameter, ecore_EEnum, EDataType, ecore_EEnumLiteral, ecore_EFactory, ecore_ENamedElement, ecore_FSM, ETypedElement, ecore_EParameter, ecore_ETypedElement, ecore_State, ecore_Transition},
    associations={details1, eModelElement2, contents3, references5, eAttributeType0, eSuperTypes9, eOperations10, eAllAttributes11, eAllReferences14, eReferences16, eAttributes19, eAllContainments22, eAllStructuralFeatures27, eAllSuperTypes30, eIDAttribute32, eStructuralFeatures35, eGenericSuperTypes37, eAllGenericSuperTypes39, eAllOperations25, ePackage42, eTypeParameters43, eLiterals44, eEnum45, ePackage46, eAnnotations48, myFSMs49, eContainingClass50, eParameters54, eExceptions55, eGenericExceptions58, eFactoryInstance61, eClassifiers62, eTypeParameters51, eSuperPackage68, eOperation70, eOpposite73, eReferenceType75, eKeys78, eSubpackages65, eContainingClass81, eType83, eGenericType85, eTypeArguments92, eRawType94, eLowerBound98, eTypeParameter100, eClassifier103, eUpperBound89, ownedState109, initialState110, finalState112, owningFSM115, eBounds106, outgoingTransition116, incomingTransition117, myClasses119, source122, target124},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EAnnotation_EModelElement, gen_ecore_EClass_EClassifier, gen_ecore_EClass_FSM, gen_ecore_EClassifier_ENamedElement, gen_ecore_EDataType_EClassifier, gen_ecore_EEnum_EDataType, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)