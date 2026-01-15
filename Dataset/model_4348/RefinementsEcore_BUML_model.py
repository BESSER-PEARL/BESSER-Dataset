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
RefinementsEcore_EAttribute = Class(name="RefinementsEcore::EAttribute")
EStructuralFeature = Class(name="EStructuralFeature")
RefinementsEcore_EReference = Class(name="RefinementsEcore::EReference")
RefinementsEcore_EStructuralFeature = Class(name="RefinementsEcore::EStructuralFeature", is_abstract=True)
RefinementsEcore_EClassifier = Class(name="RefinementsEcore::EClassifier", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
RefinementsEcore_EDataType = Class(name="RefinementsEcore::EDataType")
RefinementsEcore_EAnnotation = Class(name="RefinementsEcore::EAnnotation")
EModelElement = Class(name="EModelElement")
RefinementsEcore_EModelElement = Class(name="RefinementsEcore::EModelElement", is_abstract=True)
RefinementsEcore_EClass = Class(name="RefinementsEcore::EClass")
EClassifier = Class(name="EClassifier")
RefinementsEcore_EOperation = Class(name="RefinementsEcore::EOperation")
RefinementsEcore_EParameter = Class(name="RefinementsEcore::EParameter")
RefinementsEcore_EPackage = Class(name="RefinementsEcore::EPackage")
RefinementsEcore_EEnum = Class(name="RefinementsEcore::EEnum")
EDataType = Class(name="EDataType")
RefinementsEcore_EEnumLiteral = Class(name="RefinementsEcore::EEnumLiteral")
RefinementsEcore_ENamedElement = Class(name="RefinementsEcore::ENamedElement", is_abstract=True)
ETypedElement = Class(name="ETypedElement")
RefinementsEcore_ETypedElement = Class(name="RefinementsEcore::ETypedElement", is_abstract=True)

# RefinementsEcore_EAttribute class attributes and methods
RefinementsEcore_EAttribute_iD: Property = Property(name="iD", type=IntegerType)
RefinementsEcore_EAttribute.attributes={RefinementsEcore_EAttribute_iD}

# EStructuralFeature class attributes and methods

# RefinementsEcore_EReference class attributes and methods
RefinementsEcore_EReference_containment: Property = Property(name="containment", type=BooleanType)
RefinementsEcore_EReference_container: Property = Property(name="container", type=BooleanType)
RefinementsEcore_EReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
RefinementsEcore_EReference.attributes={RefinementsEcore_EReference_containment, RefinementsEcore_EReference_container, RefinementsEcore_EReference_resolveProxies}

# RefinementsEcore_EStructuralFeature class attributes and methods
RefinementsEcore_EStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
RefinementsEcore_EStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
RefinementsEcore_EStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
RefinementsEcore_EStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
RefinementsEcore_EStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
RefinementsEcore_EStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
RefinementsEcore_EStructuralFeature.attributes={RefinementsEcore_EStructuralFeature_volatile, RefinementsEcore_EStructuralFeature_unsettable, RefinementsEcore_EStructuralFeature_derived, RefinementsEcore_EStructuralFeature_transient, RefinementsEcore_EStructuralFeature_changeable, RefinementsEcore_EStructuralFeature_defaultValueLiteral}

# RefinementsEcore_EClassifier class attributes and methods
RefinementsEcore_EClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
RefinementsEcore_EClassifier_instanceClass: Property = Property(name="instanceClass", type=StringType)
RefinementsEcore_EClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
RefinementsEcore_EClassifier.attributes={RefinementsEcore_EClassifier_instanceClass, RefinementsEcore_EClassifier_instanceClassName, RefinementsEcore_EClassifier_instanceTypeName}

# ENamedElement class attributes and methods

# RefinementsEcore_EDataType class attributes and methods
RefinementsEcore_EDataType_serializable: Property = Property(name="serializable", type=BooleanType)
RefinementsEcore_EDataType.attributes={RefinementsEcore_EDataType_serializable}

# RefinementsEcore_EAnnotation class attributes and methods
RefinementsEcore_EAnnotation_source: Property = Property(name="source", type=StringType)
RefinementsEcore_EAnnotation.attributes={RefinementsEcore_EAnnotation_source}

# EModelElement class attributes and methods

# RefinementsEcore_EModelElement class attributes and methods

# RefinementsEcore_EClass class attributes and methods
RefinementsEcore_EClass_abstract: Property = Property(name="abstract", type=BooleanType)
RefinementsEcore_EClass_interface: Property = Property(name="interface", type=BooleanType)
RefinementsEcore_EClass.attributes={RefinementsEcore_EClass_abstract, RefinementsEcore_EClass_interface}

# EClassifier class attributes and methods

# RefinementsEcore_EOperation class attributes and methods

# RefinementsEcore_EParameter class attributes and methods

# RefinementsEcore_EPackage class attributes and methods
RefinementsEcore_EPackage_nsURI: Property = Property(name="nsURI", type=StringType)
RefinementsEcore_EPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
RefinementsEcore_EPackage.attributes={RefinementsEcore_EPackage_nsPrefix, RefinementsEcore_EPackage_nsURI}

# RefinementsEcore_EEnum class attributes and methods

# EDataType class attributes and methods

# RefinementsEcore_EEnumLiteral class attributes and methods
RefinementsEcore_EEnumLiteral_value: Property = Property(name="value", type=IntegerType)
RefinementsEcore_EEnumLiteral_literal: Property = Property(name="literal", type=StringType)
RefinementsEcore_EEnumLiteral.attributes={RefinementsEcore_EEnumLiteral_value, RefinementsEcore_EEnumLiteral_literal}

# RefinementsEcore_ENamedElement class attributes and methods
RefinementsEcore_ENamedElement_name: Property = Property(name="name", type=StringType)
RefinementsEcore_ENamedElement.attributes={RefinementsEcore_ENamedElement_name}

# ETypedElement class attributes and methods

# RefinementsEcore_ETypedElement class attributes and methods
RefinementsEcore_ETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
RefinementsEcore_ETypedElement_unique: Property = Property(name="unique", type=BooleanType)
RefinementsEcore_ETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
RefinementsEcore_ETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
RefinementsEcore_ETypedElement_many: Property = Property(name="many", type=BooleanType)
RefinementsEcore_ETypedElement_required: Property = Property(name="required", type=BooleanType)
RefinementsEcore_ETypedElement.attributes={RefinementsEcore_ETypedElement_lowerBound, RefinementsEcore_ETypedElement_ordered, RefinementsEcore_ETypedElement_required, RefinementsEcore_ETypedElement_upperBound, RefinementsEcore_ETypedElement_many, RefinementsEcore_ETypedElement_unique}

# Relationships
eReferences8: BinaryAssociation = BinaryAssociation(
    name="eReferences8",
    ends={
        Property(name="RefinementsEcore_EReference", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EClass9", type=RefinementsEcore_EReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes10: BinaryAssociation = BinaryAssociation(
    name="eAttributes10",
    ends={
        Property(name="RefinementsEcore_EAttribute12", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EClass11", type=RefinementsEcore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute13: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute13",
    ends={
        Property(name="RefinementsEcore_EAttribute15", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EClass14", type=RefinementsEcore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eStructuralFeatures16: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures16",
    ends={
        Property(name="EStructuralFeature", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass17", type=RefinementsEcore_EStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAttributeType0: BinaryAssociation = BinaryAssociation(
    name="eAttributeType0",
    ends={
        Property(name="RefinementsEcore_EDataType", type=RefinementsEcore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EAttribute", type=RefinementsEcore_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
Refines2: BinaryAssociation = BinaryAssociation(
    name="Refines2",
    ends={
        Property(name="RefinementsEcore_EAttribute3", type=RefinementsEcore_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EAttribute1", type=RefinementsEcore_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eModelElement4: BinaryAssociation = BinaryAssociation(
    name="eModelElement4",
    ends={
        Property(name="EModelElement", type=RefinementsEcore_EAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="eAnnotations", type=RefinementsEcore_EModelElement, multiplicity=Multiplicity(0, 1))
    }
)
eSuperTypes6: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes6",
    ends={
        Property(name="RefinementsEcore_EClass", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EClass5", type=RefinementsEcore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations7: BinaryAssociation = BinaryAssociation(
    name="eOperations7",
    ends={
        Property(name="EOperation", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=RefinementsEcore_EOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass22: BinaryAssociation = BinaryAssociation(
    name="eContainingClass22",
    ends={
        Property(name="EClass", type=RefinementsEcore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperations", type=RefinementsEcore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eParameters23: BinaryAssociation = BinaryAssociation(
    name="eParameters23",
    ends={
        Property(name="EParameter", type=RefinementsEcore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=RefinementsEcore_EParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions24: BinaryAssociation = BinaryAssociation(
    name="eExceptions24",
    ends={
        Property(name="RefinementsEcore_EClassifier", type=RefinementsEcore_EOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EOperation", type=RefinementsEcore_EClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
eClassifiers25: BinaryAssociation = BinaryAssociation(
    name="eClassifiers25",
    ends={
        Property(name="EClassifier", type=RefinementsEcore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=RefinementsEcore_EClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage18: BinaryAssociation = BinaryAssociation(
    name="ePackage18",
    ends={
        Property(name="EPackage", type=RefinementsEcore_EClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=RefinementsEcore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eLiterals19: BinaryAssociation = BinaryAssociation(
    name="eLiterals19",
    ends={
        Property(name="EEnumLiteral", type=RefinementsEcore_EEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=RefinementsEcore_EEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum20: BinaryAssociation = BinaryAssociation(
    name="eEnum20",
    ends={
        Property(name="EEnum", type=RefinementsEcore_EEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=RefinementsEcore_EEnum, multiplicity=Multiplicity(0, 1))
    }
)
eAnnotations21: BinaryAssociation = BinaryAssociation(
    name="eAnnotations21",
    ends={
        Property(name="EAnnotation", type=RefinementsEcore_EModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="eModelElement", type=RefinementsEcore_EAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eContainingClass46: BinaryAssociation = BinaryAssociation(
    name="eContainingClass46",
    ends={
        Property(name="EClass47", type=RefinementsEcore_EStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=RefinementsEcore_EClass, multiplicity=Multiplicity(0, 1))
    }
)
eType48: BinaryAssociation = BinaryAssociation(
    name="eType48",
    ends={
        Property(name="RefinementsEcore_EClassifier49", type=RefinementsEcore_ETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_ETypedElement", type=RefinementsEcore_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
eSubpackages27: BinaryAssociation = BinaryAssociation(
    name="eSubpackages27",
    ends={
        Property(name="EPackage28", type=RefinementsEcore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=RefinementsEcore_EPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage30: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage30",
    ends={
        Property(name="EPackage31", type=RefinementsEcore_EPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=RefinementsEcore_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation32: BinaryAssociation = BinaryAssociation(
    name="eOperation32",
    ends={
        Property(name="EOperation33", type=RefinementsEcore_EParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=RefinementsEcore_EOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite35: BinaryAssociation = BinaryAssociation(
    name="eOpposite35",
    ends={
        Property(name="RefinementsEcore_EReference36", type=RefinementsEcore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EReference34", type=RefinementsEcore_EReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType37: BinaryAssociation = BinaryAssociation(
    name="eReferenceType37",
    ends={
        Property(name="RefinementsEcore_EClass39", type=RefinementsEcore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EReference38", type=RefinementsEcore_EClass, multiplicity=Multiplicity(1, 1))
    }
)
eKeys40: BinaryAssociation = BinaryAssociation(
    name="eKeys40",
    ends={
        Property(name="RefinementsEcore_EAttribute42", type=RefinementsEcore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EReference41", type=RefinementsEcore_EAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
Refines44: BinaryAssociation = BinaryAssociation(
    name="Refines44",
    ends={
        Property(name="RefinementsEcore_EReference45", type=RefinementsEcore_EReference, multiplicity=Multiplicity(1, 1)),
        Property(name="RefinementsEcore_EReference43", type=RefinementsEcore_EReference, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_RefinementsEcore_EAttribute_EStructuralFeature = Generalization(general=EStructuralFeature, specific=RefinementsEcore_EAttribute)
gen_RefinementsEcore_EClassifier_ENamedElement = Generalization(general=ENamedElement, specific=RefinementsEcore_EClassifier)
gen_RefinementsEcore_EAnnotation_EModelElement = Generalization(general=EModelElement, specific=RefinementsEcore_EAnnotation)
gen_RefinementsEcore_EClass_EClassifier = Generalization(general=EClassifier, specific=RefinementsEcore_EClass)
gen_RefinementsEcore_EPackage_ENamedElement = Generalization(general=ENamedElement, specific=RefinementsEcore_EPackage)
gen_RefinementsEcore_EDataType_EClassifier = Generalization(general=EClassifier, specific=RefinementsEcore_EDataType)
gen_RefinementsEcore_EEnum_EDataType = Generalization(general=EDataType, specific=RefinementsEcore_EEnum)
gen_RefinementsEcore_EEnumLiteral_ENamedElement = Generalization(general=ENamedElement, specific=RefinementsEcore_EEnumLiteral)
gen_RefinementsEcore_ENamedElement_EModelElement = Generalization(general=EModelElement, specific=RefinementsEcore_ENamedElement)
gen_RefinementsEcore_EOperation_ETypedElement = Generalization(general=ETypedElement, specific=RefinementsEcore_EOperation)
gen_RefinementsEcore_ETypedElement_ENamedElement = Generalization(general=ENamedElement, specific=RefinementsEcore_ETypedElement)
gen_RefinementsEcore_EParameter_ETypedElement = Generalization(general=ETypedElement, specific=RefinementsEcore_EParameter)
gen_RefinementsEcore_EReference_EStructuralFeature = Generalization(general=EStructuralFeature, specific=RefinementsEcore_EReference)
gen_RefinementsEcore_EStructuralFeature_ETypedElement = Generalization(general=ETypedElement, specific=RefinementsEcore_EStructuralFeature)

# Domain Model
domain_model = DomainModel(
    name="RefinementsEcore",
    types={RefinementsEcore_EAttribute, EStructuralFeature, RefinementsEcore_EReference, RefinementsEcore_EStructuralFeature, RefinementsEcore_EClassifier, ENamedElement, RefinementsEcore_EDataType, RefinementsEcore_EAnnotation, EModelElement, RefinementsEcore_EModelElement, RefinementsEcore_EClass, EClassifier, RefinementsEcore_EOperation, RefinementsEcore_EParameter, RefinementsEcore_EPackage, RefinementsEcore_EEnum, EDataType, RefinementsEcore_EEnumLiteral, RefinementsEcore_ENamedElement, ETypedElement, RefinementsEcore_ETypedElement},
    associations={eReferences8, eAttributes10, eIDAttribute13, eStructuralFeatures16, eAttributeType0, Refines2, eModelElement4, eSuperTypes6, eOperations7, eContainingClass22, eParameters23, eExceptions24, eClassifiers25, ePackage18, eLiterals19, eEnum20, eAnnotations21, eContainingClass46, eType48, eSubpackages27, eSuperPackage30, eOperation32, eOpposite35, eReferenceType37, eKeys40, Refines44},
    generalizations={gen_RefinementsEcore_EAttribute_EStructuralFeature, gen_RefinementsEcore_EClassifier_ENamedElement, gen_RefinementsEcore_EAnnotation_EModelElement, gen_RefinementsEcore_EClass_EClassifier, gen_RefinementsEcore_EPackage_ENamedElement, gen_RefinementsEcore_EDataType_EClassifier, gen_RefinementsEcore_EEnum_EDataType, gen_RefinementsEcore_EEnumLiteral_ENamedElement, gen_RefinementsEcore_ENamedElement_EModelElement, gen_RefinementsEcore_EOperation_ETypedElement, gen_RefinementsEcore_ETypedElement_ENamedElement, gen_RefinementsEcore_EParameter_ETypedElement, gen_RefinementsEcore_EReference_EStructuralFeature, gen_RefinementsEcore_EStructuralFeature_ETypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)