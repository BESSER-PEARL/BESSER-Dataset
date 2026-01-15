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
ecore_EObject = Class(name="ecore::EObject")
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EGenericType = Class(name="ecore::EGenericType")
ecore_EAnnotation = Class(name="ecore::EAnnotation")
EModelElement = Class(name="EModelElement")
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")
ecore_EModelElement = Class(name="ecore::EModelElement", is_abstract=True)
EDataType = Class(name="EDataType")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_EFactory = Class(name="ecore::EFactory")
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_EDataType = Class(name="ecore::EDataType")
ecore_EEnum = Class(name="ecore::EEnum")
ETypedElement = Class(name="ETypedElement")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ecore_EReference = Class(name="ecore::EReference")
ecore_ETypeParameter = Class(name="ecore::ETypeParameter")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)

# ecore_EAttribute class attributes and methods
ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
ecore_EAttribute.attributes={ecore_EAttribute_iD}

# EStructuralFeature class attributes and methods

# ecore_EObject class attributes and methods
ecore_EObject_m_eContents: Method = Method(name="eContents", parameters={})
ecore_EObject_m_eAllContents: Method = Method(name="eAllContents", parameters={})
ecore_EObject_m_eCrossReferences: Method = Method(name="eCrossReferences", parameters={})
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature')}, type=StringType)
ecore_EObject_m_eGet: Method = Method(name="eGet", parameters={Parameter(name='feature'), Parameter(name='resolve')}, type=StringType)
ecore_EObject_m_eSet: Method = Method(name="eSet", parameters={Parameter(name='newValue'), Parameter(name='feature')})
ecore_EObject_m_eIsSet: Method = Method(name="eIsSet", parameters={Parameter(name='feature')}, type=BooleanType)
ecore_EObject_m_eUnset: Method = Method(name="eUnset", parameters={Parameter(name='feature')})
ecore_EObject_m_eInvoke: Method = Method(name="eInvoke", parameters={Parameter(name='arguments'), Parameter(name='operation')}, type=StringType)
ecore_EObject_m_eClass: Method = Method(name="eClass", parameters={}, type=StringType)
ecore_EObject_m_eIsProxy: Method = Method(name="eIsProxy", parameters={}, type=BooleanType)
ecore_EObject_m_eResource: Method = Method(name="eResource", parameters={}, type=StringType)
ecore_EObject_m_eContainer: Method = Method(name="eContainer", parameters={}, type=StringType)
ecore_EObject_m_eContainingFeature: Method = Method(name="eContainingFeature", parameters={}, type=EStructuralFeature)
ecore_EObject_m_eContainmentFeature: Method = Method(name="eContainmentFeature", parameters={}, type=StringType)
ecore_EObject.methods={ecore_EObject_m_eSet, ecore_EObject_m_eContainmentFeature, ecore_EObject_m_eGet, ecore_EObject_m_eGet, ecore_EObject_m_eContainingFeature, ecore_EObject_m_eContents, ecore_EObject_m_eContainer, ecore_EObject_m_eInvoke, ecore_EObject_m_eIsSet, ecore_EObject_m_eUnset, ecore_EObject_m_eCrossReferences, ecore_EObject_m_eClass, ecore_EObject_m_eResource, ecore_EObject_m_eIsProxy, ecore_EObject_m_eAllContents}

# ecore_EClass class attributes and methods
ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
ecore_EClass.attributes={ecore_EClass_abstract, ecore_EClass_interface}

# EClassifier class attributes and methods

# ecore_EOperation class attributes and methods

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_transient, ecore_EStructuralFeature_defaultValue, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_unsettable}

# ecore_EGenericType class attributes and methods
ecore_EGenericType_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EGenericType.methods={ecore_EGenericType_m_isInstance}

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

# EDataType class attributes and methods

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_literal}

# ecore_EFactory class attributes and methods
ecore_EFactory_m_create: Method = Method(name="create", parameters={Parameter(name='eClass')}, type=StringType)
ecore_EFactory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='literalValue'), Parameter(name='eDataType')}, type=StringType)
ecore_EFactory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='eDataType'), Parameter(name='instanceValue')}, type=StringType)
ecore_EFactory.methods={ecore_EFactory_m_convertToString, ecore_EFactory_m_createFromString, ecore_EFactory_m_create}

# ecore_EClassifier class attributes and methods

# ENamedElement class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsPrefix, ecore_EPackage_nsURI}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_EDataType class attributes and methods

# ecore_EEnum class attributes and methods

# ETypedElement class attributes and methods

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_containment, ecore_EReference_resolveProxies, ecore_EReference_container}

# ecore_ETypeParameter class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement.attributes={ecore_ETypedElement_upperBound, ecore_ETypedElement_ordered, ecore_ETypedElement_lowerBound, ecore_ETypedElement_unique}

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
eStructuralFeatures10: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures10",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass11", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericSuperTypes12: BinaryAssociation = BinaryAssociation(
    name="eGenericSuperTypes12",
    ends={
        Property(name="ecore_EGenericType", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass13", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details0: BinaryAssociation = BinaryAssociation(
    name="details0",
    ends={
        Property(name="ecore_EStringToStringMapEntry", type=ecore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAnnotation", type=ecore_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLiterals18: BinaryAssociation = BinaryAssociation(
    name="eLiterals18",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum19: BinaryAssociation = BinaryAssociation(
    name="eEnum19",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
ePackage20: BinaryAssociation = BinaryAssociation(
    name="ePackage20",
    ends={
        Property(name="EPackage21", type=ecore_EFactory, multiplicity=Multiplicity(1, 1)),
        Property(name="eFactoryInstance", type=ecore_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
eAnnotations22: BinaryAssociation = BinaryAssociation(
    name="eAnnotations22",
    ends={
        Property(name="EAnnotation", type=ecore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=ecore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllGenericSuperTypes14: BinaryAssociation = BinaryAssociation(
    name="eAllGenericSuperTypes14",
    ends={
        Property(name="ecore_EGenericType16", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass15", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage17: BinaryAssociation = BinaryAssociation(
    name="ePackage17",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass23: BinaryAssociation = BinaryAssociation(
    name="eContainingClass23",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eFactoryInstance29: BinaryAssociation = BinaryAssociation(
    name="eFactoryInstance29",
    ends={
        Property(name="EFactory", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EFactory, multiplicity=Multiplicity(1, 1))
    }
)
eClassifiers30: BinaryAssociation = BinaryAssociation(
    name="eClassifiers30",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage31", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages33: BinaryAssociation = BinaryAssociation(
    name="eSubpackages33",
    ends={
        Property(name="EPackage34", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage36: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage36",
    ends={
        Property(name="EPackage37", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation38: BinaryAssociation = BinaryAssociation(
    name="eOperation38",
    ends={
        Property(name="EOperation39", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eTypeParameters24: BinaryAssociation = BinaryAssociation(
    name="eTypeParameters24",
    ends={
        Property(name="ecore_ETypeParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eParameters25: BinaryAssociation = BinaryAssociation(
    name="eParameters25",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eGenericExceptions26: BinaryAssociation = BinaryAssociation(
    name="eGenericExceptions26",
    ends={
        Property(name="ecore_EGenericType28", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation27", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass42: BinaryAssociation = BinaryAssociation(
    name="eContainingClass42",
    ends={
        Property(name="EClass43", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType44: BinaryAssociation = BinaryAssociation(
    name="eType44",
    ends={
        Property(name="ecore_EClassifier", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eGenericType45: BinaryAssociation = BinaryAssociation(
    name="eGenericType45",
    ends={
        Property(name="ecore_EGenericType47", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement46", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eOpposite41: BinaryAssociation = BinaryAssociation(
    name="eOpposite41",
    ends={
        Property(name="ecore_EReference", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference40", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
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
eRawType54: BinaryAssociation = BinaryAssociation(
    name="eRawType54",
    ends={
        Property(name="ecore_EClassifier56", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType55", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1))
    }
)
eLowerBound58: BinaryAssociation = BinaryAssociation(
    name="eLowerBound58",
    ends={
        Property(name="ecore_EGenericType59", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType57", type=ecore_EGenericType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eTypeParameter60: BinaryAssociation = BinaryAssociation(
    name="eTypeParameter60",
    ends={
        Property(name="ecore_ETypeParameter62", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType61", type=ecore_ETypeParameter, multiplicity=Multiplicity(0, 1))
    }
)
eClassifier63: BinaryAssociation = BinaryAssociation(
    name="eClassifier63",
    ends={
        Property(name="ecore_EClassifier65", type=ecore_EGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EGenericType64", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eBounds66: BinaryAssociation = BinaryAssociation(
    name="eBounds66",
    ends={
        Property(name="ecore_EGenericType68", type=ecore_ETypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypeParameter67", type=ecore_EGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=ecore_EAnnotation)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EFactory_EModelElement = Generalization(general=EModelElement, specific=ecore_EFactory)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=ecore_ENamedElement)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)
gen_ecore_ETypeParameter_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypeParameter)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAttribute, EStructuralFeature, ecore_EObject, ecore_EClass, EClassifier, ecore_EOperation, ecore_EStructuralFeature, ecore_EGenericType, ecore_EAnnotation, EModelElement, ecore_EStringToStringMapEntry, ecore_EModelElement, EDataType, ecore_EEnumLiteral, ecore_EFactory, ecore_EClassifier, ENamedElement, ecore_EPackage, ecore_EDataType, ecore_EEnum, ETypedElement, ecore_ENamedElement, ecore_EReference, ecore_ETypeParameter, ecore_EParameter, ecore_ETypedElement},
    associations={eModelElement1, contents2, references4, eSuperTypes8, eOperations9, eStructuralFeatures10, eGenericSuperTypes12, details0, eLiterals18, eEnum19, ePackage20, eAnnotations22, eAllGenericSuperTypes14, ePackage17, eContainingClass23, eFactoryInstance29, eClassifiers30, eSubpackages33, eSuperPackage36, eOperation38, eTypeParameters24, eParameters25, eGenericExceptions26, eContainingClass42, eType44, eGenericType45, eOpposite41, eUpperBound49, eTypeArguments52, eRawType54, eLowerBound58, eTypeParameter60, eClassifier63, eBounds66},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EClass_EClassifier, gen_ecore_EAnnotation_EModelElement, gen_ecore_EEnum_EDataType, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EFactory_EModelElement, gen_ecore_EClassifier_ENamedElement, gen_ecore_EDataType_EClassifier, gen_ecore_EOperation_ETypedElement, gen_ecore_ENamedElement_EModelElement, gen_ecore_EPackage_ENamedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_ETypedElement_ENamedElement, gen_ecore_EStructuralFeature_ETypedElement, gen_ecore_ETypeParameter_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)