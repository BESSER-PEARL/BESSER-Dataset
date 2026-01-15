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
JAVA_ClassDeclaration = Class(name="JAVA::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
JAVA_TypeAccess = Class(name="JAVA::TypeAccess")
JAVA_AbstractTypeDeclaration = Class(name="JAVA::AbstractTypeDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
Type = Class(name="Type")
JAVA_FieldDeclaration = Class(name="JAVA::FieldDeclaration")
Expression = Class(name="Expression")
JAVA_TypeDeclaration = Class(name="JAVA::TypeDeclaration", is_abstract=True)
JAVA_InterfaceDeclaration = Class(name="JAVA::InterfaceDeclaration")
JAVA_Package = Class(name="JAVA::Package")
NamedElement = Class(name="NamedElement")
JAVA_Expression = Class(name="JAVA::Expression", is_abstract=True)
JAVA_Type = Class(name="JAVA::Type", is_abstract=True)
JAVA_NamedElement = Class(name="JAVA::NamedElement", is_abstract=True)
ASTNode = Class(name="ASTNode")
JAVA_ASTNode = Class(name="JAVA::ASTNode", is_abstract=True)
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
JAVA_BodyDeclaration = Class(name="JAVA::BodyDeclaration", is_abstract=True)

# JAVA_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# JAVA_TypeAccess class attributes and methods

# JAVA_AbstractTypeDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# Type class attributes and methods

# JAVA_FieldDeclaration class attributes and methods

# Expression class attributes and methods

# JAVA_TypeDeclaration class attributes and methods

# JAVA_InterfaceDeclaration class attributes and methods

# JAVA_Package class attributes and methods

# NamedElement class attributes and methods

# JAVA_Expression class attributes and methods

# JAVA_Type class attributes and methods

# JAVA_NamedElement class attributes and methods
JAVA_NamedElement_name: Property = Property(name="name", type=StringType)
JAVA_NamedElement_proxy: Property = Property(name="proxy", type=BooleanType)
JAVA_NamedElement.attributes={JAVA_NamedElement_proxy, JAVA_NamedElement_name}

# ASTNode class attributes and methods

# JAVA_ASTNode class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# JAVA_BodyDeclaration class attributes and methods

# Relationships
superClass0: BinaryAssociation = BinaryAssociation(
    name="superClass0",
    ends={
        Property(name="JAVA_TypeAccess", type=JAVA_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JAVA_ClassDeclaration", type=JAVA_TypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedElements5: BinaryAssociation = BinaryAssociation(
    name="ownedElements5",
    ends={
        Property(name="JAVA_AbstractTypeDeclaration", type=JAVA_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JAVA_Package", type=JAVA_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces6: BinaryAssociation = BinaryAssociation(
    name="superInterfaces6",
    ends={
        Property(name="JAVA_TypeAccess8", type=JAVA_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JAVA_AbstractTypeDeclaration7", type=JAVA_TypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields1: BinaryAssociation = BinaryAssociation(
    name="fields1",
    ends={
        Property(name="JAVA_FieldDeclaration", type=JAVA_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JAVA_ClassDeclaration2", type=JAVA_FieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="JAVA_TypeDeclaration", type=JAVA_TypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="JAVA_TypeAccess4", type=JAVA_TypeDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
typeAccess9: BinaryAssociation = BinaryAssociation(
    name="typeAccess9",
    ends={
        Property(name="JAVA_TypeAccess11", type=JAVA_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="JAVA_FieldDeclaration10", type=JAVA_TypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_JAVA_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=JAVA_ClassDeclaration)
gen_JAVA_AbstractTypeDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JAVA_AbstractTypeDeclaration)
gen_JAVA_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=JAVA_AbstractTypeDeclaration)
gen_JAVA_TypeAccess_Expression = Generalization(general=Expression, specific=JAVA_TypeAccess)
gen_JAVA_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=JAVA_InterfaceDeclaration)
gen_JAVA_Package_NamedElement = Generalization(general=NamedElement, specific=JAVA_Package)
gen_JAVA_Expression_ASTNode = Generalization(general=ASTNode, specific=JAVA_Expression)
gen_JAVA_FieldDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=JAVA_FieldDeclaration)
gen_JAVA_Type_NamedElement = Generalization(general=NamedElement, specific=JAVA_Type)
gen_JAVA_NamedElement_ASTNode = Generalization(general=ASTNode, specific=JAVA_NamedElement)
gen_JAVA_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=JAVA_TypeDeclaration)
gen_JAVA_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=JAVA_BodyDeclaration)

# Domain Model
domain_model = DomainModel(
    name="JAVA",
    types={JAVA_ClassDeclaration, TypeDeclaration, JAVA_TypeAccess, JAVA_AbstractTypeDeclaration, BodyDeclaration, Type, JAVA_FieldDeclaration, Expression, JAVA_TypeDeclaration, JAVA_InterfaceDeclaration, JAVA_Package, NamedElement, JAVA_Expression, JAVA_Type, JAVA_NamedElement, ASTNode, JAVA_ASTNode, AbstractTypeDeclaration, JAVA_BodyDeclaration},
    associations={superClass0, ownedElements5, superInterfaces6, fields1, type3, typeAccess9},
    generalizations={gen_JAVA_ClassDeclaration_TypeDeclaration, gen_JAVA_AbstractTypeDeclaration_BodyDeclaration, gen_JAVA_AbstractTypeDeclaration_Type, gen_JAVA_TypeAccess_Expression, gen_JAVA_InterfaceDeclaration_TypeDeclaration, gen_JAVA_Package_NamedElement, gen_JAVA_Expression_ASTNode, gen_JAVA_FieldDeclaration_BodyDeclaration, gen_JAVA_Type_NamedElement, gen_JAVA_NamedElement_ASTNode, gen_JAVA_TypeDeclaration_AbstractTypeDeclaration, gen_JAVA_BodyDeclaration_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)