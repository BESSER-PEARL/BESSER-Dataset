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
CPPParameterPassingKind: Enumeration = Enumeration(
    name="CPPParameterPassingKind",
    literals={
            EnumerationLiteral(name="BY_VALUE"),
			EnumerationLiteral(name="BY_REFERENCE"),
			EnumerationLiteral(name="BY_CONSTANT_REFERENCE")
    }
)

# Classes
cppmodel_CPPNamedElement = Class(name="cppmodel::CPPNamedElement", is_abstract=True)
cppmodel_OOPLNameProvider = Class(name="cppmodel::OOPLNameProvider")
cppmodel_CPPQualifiedNamedElement = Class(name="cppmodel::CPPQualifiedNamedElement", is_abstract=True)
CPPNamedElement = Class(name="CPPNamedElement")
cppmodel_CPPHeaderFile = Class(name="cppmodel::CPPHeaderFile")
cppmodel_CPPDirectory = Class(name="cppmodel::CPPDirectory")
cppmodel_CPPModel = Class(name="cppmodel::CPPModel")
CPPQualifiedNamedElement = Class(name="CPPQualifiedNamedElement")
cppmodel_Model = Class(name="cppmodel::Model")
cppmodel_CPPBodyFile = Class(name="cppmodel::CPPBodyFile")
cppmodel_Package = Class(name="cppmodel::Package")
cppmodel_CPPPackage = Class(name="cppmodel::CPPPackage")
cppmodel_XTProtocol = Class(name="cppmodel::XTProtocol")
cppmodel_CPPSourceFile = Class(name="cppmodel::CPPSourceFile", is_abstract=True)
cppmodel_CPPClass = Class(name="cppmodel::CPPClass")
OOPLClass = Class(name="OOPLClass")
cppmodel_CPPProtocol = Class(name="cppmodel::CPPProtocol")
cppmodel_CPPExternalHeaderInclusion = Class(name="cppmodel::CPPExternalHeaderInclusion")
CPPSourceFile = Class(name="CPPSourceFile")
cppmodel_CPPMakeFile = Class(name="cppmodel::CPPMakeFile")
cppmodel_CPPComponent = Class(name="cppmodel::CPPComponent")
cppmodel_XTComponent = Class(name="cppmodel::XTComponent")
cppmodel_CPPExternalHeader = Class(name="cppmodel::CPPExternalHeader")
cppmodel_CPPOperation = Class(name="cppmodel::CPPOperation")
cppmodel_Operation = Class(name="cppmodel::Operation")
cppmodel_Snippet = Class(name="cppmodel::Snippet")
cppmodel_CPPPort = Class(name="cppmodel::CPPPort")
cppmodel_XTPort = Class(name="cppmodel::XTPort")
cppmodel_CPPRelation = Class(name="cppmodel::CPPRelation")
OOPLRelation = Class(name="OOPLRelation")
cppmodel_CPPProtocolOperationDefinition = Class(name="cppmodel::CPPProtocolOperationDefinition")
cppmodel_XTProtocolOperationDefinition = Class(name="cppmodel::XTProtocolOperationDefinition")
cppmodel_CPPSignal = Class(name="cppmodel::CPPSignal")
cppmodel_Signal = Class(name="cppmodel::Signal")
cppmodel_CPPClassReferenceStorage = Class(name="cppmodel::CPPClassReferenceStorage")
OOPLClassReferenceStorage = Class(name="OOPLClassReferenceStorage")
cppmodel_CPPClassRefSimpleCollection = Class(name="cppmodel::CPPClassRefSimpleCollection")
OOPLClassRefSimpleCollection = Class(name="OOPLClassRefSimpleCollection")
cppmodel_CPPProtocolOperationImplementation = Class(name="cppmodel::CPPProtocolOperationImplementation")
cppmodel_XTProtocolOperationImplementation = Class(name="cppmodel::XTProtocolOperationImplementation")
cppmodel_CPPClassReference = Class(name="cppmodel::CPPClassReference")
OOPLClassReference = Class(name="OOPLClassReference")
cppmodel_Attribute = Class(name="cppmodel::Attribute")
cppmodel_CPPSequence = Class(name="cppmodel::CPPSequence")
cppmodel_OOPLDataType = Class(name="cppmodel::OOPLDataType")
cppmodel_CPPClassRefAssocCollection = Class(name="cppmodel::CPPClassRefAssocCollection")
OOPLClassRefAssocCollection = Class(name="OOPLClassRefAssocCollection")
cppmodel_CPPAttribute = Class(name="cppmodel::CPPAttribute")
cppmodel_CPPTransition = Class(name="cppmodel::CPPTransition")
cppmodel_Transition = Class(name="cppmodel::Transition")
cppmodel_CPPState = Class(name="cppmodel::CPPState")
cppmodel_State = Class(name="cppmodel::State")
cppmodel_Parameter = Class(name="cppmodel::Parameter")
cppmodel_CPPEvent = Class(name="cppmodel::CPPEvent")
cppmodel_XTEvent = Class(name="cppmodel::XTEvent")
cppmodel_CPPFormalParameter = Class(name="cppmodel::CPPFormalParameter")
cppmodel_TypedMultiplicityElement = Class(name="cppmodel::TypedMultiplicityElement")
cppmodel_CPPExternalLibrary = Class(name="cppmodel::CPPExternalLibrary")
cppmodel_CPPReturnValue = Class(name="cppmodel::CPPReturnValue")
cppmodel_CPPEnumType = Class(name="cppmodel::CPPEnumType")
OOPLEnumType = Class(name="OOPLEnumType")
cppmodel_CPPEnumerator = Class(name="cppmodel::CPPEnumerator")
OOPLEnumerator = Class(name="OOPLEnumerator")
cppmodel_CPPBasicType = Class(name="cppmodel::CPPBasicType")
OOPLBasicType = Class(name="OOPLBasicType")
OOPLSequence = Class(name="OOPLSequence")
cppmodel_CPPExternalBridge = Class(name="cppmodel::CPPExternalBridge")
cppmodel_XTClass = Class(name="cppmodel::XTClass")
cppmodel_CPPStructType = Class(name="cppmodel::CPPStructType")
OOPLStructType = Class(name="OOPLStructType")
cppmodel_CPPStructMember = Class(name="cppmodel::CPPStructMember")
OOPLStructMember = Class(name="OOPLStructMember")
cppmodel_CPPUserDefinedType = Class(name="cppmodel::CPPUserDefinedType")
OOPLUserDefinedType = Class(name="OOPLUserDefinedType")

# cppmodel_CPPNamedElement class attributes and methods
cppmodel_CPPNamedElement_cppName: Property = Property(name="cppName", type=StringType)
cppmodel_CPPNamedElement.attributes={cppmodel_CPPNamedElement_cppName}

# cppmodel_OOPLNameProvider class attributes and methods

# cppmodel_CPPQualifiedNamedElement class attributes and methods
cppmodel_CPPQualifiedNamedElement_cppPrefix: Property = Property(name="cppPrefix", type=StringType)
cppmodel_CPPQualifiedNamedElement_cppQualifiedName: Property = Property(name="cppQualifiedName", type=StringType)
cppmodel_CPPQualifiedNamedElement.attributes={cppmodel_CPPQualifiedNamedElement_cppPrefix, cppmodel_CPPQualifiedNamedElement_cppQualifiedName}

# CPPNamedElement class attributes and methods

# cppmodel_CPPHeaderFile class attributes and methods
cppmodel_CPPHeaderFile_includeName: Property = Property(name="includeName", type=StringType)
cppmodel_CPPHeaderFile_includeDirectory: Property = Property(name="includeDirectory", type=StringType)
cppmodel_CPPHeaderFile_includePath: Property = Property(name="includePath", type=StringType)
cppmodel_CPPHeaderFile.attributes={cppmodel_CPPHeaderFile_includePath, cppmodel_CPPHeaderFile_includeDirectory, cppmodel_CPPHeaderFile_includeName}

# cppmodel_CPPDirectory class attributes and methods
cppmodel_CPPDirectory_name: Property = Property(name="name", type=StringType)
cppmodel_CPPDirectory_parentDirectory: Property = Property(name="parentDirectory", type=StringType)
cppmodel_CPPDirectory_path: Property = Property(name="path", type=StringType)
cppmodel_CPPDirectory.attributes={cppmodel_CPPDirectory_path, cppmodel_CPPDirectory_parentDirectory, cppmodel_CPPDirectory_name}

# cppmodel_CPPModel class attributes and methods

# CPPQualifiedNamedElement class attributes and methods

# cppmodel_Model class attributes and methods

# cppmodel_CPPBodyFile class attributes and methods

# cppmodel_Package class attributes and methods

# cppmodel_CPPPackage class attributes and methods

# cppmodel_XTProtocol class attributes and methods

# cppmodel_CPPSourceFile class attributes and methods
cppmodel_CPPSourceFile_generationName: Property = Property(name="generationName", type=StringType)
cppmodel_CPPSourceFile_generationDirectory: Property = Property(name="generationDirectory", type=StringType)
cppmodel_CPPSourceFile_generationPath: Property = Property(name="generationPath", type=StringType)
cppmodel_CPPSourceFile.attributes={cppmodel_CPPSourceFile_generationPath, cppmodel_CPPSourceFile_generationName, cppmodel_CPPSourceFile_generationDirectory}

# cppmodel_CPPClass class attributes and methods

# OOPLClass class attributes and methods

# cppmodel_CPPProtocol class attributes and methods

# cppmodel_CPPExternalHeaderInclusion class attributes and methods
cppmodel_CPPExternalHeaderInclusion_comment: Property = Property(name="comment", type=StringType)
cppmodel_CPPExternalHeaderInclusion.attributes={cppmodel_CPPExternalHeaderInclusion_comment}

# CPPSourceFile class attributes and methods

# cppmodel_CPPMakeFile class attributes and methods

# cppmodel_CPPComponent class attributes and methods

# cppmodel_XTComponent class attributes and methods

# cppmodel_CPPExternalHeader class attributes and methods
cppmodel_CPPExternalHeader_name: Property = Property(name="name", type=StringType)
cppmodel_CPPExternalHeader.attributes={cppmodel_CPPExternalHeader_name}

# cppmodel_CPPOperation class attributes and methods

# cppmodel_Operation class attributes and methods

# cppmodel_Snippet class attributes and methods

# cppmodel_CPPPort class attributes and methods

# cppmodel_XTPort class attributes and methods

# cppmodel_CPPRelation class attributes and methods

# OOPLRelation class attributes and methods

# cppmodel_CPPProtocolOperationDefinition class attributes and methods

# cppmodel_XTProtocolOperationDefinition class attributes and methods

# cppmodel_CPPSignal class attributes and methods

# cppmodel_Signal class attributes and methods

# cppmodel_CPPClassReferenceStorage class attributes and methods

# OOPLClassReferenceStorage class attributes and methods

# cppmodel_CPPClassRefSimpleCollection class attributes and methods
cppmodel_CPPClassRefSimpleCollection_cppContainer: Property = Property(name="cppContainer", type=StringType)
cppmodel_CPPClassRefSimpleCollection.attributes={cppmodel_CPPClassRefSimpleCollection_cppContainer}

# OOPLClassRefSimpleCollection class attributes and methods

# cppmodel_CPPProtocolOperationImplementation class attributes and methods

# cppmodel_XTProtocolOperationImplementation class attributes and methods

# cppmodel_CPPClassReference class attributes and methods

# OOPLClassReference class attributes and methods

# cppmodel_Attribute class attributes and methods

# cppmodel_CPPSequence class attributes and methods
cppmodel_CPPSequence_cppContainer: Property = Property(name="cppContainer", type=StringType)
cppmodel_CPPSequence.attributes={cppmodel_CPPSequence_cppContainer}

# cppmodel_OOPLDataType class attributes and methods

# cppmodel_CPPClassRefAssocCollection class attributes and methods
cppmodel_CPPClassRefAssocCollection_cppContainer: Property = Property(name="cppContainer", type=StringType)
cppmodel_CPPClassRefAssocCollection.attributes={cppmodel_CPPClassRefAssocCollection_cppContainer}

# OOPLClassRefAssocCollection class attributes and methods

# cppmodel_CPPAttribute class attributes and methods

# cppmodel_CPPTransition class attributes and methods

# cppmodel_Transition class attributes and methods

# cppmodel_CPPState class attributes and methods

# cppmodel_State class attributes and methods

# cppmodel_Parameter class attributes and methods

# cppmodel_CPPEvent class attributes and methods

# cppmodel_XTEvent class attributes and methods

# cppmodel_CPPFormalParameter class attributes and methods
cppmodel_CPPFormalParameter_passingMode: Property = Property(name="passingMode", type=StringType)
cppmodel_CPPFormalParameter.attributes={cppmodel_CPPFormalParameter_passingMode}

# cppmodel_TypedMultiplicityElement class attributes and methods

# cppmodel_CPPExternalLibrary class attributes and methods

# cppmodel_CPPReturnValue class attributes and methods

# cppmodel_CPPEnumType class attributes and methods

# OOPLEnumType class attributes and methods

# cppmodel_CPPEnumerator class attributes and methods
cppmodel_CPPEnumerator_cppValue: Property = Property(name="cppValue", type=StringType)
cppmodel_CPPEnumerator.attributes={cppmodel_CPPEnumerator_cppValue}

# OOPLEnumerator class attributes and methods

# cppmodel_CPPBasicType class attributes and methods
cppmodel_CPPBasicType_cppSpecifier: Property = Property(name="cppSpecifier", type=StringType)
cppmodel_CPPBasicType.attributes={cppmodel_CPPBasicType_cppSpecifier}

# OOPLBasicType class attributes and methods

# OOPLSequence class attributes and methods

# cppmodel_CPPExternalBridge class attributes and methods
cppmodel_CPPExternalBridge_cppExternalNamespace: Property = Property(name="cppExternalNamespace", type=StringType)
cppmodel_CPPExternalBridge.attributes={cppmodel_CPPExternalBridge_cppExternalNamespace}

# cppmodel_XTClass class attributes and methods

# cppmodel_CPPStructType class attributes and methods

# OOPLStructType class attributes and methods

# cppmodel_CPPStructMember class attributes and methods

# OOPLStructMember class attributes and methods

# cppmodel_CPPUserDefinedType class attributes and methods

# OOPLUserDefinedType class attributes and methods

# Relationships
ooplNameProvider0: BinaryAssociation = BinaryAssociation(
    name="ooplNameProvider0",
    ends={
        Property(name="cppmodel_OOPLNameProvider", type=cppmodel_CPPNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPNamedElement", type=cppmodel_OOPLNameProvider, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarationHeaderFile6: BinaryAssociation = BinaryAssociation(
    name="declarationHeaderFile6",
    ends={
        Property(name="cppmodel_CPPHeaderFile", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel7", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
definitionHeaderFile8: BinaryAssociation = BinaryAssociation(
    name="definitionHeaderFile8",
    ends={
        Property(name="cppmodel_CPPHeaderFile10", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel9", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
apiHeaderFile11: BinaryAssociation = BinaryAssociation(
    name="apiHeaderFile11",
    ends={
        Property(name="cppmodel_CPPHeaderFile13", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel12", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(0, 1))
    }
)
headerDir14: BinaryAssociation = BinaryAssociation(
    name="headerDir14",
    ends={
        Property(name="cppmodel_CPPDirectory", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel15", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
subElements2: BinaryAssociation = BinaryAssociation(
    name="subElements2",
    ends={
        Property(name="cppmodel_CPPQualifiedNamedElement", type=cppmodel_CPPQualifiedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPQualifiedNamedElement1", type=cppmodel_CPPQualifiedNamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commonModel3: BinaryAssociation = BinaryAssociation(
    name="commonModel3",
    ends={
        Property(name="cppmodel_Model", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel", type=cppmodel_Model, multiplicity=Multiplicity(1, 1))
    }
)
bodyFile4: BinaryAssociation = BinaryAssociation(
    name="bodyFile4",
    ends={
        Property(name="cppmodel_CPPBodyFile", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel5", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(0, 1))
    }
)
commonPackage25: BinaryAssociation = BinaryAssociation(
    name="commonPackage25",
    ends={
        Property(name="cppmodel_Package", type=cppmodel_CPPPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPackage", type=cppmodel_Package, multiplicity=Multiplicity(1, 1))
    }
)
bodyFile26: BinaryAssociation = BinaryAssociation(
    name="bodyFile26",
    ends={
        Property(name="cppmodel_CPPBodyFile28", type=cppmodel_CPPPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPackage27", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(0, 1))
    }
)
headerFile29: BinaryAssociation = BinaryAssociation(
    name="headerFile29",
    ends={
        Property(name="cppmodel_CPPHeaderFile31", type=cppmodel_CPPPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPackage30", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(0, 1))
    }
)
headerDir32: BinaryAssociation = BinaryAssociation(
    name="headerDir32",
    ends={
        Property(name="cppmodel_CPPDirectory34", type=cppmodel_CPPPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPackage33", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
bodyDir35: BinaryAssociation = BinaryAssociation(
    name="bodyDir35",
    ends={
        Property(name="cppmodel_CPPDirectory37", type=cppmodel_CPPPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPackage36", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
bodyDir16: BinaryAssociation = BinaryAssociation(
    name="bodyDir16",
    ends={
        Property(name="cppmodel_CPPDirectory18", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel17", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
externalHeaderDir19: BinaryAssociation = BinaryAssociation(
    name="externalHeaderDir19",
    ends={
        Property(name="cppmodel_CPPDirectory21", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel20", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
externalBodySkeletonDir22: BinaryAssociation = BinaryAssociation(
    name="externalBodySkeletonDir22",
    ends={
        Property(name="cppmodel_CPPDirectory24", type=cppmodel_CPPModel, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPModel23", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
xtProtocol43: BinaryAssociation = BinaryAssociation(
    name="xtProtocol43",
    ends={
        Property(name="cppmodel_XTProtocol", type=cppmodel_CPPProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPProtocol", type=cppmodel_XTProtocol, multiplicity=Multiplicity(1, 1))
    }
)
headerFile44: BinaryAssociation = BinaryAssociation(
    name="headerFile44",
    ends={
        Property(name="cppmodel_CPPHeaderFile46", type=cppmodel_CPPProtocol, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPProtocol45", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
headerFile38: BinaryAssociation = BinaryAssociation(
    name="headerFile38",
    ends={
        Property(name="cppmodel_CPPHeaderFile39", type=cppmodel_CPPClass, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPClass", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
bodyFile40: BinaryAssociation = BinaryAssociation(
    name="bodyFile40",
    ends={
        Property(name="cppmodel_CPPBodyFile42", type=cppmodel_CPPClass, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPClass41", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(1, 1))
    }
)
includedHeaders47: BinaryAssociation = BinaryAssociation(
    name="includedHeaders47",
    ends={
        Property(name="cppmodel_CPPHeaderFile48", type=cppmodel_CPPSourceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPSourceFile", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(0, 9999))
    }
)
externalHeaderInclusion49: BinaryAssociation = BinaryAssociation(
    name="externalHeaderInclusion49",
    ends={
        Property(name="cppmodel_CPPExternalHeaderInclusion", type=cppmodel_CPPSourceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPSourceFile50", type=cppmodel_CPPExternalHeaderInclusion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subDirectories52: BinaryAssociation = BinaryAssociation(
    name="subDirectories52",
    ends={
        Property(name="cppmodel_CPPDirectory53", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPDirectory51", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files54: BinaryAssociation = BinaryAssociation(
    name="files54",
    ends={
        Property(name="cppmodel_CPPSourceFile56", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPDirectory55", type=cppmodel_CPPSourceFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
makeRulesFile57: BinaryAssociation = BinaryAssociation(
    name="makeRulesFile57",
    ends={
        Property(name="cppmodel_CPPMakeFile", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPDirectory58", type=cppmodel_CPPMakeFile, multiplicity=Multiplicity(0, 1))
    }
)
xtComponent59: BinaryAssociation = BinaryAssociation(
    name="xtComponent59",
    ends={
        Property(name="cppmodel_XTComponent", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent", type=cppmodel_XTComponent, multiplicity=Multiplicity(1, 1))
    }
)
mainHeaderFile60: BinaryAssociation = BinaryAssociation(
    name="mainHeaderFile60",
    ends={
        Property(name="cppmodel_CPPHeaderFile62", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent61", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
bodyDirectory75: BinaryAssociation = BinaryAssociation(
    name="bodyDirectory75",
    ends={
        Property(name="cppmodel_CPPDirectory77", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent76", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
externalHeaderDirectory78: BinaryAssociation = BinaryAssociation(
    name="externalHeaderDirectory78",
    ends={
        Property(name="cppmodel_CPPDirectory80", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent79", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
externalBodySkeletonDirectory81: BinaryAssociation = BinaryAssociation(
    name="externalBodySkeletonDirectory81",
    ends={
        Property(name="cppmodel_CPPDirectory83", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent82", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
mainBodyFile63: BinaryAssociation = BinaryAssociation(
    name="mainBodyFile63",
    ends={
        Property(name="cppmodel_CPPBodyFile65", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent64", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(1, 1))
    }
)
declarationHeaderFile66: BinaryAssociation = BinaryAssociation(
    name="declarationHeaderFile66",
    ends={
        Property(name="cppmodel_CPPHeaderFile68", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent67", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
definitionHeaderFile69: BinaryAssociation = BinaryAssociation(
    name="definitionHeaderFile69",
    ends={
        Property(name="cppmodel_CPPHeaderFile71", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent70", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
headerDirectory72: BinaryAssociation = BinaryAssociation(
    name="headerDirectory72",
    ends={
        Property(name="cppmodel_CPPDirectory74", type=cppmodel_CPPComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPComponent73", type=cppmodel_CPPDirectory, multiplicity=Multiplicity(0, 1))
    }
)
commonOperation86: BinaryAssociation = BinaryAssociation(
    name="commonOperation86",
    ends={
        Property(name="cppmodel_Operation", type=cppmodel_CPPOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPOperation", type=cppmodel_Operation, multiplicity=Multiplicity(1, 1))
    }
)
compiledBody87: BinaryAssociation = BinaryAssociation(
    name="compiledBody87",
    ends={
        Property(name="cppmodel_Snippet", type=cppmodel_CPPOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPOperation88", type=cppmodel_Snippet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalHeader84: BinaryAssociation = BinaryAssociation(
    name="externalHeader84",
    ends={
        Property(name="cppmodel_CPPExternalHeader", type=cppmodel_CPPExternalHeaderInclusion, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPExternalHeaderInclusion85", type=cppmodel_CPPExternalHeader, multiplicity=Multiplicity(1, 1))
    }
)
externalBodySkeletonFile99: BinaryAssociation = BinaryAssociation(
    name="externalBodySkeletonFile99",
    ends={
        Property(name="cppmodel_CPPBodyFile101", type=cppmodel_CPPPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPort100", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(0, 1))
    }
)
xtProtocolOperationDefinition102: BinaryAssociation = BinaryAssociation(
    name="xtProtocolOperationDefinition102",
    ends={
        Property(name="cppmodel_XTProtocolOperationDefinition", type=cppmodel_CPPProtocolOperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPProtocolOperationDefinition", type=cppmodel_XTProtocolOperationDefinition, multiplicity=Multiplicity(1, 1))
    }
)
xtPort89: BinaryAssociation = BinaryAssociation(
    name="xtPort89",
    ends={
        Property(name="cppmodel_XTPort", type=cppmodel_CPPPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPort", type=cppmodel_XTPort, multiplicity=Multiplicity(1, 1))
    }
)
headerFile90: BinaryAssociation = BinaryAssociation(
    name="headerFile90",
    ends={
        Property(name="cppmodel_CPPHeaderFile92", type=cppmodel_CPPPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPort91", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
externalHeaderFile93: BinaryAssociation = BinaryAssociation(
    name="externalHeaderFile93",
    ends={
        Property(name="cppmodel_CPPHeaderFile95", type=cppmodel_CPPPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPort94", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(0, 1))
    }
)
bodyFile96: BinaryAssociation = BinaryAssociation(
    name="bodyFile96",
    ends={
        Property(name="cppmodel_CPPBodyFile98", type=cppmodel_CPPPort, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPPort97", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(1, 1))
    }
)
commonSignal103: BinaryAssociation = BinaryAssociation(
    name="commonSignal103",
    ends={
        Property(name="cppmodel_Signal", type=cppmodel_CPPSignal, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPSignal", type=cppmodel_Signal, multiplicity=Multiplicity(1, 1))
    }
)
xtProtocolOperationImplementation104: BinaryAssociation = BinaryAssociation(
    name="xtProtocolOperationImplementation104",
    ends={
        Property(name="cppmodel_XTProtocolOperationImplementation", type=cppmodel_CPPProtocolOperationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPProtocolOperationImplementation", type=cppmodel_XTProtocolOperationImplementation, multiplicity=Multiplicity(1, 1))
    }
)
commonAttribute106: BinaryAssociation = BinaryAssociation(
    name="commonAttribute106",
    ends={
        Property(name="cppmodel_Attribute", type=cppmodel_CPPAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPAttribute107", type=cppmodel_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
unnamedSequenceType108: BinaryAssociation = BinaryAssociation(
    name="unnamedSequenceType108",
    ends={
        Property(name="cppmodel_CPPSequence", type=cppmodel_CPPAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPAttribute109", type=cppmodel_CPPSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type110: BinaryAssociation = BinaryAssociation(
    name="type110",
    ends={
        Property(name="cppmodel_OOPLDataType", type=cppmodel_CPPAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPAttribute111", type=cppmodel_OOPLDataType, multiplicity=Multiplicity(1, 1))
    }
)
cppAttribute105: BinaryAssociation = BinaryAssociation(
    name="cppAttribute105",
    ends={
        Property(name="cppmodel_CPPAttribute", type=cppmodel_CPPClassRefAssocCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPClassRefAssocCollection", type=cppmodel_CPPAttribute, multiplicity=Multiplicity(1, 1))
    }
)
compiledExitBody116: BinaryAssociation = BinaryAssociation(
    name="compiledExitBody116",
    ends={
        Property(name="cppmodel_Snippet118", type=cppmodel_CPPState, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPState117", type=cppmodel_Snippet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commonTransition119: BinaryAssociation = BinaryAssociation(
    name="commonTransition119",
    ends={
        Property(name="cppmodel_Transition", type=cppmodel_CPPTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPTransition", type=cppmodel_Transition, multiplicity=Multiplicity(1, 1))
    }
)
compiledEffectBody120: BinaryAssociation = BinaryAssociation(
    name="compiledEffectBody120",
    ends={
        Property(name="cppmodel_Snippet122", type=cppmodel_CPPTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPTransition121", type=cppmodel_Snippet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compiledGuardBody123: BinaryAssociation = BinaryAssociation(
    name="compiledGuardBody123",
    ends={
        Property(name="cppmodel_Snippet125", type=cppmodel_CPPTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPTransition124", type=cppmodel_Snippet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commonState112: BinaryAssociation = BinaryAssociation(
    name="commonState112",
    ends={
        Property(name="cppmodel_State", type=cppmodel_CPPState, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPState", type=cppmodel_State, multiplicity=Multiplicity(1, 1))
    }
)
compiledEntryBody113: BinaryAssociation = BinaryAssociation(
    name="compiledEntryBody113",
    ends={
        Property(name="cppmodel_Snippet115", type=cppmodel_CPPState, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPState114", type=cppmodel_Snippet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commonParameter127: BinaryAssociation = BinaryAssociation(
    name="commonParameter127",
    ends={
        Property(name="cppmodel_Parameter", type=cppmodel_CPPFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPFormalParameter", type=cppmodel_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
unnamedSequenceType128: BinaryAssociation = BinaryAssociation(
    name="unnamedSequenceType128",
    ends={
        Property(name="cppmodel_CPPSequence130", type=cppmodel_CPPFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPFormalParameter129", type=cppmodel_CPPSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type131: BinaryAssociation = BinaryAssociation(
    name="type131",
    ends={
        Property(name="cppmodel_OOPLDataType133", type=cppmodel_CPPFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPFormalParameter132", type=cppmodel_OOPLDataType, multiplicity=Multiplicity(1, 1))
    }
)
xtEvent126: BinaryAssociation = BinaryAssociation(
    name="xtEvent126",
    ends={
        Property(name="cppmodel_XTEvent", type=cppmodel_CPPEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPEvent", type=cppmodel_XTEvent, multiplicity=Multiplicity(1, 1))
    }
)
unnamedSequenceType136: BinaryAssociation = BinaryAssociation(
    name="unnamedSequenceType136",
    ends={
        Property(name="cppmodel_CPPSequence138", type=cppmodel_CPPReturnValue, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPReturnValue137", type=cppmodel_CPPSequence, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commonTypedMultiplicityElement139: BinaryAssociation = BinaryAssociation(
    name="commonTypedMultiplicityElement139",
    ends={
        Property(name="cppmodel_TypedMultiplicityElement", type=cppmodel_CPPReturnValue, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPReturnValue140", type=cppmodel_TypedMultiplicityElement, multiplicity=Multiplicity(1, 1))
    }
)
externalHeader141: BinaryAssociation = BinaryAssociation(
    name="externalHeader141",
    ends={
        Property(name="cppmodel_CPPExternalHeader142", type=cppmodel_CPPExternalLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPExternalLibrary", type=cppmodel_CPPExternalHeader, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type134: BinaryAssociation = BinaryAssociation(
    name="type134",
    ends={
        Property(name="cppmodel_OOPLDataType135", type=cppmodel_CPPReturnValue, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPReturnValue", type=cppmodel_OOPLDataType, multiplicity=Multiplicity(1, 1))
    }
)
headerFile143: BinaryAssociation = BinaryAssociation(
    name="headerFile143",
    ends={
        Property(name="cppmodel_CPPHeaderFile144", type=cppmodel_CPPExternalBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPExternalBridge", type=cppmodel_CPPHeaderFile, multiplicity=Multiplicity(1, 1))
    }
)
bodyFile145: BinaryAssociation = BinaryAssociation(
    name="bodyFile145",
    ends={
        Property(name="cppmodel_CPPBodyFile147", type=cppmodel_CPPExternalBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPExternalBridge146", type=cppmodel_CPPBodyFile, multiplicity=Multiplicity(1, 1))
    }
)
xtClass148: BinaryAssociation = BinaryAssociation(
    name="xtClass148",
    ends={
        Property(name="cppmodel_XTClass", type=cppmodel_CPPExternalBridge, multiplicity=Multiplicity(1, 1)),
        Property(name="cppmodel_CPPExternalBridge149", type=cppmodel_XTClass, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_cppmodel_CPPQualifiedNamedElement_CPPNamedElement = Generalization(general=CPPNamedElement, specific=cppmodel_CPPQualifiedNamedElement)
gen_cppmodel_CPPModel_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPModel)
gen_cppmodel_CPPPackage_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPPackage)
gen_cppmodel_CPPClass_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPClass)
gen_cppmodel_CPPClass_OOPLClass = Generalization(general=OOPLClass, specific=cppmodel_CPPClass)
gen_cppmodel_CPPProtocol_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPProtocol)
gen_cppmodel_CPPHeaderFile_CPPSourceFile = Generalization(general=CPPSourceFile, specific=cppmodel_CPPHeaderFile)
gen_cppmodel_CPPBodyFile_CPPSourceFile = Generalization(general=CPPSourceFile, specific=cppmodel_CPPBodyFile)
gen_cppmodel_CPPComponent_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPComponent)
gen_cppmodel_CPPOperation_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPOperation)
gen_cppmodel_CPPPort_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPPort)
gen_cppmodel_CPPRelation_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPRelation)
gen_cppmodel_CPPRelation_OOPLRelation = Generalization(general=OOPLRelation, specific=cppmodel_CPPRelation)
gen_cppmodel_CPPProtocolOperationDefinition_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPProtocolOperationDefinition)
gen_cppmodel_CPPSignal_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPSignal)
gen_cppmodel_CPPClassReferenceStorage_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPClassReferenceStorage)
gen_cppmodel_CPPClassReferenceStorage_OOPLClassReferenceStorage = Generalization(general=OOPLClassReferenceStorage, specific=cppmodel_CPPClassReferenceStorage)
gen_cppmodel_CPPClassRefSimpleCollection_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPClassRefSimpleCollection)
gen_cppmodel_CPPClassRefSimpleCollection_OOPLClassRefSimpleCollection = Generalization(general=OOPLClassRefSimpleCollection, specific=cppmodel_CPPClassRefSimpleCollection)
gen_cppmodel_CPPProtocolOperationImplementation_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPProtocolOperationImplementation)
gen_cppmodel_CPPClassReference_OOPLClassReference = Generalization(general=OOPLClassReference, specific=cppmodel_CPPClassReference)
gen_cppmodel_CPPClassReference_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPClassReference)
gen_cppmodel_CPPAttribute_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPAttribute)
gen_cppmodel_CPPClassRefAssocCollection_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPClassRefAssocCollection)
gen_cppmodel_CPPClassRefAssocCollection_OOPLClassRefAssocCollection = Generalization(general=OOPLClassRefAssocCollection, specific=cppmodel_CPPClassRefAssocCollection)
gen_cppmodel_CPPTransition_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPTransition)
gen_cppmodel_CPPState_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPState)
gen_cppmodel_CPPEvent_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPEvent)
gen_cppmodel_CPPFormalParameter_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPFormalParameter)
gen_cppmodel_CPPReturnValue_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPReturnValue)
gen_cppmodel_CPPEnumType_OOPLEnumType = Generalization(general=OOPLEnumType, specific=cppmodel_CPPEnumType)
gen_cppmodel_CPPEnumType_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPEnumType)
gen_cppmodel_CPPEnumerator_OOPLEnumerator = Generalization(general=OOPLEnumerator, specific=cppmodel_CPPEnumerator)
gen_cppmodel_CPPEnumerator_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPEnumerator)
gen_cppmodel_CPPBasicType_OOPLBasicType = Generalization(general=OOPLBasicType, specific=cppmodel_CPPBasicType)
gen_cppmodel_CPPBasicType_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPBasicType)
gen_cppmodel_CPPSequence_OOPLSequence = Generalization(general=OOPLSequence, specific=cppmodel_CPPSequence)
gen_cppmodel_CPPMakeFile_CPPSourceFile = Generalization(general=CPPSourceFile, specific=cppmodel_CPPMakeFile)
gen_cppmodel_CPPExternalBridge_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPExternalBridge)
gen_cppmodel_CPPStructType_OOPLStructType = Generalization(general=OOPLStructType, specific=cppmodel_CPPStructType)
gen_cppmodel_CPPStructType_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPStructType)
gen_cppmodel_CPPStructMember_OOPLStructMember = Generalization(general=OOPLStructMember, specific=cppmodel_CPPStructMember)
gen_cppmodel_CPPStructMember_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPStructMember)
gen_cppmodel_CPPUserDefinedType_OOPLUserDefinedType = Generalization(general=OOPLUserDefinedType, specific=cppmodel_CPPUserDefinedType)
gen_cppmodel_CPPUserDefinedType_CPPQualifiedNamedElement = Generalization(general=CPPQualifiedNamedElement, specific=cppmodel_CPPUserDefinedType)

# Domain Model
domain_model = DomainModel(
    name="cppmodel",
    types={cppmodel_CPPNamedElement, cppmodel_OOPLNameProvider, cppmodel_CPPQualifiedNamedElement, CPPNamedElement, cppmodel_CPPHeaderFile, cppmodel_CPPDirectory, cppmodel_CPPModel, CPPQualifiedNamedElement, cppmodel_Model, cppmodel_CPPBodyFile, cppmodel_Package, cppmodel_CPPPackage, cppmodel_XTProtocol, cppmodel_CPPSourceFile, cppmodel_CPPClass, OOPLClass, cppmodel_CPPProtocol, cppmodel_CPPExternalHeaderInclusion, CPPSourceFile, cppmodel_CPPMakeFile, cppmodel_CPPComponent, cppmodel_XTComponent, cppmodel_CPPExternalHeader, cppmodel_CPPOperation, cppmodel_Operation, cppmodel_Snippet, cppmodel_CPPPort, cppmodel_XTPort, cppmodel_CPPRelation, OOPLRelation, cppmodel_CPPProtocolOperationDefinition, cppmodel_XTProtocolOperationDefinition, cppmodel_CPPSignal, cppmodel_Signal, cppmodel_CPPClassReferenceStorage, OOPLClassReferenceStorage, cppmodel_CPPClassRefSimpleCollection, OOPLClassRefSimpleCollection, cppmodel_CPPProtocolOperationImplementation, cppmodel_XTProtocolOperationImplementation, cppmodel_CPPClassReference, OOPLClassReference, cppmodel_Attribute, cppmodel_CPPSequence, cppmodel_OOPLDataType, cppmodel_CPPClassRefAssocCollection, OOPLClassRefAssocCollection, cppmodel_CPPAttribute, cppmodel_CPPTransition, cppmodel_Transition, cppmodel_CPPState, cppmodel_State, cppmodel_Parameter, cppmodel_CPPEvent, cppmodel_XTEvent, cppmodel_CPPFormalParameter, cppmodel_TypedMultiplicityElement, cppmodel_CPPExternalLibrary, cppmodel_CPPReturnValue, cppmodel_CPPEnumType, OOPLEnumType, cppmodel_CPPEnumerator, OOPLEnumerator, cppmodel_CPPBasicType, OOPLBasicType, OOPLSequence, cppmodel_CPPExternalBridge, cppmodel_XTClass, cppmodel_CPPStructType, OOPLStructType, cppmodel_CPPStructMember, OOPLStructMember, cppmodel_CPPUserDefinedType, OOPLUserDefinedType, CPPParameterPassingKind},
    associations={ooplNameProvider0, declarationHeaderFile6, definitionHeaderFile8, apiHeaderFile11, headerDir14, subElements2, commonModel3, bodyFile4, commonPackage25, bodyFile26, headerFile29, headerDir32, bodyDir35, bodyDir16, externalHeaderDir19, externalBodySkeletonDir22, xtProtocol43, headerFile44, headerFile38, bodyFile40, includedHeaders47, externalHeaderInclusion49, subDirectories52, files54, makeRulesFile57, xtComponent59, mainHeaderFile60, bodyDirectory75, externalHeaderDirectory78, externalBodySkeletonDirectory81, mainBodyFile63, declarationHeaderFile66, definitionHeaderFile69, headerDirectory72, commonOperation86, compiledBody87, externalHeader84, externalBodySkeletonFile99, xtProtocolOperationDefinition102, xtPort89, headerFile90, externalHeaderFile93, bodyFile96, commonSignal103, xtProtocolOperationImplementation104, commonAttribute106, unnamedSequenceType108, type110, cppAttribute105, compiledExitBody116, commonTransition119, compiledEffectBody120, compiledGuardBody123, commonState112, compiledEntryBody113, commonParameter127, unnamedSequenceType128, type131, xtEvent126, unnamedSequenceType136, commonTypedMultiplicityElement139, externalHeader141, type134, headerFile143, bodyFile145, xtClass148},
    generalizations={gen_cppmodel_CPPQualifiedNamedElement_CPPNamedElement, gen_cppmodel_CPPModel_CPPQualifiedNamedElement, gen_cppmodel_CPPPackage_CPPQualifiedNamedElement, gen_cppmodel_CPPClass_CPPQualifiedNamedElement, gen_cppmodel_CPPClass_OOPLClass, gen_cppmodel_CPPProtocol_CPPQualifiedNamedElement, gen_cppmodel_CPPHeaderFile_CPPSourceFile, gen_cppmodel_CPPBodyFile_CPPSourceFile, gen_cppmodel_CPPComponent_CPPQualifiedNamedElement, gen_cppmodel_CPPOperation_CPPQualifiedNamedElement, gen_cppmodel_CPPPort_CPPQualifiedNamedElement, gen_cppmodel_CPPRelation_CPPQualifiedNamedElement, gen_cppmodel_CPPRelation_OOPLRelation, gen_cppmodel_CPPProtocolOperationDefinition_CPPQualifiedNamedElement, gen_cppmodel_CPPSignal_CPPQualifiedNamedElement, gen_cppmodel_CPPClassReferenceStorage_CPPQualifiedNamedElement, gen_cppmodel_CPPClassReferenceStorage_OOPLClassReferenceStorage, gen_cppmodel_CPPClassRefSimpleCollection_CPPQualifiedNamedElement, gen_cppmodel_CPPClassRefSimpleCollection_OOPLClassRefSimpleCollection, gen_cppmodel_CPPProtocolOperationImplementation_CPPQualifiedNamedElement, gen_cppmodel_CPPClassReference_OOPLClassReference, gen_cppmodel_CPPClassReference_CPPQualifiedNamedElement, gen_cppmodel_CPPAttribute_CPPQualifiedNamedElement, gen_cppmodel_CPPClassRefAssocCollection_CPPQualifiedNamedElement, gen_cppmodel_CPPClassRefAssocCollection_OOPLClassRefAssocCollection, gen_cppmodel_CPPTransition_CPPQualifiedNamedElement, gen_cppmodel_CPPState_CPPQualifiedNamedElement, gen_cppmodel_CPPEvent_CPPQualifiedNamedElement, gen_cppmodel_CPPFormalParameter_CPPQualifiedNamedElement, gen_cppmodel_CPPReturnValue_CPPQualifiedNamedElement, gen_cppmodel_CPPEnumType_OOPLEnumType, gen_cppmodel_CPPEnumType_CPPQualifiedNamedElement, gen_cppmodel_CPPEnumerator_OOPLEnumerator, gen_cppmodel_CPPEnumerator_CPPQualifiedNamedElement, gen_cppmodel_CPPBasicType_OOPLBasicType, gen_cppmodel_CPPBasicType_CPPQualifiedNamedElement, gen_cppmodel_CPPSequence_OOPLSequence, gen_cppmodel_CPPMakeFile_CPPSourceFile, gen_cppmodel_CPPExternalBridge_CPPQualifiedNamedElement, gen_cppmodel_CPPStructType_OOPLStructType, gen_cppmodel_CPPStructType_CPPQualifiedNamedElement, gen_cppmodel_CPPStructMember_OOPLStructMember, gen_cppmodel_CPPStructMember_CPPQualifiedNamedElement, gen_cppmodel_CPPUserDefinedType_OOPLUserDefinedType, gen_cppmodel_CPPUserDefinedType_CPPQualifiedNamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)