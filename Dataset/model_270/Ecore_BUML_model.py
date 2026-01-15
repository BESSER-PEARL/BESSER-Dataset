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
Ecore_EClass = Class(name="Ecore::EClass")
EClassifier = Class(name="EClassifier")
Ecore_EAttribute = Class(name="Ecore::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
Ecore_EDataType = Class(name="Ecore::EDataType")
Ecore_EReference = Class(name="Ecore::EReference")
Ecore_EStructuralFeature = Class(name="Ecore::EStructuralFeature", is_abstract=True)
Ecore_EOperation = Class(name="Ecore::EOperation")
Ecore_EClassifier = Class(name="Ecore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
Ecore_EEnum = Class(name="Ecore::EEnum")
EDataType = Class(name="EDataType")
Ecore_EEnumLiteral = Class(name="Ecore::EEnumLiteral")
Ecore_EPackage = Class(name="Ecore::EPackage")
ETypedElement = Class(name="ETypedElement")
Ecore_EParameter = Class(name="Ecore::EParameter")
Ecore_ENamedElement = Class(name="Ecore::ENamedElement", is_abstract=True)
Ecore_ETypedElement = Class(name="Ecore::ETypedElement", is_abstract=True)
Ecore_EStringToStringMapEntry = Class(name="Ecore::EStringToStringMapEntry")

# Ecore_EClass class attributes and methods
Ecore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
Ecore_EClass_interface: Property = Property(name="interface", type=BooleanType)
Ecore_EClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
Ecore_EClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
Ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=EStructuralFeature)
Ecore_EClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
Ecore_EClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=EStructuralFeature)
Ecore_EClass.attributes={Ecore_EClass_interface, Ecore_EClass_abstract}
Ecore_EClass.methods={Ecore_EClass_m_getFeatureID, Ecore_EClass_m_getEStructuralFeature, Ecore_EClass_m_getEStructuralFeature, Ecore_EClass_m_isSuperTypeOf, Ecore_EClass_m_getFeatureCount}

# EClassifier class attributes and methods

# Ecore_EAttribute class attributes and methods
Ecore_EAttribute_iD: Property = Property(name="iD", type=BooleanType)
Ecore_EAttribute.attributes={Ecore_EAttribute_iD}

# EStructuralFeature class attributes and methods

# Ecore_EDataType class attributes and methods
Ecore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
Ecore_EDataType.attributes={Ecore_EDataType_serializable}

# Ecore_EReference class attributes and methods
Ecore_EReference_containment: Property = Property(name="containment", type=BooleanType)
Ecore_EReference_container: Property = Property(name="container", type=BooleanType)
Ecore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
Ecore_EReference.attributes={Ecore_EReference_container, Ecore_EReference_containment, Ecore_EReference_resolveProxies}

# Ecore_EStructuralFeature class attributes and methods
Ecore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
Ecore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
Ecore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
Ecore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
Ecore_EStructuralFeature_defaultValue: Property = Property(name="defaultValue", type=StringType)
Ecore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
Ecore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
Ecore_EStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
Ecore_EStructuralFeature_m_getContainerClass: Method = Method(name="getContainerClass", parameters={})
Ecore_EStructuralFeature.attributes={Ecore_EStructuralFeature_defaultValueLiteral, Ecore_EStructuralFeature_unsettable, Ecore_EStructuralFeature_changeable, Ecore_EStructuralFeature_defaultValue, Ecore_EStructuralFeature_transient, Ecore_EStructuralFeature_derived, Ecore_EStructuralFeature_volatile}
Ecore_EStructuralFeature.methods={Ecore_EStructuralFeature_m_getContainerClass, Ecore_EStructuralFeature_m_getFeatureID}

# Ecore_EOperation class attributes and methods

# Ecore_EClassifier class attributes and methods
Ecore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
Ecore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
Ecore_EClassifier_defaultValue: Property = Property(name="defaultValue", type=StringType)
Ecore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
Ecore_EClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
Ecore_EClassifier_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=BooleanType)
Ecore_EClassifier.attributes={Ecore_EClassifier_defaultValue, Ecore_EClassifier_instanceTypeName, Ecore_EClassifier_instanceClassName, Ecore_EClassifier_instanceClass}
Ecore_EClassifier.methods={Ecore_EClassifier_m_isInstance, Ecore_EClassifier_m_getClassifierID}

# ENamedElement class attributes and methods

# Ecore_EEnum class attributes and methods
Ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
Ecore_EEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
Ecore_EEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
Ecore_EEnum.methods={Ecore_EEnum_m_getEEnumLiteral, Ecore_EEnum_m_getEEnumLiteralByLiteral, Ecore_EEnum_m_getEEnumLiteral}

# EDataType class attributes and methods

# Ecore_EEnumLiteral class attributes and methods
Ecore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
Ecore_EEnumLiteral_instance: Property = Property(name="instance", type=StringType)
Ecore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
Ecore_EEnumLiteral.attributes={Ecore_EEnumLiteral_value, Ecore_EEnumLiteral_instance, Ecore_EEnumLiteral_literal}

# Ecore_EPackage class attributes and methods
Ecore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
Ecore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
Ecore_EPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=EClassifier)
Ecore_EPackage.attributes={Ecore_EPackage_nsURI, Ecore_EPackage_nsPrefix}
Ecore_EPackage.methods={Ecore_EPackage_m_getEClassifier}

# ETypedElement class attributes and methods

# Ecore_EParameter class attributes and methods

# Ecore_ENamedElement class attributes and methods
Ecore_ENamedElement_name: Property = Property(name="name", type=StringType)
Ecore_ENamedElement.attributes={Ecore_ENamedElement_name}

# Ecore_ETypedElement class attributes and methods
Ecore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
Ecore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
Ecore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
Ecore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
Ecore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
Ecore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
Ecore_ETypedElement.attributes={Ecore_ETypedElement_many, Ecore_ETypedElement_ordered, Ecore_ETypedElement_required, Ecore_ETypedElement_upperBound, Ecore_ETypedElement_unique, Ecore_ETypedElement_lowerBound}

# Ecore_EStringToStringMapEntry class attributes and methods
Ecore_EStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
Ecore_EStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
Ecore_EStringToStringMapEntry.attributes={Ecore_EStringToStringMapEntry_value, Ecore_EStringToStringMapEntry_key}

# Relationships
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="Ecore_EDataType", type=Ecore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EAttribute", type=Ecore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
eAllReferences7: BinaryAssociation = BinaryAssociation(
    name="eAllReferences7",
    ends={
        Property(name="Ecore_EReference", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass8", type=Ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences9: BinaryAssociation = BinaryAssociation(
    name="eReferences9",
    ends={
        Property(name="Ecore_EReference11", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass10", type=Ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes12: BinaryAssociation = BinaryAssociation(
    name="eAttributes12",
    ends={
        Property(name="Ecore_EAttribute14", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass13", type=Ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments15: BinaryAssociation = BinaryAssociation(
    name="eAllContainments15",
    ends={
        Property(name="Ecore_EReference17", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass16", type=Ecore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations18: BinaryAssociation = BinaryAssociation(
    name="eAllOperations18",
    ends={
        Property(name="Ecore_EOperation", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass19", type=Ecore_EOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAllStructuralFeatures20: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures20",
    ends={
        Property(name="Ecore_EStructuralFeature", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass21", type=Ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eSuperTypes2: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes2",
    ends={
        Property(name="Ecore_EClass", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass1", type=Ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations3: BinaryAssociation = BinaryAssociation(
    name="eOperations3",
    ends={
        Property(name="EOperation", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=Ecore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes4: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes4",
    ends={
        Property(name="Ecore_EAttribute6", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass5", type=Ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute25: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute25",
    ends={
        Property(name="Ecore_EAttribute27", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass26", type=Ecore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures28: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures28",
    ends={
        Property(name="EStructuralFeature", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass29", type=Ecore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllSuperTypes23: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes23",
    ends={
        Property(name="Ecore_EClass24", type=Ecore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EClass22", type=Ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eLiterals31: BinaryAssociation = BinaryAssociation(
    name="eLiterals31",
    ends={
        Property(name="EEnumLiteral", type=Ecore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=Ecore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage30: BinaryAssociation = BinaryAssociation(
    name="ePackage30",
    ends={
        Property(name="EPackage", type=Ecore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=Ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass33: BinaryAssociation = BinaryAssociation(
    name="eContainingClass33",
    ends={
        Property(name="EClass", type=Ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=Ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eParameters34: BinaryAssociation = BinaryAssociation(
    name="eParameters34",
    ends={
        Property(name="EParameter", type=Ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=Ecore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions35: BinaryAssociation = BinaryAssociation(
    name="eExceptions35",
    ends={
        Property(name="Ecore_EClassifier", type=Ecore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EOperation36", type=Ecore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eEnum32: BinaryAssociation = BinaryAssociation(
    name="eEnum32",
    ends={
        Property(name="EEnum", type=Ecore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=Ecore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eClassifiers37: BinaryAssociation = BinaryAssociation(
    name="eClassifiers37",
    ends={
        Property(name="EClassifier", type=Ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=Ecore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages39: BinaryAssociation = BinaryAssociation(
    name="eSubpackages39",
    ends={
        Property(name="EPackage40", type=Ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=Ecore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage42: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage42",
    ends={
        Property(name="EPackage43", type=Ecore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=Ecore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation44: BinaryAssociation = BinaryAssociation(
    name="eOperation44",
    ends={
        Property(name="EOperation45", type=Ecore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=Ecore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite47: BinaryAssociation = BinaryAssociation(
    name="eOpposite47",
    ends={
        Property(name="Ecore_EReference48", type=Ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EReference46", type=Ecore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType49: BinaryAssociation = BinaryAssociation(
    name="eReferenceType49",
    ends={
        Property(name="Ecore_EClass51", type=Ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EReference50", type=Ecore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys52: BinaryAssociation = BinaryAssociation(
    name="eKeys52",
    ends={
        Property(name="Ecore_EAttribute54", type=Ecore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_EReference53", type=Ecore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eContainingClass55: BinaryAssociation = BinaryAssociation(
    name="eContainingClass55",
    ends={
        Property(name="EClass56", type=Ecore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=Ecore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType57: BinaryAssociation = BinaryAssociation(
    name="eType57",
    ends={
        Property(name="Ecore_EClassifier58", type=Ecore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Ecore_ETypedElement", type=Ecore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Ecore_EClass_EClassifier = Generalization(general=EClassifier, specific=Ecore_EClass)
gen_Ecore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=Ecore_EAttribute)
gen_Ecore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=Ecore_EClassifier)
gen_Ecore_EDataType_EClassifier = Generalization(general=EClassifier, specific=Ecore_EDataType)
gen_Ecore_EEnum_EDataType = Generalization(general=EDataType, specific=Ecore_EEnum)
gen_Ecore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=Ecore_EOperation)
gen_Ecore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=Ecore_EPackage)
gen_Ecore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=Ecore_EEnumLiteral)
gen_Ecore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=Ecore_EParameter)
gen_Ecore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=Ecore_EReference)
gen_Ecore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=Ecore_EStructuralFeature)
gen_Ecore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=Ecore_ETypedElement)

# Domain Model
domain_model = DomainModel(
    name="Ecore",
    types={Ecore_EClass, EClassifier, Ecore_EAttribute, EStructuralFeature, Ecore_EDataType, Ecore_EReference, Ecore_EStructuralFeature, Ecore_EOperation, Ecore_EClassifier, ENamedElement, Ecore_EEnum, EDataType, Ecore_EEnumLiteral, Ecore_EPackage, ETypedElement, Ecore_EParameter, Ecore_ENamedElement, Ecore_ETypedElement, Ecore_EStringToStringMapEntry},
    associations={eAttributeType0, eAllReferences7, eReferences9, eAttributes12, eAllContainments15, eAllOperations18, eAllStructuralFeatures20, eSuperTypes2, eOperations3, eAllAttributes4, eIDAttribute25, eStructuralFeatures28, eAllSuperTypes23, eLiterals31, ePackage30, eContainingClass33, eParameters34, eExceptions35, eEnum32, eClassifiers37, eSubpackages39, eSuperPackage42, eOperation44, eOpposite47, eReferenceType49, eKeys52, eContainingClass55, eType57},
    generalizations={gen_Ecore_EClass_EClassifier, gen_Ecore_EAttribute_EStructuralFeature, gen_Ecore_EClassifier_ENamedElement, gen_Ecore_EDataType_EClassifier, gen_Ecore_EEnum_EDataType, gen_Ecore_EOperation_ETypedElement, gen_Ecore_EPackage_ENamedElement, gen_Ecore_EEnumLiteral_ENamedElement, gen_Ecore_EParameter_ETypedElement, gen_Ecore_EReference_EStructuralFeature, gen_Ecore_EStructuralFeature_ETypedElement, gen_Ecore_ETypedElement_ENamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)