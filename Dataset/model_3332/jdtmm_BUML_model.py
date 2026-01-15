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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private")
    }
)

TrueFalseDefault: Enumeration = Enumeration(
    name="TrueFalseDefault",
    literals={
            EnumerationLiteral(name="true"),
			EnumerationLiteral(name="false"),
			EnumerationLiteral(name="default")
    }
)

# Classes
jdtmm_JDTParameter = Class(name="jdtmm::JDTParameter")
jdtmm_JDTMethodBody = Class(name="jdtmm::JDTMethodBody", is_abstract=True)
jdtmm_JDTMethod = Class(name="jdtmm::JDTMethod")
JDTMember = Class(name="JDTMember")
jdtmm_JDTType = Class(name="jdtmm::JDTType", is_abstract=True)
jdtmm_JDTParentJavaElement = Class(name="jdtmm::JDTParentJavaElement", is_abstract=True)
JDTJavaElement = Class(name="JDTJavaElement")
JDTParent = Class(name="JDTParent")
jdtmm_JDTParent = Class(name="jdtmm::JDTParent", is_abstract=True)
jdtmm_JDTMember = Class(name="jdtmm::JDTMember", is_abstract=True)
JDTParentJavaElement = Class(name="JDTParentJavaElement")
jdtmm_JDTTypeParameter = Class(name="jdtmm::JDTTypeParameter")
jdtmm_JDTJavaElement = Class(name="jdtmm::JDTJavaElement", is_abstract=True)
jdtmm_JDTCompilationUnit = Class(name="jdtmm::JDTCompilationUnit")
jdtmm_JDTField = Class(name="jdtmm::JDTField")
jdtmm_JDTPackageFragment = Class(name="jdtmm::JDTPackageFragment")
jdtmm_JDTTypeRoot = Class(name="jdtmm::JDTTypeRoot", is_abstract=True)
JDTTypeRoot = Class(name="JDTTypeRoot")
jdtmm_JDTPackageFragmentRoot = Class(name="jdtmm::JDTPackageFragmentRoot")
jdtmm_JDTJavaProject = Class(name="jdtmm::JDTJavaProject")
jdtmm_JDTJavaModel = Class(name="jdtmm::JDTJavaModel")
jdtmm_JDTImportContainer = Class(name="jdtmm::JDTImportContainer")
jdtmm_JDTException = Class(name="jdtmm::JDTException")
jdtmm_JDTOpaqueBody = Class(name="jdtmm::JDTOpaqueBody")
JDTMethodBody = Class(name="JDTMethodBody")
jdtmm_JDTClass = Class(name="jdtmm::JDTClass")
JDTType = Class(name="JDTType")
jdtmm_JDTInterface = Class(name="jdtmm::JDTInterface")
jdtmm_JDTEnum = Class(name="jdtmm::JDTEnum")
jdtmm_JDTImportDeclaration = Class(name="jdtmm::JDTImportDeclaration")

# jdtmm_JDTParameter class attributes and methods
jdtmm_JDTParameter_final: Property = Property(name="final", type=StringType)
jdtmm_JDTParameter_isMultiValued: Property = Property(name="isMultiValued", type=StringType)
jdtmm_JDTParameter.attributes={jdtmm_JDTParameter_isMultiValued, jdtmm_JDTParameter_final}

# jdtmm_JDTMethodBody class attributes and methods
jdtmm_JDTMethodBody_m_asText: Method = Method(name="asText", parameters={}, type=StringType)
jdtmm_JDTMethodBody.methods={jdtmm_JDTMethodBody_m_asText}

# jdtmm_JDTMethod class attributes and methods
jdtmm_JDTMethod_abstract: Property = Property(name="abstract", type=StringType)
jdtmm_JDTMethod_final: Property = Property(name="final", type=StringType)
jdtmm_JDTMethod_static: Property = Property(name="static", type=StringType)
jdtmm_JDTMethod_synchronized: Property = Property(name="synchronized", type=StringType)
jdtmm_JDTMethod_constructor: Property = Property(name="constructor", type=StringType)
jdtmm_JDTMethod.attributes={jdtmm_JDTMethod_constructor, jdtmm_JDTMethod_final, jdtmm_JDTMethod_static, jdtmm_JDTMethod_abstract, jdtmm_JDTMethod_synchronized}

# JDTMember class attributes and methods

# jdtmm_JDTType class attributes and methods
jdtmm_JDTType_class: Property = Property(name="class", type=StringType)
jdtmm_JDTType_interface: Property = Property(name="interface", type=StringType)
jdtmm_JDTType_enum: Property = Property(name="enum", type=StringType)
jdtmm_JDTType_abstract: Property = Property(name="abstract", type=StringType)
jdtmm_JDTType_final: Property = Property(name="final", type=StringType)
jdtmm_JDTType_static: Property = Property(name="static", type=StringType)
jdtmm_JDTType_superInterfaceNames: Property = Property(name="superInterfaceNames", type=StringType)
jdtmm_JDTType_superClassName: Property = Property(name="superClassName", type=StringType)
jdtmm_JDTType.attributes={jdtmm_JDTType_interface, jdtmm_JDTType_superInterfaceNames, jdtmm_JDTType_abstract, jdtmm_JDTType_class, jdtmm_JDTType_superClassName, jdtmm_JDTType_static, jdtmm_JDTType_enum, jdtmm_JDTType_final}

# jdtmm_JDTParentJavaElement class attributes and methods

# JDTJavaElement class attributes and methods

# JDTParent class attributes and methods

# jdtmm_JDTParent class attributes and methods
jdtmm_JDTParent_flags: Property = Property(name="flags", type=StringType)
jdtmm_JDTParent_m_setFlag: Method = Method(name="setFlag", parameters={Parameter(name='value'), Parameter(name='flag')})
jdtmm_JDTParent_m_isFlagSet: Method = Method(name="isFlagSet", parameters={Parameter(name='flag')}, type=StringType)
jdtmm_JDTParent.attributes={jdtmm_JDTParent_flags}
jdtmm_JDTParent.methods={jdtmm_JDTParent_m_setFlag, jdtmm_JDTParent_m_isFlagSet}

# jdtmm_JDTMember class attributes and methods
jdtmm_JDTMember_visibility: Property = Property(name="visibility", type=StringType)
jdtmm_JDTMember_explicitPlainTextRequiredImports: Property = Property(name="explicitPlainTextRequiredImports", type=StringType)
jdtmm_JDTMember.attributes={jdtmm_JDTMember_explicitPlainTextRequiredImports, jdtmm_JDTMember_visibility}

# JDTParentJavaElement class attributes and methods

# jdtmm_JDTTypeParameter class attributes and methods

# jdtmm_JDTJavaElement class attributes and methods
jdtmm_JDTJavaElement_elementType: Property = Property(name="elementType", type=StringType)
jdtmm_JDTJavaElement_comment: Property = Property(name="comment", type=StringType)
jdtmm_JDTJavaElement_generated: Property = Property(name="generated", type=StringType)
jdtmm_JDTJavaElement_elementName: Property = Property(name="elementName", type=StringType)
jdtmm_JDTJavaElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
jdtmm_JDTJavaElement_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
jdtmm_JDTJavaElement_m_getJDTSignature: Method = Method(name="getJDTSignature", parameters={}, type=StringType)
jdtmm_JDTJavaElement.attributes={jdtmm_JDTJavaElement_elementName, jdtmm_JDTJavaElement_elementType, jdtmm_JDTJavaElement_comment, jdtmm_JDTJavaElement_generated}
jdtmm_JDTJavaElement.methods={jdtmm_JDTJavaElement_m_accept, jdtmm_JDTJavaElement_m_getJDTSignature, jdtmm_JDTJavaElement_m_getQualifiedName}

# jdtmm_JDTCompilationUnit class attributes and methods

# jdtmm_JDTField class attributes and methods
jdtmm_JDTField_abstract: Property = Property(name="abstract", type=StringType)
jdtmm_JDTField_final: Property = Property(name="final", type=StringType)
jdtmm_JDTField_static: Property = Property(name="static", type=StringType)
jdtmm_JDTField_isMultiValued: Property = Property(name="isMultiValued", type=StringType)
jdtmm_JDTField_value: Property = Property(name="value", type=StringType)
jdtmm_JDTField_generateGetter: Property = Property(name="generateGetter", type=StringType)
jdtmm_JDTField_generateSetter: Property = Property(name="generateSetter", type=StringType)
jdtmm_JDTField.attributes={jdtmm_JDTField_value, jdtmm_JDTField_isMultiValued, jdtmm_JDTField_static, jdtmm_JDTField_abstract, jdtmm_JDTField_generateSetter, jdtmm_JDTField_final, jdtmm_JDTField_generateGetter}

# jdtmm_JDTPackageFragment class attributes and methods

# jdtmm_JDTTypeRoot class attributes and methods

# JDTTypeRoot class attributes and methods

# jdtmm_JDTPackageFragmentRoot class attributes and methods

# jdtmm_JDTJavaProject class attributes and methods

# jdtmm_JDTJavaModel class attributes and methods

# jdtmm_JDTImportContainer class attributes and methods

# jdtmm_JDTException class attributes and methods

# jdtmm_JDTOpaqueBody class attributes and methods
jdtmm_JDTOpaqueBody__body: Property = Property(name="_body", type=StringType)
jdtmm_JDTOpaqueBody.attributes={jdtmm_JDTOpaqueBody__body}

# JDTMethodBody class attributes and methods

# jdtmm_JDTClass class attributes and methods

# JDTType class attributes and methods

# jdtmm_JDTInterface class attributes and methods

# jdtmm_JDTEnum class attributes and methods

# jdtmm_JDTImportDeclaration class attributes and methods

# Relationships
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="JDTType", type=jdtmm_JDTMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1))
    }
)
returnType2: BinaryAssociation = BinaryAssociation(
    name="returnType2",
    ends={
        Property(name="JDTParameter", type=jdtmm_JDTMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="returnOwner", type=jdtmm_JDTParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="JDTParameter4", type=jdtmm_JDTMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterOwner", type=jdtmm_JDTParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="JDTMethod", type=jdtmm_JDTMethodBody, multiplicity=Multiplicity(1, 1)),
        Property(name="bodies", type=jdtmm_JDTMethod, multiplicity=Multiplicity(1, 1))
    }
)
explicitRequiredImports8: BinaryAssociation = BinaryAssociation(
    name="explicitRequiredImports8",
    ends={
        Property(name="jdtmm_JDTType9", type=jdtmm_JDTMember, multiplicity=Multiplicity(1, 1)),
        Property(name="jdtmm_JDTMember", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 9999))
    }
)
exceptions5: BinaryAssociation = BinaryAssociation(
    name="exceptions5",
    ends={
        Property(name="jdtmm_JDTType", type=jdtmm_JDTMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="jdtmm_JDTMethod", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 9999))
    }
)
bodies6: BinaryAssociation = BinaryAssociation(
    name="bodies6",
    ends={
        Property(name="JDTMethodBody", type=jdtmm_JDTMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=jdtmm_JDTMethodBody, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters7: BinaryAssociation = BinaryAssociation(
    name="typeParameters7",
    ends={
        Property(name="JDTTypeParameter", type=jdtmm_JDTMember, multiplicity=Multiplicity(1, 1)),
        Property(name="declaringMember", type=jdtmm_JDTTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent11: BinaryAssociation = BinaryAssociation(
    name="parent11",
    ends={
        Property(name="JDTParent", type=jdtmm_JDTJavaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=jdtmm_JDTParent, multiplicity=Multiplicity(0, 1))
    }
)
declaringMember12: BinaryAssociation = BinaryAssociation(
    name="declaringMember12",
    ends={
        Property(name="JDTMember", type=jdtmm_JDTTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="typeParameters", type=jdtmm_JDTMember, multiplicity=Multiplicity(0, 1))
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="JDTJavaElement", type=jdtmm_JDTParent, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=jdtmm_JDTJavaElement, multiplicity=Multiplicity(0, 9999))
    }
)
compilationUnit18: BinaryAssociation = BinaryAssociation(
    name="compilationUnit18",
    ends={
        Property(name="JDTCompilationUnit", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="types", type=jdtmm_JDTCompilationUnit, multiplicity=Multiplicity(0, 1))
    }
)
methods13: BinaryAssociation = BinaryAssociation(
    name="methods13",
    ends={
        Property(name="JDTMethod15", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="owner14", type=jdtmm_JDTMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields16: BinaryAssociation = BinaryAssociation(
    name="fields16",
    ends={
        Property(name="JDTField", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="owner17", type=jdtmm_JDTField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="jdtmm_JDTType34", type=jdtmm_JDTField, multiplicity=Multiplicity(1, 1)),
        Property(name="jdtmm_JDTField", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 1))
    }
)
types20: BinaryAssociation = BinaryAssociation(
    name="types20",
    ends={
        Property(name="JDTType22", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner24: BinaryAssociation = BinaryAssociation(
    name="owner24",
    ends={
        Property(name="JDTType26", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="types25", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 1))
    }
)
superInterfaces28: BinaryAssociation = BinaryAssociation(
    name="superInterfaces28",
    ends={
        Property(name="jdtmm_JDTType29", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="jdtmm_JDTType27", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 9999))
    }
)
superClass31: BinaryAssociation = BinaryAssociation(
    name="superClass31",
    ends={
        Property(name="jdtmm_JDTType32", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1)),
        Property(name="jdtmm_JDTType30", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 1))
    }
)
packageFragment37: BinaryAssociation = BinaryAssociation(
    name="packageFragment37",
    ends={
        Property(name="JDTPackageFragment", type=jdtmm_JDTCompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="compilationUnits", type=jdtmm_JDTPackageFragment, multiplicity=Multiplicity(0, 1))
    }
)
types38: BinaryAssociation = BinaryAssociation(
    name="types38",
    ends={
        Property(name="JDTType39", type=jdtmm_JDTCompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="compilationUnit", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner35: BinaryAssociation = BinaryAssociation(
    name="owner35",
    ends={
        Property(name="JDTType36", type=jdtmm_JDTField, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=jdtmm_JDTType, multiplicity=Multiplicity(1, 1))
    }
)
javaModel46: BinaryAssociation = BinaryAssociation(
    name="javaModel46",
    ends={
        Property(name="JDTJavaModel", type=jdtmm_JDTJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="javaProject", type=jdtmm_JDTJavaModel, multiplicity=Multiplicity(0, 1))
    }
)
packageFragmentRoots47: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoots47",
    ends={
        Property(name="JDTPackageFragmentRoot49", type=jdtmm_JDTJavaProject, multiplicity=Multiplicity(1, 1)),
        Property(name="javaProject48", type=jdtmm_JDTPackageFragmentRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javaProject50: BinaryAssociation = BinaryAssociation(
    name="javaProject50",
    ends={
        Property(name="JDTJavaProject51", type=jdtmm_JDTJavaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="javaModel", type=jdtmm_JDTJavaProject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterOwner52: BinaryAssociation = BinaryAssociation(
    name="parameterOwner52",
    ends={
        Property(name="JDTMethod53", type=jdtmm_JDTParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=jdtmm_JDTMethod, multiplicity=Multiplicity(0, 1))
    }
)
packageFragmentRoot40: BinaryAssociation = BinaryAssociation(
    name="packageFragmentRoot40",
    ends={
        Property(name="JDTPackageFragmentRoot", type=jdtmm_JDTPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragments", type=jdtmm_JDTPackageFragmentRoot, multiplicity=Multiplicity(0, 1))
    }
)
compilationUnits41: BinaryAssociation = BinaryAssociation(
    name="compilationUnits41",
    ends={
        Property(name="JDTCompilationUnit42", type=jdtmm_JDTPackageFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragment", type=jdtmm_JDTCompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
javaProject43: BinaryAssociation = BinaryAssociation(
    name="javaProject43",
    ends={
        Property(name="JDTJavaProject", type=jdtmm_JDTPackageFragmentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragmentRoots", type=jdtmm_JDTJavaProject, multiplicity=Multiplicity(0, 1))
    }
)
packageFragments44: BinaryAssociation = BinaryAssociation(
    name="packageFragments44",
    ends={
        Property(name="JDTPackageFragment45", type=jdtmm_JDTPackageFragmentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="packageFragmentRoot", type=jdtmm_JDTPackageFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="jdtmm_JDTType55", type=jdtmm_JDTParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="jdtmm_JDTParameter", type=jdtmm_JDTType, multiplicity=Multiplicity(0, 1))
    }
)
returnOwner56: BinaryAssociation = BinaryAssociation(
    name="returnOwner56",
    ends={
        Property(name="JDTMethod57", type=jdtmm_JDTParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="returnType", type=jdtmm_JDTMethod, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_jdtmm_JDTMethod_JDTMember = Generalization(general=JDTMember, specific=jdtmm_JDTMethod)
gen_jdtmm_JDTParentJavaElement_JDTJavaElement = Generalization(general=JDTJavaElement, specific=jdtmm_JDTParentJavaElement)
gen_jdtmm_JDTParentJavaElement_JDTParent = Generalization(general=JDTParent, specific=jdtmm_JDTParentJavaElement)
gen_jdtmm_JDTMember_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTMember)
gen_jdtmm_JDTTypeParameter_JDTJavaElement = Generalization(general=JDTJavaElement, specific=jdtmm_JDTTypeParameter)
gen_jdtmm_JDTType_JDTMember = Generalization(general=JDTMember, specific=jdtmm_JDTType)
gen_jdtmm_JDTField_JDTMember = Generalization(general=JDTMember, specific=jdtmm_JDTField)
gen_jdtmm_JDTCompilationUnit_JDTTypeRoot = Generalization(general=JDTTypeRoot, specific=jdtmm_JDTCompilationUnit)
gen_jdtmm_JDTTypeRoot_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTTypeRoot)
gen_jdtmm_JDTPackageFragment_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTPackageFragment)
gen_jdtmm_JDTJavaModel_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTJavaModel)
gen_jdtmm_JDTParameter_JDTMember = Generalization(general=JDTMember, specific=jdtmm_JDTParameter)
gen_jdtmm_JDTPackageFragmentRoot_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTPackageFragmentRoot)
gen_jdtmm_JDTJavaProject_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTJavaProject)
gen_jdtmm_JDTImportContainer_JDTParentJavaElement = Generalization(general=JDTParentJavaElement, specific=jdtmm_JDTImportContainer)
gen_jdtmm_JDTOpaqueBody_JDTMethodBody = Generalization(general=JDTMethodBody, specific=jdtmm_JDTOpaqueBody)
gen_jdtmm_JDTClass_JDTType = Generalization(general=JDTType, specific=jdtmm_JDTClass)
gen_jdtmm_JDTInterface_JDTType = Generalization(general=JDTType, specific=jdtmm_JDTInterface)
gen_jdtmm_JDTEnum_JDTType = Generalization(general=JDTType, specific=jdtmm_JDTEnum)
gen_jdtmm_JDTImportDeclaration_JDTJavaElement = Generalization(general=JDTJavaElement, specific=jdtmm_JDTImportDeclaration)

# Domain Model
domain_model = DomainModel(
    name="jdtmm",
    types={jdtmm_JDTParameter, jdtmm_JDTMethodBody, jdtmm_JDTMethod, JDTMember, jdtmm_JDTType, jdtmm_JDTParentJavaElement, JDTJavaElement, JDTParent, jdtmm_JDTParent, jdtmm_JDTMember, JDTParentJavaElement, jdtmm_JDTTypeParameter, jdtmm_JDTJavaElement, jdtmm_JDTCompilationUnit, jdtmm_JDTField, jdtmm_JDTPackageFragment, jdtmm_JDTTypeRoot, JDTTypeRoot, jdtmm_JDTPackageFragmentRoot, jdtmm_JDTJavaProject, jdtmm_JDTJavaModel, jdtmm_JDTImportContainer, jdtmm_JDTException, jdtmm_JDTOpaqueBody, JDTMethodBody, jdtmm_JDTClass, JDTType, jdtmm_JDTInterface, jdtmm_JDTEnum, jdtmm_JDTImportDeclaration, VisibilityKind, TrueFalseDefault},
    associations={owner1, returnType2, parameters3, owner0, explicitRequiredImports8, exceptions5, bodies6, typeParameters7, parent11, declaringMember12, children10, compilationUnit18, methods13, fields16, type33, types20, owner24, superInterfaces28, superClass31, packageFragment37, types38, owner35, javaModel46, packageFragmentRoots47, javaProject50, parameterOwner52, packageFragmentRoot40, compilationUnits41, javaProject43, packageFragments44, type54, returnOwner56},
    generalizations={gen_jdtmm_JDTMethod_JDTMember, gen_jdtmm_JDTParentJavaElement_JDTJavaElement, gen_jdtmm_JDTParentJavaElement_JDTParent, gen_jdtmm_JDTMember_JDTParentJavaElement, gen_jdtmm_JDTTypeParameter_JDTJavaElement, gen_jdtmm_JDTType_JDTMember, gen_jdtmm_JDTField_JDTMember, gen_jdtmm_JDTCompilationUnit_JDTTypeRoot, gen_jdtmm_JDTTypeRoot_JDTParentJavaElement, gen_jdtmm_JDTPackageFragment_JDTParentJavaElement, gen_jdtmm_JDTJavaModel_JDTParentJavaElement, gen_jdtmm_JDTParameter_JDTMember, gen_jdtmm_JDTPackageFragmentRoot_JDTParentJavaElement, gen_jdtmm_JDTJavaProject_JDTParentJavaElement, gen_jdtmm_JDTImportContainer_JDTParentJavaElement, gen_jdtmm_JDTOpaqueBody_JDTMethodBody, gen_jdtmm_JDTClass_JDTType, gen_jdtmm_JDTInterface_JDTType, gen_jdtmm_JDTEnum_JDTType, gen_jdtmm_JDTImportDeclaration_JDTJavaElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)