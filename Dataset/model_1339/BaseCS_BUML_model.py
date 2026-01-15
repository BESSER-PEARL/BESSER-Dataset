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
basecs_AnnotationCS = Class(name="basecs::AnnotationCS")
AnnotationElementCS = Class(name="AnnotationElementCS")
basecs_ModelElementCS = Class(name="basecs::ModelElementCS", is_abstract=True)
basecs_ModelElementRefCS = Class(name="basecs::ModelElementRefCS")
basecs_AnnotationElementCS = Class(name="basecs::AnnotationElementCS", is_abstract=True)
NamedElementCS = Class(name="NamedElementCS")
basecs_DetailCS = Class(name="basecs::DetailCS")
basecs_AttributeCS = Class(name="basecs::AttributeCS")
StructuralFeatureCS = Class(name="StructuralFeatureCS")
basecs_ClassCS = Class(name="basecs::ClassCS")
ClassifierCS = Class(name="ClassifierCS")
NamespaceCS = Class(name="NamespaceCS")
basecs_TypedRefCS = Class(name="basecs::TypedRefCS", is_abstract=True)
basecs_OperationCS = Class(name="basecs::OperationCS")
basecs_StructuralFeatureCS = Class(name="basecs::StructuralFeatureCS", is_abstract=True)
basecs_ClassifierCS = Class(name="basecs::ClassifierCS", is_abstract=True)
TypeCS = Class(name="TypeCS")
TemplateableElementCS = Class(name="TemplateableElementCS")
basecs_PackageCS = Class(name="basecs::PackageCS")
basecs_ConstraintCS = Class(name="basecs::ConstraintCS")
basecs_SpecificationCS = Class(name="basecs::SpecificationCS")
basecs_DataTypeCS = Class(name="basecs::DataTypeCS")
basecs_DocumentationCS = Class(name="basecs::DocumentationCS")
basecs_ElementCS = Class(name="basecs::ElementCS", is_abstract=True)
VisitableCS = Class(name="VisitableCS")
basecs_ElementRefCS = Class(name="basecs::ElementRefCS", is_abstract=True)
PivotableElementCS = Class(name="PivotableElementCS")
basecs_EnumerationCS = Class(name="basecs::EnumerationCS")
basecs_FeatureCS = Class(name="basecs::FeatureCS", is_abstract=True)
TypedElementCS = Class(name="TypedElementCS")
basecs_ImportCS = Class(name="basecs::ImportCS")
basecs_PathNameCS = Class(name="basecs::PathNameCS")
basecs_Namespace = Class(name="basecs::Namespace")
basecs_LambdaTypeCS = Class(name="basecs::LambdaTypeCS")
TypedRefCS = Class(name="TypedRefCS")
Nameable = Class(name="Nameable")
basecs_EnumerationLiteralCS = Class(name="basecs::EnumerationLiteralCS")
basecs_LibraryCS = Class(name="basecs::LibraryCS")
ElementRefCS = Class(name="ElementRefCS")
basecs_Element = Class(name="basecs::Element")
basecs_MultiplicityBoundsCS = Class(name="basecs::MultiplicityBoundsCS")
MultiplicityCS = Class(name="MultiplicityCS")
basecs_MultiplicityCS = Class(name="basecs::MultiplicityCS", is_abstract=True)
ElementCS = Class(name="ElementCS")
basecs_MultiplicityStringCS = Class(name="basecs::MultiplicityStringCS")
basecs_NamedElementCS = Class(name="basecs::NamedElementCS", is_abstract=True)
ModelElementCS = Class(name="ModelElementCS")
basecs_NamespaceCS = Class(name="basecs::NamespaceCS", is_abstract=True)
FeatureCS = Class(name="FeatureCS")
basecs_ParameterCS = Class(name="basecs::ParameterCS")
PackageOwnerCS = Class(name="PackageOwnerCS")
basecs_PackageOwnerCS = Class(name="basecs::PackageOwnerCS", is_abstract=True)
basecs_PathElementCS = Class(name="basecs::PathElementCS")
Pivotable = Class(name="Pivotable")
basecs_EClassifier = Class(name="basecs::EClassifier")
basecs_PathElementWithURICS = Class(name="basecs::PathElementWithURICS")
PathElementCS = Class(name="PathElementCS")
basecs_PivotableElementCS = Class(name="basecs::PivotableElementCS", is_abstract=True)
basecs_PrimitiveTypeRefCS = Class(name="basecs::PrimitiveTypeRefCS")
basecs_ReferenceCS = Class(name="basecs::ReferenceCS")
basecs_Property = Class(name="basecs::Property")
basecs_RootCS = Class(name="basecs::RootCS", is_abstract=True)
basecs_RootPackageCS = Class(name="basecs::RootPackageCS")
RootCS = Class(name="RootCS")
basecs_TemplateBindingCS = Class(name="basecs::TemplateBindingCS")
basecs_TypedTypeRefCS = Class(name="basecs::TypedTypeRefCS")
basecs_TemplateParameterSubstitutionCS = Class(name="basecs::TemplateParameterSubstitutionCS")
basecs_TemplateParameterCS = Class(name="basecs::TemplateParameterCS", is_abstract=True)
basecs_TemplateSignatureCS = Class(name="basecs::TemplateSignatureCS")
basecs_TypeRefCS = Class(name="basecs::TypeRefCS", is_abstract=True)
basecs_TemplateableElementCS = Class(name="basecs::TemplateableElementCS", is_abstract=True)
basecs_TuplePartCS = Class(name="basecs::TuplePartCS")
basecs_TupleTypeCS = Class(name="basecs::TupleTypeCS")
basecs_TypeCS = Class(name="basecs::TypeCS", is_abstract=True)
basecs_TypeParameterCS = Class(name="basecs::TypeParameterCS")
TemplateParameterCS = Class(name="TemplateParameterCS")
basecs_TypedElementCS = Class(name="basecs::TypedElementCS", is_abstract=True)
TypeRefCS = Class(name="TypeRefCS")
basecs_Type = Class(name="basecs::Type")
basecs_VisitableCS = Class(name="basecs::VisitableCS", is_abstract=True)
basecs_WildcardTypeRefCS = Class(name="basecs::WildcardTypeRefCS")

# basecs_AnnotationCS class attributes and methods

# AnnotationElementCS class attributes and methods

# basecs_ModelElementCS class attributes and methods
basecs_ModelElementCS_originalXmiId: Property = Property(name="originalXmiId", type=StringType)
basecs_ModelElementCS_csi: Property = Property(name="csi", type=StringType)
basecs_ModelElementCS.attributes={basecs_ModelElementCS_csi, basecs_ModelElementCS_originalXmiId}

# basecs_ModelElementRefCS class attributes and methods

# basecs_AnnotationElementCS class attributes and methods

# NamedElementCS class attributes and methods

# basecs_DetailCS class attributes and methods
basecs_DetailCS_value: Property = Property(name="value", type=StringType)
basecs_DetailCS.attributes={basecs_DetailCS_value}

# basecs_AttributeCS class attributes and methods

# StructuralFeatureCS class attributes and methods

# basecs_ClassCS class attributes and methods

# ClassifierCS class attributes and methods

# NamespaceCS class attributes and methods

# basecs_TypedRefCS class attributes and methods

# basecs_OperationCS class attributes and methods
basecs_OperationCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_OperationCS.methods={basecs_OperationCS_m_ast}

# basecs_StructuralFeatureCS class attributes and methods
basecs_StructuralFeatureCS_default: Property = Property(name="default", type=StringType)
basecs_StructuralFeatureCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_StructuralFeatureCS.attributes={basecs_StructuralFeatureCS_default}
basecs_StructuralFeatureCS.methods={basecs_StructuralFeatureCS_m_ast}

# basecs_ClassifierCS class attributes and methods
basecs_ClassifierCS_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
basecs_ClassifierCS_qualifier: Property = Property(name="qualifier", type=StringType)
basecs_ClassifierCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_ClassifierCS.attributes={basecs_ClassifierCS_qualifier, basecs_ClassifierCS_instanceClassName}
basecs_ClassifierCS.methods={basecs_ClassifierCS_m_ast}

# TypeCS class attributes and methods

# TemplateableElementCS class attributes and methods

# basecs_PackageCS class attributes and methods
basecs_PackageCS_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
basecs_PackageCS_nsURI: Property = Property(name="nsURI", type=StringType)
basecs_PackageCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_PackageCS_m_getClassifier: Method = Method(name="getClassifier", parameters={Parameter(name='name')}, type=ClassifierCS)
basecs_PackageCS.attributes={basecs_PackageCS_nsURI, basecs_PackageCS_nsPrefix}
basecs_PackageCS.methods={basecs_PackageCS_m_ast, basecs_PackageCS_m_getClassifier}

# basecs_ConstraintCS class attributes and methods
basecs_ConstraintCS_stereotype: Property = Property(name="stereotype", type=StringType)
basecs_ConstraintCS.attributes={basecs_ConstraintCS_stereotype}

# basecs_SpecificationCS class attributes and methods
basecs_SpecificationCS_exprString: Property = Property(name="exprString", type=StringType)
basecs_SpecificationCS.attributes={basecs_SpecificationCS_exprString}

# basecs_DataTypeCS class attributes and methods

# basecs_DocumentationCS class attributes and methods
basecs_DocumentationCS_value: Property = Property(name="value", type=StringType)
basecs_DocumentationCS.attributes={basecs_DocumentationCS_value}

# basecs_ElementCS class attributes and methods
basecs_ElementCS_m_getDescription: Method = Method(name="getDescription", parameters={}, type=StringType)
basecs_ElementCS.methods={basecs_ElementCS_m_getDescription}

# VisitableCS class attributes and methods

# basecs_ElementRefCS class attributes and methods

# PivotableElementCS class attributes and methods

# basecs_EnumerationCS class attributes and methods
basecs_EnumerationCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_EnumerationCS.methods={basecs_EnumerationCS_m_ast}

# basecs_FeatureCS class attributes and methods

# TypedElementCS class attributes and methods

# basecs_ImportCS class attributes and methods
basecs_ImportCS_all: Property = Property(name="all", type=BooleanType)
basecs_ImportCS.attributes={basecs_ImportCS_all}

# basecs_PathNameCS class attributes and methods
basecs_PathNameCS_scopeFilter: Property = Property(name="scopeFilter", type=StringType)
basecs_PathNameCS.attributes={basecs_PathNameCS_scopeFilter}

# basecs_Namespace class attributes and methods

# basecs_LambdaTypeCS class attributes and methods
basecs_LambdaTypeCS_name: Property = Property(name="name", type=StringType)
basecs_LambdaTypeCS.attributes={basecs_LambdaTypeCS_name}

# TypedRefCS class attributes and methods

# Nameable class attributes and methods

# basecs_EnumerationLiteralCS class attributes and methods
basecs_EnumerationLiteralCS_value: Property = Property(name="value", type=IntegerType)
basecs_EnumerationLiteralCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_EnumerationLiteralCS.attributes={basecs_EnumerationLiteralCS_value}
basecs_EnumerationLiteralCS.methods={basecs_EnumerationLiteralCS_m_ast}

# basecs_LibraryCS class attributes and methods

# ElementRefCS class attributes and methods

# basecs_Element class attributes and methods

# basecs_MultiplicityBoundsCS class attributes and methods
basecs_MultiplicityBoundsCS_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
basecs_MultiplicityBoundsCS_upperBound: Property = Property(name="upperBound", type=StringType)
basecs_MultiplicityBoundsCS.attributes={basecs_MultiplicityBoundsCS_lowerBound, basecs_MultiplicityBoundsCS_upperBound}

# MultiplicityCS class attributes and methods

# basecs_MultiplicityCS class attributes and methods
basecs_MultiplicityCS_m_getLower: Method = Method(name="getLower", parameters={}, type=IntegerType)
basecs_MultiplicityCS_m_getUpper: Method = Method(name="getUpper", parameters={}, type=IntegerType)
basecs_MultiplicityCS.methods={basecs_MultiplicityCS_m_getLower, basecs_MultiplicityCS_m_getUpper}

# ElementCS class attributes and methods

# basecs_MultiplicityStringCS class attributes and methods
basecs_MultiplicityStringCS_stringBounds: Property = Property(name="stringBounds", type=StringType)
basecs_MultiplicityStringCS.attributes={basecs_MultiplicityStringCS_stringBounds}

# basecs_NamedElementCS class attributes and methods
basecs_NamedElementCS_name: Property = Property(name="name", type=StringType)
basecs_NamedElementCS.attributes={basecs_NamedElementCS_name}

# ModelElementCS class attributes and methods

# basecs_NamespaceCS class attributes and methods

# FeatureCS class attributes and methods

# basecs_ParameterCS class attributes and methods
basecs_ParameterCS_m_ast: Method = Method(name="ast", parameters={}, type=StringType)
basecs_ParameterCS.methods={basecs_ParameterCS_m_ast}

# PackageOwnerCS class attributes and methods

# basecs_PackageOwnerCS class attributes and methods

# basecs_PathElementCS class attributes and methods

# Pivotable class attributes and methods

# basecs_EClassifier class attributes and methods

# basecs_PathElementWithURICS class attributes and methods
basecs_PathElementWithURICS_uri: Property = Property(name="uri", type=StringType)
basecs_PathElementWithURICS.attributes={basecs_PathElementWithURICS_uri}

# PathElementCS class attributes and methods

# basecs_PivotableElementCS class attributes and methods

# basecs_PrimitiveTypeRefCS class attributes and methods
basecs_PrimitiveTypeRefCS_name: Property = Property(name="name", type=StringType)
basecs_PrimitiveTypeRefCS.attributes={basecs_PrimitiveTypeRefCS_name}

# basecs_ReferenceCS class attributes and methods

# basecs_Property class attributes and methods

# basecs_RootCS class attributes and methods

# basecs_RootPackageCS class attributes and methods

# RootCS class attributes and methods

# basecs_TemplateBindingCS class attributes and methods

# basecs_TypedTypeRefCS class attributes and methods

# basecs_TemplateParameterSubstitutionCS class attributes and methods

# basecs_TemplateParameterCS class attributes and methods

# basecs_TemplateSignatureCS class attributes and methods

# basecs_TypeRefCS class attributes and methods

# basecs_TemplateableElementCS class attributes and methods

# basecs_TuplePartCS class attributes and methods

# basecs_TupleTypeCS class attributes and methods
basecs_TupleTypeCS_name: Property = Property(name="name", type=StringType)
basecs_TupleTypeCS.attributes={basecs_TupleTypeCS_name}

# basecs_TypeCS class attributes and methods

# basecs_TypeParameterCS class attributes and methods

# TemplateParameterCS class attributes and methods

# basecs_TypedElementCS class attributes and methods
basecs_TypedElementCS_qualifier: Property = Property(name="qualifier", type=StringType)
basecs_TypedElementCS_optional: Property = Property(name="optional", type=BooleanType)
basecs_TypedElementCS.attributes={basecs_TypedElementCS_optional, basecs_TypedElementCS_qualifier}

# TypeRefCS class attributes and methods

# basecs_Type class attributes and methods

# basecs_VisitableCS class attributes and methods

# basecs_WildcardTypeRefCS class attributes and methods

# Relationships
ownedContent0: BinaryAssociation = BinaryAssociation(
    name="ownedContent0",
    ends={
        Property(name="basecs_ModelElementCS", type=basecs_AnnotationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_AnnotationCS", type=basecs_ModelElementCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedReference1: BinaryAssociation = BinaryAssociation(
    name="ownedReference1",
    ends={
        Property(name="basecs_ModelElementRefCS", type=basecs_AnnotationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_AnnotationCS2", type=basecs_ModelElementRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSuperType4: BinaryAssociation = BinaryAssociation(
    name="ownedSuperType4",
    ends={
        Property(name="basecs_TypedRefCS", type=basecs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ClassCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation5: BinaryAssociation = BinaryAssociation(
    name="ownedOperation5",
    ends={
        Property(name="OperationCS", type=basecs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass", type=basecs_OperationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty6: BinaryAssociation = BinaryAssociation(
    name="ownedProperty6",
    ends={
        Property(name="StructuralFeatureCS", type=basecs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=basecs_StructuralFeatureCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedMetaType7: BinaryAssociation = BinaryAssociation(
    name="ownedMetaType7",
    ends={
        Property(name="basecs_TypedRefCS9", type=basecs_ClassCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ClassCS8", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner10: BinaryAssociation = BinaryAssociation(
    name="owner10",
    ends={
        Property(name="PackageCS", type=basecs_ClassifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=basecs_PackageCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedConstraint11: BinaryAssociation = BinaryAssociation(
    name="ownedConstraint11",
    ends={
        Property(name="basecs_ConstraintCS", type=basecs_ClassifierCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ClassifierCS", type=basecs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification12: BinaryAssociation = BinaryAssociation(
    name="specification12",
    ends={
        Property(name="basecs_SpecificationCS", type=basecs_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ConstraintCS13", type=basecs_SpecificationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messageSpecification14: BinaryAssociation = BinaryAssociation(
    name="messageSpecification14",
    ends={
        Property(name="basecs_SpecificationCS16", type=basecs_ConstraintCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ConstraintCS15", type=basecs_SpecificationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDetail3: BinaryAssociation = BinaryAssociation(
    name="ownedDetail3",
    ends={
        Property(name="basecs_DetailCS", type=basecs_AnnotationElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_AnnotationElementCS", type=basecs_DetailCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals17: BinaryAssociation = BinaryAssociation(
    name="literals17",
    ends={
        Property(name="basecs_EnumerationLiteralCS", type=basecs_DataTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_DataTypeCS", type=basecs_EnumerationLiteralCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalParent19: BinaryAssociation = BinaryAssociation(
    name="logicalParent19",
    ends={
        Property(name="basecs_ElementCS", type=basecs_ElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ElementCS18", type=basecs_ElementCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiterals20: BinaryAssociation = BinaryAssociation(
    name="ownedLiterals20",
    ends={
        Property(name="basecs_EnumerationLiteralCS21", type=basecs_EnumerationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_EnumerationCS", type=basecs_EnumerationLiteralCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName22: BinaryAssociation = BinaryAssociation(
    name="pathName22",
    ends={
        Property(name="basecs_PathNameCS", type=basecs_ImportCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ImportCS", type=basecs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namespace23: BinaryAssociation = BinaryAssociation(
    name="namespace23",
    ends={
        Property(name="basecs_Namespace", type=basecs_ImportCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ImportCS24", type=basecs_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedContextType25: BinaryAssociation = BinaryAssociation(
    name="ownedContextType25",
    ends={
        Property(name="basecs_TypedRefCS26", type=basecs_LambdaTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_LambdaTypeCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameterType27: BinaryAssociation = BinaryAssociation(
    name="ownedParameterType27",
    ends={
        Property(name="basecs_TypedRefCS29", type=basecs_LambdaTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_LambdaTypeCS28", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedResultType30: BinaryAssociation = BinaryAssociation(
    name="ownedResultType30",
    ends={
        Property(name="basecs_TypedRefCS32", type=basecs_LambdaTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_LambdaTypeCS31", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package33: BinaryAssociation = BinaryAssociation(
    name="package33",
    ends={
        Property(name="basecs_Namespace34", type=basecs_LibraryCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_LibraryCS", type=basecs_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedAnnotation35: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotation35",
    ends={
        Property(name="basecs_AnnotationElementCS37", type=basecs_ModelElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ModelElementCS36", type=basecs_AnnotationElementCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pathName38: BinaryAssociation = BinaryAssociation(
    name="pathName38",
    ends={
        Property(name="basecs_PathNameCS40", type=basecs_ModelElementRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ModelElementRefCS39", type=basecs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element41: BinaryAssociation = BinaryAssociation(
    name="element41",
    ends={
        Property(name="basecs_Element", type=basecs_ModelElementRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ModelElementRefCS42", type=basecs_Element, multiplicity=Multiplicity(0, 1))
    }
)
owningClass43: BinaryAssociation = BinaryAssociation(
    name="owningClass43",
    ends={
        Property(name="ClassCS", type=basecs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=basecs_ClassCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter44: BinaryAssociation = BinaryAssociation(
    name="ownedParameter44",
    ends={
        Property(name="ParameterCS", type=basecs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owner45", type=basecs_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedException46: BinaryAssociation = BinaryAssociation(
    name="ownedException46",
    ends={
        Property(name="basecs_TypedRefCS47", type=basecs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_OperationCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPrecondition48: BinaryAssociation = BinaryAssociation(
    name="ownedPrecondition48",
    ends={
        Property(name="basecs_ConstraintCS50", type=basecs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_OperationCS49", type=basecs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPostcondition51: BinaryAssociation = BinaryAssociation(
    name="ownedPostcondition51",
    ends={
        Property(name="basecs_ConstraintCS53", type=basecs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_OperationCS52", type=basecs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBodyExpression54: BinaryAssociation = BinaryAssociation(
    name="ownedBodyExpression54",
    ends={
        Property(name="basecs_SpecificationCS56", type=basecs_OperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_OperationCS55", type=basecs_SpecificationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType57: BinaryAssociation = BinaryAssociation(
    name="ownedType57",
    ends={
        Property(name="ClassifierCS", type=basecs_PackageCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owner58", type=basecs_ClassifierCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedNestedPackage59: BinaryAssociation = BinaryAssociation(
    name="ownedNestedPackage59",
    ends={
        Property(name="basecs_PackageCS", type=basecs_PackageOwnerCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_PackageOwnerCS", type=basecs_PackageCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner60: BinaryAssociation = BinaryAssociation(
    name="owner60",
    ends={
        Property(name="OperationCS61", type=basecs_ParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=basecs_OperationCS, multiplicity=Multiplicity(0, 1))
    }
)
pathName62: BinaryAssociation = BinaryAssociation(
    name="pathName62",
    ends={
        Property(name="PathNameCS", type=basecs_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="path", type=basecs_PathNameCS, multiplicity=Multiplicity(1, 1))
    }
)
element63: BinaryAssociation = BinaryAssociation(
    name="element63",
    ends={
        Property(name="basecs_Element64", type=basecs_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_PathElementCS", type=basecs_Element, multiplicity=Multiplicity(1, 1))
    }
)
elementType65: BinaryAssociation = BinaryAssociation(
    name="elementType65",
    ends={
        Property(name="basecs_EClassifier", type=basecs_PathElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_PathElementCS66", type=basecs_EClassifier, multiplicity=Multiplicity(0, 1))
    }
)
path67: BinaryAssociation = BinaryAssociation(
    name="path67",
    ends={
        Property(name="PathElementCS", type=basecs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="pathName", type=basecs_PathElementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
element68: BinaryAssociation = BinaryAssociation(
    name="element68",
    ends={
        Property(name="basecs_Element70", type=basecs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_PathNameCS69", type=basecs_Element, multiplicity=Multiplicity(1, 1))
    }
)
context71: BinaryAssociation = BinaryAssociation(
    name="context71",
    ends={
        Property(name="basecs_ElementCS73", type=basecs_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_PathNameCS72", type=basecs_ElementCS, multiplicity=Multiplicity(0, 1))
    }
)
pivot74: BinaryAssociation = BinaryAssociation(
    name="pivot74",
    ends={
        Property(name="basecs_Element75", type=basecs_PivotableElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_PivotableElementCS", type=basecs_Element, multiplicity=Multiplicity(0, 1))
    }
)
opposite76: BinaryAssociation = BinaryAssociation(
    name="opposite76",
    ends={
        Property(name="basecs_Property", type=basecs_ReferenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ReferenceCS", type=basecs_Property, multiplicity=Multiplicity(0, 1))
    }
)
ownedImport80: BinaryAssociation = BinaryAssociation(
    name="ownedImport80",
    ends={
        Property(name="basecs_ImportCS81", type=basecs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_RootCS", type=basecs_ImportCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLibrary82: BinaryAssociation = BinaryAssociation(
    name="ownedLibrary82",
    ends={
        Property(name="basecs_LibraryCS84", type=basecs_RootCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_RootCS83", type=basecs_LibraryCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner85: BinaryAssociation = BinaryAssociation(
    name="owner85",
    ends={
        Property(name="ClassCS86", type=basecs_StructuralFeatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedProperty", type=basecs_ClassCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefaultExpression87: BinaryAssociation = BinaryAssociation(
    name="ownedDefaultExpression87",
    ends={
        Property(name="basecs_SpecificationCS88", type=basecs_StructuralFeatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_StructuralFeatureCS", type=basecs_SpecificationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningTemplateBindableElement89: BinaryAssociation = BinaryAssociation(
    name="owningTemplateBindableElement89",
    ends={
        Property(name="TypedTypeRefCS", type=basecs_TemplateBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateBinding", type=basecs_TypedTypeRefCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameterSubstitution90: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSubstitution90",
    ends={
        Property(name="TemplateParameterSubstitutionCS", type=basecs_TemplateBindingCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateBinding", type=basecs_TemplateParameterSubstitutionCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningTemplateSignature91: BinaryAssociation = BinaryAssociation(
    name="owningTemplateSignature91",
    ends={
        Property(name="TemplateSignatureCS", type=basecs_TemplateParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateParameter", type=basecs_TemplateSignatureCS, multiplicity=Multiplicity(1, 1))
    }
)
keys77: BinaryAssociation = BinaryAssociation(
    name="keys77",
    ends={
        Property(name="basecs_Property79", type=basecs_ReferenceCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_ReferenceCS78", type=basecs_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedActualParameter93: BinaryAssociation = BinaryAssociation(
    name="ownedActualParameter93",
    ends={
        Property(name="basecs_TypeRefCS", type=basecs_TemplateParameterSubstitutionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TemplateParameterSubstitutionCS", type=basecs_TypeRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningTemplateElement94: BinaryAssociation = BinaryAssociation(
    name="owningTemplateElement94",
    ends={
        Property(name="TemplateableElementCS", type=basecs_TemplateSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=basecs_TemplateableElementCS, multiplicity=Multiplicity(0, 1))
    }
)
ownedTemplateParameter95: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateParameter95",
    ends={
        Property(name="TemplateParameterCS", type=basecs_TemplateSignatureCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateSignature", type=basecs_TemplateParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature96: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature96",
    ends={
        Property(name="TemplateSignatureCS97", type=basecs_TemplateableElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateElement", type=basecs_TemplateSignatureCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParts98: BinaryAssociation = BinaryAssociation(
    name="ownedParts98",
    ends={
        Property(name="basecs_TuplePartCS", type=basecs_TupleTypeCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TupleTypeCS", type=basecs_TuplePartCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtends99: BinaryAssociation = BinaryAssociation(
    name="ownedExtends99",
    ends={
        Property(name="basecs_TypedRefCS100", type=basecs_TypeParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TypeParameterCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSuper101: BinaryAssociation = BinaryAssociation(
    name="ownedSuper101",
    ends={
        Property(name="basecs_TypedRefCS103", type=basecs_TypeParameterCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TypeParameterCS102", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedType104: BinaryAssociation = BinaryAssociation(
    name="ownedType104",
    ends={
        Property(name="basecs_TypedRefCS105", type=basecs_TypedElementCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TypedElementCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningTemplateBinding92: BinaryAssociation = BinaryAssociation(
    name="owningTemplateBinding92",
    ends={
        Property(name="TemplateBindingCS", type=basecs_TemplateParameterSubstitutionCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameterSubstitution", type=basecs_TemplateBindingCS, multiplicity=Multiplicity(0, 1))
    }
)
pathName108: BinaryAssociation = BinaryAssociation(
    name="pathName108",
    ends={
        Property(name="basecs_PathNameCS109", type=basecs_TypedTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TypedTypeRefCS", type=basecs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type110: BinaryAssociation = BinaryAssociation(
    name="type110",
    ends={
        Property(name="basecs_Type", type=basecs_TypedTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TypedTypeRefCS111", type=basecs_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedTemplateBinding112: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateBinding112",
    ends={
        Property(name="TemplateBindingCS113", type=basecs_TypedTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateBindableElement", type=basecs_TemplateBindingCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends114: BinaryAssociation = BinaryAssociation(
    name="extends114",
    ends={
        Property(name="basecs_TypedRefCS115", type=basecs_WildcardTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_WildcardTypeRefCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
super116: BinaryAssociation = BinaryAssociation(
    name="super116",
    ends={
        Property(name="basecs_TypedRefCS118", type=basecs_WildcardTypeRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_WildcardTypeRefCS117", type=basecs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiplicity106: BinaryAssociation = BinaryAssociation(
    name="multiplicity106",
    ends={
        Property(name="basecs_MultiplicityCS", type=basecs_TypedRefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="basecs_TypedRefCS107", type=basecs_MultiplicityCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_basecs_AnnotationCS_AnnotationElementCS = Generalization(general=AnnotationElementCS, specific=basecs_AnnotationCS)
gen_basecs_AnnotationElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_AnnotationElementCS)
gen_basecs_AttributeCS_StructuralFeatureCS = Generalization(general=StructuralFeatureCS, specific=basecs_AttributeCS)
gen_basecs_ClassCS_ClassifierCS = Generalization(general=ClassifierCS, specific=basecs_ClassCS)
gen_basecs_ClassCS_NamespaceCS = Generalization(general=NamespaceCS, specific=basecs_ClassCS)
gen_basecs_ClassifierCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_ClassifierCS)
gen_basecs_ClassifierCS_TypeCS = Generalization(general=TypeCS, specific=basecs_ClassifierCS)
gen_basecs_ClassifierCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=basecs_ClassifierCS)
gen_basecs_ConstraintCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_ConstraintCS)
gen_basecs_DataTypeCS_ClassifierCS = Generalization(general=ClassifierCS, specific=basecs_DataTypeCS)
gen_basecs_DataTypeCS_NamespaceCS = Generalization(general=NamespaceCS, specific=basecs_DataTypeCS)
gen_basecs_DetailCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_DetailCS)
gen_basecs_DocumentationCS_AnnotationElementCS = Generalization(general=AnnotationElementCS, specific=basecs_DocumentationCS)
gen_basecs_ElementCS_VisitableCS = Generalization(general=VisitableCS, specific=basecs_ElementCS)
gen_basecs_ElementRefCS_PivotableElementCS = Generalization(general=PivotableElementCS, specific=basecs_ElementRefCS)
gen_basecs_EnumerationCS_ClassifierCS = Generalization(general=ClassifierCS, specific=basecs_EnumerationCS)
gen_basecs_EnumerationCS_NamespaceCS = Generalization(general=NamespaceCS, specific=basecs_EnumerationCS)
gen_basecs_EnumerationLiteralCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_EnumerationLiteralCS)
gen_basecs_FeatureCS_TypedElementCS = Generalization(general=TypedElementCS, specific=basecs_FeatureCS)
gen_basecs_ImportCS_NamespaceCS = Generalization(general=NamespaceCS, specific=basecs_ImportCS)
gen_basecs_LambdaTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=basecs_LambdaTypeCS)
gen_basecs_LambdaTypeCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=basecs_LambdaTypeCS)
gen_basecs_LambdaTypeCS_Nameable = Generalization(general=Nameable, specific=basecs_LambdaTypeCS)
gen_basecs_LibraryCS_NamespaceCS = Generalization(general=NamespaceCS, specific=basecs_LibraryCS)
gen_basecs_ModelElementCS_PivotableElementCS = Generalization(general=PivotableElementCS, specific=basecs_ModelElementCS)
gen_basecs_ModelElementRefCS_ElementRefCS = Generalization(general=ElementRefCS, specific=basecs_ModelElementRefCS)
gen_basecs_MultiplicityBoundsCS_MultiplicityCS = Generalization(general=MultiplicityCS, specific=basecs_MultiplicityBoundsCS)
gen_basecs_MultiplicityCS_ElementCS = Generalization(general=ElementCS, specific=basecs_MultiplicityCS)
gen_basecs_MultiplicityStringCS_MultiplicityCS = Generalization(general=MultiplicityCS, specific=basecs_MultiplicityStringCS)
gen_basecs_NamespaceCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_NamespaceCS)
gen_basecs_OperationCS_FeatureCS = Generalization(general=FeatureCS, specific=basecs_OperationCS)
gen_basecs_OperationCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=basecs_OperationCS)
gen_basecs_PackageCS_PackageOwnerCS = Generalization(general=PackageOwnerCS, specific=basecs_PackageCS)
gen_basecs_PackageCS_NamespaceCS = Generalization(general=NamespaceCS, specific=basecs_PackageCS)
gen_basecs_PackageOwnerCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_PackageOwnerCS)
gen_basecs_NamedElementCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_NamedElementCS)
gen_basecs_NamedElementCS_Nameable = Generalization(general=Nameable, specific=basecs_NamedElementCS)
gen_basecs_PathElementCS_ElementCS = Generalization(general=ElementCS, specific=basecs_PathElementCS)
gen_basecs_PathElementCS_Pivotable = Generalization(general=Pivotable, specific=basecs_PathElementCS)
gen_basecs_PathElementWithURICS_PathElementCS = Generalization(general=PathElementCS, specific=basecs_PathElementWithURICS)
gen_basecs_PathNameCS_ElementCS = Generalization(general=ElementCS, specific=basecs_PathNameCS)
gen_basecs_PathNameCS_Pivotable = Generalization(general=Pivotable, specific=basecs_PathNameCS)
gen_basecs_PivotableElementCS_ElementCS = Generalization(general=ElementCS, specific=basecs_PivotableElementCS)
gen_basecs_PivotableElementCS_Pivotable = Generalization(general=Pivotable, specific=basecs_PivotableElementCS)
gen_basecs_PrimitiveTypeRefCS_TypedRefCS = Generalization(general=TypedRefCS, specific=basecs_PrimitiveTypeRefCS)
gen_basecs_PrimitiveTypeRefCS_Nameable = Generalization(general=Nameable, specific=basecs_PrimitiveTypeRefCS)
gen_basecs_ReferenceCS_StructuralFeatureCS = Generalization(general=StructuralFeatureCS, specific=basecs_ReferenceCS)
gen_basecs_ParameterCS_TypedElementCS = Generalization(general=TypedElementCS, specific=basecs_ParameterCS)
gen_basecs_RootCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_RootCS)
gen_basecs_RootPackageCS_PackageOwnerCS = Generalization(general=PackageOwnerCS, specific=basecs_RootPackageCS)
gen_basecs_RootPackageCS_RootCS = Generalization(general=RootCS, specific=basecs_RootPackageCS)
gen_basecs_SpecificationCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_SpecificationCS)
gen_basecs_StructuralFeatureCS_FeatureCS = Generalization(general=FeatureCS, specific=basecs_StructuralFeatureCS)
gen_basecs_TemplateBindingCS_ElementRefCS = Generalization(general=ElementRefCS, specific=basecs_TemplateBindingCS)
gen_basecs_TemplateParameterCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_TemplateParameterCS)
gen_basecs_TemplateParameterSubstitutionCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_TemplateParameterSubstitutionCS)
gen_basecs_TemplateSignatureCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_TemplateSignatureCS)
gen_basecs_TemplateableElementCS_ElementCS = Generalization(general=ElementCS, specific=basecs_TemplateableElementCS)
gen_basecs_TuplePartCS_TypedElementCS = Generalization(general=TypedElementCS, specific=basecs_TuplePartCS)
gen_basecs_TupleTypeCS_TypedRefCS = Generalization(general=TypedRefCS, specific=basecs_TupleTypeCS)
gen_basecs_TupleTypeCS_Nameable = Generalization(general=Nameable, specific=basecs_TupleTypeCS)
gen_basecs_TypeCS_ModelElementCS = Generalization(general=ModelElementCS, specific=basecs_TypeCS)
gen_basecs_TypeParameterCS_TemplateParameterCS = Generalization(general=TemplateParameterCS, specific=basecs_TypeParameterCS)
gen_basecs_TypeParameterCS_TypeCS = Generalization(general=TypeCS, specific=basecs_TypeParameterCS)
gen_basecs_TypeRefCS_ElementRefCS = Generalization(general=ElementRefCS, specific=basecs_TypeRefCS)
gen_basecs_TypedElementCS_NamedElementCS = Generalization(general=NamedElementCS, specific=basecs_TypedElementCS)
gen_basecs_TypedRefCS_TypeRefCS = Generalization(general=TypeRefCS, specific=basecs_TypedRefCS)
gen_basecs_TypedTypeRefCS_TypedRefCS = Generalization(general=TypedRefCS, specific=basecs_TypedTypeRefCS)
gen_basecs_WildcardTypeRefCS_TypeRefCS = Generalization(general=TypeRefCS, specific=basecs_WildcardTypeRefCS)

# Domain Model
domain_model = DomainModel(
    name="basecs",
    types={basecs_AnnotationCS, AnnotationElementCS, basecs_ModelElementCS, basecs_ModelElementRefCS, basecs_AnnotationElementCS, NamedElementCS, basecs_DetailCS, basecs_AttributeCS, StructuralFeatureCS, basecs_ClassCS, ClassifierCS, NamespaceCS, basecs_TypedRefCS, basecs_OperationCS, basecs_StructuralFeatureCS, basecs_ClassifierCS, TypeCS, TemplateableElementCS, basecs_PackageCS, basecs_ConstraintCS, basecs_SpecificationCS, basecs_DataTypeCS, basecs_DocumentationCS, basecs_ElementCS, VisitableCS, basecs_ElementRefCS, PivotableElementCS, basecs_EnumerationCS, basecs_FeatureCS, TypedElementCS, basecs_ImportCS, basecs_PathNameCS, basecs_Namespace, basecs_LambdaTypeCS, TypedRefCS, Nameable, basecs_EnumerationLiteralCS, basecs_LibraryCS, ElementRefCS, basecs_Element, basecs_MultiplicityBoundsCS, MultiplicityCS, basecs_MultiplicityCS, ElementCS, basecs_MultiplicityStringCS, basecs_NamedElementCS, ModelElementCS, basecs_NamespaceCS, FeatureCS, basecs_ParameterCS, PackageOwnerCS, basecs_PackageOwnerCS, basecs_PathElementCS, Pivotable, basecs_EClassifier, basecs_PathElementWithURICS, PathElementCS, basecs_PivotableElementCS, basecs_PrimitiveTypeRefCS, basecs_ReferenceCS, basecs_Property, basecs_RootCS, basecs_RootPackageCS, RootCS, basecs_TemplateBindingCS, basecs_TypedTypeRefCS, basecs_TemplateParameterSubstitutionCS, basecs_TemplateParameterCS, basecs_TemplateSignatureCS, basecs_TypeRefCS, basecs_TemplateableElementCS, basecs_TuplePartCS, basecs_TupleTypeCS, basecs_TypeCS, basecs_TypeParameterCS, TemplateParameterCS, basecs_TypedElementCS, TypeRefCS, basecs_Type, basecs_VisitableCS, basecs_WildcardTypeRefCS, IteratorKind},
    associations={ownedContent0, ownedReference1, ownedSuperType4, ownedOperation5, ownedProperty6, ownedMetaType7, owner10, ownedConstraint11, specification12, messageSpecification14, ownedDetail3, literals17, logicalParent19, ownedLiterals20, pathName22, namespace23, ownedContextType25, ownedParameterType27, ownedResultType30, package33, ownedAnnotation35, pathName38, element41, owningClass43, ownedParameter44, ownedException46, ownedPrecondition48, ownedPostcondition51, ownedBodyExpression54, ownedType57, ownedNestedPackage59, owner60, pathName62, element63, elementType65, path67, element68, context71, pivot74, opposite76, ownedImport80, ownedLibrary82, owner85, ownedDefaultExpression87, owningTemplateBindableElement89, ownedParameterSubstitution90, owningTemplateSignature91, keys77, ownedActualParameter93, owningTemplateElement94, ownedTemplateParameter95, ownedTemplateSignature96, ownedParts98, ownedExtends99, ownedSuper101, ownedType104, owningTemplateBinding92, pathName108, type110, ownedTemplateBinding112, extends114, super116, multiplicity106},
    generalizations={gen_basecs_AnnotationCS_AnnotationElementCS, gen_basecs_AnnotationElementCS_NamedElementCS, gen_basecs_AttributeCS_StructuralFeatureCS, gen_basecs_ClassCS_ClassifierCS, gen_basecs_ClassCS_NamespaceCS, gen_basecs_ClassifierCS_NamedElementCS, gen_basecs_ClassifierCS_TypeCS, gen_basecs_ClassifierCS_TemplateableElementCS, gen_basecs_ConstraintCS_NamedElementCS, gen_basecs_DataTypeCS_ClassifierCS, gen_basecs_DataTypeCS_NamespaceCS, gen_basecs_DetailCS_NamedElementCS, gen_basecs_DocumentationCS_AnnotationElementCS, gen_basecs_ElementCS_VisitableCS, gen_basecs_ElementRefCS_PivotableElementCS, gen_basecs_EnumerationCS_ClassifierCS, gen_basecs_EnumerationCS_NamespaceCS, gen_basecs_EnumerationLiteralCS_NamedElementCS, gen_basecs_FeatureCS_TypedElementCS, gen_basecs_ImportCS_NamespaceCS, gen_basecs_LambdaTypeCS_TypedRefCS, gen_basecs_LambdaTypeCS_TemplateableElementCS, gen_basecs_LambdaTypeCS_Nameable, gen_basecs_LibraryCS_NamespaceCS, gen_basecs_ModelElementCS_PivotableElementCS, gen_basecs_ModelElementRefCS_ElementRefCS, gen_basecs_MultiplicityBoundsCS_MultiplicityCS, gen_basecs_MultiplicityCS_ElementCS, gen_basecs_MultiplicityStringCS_MultiplicityCS, gen_basecs_NamespaceCS_NamedElementCS, gen_basecs_OperationCS_FeatureCS, gen_basecs_OperationCS_TemplateableElementCS, gen_basecs_PackageCS_PackageOwnerCS, gen_basecs_PackageCS_NamespaceCS, gen_basecs_PackageOwnerCS_ModelElementCS, gen_basecs_NamedElementCS_ModelElementCS, gen_basecs_NamedElementCS_Nameable, gen_basecs_PathElementCS_ElementCS, gen_basecs_PathElementCS_Pivotable, gen_basecs_PathElementWithURICS_PathElementCS, gen_basecs_PathNameCS_ElementCS, gen_basecs_PathNameCS_Pivotable, gen_basecs_PivotableElementCS_ElementCS, gen_basecs_PivotableElementCS_Pivotable, gen_basecs_PrimitiveTypeRefCS_TypedRefCS, gen_basecs_PrimitiveTypeRefCS_Nameable, gen_basecs_ReferenceCS_StructuralFeatureCS, gen_basecs_ParameterCS_TypedElementCS, gen_basecs_RootCS_ModelElementCS, gen_basecs_RootPackageCS_PackageOwnerCS, gen_basecs_RootPackageCS_RootCS, gen_basecs_SpecificationCS_ModelElementCS, gen_basecs_StructuralFeatureCS_FeatureCS, gen_basecs_TemplateBindingCS_ElementRefCS, gen_basecs_TemplateParameterCS_NamedElementCS, gen_basecs_TemplateParameterSubstitutionCS_ModelElementCS, gen_basecs_TemplateSignatureCS_ModelElementCS, gen_basecs_TemplateableElementCS_ElementCS, gen_basecs_TuplePartCS_TypedElementCS, gen_basecs_TupleTypeCS_TypedRefCS, gen_basecs_TupleTypeCS_Nameable, gen_basecs_TypeCS_ModelElementCS, gen_basecs_TypeParameterCS_TemplateParameterCS, gen_basecs_TypeParameterCS_TypeCS, gen_basecs_TypeRefCS_ElementRefCS, gen_basecs_TypedElementCS_NamedElementCS, gen_basecs_TypedRefCS_TypeRefCS, gen_basecs_TypedTypeRefCS_TypedRefCS, gen_basecs_WildcardTypeRefCS_TypeRefCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)