from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CPPParameterPassingKind(Enum):
    BY_VALUE = "BY_VALUE"
    BY_REFERENCE = "BY_REFERENCE"
    BY_CONSTANT_REFERENCE = "BY_CONSTANT_REFERENCE"


############################################
# Definition of Classes
############################################

class OOPLUserDefinedType:

    pass
class OOPLStructMember:

    pass
class OOPLStructType:

    pass
class cppmodel_XTClass:

    pass
class OOPLSequence:

    pass
class OOPLBasicType:

    pass
class OOPLEnumerator:

    pass
class OOPLEnumType:

    pass
class cppmodel_CPPExternalLibrary:

    pass
class cppmodel_TypedMultiplicityElement:

    pass
class cppmodel_XTEvent:

    pass
class cppmodel_Parameter:

    pass
class cppmodel_State:

    pass
class cppmodel_Transition:

    pass
class OOPLClassRefAssocCollection:

    pass
class cppmodel_OOPLDataType:

    pass
class cppmodel_CPPSequence(OOPLSequence):

    def __init__(self, cppContainer: str, cppmodel_CPPSequence: "cppmodel_CPPAttribute" = None, cppmodel_CPPSequence130: "cppmodel_CPPFormalParameter" = None, cppmodel_CPPSequence138: "cppmodel_CPPReturnValue" = None):
        self.cppContainer = cppContainer
        self.cppmodel_CPPSequence = cppmodel_CPPSequence
        self.cppmodel_CPPSequence130 = cppmodel_CPPSequence130
        self.cppmodel_CPPSequence138 = cppmodel_CPPSequence138
        
    @property
    def cppContainer(self) -> str:
        return self.__cppContainer

    @cppContainer.setter
    def cppContainer(self, cppContainer: str):
        self.__cppContainer = cppContainer

    @property
    def cppmodel_CPPSequence138(self):
        return self.__cppmodel_CPPSequence138

    @cppmodel_CPPSequence138.setter
    def cppmodel_CPPSequence138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPSequence__cppmodel_CPPSequence138", None)
        self.__cppmodel_CPPSequence138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPReturnValue137"):
                opp_val = getattr(old_value, "cppmodel_CPPReturnValue137", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPReturnValue137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPReturnValue137"):
                opp_val = getattr(value, "cppmodel_CPPReturnValue137", None)
                setattr(value, "cppmodel_CPPReturnValue137", self)

    @property
    def cppmodel_CPPSequence130(self):
        return self.__cppmodel_CPPSequence130

    @cppmodel_CPPSequence130.setter
    def cppmodel_CPPSequence130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPSequence__cppmodel_CPPSequence130", None)
        self.__cppmodel_CPPSequence130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPFormalParameter129"):
                opp_val = getattr(old_value, "cppmodel_CPPFormalParameter129", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPFormalParameter129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPFormalParameter129"):
                opp_val = getattr(value, "cppmodel_CPPFormalParameter129", None)
                setattr(value, "cppmodel_CPPFormalParameter129", self)

    @property
    def cppmodel_CPPSequence(self):
        return self.__cppmodel_CPPSequence

    @cppmodel_CPPSequence.setter
    def cppmodel_CPPSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPSequence__cppmodel_CPPSequence", None)
        self.__cppmodel_CPPSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPAttribute109"):
                opp_val = getattr(old_value, "cppmodel_CPPAttribute109", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPAttribute109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPAttribute109"):
                opp_val = getattr(value, "cppmodel_CPPAttribute109", None)
                setattr(value, "cppmodel_CPPAttribute109", self)

class cppmodel_Attribute:

    pass
class OOPLClassReference:

    pass
class cppmodel_XTProtocolOperationImplementation:

    pass
class OOPLClassRefSimpleCollection:

    pass
class OOPLClassReferenceStorage:

    pass
class cppmodel_Signal:

    pass
class cppmodel_XTProtocolOperationDefinition:

    pass
class OOPLRelation:

    pass
class cppmodel_XTPort:

    pass
class cppmodel_Snippet:

    pass
class cppmodel_Operation:

    pass
class cppmodel_CPPExternalHeader:

    def __init__(self, name: str, cppmodel_CPPExternalHeader: "cppmodel_CPPExternalHeaderInclusion" = None, cppmodel_CPPExternalHeader142: "cppmodel_CPPExternalLibrary" = None):
        self.name = name
        self.cppmodel_CPPExternalHeader = cppmodel_CPPExternalHeader
        self.cppmodel_CPPExternalHeader142 = cppmodel_CPPExternalHeader142
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cppmodel_CPPExternalHeader142(self):
        return self.__cppmodel_CPPExternalHeader142

    @cppmodel_CPPExternalHeader142.setter
    def cppmodel_CPPExternalHeader142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalHeader__cppmodel_CPPExternalHeader142", None)
        self.__cppmodel_CPPExternalHeader142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPExternalLibrary"):
                opp_val = getattr(old_value, "cppmodel_CPPExternalLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPExternalLibrary"):
                opp_val = getattr(value, "cppmodel_CPPExternalLibrary", None)
                if opp_val is None:
                    setattr(value, "cppmodel_CPPExternalLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cppmodel_CPPExternalHeader(self):
        return self.__cppmodel_CPPExternalHeader

    @cppmodel_CPPExternalHeader.setter
    def cppmodel_CPPExternalHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalHeader__cppmodel_CPPExternalHeader", None)
        self.__cppmodel_CPPExternalHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPExternalHeaderInclusion85"):
                opp_val = getattr(old_value, "cppmodel_CPPExternalHeaderInclusion85", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPExternalHeaderInclusion85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPExternalHeaderInclusion85"):
                opp_val = getattr(value, "cppmodel_CPPExternalHeaderInclusion85", None)
                setattr(value, "cppmodel_CPPExternalHeaderInclusion85", self)

class cppmodel_XTComponent:

    pass
class CPPSourceFile:

    pass
class cppmodel_CPPMakeFile(CPPSourceFile):

    pass
class cppmodel_CPPExternalHeaderInclusion:

    def __init__(self, comment: str, cppmodel_CPPExternalHeaderInclusion: "cppmodel_CPPSourceFile" = None, cppmodel_CPPExternalHeaderInclusion85: "cppmodel_CPPExternalHeader" = None):
        self.comment = comment
        self.cppmodel_CPPExternalHeaderInclusion = cppmodel_CPPExternalHeaderInclusion
        self.cppmodel_CPPExternalHeaderInclusion85 = cppmodel_CPPExternalHeaderInclusion85
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def cppmodel_CPPExternalHeaderInclusion85(self):
        return self.__cppmodel_CPPExternalHeaderInclusion85

    @cppmodel_CPPExternalHeaderInclusion85.setter
    def cppmodel_CPPExternalHeaderInclusion85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalHeaderInclusion__cppmodel_CPPExternalHeaderInclusion85", None)
        self.__cppmodel_CPPExternalHeaderInclusion85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPExternalHeader"):
                opp_val = getattr(old_value, "cppmodel_CPPExternalHeader", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPExternalHeader", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPExternalHeader"):
                opp_val = getattr(value, "cppmodel_CPPExternalHeader", None)
                setattr(value, "cppmodel_CPPExternalHeader", self)

    @property
    def cppmodel_CPPExternalHeaderInclusion(self):
        return self.__cppmodel_CPPExternalHeaderInclusion

    @cppmodel_CPPExternalHeaderInclusion.setter
    def cppmodel_CPPExternalHeaderInclusion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalHeaderInclusion__cppmodel_CPPExternalHeaderInclusion", None)
        self.__cppmodel_CPPExternalHeaderInclusion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPSourceFile50"):
                opp_val = getattr(old_value, "cppmodel_CPPSourceFile50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPSourceFile50"):
                opp_val = getattr(value, "cppmodel_CPPSourceFile50", None)
                if opp_val is None:
                    setattr(value, "cppmodel_CPPSourceFile50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OOPLClass:

    pass
class cppmodel_CPPSourceFile(ABC):

    def __init__(self, generationName: str, generationDirectory: str, generationPath: str, cppmodel_CPPSourceFile: set["cppmodel_CPPHeaderFile"] = None, cppmodel_CPPSourceFile50: set["cppmodel_CPPExternalHeaderInclusion"] = None, cppmodel_CPPSourceFile56: "cppmodel_CPPDirectory" = None):
        self.generationName = generationName
        self.generationDirectory = generationDirectory
        self.generationPath = generationPath
        self.cppmodel_CPPSourceFile = cppmodel_CPPSourceFile if cppmodel_CPPSourceFile is not None else set()
        self.cppmodel_CPPSourceFile50 = cppmodel_CPPSourceFile50 if cppmodel_CPPSourceFile50 is not None else set()
        self.cppmodel_CPPSourceFile56 = cppmodel_CPPSourceFile56
        
    @property
    def generationPath(self) -> str:
        return self.__generationPath

    @generationPath.setter
    def generationPath(self, generationPath: str):
        self.__generationPath = generationPath

    @property
    def generationName(self) -> str:
        return self.__generationName

    @generationName.setter
    def generationName(self, generationName: str):
        self.__generationName = generationName

    @property
    def generationDirectory(self) -> str:
        return self.__generationDirectory

    @generationDirectory.setter
    def generationDirectory(self, generationDirectory: str):
        self.__generationDirectory = generationDirectory

    @property
    def cppmodel_CPPSourceFile50(self):
        return self.__cppmodel_CPPSourceFile50

    @cppmodel_CPPSourceFile50.setter
    def cppmodel_CPPSourceFile50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPSourceFile__cppmodel_CPPSourceFile50", None)
        self.__cppmodel_CPPSourceFile50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cppmodel_CPPExternalHeaderInclusion"):
                    opp_val = getattr(item, "cppmodel_CPPExternalHeaderInclusion", None)
                    
                    if opp_val == self:
                        setattr(item, "cppmodel_CPPExternalHeaderInclusion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cppmodel_CPPExternalHeaderInclusion"):
                    opp_val = getattr(item, "cppmodel_CPPExternalHeaderInclusion", None)
                    
                    setattr(item, "cppmodel_CPPExternalHeaderInclusion", self)
                    

    @property
    def cppmodel_CPPSourceFile(self):
        return self.__cppmodel_CPPSourceFile

    @cppmodel_CPPSourceFile.setter
    def cppmodel_CPPSourceFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPSourceFile__cppmodel_CPPSourceFile", None)
        self.__cppmodel_CPPSourceFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cppmodel_CPPHeaderFile48"):
                    opp_val = getattr(item, "cppmodel_CPPHeaderFile48", None)
                    
                    if opp_val == self:
                        setattr(item, "cppmodel_CPPHeaderFile48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cppmodel_CPPHeaderFile48"):
                    opp_val = getattr(item, "cppmodel_CPPHeaderFile48", None)
                    
                    setattr(item, "cppmodel_CPPHeaderFile48", self)
                    

    @property
    def cppmodel_CPPSourceFile56(self):
        return self.__cppmodel_CPPSourceFile56

    @cppmodel_CPPSourceFile56.setter
    def cppmodel_CPPSourceFile56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPSourceFile__cppmodel_CPPSourceFile56", None)
        self.__cppmodel_CPPSourceFile56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPDirectory55"):
                opp_val = getattr(old_value, "cppmodel_CPPDirectory55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPDirectory55"):
                opp_val = getattr(value, "cppmodel_CPPDirectory55", None)
                if opp_val is None:
                    setattr(value, "cppmodel_CPPDirectory55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cppmodel_XTProtocol:

    pass
class cppmodel_Package:

    pass
class cppmodel_CPPBodyFile(CPPSourceFile):

    pass
class cppmodel_Model:

    pass
class CPPQualifiedNamedElement:

    pass
class cppmodel_CPPStructType(OOPLStructType, CPPQualifiedNamedElement):

    pass
class cppmodel_CPPFormalParameter(CPPQualifiedNamedElement):

    def __init__(self, passingMode: str, cppmodel_CPPFormalParameter: "cppmodel_Parameter" = None, cppmodel_CPPFormalParameter129: "cppmodel_CPPSequence" = None, cppmodel_CPPFormalParameter132: "cppmodel_OOPLDataType" = None):
        self.passingMode = passingMode
        self.cppmodel_CPPFormalParameter = cppmodel_CPPFormalParameter
        self.cppmodel_CPPFormalParameter129 = cppmodel_CPPFormalParameter129
        self.cppmodel_CPPFormalParameter132 = cppmodel_CPPFormalParameter132
        
    @property
    def passingMode(self) -> str:
        return self.__passingMode

    @passingMode.setter
    def passingMode(self, passingMode: str):
        self.__passingMode = passingMode

    @property
    def cppmodel_CPPFormalParameter132(self):
        return self.__cppmodel_CPPFormalParameter132

    @cppmodel_CPPFormalParameter132.setter
    def cppmodel_CPPFormalParameter132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPFormalParameter__cppmodel_CPPFormalParameter132", None)
        self.__cppmodel_CPPFormalParameter132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_OOPLDataType133"):
                opp_val = getattr(old_value, "cppmodel_OOPLDataType133", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_OOPLDataType133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_OOPLDataType133"):
                opp_val = getattr(value, "cppmodel_OOPLDataType133", None)
                setattr(value, "cppmodel_OOPLDataType133", self)

    @property
    def cppmodel_CPPFormalParameter(self):
        return self.__cppmodel_CPPFormalParameter

    @cppmodel_CPPFormalParameter.setter
    def cppmodel_CPPFormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPFormalParameter__cppmodel_CPPFormalParameter", None)
        self.__cppmodel_CPPFormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_Parameter"):
                opp_val = getattr(old_value, "cppmodel_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_Parameter"):
                opp_val = getattr(value, "cppmodel_Parameter", None)
                setattr(value, "cppmodel_Parameter", self)

    @property
    def cppmodel_CPPFormalParameter129(self):
        return self.__cppmodel_CPPFormalParameter129

    @cppmodel_CPPFormalParameter129.setter
    def cppmodel_CPPFormalParameter129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPFormalParameter__cppmodel_CPPFormalParameter129", None)
        self.__cppmodel_CPPFormalParameter129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPSequence130"):
                opp_val = getattr(old_value, "cppmodel_CPPSequence130", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPSequence130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPSequence130"):
                opp_val = getattr(value, "cppmodel_CPPSequence130", None)
                setattr(value, "cppmodel_CPPSequence130", self)

class cppmodel_CPPReturnValue(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPClassRefSimpleCollection(OOPLClassRefSimpleCollection, CPPQualifiedNamedElement):

    def __init__(self, cppContainer: str):
        self.cppContainer = cppContainer
        
    @property
    def cppContainer(self) -> str:
        return self.__cppContainer

    @cppContainer.setter
    def cppContainer(self, cppContainer: str):
        self.__cppContainer = cppContainer

class cppmodel_CPPProtocol(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPOperation(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPComponent(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPClass(CPPQualifiedNamedElement, OOPLClass):

    pass
class cppmodel_CPPEvent(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPState(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPProtocolOperationImplementation(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPClassReference(CPPQualifiedNamedElement, OOPLClassReference):

    pass
class cppmodel_CPPBasicType(OOPLBasicType, CPPQualifiedNamedElement):

    def __init__(self, cppSpecifier: str):
        self.cppSpecifier = cppSpecifier
        
    @property
    def cppSpecifier(self) -> str:
        return self.__cppSpecifier

    @cppSpecifier.setter
    def cppSpecifier(self, cppSpecifier: str):
        self.__cppSpecifier = cppSpecifier

class cppmodel_CPPProtocolOperationDefinition(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPTransition(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPStructMember(CPPQualifiedNamedElement, OOPLStructMember):

    pass
class cppmodel_CPPAttribute(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPEnumType(OOPLEnumType, CPPQualifiedNamedElement):

    pass
class cppmodel_CPPPort(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPSignal(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPRelation(CPPQualifiedNamedElement, OOPLRelation):

    pass
class cppmodel_CPPEnumerator(CPPQualifiedNamedElement, OOPLEnumerator):

    def __init__(self, cppValue: str):
        self.cppValue = cppValue
        
    @property
    def cppValue(self) -> str:
        return self.__cppValue

    @cppValue.setter
    def cppValue(self, cppValue: str):
        self.__cppValue = cppValue

class cppmodel_CPPPackage(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPUserDefinedType(CPPQualifiedNamedElement, OOPLUserDefinedType):

    pass
class cppmodel_CPPExternalBridge(CPPQualifiedNamedElement):

    def __init__(self, cppExternalNamespace: str, cppmodel_CPPExternalBridge: "cppmodel_CPPHeaderFile" = None, cppmodel_CPPExternalBridge146: "cppmodel_CPPBodyFile" = None, cppmodel_CPPExternalBridge149: "cppmodel_XTClass" = None):
        self.cppExternalNamespace = cppExternalNamespace
        self.cppmodel_CPPExternalBridge = cppmodel_CPPExternalBridge
        self.cppmodel_CPPExternalBridge146 = cppmodel_CPPExternalBridge146
        self.cppmodel_CPPExternalBridge149 = cppmodel_CPPExternalBridge149
        
    @property
    def cppExternalNamespace(self) -> str:
        return self.__cppExternalNamespace

    @cppExternalNamespace.setter
    def cppExternalNamespace(self, cppExternalNamespace: str):
        self.__cppExternalNamespace = cppExternalNamespace

    @property
    def cppmodel_CPPExternalBridge146(self):
        return self.__cppmodel_CPPExternalBridge146

    @cppmodel_CPPExternalBridge146.setter
    def cppmodel_CPPExternalBridge146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalBridge__cppmodel_CPPExternalBridge146", None)
        self.__cppmodel_CPPExternalBridge146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPBodyFile147"):
                opp_val = getattr(old_value, "cppmodel_CPPBodyFile147", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPBodyFile147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPBodyFile147"):
                opp_val = getattr(value, "cppmodel_CPPBodyFile147", None)
                setattr(value, "cppmodel_CPPBodyFile147", self)

    @property
    def cppmodel_CPPExternalBridge(self):
        return self.__cppmodel_CPPExternalBridge

    @cppmodel_CPPExternalBridge.setter
    def cppmodel_CPPExternalBridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalBridge__cppmodel_CPPExternalBridge", None)
        self.__cppmodel_CPPExternalBridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPHeaderFile144"):
                opp_val = getattr(old_value, "cppmodel_CPPHeaderFile144", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPHeaderFile144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPHeaderFile144"):
                opp_val = getattr(value, "cppmodel_CPPHeaderFile144", None)
                setattr(value, "cppmodel_CPPHeaderFile144", self)

    @property
    def cppmodel_CPPExternalBridge149(self):
        return self.__cppmodel_CPPExternalBridge149

    @cppmodel_CPPExternalBridge149.setter
    def cppmodel_CPPExternalBridge149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPExternalBridge__cppmodel_CPPExternalBridge149", None)
        self.__cppmodel_CPPExternalBridge149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_XTClass"):
                opp_val = getattr(old_value, "cppmodel_XTClass", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_XTClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_XTClass"):
                opp_val = getattr(value, "cppmodel_XTClass", None)
                setattr(value, "cppmodel_XTClass", self)

class cppmodel_CPPClassRefAssocCollection(CPPQualifiedNamedElement, OOPLClassRefAssocCollection):

    def __init__(self, cppContainer: str, cppmodel_CPPClassRefAssocCollection: "cppmodel_CPPAttribute" = None):
        self.cppContainer = cppContainer
        self.cppmodel_CPPClassRefAssocCollection = cppmodel_CPPClassRefAssocCollection
        
    @property
    def cppContainer(self) -> str:
        return self.__cppContainer

    @cppContainer.setter
    def cppContainer(self, cppContainer: str):
        self.__cppContainer = cppContainer

    @property
    def cppmodel_CPPClassRefAssocCollection(self):
        return self.__cppmodel_CPPClassRefAssocCollection

    @cppmodel_CPPClassRefAssocCollection.setter
    def cppmodel_CPPClassRefAssocCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPClassRefAssocCollection__cppmodel_CPPClassRefAssocCollection", None)
        self.__cppmodel_CPPClassRefAssocCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPAttribute"):
                opp_val = getattr(old_value, "cppmodel_CPPAttribute", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPAttribute"):
                opp_val = getattr(value, "cppmodel_CPPAttribute", None)
                setattr(value, "cppmodel_CPPAttribute", self)

class cppmodel_CPPClassReferenceStorage(CPPQualifiedNamedElement, OOPLClassReferenceStorage):

    pass
class cppmodel_CPPModel(CPPQualifiedNamedElement):

    pass
class cppmodel_CPPDirectory:

    def __init__(self, name: str, parentDirectory: str, path: str, cppmodel_CPPDirectory: "cppmodel_CPPModel" = None, cppmodel_CPPDirectory34: "cppmodel_CPPPackage" = None, cppmodel_CPPDirectory37: "cppmodel_CPPPackage" = None, cppmodel_CPPDirectory18: "cppmodel_CPPModel" = None, cppmodel_CPPDirectory21: "cppmodel_CPPModel" = None, cppmodel_CPPDirectory24: "cppmodel_CPPModel" = None, cppmodel_CPPDirectory53: "cppmodel_CPPDirectory" = None, cppmodel_CPPDirectory51: set["cppmodel_CPPDirectory"] = None, cppmodel_CPPDirectory55: set["cppmodel_CPPSourceFile"] = None, cppmodel_CPPDirectory58: "cppmodel_CPPMakeFile" = None, cppmodel_CPPDirectory77: "cppmodel_CPPComponent" = None, cppmodel_CPPDirectory80: "cppmodel_CPPComponent" = None, cppmodel_CPPDirectory83: "cppmodel_CPPComponent" = None, cppmodel_CPPDirectory74: "cppmodel_CPPComponent" = None):
        self.name = name
        self.parentDirectory = parentDirectory
        self.path = path
        self.cppmodel_CPPDirectory = cppmodel_CPPDirectory
        self.cppmodel_CPPDirectory34 = cppmodel_CPPDirectory34
        self.cppmodel_CPPDirectory37 = cppmodel_CPPDirectory37
        self.cppmodel_CPPDirectory18 = cppmodel_CPPDirectory18
        self.cppmodel_CPPDirectory21 = cppmodel_CPPDirectory21
        self.cppmodel_CPPDirectory24 = cppmodel_CPPDirectory24
        self.cppmodel_CPPDirectory53 = cppmodel_CPPDirectory53
        self.cppmodel_CPPDirectory51 = cppmodel_CPPDirectory51 if cppmodel_CPPDirectory51 is not None else set()
        self.cppmodel_CPPDirectory55 = cppmodel_CPPDirectory55 if cppmodel_CPPDirectory55 is not None else set()
        self.cppmodel_CPPDirectory58 = cppmodel_CPPDirectory58
        self.cppmodel_CPPDirectory77 = cppmodel_CPPDirectory77
        self.cppmodel_CPPDirectory80 = cppmodel_CPPDirectory80
        self.cppmodel_CPPDirectory83 = cppmodel_CPPDirectory83
        self.cppmodel_CPPDirectory74 = cppmodel_CPPDirectory74
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def parentDirectory(self) -> str:
        return self.__parentDirectory

    @parentDirectory.setter
    def parentDirectory(self, parentDirectory: str):
        self.__parentDirectory = parentDirectory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cppmodel_CPPDirectory21(self):
        return self.__cppmodel_CPPDirectory21

    @cppmodel_CPPDirectory21.setter
    def cppmodel_CPPDirectory21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory21", None)
        self.__cppmodel_CPPDirectory21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel20"):
                opp_val = getattr(old_value, "cppmodel_CPPModel20", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel20"):
                opp_val = getattr(value, "cppmodel_CPPModel20", None)
                setattr(value, "cppmodel_CPPModel20", self)

    @property
    def cppmodel_CPPDirectory77(self):
        return self.__cppmodel_CPPDirectory77

    @cppmodel_CPPDirectory77.setter
    def cppmodel_CPPDirectory77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory77", None)
        self.__cppmodel_CPPDirectory77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent76"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent76", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent76"):
                opp_val = getattr(value, "cppmodel_CPPComponent76", None)
                setattr(value, "cppmodel_CPPComponent76", self)

    @property
    def cppmodel_CPPDirectory55(self):
        return self.__cppmodel_CPPDirectory55

    @cppmodel_CPPDirectory55.setter
    def cppmodel_CPPDirectory55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory55", None)
        self.__cppmodel_CPPDirectory55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cppmodel_CPPSourceFile56"):
                    opp_val = getattr(item, "cppmodel_CPPSourceFile56", None)
                    
                    if opp_val == self:
                        setattr(item, "cppmodel_CPPSourceFile56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cppmodel_CPPSourceFile56"):
                    opp_val = getattr(item, "cppmodel_CPPSourceFile56", None)
                    
                    setattr(item, "cppmodel_CPPSourceFile56", self)
                    

    @property
    def cppmodel_CPPDirectory(self):
        return self.__cppmodel_CPPDirectory

    @cppmodel_CPPDirectory.setter
    def cppmodel_CPPDirectory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory", None)
        self.__cppmodel_CPPDirectory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel15"):
                opp_val = getattr(old_value, "cppmodel_CPPModel15", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel15"):
                opp_val = getattr(value, "cppmodel_CPPModel15", None)
                setattr(value, "cppmodel_CPPModel15", self)

    @property
    def cppmodel_CPPDirectory58(self):
        return self.__cppmodel_CPPDirectory58

    @cppmodel_CPPDirectory58.setter
    def cppmodel_CPPDirectory58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory58", None)
        self.__cppmodel_CPPDirectory58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPMakeFile"):
                opp_val = getattr(old_value, "cppmodel_CPPMakeFile", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPMakeFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPMakeFile"):
                opp_val = getattr(value, "cppmodel_CPPMakeFile", None)
                setattr(value, "cppmodel_CPPMakeFile", self)

    @property
    def cppmodel_CPPDirectory24(self):
        return self.__cppmodel_CPPDirectory24

    @cppmodel_CPPDirectory24.setter
    def cppmodel_CPPDirectory24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory24", None)
        self.__cppmodel_CPPDirectory24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel23"):
                opp_val = getattr(old_value, "cppmodel_CPPModel23", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel23"):
                opp_val = getattr(value, "cppmodel_CPPModel23", None)
                setattr(value, "cppmodel_CPPModel23", self)

    @property
    def cppmodel_CPPDirectory37(self):
        return self.__cppmodel_CPPDirectory37

    @cppmodel_CPPDirectory37.setter
    def cppmodel_CPPDirectory37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory37", None)
        self.__cppmodel_CPPDirectory37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPPackage36"):
                opp_val = getattr(old_value, "cppmodel_CPPPackage36", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPPackage36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPPackage36"):
                opp_val = getattr(value, "cppmodel_CPPPackage36", None)
                setattr(value, "cppmodel_CPPPackage36", self)

    @property
    def cppmodel_CPPDirectory80(self):
        return self.__cppmodel_CPPDirectory80

    @cppmodel_CPPDirectory80.setter
    def cppmodel_CPPDirectory80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory80", None)
        self.__cppmodel_CPPDirectory80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent79"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent79", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent79"):
                opp_val = getattr(value, "cppmodel_CPPComponent79", None)
                setattr(value, "cppmodel_CPPComponent79", self)

    @property
    def cppmodel_CPPDirectory83(self):
        return self.__cppmodel_CPPDirectory83

    @cppmodel_CPPDirectory83.setter
    def cppmodel_CPPDirectory83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory83", None)
        self.__cppmodel_CPPDirectory83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent82"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent82", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent82"):
                opp_val = getattr(value, "cppmodel_CPPComponent82", None)
                setattr(value, "cppmodel_CPPComponent82", self)

    @property
    def cppmodel_CPPDirectory74(self):
        return self.__cppmodel_CPPDirectory74

    @cppmodel_CPPDirectory74.setter
    def cppmodel_CPPDirectory74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory74", None)
        self.__cppmodel_CPPDirectory74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent73"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent73", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent73"):
                opp_val = getattr(value, "cppmodel_CPPComponent73", None)
                setattr(value, "cppmodel_CPPComponent73", self)

    @property
    def cppmodel_CPPDirectory34(self):
        return self.__cppmodel_CPPDirectory34

    @cppmodel_CPPDirectory34.setter
    def cppmodel_CPPDirectory34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory34", None)
        self.__cppmodel_CPPDirectory34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPPackage33"):
                opp_val = getattr(old_value, "cppmodel_CPPPackage33", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPPackage33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPPackage33"):
                opp_val = getattr(value, "cppmodel_CPPPackage33", None)
                setattr(value, "cppmodel_CPPPackage33", self)

    @property
    def cppmodel_CPPDirectory51(self):
        return self.__cppmodel_CPPDirectory51

    @cppmodel_CPPDirectory51.setter
    def cppmodel_CPPDirectory51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory51", None)
        self.__cppmodel_CPPDirectory51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cppmodel_CPPDirectory53"):
                    opp_val = getattr(item, "cppmodel_CPPDirectory53", None)
                    
                    if opp_val == self:
                        setattr(item, "cppmodel_CPPDirectory53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cppmodel_CPPDirectory53"):
                    opp_val = getattr(item, "cppmodel_CPPDirectory53", None)
                    
                    setattr(item, "cppmodel_CPPDirectory53", self)
                    

    @property
    def cppmodel_CPPDirectory53(self):
        return self.__cppmodel_CPPDirectory53

    @cppmodel_CPPDirectory53.setter
    def cppmodel_CPPDirectory53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory53", None)
        self.__cppmodel_CPPDirectory53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPDirectory51"):
                opp_val = getattr(old_value, "cppmodel_CPPDirectory51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPDirectory51"):
                opp_val = getattr(value, "cppmodel_CPPDirectory51", None)
                if opp_val is None:
                    setattr(value, "cppmodel_CPPDirectory51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cppmodel_CPPDirectory18(self):
        return self.__cppmodel_CPPDirectory18

    @cppmodel_CPPDirectory18.setter
    def cppmodel_CPPDirectory18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPDirectory__cppmodel_CPPDirectory18", None)
        self.__cppmodel_CPPDirectory18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel17"):
                opp_val = getattr(old_value, "cppmodel_CPPModel17", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel17"):
                opp_val = getattr(value, "cppmodel_CPPModel17", None)
                setattr(value, "cppmodel_CPPModel17", self)

class cppmodel_CPPHeaderFile(CPPSourceFile):

    def __init__(self, includeName: str, includeDirectory: str, includePath: str, cppmodel_CPPHeaderFile: "cppmodel_CPPModel" = None, cppmodel_CPPHeaderFile10: "cppmodel_CPPModel" = None, cppmodel_CPPHeaderFile13: "cppmodel_CPPModel" = None, cppmodel_CPPHeaderFile31: "cppmodel_CPPPackage" = None, cppmodel_CPPHeaderFile46: "cppmodel_CPPProtocol" = None, cppmodel_CPPHeaderFile39: "cppmodel_CPPClass" = None, cppmodel_CPPHeaderFile48: "cppmodel_CPPSourceFile" = None, cppmodel_CPPHeaderFile62: "cppmodel_CPPComponent" = None, cppmodel_CPPHeaderFile68: "cppmodel_CPPComponent" = None, cppmodel_CPPHeaderFile71: "cppmodel_CPPComponent" = None, cppmodel_CPPHeaderFile92: "cppmodel_CPPPort" = None, cppmodel_CPPHeaderFile95: "cppmodel_CPPPort" = None, cppmodel_CPPHeaderFile144: "cppmodel_CPPExternalBridge" = None):
        self.includeName = includeName
        self.includeDirectory = includeDirectory
        self.includePath = includePath
        self.cppmodel_CPPHeaderFile = cppmodel_CPPHeaderFile
        self.cppmodel_CPPHeaderFile10 = cppmodel_CPPHeaderFile10
        self.cppmodel_CPPHeaderFile13 = cppmodel_CPPHeaderFile13
        self.cppmodel_CPPHeaderFile31 = cppmodel_CPPHeaderFile31
        self.cppmodel_CPPHeaderFile46 = cppmodel_CPPHeaderFile46
        self.cppmodel_CPPHeaderFile39 = cppmodel_CPPHeaderFile39
        self.cppmodel_CPPHeaderFile48 = cppmodel_CPPHeaderFile48
        self.cppmodel_CPPHeaderFile62 = cppmodel_CPPHeaderFile62
        self.cppmodel_CPPHeaderFile68 = cppmodel_CPPHeaderFile68
        self.cppmodel_CPPHeaderFile71 = cppmodel_CPPHeaderFile71
        self.cppmodel_CPPHeaderFile92 = cppmodel_CPPHeaderFile92
        self.cppmodel_CPPHeaderFile95 = cppmodel_CPPHeaderFile95
        self.cppmodel_CPPHeaderFile144 = cppmodel_CPPHeaderFile144
        
    @property
    def includePath(self) -> str:
        return self.__includePath

    @includePath.setter
    def includePath(self, includePath: str):
        self.__includePath = includePath

    @property
    def includeDirectory(self) -> str:
        return self.__includeDirectory

    @includeDirectory.setter
    def includeDirectory(self, includeDirectory: str):
        self.__includeDirectory = includeDirectory

    @property
    def includeName(self) -> str:
        return self.__includeName

    @includeName.setter
    def includeName(self, includeName: str):
        self.__includeName = includeName

    @property
    def cppmodel_CPPHeaderFile48(self):
        return self.__cppmodel_CPPHeaderFile48

    @cppmodel_CPPHeaderFile48.setter
    def cppmodel_CPPHeaderFile48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile48", None)
        self.__cppmodel_CPPHeaderFile48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPSourceFile"):
                opp_val = getattr(old_value, "cppmodel_CPPSourceFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPSourceFile"):
                opp_val = getattr(value, "cppmodel_CPPSourceFile", None)
                if opp_val is None:
                    setattr(value, "cppmodel_CPPSourceFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cppmodel_CPPHeaderFile46(self):
        return self.__cppmodel_CPPHeaderFile46

    @cppmodel_CPPHeaderFile46.setter
    def cppmodel_CPPHeaderFile46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile46", None)
        self.__cppmodel_CPPHeaderFile46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPProtocol45"):
                opp_val = getattr(old_value, "cppmodel_CPPProtocol45", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPProtocol45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPProtocol45"):
                opp_val = getattr(value, "cppmodel_CPPProtocol45", None)
                setattr(value, "cppmodel_CPPProtocol45", self)

    @property
    def cppmodel_CPPHeaderFile31(self):
        return self.__cppmodel_CPPHeaderFile31

    @cppmodel_CPPHeaderFile31.setter
    def cppmodel_CPPHeaderFile31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile31", None)
        self.__cppmodel_CPPHeaderFile31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPPackage30"):
                opp_val = getattr(old_value, "cppmodel_CPPPackage30", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPPackage30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPPackage30"):
                opp_val = getattr(value, "cppmodel_CPPPackage30", None)
                setattr(value, "cppmodel_CPPPackage30", self)

    @property
    def cppmodel_CPPHeaderFile39(self):
        return self.__cppmodel_CPPHeaderFile39

    @cppmodel_CPPHeaderFile39.setter
    def cppmodel_CPPHeaderFile39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile39", None)
        self.__cppmodel_CPPHeaderFile39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPClass"):
                opp_val = getattr(old_value, "cppmodel_CPPClass", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPClass"):
                opp_val = getattr(value, "cppmodel_CPPClass", None)
                setattr(value, "cppmodel_CPPClass", self)

    @property
    def cppmodel_CPPHeaderFile95(self):
        return self.__cppmodel_CPPHeaderFile95

    @cppmodel_CPPHeaderFile95.setter
    def cppmodel_CPPHeaderFile95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile95", None)
        self.__cppmodel_CPPHeaderFile95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPPort94"):
                opp_val = getattr(old_value, "cppmodel_CPPPort94", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPPort94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPPort94"):
                opp_val = getattr(value, "cppmodel_CPPPort94", None)
                setattr(value, "cppmodel_CPPPort94", self)

    @property
    def cppmodel_CPPHeaderFile10(self):
        return self.__cppmodel_CPPHeaderFile10

    @cppmodel_CPPHeaderFile10.setter
    def cppmodel_CPPHeaderFile10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile10", None)
        self.__cppmodel_CPPHeaderFile10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel9"):
                opp_val = getattr(old_value, "cppmodel_CPPModel9", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel9"):
                opp_val = getattr(value, "cppmodel_CPPModel9", None)
                setattr(value, "cppmodel_CPPModel9", self)

    @property
    def cppmodel_CPPHeaderFile144(self):
        return self.__cppmodel_CPPHeaderFile144

    @cppmodel_CPPHeaderFile144.setter
    def cppmodel_CPPHeaderFile144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile144", None)
        self.__cppmodel_CPPHeaderFile144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPExternalBridge"):
                opp_val = getattr(old_value, "cppmodel_CPPExternalBridge", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPExternalBridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPExternalBridge"):
                opp_val = getattr(value, "cppmodel_CPPExternalBridge", None)
                setattr(value, "cppmodel_CPPExternalBridge", self)

    @property
    def cppmodel_CPPHeaderFile71(self):
        return self.__cppmodel_CPPHeaderFile71

    @cppmodel_CPPHeaderFile71.setter
    def cppmodel_CPPHeaderFile71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile71", None)
        self.__cppmodel_CPPHeaderFile71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent70"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent70", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent70"):
                opp_val = getattr(value, "cppmodel_CPPComponent70", None)
                setattr(value, "cppmodel_CPPComponent70", self)

    @property
    def cppmodel_CPPHeaderFile62(self):
        return self.__cppmodel_CPPHeaderFile62

    @cppmodel_CPPHeaderFile62.setter
    def cppmodel_CPPHeaderFile62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile62", None)
        self.__cppmodel_CPPHeaderFile62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent61"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent61", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent61"):
                opp_val = getattr(value, "cppmodel_CPPComponent61", None)
                setattr(value, "cppmodel_CPPComponent61", self)

    @property
    def cppmodel_CPPHeaderFile68(self):
        return self.__cppmodel_CPPHeaderFile68

    @cppmodel_CPPHeaderFile68.setter
    def cppmodel_CPPHeaderFile68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile68", None)
        self.__cppmodel_CPPHeaderFile68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPComponent67"):
                opp_val = getattr(old_value, "cppmodel_CPPComponent67", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPComponent67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPComponent67"):
                opp_val = getattr(value, "cppmodel_CPPComponent67", None)
                setattr(value, "cppmodel_CPPComponent67", self)

    @property
    def cppmodel_CPPHeaderFile13(self):
        return self.__cppmodel_CPPHeaderFile13

    @cppmodel_CPPHeaderFile13.setter
    def cppmodel_CPPHeaderFile13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile13", None)
        self.__cppmodel_CPPHeaderFile13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel12"):
                opp_val = getattr(old_value, "cppmodel_CPPModel12", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel12"):
                opp_val = getattr(value, "cppmodel_CPPModel12", None)
                setattr(value, "cppmodel_CPPModel12", self)

    @property
    def cppmodel_CPPHeaderFile92(self):
        return self.__cppmodel_CPPHeaderFile92

    @cppmodel_CPPHeaderFile92.setter
    def cppmodel_CPPHeaderFile92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile92", None)
        self.__cppmodel_CPPHeaderFile92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPPort91"):
                opp_val = getattr(old_value, "cppmodel_CPPPort91", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPPort91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPPort91"):
                opp_val = getattr(value, "cppmodel_CPPPort91", None)
                setattr(value, "cppmodel_CPPPort91", self)

    @property
    def cppmodel_CPPHeaderFile(self):
        return self.__cppmodel_CPPHeaderFile

    @cppmodel_CPPHeaderFile.setter
    def cppmodel_CPPHeaderFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPHeaderFile__cppmodel_CPPHeaderFile", None)
        self.__cppmodel_CPPHeaderFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPModel7"):
                opp_val = getattr(old_value, "cppmodel_CPPModel7", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_CPPModel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPModel7"):
                opp_val = getattr(value, "cppmodel_CPPModel7", None)
                setattr(value, "cppmodel_CPPModel7", self)

class CPPNamedElement:

    pass
class cppmodel_CPPQualifiedNamedElement(CPPNamedElement):

    def __init__(self, cppPrefix: str, cppQualifiedName: str, cppmodel_CPPQualifiedNamedElement: "cppmodel_CPPQualifiedNamedElement" = None, cppmodel_CPPQualifiedNamedElement1: set["cppmodel_CPPQualifiedNamedElement"] = None):
        self.cppPrefix = cppPrefix
        self.cppQualifiedName = cppQualifiedName
        self.cppmodel_CPPQualifiedNamedElement = cppmodel_CPPQualifiedNamedElement
        self.cppmodel_CPPQualifiedNamedElement1 = cppmodel_CPPQualifiedNamedElement1 if cppmodel_CPPQualifiedNamedElement1 is not None else set()
        
    @property
    def cppPrefix(self) -> str:
        return self.__cppPrefix

    @cppPrefix.setter
    def cppPrefix(self, cppPrefix: str):
        self.__cppPrefix = cppPrefix

    @property
    def cppQualifiedName(self) -> str:
        return self.__cppQualifiedName

    @cppQualifiedName.setter
    def cppQualifiedName(self, cppQualifiedName: str):
        self.__cppQualifiedName = cppQualifiedName

    @property
    def cppmodel_CPPQualifiedNamedElement1(self):
        return self.__cppmodel_CPPQualifiedNamedElement1

    @cppmodel_CPPQualifiedNamedElement1.setter
    def cppmodel_CPPQualifiedNamedElement1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPQualifiedNamedElement__cppmodel_CPPQualifiedNamedElement1", None)
        self.__cppmodel_CPPQualifiedNamedElement1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cppmodel_CPPQualifiedNamedElement"):
                    opp_val = getattr(item, "cppmodel_CPPQualifiedNamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "cppmodel_CPPQualifiedNamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cppmodel_CPPQualifiedNamedElement"):
                    opp_val = getattr(item, "cppmodel_CPPQualifiedNamedElement", None)
                    
                    setattr(item, "cppmodel_CPPQualifiedNamedElement", self)
                    

    @property
    def cppmodel_CPPQualifiedNamedElement(self):
        return self.__cppmodel_CPPQualifiedNamedElement

    @cppmodel_CPPQualifiedNamedElement.setter
    def cppmodel_CPPQualifiedNamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPQualifiedNamedElement__cppmodel_CPPQualifiedNamedElement", None)
        self.__cppmodel_CPPQualifiedNamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_CPPQualifiedNamedElement1"):
                opp_val = getattr(old_value, "cppmodel_CPPQualifiedNamedElement1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_CPPQualifiedNamedElement1"):
                opp_val = getattr(value, "cppmodel_CPPQualifiedNamedElement1", None)
                if opp_val is None:
                    setattr(value, "cppmodel_CPPQualifiedNamedElement1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cppmodel_OOPLNameProvider:

    pass
class cppmodel_CPPNamedElement(ABC):

    def __init__(self, cppName: str, cppmodel_CPPNamedElement: "cppmodel_OOPLNameProvider" = None):
        self.cppName = cppName
        self.cppmodel_CPPNamedElement = cppmodel_CPPNamedElement
        
    @property
    def cppName(self) -> str:
        return self.__cppName

    @cppName.setter
    def cppName(self, cppName: str):
        self.__cppName = cppName

    @property
    def cppmodel_CPPNamedElement(self):
        return self.__cppmodel_CPPNamedElement

    @cppmodel_CPPNamedElement.setter
    def cppmodel_CPPNamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cppmodel_CPPNamedElement__cppmodel_CPPNamedElement", None)
        self.__cppmodel_CPPNamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cppmodel_OOPLNameProvider"):
                opp_val = getattr(old_value, "cppmodel_OOPLNameProvider", None)
                if opp_val == self:
                    setattr(old_value, "cppmodel_OOPLNameProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cppmodel_OOPLNameProvider"):
                opp_val = getattr(value, "cppmodel_OOPLNameProvider", None)
                setattr(value, "cppmodel_OOPLNameProvider", self)
