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

# Enumerations
IteratorKind: Enumeration = Enumeration(
    name="IteratorKind",
    literals={
            EnumerationLiteral(name="Parameter"),
			EnumerationLiteral(name="Iterator"),
			EnumerationLiteral(name="Accumulator")
    }
)

# Classes
baseCST_ClassCS = Class(name="baseCST::ClassCS")
ClassifierCS = Class(name="ClassifierCS")
NamespaceCS = Class(name="NamespaceCS")
baseCST_AnnotationCS = Class(name="baseCST::AnnotationCS")
AnnotationElementCS = Class(name="AnnotationElementCS")
baseCST_ModelElementCS = Class(name="baseCST::ModelElementCS", is_abstract=True)
baseCST_ModelElementRefCS = Class(name="baseCST::ModelElementRefCS")
baseCST_AnnotationElementCS = Class(name="baseCST::AnnotationElementCS", is_abstract=True)
NamedElementCS = Class(name="NamedElementCS")
baseCST_DetailCS = Class(name="baseCST::DetailCS")
baseCST_AttributeCS = Class(name="baseCST::AttributeCS")
StructuralFeatureCS = Class(name="StructuralFeatureCS")
baseCST_TypedRefCS = Class(name="baseCST::TypedRefCS", is_abstract=True)
baseCST_OperationCS = Class(name="baseCST::OperationCS")
baseCST_StructuralFeatureCS = Class(name="baseCST::StructuralFeatureCS", is_abstract=True)
baseCST_ClassifierCS = Class(name="baseCST::ClassifierCS", is_abstract=True)
TypeCS = Class(name="TypeCS")
TemplateableElementCS = Class(name="TemplateableElementCS")
baseCST_PackageCS = Class(name="baseCST::PackageCS")
baseCST_ConstraintCS = Class(name="baseCST::ConstraintCS")
baseCST_SpecificationCS = Class(name="baseCST::SpecificationCS")
baseCST_DataTypeCS = Class(name="baseCST::DataTypeCS")
baseCST_EnumerationLiteralCS = Class(name="baseCST::EnumerationLiteralCS")
baseCST_DocumentationCS = Class(name="baseCST::DocumentationCS")
baseCST_ElementCS = Class(name="baseCST::ElementCS", is_abstract=True)
VisitableCS = Class(name="VisitableCS")
baseCST_ElementRefCS = Class(name="baseCST::ElementRefCS", is_abstract=True)
PivotableElementCS = Class(name="PivotableElementCS")
baseCST_EnumerationCS = Class(name="baseCST::EnumerationCS")
baseCST_FeatureCS = Class(name="baseCST::FeatureCS", is_abstract=True)
TypedElementCS = Class(name="TypedElementCS")
baseCST_ImportCS = Class(name="baseCST::ImportCS")
baseCST_PathNameCS = Class(name="baseCST::PathNameCS")
baseCST_Namespace = Class(name="baseCST::Namespace")
baseCST_LambdaTypeCS = Class(name="baseCST::LambdaTypeCS")
TypedRefCS = Class(name="TypedRefCS")
Nameable = Class(name="Nameable")
baseCST_LibraryCS = Class(name="baseCST::LibraryCS")
ElementRefCS = Class(name="ElementRefCS")
baseCST_Element = Class(name="baseCST::Element")
baseCST_MultiplicityBoundsCS = Class(name="baseCST::MultiplicityBoundsCS")
MultiplicityCS = Class(name="MultiplicityCS")
baseCST_MultiplicityCS = Class(name="baseCST::MultiplicityCS", is_abstract=True)
ElementCS = Class(name="ElementCS")
baseCST_ParameterCS = Class(name="baseCST::ParameterCS")
baseCST_MultiplicityStringCS = Class(name="baseCST::MultiplicityStringCS")
baseCST_NamedElementCS = Class(name="baseCST::NamedElementCS", is_abstract=True)
ModelElementCS = Class(name="ModelElementCS")
baseCST_NamespaceCS = Class(name="baseCST::NamespaceCS", is_abstract=True)
FeatureCS = Class(name="FeatureCS")
baseCST_EClassifier = Class(name="baseCST::EClassifier")
baseCST_PathElementWithURICS = Class(name="baseCST::PathElementWithURICS")
PathElementCS = Class(name="PathElementCS")
baseCST_PathElementCS = Class(name="baseCST::PathElementCS")
Pivotable = Class(name="Pivotable")
baseCST_RootPackageCS = Class(name="baseCST::RootPackageCS")
PackageCS = Class(name="PackageCS")
RootCS = Class(name="RootCS")
baseCST_TemplateBindingCS = Class(name="baseCST::TemplateBindingCS")
baseCST_PivotableElementCS = Class(name="baseCST::PivotableElementCS", is_abstract=True)
baseCST_PrimitiveTypeRefCS = Class(name="baseCST::PrimitiveTypeRefCS")
baseCST_ReferenceCS = Class(name="baseCST::ReferenceCS")
baseCST_Property = Class(name="baseCST::Property")
baseCST_RootCS = Class(name="baseCST::RootCS", is_abstract=True)
baseCST_TuplePartCS = Class(name="baseCST::TuplePartCS")
baseCST_TupleTypeCS = Class(name="baseCST::TupleTypeCS")
baseCST_TypeCS = Class(name="baseCST::TypeCS", is_abstract=True)
baseCST_TypeParameterCS = Class(name="baseCST::TypeParameterCS")
TemplateParameterCS = Class(name="TemplateParameterCS")
baseCST_TypedTypeRefCS = Class(name="baseCST::TypedTypeRefCS")
baseCST_TemplateParameterSubstitutionCS = Class(name="baseCST::TemplateParameterSubstitutionCS")
baseCST_TemplateParameterCS = Class(name="baseCST::TemplateParameterCS", is_abstract=True)
baseCST_TemplateSignatureCS = Class(name="baseCST::TemplateSignatureCS")
baseCST_TypeRefCS = Class(name="baseCST::TypeRefCS", is_abstract=True)
baseCST_TemplateableElementCS = Class(name="baseCST::TemplateableElementCS", is_abstract=True)
baseCST_Type = Class(name="baseCST::Type")
baseCST_VisitableCS = Class(name="baseCST::VisitableCS", is_abstract=True)
baseCST_WildcardTypeRefCS = Class(name="baseCST::WildcardTypeRefCS")
baseCST_TypedElementCS = Class(name="baseCST::TypedElementCS", is_abstract=True)
TypeRefCS = Class(name="TypeRefCS")

# baseCST_ClassCS class attributes and methods

# ClassifierCS class attributes and methods

# NamespaceCS class attributes and methods

# baseCST_AnnotationCS class attributes and methods

# AnnotationElementCS class attributes and methods

# baseCST_ModelElementCS class attributes and methods
baseCST_ModelElementCS_originalXmiId: Property = Property(name="originalXmiId", type=StringType)
baseCST_ModelElementCS_csi: Property = Property(name="csi", type=StringType)
baseCST_ModelElementCS.attributes={baseCST_ModelElementCS_csi, baseCST_ModelElementCS_originalXmiId}

# baseCST_ModelElementRefCS class attributes and methods

# baseCST_AnnotationElementCS class attributes and methods

# NamedElementCS class attributes and methods

# baseCST_DetailCS class attributes and methods
baseCST_DetailCS_value: Property = Property(name="value", type=StringType)
baseCST_DetailCS.attributes={baseCST_DetailCS_value}

# baseCST_AttributeCS class attributes and methods

# StructuralFeatureCS class attributes and methods

# baseCST_TypedRefCS class attributes and methods

# baseCST_OperationCS class attributes and methods

# baseCST_StructuralFeatureCS class attributes and methods
baseCST_StructuralFeatureCS_default: Property = Property(name="default", type=StringType)
baseCST_StructuralFeatureCS.attributes={baseCST_StructuralFeatureCS_default}

# baseCST_ClassifierCS class attributes and methods
baseCST_ClassifierCS_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
baseCST_ClassifierCS_qualifier: Property = Property(name="qualifier", type=StringType)
baseCST_ClassifierCS.attributes={baseCST_ClassifierCS_qualifier, baseCST_ClassifierCS_instanceClassName}

# TypeCS class attributes and methods

# TemplateableElementCS class attributes and methods

# baseCST_PackageCS class attributes and methods
baseCST_PackageCS_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
baseCST_PackageCS_nsURI: Property = Property(name="nsURI", type=StringType)
baseCST_PackageCS_m_getClassifier: Method = Method(name="getClassifier", parameters={Parameter(name='name')}, type=ClassifierCS)
baseCST_PackageCS.attributes={baseCST_PackageCS_nsURI, baseCST_PackageCS_nsPrefix}
baseCST_PackageCS.methods={baseCST_PackageCS_m_getClassifier}

# baseCST_ConstraintCS class attributes and methods
baseCST_ConstraintCS_stereotype: Property = Property(name="stereotype", type=StringType)
baseCST_ConstraintCS.attributes={baseCST_ConstraintCS_stereotype}

# baseCST_SpecificationCS class attributes and methods
baseCST_SpecificationCS_exprString: Property = Property(name="exprString", type=StringType)
baseCST_SpecificationCS.attributes={baseCST_SpecificationCS_exprString}

# baseCST_DataTypeCS class attributes and methods

# baseCST_EnumerationLiteralCS class attributes and methods
baseCST_EnumerationLiteralCS_value: Property = Property(name="value", type=IntegerType)
baseCST_EnumerationLiteralCS.attributes={baseCST_EnumerationLiteralCS_value}

# baseCST_DocumentationCS class attributes and methods
baseCST_DocumentationCS_value: Property = Property(name="value", type=StringType)
baseCST_DocumentationCS.attributes={baseCST_DocumentationCS_value}

# baseCST_ElementCS class attributes and methods
baseCST_ElementCS_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
baseCST_ElementCS.methods={baseCST_ElementCS_m_getDescription}

# VisitableCS class attributes and methods

# baseCST_ElementRefCS class attributes and methods

# PivotableElementCS class attributes and methods

# baseCST_EnumerationCS class attributes and methods

# baseCST_FeatureCS class attributes and methods

# TypedElementCS class attributes and methods

# baseCST_ImportCS class attributes and methods
baseCST_ImportCS_all: Property = Property(name="all", type=BooleanType)
baseCST_ImportCS.attributes={baseCST_ImportCS_all}

# baseCST_PathNameCS class attributes and methods
baseCST_PathNameCS_scopeFilter: Property = Property(name="scopeFilter", type=StringType)
baseCST_PathNameCS.attributes={baseCST_PathNameCS_scopeFilter}

# baseCST_Namespace class attributes and methods

# baseCST_LambdaTypeCS class attributes and methods
baseCST_LambdaTypeCS_name: Property = Property(name="name", type=StringType)
baseCST_LambdaTypeCS.attributes={baseCST_LambdaTypeCS_name}

# TypedRefCS class attributes and methods

# Nameable class attributes and methods

# baseCST_LibraryCS class attributes and methods

# ElementRefCS class attributes and methods

# baseCST_Element class attributes and methods

# baseCST_MultiplicityBoundsCS class attributes and methods
baseCST_MultiplicityBoundsCS_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
baseCST_MultiplicityBoundsCS_upperBound: Property = Property(name="upperBound", type=StringType)
baseCST_MultiplicityBoundsCS.attributes={baseCST_MultiplicityBoundsCS_lowerBound, baseCST_MultiplicityBoundsCS_upperBound}

# MultiplicityCS class attributes and methods

# baseCST_MultiplicityCS class attributes and methods
baseCST_MultiplicityCS_m_getLower: Method = Method(name="getLower", parameters={}, type=IntegerType)
baseCST_MultiplicityCS_m_getUpper: Method = Method(name="getUpper", parameters={}, type=IntegerType)
baseCST_MultiplicityCS.methods={baseCST_MultiplicityCS_m_getUpper, baseCST_MultiplicityCS_m_getLower}

# ElementCS class attributes and methods

# baseCST_ParameterCS class attributes and methods

# baseCST_MultiplicityStringCS class attributes and methods
baseCST_MultiplicityStringCS_stringBounds: Property = Property(name="stringBounds", type=StringType)
baseCST_MultiplicityStringCS.attributes={baseCST_MultiplicityStringCS_stringBounds}

# baseCST_NamedElementCS class attributes and methods
baseCST_NamedElementCS_name: Property = Property(name="name", type=StringType)
baseCST_NamedElementCS.attributes={baseCST_NamedElementCS_name}

# ModelElementCS class attributes and methods

# baseCST_NamespaceCS class attributes and methods

# FeatureCS class attributes and methods

# baseCST_EClassifier class attributes and methods

# baseCST_PathElementWithURICS class attributes and methods
baseCST_PathElementWithURICS_uri: Property = Property(name="uri", type=StringType)
baseCST_PathElementWithURICS.attributes={baseCST_PathElementWithURICS_uri}

# PathElementCS class attributes and methods

# baseCST_PathElementCS class attributes and methods

# Pivotable class attributes and methods

# baseCST_RootPackageCS class attributes and methods

# PackageCS class attributes and methods

# RootCS class attributes and methods

# baseCST_TemplateBindingCS class attributes and methods

# baseCST_PivotableElementCS class attributes and methods

# baseCST_PrimitiveTypeRefCS class attributes and methods
baseCST_PrimitiveTypeRefCS_name: Property = Property(name="name", type=StringType)
baseCST_PrimitiveTypeRefCS.attributes={baseCST_PrimitiveTypeRefCS_name}

# baseCST_ReferenceCS class attributes and methods

# baseCST_Property class attributes and methods

# baseCST_RootCS class attributes and methods

# baseCST_TuplePartCS class attributes and methods

# baseCST_TupleTypeCS class attributes and methods
baseCST_TupleTypeCS_name: Property = Property(name="name", type=StringType)
baseCST_TupleTypeCS.attributes={baseCST_TupleTypeCS_name}

# baseCST_TypeCS class attributes and methods

# baseCST_TypeParameterCS class attributes and methods

# TemplateParameterCS class attributes and methods

# baseCST_TypedTypeRefCS class attributes and methods

# baseCST_TemplateParameterSubstitutionCS class attributes and methods

# baseCST_TemplateParameterCS class attributes and methods

# baseCST_TemplateSignatureCS class attributes and methods

# baseCST_TypeRefCS class attributes and methods

# baseCST_TemplateableElementCS class attributes and methods

# baseCST_Type class attributes and methods

# baseCST_VisitableCS class attributes and methods

# baseCST_WildcardTypeRefCS class attributes and methods

# baseCST_TypedElementCS class attributes and methods
baseCST_TypedElementCS_qualifier: Property = Property(name="qualifier", type=StringType)
baseCST_TypedElementCS_optional: Property = Property(name="optional", type=BooleanType)
baseCST_TypedElementCS.attributes={baseCST_TypedElementCS_optional, baseCST_TypedElementCS_qualifier}

# TypeRefCS class attributes and methods

# Relationships
ownedContent0: BinaryAssociation = BinaryAssociation(
    name="ownedContent0",
    ends={
        Property(name="baseCST_ModelElementCS", type=baseCST_AnnotationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_AnnotationCS", type=baseCST_ModelElementCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReference1: BinaryAssociation = BinaryAssociation(
    name="ownedReference1",
    ends={
        Property(name="baseCST_ModelElementRefCS", type=baseCST_AnnotationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_AnnotationCS2", type=baseCST_ModelElementRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDetail3: BinaryAssociation = BinaryAssociation(
    name="ownedDetail3",
    ends={
        Property(name="baseCST_DetailCS", type=baseCST_AnnotationElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_AnnotationElementCS", type=baseCST_DetailCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSuperType4: BinaryAssociation = BinaryAssociation(
    name="ownedSuperType4",
    ends={
        Property(name="baseCST_TypedRefCS", type=baseCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ClassCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation5: BinaryAssociation = BinaryAssociation(
    name="ownedOperation5",
    ends={
        Property(name="OperationCS", type=baseCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass", type=baseCST_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty6: BinaryAssociation = BinaryAssociation(
    name="ownedProperty6",
    ends={
        Property(name="StructuralFeatureCS", type=baseCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=baseCST_StructuralFeatureCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMetaType7: BinaryAssociation = BinaryAssociation(
    name="ownedMetaType7",
    ends={
        Property(name="baseCST_TypedRefCS9", type=baseCST_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ClassCS8", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="PackageCS", type=baseCST_ClassifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=baseCST_PackageCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedConstraint11: BinaryAssociation = BinaryAssociation(
    name="ownedConstraint11",
    ends={
        Property(name="baseCST_ConstraintCS", type=baseCST_ClassifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ClassifierCS", type=baseCST_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification12: BinaryAssociation = BinaryAssociation(
    name="specification12",
    ends={
        Property(name="baseCST_SpecificationCS", type=baseCST_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ConstraintCS13", type=baseCST_SpecificationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageSpecification14: BinaryAssociation = BinaryAssociation(
    name="messageSpecification14",
    ends={
        Property(name="baseCST_SpecificationCS16", type=baseCST_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ConstraintCS15", type=baseCST_SpecificationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literals17: BinaryAssociation = BinaryAssociation(
    name="literals17",
    ends={
        Property(name="baseCST_EnumerationLiteralCS", type=baseCST_DataTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_DataTypeCS", type=baseCST_EnumerationLiteralCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalParent19: BinaryAssociation = BinaryAssociation(
    name="logicalParent19",
    ends={
        Property(name="baseCST_ElementCS", type=baseCST_ElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ElementCS18", type=baseCST_ElementCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiterals20: BinaryAssociation = BinaryAssociation(
    name="ownedLiterals20",
    ends={
        Property(name="baseCST_EnumerationLiteralCS21", type=baseCST_EnumerationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_EnumerationCS", type=baseCST_EnumerationLiteralCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName22: BinaryAssociation = BinaryAssociation(
    name="pathName22",
    ends={
        Property(name="baseCST_PathNameCS", type=baseCST_ImportCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ImportCS", type=baseCST_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespace23: BinaryAssociation = BinaryAssociation(
    name="namespace23",
    ends={
        Property(name="baseCST_Namespace", type=baseCST_ImportCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ImportCS24", type=baseCST_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedContextType25: BinaryAssociation = BinaryAssociation(
    name="ownedContextType25",
    ends={
        Property(name="baseCST_TypedRefCS26", type=baseCST_LambdaTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_LambdaTypeCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameterType27: BinaryAssociation = BinaryAssociation(
    name="ownedParameterType27",
    ends={
        Property(name="baseCST_TypedRefCS29", type=baseCST_LambdaTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_LambdaTypeCS28", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedResultType30: BinaryAssociation = BinaryAssociation(
    name="ownedResultType30",
    ends={
        Property(name="baseCST_TypedRefCS32", type=baseCST_LambdaTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_LambdaTypeCS31", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package33: BinaryAssociation = BinaryAssociation(
    name="package33",
    ends={
        Property(name="baseCST_Namespace34", type=baseCST_LibraryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_LibraryCS", type=baseCST_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedAnnotation35: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotation35",
    ends={
        Property(name="baseCST_AnnotationElementCS37", type=baseCST_ModelElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ModelElementCS36", type=baseCST_AnnotationElementCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName38: BinaryAssociation = BinaryAssociation(
    name="pathName38",
    ends={
        Property(name="baseCST_PathNameCS40", type=baseCST_ModelElementRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ModelElementRefCS39", type=baseCST_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element41: BinaryAssociation = BinaryAssociation(
    name="element41",
    ends={
        Property(name="baseCST_Element", type=baseCST_ModelElementRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ModelElementRefCS42", type=baseCST_Element, multiplicity=Multiplicity(0, 1))
    }
)
owningClass43: BinaryAssociation = BinaryAssociation(
    name="owningClass43",
    ends={
        Property(name="ownedOperation", type=baseCST_ClassCS, multiplicity=Multiplicity(0, 1)),
        Property(name="ClassCS", type=baseCST_OperationCS, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter44: BinaryAssociation = BinaryAssociation(
    name="ownedParameter44",
    ends={
        Property(name="ParameterCS", type=baseCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owner45", type=baseCST_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedException46: BinaryAssociation = BinaryAssociation(
    name="ownedException46",
    ends={
        Property(name="baseCST_TypedRefCS47", type=baseCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_OperationCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrecondition48: BinaryAssociation = BinaryAssociation(
    name="ownedPrecondition48",
    ends={
        Property(name="baseCST_ConstraintCS50", type=baseCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_OperationCS49", type=baseCST_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPostcondition51: BinaryAssociation = BinaryAssociation(
    name="ownedPostcondition51",
    ends={
        Property(name="baseCST_ConstraintCS53", type=baseCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_OperationCS52", type=baseCST_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBodyExpression54: BinaryAssociation = BinaryAssociation(
    name="ownedBodyExpression54",
    ends={
        Property(name="baseCST_SpecificationCS56", type=baseCST_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_OperationCS55", type=baseCST_SpecificationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element64: BinaryAssociation = BinaryAssociation(
    name="element64",
    ends={
        Property(name="baseCST_Element65", type=baseCST_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_PathElementCS", type=baseCST_Element, multiplicity=Multiplicity(1, 1))
    }
)
elementType66: BinaryAssociation = BinaryAssociation(
    name="elementType66",
    ends={
        Property(name="baseCST_EClassifier", type=baseCST_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_PathElementCS67", type=baseCST_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
path68: BinaryAssociation = BinaryAssociation(
    name="path68",
    ends={
        Property(name="PathElementCS", type=baseCST_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="pathName", type=baseCST_PathElementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
element69: BinaryAssociation = BinaryAssociation(
    name="element69",
    ends={
        Property(name="baseCST_Element71", type=baseCST_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_PathNameCS70", type=baseCST_Element, multiplicity=Multiplicity(1, 1))
    }
)
context72: BinaryAssociation = BinaryAssociation(
    name="context72",
    ends={
        Property(name="baseCST_ElementCS74", type=baseCST_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_PathNameCS73", type=baseCST_ElementCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedType57: BinaryAssociation = BinaryAssociation(
    name="ownedType57",
    ends={
        Property(name="ClassifierCS", type=baseCST_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owner58", type=baseCST_ClassifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedNestedPackage60: BinaryAssociation = BinaryAssociation(
    name="ownedNestedPackage60",
    ends={
        Property(name="baseCST_PackageCS", type=baseCST_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_PackageCS59", type=baseCST_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner61: BinaryAssociation = BinaryAssociation(
    name="owner61",
    ends={
        Property(name="OperationCS62", type=baseCST_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=baseCST_OperationCS, multiplicity=Multiplicity(0, 1))
    }
)
pathName63: BinaryAssociation = BinaryAssociation(
    name="pathName63",
    ends={
        Property(name="PathNameCS", type=baseCST_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="path", type=baseCST_PathNameCS, multiplicity=Multiplicity(1, 1))
    }
)
ownedImport81: BinaryAssociation = BinaryAssociation(
    name="ownedImport81",
    ends={
        Property(name="baseCST_ImportCS82", type=baseCST_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_RootCS", type=baseCST_ImportCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLibrary83: BinaryAssociation = BinaryAssociation(
    name="ownedLibrary83",
    ends={
        Property(name="baseCST_LibraryCS85", type=baseCST_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_RootCS84", type=baseCST_LibraryCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner86: BinaryAssociation = BinaryAssociation(
    name="owner86",
    ends={
        Property(name="ClassCS87", type=baseCST_StructuralFeatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedProperty", type=baseCST_ClassCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefaultExpression88: BinaryAssociation = BinaryAssociation(
    name="ownedDefaultExpression88",
    ends={
        Property(name="baseCST_SpecificationCS89", type=baseCST_StructuralFeatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_StructuralFeatureCS", type=baseCST_SpecificationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pivot75: BinaryAssociation = BinaryAssociation(
    name="pivot75",
    ends={
        Property(name="baseCST_Element76", type=baseCST_PivotableElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_PivotableElementCS", type=baseCST_Element, multiplicity=Multiplicity(0, 1))
    }
)
opposite77: BinaryAssociation = BinaryAssociation(
    name="opposite77",
    ends={
        Property(name="baseCST_Property", type=baseCST_ReferenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ReferenceCS", type=baseCST_Property, multiplicity=Multiplicity(0, 1))
    }
)
keys78: BinaryAssociation = BinaryAssociation(
    name="keys78",
    ends={
        Property(name="baseCST_Property80", type=baseCST_ReferenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_ReferenceCS79", type=baseCST_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTemplateParameter96: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateParameter96",
    ends={
        Property(name="TemplateParameterCS", type=baseCST_TemplateSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateSignature", type=baseCST_TemplateParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature97: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature97",
    ends={
        Property(name="TemplateSignatureCS98", type=baseCST_TemplateableElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateElement", type=baseCST_TemplateSignatureCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts99: BinaryAssociation = BinaryAssociation(
    name="ownedParts99",
    ends={
        Property(name="baseCST_TuplePartCS", type=baseCST_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TupleTypeCS", type=baseCST_TuplePartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtends100: BinaryAssociation = BinaryAssociation(
    name="ownedExtends100",
    ends={
        Property(name="baseCST_TypedRefCS101", type=baseCST_TypeParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TypeParameterCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningTemplateBindableElement90: BinaryAssociation = BinaryAssociation(
    name="owningTemplateBindableElement90",
    ends={
        Property(name="TypedTypeRefCS", type=baseCST_TemplateBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateBinding", type=baseCST_TypedTypeRefCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameterSubstitution91: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSubstitution91",
    ends={
        Property(name="TemplateParameterSubstitutionCS", type=baseCST_TemplateBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateBinding", type=baseCST_TemplateParameterSubstitutionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningTemplateSignature92: BinaryAssociation = BinaryAssociation(
    name="owningTemplateSignature92",
    ends={
        Property(name="TemplateSignatureCS", type=baseCST_TemplateParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateParameter", type=baseCST_TemplateSignatureCS, multiplicity=Multiplicity(1, 1))
    }
)
owningTemplateBinding93: BinaryAssociation = BinaryAssociation(
    name="owningTemplateBinding93",
    ends={
        Property(name="TemplateBindingCS", type=baseCST_TemplateParameterSubstitutionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameterSubstitution", type=baseCST_TemplateBindingCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedActualParameter94: BinaryAssociation = BinaryAssociation(
    name="ownedActualParameter94",
    ends={
        Property(name="baseCST_TypeRefCS", type=baseCST_TemplateParameterSubstitutionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TemplateParameterSubstitutionCS", type=baseCST_TypeRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningTemplateElement95: BinaryAssociation = BinaryAssociation(
    name="owningTemplateElement95",
    ends={
        Property(name="TemplateableElementCS", type=baseCST_TemplateSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=baseCST_TemplateableElementCS, multiplicity=Multiplicity(0, 1))
    }
)
type111: BinaryAssociation = BinaryAssociation(
    name="type111",
    ends={
        Property(name="baseCST_Type", type=baseCST_TypedTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TypedTypeRefCS112", type=baseCST_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedTemplateBinding113: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateBinding113",
    ends={
        Property(name="TemplateBindingCS114", type=baseCST_TypedTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateBindableElement", type=baseCST_TemplateBindingCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends115: BinaryAssociation = BinaryAssociation(
    name="extends115",
    ends={
        Property(name="baseCST_TypedRefCS116", type=baseCST_WildcardTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_WildcardTypeRefCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
super117: BinaryAssociation = BinaryAssociation(
    name="super117",
    ends={
        Property(name="baseCST_TypedRefCS119", type=baseCST_WildcardTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_WildcardTypeRefCS118", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedSuper102: BinaryAssociation = BinaryAssociation(
    name="ownedSuper102",
    ends={
        Property(name="baseCST_TypedRefCS104", type=baseCST_TypeParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TypeParameterCS103", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType105: BinaryAssociation = BinaryAssociation(
    name="ownedType105",
    ends={
        Property(name="baseCST_TypedRefCS106", type=baseCST_TypedElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TypedElementCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity107: BinaryAssociation = BinaryAssociation(
    name="multiplicity107",
    ends={
        Property(name="baseCST_MultiplicityCS", type=baseCST_TypedRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TypedRefCS108", type=baseCST_MultiplicityCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pathName109: BinaryAssociation = BinaryAssociation(
    name="pathName109",
    ends={
        Property(name="baseCST_PathNameCS110", type=baseCST_TypedTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="baseCST_TypedTypeRefCS", type=baseCST_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_baseCST_ClassCS_ClassifierCS = Generalization(general=ClassifierCS, specific=baseCST_ClassCS)
gen_baseCST_ClassCS_NamespaceCS = Generalization(general=NamespaceCS, specific=baseCST_ClassCS)
gen_baseCST_AnnotationCS_AnnotationElementCS = Generalization(general=AnnotationElementCS, specific=baseCST_AnnotationCS)
gen_baseCST_AnnotationElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_AnnotationElementCS)
gen_baseCST_AttributeCS_StructuralFeatureCS = Generalization(general=StructuralFeatureCS, specific=baseCST_AttributeCS)
gen_baseCST_DetailCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_DetailCS)
gen_baseCST_ClassifierCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_ClassifierCS)
gen_baseCST_ClassifierCS_TypeCS = Generalization(general=TypeCS, specific=baseCST_ClassifierCS)
gen_baseCST_ClassifierCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=baseCST_ClassifierCS)
gen_baseCST_ConstraintCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_ConstraintCS)
gen_baseCST_DataTypeCS_ClassifierCS = Generalization(general=ClassifierCS, specific=baseCST_DataTypeCS)
gen_baseCST_DataTypeCS_NamespaceCS = Generalization(general=NamespaceCS, specific=baseCST_DataTypeCS)
gen_baseCST_DocumentationCS_AnnotationElementCS = Generalization(general=AnnotationElementCS, specific=baseCST_DocumentationCS)
gen_baseCST_ElementCS_VisitableCS = Generalization(general=VisitableCS, specific=baseCST_ElementCS)
gen_baseCST_ElementRefCS_PivotableElementCS = Generalization(general=PivotableElementCS, specific=baseCST_ElementRefCS)
gen_baseCST_EnumerationCS_ClassifierCS = Generalization(general=ClassifierCS, specific=baseCST_EnumerationCS)
gen_baseCST_EnumerationCS_NamespaceCS = Generalization(general=NamespaceCS, specific=baseCST_EnumerationCS)
gen_baseCST_EnumerationLiteralCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_EnumerationLiteralCS)
gen_baseCST_FeatureCS_TypedElementCS = Generalization(general=TypedElementCS, specific=baseCST_FeatureCS)
gen_baseCST_ImportCS_NamespaceCS = Generalization(general=NamespaceCS, specific=baseCST_ImportCS)
gen_baseCST_LambdaTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=baseCST_LambdaTypeCS)
gen_baseCST_LambdaTypeCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=baseCST_LambdaTypeCS)
gen_baseCST_LambdaTypeCS_Nameable = Generalization(general=Nameable, specific=baseCST_LambdaTypeCS)
gen_baseCST_LibraryCS_NamespaceCS = Generalization(general=NamespaceCS, specific=baseCST_LibraryCS)
gen_baseCST_ModelElementCS_PivotableElementCS = Generalization(general=PivotableElementCS, specific=baseCST_ModelElementCS)
gen_baseCST_ModelElementRefCS_ElementRefCS = Generalization(general=ElementRefCS, specific=baseCST_ModelElementRefCS)
gen_baseCST_MultiplicityBoundsCS_MultiplicityCS = Generalization(general=MultiplicityCS, specific=baseCST_MultiplicityBoundsCS)
gen_baseCST_MultiplicityCS_ElementCS = Generalization(general=ElementCS, specific=baseCST_MultiplicityCS)
gen_baseCST_PackageCS_NamespaceCS = Generalization(general=NamespaceCS, specific=baseCST_PackageCS)
gen_baseCST_MultiplicityStringCS_MultiplicityCS = Generalization(general=MultiplicityCS, specific=baseCST_MultiplicityStringCS)
gen_baseCST_NamedElementCS_ModelElementCS = Generalization(general=ModelElementCS, specific=baseCST_NamedElementCS)
gen_baseCST_NamedElementCS_Nameable = Generalization(general=Nameable, specific=baseCST_NamedElementCS)
gen_baseCST_NamespaceCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_NamespaceCS)
gen_baseCST_OperationCS_FeatureCS = Generalization(general=FeatureCS, specific=baseCST_OperationCS)
gen_baseCST_OperationCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=baseCST_OperationCS)
gen_baseCST_PathElementWithURICS_PathElementCS = Generalization(general=PathElementCS, specific=baseCST_PathElementWithURICS)
gen_baseCST_PathNameCS_ElementCS = Generalization(general=ElementCS, specific=baseCST_PathNameCS)
gen_baseCST_PathNameCS_Pivotable = Generalization(general=Pivotable, specific=baseCST_PathNameCS)
gen_baseCST_ParameterCS_TypedElementCS = Generalization(general=TypedElementCS, specific=baseCST_ParameterCS)
gen_baseCST_PathElementCS_ElementCS = Generalization(general=ElementCS, specific=baseCST_PathElementCS)
gen_baseCST_PathElementCS_Pivotable = Generalization(general=Pivotable, specific=baseCST_PathElementCS)
gen_baseCST_RootPackageCS_PackageCS = Generalization(general=PackageCS, specific=baseCST_RootPackageCS)
gen_baseCST_RootPackageCS_RootCS = Generalization(general=RootCS, specific=baseCST_RootPackageCS)
gen_baseCST_SpecificationCS_ModelElementCS = Generalization(general=ModelElementCS, specific=baseCST_SpecificationCS)
gen_baseCST_StructuralFeatureCS_FeatureCS = Generalization(general=FeatureCS, specific=baseCST_StructuralFeatureCS)
gen_baseCST_TemplateBindingCS_ElementRefCS = Generalization(general=ElementRefCS, specific=baseCST_TemplateBindingCS)
gen_baseCST_PivotableElementCS_ElementCS = Generalization(general=ElementCS, specific=baseCST_PivotableElementCS)
gen_baseCST_PivotableElementCS_Pivotable = Generalization(general=Pivotable, specific=baseCST_PivotableElementCS)
gen_baseCST_PrimitiveTypeRefCS_TypedRefCS = Generalization(general=TypedRefCS, specific=baseCST_PrimitiveTypeRefCS)
gen_baseCST_PrimitiveTypeRefCS_Nameable = Generalization(general=Nameable, specific=baseCST_PrimitiveTypeRefCS)
gen_baseCST_ReferenceCS_StructuralFeatureCS = Generalization(general=StructuralFeatureCS, specific=baseCST_ReferenceCS)
gen_baseCST_RootCS_ModelElementCS = Generalization(general=ModelElementCS, specific=baseCST_RootCS)
gen_baseCST_TemplateableElementCS_ElementCS = Generalization(general=ElementCS, specific=baseCST_TemplateableElementCS)
gen_baseCST_TuplePartCS_TypedElementCS = Generalization(general=TypedElementCS, specific=baseCST_TuplePartCS)
gen_baseCST_TupleTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=baseCST_TupleTypeCS)
gen_baseCST_TupleTypeCS_Nameable = Generalization(general=Nameable, specific=baseCST_TupleTypeCS)
gen_baseCST_TypeCS_ModelElementCS = Generalization(general=ModelElementCS, specific=baseCST_TypeCS)
gen_baseCST_TypeParameterCS_TemplateParameterCS = Generalization(general=TemplateParameterCS, specific=baseCST_TypeParameterCS)
gen_baseCST_TypeParameterCS_TypeCS = Generalization(general=TypeCS, specific=baseCST_TypeParameterCS)
gen_baseCST_TemplateParameterCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_TemplateParameterCS)
gen_baseCST_TemplateParameterSubstitutionCS_ModelElementCS = Generalization(general=ModelElementCS, specific=baseCST_TemplateParameterSubstitutionCS)
gen_baseCST_TemplateSignatureCS_ModelElementCS = Generalization(general=ModelElementCS, specific=baseCST_TemplateSignatureCS)
gen_baseCST_WildcardTypeRefCS_TypeRefCS = Generalization(general=TypeRefCS, specific=baseCST_WildcardTypeRefCS)
gen_baseCST_TypeRefCS_ElementRefCS = Generalization(general=ElementRefCS, specific=baseCST_TypeRefCS)
gen_baseCST_TypedElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=baseCST_TypedElementCS)
gen_baseCST_TypedRefCS_TypeRefCS = Generalization(general=TypeRefCS, specific=baseCST_TypedRefCS)
gen_baseCST_TypedTypeRefCS_TypedRefCS = Generalization(general=TypedRefCS, specific=baseCST_TypedTypeRefCS)

# Domain Model
domain_model = DomainModel(
    name="baseCST",
    types={baseCST_ClassCS, ClassifierCS, NamespaceCS, baseCST_AnnotationCS, AnnotationElementCS, baseCST_ModelElementCS, baseCST_ModelElementRefCS, baseCST_AnnotationElementCS, NamedElementCS, baseCST_DetailCS, baseCST_AttributeCS, StructuralFeatureCS, baseCST_TypedRefCS, baseCST_OperationCS, baseCST_StructuralFeatureCS, baseCST_ClassifierCS, TypeCS, TemplateableElementCS, baseCST_PackageCS, baseCST_ConstraintCS, baseCST_SpecificationCS, baseCST_DataTypeCS, baseCST_EnumerationLiteralCS, baseCST_DocumentationCS, baseCST_ElementCS, VisitableCS, baseCST_ElementRefCS, PivotableElementCS, baseCST_EnumerationCS, baseCST_FeatureCS, TypedElementCS, baseCST_ImportCS, baseCST_PathNameCS, baseCST_Namespace, baseCST_LambdaTypeCS, TypedRefCS, Nameable, baseCST_LibraryCS, ElementRefCS, baseCST_Element, baseCST_MultiplicityBoundsCS, MultiplicityCS, baseCST_MultiplicityCS, ElementCS, baseCST_ParameterCS, baseCST_MultiplicityStringCS, baseCST_NamedElementCS, ModelElementCS, baseCST_NamespaceCS, FeatureCS, baseCST_EClassifier, baseCST_PathElementWithURICS, PathElementCS, baseCST_PathElementCS, Pivotable, baseCST_RootPackageCS, PackageCS, RootCS, baseCST_TemplateBindingCS, baseCST_PivotableElementCS, baseCST_PrimitiveTypeRefCS, baseCST_ReferenceCS, baseCST_Property, baseCST_RootCS, baseCST_TuplePartCS, baseCST_TupleTypeCS, baseCST_TypeCS, baseCST_TypeParameterCS, TemplateParameterCS, baseCST_TypedTypeRefCS, baseCST_TemplateParameterSubstitutionCS, baseCST_TemplateParameterCS, baseCST_TemplateSignatureCS, baseCST_TypeRefCS, baseCST_TemplateableElementCS, baseCST_Type, baseCST_VisitableCS, baseCST_WildcardTypeRefCS, baseCST_TypedElementCS, TypeRefCS, IteratorKind},
    associations={ownedContent0, ownedReference1, ownedDetail3, ownedSuperType4, ownedOperation5, ownedProperty6, ownedMetaType7, owner10, ownedConstraint11, specification12, messageSpecification14, literals17, logicalParent19, ownedLiterals20, pathName22, namespace23, ownedContextType25, ownedParameterType27, ownedResultType30, package33, ownedAnnotation35, pathName38, element41, owningClass43, ownedParameter44, ownedException46, ownedPrecondition48, ownedPostcondition51, ownedBodyExpression54, element64, elementType66, path68, element69, context72, ownedType57, ownedNestedPackage60, owner61, pathName63, ownedImport81, ownedLibrary83, owner86, ownedDefaultExpression88, pivot75, opposite77, keys78, ownedTemplateParameter96, ownedTemplateSignature97, ownedParts99, ownedExtends100, owningTemplateBindableElement90, ownedParameterSubstitution91, owningTemplateSignature92, owningTemplateBinding93, ownedActualParameter94, owningTemplateElement95, type111, ownedTemplateBinding113, extends115, super117, ownedSuper102, ownedType105, multiplicity107, pathName109},
    generalizations={gen_baseCST_ClassCS_ClassifierCS, gen_baseCST_ClassCS_NamespaceCS, gen_baseCST_AnnotationCS_AnnotationElementCS, gen_baseCST_AnnotationElementCS_NamedElementCS, gen_baseCST_AttributeCS_StructuralFeatureCS, gen_baseCST_DetailCS_NamedElementCS, gen_baseCST_ClassifierCS_NamedElementCS, gen_baseCST_ClassifierCS_TypeCS, gen_baseCST_ClassifierCS_TemplateableElementCS, gen_baseCST_ConstraintCS_NamedElementCS, gen_baseCST_DataTypeCS_ClassifierCS, gen_baseCST_DataTypeCS_NamespaceCS, gen_baseCST_DocumentationCS_AnnotationElementCS, gen_baseCST_ElementCS_VisitableCS, gen_baseCST_ElementRefCS_PivotableElementCS, gen_baseCST_EnumerationCS_ClassifierCS, gen_baseCST_EnumerationCS_NamespaceCS, gen_baseCST_EnumerationLiteralCS_NamedElementCS, gen_baseCST_FeatureCS_TypedElementCS, gen_baseCST_ImportCS_NamespaceCS, gen_baseCST_LambdaTypeCS_TypedRefCS, gen_baseCST_LambdaTypeCS_TemplateableElementCS, gen_baseCST_LambdaTypeCS_Nameable, gen_baseCST_LibraryCS_NamespaceCS, gen_baseCST_ModelElementCS_PivotableElementCS, gen_baseCST_ModelElementRefCS_ElementRefCS, gen_baseCST_MultiplicityBoundsCS_MultiplicityCS, gen_baseCST_MultiplicityCS_ElementCS, gen_baseCST_PackageCS_NamespaceCS, gen_baseCST_MultiplicityStringCS_MultiplicityCS, gen_baseCST_NamedElementCS_ModelElementCS, gen_baseCST_NamedElementCS_Nameable, gen_baseCST_NamespaceCS_NamedElementCS, gen_baseCST_OperationCS_FeatureCS, gen_baseCST_OperationCS_TemplateableElementCS, gen_baseCST_PathElementWithURICS_PathElementCS, gen_baseCST_PathNameCS_ElementCS, gen_baseCST_PathNameCS_Pivotable, gen_baseCST_ParameterCS_TypedElementCS, gen_baseCST_PathElementCS_ElementCS, gen_baseCST_PathElementCS_Pivotable, gen_baseCST_RootPackageCS_PackageCS, gen_baseCST_RootPackageCS_RootCS, gen_baseCST_SpecificationCS_ModelElementCS, gen_baseCST_StructuralFeatureCS_FeatureCS, gen_baseCST_TemplateBindingCS_ElementRefCS, gen_baseCST_PivotableElementCS_ElementCS, gen_baseCST_PivotableElementCS_Pivotable, gen_baseCST_PrimitiveTypeRefCS_TypedRefCS, gen_baseCST_PrimitiveTypeRefCS_Nameable, gen_baseCST_ReferenceCS_StructuralFeatureCS, gen_baseCST_RootCS_ModelElementCS, gen_baseCST_TemplateableElementCS_ElementCS, gen_baseCST_TuplePartCS_TypedElementCS, gen_baseCST_TupleTypeCS_TypedRefCS, gen_baseCST_TupleTypeCS_Nameable, gen_baseCST_TypeCS_ModelElementCS, gen_baseCST_TypeParameterCS_TemplateParameterCS, gen_baseCST_TypeParameterCS_TypeCS, gen_baseCST_TemplateParameterCS_NamedElementCS, gen_baseCST_TemplateParameterSubstitutionCS_ModelElementCS, gen_baseCST_TemplateSignatureCS_ModelElementCS, gen_baseCST_WildcardTypeRefCS_TypeRefCS, gen_baseCST_TypeRefCS_ElementRefCS, gen_baseCST_TypedElementCS_NamedElementCS, gen_baseCST_TypedRefCS_TypeRefCS, gen_baseCST_TypedTypeRefCS_TypedRefCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)