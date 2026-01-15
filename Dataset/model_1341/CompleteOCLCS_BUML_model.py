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
completeoclcs_ConstraintCS = Class(name="completeoclcs::ConstraintCS")
completeoclcs_Class = Class(name="completeoclcs::Class")
completeoclcs_CompleteOCLDocumentCS = Class(name="completeoclcs::CompleteOCLDocumentCS")
NamespaceCS = Class(name="NamespaceCS")
RootCS = Class(name="RootCS")
completeoclcs_ClassifierContextDeclCS = Class(name="completeoclcs::ClassifierContextDeclCS")
ContextDeclCS = Class(name="ContextDeclCS")
TemplateableElementCS = Class(name="TemplateableElementCS")
completeoclcs_DefCS = Class(name="completeoclcs::DefCS", is_abstract=True)
completeoclcs_DefOperationCS = Class(name="completeoclcs::DefOperationCS")
DefCS = Class(name="DefCS")
completeoclcs_ParameterCS = Class(name="completeoclcs::ParameterCS")
completeoclcs_DefPropertyCS = Class(name="completeoclcs::DefPropertyCS")
completeoclcs_FeatureContextDeclCS = Class(name="completeoclcs::FeatureContextDeclCS", is_abstract=True)
completeoclcs_TypedRefCS = Class(name="completeoclcs::TypedRefCS")
completeoclcs_ContextDeclCS = Class(name="completeoclcs::ContextDeclCS", is_abstract=True)
completeoclcs_PackageDeclarationCS = Class(name="completeoclcs::PackageDeclarationCS")
PathNameDeclCS = Class(name="PathNameDeclCS")
TypedElementCS = Class(name="TypedElementCS")
completeoclcs_ExpSpecificationCS = Class(name="completeoclcs::ExpSpecificationCS")
completeoclcs_Package = Class(name="completeoclcs::Package")
completeoclcs_PathNameDeclCS = Class(name="completeoclcs::PathNameDeclCS", is_abstract=True)
ModelElementCS = Class(name="ModelElementCS")
MorePivotable = Class(name="MorePivotable")
completeoclcs_PathNameCS = Class(name="completeoclcs::PathNameCS")
completeoclcs_PropertyContextDeclCS = Class(name="completeoclcs::PropertyContextDeclCS")
completeoclcs_OCLMessageArgCS = Class(name="completeoclcs::OCLMessageArgCS")
ExpCS = Class(name="ExpCS")
completeoclcs_OperationContextDeclCS = Class(name="completeoclcs::OperationContextDeclCS")
FeatureContextDeclCS = Class(name="FeatureContextDeclCS")
completeoclcs_VariableCS = Class(name="completeoclcs::VariableCS")
completeoclcs_Operation = Class(name="completeoclcs::Operation")
completeoclcs_Property = Class(name="completeoclcs::Property")

# completeoclcs_ConstraintCS class attributes and methods

# completeoclcs_Class class attributes and methods

# completeoclcs_CompleteOCLDocumentCS class attributes and methods

# NamespaceCS class attributes and methods

# RootCS class attributes and methods

# completeoclcs_ClassifierContextDeclCS class attributes and methods
completeoclcs_ClassifierContextDeclCS_selfName: Property = Property(name="selfName", type=StringType)
completeoclcs_ClassifierContextDeclCS.attributes={completeoclcs_ClassifierContextDeclCS_selfName}

# ContextDeclCS class attributes and methods

# TemplateableElementCS class attributes and methods

# completeoclcs_DefCS class attributes and methods
completeoclcs_DefCS_isStatic: Property = Property(name="isStatic", type=BooleanType)
completeoclcs_DefCS.attributes={completeoclcs_DefCS_isStatic}

# completeoclcs_DefOperationCS class attributes and methods

# DefCS class attributes and methods

# completeoclcs_ParameterCS class attributes and methods

# completeoclcs_DefPropertyCS class attributes and methods

# completeoclcs_FeatureContextDeclCS class attributes and methods

# completeoclcs_TypedRefCS class attributes and methods

# completeoclcs_ContextDeclCS class attributes and methods

# completeoclcs_PackageDeclarationCS class attributes and methods

# PathNameDeclCS class attributes and methods

# TypedElementCS class attributes and methods

# completeoclcs_ExpSpecificationCS class attributes and methods

# completeoclcs_Package class attributes and methods

# completeoclcs_PathNameDeclCS class attributes and methods

# ModelElementCS class attributes and methods

# MorePivotable class attributes and methods

# completeoclcs_PathNameCS class attributes and methods

# completeoclcs_PropertyContextDeclCS class attributes and methods

# completeoclcs_OCLMessageArgCS class attributes and methods

# ExpCS class attributes and methods

# completeoclcs_OperationContextDeclCS class attributes and methods

# FeatureContextDeclCS class attributes and methods

# completeoclcs_VariableCS class attributes and methods

# completeoclcs_Operation class attributes and methods

# completeoclcs_Property class attributes and methods

# Relationships
ownedInvariants1: BinaryAssociation = BinaryAssociation(
    name="ownedInvariants1",
    ends={
        Property(name="completeoclcs_ConstraintCS", type=completeoclcs_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_ClassifierContextDeclCS", type=completeoclcs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredClass2: BinaryAssociation = BinaryAssociation(
    name="referredClass2",
    ends={
        Property(name="completeoclcs_Class", type=completeoclcs_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_ClassifierContextDeclCS3", type=completeoclcs_Class, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefinitions0: BinaryAssociation = BinaryAssociation(
    name="ownedDefinitions0",
    ends={
        Property(name="DefCS", type=completeoclcs_ClassifierContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClassifierContextDecl", type=completeoclcs_DefCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameters9: BinaryAssociation = BinaryAssociation(
    name="ownedParameters9",
    ends={
        Property(name="completeoclcs_ParameterCS", type=completeoclcs_DefOperationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_DefOperationCS", type=completeoclcs_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType10: BinaryAssociation = BinaryAssociation(
    name="ownedType10",
    ends={
        Property(name="completeoclcs_TypedRefCS", type=completeoclcs_FeatureContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_FeatureContextDeclCS", type=completeoclcs_TypedRefCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedContexts4: BinaryAssociation = BinaryAssociation(
    name="ownedContexts4",
    ends={
        Property(name="completeoclcs_ContextDeclCS", type=completeoclcs_CompleteOCLDocumentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_CompleteOCLDocumentCS", type=completeoclcs_ContextDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages5: BinaryAssociation = BinaryAssociation(
    name="ownedPackages5",
    ends={
        Property(name="completeoclcs_PackageDeclarationCS", type=completeoclcs_CompleteOCLDocumentCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_CompleteOCLDocumentCS6", type=completeoclcs_PackageDeclarationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSpecification7: BinaryAssociation = BinaryAssociation(
    name="ownedSpecification7",
    ends={
        Property(name="completeoclcs_ExpSpecificationCS", type=completeoclcs_DefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_DefCS", type=completeoclcs_ExpSpecificationCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningClassifierContextDecl8: BinaryAssociation = BinaryAssociation(
    name="owningClassifierContextDecl8",
    ends={
        Property(name="ClassifierContextDeclCS", type=completeoclcs_DefCS, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedDefinitions", type=completeoclcs_ClassifierContextDeclCS, multiplicity=Multiplicity(0, 1))
    }
)
referredPackage32: BinaryAssociation = BinaryAssociation(
    name="referredPackage32",
    ends={
        Property(name="completeoclcs_Package", type=completeoclcs_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PackageDeclarationCS33", type=completeoclcs_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedPathName34: BinaryAssociation = BinaryAssociation(
    name="ownedPathName34",
    ends={
        Property(name="completeoclcs_PathNameCS", type=completeoclcs_PathNameDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PathNameDeclCS", type=completeoclcs_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedDefaultExpressions35: BinaryAssociation = BinaryAssociation(
    name="ownedDefaultExpressions35",
    ends={
        Property(name="completeoclcs_ExpSpecificationCS36", type=completeoclcs_PropertyContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PropertyContextDeclCS", type=completeoclcs_ExpSpecificationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDerivedInvariants37: BinaryAssociation = BinaryAssociation(
    name="ownedDerivedInvariants37",
    ends={
        Property(name="completeoclcs_ConstraintCS39", type=completeoclcs_PropertyContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PropertyContextDeclCS38", type=completeoclcs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBodies11: BinaryAssociation = BinaryAssociation(
    name="ownedBodies11",
    ends={
        Property(name="completeoclcs_ExpSpecificationCS12", type=completeoclcs_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_OperationContextDeclCS", type=completeoclcs_ExpSpecificationCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameters13: BinaryAssociation = BinaryAssociation(
    name="ownedParameters13",
    ends={
        Property(name="completeoclcs_ParameterCS15", type=completeoclcs_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_OperationContextDeclCS14", type=completeoclcs_ParameterCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPostconditions16: BinaryAssociation = BinaryAssociation(
    name="ownedPostconditions16",
    ends={
        Property(name="completeoclcs_ConstraintCS18", type=completeoclcs_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_OperationContextDeclCS17", type=completeoclcs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPreconditions19: BinaryAssociation = BinaryAssociation(
    name="ownedPreconditions19",
    ends={
        Property(name="completeoclcs_ConstraintCS21", type=completeoclcs_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_OperationContextDeclCS20", type=completeoclcs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedResult22: BinaryAssociation = BinaryAssociation(
    name="ownedResult22",
    ends={
        Property(name="completeoclcs_VariableCS", type=completeoclcs_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_OperationContextDeclCS23", type=completeoclcs_VariableCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredOperation24: BinaryAssociation = BinaryAssociation(
    name="referredOperation24",
    ends={
        Property(name="completeoclcs_Operation", type=completeoclcs_OperationContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_OperationContextDeclCS25", type=completeoclcs_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ownedContexts26: BinaryAssociation = BinaryAssociation(
    name="ownedContexts26",
    ends={
        Property(name="completeoclcs_ContextDeclCS28", type=completeoclcs_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PackageDeclarationCS27", type=completeoclcs_ContextDeclCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInvariants29: BinaryAssociation = BinaryAssociation(
    name="ownedInvariants29",
    ends={
        Property(name="completeoclcs_ConstraintCS31", type=completeoclcs_PackageDeclarationCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PackageDeclarationCS30", type=completeoclcs_ConstraintCS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredProperty40: BinaryAssociation = BinaryAssociation(
    name="referredProperty40",
    ends={
        Property(name="completeoclcs_Property", type=completeoclcs_PropertyContextDeclCS, multiplicity=Multiplicity(1, 1)),
        Property(name="completeoclcs_PropertyContextDeclCS41", type=completeoclcs_Property, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_completeoclcs_CompleteOCLDocumentCS_NamespaceCS = Generalization(general=NamespaceCS, specific=completeoclcs_CompleteOCLDocumentCS)
gen_completeoclcs_CompleteOCLDocumentCS_RootCS = Generalization(general=RootCS, specific=completeoclcs_CompleteOCLDocumentCS)
gen_completeoclcs_ClassifierContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=completeoclcs_ClassifierContextDeclCS)
gen_completeoclcs_ClassifierContextDeclCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=completeoclcs_ClassifierContextDeclCS)
gen_completeoclcs_DefOperationCS_DefCS = Generalization(general=DefCS, specific=completeoclcs_DefOperationCS)
gen_completeoclcs_DefOperationCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=completeoclcs_DefOperationCS)
gen_completeoclcs_DefPropertyCS_DefCS = Generalization(general=DefCS, specific=completeoclcs_DefPropertyCS)
gen_completeoclcs_FeatureContextDeclCS_ContextDeclCS = Generalization(general=ContextDeclCS, specific=completeoclcs_FeatureContextDeclCS)
gen_completeoclcs_ContextDeclCS_PathNameDeclCS = Generalization(general=PathNameDeclCS, specific=completeoclcs_ContextDeclCS)
gen_completeoclcs_DefCS_TypedElementCS = Generalization(general=TypedElementCS, specific=completeoclcs_DefCS)
gen_completeoclcs_PathNameDeclCS_ModelElementCS = Generalization(general=ModelElementCS, specific=completeoclcs_PathNameDeclCS)
gen_completeoclcs_PathNameDeclCS_MorePivotable = Generalization(general=MorePivotable, specific=completeoclcs_PathNameDeclCS)
gen_completeoclcs_PropertyContextDeclCS_FeatureContextDeclCS = Generalization(general=FeatureContextDeclCS, specific=completeoclcs_PropertyContextDeclCS)
gen_completeoclcs_OCLMessageArgCS_ExpCS = Generalization(general=ExpCS, specific=completeoclcs_OCLMessageArgCS)
gen_completeoclcs_OperationContextDeclCS_FeatureContextDeclCS = Generalization(general=FeatureContextDeclCS, specific=completeoclcs_OperationContextDeclCS)
gen_completeoclcs_OperationContextDeclCS_TemplateableElementCS = Generalization(general=TemplateableElementCS, specific=completeoclcs_OperationContextDeclCS)
gen_completeoclcs_PackageDeclarationCS_PathNameDeclCS = Generalization(general=PathNameDeclCS, specific=completeoclcs_PackageDeclarationCS)

# Domain Model
domain_model = DomainModel(
    name="completeoclcs",
    types={completeoclcs_ConstraintCS, completeoclcs_Class, completeoclcs_CompleteOCLDocumentCS, NamespaceCS, RootCS, completeoclcs_ClassifierContextDeclCS, ContextDeclCS, TemplateableElementCS, completeoclcs_DefCS, completeoclcs_DefOperationCS, DefCS, completeoclcs_ParameterCS, completeoclcs_DefPropertyCS, completeoclcs_FeatureContextDeclCS, completeoclcs_TypedRefCS, completeoclcs_ContextDeclCS, completeoclcs_PackageDeclarationCS, PathNameDeclCS, TypedElementCS, completeoclcs_ExpSpecificationCS, completeoclcs_Package, completeoclcs_PathNameDeclCS, ModelElementCS, MorePivotable, completeoclcs_PathNameCS, completeoclcs_PropertyContextDeclCS, completeoclcs_OCLMessageArgCS, ExpCS, completeoclcs_OperationContextDeclCS, FeatureContextDeclCS, completeoclcs_VariableCS, completeoclcs_Operation, completeoclcs_Property},
    associations={ownedInvariants1, referredClass2, ownedDefinitions0, ownedParameters9, ownedType10, ownedContexts4, ownedPackages5, ownedSpecification7, owningClassifierContextDecl8, referredPackage32, ownedPathName34, ownedDefaultExpressions35, ownedDerivedInvariants37, ownedBodies11, ownedParameters13, ownedPostconditions16, ownedPreconditions19, ownedResult22, referredOperation24, ownedContexts26, ownedInvariants29, referredProperty40},
    generalizations={gen_completeoclcs_CompleteOCLDocumentCS_NamespaceCS, gen_completeoclcs_CompleteOCLDocumentCS_RootCS, gen_completeoclcs_ClassifierContextDeclCS_ContextDeclCS, gen_completeoclcs_ClassifierContextDeclCS_TemplateableElementCS, gen_completeoclcs_DefOperationCS_DefCS, gen_completeoclcs_DefOperationCS_TemplateableElementCS, gen_completeoclcs_DefPropertyCS_DefCS, gen_completeoclcs_FeatureContextDeclCS_ContextDeclCS, gen_completeoclcs_ContextDeclCS_PathNameDeclCS, gen_completeoclcs_DefCS_TypedElementCS, gen_completeoclcs_PathNameDeclCS_ModelElementCS, gen_completeoclcs_PathNameDeclCS_MorePivotable, gen_completeoclcs_PropertyContextDeclCS_FeatureContextDeclCS, gen_completeoclcs_OCLMessageArgCS_ExpCS, gen_completeoclcs_OperationContextDeclCS_FeatureContextDeclCS, gen_completeoclcs_OperationContextDeclCS_TemplateableElementCS, gen_completeoclcs_PackageDeclarationCS_PathNameDeclCS},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)