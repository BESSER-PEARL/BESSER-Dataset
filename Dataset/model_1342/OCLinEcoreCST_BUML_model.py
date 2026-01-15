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
oclinEcoreCST_AnnotationCS = Class(name="oclinEcoreCST::AnnotationCS")
ModelElementCS = Class(name="ModelElementCS")
oclinEcoreCST_DetailCS = Class(name="oclinEcoreCST::DetailCS")
oclinEcoreCST_AttributeRef = Class(name="oclinEcoreCST::AttributeRef", is_abstract=True)
oclinEcoreCST_ClassCS = Class(name="oclinEcoreCST::ClassCS")
ClassifierCS = Class(name="ClassifierCS")
oclinEcoreCST_ClassRef = Class(name="oclinEcoreCST::ClassRef", is_abstract=True)
oclinEcoreCST_OperationCS = Class(name="oclinEcoreCST::OperationCS")
oclinEcoreCST_StructuralFeatureCS = Class(name="oclinEcoreCST::StructuralFeatureCS", is_abstract=True)
oclinEcoreCST_AttributeCS = Class(name="oclinEcoreCST::AttributeCS")
StructuralFeatureCS = Class(name="StructuralFeatureCS")
oclinEcoreCST_AttributeCSRef = Class(name="oclinEcoreCST::AttributeCSRef")
AttributeRef = Class(name="AttributeRef")
ClassifierRef = Class(name="ClassifierRef")
oclinEcoreCST_ClassCSRef = Class(name="oclinEcoreCST::ClassCSRef")
ClassRef = Class(name="ClassRef")
oclinEcoreCST_ConstraintCS = Class(name="oclinEcoreCST::ConstraintCS")
oclinEcoreCST_ClassifierCS = Class(name="oclinEcoreCST::ClassifierCS", is_abstract=True)
NamedElementCS = Class(name="NamedElementCS")
oclinEcoreCST_ClassifierRef = Class(name="oclinEcoreCST::ClassifierRef", is_abstract=True)
oclinEcoreCST_OclExpressionCS = Class(name="oclinEcoreCST::OclExpressionCS")
oclinEcoreCST_DataTypeRef = Class(name="oclinEcoreCST::DataTypeRef", is_abstract=True)
oclinEcoreCST_DataTypeCS = Class(name="oclinEcoreCST::DataTypeCS")
DataTypeOrEnumCS = Class(name="DataTypeOrEnumCS")
oclinEcoreCST_DataTypeOrEnumCS = Class(name="oclinEcoreCST::DataTypeOrEnumCS", is_abstract=True)
oclinEcoreCST_DataTypeCSRef = Class(name="oclinEcoreCST::DataTypeCSRef")
DataTypeRef = Class(name="DataTypeRef")
oclinEcoreCST_DocumentCS = Class(name="oclinEcoreCST::DocumentCS")
oclinEcoreCST_ImportCS = Class(name="oclinEcoreCST::ImportCS")
oclinEcoreCST_PackageCS = Class(name="oclinEcoreCST::PackageCS")
oclinEcoreCST_EAttributeRef = Class(name="oclinEcoreCST::EAttributeRef")
oclinEcoreCST_EAttribute = Class(name="oclinEcoreCST::EAttribute")
oclinEcoreCST_TypeParameterCS = Class(name="oclinEcoreCST::TypeParameterCS", is_abstract=True)
oclinEcoreCST_ClassifierCSRef = Class(name="oclinEcoreCST::ClassifierCSRef")
oclinEcoreCST_EDataTypeRef = Class(name="oclinEcoreCST::EDataTypeRef")
oclinEcoreCST_EDataType = Class(name="oclinEcoreCST::EDataType")
oclinEcoreCST_EReferenceRef = Class(name="oclinEcoreCST::EReferenceRef")
ReferenceRef = Class(name="ReferenceRef")
oclinEcoreCST_EReference = Class(name="oclinEcoreCST::EReference")
oclinEcoreCST_EnumCS = Class(name="oclinEcoreCST::EnumCS")
oclinEcoreCST_EnumLiteralCS = Class(name="oclinEcoreCST::EnumLiteralCS")
oclinEcoreCST_ModelElementCS = Class(name="oclinEcoreCST::ModelElementCS", is_abstract=True)
oclinEcoreCST_NamedElementCS = Class(name="oclinEcoreCST::NamedElementCS", is_abstract=True)
TypedElementCS = Class(name="TypedElementCS")
oclinEcoreCST_EClassRef = Class(name="oclinEcoreCST::EClassRef")
oclinEcoreCST_EClass = Class(name="oclinEcoreCST::EClass")
oclinEcoreCST_EClassifierRef = Class(name="oclinEcoreCST::EClassifierRef")
oclinEcoreCST_EClassifier = Class(name="oclinEcoreCST::EClassifier")
oclinEcoreCST_ReferenceCS = Class(name="oclinEcoreCST::ReferenceCS")
oclinEcoreCST_ReferenceRef = Class(name="oclinEcoreCST::ReferenceRef", is_abstract=True)
oclinEcoreCST_ReferenceCSRef = Class(name="oclinEcoreCST::ReferenceCSRef")
oclinEcoreCST_ParameterCS = Class(name="oclinEcoreCST::ParameterCS")
oclinEcoreCST_TypedElementCS = Class(name="oclinEcoreCST::TypedElementCS", is_abstract=True)

# oclinEcoreCST_AnnotationCS class attributes and methods
oclinEcoreCST_AnnotationCS_idSource: Property = Property(name="idSource", type=StringType)
oclinEcoreCST_AnnotationCS_stringSource: Property = Property(name="stringSource", type=StringType)
oclinEcoreCST_AnnotationCS.attributes={oclinEcoreCST_AnnotationCS_idSource, oclinEcoreCST_AnnotationCS_stringSource}

# ModelElementCS class attributes and methods

# oclinEcoreCST_DetailCS class attributes and methods
oclinEcoreCST_DetailCS_idName: Property = Property(name="idName", type=StringType)
oclinEcoreCST_DetailCS_stringName: Property = Property(name="stringName", type=StringType)
oclinEcoreCST_DetailCS_value: Property = Property(name="value", type=StringType)
oclinEcoreCST_DetailCS.attributes={oclinEcoreCST_DetailCS_value, oclinEcoreCST_DetailCS_stringName, oclinEcoreCST_DetailCS_idName}

# oclinEcoreCST_AttributeRef class attributes and methods

# oclinEcoreCST_ClassCS class attributes and methods

# ClassifierCS class attributes and methods

# oclinEcoreCST_ClassRef class attributes and methods

# oclinEcoreCST_OperationCS class attributes and methods

# oclinEcoreCST_StructuralFeatureCS class attributes and methods

# oclinEcoreCST_AttributeCS class attributes and methods

# StructuralFeatureCS class attributes and methods

# oclinEcoreCST_AttributeCSRef class attributes and methods

# AttributeRef class attributes and methods

# ClassifierRef class attributes and methods

# oclinEcoreCST_ClassCSRef class attributes and methods

# ClassRef class attributes and methods

# oclinEcoreCST_ConstraintCS class attributes and methods
oclinEcoreCST_ConstraintCS_stereotype: Property = Property(name="stereotype", type=StringType)
oclinEcoreCST_ConstraintCS.attributes={oclinEcoreCST_ConstraintCS_stereotype}

# oclinEcoreCST_ClassifierCS class attributes and methods
oclinEcoreCST_ClassifierCS_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
oclinEcoreCST_ClassifierCS_qualifiers: Property = Property(name="qualifiers", type=StringType)
oclinEcoreCST_ClassifierCS.attributes={oclinEcoreCST_ClassifierCS_qualifiers, oclinEcoreCST_ClassifierCS_instanceClassName}

# NamedElementCS class attributes and methods

# oclinEcoreCST_ClassifierRef class attributes and methods

# oclinEcoreCST_OclExpressionCS class attributes and methods

# oclinEcoreCST_DataTypeRef class attributes and methods

# oclinEcoreCST_DataTypeCS class attributes and methods

# DataTypeOrEnumCS class attributes and methods

# oclinEcoreCST_DataTypeOrEnumCS class attributes and methods

# oclinEcoreCST_DataTypeCSRef class attributes and methods

# DataTypeRef class attributes and methods

# oclinEcoreCST_DocumentCS class attributes and methods

# oclinEcoreCST_ImportCS class attributes and methods
oclinEcoreCST_ImportCS_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
oclinEcoreCST_ImportCS.attributes={oclinEcoreCST_ImportCS_importedNamespace}

# oclinEcoreCST_PackageCS class attributes and methods

# oclinEcoreCST_EAttributeRef class attributes and methods

# oclinEcoreCST_EAttribute class attributes and methods

# oclinEcoreCST_TypeParameterCS class attributes and methods

# oclinEcoreCST_ClassifierCSRef class attributes and methods

# oclinEcoreCST_EDataTypeRef class attributes and methods

# oclinEcoreCST_EDataType class attributes and methods

# oclinEcoreCST_EReferenceRef class attributes and methods

# ReferenceRef class attributes and methods

# oclinEcoreCST_EReference class attributes and methods

# oclinEcoreCST_EnumCS class attributes and methods

# oclinEcoreCST_EnumLiteralCS class attributes and methods
oclinEcoreCST_EnumLiteralCS_value: Property = Property(name="value", type=IntegerType)
oclinEcoreCST_EnumLiteralCS.attributes={oclinEcoreCST_EnumLiteralCS_value}

# oclinEcoreCST_ModelElementCS class attributes and methods

# oclinEcoreCST_NamedElementCS class attributes and methods
oclinEcoreCST_NamedElementCS_name: Property = Property(name="name", type=StringType)
oclinEcoreCST_NamedElementCS.attributes={oclinEcoreCST_NamedElementCS_name}

# TypedElementCS class attributes and methods

# oclinEcoreCST_EClassRef class attributes and methods

# oclinEcoreCST_EClass class attributes and methods

# oclinEcoreCST_EClassifierRef class attributes and methods

# oclinEcoreCST_EClassifier class attributes and methods

# oclinEcoreCST_ReferenceCS class attributes and methods
oclinEcoreCST_ReferenceCS_containment: Property = Property(name="containment", type=BooleanType)
oclinEcoreCST_ReferenceCS.attributes={oclinEcoreCST_ReferenceCS_containment}

# oclinEcoreCST_ReferenceRef class attributes and methods

# oclinEcoreCST_ReferenceCSRef class attributes and methods

# oclinEcoreCST_ParameterCS class attributes and methods

# oclinEcoreCST_TypedElementCS class attributes and methods
oclinEcoreCST_TypedElementCS_lower: Property = Property(name="lower", type=IntegerType)
oclinEcoreCST_TypedElementCS_multiplicity: Property = Property(name="multiplicity", type=StringType)
oclinEcoreCST_TypedElementCS_qualifiers: Property = Property(name="qualifiers", type=StringType)
oclinEcoreCST_TypedElementCS_upper: Property = Property(name="upper", type=IntegerType)
oclinEcoreCST_TypedElementCS.attributes={oclinEcoreCST_TypedElementCS_multiplicity, oclinEcoreCST_TypedElementCS_qualifiers, oclinEcoreCST_TypedElementCS_upper, oclinEcoreCST_TypedElementCS_lower}

# Relationships
ref1: BinaryAssociation = BinaryAssociation(
    name="ref1",
    ends={
        Property(name="oclinEcoreCST_AttributeCS", type=oclinEcoreCST_AttributeCSRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_AttributeCSRef", type=oclinEcoreCST_AttributeCS, multiplicity=Multiplicity(0, 1))
    }
)
superTypes2: BinaryAssociation = BinaryAssociation(
    name="superTypes2",
    ends={
        Property(name="oclinEcoreCST_ClassRef", type=oclinEcoreCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassCS", type=oclinEcoreCST_ClassRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations3: BinaryAssociation = BinaryAssociation(
    name="operations3",
    ends={
        Property(name="oclinEcoreCST_OperationCS", type=oclinEcoreCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassCS4", type=oclinEcoreCST_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
details0: BinaryAssociation = BinaryAssociation(
    name="details0",
    ends={
        Property(name="oclinEcoreCST_DetailCS", type=oclinEcoreCST_AnnotationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_AnnotationCS", type=oclinEcoreCST_DetailCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref7: BinaryAssociation = BinaryAssociation(
    name="ref7",
    ends={
        Property(name="oclinEcoreCST_ClassCS8", type=oclinEcoreCST_ClassCSRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassCSRef", type=oclinEcoreCST_ClassCS, multiplicity=Multiplicity(0, 1))
    }
)
structuralFeatures5: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures5",
    ends={
        Property(name="oclinEcoreCST_StructuralFeatureCS", type=oclinEcoreCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassCS6", type=oclinEcoreCST_StructuralFeatureCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints9: BinaryAssociation = BinaryAssociation(
    name="constraints9",
    ends={
        Property(name="oclinEcoreCST_ConstraintCS", type=oclinEcoreCST_ClassifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassifierCS", type=oclinEcoreCST_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr14: BinaryAssociation = BinaryAssociation(
    name="expr14",
    ends={
        Property(name="oclinEcoreCST_OclExpressionCS", type=oclinEcoreCST_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ConstraintCS15", type=oclinEcoreCST_OclExpressionCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref16: BinaryAssociation = BinaryAssociation(
    name="ref16",
    ends={
        Property(name="oclinEcoreCST_DataTypeOrEnumCS", type=oclinEcoreCST_DataTypeCSRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_DataTypeCSRef", type=oclinEcoreCST_DataTypeOrEnumCS, multiplicity=Multiplicity(0, 1))
    }
)
imports17: BinaryAssociation = BinaryAssociation(
    name="imports17",
    ends={
        Property(name="oclinEcoreCST_ImportCS", type=oclinEcoreCST_DocumentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_DocumentCS", type=oclinEcoreCST_ImportCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages18: BinaryAssociation = BinaryAssociation(
    name="packages18",
    ends={
        Property(name="oclinEcoreCST_PackageCS", type=oclinEcoreCST_DocumentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_DocumentCS19", type=oclinEcoreCST_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters10: BinaryAssociation = BinaryAssociation(
    name="typeParameters10",
    ends={
        Property(name="oclinEcoreCST_TypeParameterCS", type=oclinEcoreCST_ClassifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassifierCS11", type=oclinEcoreCST_TypeParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref12: BinaryAssociation = BinaryAssociation(
    name="ref12",
    ends={
        Property(name="oclinEcoreCST_ClassifierCS13", type=oclinEcoreCST_ClassifierCSRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ClassifierCSRef", type=oclinEcoreCST_ClassifierCS, multiplicity=Multiplicity(0, 1))
    }
)
ref23: BinaryAssociation = BinaryAssociation(
    name="ref23",
    ends={
        Property(name="oclinEcoreCST_EDataType", type=oclinEcoreCST_EDataTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_EDataTypeRef", type=oclinEcoreCST_EDataType, multiplicity=Multiplicity(0, 1))
    }
)
ref24: BinaryAssociation = BinaryAssociation(
    name="ref24",
    ends={
        Property(name="oclinEcoreCST_EReference", type=oclinEcoreCST_EReferenceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_EReferenceRef", type=oclinEcoreCST_EReference, multiplicity=Multiplicity(0, 1))
    }
)
literals25: BinaryAssociation = BinaryAssociation(
    name="literals25",
    ends={
        Property(name="oclinEcoreCST_EnumLiteralCS", type=oclinEcoreCST_EnumCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_EnumCS", type=oclinEcoreCST_EnumLiteralCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations26: BinaryAssociation = BinaryAssociation(
    name="annotations26",
    ends={
        Property(name="oclinEcoreCST_AnnotationCS27", type=oclinEcoreCST_ModelElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ModelElementCS", type=oclinEcoreCST_AnnotationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref20: BinaryAssociation = BinaryAssociation(
    name="ref20",
    ends={
        Property(name="oclinEcoreCST_EAttribute", type=oclinEcoreCST_EAttributeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_EAttributeRef", type=oclinEcoreCST_EAttribute, multiplicity=Multiplicity(0, 1))
    }
)
ref21: BinaryAssociation = BinaryAssociation(
    name="ref21",
    ends={
        Property(name="oclinEcoreCST_EClass", type=oclinEcoreCST_EClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_EClassRef", type=oclinEcoreCST_EClass, multiplicity=Multiplicity(0, 1))
    }
)
ref22: BinaryAssociation = BinaryAssociation(
    name="ref22",
    ends={
        Property(name="oclinEcoreCST_EClassifier", type=oclinEcoreCST_EClassifierRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_EClassifierRef", type=oclinEcoreCST_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
classifiers38: BinaryAssociation = BinaryAssociation(
    name="classifiers38",
    ends={
        Property(name="oclinEcoreCST_ClassifierCS40", type=oclinEcoreCST_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_PackageCS39", type=oclinEcoreCST_ClassifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subpackages42: BinaryAssociation = BinaryAssociation(
    name="subpackages42",
    ends={
        Property(name="oclinEcoreCST_PackageCS43", type=oclinEcoreCST_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_PackageCS41", type=oclinEcoreCST_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opposite44: BinaryAssociation = BinaryAssociation(
    name="opposite44",
    ends={
        Property(name="oclinEcoreCST_ReferenceRef", type=oclinEcoreCST_ReferenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ReferenceCS", type=oclinEcoreCST_ReferenceRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keys45: BinaryAssociation = BinaryAssociation(
    name="keys45",
    ends={
        Property(name="oclinEcoreCST_AttributeRef", type=oclinEcoreCST_ReferenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ReferenceCS46", type=oclinEcoreCST_AttributeRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref47: BinaryAssociation = BinaryAssociation(
    name="ref47",
    ends={
        Property(name="oclinEcoreCST_ReferenceCS48", type=oclinEcoreCST_ReferenceCSRef, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_ReferenceCSRef", type=oclinEcoreCST_ReferenceCS, multiplicity=Multiplicity(0, 1))
    }
)
constraints28: BinaryAssociation = BinaryAssociation(
    name="constraints28",
    ends={
        Property(name="oclinEcoreCST_ConstraintCS30", type=oclinEcoreCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_OperationCS29", type=oclinEcoreCST_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="oclinEcoreCST_ParameterCS", type=oclinEcoreCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_OperationCS32", type=oclinEcoreCST_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters33: BinaryAssociation = BinaryAssociation(
    name="typeParameters33",
    ends={
        Property(name="oclinEcoreCST_TypeParameterCS35", type=oclinEcoreCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_OperationCS34", type=oclinEcoreCST_TypeParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions36: BinaryAssociation = BinaryAssociation(
    name="exceptions36",
    ends={
        Property(name="oclinEcoreCST_ClassifierRef", type=oclinEcoreCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_OperationCS37", type=oclinEcoreCST_ClassifierRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints49: BinaryAssociation = BinaryAssociation(
    name="constraints49",
    ends={
        Property(name="oclinEcoreCST_StructuralFeatureCS50", type=oclinEcoreCST_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="oclinEcoreCST_ConstraintCS51", type=oclinEcoreCST_StructuralFeatureCS, multiplicity=Multiplicity(1, 1))
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="oclinEcoreCST_ClassifierRef53", type=oclinEcoreCST_TypedElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_TypedElementCS", type=oclinEcoreCST_ClassifierRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends54: BinaryAssociation = BinaryAssociation(
    name="extends54",
    ends={
        Property(name="oclinEcoreCST_ClassifierRef56", type=oclinEcoreCST_TypeParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_TypeParameterCS55", type=oclinEcoreCST_ClassifierRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super57: BinaryAssociation = BinaryAssociation(
    name="super57",
    ends={
        Property(name="oclinEcoreCST_ClassifierRef59", type=oclinEcoreCST_TypeParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="oclinEcoreCST_TypeParameterCS58", type=oclinEcoreCST_ClassifierRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_oclinEcoreCST_AnnotationCS_ModelElementCS = Generalization(general=ModelElementCS, specific=oclinEcoreCST_AnnotationCS)
gen_oclinEcoreCST_AttributeCSRef_AttributeRef = Generalization(general=AttributeRef, specific=oclinEcoreCST_AttributeCSRef)
gen_oclinEcoreCST_ClassCS_ClassifierCS = Generalization(general=ClassifierCS, specific=oclinEcoreCST_ClassCS)
gen_oclinEcoreCST_AttributeCS_StructuralFeatureCS = Generalization(general=StructuralFeatureCS, specific=oclinEcoreCST_AttributeCS)
gen_oclinEcoreCST_ClassRef_ClassifierRef = Generalization(general=ClassifierRef, specific=oclinEcoreCST_ClassRef)
gen_oclinEcoreCST_ClassCSRef_ClassRef = Generalization(general=ClassRef, specific=oclinEcoreCST_ClassCSRef)
gen_oclinEcoreCST_ClassifierCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclinEcoreCST_ClassifierCS)
gen_oclinEcoreCST_ConstraintCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclinEcoreCST_ConstraintCS)
gen_oclinEcoreCST_DataTypeRef_ClassifierRef = Generalization(general=ClassifierRef, specific=oclinEcoreCST_DataTypeRef)
gen_oclinEcoreCST_DataTypeCS_DataTypeOrEnumCS = Generalization(general=DataTypeOrEnumCS, specific=oclinEcoreCST_DataTypeCS)
gen_oclinEcoreCST_DataTypeOrEnumCS_ClassifierCS = Generalization(general=ClassifierCS, specific=oclinEcoreCST_DataTypeOrEnumCS)
gen_oclinEcoreCST_DataTypeCSRef_DataTypeRef = Generalization(general=DataTypeRef, specific=oclinEcoreCST_DataTypeCSRef)
gen_oclinEcoreCST_EAttributeRef_AttributeRef = Generalization(general=AttributeRef, specific=oclinEcoreCST_EAttributeRef)
gen_oclinEcoreCST_ClassifierCSRef_ClassifierRef = Generalization(general=ClassifierRef, specific=oclinEcoreCST_ClassifierCSRef)
gen_oclinEcoreCST_EDataTypeRef_DataTypeRef = Generalization(general=DataTypeRef, specific=oclinEcoreCST_EDataTypeRef)
gen_oclinEcoreCST_EReferenceRef_ReferenceRef = Generalization(general=ReferenceRef, specific=oclinEcoreCST_EReferenceRef)
gen_oclinEcoreCST_EnumCS_DataTypeOrEnumCS = Generalization(general=DataTypeOrEnumCS, specific=oclinEcoreCST_EnumCS)
gen_oclinEcoreCST_EnumLiteralCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclinEcoreCST_EnumLiteralCS)
gen_oclinEcoreCST_NamedElementCS_ModelElementCS = Generalization(general=ModelElementCS, specific=oclinEcoreCST_NamedElementCS)
gen_oclinEcoreCST_OperationCS_TypedElementCS = Generalization(general=TypedElementCS, specific=oclinEcoreCST_OperationCS)
gen_oclinEcoreCST_EClassRef_ClassRef = Generalization(general=ClassRef, specific=oclinEcoreCST_EClassRef)
gen_oclinEcoreCST_EClassifierRef_ClassifierRef = Generalization(general=ClassifierRef, specific=oclinEcoreCST_EClassifierRef)
gen_oclinEcoreCST_PackageCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclinEcoreCST_PackageCS)
gen_oclinEcoreCST_ParameterCS_TypedElementCS = Generalization(general=TypedElementCS, specific=oclinEcoreCST_ParameterCS)
gen_oclinEcoreCST_ReferenceCS_StructuralFeatureCS = Generalization(general=StructuralFeatureCS, specific=oclinEcoreCST_ReferenceCS)
gen_oclinEcoreCST_ReferenceCSRef_ReferenceRef = Generalization(general=ReferenceRef, specific=oclinEcoreCST_ReferenceCSRef)
gen_oclinEcoreCST_TypedElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclinEcoreCST_TypedElementCS)
gen_oclinEcoreCST_TypeParameterCS_NamedElementCS = Generalization(general=NamedElementCS, specific=oclinEcoreCST_TypeParameterCS)
gen_oclinEcoreCST_StructuralFeatureCS_TypedElementCS = Generalization(general=TypedElementCS, specific=oclinEcoreCST_StructuralFeatureCS)

# Domain Model
domain_model = DomainModel(
    name="oclinEcoreCST",
    types={oclinEcoreCST_AnnotationCS, ModelElementCS, oclinEcoreCST_DetailCS, oclinEcoreCST_AttributeRef, oclinEcoreCST_ClassCS, ClassifierCS, oclinEcoreCST_ClassRef, oclinEcoreCST_OperationCS, oclinEcoreCST_StructuralFeatureCS, oclinEcoreCST_AttributeCS, StructuralFeatureCS, oclinEcoreCST_AttributeCSRef, AttributeRef, ClassifierRef, oclinEcoreCST_ClassCSRef, ClassRef, oclinEcoreCST_ConstraintCS, oclinEcoreCST_ClassifierCS, NamedElementCS, oclinEcoreCST_ClassifierRef, oclinEcoreCST_OclExpressionCS, oclinEcoreCST_DataTypeRef, oclinEcoreCST_DataTypeCS, DataTypeOrEnumCS, oclinEcoreCST_DataTypeOrEnumCS, oclinEcoreCST_DataTypeCSRef, DataTypeRef, oclinEcoreCST_DocumentCS, oclinEcoreCST_ImportCS, oclinEcoreCST_PackageCS, oclinEcoreCST_EAttributeRef, oclinEcoreCST_EAttribute, oclinEcoreCST_TypeParameterCS, oclinEcoreCST_ClassifierCSRef, oclinEcoreCST_EDataTypeRef, oclinEcoreCST_EDataType, oclinEcoreCST_EReferenceRef, ReferenceRef, oclinEcoreCST_EReference, oclinEcoreCST_EnumCS, oclinEcoreCST_EnumLiteralCS, oclinEcoreCST_ModelElementCS, oclinEcoreCST_NamedElementCS, TypedElementCS, oclinEcoreCST_EClassRef, oclinEcoreCST_EClass, oclinEcoreCST_EClassifierRef, oclinEcoreCST_EClassifier, oclinEcoreCST_ReferenceCS, oclinEcoreCST_ReferenceRef, oclinEcoreCST_ReferenceCSRef, oclinEcoreCST_ParameterCS, oclinEcoreCST_TypedElementCS},
    associations={ref1, superTypes2, operations3, details0, ref7, structuralFeatures5, constraints9, expr14, ref16, imports17, packages18, typeParameters10, ref12, ref23, ref24, literals25, annotations26, ref20, ref21, ref22, classifiers38, subpackages42, opposite44, keys45, ref47, constraints28, parameters31, typeParameters33, exceptions36, constraints49, type52, extends54, super57},
    generalizations={gen_oclinEcoreCST_AnnotationCS_ModelElementCS, gen_oclinEcoreCST_AttributeCSRef_AttributeRef, gen_oclinEcoreCST_ClassCS_ClassifierCS, gen_oclinEcoreCST_AttributeCS_StructuralFeatureCS, gen_oclinEcoreCST_ClassRef_ClassifierRef, gen_oclinEcoreCST_ClassCSRef_ClassRef, gen_oclinEcoreCST_ClassifierCS_NamedElementCS, gen_oclinEcoreCST_ConstraintCS_NamedElementCS, gen_oclinEcoreCST_DataTypeRef_ClassifierRef, gen_oclinEcoreCST_DataTypeCS_DataTypeOrEnumCS, gen_oclinEcoreCST_DataTypeOrEnumCS_ClassifierCS, gen_oclinEcoreCST_DataTypeCSRef_DataTypeRef, gen_oclinEcoreCST_EAttributeRef_AttributeRef, gen_oclinEcoreCST_ClassifierCSRef_ClassifierRef, gen_oclinEcoreCST_EDataTypeRef_DataTypeRef, gen_oclinEcoreCST_EReferenceRef_ReferenceRef, gen_oclinEcoreCST_EnumCS_DataTypeOrEnumCS, gen_oclinEcoreCST_EnumLiteralCS_NamedElementCS, gen_oclinEcoreCST_NamedElementCS_ModelElementCS, gen_oclinEcoreCST_OperationCS_TypedElementCS, gen_oclinEcoreCST_EClassRef_ClassRef, gen_oclinEcoreCST_EClassifierRef_ClassifierRef, gen_oclinEcoreCST_PackageCS_NamedElementCS, gen_oclinEcoreCST_ParameterCS_TypedElementCS, gen_oclinEcoreCST_ReferenceCS_StructuralFeatureCS, gen_oclinEcoreCST_ReferenceCSRef_ReferenceRef, gen_oclinEcoreCST_TypedElementCS_NamedElementCS, gen_oclinEcoreCST_TypeParameterCS_NamedElementCS, gen_oclinEcoreCST_StructuralFeatureCS_TypedElementCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)