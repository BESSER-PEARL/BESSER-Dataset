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
SimpleType: Enumeration = Enumeration(
    name="SimpleType",
    literals={
            EnumerationLiteral(name="bool"),
			EnumerationLiteral(name="byte"),
			EnumerationLiteral(name="char"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="sbyte"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="uint"),
			EnumerationLiteral(name="ulong"),
			EnumerationLiteral(name="ushort"),
			EnumerationLiteral(name="void"),
			EnumerationLiteral(name="object"),
			EnumerationLiteral(name="string")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="internal_protected"),
			EnumerationLiteral(name="private_protected")
    }
)

ModifierKind: Enumeration = Enumeration(
    name="ModifierKind",
    literals={
            EnumerationLiteral(name="static"),
			EnumerationLiteral(name="native"),
			EnumerationLiteral(name="sinchronized"),
			EnumerationLiteral(name="virtual"),
			EnumerationLiteral(name="override"),
			EnumerationLiteral(name="readonly"),
			EnumerationLiteral(name="const"),
			EnumerationLiteral(name="new"),
			EnumerationLiteral(name="none")
    }
)

InheritanceKind: Enumeration = Enumeration(
    name="InheritanceKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="sealed")
    }
)

# Classes
cSharpArchId_Model = Class(name="cSharpArchId::Model")
cSharpArchId_Archive = Class(name="cSharpArchId::Archive")
cSharpArchId_CompileUnit = Class(name="cSharpArchId::CompileUnit")
cSharpArchId_EnumerationLiteral = Class(name="cSharpArchId::EnumerationLiteral")
NamedElement = Class(name="NamedElement")
cSharpArchId_NamedElement = Class(name="cSharpArchId::NamedElement", is_abstract=True)
ASTNode = Class(name="ASTNode")
cSharpArchId_Type = Class(name="cSharpArchId::Type", is_abstract=True)
cSharpArchId_Enumeration = Class(name="cSharpArchId::Enumeration")
Type = Class(name="Type")
cSharpArchId_ClassDeclaration = Class(name="cSharpArchId::ClassDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
cSharpArchId_InterfaceDeclaration = Class(name="cSharpArchId::InterfaceDeclaration")
cSharpArchId_PrimitiveType = Class(name="cSharpArchId::PrimitiveType")
cSharpArchId_Namespace = Class(name="cSharpArchId::Namespace")
cSharpArchId_MethodParameter = Class(name="cSharpArchId::MethodParameter")
cSharpArchId_Comment = Class(name="cSharpArchId::Comment", is_abstract=True)
cSharpArchId_AbstractTypeDeclaration = Class(name="cSharpArchId::AbstractTypeDeclaration", is_abstract=True)
cSharpArchId_UsingDeclaration = Class(name="cSharpArchId::UsingDeclaration")
cSharpArchId_ElementRef = Class(name="cSharpArchId::ElementRef")
cSharpArchId_ASTNode = Class(name="cSharpArchId::ASTNode", is_abstract=True)
cSharpArchId_LineComment = Class(name="cSharpArchId::LineComment")
Comment = Class(name="Comment")
cSharpArchId_BlockComment = Class(name="cSharpArchId::BlockComment")
cSharpArchId_BodyDeclaration = Class(name="cSharpArchId::BodyDeclaration", is_abstract=True)
cSharpArchId_Modifier = Class(name="cSharpArchId::Modifier")
cSharpArchId_TypeDeclaration = Class(name="cSharpArchId::TypeDeclaration", is_abstract=True)
AbstractTypeDeclaration = Class(name="AbstractTypeDeclaration")
cSharpArchId_TypeAcces = Class(name="cSharpArchId::TypeAcces")
Expresion = Class(name="Expresion")
cSharpArchId_Expresion = Class(name="cSharpArchId::Expresion", is_abstract=True)
cSharpArchId_Annotation = Class(name="cSharpArchId::Annotation")
cSharpArchId_AbstractMethodDeclaration = Class(name="cSharpArchId::AbstractMethodDeclaration", is_abstract=True)
BodyDeclaration = Class(name="BodyDeclaration")
cSharpArchId_Block = Class(name="cSharpArchId::Block")
cSharpArchId_VariableDeclaration = Class(name="cSharpArchId::VariableDeclaration", is_abstract=True)
cSharpArchId_TypeParameter = Class(name="cSharpArchId::TypeParameter")
Statement = Class(name="Statement")
cSharpArchId_Statement = Class(name="cSharpArchId::Statement", is_abstract=True)
cSharpArchId_SingleVariableDeclaration = Class(name="cSharpArchId::SingleVariableDeclaration")
VariableDeclaration = Class(name="VariableDeclaration")
cSharpArchId_MethodDeclaration = Class(name="cSharpArchId::MethodDeclaration")
AbstractMethodDeclaration = Class(name="AbstractMethodDeclaration")
cSharpArchId_ConstructorDeclaration = Class(name="cSharpArchId::ConstructorDeclaration")
cSharpArchId_AbstractMethodInvocation = Class(name="cSharpArchId::AbstractMethodInvocation", is_abstract=True)
cSharpArchId_MethodInvocation = Class(name="cSharpArchId::MethodInvocation")
AbstractMethodInvocation = Class(name="AbstractMethodInvocation")
cSharpArchId_Assignment = Class(name="cSharpArchId::Assignment")
cSharpArchId_ClassInstanceCreation = Class(name="cSharpArchId::ClassInstanceCreation")
cSharpArchId_ConstructorInvocation = Class(name="cSharpArchId::ConstructorInvocation")
cSharpArchId_ReturnType = Class(name="cSharpArchId::ReturnType")

# cSharpArchId_Model class attributes and methods
cSharpArchId_Model_name: Property = Property(name="name", type=StringType)
cSharpArchId_Model.attributes={cSharpArchId_Model_name}

# cSharpArchId_Archive class attributes and methods
cSharpArchId_Archive_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
cSharpArchId_Archive.attributes={cSharpArchId_Archive_originalFilePath}

# cSharpArchId_CompileUnit class attributes and methods
cSharpArchId_CompileUnit_originalFilePath: Property = Property(name="originalFilePath", type=StringType)
cSharpArchId_CompileUnit.attributes={cSharpArchId_CompileUnit_originalFilePath}

# cSharpArchId_EnumerationLiteral class attributes and methods

# NamedElement class attributes and methods

# cSharpArchId_NamedElement class attributes and methods
cSharpArchId_NamedElement_name: Property = Property(name="name", type=StringType)
cSharpArchId_NamedElement.attributes={cSharpArchId_NamedElement_name}

# ASTNode class attributes and methods

# cSharpArchId_Type class attributes and methods

# cSharpArchId_Enumeration class attributes and methods

# Type class attributes and methods

# cSharpArchId_ClassDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# cSharpArchId_InterfaceDeclaration class attributes and methods

# cSharpArchId_PrimitiveType class attributes and methods
cSharpArchId_PrimitiveType_kind: Property = Property(name="kind", type=StringType)
cSharpArchId_PrimitiveType.attributes={cSharpArchId_PrimitiveType_kind}

# cSharpArchId_Namespace class attributes and methods

# cSharpArchId_MethodParameter class attributes and methods

# cSharpArchId_Comment class attributes and methods
cSharpArchId_Comment_content: Property = Property(name="content", type=StringType)
cSharpArchId_Comment.attributes={cSharpArchId_Comment_content}

# cSharpArchId_AbstractTypeDeclaration class attributes and methods

# cSharpArchId_UsingDeclaration class attributes and methods

# cSharpArchId_ElementRef class attributes and methods

# cSharpArchId_ASTNode class attributes and methods

# cSharpArchId_LineComment class attributes and methods

# Comment class attributes and methods

# cSharpArchId_BlockComment class attributes and methods

# cSharpArchId_BodyDeclaration class attributes and methods

# cSharpArchId_Modifier class attributes and methods
cSharpArchId_Modifier_visibility: Property = Property(name="visibility", type=StringType)
cSharpArchId_Modifier_inheritance: Property = Property(name="inheritance", type=StringType)
cSharpArchId_Modifier_static: Property = Property(name="static", type=BooleanType)
cSharpArchId_Modifier_modifier: Property = Property(name="modifier", type=StringType)
cSharpArchId_Modifier.attributes={cSharpArchId_Modifier_static, cSharpArchId_Modifier_visibility, cSharpArchId_Modifier_modifier, cSharpArchId_Modifier_inheritance}

# cSharpArchId_TypeDeclaration class attributes and methods

# AbstractTypeDeclaration class attributes and methods

# cSharpArchId_TypeAcces class attributes and methods

# Expresion class attributes and methods

# cSharpArchId_Expresion class attributes and methods

# cSharpArchId_Annotation class attributes and methods

# cSharpArchId_AbstractMethodDeclaration class attributes and methods

# BodyDeclaration class attributes and methods

# cSharpArchId_Block class attributes and methods

# cSharpArchId_VariableDeclaration class attributes and methods

# cSharpArchId_TypeParameter class attributes and methods

# Statement class attributes and methods

# cSharpArchId_Statement class attributes and methods

# cSharpArchId_SingleVariableDeclaration class attributes and methods

# VariableDeclaration class attributes and methods

# cSharpArchId_MethodDeclaration class attributes and methods

# AbstractMethodDeclaration class attributes and methods

# cSharpArchId_ConstructorDeclaration class attributes and methods

# cSharpArchId_AbstractMethodInvocation class attributes and methods

# cSharpArchId_MethodInvocation class attributes and methods

# AbstractMethodInvocation class attributes and methods

# cSharpArchId_Assignment class attributes and methods

# cSharpArchId_ClassInstanceCreation class attributes and methods

# cSharpArchId_ConstructorInvocation class attributes and methods

# cSharpArchId_ReturnType class attributes and methods
cSharpArchId_ReturnType_returnType: Property = Property(name="returnType", type=StringType)
cSharpArchId_ReturnType.attributes={cSharpArchId_ReturnType_returnType}

# Relationships
archives0: BinaryAssociation = BinaryAssociation(
    name="archives0",
    ends={
        Property(name="cSharpArchId_Archive", type=cSharpArchId_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Model", type=cSharpArchId_Archive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compileUnits1: BinaryAssociation = BinaryAssociation(
    name="compileUnits1",
    ends={
        Property(name="cSharpArchId_CompileUnit", type=cSharpArchId_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Model2", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumLiterals3: BinaryAssociation = BinaryAssociation(
    name="enumLiterals3",
    ends={
        Property(name="cSharpArchId_EnumerationLiteral", type=cSharpArchId_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Enumeration", type=cSharpArchId_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass4: BinaryAssociation = BinaryAssociation(
    name="superClass4",
    ends={
        Property(name="cSharpArchId_Type", type=cSharpArchId_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_ClassDeclaration", type=cSharpArchId_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classes5: BinaryAssociation = BinaryAssociation(
    name="classes5",
    ends={
        Property(name="cSharpArchId_ClassDeclaration6", type=cSharpArchId_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Namespace", type=cSharpArchId_ClassDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumerations7: BinaryAssociation = BinaryAssociation(
    name="enumerations7",
    ends={
        Property(name="cSharpArchId_Enumeration9", type=cSharpArchId_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Namespace8", type=cSharpArchId_Enumeration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="cSharpArchId_Type11", type=cSharpArchId_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_MethodParameter", type=cSharpArchId_Type, multiplicity=Multiplicity(1, 1))
    }
)
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="cSharpArchId_NamedElement", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_CompileUnit13", type=cSharpArchId_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentList14: BinaryAssociation = BinaryAssociation(
    name="commentList14",
    ends={
        Property(name="cSharpArchId_Comment", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_CompileUnit15", type=cSharpArchId_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclaration16: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration16",
    ends={
        Property(name="cSharpArchId_AbstractTypeDeclaration", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_CompileUnit17", type=cSharpArchId_AbstractTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
usings18: BinaryAssociation = BinaryAssociation(
    name="usings18",
    ends={
        Property(name="cSharpArchId_UsingDeclaration", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_CompileUnit19", type=cSharpArchId_UsingDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespace20: BinaryAssociation = BinaryAssociation(
    name="namespace20",
    ends={
        Property(name="cSharpArchId_Namespace22", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_CompileUnit21", type=cSharpArchId_Namespace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
originalCompilationUnit23: BinaryAssociation = BinaryAssociation(
    name="originalCompilationUnit23",
    ends={
        Property(name="cSharpArchId_CompileUnit24", type=cSharpArchId_ASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_ASTNode", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(0, 1))
    }
)
compileUnits25: BinaryAssociation = BinaryAssociation(
    name="compileUnits25",
    ends={
        Property(name="cSharpArchId_CompileUnit27", type=cSharpArchId_Archive, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Archive26", type=cSharpArchId_CompileUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeBody28: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeBody28",
    ends={
        Property(name="cSharpArchId_Comment30", type=cSharpArchId_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractTypeDeclaration29", type=cSharpArchId_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsAfterBody31: BinaryAssociation = BinaryAssociation(
    name="commentsAfterBody31",
    ends={
        Property(name="cSharpArchId_Comment33", type=cSharpArchId_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractTypeDeclaration32", type=cSharpArchId_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyDeclarations34: BinaryAssociation = BinaryAssociation(
    name="bodyDeclarations34",
    ends={
        Property(name="cSharpArchId_BodyDeclaration", type=cSharpArchId_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractTypeDeclaration35", type=cSharpArchId_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier38: BinaryAssociation = BinaryAssociation(
    name="modifier38",
    ends={
        Property(name="Modifier", type=cSharpArchId_BodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyDeclaration", type=cSharpArchId_Modifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyDeclaration39: BinaryAssociation = BinaryAssociation(
    name="bodyDeclaration39",
    ends={
        Property(name="BodyDeclaration", type=cSharpArchId_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="modifier", type=cSharpArchId_BodyDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
annotations40: BinaryAssociation = BinaryAssociation(
    name="annotations40",
    ends={
        Property(name="cSharpArchId_Annotation", type=cSharpArchId_Modifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Modifier41", type=cSharpArchId_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifier36: BinaryAssociation = BinaryAssociation(
    name="modifier36",
    ends={
        Property(name="cSharpArchId_Modifier", type=cSharpArchId_AbstractTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractTypeDeclaration37", type=cSharpArchId_Modifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeacces42: BinaryAssociation = BinaryAssociation(
    name="typeacces42",
    ends={
        Property(name="cSharpArchId_TypeAcces", type=cSharpArchId_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_Annotation43", type=cSharpArchId_TypeAcces, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body44: BinaryAssociation = BinaryAssociation(
    name="body44",
    ends={
        Property(name="cSharpArchId_Block", type=cSharpArchId_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractMethodDeclaration", type=cSharpArchId_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="VariableDeclaration", type=cSharpArchId_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=cSharpArchId_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters46: BinaryAssociation = BinaryAssociation(
    name="typeParameters46",
    ends={
        Property(name="cSharpArchId_TypeParameter", type=cSharpArchId_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractMethodDeclaration47", type=cSharpArchId_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thrownExceptions48: BinaryAssociation = BinaryAssociation(
    name="thrownExceptions48",
    ends={
        Property(name="cSharpArchId_TypeAcces50", type=cSharpArchId_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractMethodDeclaration49", type=cSharpArchId_TypeAcces, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType51: BinaryAssociation = BinaryAssociation(
    name="returnType51",
    ends={
        Property(name="cSharpArchId_Type53", type=cSharpArchId_AbstractMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractMethodDeclaration52", type=cSharpArchId_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodDeclaration54: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration54",
    ends={
        Property(name="AbstractMethodDeclaration", type=cSharpArchId_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=cSharpArchId_AbstractMethodDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="cSharpArchId_Type56", type=cSharpArchId_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_VariableDeclaration", type=cSharpArchId_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
localVariableDeclaration57: BinaryAssociation = BinaryAssociation(
    name="localVariableDeclaration57",
    ends={
        Property(name="cSharpArchId_BodyDeclaration58", type=cSharpArchId_MethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_MethodDeclaration", type=cSharpArchId_BodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments61: BinaryAssociation = BinaryAssociation(
    name="arguments61",
    ends={
        Property(name="cSharpArchId_Expresion", type=cSharpArchId_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractMethodInvocation62", type=cSharpArchId_Expresion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression63: BinaryAssociation = BinaryAssociation(
    name="expression63",
    ends={
        Property(name="cSharpArchId_Expresion64", type=cSharpArchId_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_MethodInvocation", type=cSharpArchId_Expresion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="cSharpArchId_TypeAcces66", type=cSharpArchId_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_ClassInstanceCreation", type=cSharpArchId_TypeAcces, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expresion67: BinaryAssociation = BinaryAssociation(
    name="expresion67",
    ends={
        Property(name="cSharpArchId_Expresion69", type=cSharpArchId_ClassInstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_ClassInstanceCreation68", type=cSharpArchId_Expresion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArguments59: BinaryAssociation = BinaryAssociation(
    name="typeArguments59",
    ends={
        Property(name="cSharpArchId_TypeAcces60", type=cSharpArchId_AbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="cSharpArchId_AbstractMethodInvocation", type=cSharpArchId_TypeAcces, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cSharpArchId_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_EnumerationLiteral)
gen_cSharpArchId_NamedElement_ASTNode = Generalization(general=ASTNode, specific=cSharpArchId_NamedElement)
gen_cSharpArchId_Type_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_Type)
gen_cSharpArchId_Enumeration_Type = Generalization(general=Type, specific=cSharpArchId_Enumeration)
gen_cSharpArchId_ClassDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=cSharpArchId_ClassDeclaration)
gen_cSharpArchId_InterfaceDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=cSharpArchId_InterfaceDeclaration)
gen_cSharpArchId_PrimitiveType_Type = Generalization(general=Type, specific=cSharpArchId_PrimitiveType)
gen_cSharpArchId_Namespace_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_Namespace)
gen_cSharpArchId_MethodParameter_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_MethodParameter)
gen_cSharpArchId_CompileUnit_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_CompileUnit)
gen_cSharpArchId_ElementRef_Type = Generalization(general=Type, specific=cSharpArchId_ElementRef)
gen_cSharpArchId_Archive_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_Archive)
gen_cSharpArchId_UsingDeclaration_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_UsingDeclaration)
gen_cSharpArchId_Comment_ASTNode = Generalization(general=ASTNode, specific=cSharpArchId_Comment)
gen_cSharpArchId_LineComment_Comment = Generalization(general=Comment, specific=cSharpArchId_LineComment)
gen_cSharpArchId_BlockComment_Comment = Generalization(general=Comment, specific=cSharpArchId_BlockComment)
gen_cSharpArchId_AbstractTypeDeclaration_Type = Generalization(general=Type, specific=cSharpArchId_AbstractTypeDeclaration)
gen_cSharpArchId_TypeDeclaration_AbstractTypeDeclaration = Generalization(general=AbstractTypeDeclaration, specific=cSharpArchId_TypeDeclaration)
gen_cSharpArchId_TypeAcces_Expresion = Generalization(general=Expresion, specific=cSharpArchId_TypeAcces)
gen_cSharpArchId_Expresion_ASTNode = Generalization(general=ASTNode, specific=cSharpArchId_Expresion)
gen_cSharpArchId_BodyDeclaration_NamedElement = Generalization(general=NamedElement, specific=cSharpArchId_BodyDeclaration)
gen_cSharpArchId_Modifier_ASTNode = Generalization(general=ASTNode, specific=cSharpArchId_Modifier)
gen_cSharpArchId_Annotation_Expresion = Generalization(general=Expresion, specific=cSharpArchId_Annotation)
gen_cSharpArchId_AbstractMethodDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=cSharpArchId_AbstractMethodDeclaration)
gen_cSharpArchId_Block_Statement = Generalization(general=Statement, specific=cSharpArchId_Block)
gen_cSharpArchId_Statement_ASTNode = Generalization(general=ASTNode, specific=cSharpArchId_Statement)
gen_cSharpArchId_VariableDeclaration_BodyDeclaration = Generalization(general=BodyDeclaration, specific=cSharpArchId_VariableDeclaration)
gen_cSharpArchId_SingleVariableDeclaration_VariableDeclaration = Generalization(general=VariableDeclaration, specific=cSharpArchId_SingleVariableDeclaration)
gen_cSharpArchId_TypeParameter_Type = Generalization(general=Type, specific=cSharpArchId_TypeParameter)
gen_cSharpArchId_MethodDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=cSharpArchId_MethodDeclaration)
gen_cSharpArchId_ConstructorDeclaration_AbstractMethodDeclaration = Generalization(general=AbstractMethodDeclaration, specific=cSharpArchId_ConstructorDeclaration)
gen_cSharpArchId_AbstractMethodInvocation_ASTNode = Generalization(general=ASTNode, specific=cSharpArchId_AbstractMethodInvocation)
gen_cSharpArchId_MethodInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=cSharpArchId_MethodInvocation)
gen_cSharpArchId_Assignment_Expresion = Generalization(general=Expresion, specific=cSharpArchId_Assignment)
gen_cSharpArchId_ClassInstanceCreation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=cSharpArchId_ClassInstanceCreation)
gen_cSharpArchId_ConstructorInvocation_AbstractMethodInvocation = Generalization(general=AbstractMethodInvocation, specific=cSharpArchId_ConstructorInvocation)
gen_cSharpArchId_ReturnType_Type = Generalization(general=Type, specific=cSharpArchId_ReturnType)

# Domain Model
domain_model = DomainModel(
    name="cSharpArchId",
    types={cSharpArchId_Model, cSharpArchId_Archive, cSharpArchId_CompileUnit, cSharpArchId_EnumerationLiteral, NamedElement, cSharpArchId_NamedElement, ASTNode, cSharpArchId_Type, cSharpArchId_Enumeration, Type, cSharpArchId_ClassDeclaration, TypeDeclaration, cSharpArchId_InterfaceDeclaration, cSharpArchId_PrimitiveType, cSharpArchId_Namespace, cSharpArchId_MethodParameter, cSharpArchId_Comment, cSharpArchId_AbstractTypeDeclaration, cSharpArchId_UsingDeclaration, cSharpArchId_ElementRef, cSharpArchId_ASTNode, cSharpArchId_LineComment, Comment, cSharpArchId_BlockComment, cSharpArchId_BodyDeclaration, cSharpArchId_Modifier, cSharpArchId_TypeDeclaration, AbstractTypeDeclaration, cSharpArchId_TypeAcces, Expresion, cSharpArchId_Expresion, cSharpArchId_Annotation, cSharpArchId_AbstractMethodDeclaration, BodyDeclaration, cSharpArchId_Block, cSharpArchId_VariableDeclaration, cSharpArchId_TypeParameter, Statement, cSharpArchId_Statement, cSharpArchId_SingleVariableDeclaration, VariableDeclaration, cSharpArchId_MethodDeclaration, AbstractMethodDeclaration, cSharpArchId_ConstructorDeclaration, cSharpArchId_AbstractMethodInvocation, cSharpArchId_MethodInvocation, AbstractMethodInvocation, cSharpArchId_Assignment, cSharpArchId_ClassInstanceCreation, cSharpArchId_ConstructorInvocation, cSharpArchId_ReturnType, SimpleType, VisibilityKind, ModifierKind, InheritanceKind},
    associations={archives0, compileUnits1, enumLiterals3, superClass4, classes5, enumerations7, type10, elements12, commentList14, typeDeclaration16, usings18, namespace20, originalCompilationUnit23, compileUnits25, commentsBeforeBody28, commentsAfterBody31, bodyDeclarations34, modifier38, bodyDeclaration39, annotations40, modifier36, typeacces42, body44, parameters45, typeParameters46, thrownExceptions48, returnType51, methodDeclaration54, type55, localVariableDeclaration57, arguments61, expression63, type65, expresion67, typeArguments59},
    generalizations={gen_cSharpArchId_EnumerationLiteral_NamedElement, gen_cSharpArchId_NamedElement_ASTNode, gen_cSharpArchId_Type_NamedElement, gen_cSharpArchId_Enumeration_Type, gen_cSharpArchId_ClassDeclaration_TypeDeclaration, gen_cSharpArchId_InterfaceDeclaration_TypeDeclaration, gen_cSharpArchId_PrimitiveType_Type, gen_cSharpArchId_Namespace_NamedElement, gen_cSharpArchId_MethodParameter_NamedElement, gen_cSharpArchId_CompileUnit_NamedElement, gen_cSharpArchId_ElementRef_Type, gen_cSharpArchId_Archive_NamedElement, gen_cSharpArchId_UsingDeclaration_NamedElement, gen_cSharpArchId_Comment_ASTNode, gen_cSharpArchId_LineComment_Comment, gen_cSharpArchId_BlockComment_Comment, gen_cSharpArchId_AbstractTypeDeclaration_Type, gen_cSharpArchId_TypeDeclaration_AbstractTypeDeclaration, gen_cSharpArchId_TypeAcces_Expresion, gen_cSharpArchId_Expresion_ASTNode, gen_cSharpArchId_BodyDeclaration_NamedElement, gen_cSharpArchId_Modifier_ASTNode, gen_cSharpArchId_Annotation_Expresion, gen_cSharpArchId_AbstractMethodDeclaration_BodyDeclaration, gen_cSharpArchId_Block_Statement, gen_cSharpArchId_Statement_ASTNode, gen_cSharpArchId_VariableDeclaration_BodyDeclaration, gen_cSharpArchId_SingleVariableDeclaration_VariableDeclaration, gen_cSharpArchId_TypeParameter_Type, gen_cSharpArchId_MethodDeclaration_AbstractMethodDeclaration, gen_cSharpArchId_ConstructorDeclaration_AbstractMethodDeclaration, gen_cSharpArchId_AbstractMethodInvocation_ASTNode, gen_cSharpArchId_MethodInvocation_AbstractMethodInvocation, gen_cSharpArchId_Assignment_Expresion, gen_cSharpArchId_ClassInstanceCreation_AbstractMethodInvocation, gen_cSharpArchId_ConstructorInvocation_AbstractMethodInvocation, gen_cSharpArchId_ReturnType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)