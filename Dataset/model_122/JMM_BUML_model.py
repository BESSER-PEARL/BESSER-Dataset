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
InheritanceKind: Enumeration = Enumeration(
    name="InheritanceKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="final")
    }
)

# Classes
JMM_FieldDeclaration = Class(name="JMM::FieldDeclaration")
BodyDeclaration = Class(name="BodyDeclaration")
JMM_Package = Class(name="JMM::Package")
JMM_MethodDeclaration = Class(name="JMM::MethodDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
JMM_ConstructorDeclaration = Class(name="JMM::ConstructorDeclaration")
JMM_ClassDeclaration = Class(name="JMM::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
JMM_TypeAccess = Class(name="JMM::TypeAccess")
JMM_InterfaceDeclaration = Class(name="JMM::InterfaceDeclaration")
AbstractVariablesContainer = Class(name="AbstractVariablesContainer")
JMM_AnnotationTypeDeclaration = Class(name="JMM::AnnotationTypeDeclaration")
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
JMM_Model = Class(name="JMM::Model")
Type = Class(name="Type")
JMM_BodyDeclaration = Class(name="JMM::BodyDeclaration", is_abstract=True)
JMM_Modifier = Class(name="JMM::Modifier")
JMM_NamedElement = Class(name="JMM::NamedElement", is_abstract=True)
ASTNode = Class(name="ASTNode")
Expression = Class(name="Expression")
NamespaceAccess = Class(name="NamespaceAccess")
JMM_Type = Class(name="JMM::Type", is_abstract=True)
NamedElement = Class(name="NamedElement")
JMM_AbstractTypeDeclaration = Class(name="JMM::AbstractTypeDeclaration", is_abstract=True)
JMM_ASTNode = Class(name="JMM::ASTNode", is_abstract=True)
JMM_AbstractVariablesContainer = Class(name="JMM::AbstractVariablesContainer", is_abstract=True)
JMM_AbstractMethodDeclaration = Class(name="JMM::AbstractMethodDeclaration", is_abstract=True)
JMM_TypeDeclaration = Class(name="JMM::TypeDeclaration", is_abstract=True)
JMM_Expression = Class(name="JMM::Expression", is_abstract=True)
JMM_NamespaceAccess = Class(name="JMM::NamespaceAccess", is_abstract=True)

# JMM_FieldDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# JMM_Package class attributes and methods

# JMM_MethodDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# JMM_ConstructorDeclaration class attributes and methods

# JMM_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# JMM_TypeAccess class attributes and methods

# JMM_InterfaceDeclaration class attributes and methods

# AbstractVariablesContainer class attributes and methods

# JMM_AnnotationTypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# JMM_Model class attributes and methods
JMM_Model_name: Property = Property(name="name", type=StringType)
JMM_Model.attributes={JMM_Model_name}

# Type class attributes and methods

# JMM_BodyDeclaration class attributes and methods

# JMM_Modifier class attributes and methods
JMM_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
JMM_Modifier.attributes={JMM_Modifier_inheritance}

# JMM_NamedElement class attributes and methods
JMM_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
JMM_NamedElement_name: Property = Property(name="name", type=StringType)
JMM_NamedElement.attributes={JMM_NamedElement_proxy, JMM_NamedElement_name}

# ASTNode class attributes and methods

# Expression class attributes and methods

# NamespaceAccess class attributes and methods

# JMM_Type class attributes and methods

# NamedElement class attributes and methods

# JMM_AbstractTypeDeclaration class attributes and methods

# JMM_ASTNode class attributes and methods

# JMM_AbstractVariablesContainer class attributes and methods

# JMM_AbstractMethodDeclaration class attributes and methods

# JMM_TypeDeclaration class attributes and methods

# JMM_Expression class attributes and methods

# JMM_NamespaceAccess class attributes and methods

# Relationships
ownedElements0: BinaryAssociation = BinaryAssociation(
    name="ownedElements0",
    ends={
        Property(name="JMM_Package", type=JMM_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_Model", type=JMM_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass1: BinaryAssociation = BinaryAssociation(
    name="superClass1",
    ends={
        Property(name="JMM_TypeAccess", type=JMM_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_ClassDeclaration", type=JMM_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyDeclarations9: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations9",
    ends={
        Property(name="JMM_BodyDeclaration", type=JMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_AbstractTypeDeclaration10", type=JMM_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces11: BinaryAssociation = BinaryAssociation(
    name="superInterfaces11",
    ends={
        Property(name="JMM_TypeAccess13", type=JMM_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_AbstractTypeDeclaration12", type=JMM_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier14: BinaryAssociation = BinaryAssociation(
    name="modifier14",
    ends={
        Property(name="JMM_Modifier", type=JMM_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_BodyDeclaration15", type=JMM_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="JMM_Type", type=JMM_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_TypeAccess3", type=JMM_Type, multiplicity=Multiplicity(1, 1))
    }
)
ownedPackages5: BinaryAssociation = BinaryAssociation(
    name="ownedPackages5",
    ends={
        Property(name="JMM_Package6", type=JMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_Package4", type=JMM_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElements7: BinaryAssociation = BinaryAssociation(
    name="ownedElements7",
    ends={
        Property(name="JMM_AbstractTypeDeclaration", type=JMM_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JMM_Package8", type=JMM_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_JMM_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=JMM_MethodDeclaration)
gen_JMM_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=JMM_ConstructorDeclaration)
gen_JMM_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=JMM_ClassDeclaration)
gen_JMM_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=JMM_InterfaceDeclaration)
gen_JMM_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JMM_FieldDeclaration)
gen_JMM_FieldDeclaration_AbstractVariablesContainer = Generalization(general=AbstractVariablesContainer, specific=JMM_FieldDeclaration)
gen_JMM_AnnotationTypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JMM_AnnotationTypeDeclaration)
gen_JMM_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JMM_AbstractTypeDeclaration)
gen_JMM_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=JMM_AbstractTypeDeclaration)
gen_JMM_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=JMM_BodyDeclaration)
gen_JMM_NamedElement_ASTNode = Generalization(general=ASTNode, specific=JMM_NamedElement)
gen_JMM_TypeAccess_Expression = Generalization(general=Expression, specific=JMM_TypeAccess)
gen_JMM_TypeAccess_NamespaceAccess = Generalization(general=NamespaceAccess, specific=JMM_TypeAccess)
gen_JMM_Package_NamedElement = Generalization(general=NamedElement, specific=JMM_Package)
gen_JMM_AbstractVariablesContainer_ASTNode = Generalization(general=ASTNode, specific=JMM_AbstractVariablesContainer)
gen_JMM_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JMM_AbstractMethodDeclaration)
gen_JMM_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JMM_TypeDeclaration)
gen_JMM_Expression_ASTNode = Generalization(general=ASTNode, specific=JMM_Expression)
gen_JMM_NamespaceAccess_ASTNode = Generalization(general=ASTNode, specific=JMM_NamespaceAccess)
gen_JMM_Modifier_ASTNode = Generalization(general=ASTNode, specific=JMM_Modifier)
gen_JMM_Type_NamedElement = Generalization(general=NamedElement, specific=JMM_Type)

# Domain Model
domain_model = DomainModel(
    name="JMM",
    types={JMM_FieldDeclaration, BodyDeclaration, JMM_Package, JMM_MethodDeclaration, AbstractMethodDeclaration, JMM_ConstructorDeclaration, JMM_ClassDeclaration, TypeDeclaration, JMM_TypeAccess, JMM_InterfaceDeclaration, AbstractVariablesContainer, JMM_AnnotationTypeDeclaration, AbstractTypeDeclaration, JMM_Model, Type, JMM_BodyDeclaration, JMM_Modifier, JMM_NamedElement, ASTNode, Expression, NamespaceAccess, JMM_Type, NamedElement, JMM_AbstractTypeDeclaration, JMM_ASTNode, JMM_AbstractVariablesContainer, JMM_AbstractMethodDeclaration, JMM_TypeDeclaration, JMM_Expression, JMM_NamespaceAccess, InheritanceKind},
    associations={ownedElements0, superClass1, bodyDeclarations9, superInterfaces11, modifier14, type2, ownedPackages5, ownedElements7},
    generalizations={gen_JMM_MethodDeclaration_AbstractMethodDeclaration, gen_JMM_ConstructorDeclaration_AbstractMethodDeclaration, gen_JMM_ClassDeclaration_TypeDeclaration, gen_JMM_InterfaceDeclaration_TypeDeclaration, gen_JMM_FieldDeclaration_BodyDeclaration, gen_JMM_FieldDeclaration_AbstractVariablesContainer, gen_JMM_AnnotationTypeDeclaration_AbstractTypeDeclaration, gen_JMM_AbstractTypeDeclaration_BodyDeclaration, gen_JMM_AbstractTypeDeclaration_Type, gen_JMM_BodyDeclaration_NamedElement, gen_JMM_NamedElement_ASTNode, gen_JMM_TypeAccess_Expression, gen_JMM_TypeAccess_NamespaceAccess, gen_JMM_Package_NamedElement, gen_JMM_AbstractVariablesContainer_ASTNode, gen_JMM_AbstractMethodDeclaration_BodyDeclaration, gen_JMM_TypeDeclaration_AbstractTypeDeclaration, gen_JMM_Expression_ASTNode, gen_JMM_NamespaceAccess_ASTNode, gen_JMM_Modifier_ASTNode, gen_JMM_Type_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)