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
ecore_EClass = Class(name="ecore::EClass")
EClassifier = Class(name="EClassifier")
ecore_EOperation = Class(name="ecore::EOperation")
ecore_EReference = Class(name="ecore::EReference")
ecore_EEnum = Class(name="ecore::EEnum")
EDataType = Class(name="EDataType")
ecore_EStructuralFeature = Class(name="ecore::EStructuralFeature", is_abstract=True)
ecore_EClassifier = Class(name="ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
ecore_EPackage = Class(name="ecore::EPackage")
ecore_EEnumLiteral = Class(name="ecore::EEnumLiteral")
ecore_ENamedElement = Class(name="ecore::ENamedElement", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
ecore_EParameter = Class(name="ecore::EParameter")
ecore_ETypedElement = Class(name="ecore::ETypedElement", is_abstract=True)
ecore_EStringToStringMapEntry = Class(name="ecore::EStringToStringMapEntry")

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
ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
ecore_EClass.attributes={ecore_EClass_interface, ecore_EClass_abstract}
ecore_EClass.methods={ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_getEStructuralFeature, ecore_EClass_m_isSuperTypeOf, ecore_EClass_m_getFeatureCount, ecore_EClass_m_getFeatureID}

# EClassifier class attributes and methods

# ecore_EOperation class attributes and methods

# ecore_EReference class attributes and methods
ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
ecore_EReference_container: Property = Property(name="container", type=BooleanType)
ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
ecore_EReference.attributes={ecore_EReference_resolveProxies, ecore_EReference_container, ecore_EReference_containment}

# ecore_EEnum class attributes and methods
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
ecore_EEnum.methods={ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteral, ecore_EEnum_m_getEEnumLiteralByLiteral}

# EDataType class attributes and methods

# ecore_EStructuralFeature class attributes and methods
ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
ecore_EStructuralFeature.attributes={ecore_EStructuralFeature_defaultValueLiteral, ecore_EStructuralFeature_changeable, ecore_EStructuralFeature_transient, ecore_EStructuralFeature_unsettable, ecore_EStructuralFeature_volatile, ecore_EStructuralFeature_derived, ecore_EStructuralFeature_defaultValue}
ecore_EStructuralFeature.methods={ecore_EStructuralFeature_m_getContainerClass, ecore_EStructuralFeature_m_getFeatureID}

# ecore_EClassifier class attributes and methods
ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
ecore_EClassifier.attributes={ecore_EClassifier_instanceTypeName, ecore_EClassifier_defaultValue, ecore_EClassifier_instanceClassName, ecore_EClassifier_instanceClass}
ecore_EClassifier.methods={ecore_EClassifier_m_isInstance, ecore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# ecore_EPackage class attributes and methods
ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
ecore_EPackage.attributes={ecore_EPackage_nsURI, ecore_EPackage_nsPrefix}
ecore_EPackage.methods={ecore_EPackage_m_getEClassifier}

# ecore_EEnumLiteral class attributes and methods
ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
ecore_EEnumLiteral.attributes={ecore_EEnumLiteral_literal, ecore_EEnumLiteral_value, ecore_EEnumLiteral_instance}

# ecore_ENamedElement class attributes and methods
ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
ecore_ENamedElement.attributes={ecore_ENamedElement_name}

# ETypedElement class attributes and methods

# ecore_EParameter class attributes and methods

# ecore_ETypedElement class attributes and methods
ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
ecore_ETypedElement.attributes={ecore_ETypedElement_lowerBound, ecore_ETypedElement_unique, ecore_ETypedElement_upperBound, ecore_ETypedElement_many, ecore_ETypedElement_required, ecore_ETypedElement_ordered}

# ecore_EStringToStringMapEntry class attributes and methods
ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
ecore_EStringToStringMapEntry.attributes={ecore_EStringToStringMapEntry_value, ecore_EStringToStringMapEntry_key}

# Relationships
eReferences9: BinaryAssociation = BinaryAssociation(
    name="eReferences9",
    ends={
        Property(name="ecore_EReference11", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass10", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes12: BinaryAssociation = BinaryAssociation(
    name="eAttributes12",
    ends={
        Property(name="ecore_EAttribute14", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass13", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments15: BinaryAssociation = BinaryAssociation(
    name="eAllContainments15",
    ends={
        Property(name="ecore_EReference17", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass16", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="ecore_EDataType", type=ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EAttribute", type=ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eSuperTypes2: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes2",
    ends={
        Property(name="ecore_EClass", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass1", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations3: BinaryAssociation = BinaryAssociation(
    name="eOperations3",
    ends={
        Property(name="EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes4: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes4",
    ends={
        Property(name="ecore_EAttribute6", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass5", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage30: BinaryAssociation = BinaryAssociation(
    name="ePackage30",
    ends={
        Property(name="EPackage", type=ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eAllReferences7: BinaryAssociation = BinaryAssociation(
    name="eAllReferences7",
    ends={
        Property(name="ecore_EReference", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass8", type=ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations18: BinaryAssociation = BinaryAssociation(
    name="eAllOperations18",
    ends={
        Property(name="ecore_EOperation", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass19", type=ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures20: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures20",
    ends={
        Property(name="ecore_EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass21", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes23: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes23",
    ends={
        Property(name="ecore_EClass24", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass22", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute25: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute25",
    ends={
        Property(name="ecore_EAttribute27", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EClass26", type=ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures28: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures28",
    ends={
        Property(name="EStructuralFeature", type=ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass29", type=ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eClassifiers37: BinaryAssociation = BinaryAssociation(
    name="eClassifiers37",
    ends={
        Property(name="EClassifier", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages39: BinaryAssociation = BinaryAssociation(
    name="eSubpackages39",
    ends={
        Property(name="EPackage40", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eLiterals31: BinaryAssociation = BinaryAssociation(
    name="eLiterals31",
    ends={
        Property(name="EEnumLiteral", type=ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum32: BinaryAssociation = BinaryAssociation(
    name="eEnum32",
    ends={
        Property(name="EEnum", type=ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass33: BinaryAssociation = BinaryAssociation(
    name="eContainingClass33",
    ends={
        Property(name="EClass", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eParameters34: BinaryAssociation = BinaryAssociation(
    name="eParameters34",
    ends={
        Property(name="EParameter", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions35: BinaryAssociation = BinaryAssociation(
    name="eExceptions35",
    ends={
        Property(name="ecore_EClassifier", type=ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EOperation36", type=ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eContainingClass55: BinaryAssociation = BinaryAssociation(
    name="eContainingClass55",
    ends={
        Property(name="EClass56", type=ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eSuperPackage42: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage42",
    ends={
        Property(name="EPackage43", type=ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation44: BinaryAssociation = BinaryAssociation(
    name="eOperation44",
    ends={
        Property(name="EOperation45", type=ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite47: BinaryAssociation = BinaryAssociation(
    name="eOpposite47",
    ends={
        Property(name="ecore_EReference48", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference46", type=ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType49: BinaryAssociation = BinaryAssociation(
    name="eReferenceType49",
    ends={
        Property(name="ecore_EClass51", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference50", type=ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys52: BinaryAssociation = BinaryAssociation(
    name="eKeys52",
    ends={
        Property(name="ecore_EAttribute54", type=ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_EReference53", type=ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eType57: BinaryAssociation = BinaryAssociation(
    name="eType57",
    ends={
        Property(name="ecore_EClassifier58", type=ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ETypedElement", type=ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EAttribute)
gen_ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=ecore_EClass)
gen_ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=ecore_EDataType)
gen_ecore_EEnum_EDataType = Generalization(general=EDataType, specific=ecore_EEnum)
gen_ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EClassifier)
gen_ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EEnumLiteral)
gen_ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EOperation)
gen_ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=ecore_EPackage)
gen_ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=ecore_ETypedElement)
gen_ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EParameter)
gen_ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=ecore_EReference)
gen_ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=ecore_EStructuralFeature)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_EAttribute, EStructuralFeature, ecore_EDataType, ecore_EClass, EClassifier, ecore_EOperation, ecore_EReference, ecore_EEnum, EDataType, ecore_EStructuralFeature, ecore_EClassifier, ENamedElement, ecore_EPackage, ecore_EEnumLiteral, ecore_ENamedElement, ETypedElement, ecore_EParameter, ecore_ETypedElement, ecore_EStringToStringMapEntry},
    associations={eReferences9, eAttributes12, eAllContainments15, eAttributeType0, eSuperTypes2, eOperations3, eAllAttributes4, ePackage30, eAllReferences7, eAllOperations18, eAllStructuralFeatures20, eAllSuperTypes23, eIDAttribute25, eStructuralFeatures28, eClassifiers37, eSubpackages39, eLiterals31, eEnum32, eContainingClass33, eParameters34, eExceptions35, eContainingClass55, eSuperPackage42, eOperation44, eOpposite47, eReferenceType49, eKeys52, eType57},
    generalizations={gen_ecore_EAttribute_EStructuralFeature, gen_ecore_EClass_EClassifier, gen_ecore_EDataType_EClassifier, gen_ecore_EEnum_EDataType, gen_ecore_EClassifier_ENamedElement, gen_ecore_EEnumLiteral_ENamedElement, gen_ecore_EOperation_ETypedElement, gen_ecore_EPackage_ENamedElement, gen_ecore_ETypedElement_ENamedElement, gen_ecore_EParameter_ETypedElement, gen_ecore_EReference_EStructuralFeature, gen_ecore_EStructuralFeature_ETypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)