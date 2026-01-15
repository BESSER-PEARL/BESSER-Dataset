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
MPrimitiveTypes: Enumeration = Enumeration(
    name="MPrimitiveTypes",
    literals={
            EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="byte"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="char")
    }
)

MVisibility: Enumeration = Enumeration(
    name="MVisibility",
    literals={
            EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="PRIVATE")
    }
)

# Classes
model_AbstractMPackageContainer = Class(name="model::AbstractMPackageContainer", is_abstract=True)
model_MPackage = Class(name="model::MPackage")
model_MRoot = Class(name="model::MRoot")
AbstractMPackageContainer = Class(name="AbstractMPackageContainer")
model_AbstractMExternalType = Class(name="model::AbstractMExternalType", is_abstract=True)
model_AbstractMResource = Class(name="model::AbstractMResource", is_abstract=True)
model_MResource = Class(name="model::MResource")
AbstractMResource = Class(name="AbstractMResource")
model_AbstractMTypeContainer = Class(name="model::AbstractMTypeContainer", is_abstract=True)
model_AbstractMDeclaredType = Class(name="model::AbstractMDeclaredType", is_abstract=True)
model_MCompilationUnit = Class(name="model::MCompilationUnit")
AbstractMTypeContainer = Class(name="AbstractMTypeContainer")
model_AbstractMType = Class(name="model::AbstractMType", is_abstract=True)
model_AbstractMTypeWithNameDeclaration = Class(name="model::AbstractMTypeWithNameDeclaration", is_abstract=True)
model_AbstractMClass = Class(name="model::AbstractMClass", is_abstract=True)
AbstractMType = Class(name="AbstractMType")
model_AbstractMTypeReference = Class(name="model::AbstractMTypeReference", is_abstract=True)
model_MDeclaredTypeReference = Class(name="model::MDeclaredTypeReference")
AbstractMTypeReference = Class(name="AbstractMTypeReference")
model_MExternalTypeReference = Class(name="model::MExternalTypeReference")
model_MPrimitiveTypeReference = Class(name="model::MPrimitiveTypeReference")
model_AbstractModifiers = Class(name="model::AbstractModifiers", is_abstract=True)
model_AbstractMMethodLike = Class(name="model::AbstractMMethodLike", is_abstract=True)
AbstractModifiers = Class(name="AbstractModifiers")
model_AbstractCStatement = Class(name="model::AbstractCStatement", is_abstract=True)
model_MAbstractDeclaredClass = Class(name="model::MAbstractDeclaredClass")
MDeclaredClass = Class(name="MDeclaredClass")
model_MAbstractClassMethodDeclaration = Class(name="model::MAbstractClassMethodDeclaration")
model_MDeclaredClass = Class(name="model::MDeclaredClass")
AbstractMClass = Class(name="AbstractMClass")
AbstractMDeclaredType = Class(name="AbstractMDeclaredType")
model_AbstractMInterface = Class(name="model::AbstractMInterface", is_abstract=True)
model_MStaticClassFieldDeclaration = Class(name="model::MStaticClassFieldDeclaration")
model_MInstanceClassFieldDeclaration = Class(name="model::MInstanceClassFieldDeclaration")
model_MConstructor = Class(name="model::MConstructor")
model_AbstractMMethodImplementation = Class(name="model::AbstractMMethodImplementation", is_abstract=True)
model_MNativeMethodDeclaration = Class(name="model::MNativeMethodDeclaration")
model_MExternalClass = Class(name="model::MExternalClass")
AbstractMExternalType = Class(name="AbstractMExternalType")
model_MDeclaredInterface = Class(name="model::MDeclaredInterface")
AbstractMInterface = Class(name="AbstractMInterface")
model_MConstantInterfaceFieldDeclaration = Class(name="model::MConstantInterfaceFieldDeclaration")
model_MInterfaceMethodDeclaration = Class(name="model::MInterfaceMethodDeclaration")
model_MExternalInterface = Class(name="model::MExternalInterface")
model_AbstractMFieldDeclaration = Class(name="model::AbstractMFieldDeclaration", is_abstract=True)
AbstractMTypeWithNameDeclaration = Class(name="AbstractMTypeWithNameDeclaration")
model_AbstractCExpression = Class(name="model::AbstractCExpression", is_abstract=True)
model_AbstractMClassFieldDeclaration = Class(name="model::AbstractMClassFieldDeclaration", is_abstract=True)
AbstractMFieldDeclaration = Class(name="AbstractMFieldDeclaration")
model_AbstractMImplementableMethodDeclaration = Class(name="model::AbstractMImplementableMethodDeclaration", is_abstract=True)
AbstractMClassFieldDeclaration = Class(name="AbstractMClassFieldDeclaration")
model_AbstractMMethodDeclaration = Class(name="model::AbstractMMethodDeclaration", is_abstract=True)
model_MMethodDeclarationParameter = Class(name="model::MMethodDeclarationParameter")
model_MImplicitMethodDeclaration = Class(name="model::MImplicitMethodDeclaration")
AbstractMMethodDeclaration = Class(name="AbstractMMethodDeclaration")
model_MDirectMethodImplementation = Class(name="model::MDirectMethodImplementation")
model_MDeclaredMethodImplementation = Class(name="model::MDeclaredMethodImplementation")
AbstractMImplementableMethodDeclaration = Class(name="AbstractMImplementableMethodDeclaration")
AbstractMMethodLike = Class(name="AbstractMMethodLike")
model_MMethodImplementationParameter = Class(name="model::MMethodImplementationParameter")
AbstractMMethodImplementation = Class(name="AbstractMMethodImplementation")
model_CBlockStatement = Class(name="model::CBlockStatement")
AbstractCStatement = Class(name="AbstractCStatement")
model_MConstructorParameter = Class(name="model::MConstructorParameter")
model_CUnparsedStatement = Class(name="model::CUnparsedStatement")
model_CConditionalExpression = Class(name="model::CConditionalExpression")
AbstractCExpression = Class(name="AbstractCExpression")
model_CDeclarationStatement = Class(name="model::CDeclarationStatement")
model_CExpressionStatement = Class(name="model::CExpressionStatement")
model_CIfStatement = Class(name="model::CIfStatement")
model_CUnparsedExpression = Class(name="model::CUnparsedExpression")

# model_AbstractMPackageContainer class attributes and methods

# model_MPackage class attributes and methods
model_MPackage_name: Property = Property(name="name", type=StringType)
model_MPackage.attributes={model_MPackage_name}

# model_MRoot class attributes and methods

# AbstractMPackageContainer class attributes and methods

# model_AbstractMExternalType class attributes and methods
model_AbstractMExternalType_fullQualifiedName: Property = Property(name="fullQualifiedName", type=StringType)
model_AbstractMExternalType.attributes={model_AbstractMExternalType_fullQualifiedName}

# model_AbstractMResource class attributes and methods
model_AbstractMResource_name: Property = Property(name="name", type=StringType)
model_AbstractMResource_derived: Property = Property(name="derived", type=BooleanType)
model_AbstractMResource.attributes={model_AbstractMResource_name, model_AbstractMResource_derived}

# model_MResource class attributes and methods
model_MResource_content: Property = Property(name="content", type=StringType)
model_MResource.attributes={model_MResource_content}

# AbstractMResource class attributes and methods

# model_AbstractMTypeContainer class attributes and methods

# model_AbstractMDeclaredType class attributes and methods
model_AbstractMDeclaredType_name: Property = Property(name="name", type=StringType)
model_AbstractMDeclaredType.attributes={model_AbstractMDeclaredType_name}

# model_MCompilationUnit class attributes and methods

# AbstractMTypeContainer class attributes and methods

# model_AbstractMType class attributes and methods

# model_AbstractMTypeWithNameDeclaration class attributes and methods
model_AbstractMTypeWithNameDeclaration_name: Property = Property(name="name", type=StringType)
model_AbstractMTypeWithNameDeclaration.attributes={model_AbstractMTypeWithNameDeclaration_name}

# model_AbstractMClass class attributes and methods

# AbstractMType class attributes and methods

# model_AbstractMTypeReference class attributes and methods
model_AbstractMTypeReference_array: Property = Property(name="array", type=BooleanType)
model_AbstractMTypeReference.attributes={model_AbstractMTypeReference_array}

# model_MDeclaredTypeReference class attributes and methods

# AbstractMTypeReference class attributes and methods

# model_MExternalTypeReference class attributes and methods

# model_MPrimitiveTypeReference class attributes and methods
model_MPrimitiveTypeReference_type: Property = Property(name="type", type=StringType)
model_MPrimitiveTypeReference.attributes={model_MPrimitiveTypeReference_type}

# model_AbstractModifiers class attributes and methods
model_AbstractModifiers_visibility: Property = Property(name="visibility", type=StringType)
model_AbstractModifiers_final: Property = Property(name="final", type=BooleanType)
model_AbstractModifiers_synchronized: Property = Property(name="synchronized", type=BooleanType)
model_AbstractModifiers.attributes={model_AbstractModifiers_final, model_AbstractModifiers_synchronized, model_AbstractModifiers_visibility}

# model_AbstractMMethodLike class attributes and methods

# AbstractModifiers class attributes and methods

# model_AbstractCStatement class attributes and methods

# model_MAbstractDeclaredClass class attributes and methods

# MDeclaredClass class attributes and methods

# model_MAbstractClassMethodDeclaration class attributes and methods
model_MAbstractClassMethodDeclaration_visibility: Property = Property(name="visibility", type=StringType)
model_MAbstractClassMethodDeclaration.attributes={model_MAbstractClassMethodDeclaration_visibility}

# model_MDeclaredClass class attributes and methods

# AbstractMClass class attributes and methods

# AbstractMDeclaredType class attributes and methods

# model_AbstractMInterface class attributes and methods

# model_MStaticClassFieldDeclaration class attributes and methods

# model_MInstanceClassFieldDeclaration class attributes and methods
model_MInstanceClassFieldDeclaration_transient: Property = Property(name="transient", type=BooleanType)
model_MInstanceClassFieldDeclaration.attributes={model_MInstanceClassFieldDeclaration_transient}

# model_MConstructor class attributes and methods

# model_AbstractMMethodImplementation class attributes and methods

# model_MNativeMethodDeclaration class attributes and methods

# model_MExternalClass class attributes and methods

# AbstractMExternalType class attributes and methods

# model_MDeclaredInterface class attributes and methods

# AbstractMInterface class attributes and methods

# model_MConstantInterfaceFieldDeclaration class attributes and methods

# model_MInterfaceMethodDeclaration class attributes and methods

# model_MExternalInterface class attributes and methods

# model_AbstractMFieldDeclaration class attributes and methods

# AbstractMTypeWithNameDeclaration class attributes and methods

# model_AbstractCExpression class attributes and methods

# model_AbstractMClassFieldDeclaration class attributes and methods
model_AbstractMClassFieldDeclaration_visibility: Property = Property(name="visibility", type=StringType)
model_AbstractMClassFieldDeclaration_final: Property = Property(name="final", type=BooleanType)
model_AbstractMClassFieldDeclaration.attributes={model_AbstractMClassFieldDeclaration_final, model_AbstractMClassFieldDeclaration_visibility}

# AbstractMFieldDeclaration class attributes and methods

# model_AbstractMImplementableMethodDeclaration class attributes and methods

# AbstractMClassFieldDeclaration class attributes and methods

# model_AbstractMMethodDeclaration class attributes and methods

# model_MMethodDeclarationParameter class attributes and methods

# model_MImplicitMethodDeclaration class attributes and methods

# AbstractMMethodDeclaration class attributes and methods

# model_MDirectMethodImplementation class attributes and methods

# model_MDeclaredMethodImplementation class attributes and methods

# AbstractMImplementableMethodDeclaration class attributes and methods

# AbstractMMethodLike class attributes and methods

# model_MMethodImplementationParameter class attributes and methods
model_MMethodImplementationParameter_final: Property = Property(name="final", type=BooleanType)
model_MMethodImplementationParameter_name: Property = Property(name="name", type=StringType)
model_MMethodImplementationParameter.attributes={model_MMethodImplementationParameter_name, model_MMethodImplementationParameter_final}

# AbstractMMethodImplementation class attributes and methods

# model_CBlockStatement class attributes and methods

# AbstractCStatement class attributes and methods

# model_MConstructorParameter class attributes and methods
model_MConstructorParameter_final: Property = Property(name="final", type=BooleanType)
model_MConstructorParameter.attributes={model_MConstructorParameter_final}

# model_CUnparsedStatement class attributes and methods
model_CUnparsedStatement_code: Property = Property(name="code", type=StringType)
model_CUnparsedStatement.attributes={model_CUnparsedStatement_code}

# model_CConditionalExpression class attributes and methods

# AbstractCExpression class attributes and methods

# model_CDeclarationStatement class attributes and methods
model_CDeclarationStatement_final: Property = Property(name="final", type=BooleanType)
model_CDeclarationStatement.attributes={model_CDeclarationStatement_final}

# model_CExpressionStatement class attributes and methods

# model_CIfStatement class attributes and methods

# model_CUnparsedExpression class attributes and methods
model_CUnparsedExpression_code: Property = Property(name="code", type=StringType)
model_CUnparsedExpression.attributes={model_CUnparsedExpression_code}

# Relationships
package4: BinaryAssociation = BinaryAssociation(
    name="package4",
    ends={
        Property(name="MPackage5", type=model_AbstractMResource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=model_MPackage, multiplicity=Multiplicity(1, 1))
    }
)
derivedFrom7: BinaryAssociation = BinaryAssociation(
    name="derivedFrom7",
    ends={
        Property(name="AbstractMResource8", type=model_AbstractMResource, multiplicity=Multiplicity(1, 1)),
        Property(name="superOf", type=model_AbstractMResource, multiplicity=Multiplicity(0, 9999))
    }
)
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="MPackage", type=model_AbstractMPackageContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="packageContainer", type=model_MPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalTypes1: BinaryAssociation = BinaryAssociation(
    name="externalTypes1",
    ends={
        Property(name="AbstractMExternalType", type=model_MRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=model_AbstractMExternalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageContainer2: BinaryAssociation = BinaryAssociation(
    name="packageContainer2",
    ends={
        Property(name="AbstractMPackageContainer", type=model_MPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=model_AbstractMPackageContainer, multiplicity=Multiplicity(1, 1))
    }
)
resources3: BinaryAssociation = BinaryAssociation(
    name="resources3",
    ends={
        Property(name="AbstractMResource", type=model_MPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=model_AbstractMResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root15: BinaryAssociation = BinaryAssociation(
    name="root15",
    ends={
        Property(name="MRoot", type=model_AbstractMExternalType, multiplicity=Multiplicity(1, 1)),
        Property(name="externalTypes", type=model_MRoot, multiplicity=Multiplicity(1, 1))
    }
)
superOf10: BinaryAssociation = BinaryAssociation(
    name="superOf10",
    ends={
        Property(name="AbstractMResource11", type=model_AbstractMResource, multiplicity=Multiplicity(1, 1)),
        Property(name="derivedFrom", type=model_AbstractMResource, multiplicity=Multiplicity(0, 9999))
    }
)
types12: BinaryAssociation = BinaryAssociation(
    name="types12",
    ends={
        Property(name="AbstractMDeclaredType", type=model_AbstractMTypeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="typeContainer", type=model_AbstractMDeclaredType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports13: BinaryAssociation = BinaryAssociation(
    name="imports13",
    ends={
        Property(name="model_AbstractMType", type=model_MCompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MCompilationUnit", type=model_AbstractMType, multiplicity=Multiplicity(0, 9999))
    }
)
typeContainer14: BinaryAssociation = BinaryAssociation(
    name="typeContainer14",
    ends={
        Property(name="AbstractMTypeContainer", type=model_AbstractMDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=model_AbstractMTypeContainer, multiplicity=Multiplicity(1, 1))
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="model_AbstractMTypeReference", type=model_AbstractMTypeWithNameDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractMTypeWithNameDeclaration", type=model_AbstractMTypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="model_AbstractMDeclaredType", type=model_MDeclaredTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MDeclaredTypeReference", type=model_AbstractMDeclaredType, multiplicity=Multiplicity(1, 1))
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="model_AbstractMExternalType", type=model_MExternalTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MExternalTypeReference", type=model_AbstractMExternalType, multiplicity=Multiplicity(1, 1))
    }
)
statement18: BinaryAssociation = BinaryAssociation(
    name="statement18",
    ends={
        Property(name="model_AbstractCStatement", type=model_AbstractMMethodLike, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractMMethodLike", type=model_AbstractCStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractMethods32: BinaryAssociation = BinaryAssociation(
    name="abstractMethods32",
    ends={
        Property(name="MAbstractClassMethodDeclaration", type=model_MAbstractDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner33", type=model_MAbstractClassMethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends20: BinaryAssociation = BinaryAssociation(
    name="extends20",
    ends={
        Property(name="model_AbstractMClass", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MDeclaredClass", type=model_AbstractMClass, multiplicity=Multiplicity(0, 1))
    }
)
implements21: BinaryAssociation = BinaryAssociation(
    name="implements21",
    ends={
        Property(name="model_AbstractMInterface", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MDeclaredClass22", type=model_AbstractMInterface, multiplicity=Multiplicity(0, 9999))
    }
)
staticFields23: BinaryAssociation = BinaryAssociation(
    name="staticFields23",
    ends={
        Property(name="MStaticClassFieldDeclaration", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=model_MStaticClassFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instanceFields24: BinaryAssociation = BinaryAssociation(
    name="instanceFields24",
    ends={
        Property(name="MInstanceClassFieldDeclaration", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner25", type=model_MInstanceClassFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors26: BinaryAssociation = BinaryAssociation(
    name="constructors26",
    ends={
        Property(name="MConstructor", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner27", type=model_MConstructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedMethods28: BinaryAssociation = BinaryAssociation(
    name="implementedMethods28",
    ends={
        Property(name="AbstractMMethodImplementation", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner29", type=model_AbstractMMethodImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nativeMethods30: BinaryAssociation = BinaryAssociation(
    name="nativeMethods30",
    ends={
        Property(name="MNativeMethodDeclaration", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner31", type=model_MNativeMethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends34: BinaryAssociation = BinaryAssociation(
    name="extends34",
    ends={
        Property(name="model_AbstractMInterface35", type=model_MDeclaredInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MDeclaredInterface", type=model_AbstractMInterface, multiplicity=Multiplicity(0, 9999))
    }
)
constants36: BinaryAssociation = BinaryAssociation(
    name="constants36",
    ends={
        Property(name="MConstantInterfaceFieldDeclaration", type=model_MDeclaredInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="owner37", type=model_MConstantInterfaceFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods38: BinaryAssociation = BinaryAssociation(
    name="methods38",
    ends={
        Property(name="MInterfaceMethodDeclaration", type=model_MDeclaredInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="owner39", type=model_MInterfaceMethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue40: BinaryAssociation = BinaryAssociation(
    name="initialValue40",
    ends={
        Property(name="model_AbstractCExpression", type=model_AbstractMFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_AbstractMFieldDeclaration", type=model_AbstractCExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner47: BinaryAssociation = BinaryAssociation(
    name="owner47",
    ends={
        Property(name="MDirectMethodImplementation", type=model_MImplicitMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=model_MDirectMethodImplementation, multiplicity=Multiplicity(1, 1))
    }
)
owner41: BinaryAssociation = BinaryAssociation(
    name="owner41",
    ends={
        Property(name="MDeclaredClass", type=model_MStaticClassFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="staticFields", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner42: BinaryAssociation = BinaryAssociation(
    name="owner42",
    ends={
        Property(name="MDeclaredClass43", type=model_MInstanceClassFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="instanceFields", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner44: BinaryAssociation = BinaryAssociation(
    name="owner44",
    ends={
        Property(name="MDeclaredInterface", type=model_MConstantInterfaceFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="constants", type=model_MDeclaredInterface, multiplicity=Multiplicity(1, 1))
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="MMethodDeclarationParameter", type=model_AbstractMMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=model_MMethodDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodDeclaration46: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration46",
    ends={
        Property(name="AbstractMMethodDeclaration", type=model_MMethodDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=model_AbstractMMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
declaration58: BinaryAssociation = BinaryAssociation(
    name="declaration58",
    ends={
        Property(name="AbstractMImplementableMethodDeclaration", type=model_MDeclaredMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="implementations", type=model_AbstractMImplementableMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
implementations48: BinaryAssociation = BinaryAssociation(
    name="implementations48",
    ends={
        Property(name="MDeclaredMethodImplementation", type=model_AbstractMImplementableMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration49", type=model_MDeclaredMethodImplementation, multiplicity=Multiplicity(0, 9999))
    }
)
declaration59: BinaryAssociation = BinaryAssociation(
    name="declaration59",
    ends={
        Property(name="MImplicitMethodDeclaration", type=model_MDirectMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner60", type=model_MImplicitMethodDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owner50: BinaryAssociation = BinaryAssociation(
    name="owner50",
    ends={
        Property(name="MAbstractDeclaredClass", type=model_MAbstractClassMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractMethods", type=model_MAbstractDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner51: BinaryAssociation = BinaryAssociation(
    name="owner51",
    ends={
        Property(name="MDeclaredInterface52", type=model_MInterfaceMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=model_MDeclaredInterface, multiplicity=Multiplicity(1, 1))
    }
)
owner53: BinaryAssociation = BinaryAssociation(
    name="owner53",
    ends={
        Property(name="MDeclaredClass54", type=model_MNativeMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nativeMethods", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner55: BinaryAssociation = BinaryAssociation(
    name="owner55",
    ends={
        Property(name="MDeclaredClass56", type=model_AbstractMMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="implementedMethods", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
parameters57: BinaryAssociation = BinaryAssociation(
    name="parameters57",
    ends={
        Property(name="MMethodImplementationParameter", type=model_AbstractMMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="methodImplementation", type=model_MMethodImplementationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructor67: BinaryAssociation = BinaryAssociation(
    name="constructor67",
    ends={
        Property(name="MConstructor69", type=model_MConstructorParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters68", type=model_MConstructor, multiplicity=Multiplicity(1, 1))
    }
)
methodImplementation61: BinaryAssociation = BinaryAssociation(
    name="methodImplementation61",
    ends={
        Property(name="AbstractMMethodImplementation63", type=model_MMethodImplementationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters62", type=model_AbstractMMethodImplementation, multiplicity=Multiplicity(1, 1))
    }
)
owner64: BinaryAssociation = BinaryAssociation(
    name="owner64",
    ends={
        Property(name="MDeclaredClass65", type=model_MConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructors", type=model_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
parameters66: BinaryAssociation = BinaryAssociation(
    name="parameters66",
    ends={
        Property(name="MConstructorParameter", type=model_MConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructor", type=model_MConstructorParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements70: BinaryAssociation = BinaryAssociation(
    name="statements70",
    ends={
        Property(name="model_AbstractCStatement71", type=model_CBlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CBlockStatement", type=model_AbstractCStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value72: BinaryAssociation = BinaryAssociation(
    name="value72",
    ends={
        Property(name="model_AbstractCExpression73", type=model_CDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CDeclarationStatement", type=model_AbstractCExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="model_AbstractCExpression75", type=model_CExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CExpressionStatement", type=model_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition76: BinaryAssociation = BinaryAssociation(
    name="condition76",
    ends={
        Property(name="model_AbstractCExpression77", type=model_CIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CIfStatement", type=model_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueStatement78: BinaryAssociation = BinaryAssociation(
    name="trueStatement78",
    ends={
        Property(name="model_AbstractCStatement80", type=model_CIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CIfStatement79", type=model_AbstractCStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseStatement81: BinaryAssociation = BinaryAssociation(
    name="falseStatement81",
    ends={
        Property(name="model_AbstractCStatement83", type=model_CIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CIfStatement82", type=model_AbstractCStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="model_AbstractCExpression85", type=model_CConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CConditionalExpression", type=model_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueExpression86: BinaryAssociation = BinaryAssociation(
    name="trueExpression86",
    ends={
        Property(name="model_AbstractCExpression88", type=model_CConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CConditionalExpression87", type=model_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseExpression89: BinaryAssociation = BinaryAssociation(
    name="falseExpression89",
    ends={
        Property(name="model_AbstractCExpression91", type=model_CConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_CConditionalExpression90", type=model_AbstractCExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_MRoot_AbstractMPackageContainer = Generalization(general=AbstractMPackageContainer, specific=model_MRoot)
gen_model_MPackage_AbstractMPackageContainer = Generalization(general=AbstractMPackageContainer, specific=model_MPackage)
gen_model_MResource_AbstractMResource = Generalization(general=AbstractMResource, specific=model_MResource)
gen_model_MCompilationUnit_AbstractMResource = Generalization(general=AbstractMResource, specific=model_MCompilationUnit)
gen_model_MCompilationUnit_AbstractMTypeContainer = Generalization(general=AbstractMTypeContainer, specific=model_MCompilationUnit)
gen_model_AbstractMDeclaredType_AbstractMTypeContainer = Generalization(general=AbstractMTypeContainer, specific=model_AbstractMDeclaredType)
gen_model_MDeclaredTypeReference_AbstractMTypeReference = Generalization(general=AbstractMTypeReference, specific=model_MDeclaredTypeReference)
gen_model_MExternalTypeReference_AbstractMTypeReference = Generalization(general=AbstractMTypeReference, specific=model_MExternalTypeReference)
gen_model_MPrimitiveTypeReference_AbstractMTypeReference = Generalization(general=AbstractMTypeReference, specific=model_MPrimitiveTypeReference)
gen_model_AbstractMMethodLike_AbstractModifiers = Generalization(general=AbstractModifiers, specific=model_AbstractMMethodLike)
gen_model_MAbstractDeclaredClass_MDeclaredClass = Generalization(general=MDeclaredClass, specific=model_MAbstractDeclaredClass)
gen_model_AbstractMClass_AbstractMType = Generalization(general=AbstractMType, specific=model_AbstractMClass)
gen_model_MDeclaredClass_AbstractMClass = Generalization(general=AbstractMClass, specific=model_MDeclaredClass)
gen_model_MDeclaredClass_AbstractMDeclaredType = Generalization(general=AbstractMDeclaredType, specific=model_MDeclaredClass)
gen_model_MExternalClass_AbstractMClass = Generalization(general=AbstractMClass, specific=model_MExternalClass)
gen_model_MExternalClass_AbstractMExternalType = Generalization(general=AbstractMExternalType, specific=model_MExternalClass)
gen_model_AbstractMInterface_AbstractMType = Generalization(general=AbstractMType, specific=model_AbstractMInterface)
gen_model_MDeclaredInterface_AbstractMInterface = Generalization(general=AbstractMInterface, specific=model_MDeclaredInterface)
gen_model_MDeclaredInterface_AbstractMDeclaredType = Generalization(general=AbstractMDeclaredType, specific=model_MDeclaredInterface)
gen_model_MExternalInterface_AbstractMInterface = Generalization(general=AbstractMInterface, specific=model_MExternalInterface)
gen_model_MExternalInterface_AbstractMExternalType = Generalization(general=AbstractMExternalType, specific=model_MExternalInterface)
gen_model_AbstractMFieldDeclaration_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=model_AbstractMFieldDeclaration)
gen_model_AbstractMClassFieldDeclaration_AbstractMFieldDeclaration = Generalization(general=AbstractMFieldDeclaration, specific=model_AbstractMClassFieldDeclaration)
gen_model_AbstractMImplementableMethodDeclaration_AbstractMMethodDeclaration = Generalization(general=AbstractMMethodDeclaration, specific=model_AbstractMImplementableMethodDeclaration)
gen_model_MStaticClassFieldDeclaration_AbstractMClassFieldDeclaration = Generalization(general=AbstractMClassFieldDeclaration, specific=model_MStaticClassFieldDeclaration)
gen_model_MInstanceClassFieldDeclaration_AbstractMClassFieldDeclaration = Generalization(general=AbstractMClassFieldDeclaration, specific=model_MInstanceClassFieldDeclaration)
gen_model_MConstantInterfaceFieldDeclaration_AbstractMFieldDeclaration = Generalization(general=AbstractMFieldDeclaration, specific=model_MConstantInterfaceFieldDeclaration)
gen_model_AbstractMMethodDeclaration_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=model_AbstractMMethodDeclaration)
gen_model_MMethodDeclarationParameter_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=model_MMethodDeclarationParameter)
gen_model_MImplicitMethodDeclaration_AbstractMMethodDeclaration = Generalization(general=AbstractMMethodDeclaration, specific=model_MImplicitMethodDeclaration)
gen_model_MDirectMethodImplementation_AbstractMMethodImplementation = Generalization(general=AbstractMMethodImplementation, specific=model_MDirectMethodImplementation)
gen_model_MAbstractClassMethodDeclaration_AbstractMImplementableMethodDeclaration = Generalization(general=AbstractMImplementableMethodDeclaration, specific=model_MAbstractClassMethodDeclaration)
gen_model_MInterfaceMethodDeclaration_AbstractMImplementableMethodDeclaration = Generalization(general=AbstractMImplementableMethodDeclaration, specific=model_MInterfaceMethodDeclaration)
gen_model_MNativeMethodDeclaration_AbstractMMethodDeclaration = Generalization(general=AbstractMMethodDeclaration, specific=model_MNativeMethodDeclaration)
gen_model_AbstractMMethodImplementation_AbstractMMethodLike = Generalization(general=AbstractMMethodLike, specific=model_AbstractMMethodImplementation)
gen_model_MDeclaredMethodImplementation_AbstractMMethodImplementation = Generalization(general=AbstractMMethodImplementation, specific=model_MDeclaredMethodImplementation)
gen_model_CBlockStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=model_CBlockStatement)
gen_model_MConstructor_AbstractMMethodLike = Generalization(general=AbstractMMethodLike, specific=model_MConstructor)
gen_model_MConstructorParameter_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=model_MConstructorParameter)
gen_model_CUnparsedStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=model_CUnparsedStatement)
gen_model_CConditionalExpression_AbstractCExpression = Generalization(general=AbstractCExpression, specific=model_CConditionalExpression)
gen_model_CDeclarationStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=model_CDeclarationStatement)
gen_model_CDeclarationStatement_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=model_CDeclarationStatement)
gen_model_CExpressionStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=model_CExpressionStatement)
gen_model_CIfStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=model_CIfStatement)
gen_model_CUnparsedExpression_AbstractCExpression = Generalization(general=AbstractCExpression, specific=model_CUnparsedExpression)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_AbstractMPackageContainer, model_MPackage, model_MRoot, AbstractMPackageContainer, model_AbstractMExternalType, model_AbstractMResource, model_MResource, AbstractMResource, model_AbstractMTypeContainer, model_AbstractMDeclaredType, model_MCompilationUnit, AbstractMTypeContainer, model_AbstractMType, model_AbstractMTypeWithNameDeclaration, model_AbstractMClass, AbstractMType, model_AbstractMTypeReference, model_MDeclaredTypeReference, AbstractMTypeReference, model_MExternalTypeReference, model_MPrimitiveTypeReference, model_AbstractModifiers, model_AbstractMMethodLike, AbstractModifiers, model_AbstractCStatement, model_MAbstractDeclaredClass, MDeclaredClass, model_MAbstractClassMethodDeclaration, model_MDeclaredClass, AbstractMClass, AbstractMDeclaredType, model_AbstractMInterface, model_MStaticClassFieldDeclaration, model_MInstanceClassFieldDeclaration, model_MConstructor, model_AbstractMMethodImplementation, model_MNativeMethodDeclaration, model_MExternalClass, AbstractMExternalType, model_MDeclaredInterface, AbstractMInterface, model_MConstantInterfaceFieldDeclaration, model_MInterfaceMethodDeclaration, model_MExternalInterface, model_AbstractMFieldDeclaration, AbstractMTypeWithNameDeclaration, model_AbstractCExpression, model_AbstractMClassFieldDeclaration, AbstractMFieldDeclaration, model_AbstractMImplementableMethodDeclaration, AbstractMClassFieldDeclaration, model_AbstractMMethodDeclaration, model_MMethodDeclarationParameter, model_MImplicitMethodDeclaration, AbstractMMethodDeclaration, model_MDirectMethodImplementation, model_MDeclaredMethodImplementation, AbstractMImplementableMethodDeclaration, AbstractMMethodLike, model_MMethodImplementationParameter, AbstractMMethodImplementation, model_CBlockStatement, AbstractCStatement, model_MConstructorParameter, model_CUnparsedStatement, model_CConditionalExpression, AbstractCExpression, model_CDeclarationStatement, model_CExpressionStatement, model_CIfStatement, model_CUnparsedExpression, MPrimitiveTypes, MVisibility},
    associations={package4, derivedFrom7, packages0, externalTypes1, packageContainer2, resources3, root15, superOf10, types12, imports13, typeContainer14, type19, type16, type17, statement18, abstractMethods32, extends20, implements21, staticFields23, instanceFields24, constructors26, implementedMethods28, nativeMethods30, extends34, constants36, methods38, initialValue40, owner47, owner41, owner42, owner44, parameters45, methodDeclaration46, declaration58, implementations48, declaration59, owner50, owner51, owner53, owner55, parameters57, constructor67, methodImplementation61, owner64, parameters66, statements70, value72, expression74, condition76, trueStatement78, falseStatement81, condition84, trueExpression86, falseExpression89},
    generalizations={gen_model_MRoot_AbstractMPackageContainer, gen_model_MPackage_AbstractMPackageContainer, gen_model_MResource_AbstractMResource, gen_model_MCompilationUnit_AbstractMResource, gen_model_MCompilationUnit_AbstractMTypeContainer, gen_model_AbstractMDeclaredType_AbstractMTypeContainer, gen_model_MDeclaredTypeReference_AbstractMTypeReference, gen_model_MExternalTypeReference_AbstractMTypeReference, gen_model_MPrimitiveTypeReference_AbstractMTypeReference, gen_model_AbstractMMethodLike_AbstractModifiers, gen_model_MAbstractDeclaredClass_MDeclaredClass, gen_model_AbstractMClass_AbstractMType, gen_model_MDeclaredClass_AbstractMClass, gen_model_MDeclaredClass_AbstractMDeclaredType, gen_model_MExternalClass_AbstractMClass, gen_model_MExternalClass_AbstractMExternalType, gen_model_AbstractMInterface_AbstractMType, gen_model_MDeclaredInterface_AbstractMInterface, gen_model_MDeclaredInterface_AbstractMDeclaredType, gen_model_MExternalInterface_AbstractMInterface, gen_model_MExternalInterface_AbstractMExternalType, gen_model_AbstractMFieldDeclaration_AbstractMTypeWithNameDeclaration, gen_model_AbstractMClassFieldDeclaration_AbstractMFieldDeclaration, gen_model_AbstractMImplementableMethodDeclaration_AbstractMMethodDeclaration, gen_model_MStaticClassFieldDeclaration_AbstractMClassFieldDeclaration, gen_model_MInstanceClassFieldDeclaration_AbstractMClassFieldDeclaration, gen_model_MConstantInterfaceFieldDeclaration_AbstractMFieldDeclaration, gen_model_AbstractMMethodDeclaration_AbstractMTypeWithNameDeclaration, gen_model_MMethodDeclarationParameter_AbstractMTypeWithNameDeclaration, gen_model_MImplicitMethodDeclaration_AbstractMMethodDeclaration, gen_model_MDirectMethodImplementation_AbstractMMethodImplementation, gen_model_MAbstractClassMethodDeclaration_AbstractMImplementableMethodDeclaration, gen_model_MInterfaceMethodDeclaration_AbstractMImplementableMethodDeclaration, gen_model_MNativeMethodDeclaration_AbstractMMethodDeclaration, gen_model_AbstractMMethodImplementation_AbstractMMethodLike, gen_model_MDeclaredMethodImplementation_AbstractMMethodImplementation, gen_model_CBlockStatement_AbstractCStatement, gen_model_MConstructor_AbstractMMethodLike, gen_model_MConstructorParameter_AbstractMTypeWithNameDeclaration, gen_model_CUnparsedStatement_AbstractCStatement, gen_model_CConditionalExpression_AbstractCExpression, gen_model_CDeclarationStatement_AbstractCStatement, gen_model_CDeclarationStatement_AbstractMTypeWithNameDeclaration, gen_model_CExpressionStatement_AbstractCStatement, gen_model_CIfStatement_AbstractCStatement, gen_model_CUnparsedExpression_AbstractCExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)