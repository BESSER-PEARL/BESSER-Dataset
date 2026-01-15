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
Modifiers: Enumeration = Enumeration(
    name="Modifiers",
    literals={
            EnumerationLiteral(name="bridge"),
			EnumerationLiteral(name="default"),
			EnumerationLiteral(name="deprecated"),
			EnumerationLiteral(name="enum"),
			EnumerationLiteral(name="final"),
			EnumerationLiteral(name="interface"),
			EnumerationLiteral(name="native"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="static"),
			EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="annotation"),
			EnumerationLiteral(name="strictfp"),
			EnumerationLiteral(name="super"),
			EnumerationLiteral(name="synchronized"),
			EnumerationLiteral(name="synthetic"),
			EnumerationLiteral(name="transient"),
			EnumerationLiteral(name="varargs"),
			EnumerationLiteral(name="volatile")
    }
)

# Classes
Core_IJavaProject = Class(name="Core::IJavaProject")
Core_IPackageFragmentRoot = Class(name="Core::IPackageFragmentRoot", is_abstract=True)
IJavaElement = Class(name="IJavaElement")
Core_IJavaElement = Class(name="Core::IJavaElement", is_abstract=True)
Core_PhysicalElement = Class(name="Core::PhysicalElement", is_abstract=True)
Core_IJavaModel = Class(name="Core::IJavaModel")
PhysicalElement = Class(name="PhysicalElement")
Core_IClassFile = Class(name="Core::IClassFile")
Core_IPackageFragment = Class(name="Core::IPackageFragment")
Core_BinaryPackageFragmentRoot = Class(name="Core::BinaryPackageFragmentRoot")
IPackageFragmentRoot = Class(name="IPackageFragmentRoot")
Core_SourcePackageFragmentRoot = Class(name="Core::SourcePackageFragmentRoot")
Core_CompilationUnit = Class(name="Core::CompilationUnit")
Core_ICompilationUnit = Class(name="Core::ICompilationUnit")
Core_ITypeRoot = Class(name="Core::ITypeRoot", is_abstract=True)
ISourceReference = Class(name="ISourceReference")
ITypeRoot = Class(name="ITypeRoot")
Core_IType = Class(name="Core::IType")
Core_IImportDeclaration = Class(name="Core::IImportDeclaration")
IMember = Class(name="IMember")
Core_ISourceReference = Class(name="Core::ISourceReference", is_abstract=True)
Core_ISourceRange = Class(name="Core::ISourceRange")
Core_IMember = Class(name="Core::IMember", is_abstract=True)
Core_IInitializer = Class(name="Core::IInitializer")
Core_IField = Class(name="Core::IField")
Core_IMethod = Class(name="Core::IMethod")
Core_ITypeParameter = Class(name="Core::ITypeParameter")
Core_Parameter = Class(name="Core::Parameter")

# Core_IJavaProject class attributes and methods

# Core_IPackageFragmentRoot class attributes and methods

# IJavaElement class attributes and methods

# Core_IJavaElement class attributes and methods
Core_IJavaElement_elementName: Property = Property(name="elementName", type=StringType)
Core_IJavaElement.attributes={Core_IJavaElement_elementName}

# Core_PhysicalElement class attributes and methods
Core_PhysicalElement_path: Property = Property(name="path", type=StringType)
Core_PhysicalElement_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
Core_PhysicalElement.attributes={Core_PhysicalElement_path, Core_PhysicalElement_isReadOnly}

# Core_IJavaModel class attributes and methods

# PhysicalElement class attributes and methods

# Core_IClassFile class attributes and methods
Core_IClassFile_isClass: Property = Property(name="isClass", type=StringType)
Core_IClassFile_isInterface: Property = Property(name="isInterface", type=StringType)
Core_IClassFile.attributes={Core_IClassFile_isClass, Core_IClassFile_isInterface}

# Core_IPackageFragment class attributes and methods
Core_IPackageFragment_isDefaultPackage: Property = Property(name="isDefaultPackage", type=StringType)
Core_IPackageFragment.attributes={Core_IPackageFragment_isDefaultPackage}

# Core_BinaryPackageFragmentRoot class attributes and methods

# IPackageFragmentRoot class attributes and methods

# Core_SourcePackageFragmentRoot class attributes and methods

# Core_CompilationUnit class attributes and methods

# Core_ICompilationUnit class attributes and methods

# Core_ITypeRoot class attributes and methods

# ISourceReference class attributes and methods

# ITypeRoot class attributes and methods

# Core_IType class attributes and methods
Core_IType_fullyQualifiedName: Property = Property(name="fullyQualifiedName", type=StringType)
Core_IType_fullyQualifiedParametrizedName: Property = Property(name="fullyQualifiedParametrizedName", type=StringType)
Core_IType.attributes={Core_IType_fullyQualifiedParametrizedName, Core_IType_fullyQualifiedName}

# Core_IImportDeclaration class attributes and methods
Core_IImportDeclaration_isOnDemand: Property = Property(name="isOnDemand", type=StringType)
Core_IImportDeclaration_isStatic: Property = Property(name="isStatic", type=StringType)
Core_IImportDeclaration.attributes={Core_IImportDeclaration_isOnDemand, Core_IImportDeclaration_isStatic}

# IMember class attributes and methods

# Core_ISourceReference class attributes and methods
Core_ISourceReference_source: Property = Property(name="source", type=StringType)
Core_ISourceReference.attributes={Core_ISourceReference_source}

# Core_ISourceRange class attributes and methods
Core_ISourceRange_length: Property = Property(name="length", type=StringType)
Core_ISourceRange_offset: Property = Property(name="offset", type=StringType)
Core_ISourceRange.attributes={Core_ISourceRange_length, Core_ISourceRange_offset}

# Core_IMember class attributes and methods

# Core_IInitializer class attributes and methods

# Core_IField class attributes and methods
Core_IField_constant: Property = Property(name="constant", type=StringType)
Core_IField_isEnumConstant: Property = Property(name="isEnumConstant", type=StringType)
Core_IField_typeSignature: Property = Property(name="typeSignature", type=StringType)
Core_IField_isVolatile: Property = Property(name="isVolatile", type=StringType)
Core_IField_isTransient: Property = Property(name="isTransient", type=StringType)
Core_IField.attributes={Core_IField_constant, Core_IField_isEnumConstant, Core_IField_isVolatile, Core_IField_typeSignature, Core_IField_isTransient}

# Core_IMethod class attributes and methods
Core_IMethod_returnType: Property = Property(name="returnType", type=StringType)
Core_IMethod_isConstructor: Property = Property(name="isConstructor", type=StringType)
Core_IMethod_isMainMethod: Property = Property(name="isMainMethod", type=StringType)
Core_IMethod_exceptionTypes: Property = Property(name="exceptionTypes", type=StringType)
Core_IMethod.attributes={Core_IMethod_exceptionTypes, Core_IMethod_isMainMethod, Core_IMethod_returnType, Core_IMethod_isConstructor}

# Core_ITypeParameter class attributes and methods
Core_ITypeParameter_bounds: Property = Property(name="bounds", type=StringType)
Core_ITypeParameter.attributes={Core_ITypeParameter_bounds}

# Core_Parameter class attributes and methods
Core_Parameter_name: Property = Property(name="name", type=StringType)
Core_Parameter_type: Property = Property(name="type", type=StringType)
Core_Parameter.attributes={Core_Parameter_type, Core_Parameter_name}

# Relationships
javaProjects0: BinaryAssociation = BinaryAssociation(
    name="javaProjects0",
    ends={
        Property(name="Core_IJavaProject", type=Core_IJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaModel", type=Core_IJavaProject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackageFragmentRoots1: BinaryAssociation = BinaryAssociation(
    name="externalPackageFragmentRoots1",
    ends={
        Property(name="Core_IPackageFragmentRoot", type=Core_IJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaModel2", type=Core_IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageFragmentRoot13: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoot13",
    ends={
        Property(name="IPackageFragmentRoot", type=Core_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragments", type=Core_IPackageFragmentRoot, multiplicity=Multiplicity(1, 1))
    }
)
classFiles14: BinaryAssociation = BinaryAssociation(
    name="classFiles14",
    ends={
        Property(name="Core_IClassFile", type=Core_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IPackageFragment", type=Core_IClassFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageFragmentRoots3: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoots3",
    ends={
        Property(name="Core_IPackageFragmentRoot5", type=Core_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaProject4", type=Core_IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalPackageFragmentRoots6: BinaryAssociation = BinaryAssociation(
    name="externalPackageFragmentRoots6",
    ends={
        Property(name="Core_IPackageFragmentRoot8", type=Core_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaProject7", type=Core_IPackageFragmentRoot, multiplicity=Multiplicity(0, 9999))
    }
)
requiredProjects10: BinaryAssociation = BinaryAssociation(
    name="requiredProjects10",
    ends={
        Property(name="Core_IJavaProject11", type=Core_IJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IJavaProject9", type=Core_IJavaProject, multiplicity=Multiplicity(0, 9999))
    }
)
packageFragments12: BinaryAssociation = BinaryAssociation(
    name="packageFragments12",
    ends={
        Property(name="IPackageFragment", type=Core_IPackageFragmentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragmentRoot", type=Core_IPackageFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ast27: BinaryAssociation = BinaryAssociation(
    name="ast27",
    ends={
        Property(name="Core_CompilationUnit", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit28", type=Core_CompilationUnit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="Core_IType31", type=Core_IClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IClassFile30", type=Core_IType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compilationUnits15: BinaryAssociation = BinaryAssociation(
    name="compilationUnits15",
    ends={
        Property(name="Core_ICompilationUnit", type=Core_IPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IPackageFragment16", type=Core_ICompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allType17: BinaryAssociation = BinaryAssociation(
    name="allType17",
    ends={
        Property(name="Core_IType", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit18", type=Core_IType, multiplicity=Multiplicity(0, 9999))
    }
)
imports19: BinaryAssociation = BinaryAssociation(
    name="imports19",
    ends={
        Property(name="Core_IImportDeclaration", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit20", type=Core_IImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types21: BinaryAssociation = BinaryAssociation(
    name="types21",
    ends={
        Property(name="Core_IType23", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit22", type=Core_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primary25: BinaryAssociation = BinaryAssociation(
    name="primary25",
    ends={
        Property(name="Core_ICompilationUnit26", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ICompilationUnit24", type=Core_ICompilationUnit, multiplicity=Multiplicity(1, 1))
    }
)
javadocRange33: BinaryAssociation = BinaryAssociation(
    name="javadocRange33",
    ends={
        Property(name="Core_ISourceRange34", type=Core_IMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IMember", type=Core_ISourceRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameRange35: BinaryAssociation = BinaryAssociation(
    name="nameRange35",
    ends={
        Property(name="Core_ISourceRange37", type=Core_IMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IMember36", type=Core_ISourceRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceRange32: BinaryAssociation = BinaryAssociation(
    name="sourceRange32",
    ends={
        Property(name="Core_ISourceRange", type=Core_ISourceReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_ISourceReference", type=Core_ISourceRange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializers38: BinaryAssociation = BinaryAssociation(
    name="initializers38",
    ends={
        Property(name="Core_IInitializer", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType39", type=Core_IInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields40: BinaryAssociation = BinaryAssociation(
    name="fields40",
    ends={
        Property(name="Core_IField", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType41", type=Core_IField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods42: BinaryAssociation = BinaryAssociation(
    name="methods42",
    ends={
        Property(name="Core_IMethod", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType43", type=Core_IMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types45: BinaryAssociation = BinaryAssociation(
    name="types45",
    ends={
        Property(name="Core_IType46", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType44", type=Core_IType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters47: BinaryAssociation = BinaryAssociation(
    name="typeParameters47",
    ends={
        Property(name="Core_ITypeParameter", type=Core_IType, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IType48", type=Core_ITypeParameter, multiplicity=Multiplicity(0, 9999))
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="Core_Parameter", type=Core_IMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_IMethod50", type=Core_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Core_IJavaProject_IJavaElement = Generalization(general=IJavaElement, specific=Core_IJavaProject)
gen_Core_IJavaProject_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IJavaProject)
gen_Core_IJavaModel_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IJavaModel)
gen_Core_IPackageFragment_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IPackageFragment)
gen_Core_IPackageFragmentRoot_IJavaElement = Generalization(general=IJavaElement, specific=Core_IPackageFragmentRoot)
gen_Core_IPackageFragmentRoot_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_IPackageFragmentRoot)
gen_Core_BinaryPackageFragmentRoot_IPackageFragmentRoot = Generalization(general=IPackageFragmentRoot, specific=Core_BinaryPackageFragmentRoot)
gen_Core_SourcePackageFragmentRoot_IPackageFragmentRoot = Generalization(general=IPackageFragmentRoot, specific=Core_SourcePackageFragmentRoot)
gen_Core_IPackageFragment_IJavaElement = Generalization(general=IJavaElement, specific=Core_IPackageFragment)
gen_Core_IClassFile_ITypeRoot = Generalization(general=ITypeRoot, specific=Core_IClassFile)
gen_Core_ITypeRoot_IJavaElement = Generalization(general=IJavaElement, specific=Core_ITypeRoot)
gen_Core_ITypeRoot_ISourceReference = Generalization(general=ISourceReference, specific=Core_ITypeRoot)
gen_Core_ITypeRoot_PhysicalElement = Generalization(general=PhysicalElement, specific=Core_ITypeRoot)
gen_Core_ICompilationUnit_ITypeRoot = Generalization(general=ITypeRoot, specific=Core_ICompilationUnit)
gen_Core_IType_IMember = Generalization(general=IMember, specific=Core_IType)
gen_Core_IImportDeclaration_IJavaElement = Generalization(general=IJavaElement, specific=Core_IImportDeclaration)
gen_Core_IImportDeclaration_ISourceReference = Generalization(general=ISourceReference, specific=Core_IImportDeclaration)
gen_Core_IMember_IJavaElement = Generalization(general=IJavaElement, specific=Core_IMember)
gen_Core_IMember_ISourceReference = Generalization(general=ISourceReference, specific=Core_IMember)
gen_Core_IInitializer_IMember = Generalization(general=IMember, specific=Core_IInitializer)
gen_Core_IField_IMember = Generalization(general=IMember, specific=Core_IField)
gen_Core_ITypeParameter_IJavaElement = Generalization(general=IJavaElement, specific=Core_ITypeParameter)
gen_Core_ITypeParameter_ISourceReference = Generalization(general=ISourceReference, specific=Core_ITypeParameter)
gen_Core_IMethod_IMember = Generalization(general=IMember, specific=Core_IMethod)

# Domain Model
domain_model = DomainModel(
    name="Core",
    types={Core_IJavaProject, Core_IPackageFragmentRoot, IJavaElement, Core_IJavaElement, Core_PhysicalElement, Core_IJavaModel, PhysicalElement, Core_IClassFile, Core_IPackageFragment, Core_BinaryPackageFragmentRoot, IPackageFragmentRoot, Core_SourcePackageFragmentRoot, Core_CompilationUnit, Core_ICompilationUnit, Core_ITypeRoot, ISourceReference, ITypeRoot, Core_IType, Core_IImportDeclaration, IMember, Core_ISourceReference, Core_ISourceRange, Core_IMember, Core_IInitializer, Core_IField, Core_IMethod, Core_ITypeParameter, Core_Parameter, Modifiers},
    associations={javaProjects0, externalPackageFragmentRoots1, packageFragmentRoot13, classFiles14, packageFragmentRoots3, externalPackageFragmentRoots6, requiredProjects10, packageFragments12, ast27, type29, compilationUnits15, allType17, imports19, types21, primary25, javadocRange33, nameRange35, sourceRange32, initializers38, fields40, methods42, types45, typeParameters47, parameters49},
    generalizations={gen_Core_IJavaProject_IJavaElement, gen_Core_IJavaProject_PhysicalElement, gen_Core_IJavaModel_PhysicalElement, gen_Core_IPackageFragment_PhysicalElement, gen_Core_IPackageFragmentRoot_IJavaElement, gen_Core_IPackageFragmentRoot_PhysicalElement, gen_Core_BinaryPackageFragmentRoot_IPackageFragmentRoot, gen_Core_SourcePackageFragmentRoot_IPackageFragmentRoot, gen_Core_IPackageFragment_IJavaElement, gen_Core_IClassFile_ITypeRoot, gen_Core_ITypeRoot_IJavaElement, gen_Core_ITypeRoot_ISourceReference, gen_Core_ITypeRoot_PhysicalElement, gen_Core_ICompilationUnit_ITypeRoot, gen_Core_IType_IMember, gen_Core_IImportDeclaration_IJavaElement, gen_Core_IImportDeclaration_ISourceReference, gen_Core_IMember_IJavaElement, gen_Core_IMember_ISourceReference, gen_Core_IInitializer_IMember, gen_Core_IField_IMember, gen_Core_ITypeParameter_IJavaElement, gen_Core_ITypeParameter_ISourceReference, gen_Core_IMethod_IMember},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)