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
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC")
    }
)

# Classes
jsm_AbstractMPackageContainer = Class(name="jsm::AbstractMPackageContainer", is_abstract=True)
jsm_MPackage = Class(name="jsm::MPackage")
jsm_MRoot = Class(name="jsm::MRoot")
AbstractMPackageContainer = Class(name="AbstractMPackageContainer")
jsm_AbstractMExternalType = Class(name="jsm::AbstractMExternalType", is_abstract=True)
jsm_MResource = Class(name="jsm::MResource")
AbstractMResource = Class(name="AbstractMResource")
jsm_AbstractMTypeContainer = Class(name="jsm::AbstractMTypeContainer", is_abstract=True)
jsm_AbstractMDeclaredType = Class(name="jsm::AbstractMDeclaredType", is_abstract=True)
jsm_AbstractMResource = Class(name="jsm::AbstractMResource", is_abstract=True)
jsm_MCompilationUnit = Class(name="jsm::MCompilationUnit")
AbstractMTypeContainer = Class(name="AbstractMTypeContainer")
jsm_AbstractMType = Class(name="jsm::AbstractMType", is_abstract=True)
jsm_AbstractMTypeReference = Class(name="jsm::AbstractMTypeReference", is_abstract=True)
jsm_MDeclaredTypeReference = Class(name="jsm::MDeclaredTypeReference")
AbstractMTypeReference = Class(name="AbstractMTypeReference")
jsm_MExternalTypeReference = Class(name="jsm::MExternalTypeReference")
jsm_MPrimitiveTypeReference = Class(name="jsm::MPrimitiveTypeReference")
jsm_AbstractModifiers = Class(name="jsm::AbstractModifiers", is_abstract=True)
jsm_AbstractMMethodLike = Class(name="jsm::AbstractMMethodLike", is_abstract=True)
AbstractModifiers = Class(name="AbstractModifiers")
jsm_AbstractCStatement = Class(name="jsm::AbstractCStatement", is_abstract=True)
jsm_AbstractMTypeWithNameDeclaration = Class(name="jsm::AbstractMTypeWithNameDeclaration", is_abstract=True)
jsm_AbstractMClass = Class(name="jsm::AbstractMClass", is_abstract=True)
AbstractMType = Class(name="AbstractMType")
jsm_MDeclaredClass = Class(name="jsm::MDeclaredClass")
AbstractMClass = Class(name="AbstractMClass")
AbstractMDeclaredType = Class(name="AbstractMDeclaredType")
jsm_AbstractMInterface = Class(name="jsm::AbstractMInterface", is_abstract=True)
jsm_MStaticClassFieldDeclaration = Class(name="jsm::MStaticClassFieldDeclaration")
jsm_MInstanceClassFieldDeclaration = Class(name="jsm::MInstanceClassFieldDeclaration")
jsm_MConstructor = Class(name="jsm::MConstructor")
jsm_AbstractMMethodImplementation = Class(name="jsm::AbstractMMethodImplementation", is_abstract=True)
jsm_MAbstractDeclaredClass = Class(name="jsm::MAbstractDeclaredClass")
MDeclaredClass = Class(name="MDeclaredClass")
jsm_MAbstractClassMethodDeclaration = Class(name="jsm::MAbstractClassMethodDeclaration")
jsm_MExternalClass = Class(name="jsm::MExternalClass")
AbstractMExternalType = Class(name="AbstractMExternalType")
jsm_MDeclaredInterface = Class(name="jsm::MDeclaredInterface")
AbstractMInterface = Class(name="AbstractMInterface")
jsm_MConstantInterfaceFieldDeclaration = Class(name="jsm::MConstantInterfaceFieldDeclaration")
jsm_MInterfaceMethodDeclaration = Class(name="jsm::MInterfaceMethodDeclaration")
jsm_MExternalInterface = Class(name="jsm::MExternalInterface")
jsm_MNativeMethodDeclaration = Class(name="jsm::MNativeMethodDeclaration")
jsm_AbstractMClassFieldDeclaration = Class(name="jsm::AbstractMClassFieldDeclaration", is_abstract=True)
AbstractMFieldDeclaration = Class(name="AbstractMFieldDeclaration")
AbstractMClassFieldDeclaration = Class(name="AbstractMClassFieldDeclaration")
jsm_AbstractMMethodDeclaration = Class(name="jsm::AbstractMMethodDeclaration", is_abstract=True)
jsm_MMethodDeclarationParameter = Class(name="jsm::MMethodDeclarationParameter")
jsm_AbstractMFieldDeclaration = Class(name="jsm::AbstractMFieldDeclaration", is_abstract=True)
AbstractMTypeWithNameDeclaration = Class(name="AbstractMTypeWithNameDeclaration")
jsm_AbstractCExpression = Class(name="jsm::AbstractCExpression", is_abstract=True)
jsm_MImplicitMethodDeclaration = Class(name="jsm::MImplicitMethodDeclaration")
AbstractMMethodDeclaration = Class(name="AbstractMMethodDeclaration")
jsm_MDirectMethodImplementation = Class(name="jsm::MDirectMethodImplementation")
jsm_AbstractMImplementableMethodDeclaration = Class(name="jsm::AbstractMImplementableMethodDeclaration", is_abstract=True)
jsm_MDeclaredMethodImplementation = Class(name="jsm::MDeclaredMethodImplementation")
AbstractMImplementableMethodDeclaration = Class(name="AbstractMImplementableMethodDeclaration")
jsm_MMethodImplementationParameter = Class(name="jsm::MMethodImplementationParameter")
AbstractMMethodImplementation = Class(name="AbstractMMethodImplementation")
AbstractMMethodLike = Class(name="AbstractMMethodLike")
jsm_MConstructorParameter = Class(name="jsm::MConstructorParameter")
jsm_CBlockStatement = Class(name="jsm::CBlockStatement")
AbstractCStatement = Class(name="AbstractCStatement")
jsm_CDeclarationStatement = Class(name="jsm::CDeclarationStatement")
jsm_CExpressionStatement = Class(name="jsm::CExpressionStatement")
jsm_CIfStatement = Class(name="jsm::CIfStatement")
jsm_CConditionalExpression = Class(name="jsm::CConditionalExpression")
AbstractCExpression = Class(name="AbstractCExpression")
jsm_CUnparsedExpression = Class(name="jsm::CUnparsedExpression")
jsm_CUnparsedStatement = Class(name="jsm::CUnparsedStatement")

# jsm_AbstractMPackageContainer class attributes and methods

# jsm_MPackage class attributes and methods
jsm_MPackage_name: Property = Property(name="name", type=StringType)
jsm_MPackage.attributes={jsm_MPackage_name}

# jsm_MRoot class attributes and methods

# AbstractMPackageContainer class attributes and methods

# jsm_AbstractMExternalType class attributes and methods
jsm_AbstractMExternalType_fullQualifiedName: Property = Property(name="fullQualifiedName", type=StringType)
jsm_AbstractMExternalType.attributes={jsm_AbstractMExternalType_fullQualifiedName}

# jsm_MResource class attributes and methods
jsm_MResource_content: Property = Property(name="content", type=StringType)
jsm_MResource.attributes={jsm_MResource_content}

# AbstractMResource class attributes and methods

# jsm_AbstractMTypeContainer class attributes and methods

# jsm_AbstractMDeclaredType class attributes and methods
jsm_AbstractMDeclaredType_name: Property = Property(name="name", type=StringType)
jsm_AbstractMDeclaredType.attributes={jsm_AbstractMDeclaredType_name}

# jsm_AbstractMResource class attributes and methods
jsm_AbstractMResource_name: Property = Property(name="name", type=StringType)
jsm_AbstractMResource_derived: Property = Property(name="derived", type=BooleanType)
jsm_AbstractMResource.attributes={jsm_AbstractMResource_derived, jsm_AbstractMResource_name}

# jsm_MCompilationUnit class attributes and methods

# AbstractMTypeContainer class attributes and methods

# jsm_AbstractMType class attributes and methods

# jsm_AbstractMTypeReference class attributes and methods
jsm_AbstractMTypeReference_array: Property = Property(name="array", type=BooleanType)
jsm_AbstractMTypeReference.attributes={jsm_AbstractMTypeReference_array}

# jsm_MDeclaredTypeReference class attributes and methods

# AbstractMTypeReference class attributes and methods

# jsm_MExternalTypeReference class attributes and methods

# jsm_MPrimitiveTypeReference class attributes and methods
jsm_MPrimitiveTypeReference_type: Property = Property(name="type", type=StringType)
jsm_MPrimitiveTypeReference.attributes={jsm_MPrimitiveTypeReference_type}

# jsm_AbstractModifiers class attributes and methods
jsm_AbstractModifiers_visibility: Property = Property(name="visibility", type=StringType)
jsm_AbstractModifiers_final: Property = Property(name="final", type=BooleanType)
jsm_AbstractModifiers_synchronized: Property = Property(name="synchronized", type=BooleanType)
jsm_AbstractModifiers.attributes={jsm_AbstractModifiers_final, jsm_AbstractModifiers_visibility, jsm_AbstractModifiers_synchronized}

# jsm_AbstractMMethodLike class attributes and methods

# AbstractModifiers class attributes and methods

# jsm_AbstractCStatement class attributes and methods

# jsm_AbstractMTypeWithNameDeclaration class attributes and methods
jsm_AbstractMTypeWithNameDeclaration_name: Property = Property(name="name", type=StringType)
jsm_AbstractMTypeWithNameDeclaration.attributes={jsm_AbstractMTypeWithNameDeclaration_name}

# jsm_AbstractMClass class attributes and methods

# AbstractMType class attributes and methods

# jsm_MDeclaredClass class attributes and methods

# AbstractMClass class attributes and methods

# AbstractMDeclaredType class attributes and methods

# jsm_AbstractMInterface class attributes and methods

# jsm_MStaticClassFieldDeclaration class attributes and methods

# jsm_MInstanceClassFieldDeclaration class attributes and methods
jsm_MInstanceClassFieldDeclaration_transient: Property = Property(name="transient", type=BooleanType)
jsm_MInstanceClassFieldDeclaration.attributes={jsm_MInstanceClassFieldDeclaration_transient}

# jsm_MConstructor class attributes and methods

# jsm_AbstractMMethodImplementation class attributes and methods

# jsm_MAbstractDeclaredClass class attributes and methods

# MDeclaredClass class attributes and methods

# jsm_MAbstractClassMethodDeclaration class attributes and methods
jsm_MAbstractClassMethodDeclaration_visibility: Property = Property(name="visibility", type=StringType)
jsm_MAbstractClassMethodDeclaration.attributes={jsm_MAbstractClassMethodDeclaration_visibility}

# jsm_MExternalClass class attributes and methods

# AbstractMExternalType class attributes and methods

# jsm_MDeclaredInterface class attributes and methods

# AbstractMInterface class attributes and methods

# jsm_MConstantInterfaceFieldDeclaration class attributes and methods

# jsm_MInterfaceMethodDeclaration class attributes and methods

# jsm_MExternalInterface class attributes and methods

# jsm_MNativeMethodDeclaration class attributes and methods

# jsm_AbstractMClassFieldDeclaration class attributes and methods
jsm_AbstractMClassFieldDeclaration_visibility: Property = Property(name="visibility", type=StringType)
jsm_AbstractMClassFieldDeclaration_final: Property = Property(name="final", type=BooleanType)
jsm_AbstractMClassFieldDeclaration.attributes={jsm_AbstractMClassFieldDeclaration_final, jsm_AbstractMClassFieldDeclaration_visibility}

# AbstractMFieldDeclaration class attributes and methods

# AbstractMClassFieldDeclaration class attributes and methods

# jsm_AbstractMMethodDeclaration class attributes and methods

# jsm_MMethodDeclarationParameter class attributes and methods

# jsm_AbstractMFieldDeclaration class attributes and methods

# AbstractMTypeWithNameDeclaration class attributes and methods

# jsm_AbstractCExpression class attributes and methods

# jsm_MImplicitMethodDeclaration class attributes and methods

# AbstractMMethodDeclaration class attributes and methods

# jsm_MDirectMethodImplementation class attributes and methods

# jsm_AbstractMImplementableMethodDeclaration class attributes and methods

# jsm_MDeclaredMethodImplementation class attributes and methods

# AbstractMImplementableMethodDeclaration class attributes and methods

# jsm_MMethodImplementationParameter class attributes and methods
jsm_MMethodImplementationParameter_final: Property = Property(name="final", type=BooleanType)
jsm_MMethodImplementationParameter_name: Property = Property(name="name", type=StringType)
jsm_MMethodImplementationParameter.attributes={jsm_MMethodImplementationParameter_name, jsm_MMethodImplementationParameter_final}

# AbstractMMethodImplementation class attributes and methods

# AbstractMMethodLike class attributes and methods

# jsm_MConstructorParameter class attributes and methods
jsm_MConstructorParameter_final: Property = Property(name="final", type=BooleanType)
jsm_MConstructorParameter.attributes={jsm_MConstructorParameter_final}

# jsm_CBlockStatement class attributes and methods

# AbstractCStatement class attributes and methods

# jsm_CDeclarationStatement class attributes and methods
jsm_CDeclarationStatement_final: Property = Property(name="final", type=BooleanType)
jsm_CDeclarationStatement.attributes={jsm_CDeclarationStatement_final}

# jsm_CExpressionStatement class attributes and methods

# jsm_CIfStatement class attributes and methods

# jsm_CConditionalExpression class attributes and methods

# AbstractCExpression class attributes and methods

# jsm_CUnparsedExpression class attributes and methods
jsm_CUnparsedExpression_code: Property = Property(name="code", type=StringType)
jsm_CUnparsedExpression.attributes={jsm_CUnparsedExpression_code}

# jsm_CUnparsedStatement class attributes and methods
jsm_CUnparsedStatement_code: Property = Property(name="code", type=StringType)
jsm_CUnparsedStatement.attributes={jsm_CUnparsedStatement_code}

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="MPackage", type=jsm_AbstractMPackageContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="packageContainer", type=jsm_MPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalTypes1: BinaryAssociation = BinaryAssociation(
    name="externalTypes1",
    ends={
        Property(name="AbstractMExternalType", type=jsm_MRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=jsm_AbstractMExternalType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageContainer2: BinaryAssociation = BinaryAssociation(
    name="packageContainer2",
    ends={
        Property(name="AbstractMPackageContainer", type=jsm_MPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=jsm_AbstractMPackageContainer, multiplicity=Multiplicity(1, 1))
    }
)
resources3: BinaryAssociation = BinaryAssociation(
    name="resources3",
    ends={
        Property(name="AbstractMResource", type=jsm_MPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=jsm_AbstractMResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package4: BinaryAssociation = BinaryAssociation(
    name="package4",
    ends={
        Property(name="MPackage5", type=jsm_AbstractMResource, multiplicity=Multiplicity(1, 1)),
        Property(name="resources", type=jsm_MPackage, multiplicity=Multiplicity(1, 1))
    }
)
derivedFrom7: BinaryAssociation = BinaryAssociation(
    name="derivedFrom7",
    ends={
        Property(name="AbstractMResource8", type=jsm_AbstractMResource, multiplicity=Multiplicity(1, 1)),
        Property(name="superOf", type=jsm_AbstractMResource, multiplicity=Multiplicity(0, 9999))
    }
)
superOf10: BinaryAssociation = BinaryAssociation(
    name="superOf10",
    ends={
        Property(name="AbstractMResource11", type=jsm_AbstractMResource, multiplicity=Multiplicity(1, 1)),
        Property(name="derivedFrom", type=jsm_AbstractMResource, multiplicity=Multiplicity(0, 9999))
    }
)
imports13: BinaryAssociation = BinaryAssociation(
    name="imports13",
    ends={
        Property(name="jsm_AbstractMType", type=jsm_MCompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_MCompilationUnit", type=jsm_AbstractMType, multiplicity=Multiplicity(0, 9999))
    }
)
typeContainer14: BinaryAssociation = BinaryAssociation(
    name="typeContainer14",
    ends={
        Property(name="AbstractMTypeContainer", type=jsm_AbstractMDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=jsm_AbstractMTypeContainer, multiplicity=Multiplicity(1, 1))
    }
)
root15: BinaryAssociation = BinaryAssociation(
    name="root15",
    ends={
        Property(name="MRoot", type=jsm_AbstractMExternalType, multiplicity=Multiplicity(1, 1)),
        Property(name="externalTypes", type=jsm_MRoot, multiplicity=Multiplicity(1, 1))
    }
)
types12: BinaryAssociation = BinaryAssociation(
    name="types12",
    ends={
        Property(name="AbstractMDeclaredType", type=jsm_AbstractMTypeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="typeContainer", type=jsm_AbstractMDeclaredType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="jsm_AbstractMExternalType", type=jsm_MExternalTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_MExternalTypeReference", type=jsm_AbstractMExternalType, multiplicity=Multiplicity(1, 1))
    }
)
statement18: BinaryAssociation = BinaryAssociation(
    name="statement18",
    ends={
        Property(name="jsm_AbstractCStatement", type=jsm_AbstractMMethodLike, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_AbstractMMethodLike", type=jsm_AbstractCStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="jsm_AbstractMTypeReference", type=jsm_AbstractMTypeWithNameDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_AbstractMTypeWithNameDeclaration", type=jsm_AbstractMTypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="jsm_AbstractMDeclaredType", type=jsm_MDeclaredTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_MDeclaredTypeReference", type=jsm_AbstractMDeclaredType, multiplicity=Multiplicity(1, 1))
    }
)
extends20: BinaryAssociation = BinaryAssociation(
    name="extends20",
    ends={
        Property(name="jsm_AbstractMClass", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_MDeclaredClass", type=jsm_AbstractMClass, multiplicity=Multiplicity(0, 1))
    }
)
implements21: BinaryAssociation = BinaryAssociation(
    name="implements21",
    ends={
        Property(name="jsm_AbstractMInterface", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_MDeclaredClass22", type=jsm_AbstractMInterface, multiplicity=Multiplicity(0, 9999))
    }
)
staticFields23: BinaryAssociation = BinaryAssociation(
    name="staticFields23",
    ends={
        Property(name="MStaticClassFieldDeclaration", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=jsm_MStaticClassFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instanceFields24: BinaryAssociation = BinaryAssociation(
    name="instanceFields24",
    ends={
        Property(name="MInstanceClassFieldDeclaration", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner25", type=jsm_MInstanceClassFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors26: BinaryAssociation = BinaryAssociation(
    name="constructors26",
    ends={
        Property(name="MConstructor", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner27", type=jsm_MConstructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedMethods28: BinaryAssociation = BinaryAssociation(
    name="implementedMethods28",
    ends={
        Property(name="AbstractMMethodImplementation", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner29", type=jsm_AbstractMMethodImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nativeMethods30: BinaryAssociation = BinaryAssociation(
    name="nativeMethods30",
    ends={
        Property(name="owner31", type=jsm_MNativeMethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="MNativeMethodDeclaration", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
abstractMethods32: BinaryAssociation = BinaryAssociation(
    name="abstractMethods32",
    ends={
        Property(name="MAbstractClassMethodDeclaration", type=jsm_MAbstractDeclaredClass, multiplicity=Multiplicity(1, 1)),
        Property(name="owner33", type=jsm_MAbstractClassMethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends34: BinaryAssociation = BinaryAssociation(
    name="extends34",
    ends={
        Property(name="jsm_AbstractMInterface35", type=jsm_MDeclaredInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_MDeclaredInterface", type=jsm_AbstractMInterface, multiplicity=Multiplicity(0, 9999))
    }
)
constants36: BinaryAssociation = BinaryAssociation(
    name="constants36",
    ends={
        Property(name="MConstantInterfaceFieldDeclaration", type=jsm_MDeclaredInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="owner37", type=jsm_MConstantInterfaceFieldDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods38: BinaryAssociation = BinaryAssociation(
    name="methods38",
    ends={
        Property(name="MInterfaceMethodDeclaration", type=jsm_MDeclaredInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="owner39", type=jsm_MInterfaceMethodDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner41: BinaryAssociation = BinaryAssociation(
    name="owner41",
    ends={
        Property(name="MDeclaredClass", type=jsm_MStaticClassFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="staticFields", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner42: BinaryAssociation = BinaryAssociation(
    name="owner42",
    ends={
        Property(name="MDeclaredClass43", type=jsm_MInstanceClassFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="instanceFields", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner44: BinaryAssociation = BinaryAssociation(
    name="owner44",
    ends={
        Property(name="MDeclaredInterface", type=jsm_MConstantInterfaceFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="constants", type=jsm_MDeclaredInterface, multiplicity=Multiplicity(1, 1))
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="MMethodDeclarationParameter", type=jsm_AbstractMMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methodDeclaration", type=jsm_MMethodDeclarationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue40: BinaryAssociation = BinaryAssociation(
    name="initialValue40",
    ends={
        Property(name="jsm_AbstractCExpression", type=jsm_AbstractMFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_AbstractMFieldDeclaration", type=jsm_AbstractCExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodDeclaration46: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration46",
    ends={
        Property(name="AbstractMMethodDeclaration", type=jsm_MMethodDeclarationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=jsm_AbstractMMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
owner47: BinaryAssociation = BinaryAssociation(
    name="owner47",
    ends={
        Property(name="MDirectMethodImplementation", type=jsm_MImplicitMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=jsm_MDirectMethodImplementation, multiplicity=Multiplicity(1, 1))
    }
)
implementations48: BinaryAssociation = BinaryAssociation(
    name="implementations48",
    ends={
        Property(name="MDeclaredMethodImplementation", type=jsm_AbstractMImplementableMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration49", type=jsm_MDeclaredMethodImplementation, multiplicity=Multiplicity(0, 9999))
    }
)
owner50: BinaryAssociation = BinaryAssociation(
    name="owner50",
    ends={
        Property(name="MAbstractDeclaredClass", type=jsm_MAbstractClassMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="abstractMethods", type=jsm_MAbstractDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner51: BinaryAssociation = BinaryAssociation(
    name="owner51",
    ends={
        Property(name="MDeclaredInterface52", type=jsm_MInterfaceMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=jsm_MDeclaredInterface, multiplicity=Multiplicity(1, 1))
    }
)
owner53: BinaryAssociation = BinaryAssociation(
    name="owner53",
    ends={
        Property(name="MDeclaredClass54", type=jsm_MNativeMethodDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="nativeMethods", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
owner55: BinaryAssociation = BinaryAssociation(
    name="owner55",
    ends={
        Property(name="MDeclaredClass56", type=jsm_AbstractMMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="implementedMethods", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
parameters57: BinaryAssociation = BinaryAssociation(
    name="parameters57",
    ends={
        Property(name="MMethodImplementationParameter", type=jsm_AbstractMMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="methodImplementation", type=jsm_MMethodImplementationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration58: BinaryAssociation = BinaryAssociation(
    name="declaration58",
    ends={
        Property(name="AbstractMImplementableMethodDeclaration", type=jsm_MDeclaredMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="implementations", type=jsm_AbstractMImplementableMethodDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
declaration59: BinaryAssociation = BinaryAssociation(
    name="declaration59",
    ends={
        Property(name="MImplicitMethodDeclaration", type=jsm_MDirectMethodImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="owner60", type=jsm_MImplicitMethodDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owner64: BinaryAssociation = BinaryAssociation(
    name="owner64",
    ends={
        Property(name="MDeclaredClass65", type=jsm_MConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructors", type=jsm_MDeclaredClass, multiplicity=Multiplicity(1, 1))
    }
)
parameters66: BinaryAssociation = BinaryAssociation(
    name="parameters66",
    ends={
        Property(name="MConstructorParameter", type=jsm_MConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructor", type=jsm_MConstructorParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodImplementation61: BinaryAssociation = BinaryAssociation(
    name="methodImplementation61",
    ends={
        Property(name="AbstractMMethodImplementation63", type=jsm_MMethodImplementationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters62", type=jsm_AbstractMMethodImplementation, multiplicity=Multiplicity(1, 1))
    }
)
statements70: BinaryAssociation = BinaryAssociation(
    name="statements70",
    ends={
        Property(name="jsm_AbstractCStatement71", type=jsm_CBlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CBlockStatement", type=jsm_AbstractCStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value72: BinaryAssociation = BinaryAssociation(
    name="value72",
    ends={
        Property(name="jsm_AbstractCExpression73", type=jsm_CDeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CDeclarationStatement", type=jsm_AbstractCExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="jsm_AbstractCExpression75", type=jsm_CExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CExpressionStatement", type=jsm_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition76: BinaryAssociation = BinaryAssociation(
    name="condition76",
    ends={
        Property(name="jsm_AbstractCExpression77", type=jsm_CIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CIfStatement", type=jsm_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueStatement78: BinaryAssociation = BinaryAssociation(
    name="trueStatement78",
    ends={
        Property(name="jsm_AbstractCStatement80", type=jsm_CIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CIfStatement79", type=jsm_AbstractCStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseStatement81: BinaryAssociation = BinaryAssociation(
    name="falseStatement81",
    ends={
        Property(name="jsm_AbstractCStatement83", type=jsm_CIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CIfStatement82", type=jsm_AbstractCStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructor67: BinaryAssociation = BinaryAssociation(
    name="constructor67",
    ends={
        Property(name="MConstructor69", type=jsm_MConstructorParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters68", type=jsm_MConstructor, multiplicity=Multiplicity(1, 1))
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="jsm_AbstractCExpression85", type=jsm_CConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CConditionalExpression", type=jsm_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueExpression86: BinaryAssociation = BinaryAssociation(
    name="trueExpression86",
    ends={
        Property(name="jsm_AbstractCExpression88", type=jsm_CConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CConditionalExpression87", type=jsm_AbstractCExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseExpression89: BinaryAssociation = BinaryAssociation(
    name="falseExpression89",
    ends={
        Property(name="jsm_AbstractCExpression91", type=jsm_CConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="jsm_CConditionalExpression90", type=jsm_AbstractCExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_jsm_MRoot_AbstractMPackageContainer = Generalization(general=AbstractMPackageContainer, specific=jsm_MRoot)
gen_jsm_MPackage_AbstractMPackageContainer = Generalization(general=AbstractMPackageContainer, specific=jsm_MPackage)
gen_jsm_MResource_AbstractMResource = Generalization(general=AbstractMResource, specific=jsm_MResource)
gen_jsm_MCompilationUnit_AbstractMResource = Generalization(general=AbstractMResource, specific=jsm_MCompilationUnit)
gen_jsm_MCompilationUnit_AbstractMTypeContainer = Generalization(general=AbstractMTypeContainer, specific=jsm_MCompilationUnit)
gen_jsm_AbstractMDeclaredType_AbstractMTypeContainer = Generalization(general=AbstractMTypeContainer, specific=jsm_AbstractMDeclaredType)
gen_jsm_MDeclaredTypeReference_AbstractMTypeReference = Generalization(general=AbstractMTypeReference, specific=jsm_MDeclaredTypeReference)
gen_jsm_MExternalTypeReference_AbstractMTypeReference = Generalization(general=AbstractMTypeReference, specific=jsm_MExternalTypeReference)
gen_jsm_MPrimitiveTypeReference_AbstractMTypeReference = Generalization(general=AbstractMTypeReference, specific=jsm_MPrimitiveTypeReference)
gen_jsm_AbstractMMethodLike_AbstractModifiers = Generalization(general=AbstractModifiers, specific=jsm_AbstractMMethodLike)
gen_jsm_AbstractMClass_AbstractMType = Generalization(general=AbstractMType, specific=jsm_AbstractMClass)
gen_jsm_MDeclaredClass_AbstractMClass = Generalization(general=AbstractMClass, specific=jsm_MDeclaredClass)
gen_jsm_MDeclaredClass_AbstractMDeclaredType = Generalization(general=AbstractMDeclaredType, specific=jsm_MDeclaredClass)
gen_jsm_MAbstractDeclaredClass_MDeclaredClass = Generalization(general=MDeclaredClass, specific=jsm_MAbstractDeclaredClass)
gen_jsm_MExternalClass_AbstractMClass = Generalization(general=AbstractMClass, specific=jsm_MExternalClass)
gen_jsm_MExternalClass_AbstractMExternalType = Generalization(general=AbstractMExternalType, specific=jsm_MExternalClass)
gen_jsm_AbstractMInterface_AbstractMType = Generalization(general=AbstractMType, specific=jsm_AbstractMInterface)
gen_jsm_MDeclaredInterface_AbstractMInterface = Generalization(general=AbstractMInterface, specific=jsm_MDeclaredInterface)
gen_jsm_MDeclaredInterface_AbstractMDeclaredType = Generalization(general=AbstractMDeclaredType, specific=jsm_MDeclaredInterface)
gen_jsm_MExternalInterface_AbstractMInterface = Generalization(general=AbstractMInterface, specific=jsm_MExternalInterface)
gen_jsm_MExternalInterface_AbstractMExternalType = Generalization(general=AbstractMExternalType, specific=jsm_MExternalInterface)
gen_jsm_AbstractMClassFieldDeclaration_AbstractMFieldDeclaration = Generalization(general=AbstractMFieldDeclaration, specific=jsm_AbstractMClassFieldDeclaration)
gen_jsm_MStaticClassFieldDeclaration_AbstractMClassFieldDeclaration = Generalization(general=AbstractMClassFieldDeclaration, specific=jsm_MStaticClassFieldDeclaration)
gen_jsm_MInstanceClassFieldDeclaration_AbstractMClassFieldDeclaration = Generalization(general=AbstractMClassFieldDeclaration, specific=jsm_MInstanceClassFieldDeclaration)
gen_jsm_MConstantInterfaceFieldDeclaration_AbstractMFieldDeclaration = Generalization(general=AbstractMFieldDeclaration, specific=jsm_MConstantInterfaceFieldDeclaration)
gen_jsm_AbstractMMethodDeclaration_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=jsm_AbstractMMethodDeclaration)
gen_jsm_AbstractMFieldDeclaration_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=jsm_AbstractMFieldDeclaration)
gen_jsm_MImplicitMethodDeclaration_AbstractMMethodDeclaration = Generalization(general=AbstractMMethodDeclaration, specific=jsm_MImplicitMethodDeclaration)
gen_jsm_AbstractMImplementableMethodDeclaration_AbstractMMethodDeclaration = Generalization(general=AbstractMMethodDeclaration, specific=jsm_AbstractMImplementableMethodDeclaration)
gen_jsm_MAbstractClassMethodDeclaration_AbstractMImplementableMethodDeclaration = Generalization(general=AbstractMImplementableMethodDeclaration, specific=jsm_MAbstractClassMethodDeclaration)
gen_jsm_MInterfaceMethodDeclaration_AbstractMImplementableMethodDeclaration = Generalization(general=AbstractMImplementableMethodDeclaration, specific=jsm_MInterfaceMethodDeclaration)
gen_jsm_MNativeMethodDeclaration_AbstractMMethodDeclaration = Generalization(general=AbstractMMethodDeclaration, specific=jsm_MNativeMethodDeclaration)
gen_jsm_MMethodDeclarationParameter_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=jsm_MMethodDeclarationParameter)
gen_jsm_MDeclaredMethodImplementation_AbstractMMethodImplementation = Generalization(general=AbstractMMethodImplementation, specific=jsm_MDeclaredMethodImplementation)
gen_jsm_MDirectMethodImplementation_AbstractMMethodImplementation = Generalization(general=AbstractMMethodImplementation, specific=jsm_MDirectMethodImplementation)
gen_jsm_AbstractMMethodImplementation_AbstractMMethodLike = Generalization(general=AbstractMMethodLike, specific=jsm_AbstractMMethodImplementation)
gen_jsm_MConstructor_AbstractMMethodLike = Generalization(general=AbstractMMethodLike, specific=jsm_MConstructor)
gen_jsm_MConstructorParameter_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=jsm_MConstructorParameter)
gen_jsm_CBlockStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=jsm_CBlockStatement)
gen_jsm_CDeclarationStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=jsm_CDeclarationStatement)
gen_jsm_CDeclarationStatement_AbstractMTypeWithNameDeclaration = Generalization(general=AbstractMTypeWithNameDeclaration, specific=jsm_CDeclarationStatement)
gen_jsm_CExpressionStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=jsm_CExpressionStatement)
gen_jsm_CIfStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=jsm_CIfStatement)
gen_jsm_CConditionalExpression_AbstractCExpression = Generalization(general=AbstractCExpression, specific=jsm_CConditionalExpression)
gen_jsm_CUnparsedExpression_AbstractCExpression = Generalization(general=AbstractCExpression, specific=jsm_CUnparsedExpression)
gen_jsm_CUnparsedStatement_AbstractCStatement = Generalization(general=AbstractCStatement, specific=jsm_CUnparsedStatement)

# Domain Model
domain_model = DomainModel(
    name="jsm",
    types={jsm_AbstractMPackageContainer, jsm_MPackage, jsm_MRoot, AbstractMPackageContainer, jsm_AbstractMExternalType, jsm_MResource, AbstractMResource, jsm_AbstractMTypeContainer, jsm_AbstractMDeclaredType, jsm_AbstractMResource, jsm_MCompilationUnit, AbstractMTypeContainer, jsm_AbstractMType, jsm_AbstractMTypeReference, jsm_MDeclaredTypeReference, AbstractMTypeReference, jsm_MExternalTypeReference, jsm_MPrimitiveTypeReference, jsm_AbstractModifiers, jsm_AbstractMMethodLike, AbstractModifiers, jsm_AbstractCStatement, jsm_AbstractMTypeWithNameDeclaration, jsm_AbstractMClass, AbstractMType, jsm_MDeclaredClass, AbstractMClass, AbstractMDeclaredType, jsm_AbstractMInterface, jsm_MStaticClassFieldDeclaration, jsm_MInstanceClassFieldDeclaration, jsm_MConstructor, jsm_AbstractMMethodImplementation, jsm_MAbstractDeclaredClass, MDeclaredClass, jsm_MAbstractClassMethodDeclaration, jsm_MExternalClass, AbstractMExternalType, jsm_MDeclaredInterface, AbstractMInterface, jsm_MConstantInterfaceFieldDeclaration, jsm_MInterfaceMethodDeclaration, jsm_MExternalInterface, jsm_MNativeMethodDeclaration, jsm_AbstractMClassFieldDeclaration, AbstractMFieldDeclaration, AbstractMClassFieldDeclaration, jsm_AbstractMMethodDeclaration, jsm_MMethodDeclarationParameter, jsm_AbstractMFieldDeclaration, AbstractMTypeWithNameDeclaration, jsm_AbstractCExpression, jsm_MImplicitMethodDeclaration, AbstractMMethodDeclaration, jsm_MDirectMethodImplementation, jsm_AbstractMImplementableMethodDeclaration, jsm_MDeclaredMethodImplementation, AbstractMImplementableMethodDeclaration, jsm_MMethodImplementationParameter, AbstractMMethodImplementation, AbstractMMethodLike, jsm_MConstructorParameter, jsm_CBlockStatement, AbstractCStatement, jsm_CDeclarationStatement, jsm_CExpressionStatement, jsm_CIfStatement, jsm_CConditionalExpression, AbstractCExpression, jsm_CUnparsedExpression, jsm_CUnparsedStatement, MPrimitiveTypes, MVisibility},
    associations={packages0, externalTypes1, packageContainer2, resources3, package4, derivedFrom7, superOf10, imports13, typeContainer14, root15, types12, type17, statement18, type19, type16, extends20, implements21, staticFields23, instanceFields24, constructors26, implementedMethods28, nativeMethods30, abstractMethods32, extends34, constants36, methods38, owner41, owner42, owner44, parameters45, initialValue40, methodDeclaration46, owner47, implementations48, owner50, owner51, owner53, owner55, parameters57, declaration58, declaration59, owner64, parameters66, methodImplementation61, statements70, value72, expression74, condition76, trueStatement78, falseStatement81, constructor67, condition84, trueExpression86, falseExpression89},
    generalizations={gen_jsm_MRoot_AbstractMPackageContainer, gen_jsm_MPackage_AbstractMPackageContainer, gen_jsm_MResource_AbstractMResource, gen_jsm_MCompilationUnit_AbstractMResource, gen_jsm_MCompilationUnit_AbstractMTypeContainer, gen_jsm_AbstractMDeclaredType_AbstractMTypeContainer, gen_jsm_MDeclaredTypeReference_AbstractMTypeReference, gen_jsm_MExternalTypeReference_AbstractMTypeReference, gen_jsm_MPrimitiveTypeReference_AbstractMTypeReference, gen_jsm_AbstractMMethodLike_AbstractModifiers, gen_jsm_AbstractMClass_AbstractMType, gen_jsm_MDeclaredClass_AbstractMClass, gen_jsm_MDeclaredClass_AbstractMDeclaredType, gen_jsm_MAbstractDeclaredClass_MDeclaredClass, gen_jsm_MExternalClass_AbstractMClass, gen_jsm_MExternalClass_AbstractMExternalType, gen_jsm_AbstractMInterface_AbstractMType, gen_jsm_MDeclaredInterface_AbstractMInterface, gen_jsm_MDeclaredInterface_AbstractMDeclaredType, gen_jsm_MExternalInterface_AbstractMInterface, gen_jsm_MExternalInterface_AbstractMExternalType, gen_jsm_AbstractMClassFieldDeclaration_AbstractMFieldDeclaration, gen_jsm_MStaticClassFieldDeclaration_AbstractMClassFieldDeclaration, gen_jsm_MInstanceClassFieldDeclaration_AbstractMClassFieldDeclaration, gen_jsm_MConstantInterfaceFieldDeclaration_AbstractMFieldDeclaration, gen_jsm_AbstractMMethodDeclaration_AbstractMTypeWithNameDeclaration, gen_jsm_AbstractMFieldDeclaration_AbstractMTypeWithNameDeclaration, gen_jsm_MImplicitMethodDeclaration_AbstractMMethodDeclaration, gen_jsm_AbstractMImplementableMethodDeclaration_AbstractMMethodDeclaration, gen_jsm_MAbstractClassMethodDeclaration_AbstractMImplementableMethodDeclaration, gen_jsm_MInterfaceMethodDeclaration_AbstractMImplementableMethodDeclaration, gen_jsm_MNativeMethodDeclaration_AbstractMMethodDeclaration, gen_jsm_MMethodDeclarationParameter_AbstractMTypeWithNameDeclaration, gen_jsm_MDeclaredMethodImplementation_AbstractMMethodImplementation, gen_jsm_MDirectMethodImplementation_AbstractMMethodImplementation, gen_jsm_AbstractMMethodImplementation_AbstractMMethodLike, gen_jsm_MConstructor_AbstractMMethodLike, gen_jsm_MConstructorParameter_AbstractMTypeWithNameDeclaration, gen_jsm_CBlockStatement_AbstractCStatement, gen_jsm_CDeclarationStatement_AbstractCStatement, gen_jsm_CDeclarationStatement_AbstractMTypeWithNameDeclaration, gen_jsm_CExpressionStatement_AbstractCStatement, gen_jsm_CIfStatement_AbstractCStatement, gen_jsm_CConditionalExpression_AbstractCExpression, gen_jsm_CUnparsedExpression_AbstractCExpression, gen_jsm_CUnparsedStatement_AbstractCStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)