from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class JvmVisibility(Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"


############################################
# Definition of Classes
############################################

class ElseIfCondition:

    pass
class ElseStart:

    pass
class RichStringIf:

    pass
class IfConditionStart:

    pass
class EndIf:

    pass
class ForLoopEnd:

    pass
class RichStringForLoop:

    pass
class Literal:

    pass
class model_richstring_LineBreak(Literal):

    pass
class ForLoopStart:

    pass
class model_richstring_Line:

    pass
class Line:

    pass
class RichStringLiteral:

    pass
class model_richstring_LinePart:

    pass
class ProcessedRichString:

    pass
class LinePart:

    pass
class model_richstring_ForLoopStart(LinePart):

    pass
class model_richstring_ElseIfCondition(LinePart):

    pass
class model_richstring_Literal(LinePart):

    def __init__(self, offset: int, length: int, model_richstring_Literal: "RichStringLiteral" = None, richstring418: "model_richstring_Line"):
        self.offset = offset
        self.length = length
        self.model_richstring_Literal = model_richstring_Literal
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def offset(self) -> int:
        return self.__offset

    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset

    @property
    def model_richstring_Literal(self):
        return self.__model_richstring_Literal

    @model_richstring_Literal.setter
    def model_richstring_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_richstring_Literal__model_richstring_Literal", None)
        self.__model_richstring_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RichStringLiteral"):
                opp_val = getattr(old_value, "RichStringLiteral", None)
                if opp_val == self:
                    setattr(old_value, "RichStringLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RichStringLiteral"):
                opp_val = getattr(value, "RichStringLiteral", None)
                setattr(value, "RichStringLiteral", self)

class model_richstring_ElseStart(LinePart):

    pass
class model_richstring_EndIf(LinePart):

    pass
class model_richstring_ForLoopEnd(LinePart):

    pass
class model_richstring_IfConditionStart(LinePart):

    pass
class model_richstring_PrintedExpression(LinePart):

    pass
class XExportDeclaration:

    pass
class model_xtype_XExportSection:

    pass
class RichString:

    pass
class model_richstring_ProcessedRichString:

    pass
class model_xtype_XExportItem:

    def __init__(self, alias: str, model_xtype_XExportItem: "JvmIdentifiableElement" = None):
        self.alias = alias
        self.model_xtype_XExportItem = model_xtype_XExportItem
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def model_xtype_XExportItem(self):
        return self.__model_xtype_XExportItem

    @model_xtype_XExportItem.setter
    def model_xtype_XExportItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XExportItem__model_xtype_XExportItem", None)
        self.__model_xtype_XExportItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmIdentifiableElement414"):
                opp_val = getattr(old_value, "JvmIdentifiableElement414", None)
                if opp_val == self:
                    setattr(old_value, "JvmIdentifiableElement414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmIdentifiableElement414"):
                opp_val = getattr(value, "JvmIdentifiableElement414", None)
                setattr(value, "JvmIdentifiableElement414", self)

class XExportItem:

    pass
class model_xtype_XExportDeclaration:

    def __init__(self, alias: str, wildcard: bool, importURI: str, model_xtype_XExportDeclaration: set["XExportItem"] = None):
        self.alias = alias
        self.wildcard = wildcard
        self.importURI = importURI
        self.model_xtype_XExportDeclaration = model_xtype_XExportDeclaration if model_xtype_XExportDeclaration is not None else set()
        
    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def wildcard(self) -> bool:
        return self.__wildcard

    @wildcard.setter
    def wildcard(self, wildcard: bool):
        self.__wildcard = wildcard

    @property
    def model_xtype_XExportDeclaration(self):
        return self.__model_xtype_XExportDeclaration

    @model_xtype_XExportDeclaration.setter
    def model_xtype_XExportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XExportDeclaration__model_xtype_XExportDeclaration", None)
        self.__model_xtype_XExportDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExportItem"):
                    opp_val = getattr(item, "XExportItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XExportItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExportItem"):
                    opp_val = getattr(item, "XExportItem", None)
                    
                    setattr(item, "XExportItem", self)
                    

class model_xtype_XImportDeclaration:

    def __init__(self, importedNamespace: str, wildcard: bool, extension: bool, static: bool, model_xtype_XImportDeclaration: "JvmDeclaredType" = None):
        self.importedNamespace = importedNamespace
        self.wildcard = wildcard
        self.extension = extension
        self.static = static
        self.model_xtype_XImportDeclaration = model_xtype_XImportDeclaration
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def wildcard(self) -> bool:
        return self.__wildcard

    @wildcard.setter
    def wildcard(self, wildcard: bool):
        self.__wildcard = wildcard

    @property
    def extension(self) -> bool:
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension

    @property
    def model_xtype_XImportDeclaration(self):
        return self.__model_xtype_XImportDeclaration

    @model_xtype_XImportDeclaration.setter
    def model_xtype_XImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XImportDeclaration__model_xtype_XImportDeclaration", None)
        self.__model_xtype_XImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmDeclaredType406"):
                opp_val = getattr(old_value, "JvmDeclaredType406", None)
                if opp_val == self:
                    setattr(old_value, "JvmDeclaredType406", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmDeclaredType406"):
                opp_val = getattr(value, "JvmDeclaredType406", None)
                setattr(value, "JvmDeclaredType406", self)

    def getImportedTypeName(self) -> str:
        # TODO: Implement getImportedTypeName method
        pass

class XImportDeclaration:

    pass
class model_xtype_XImportItem:

    def __init__(self, alias: str, model_xtype_XImportItem: "JvmIdentifiableElement" = None):
        self.alias = alias
        self.model_xtype_XImportItem = model_xtype_XImportItem
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def model_xtype_XImportItem(self):
        return self.__model_xtype_XImportItem

    @model_xtype_XImportItem.setter
    def model_xtype_XImportItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XImportItem__model_xtype_XImportItem", None)
        self.__model_xtype_XImportItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmIdentifiableElement410"):
                opp_val = getattr(old_value, "JvmIdentifiableElement410", None)
                if opp_val == self:
                    setattr(old_value, "JvmIdentifiableElement410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmIdentifiableElement410"):
                opp_val = getattr(value, "JvmIdentifiableElement410", None)
                setattr(value, "JvmIdentifiableElement410", self)

class XImportItem:

    pass
class model_xtype_XImportDeclaration1:

    def __init__(self, alias: str, importURI: str, model_xtype_XImportDeclaration1: set["XImportItem"] = None):
        self.alias = alias
        self.importURI = importURI
        self.model_xtype_XImportDeclaration1 = model_xtype_XImportDeclaration1 if model_xtype_XImportDeclaration1 is not None else set()
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def model_xtype_XImportDeclaration1(self):
        return self.__model_xtype_XImportDeclaration1

    @model_xtype_XImportDeclaration1.setter
    def model_xtype_XImportDeclaration1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XImportDeclaration1__model_xtype_XImportDeclaration1", None)
        self.__model_xtype_XImportDeclaration1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XImportItem"):
                    opp_val = getattr(item, "XImportItem", None)
                    
                    if opp_val == self:
                        setattr(item, "XImportItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XImportItem"):
                    opp_val = getattr(item, "XImportItem", None)
                    
                    setattr(item, "XImportItem", self)
                    

    def isWildcard(self) -> bool:
        # TODO: Implement isWildcard method
        pass

class XImportDeclaration1:

    pass
class model_xtype_XImportSection1:

    pass
class JvmSpecializedTypeReference:

    pass
class model_xtype_XFunctionTypeRef(JvmSpecializedTypeReference):

    def __init__(self, instanceContext: bool, model_xtype_XFunctionTypeRef: set["JvmTypeReference"] = None, model_xtype_XFunctionTypeRef399: "JvmTypeReference" = None, model_xtype_XFunctionTypeRef402: "JvmType" = None):
        self.instanceContext = instanceContext
        self.model_xtype_XFunctionTypeRef = model_xtype_XFunctionTypeRef if model_xtype_XFunctionTypeRef is not None else set()
        self.model_xtype_XFunctionTypeRef399 = model_xtype_XFunctionTypeRef399
        self.model_xtype_XFunctionTypeRef402 = model_xtype_XFunctionTypeRef402
        
    @property
    def instanceContext(self) -> bool:
        return self.__instanceContext

    @instanceContext.setter
    def instanceContext(self, instanceContext: bool):
        self.__instanceContext = instanceContext

    @property
    def model_xtype_XFunctionTypeRef(self):
        return self.__model_xtype_XFunctionTypeRef

    @model_xtype_XFunctionTypeRef.setter
    def model_xtype_XFunctionTypeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XFunctionTypeRef__model_xtype_XFunctionTypeRef", None)
        self.__model_xtype_XFunctionTypeRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference397"):
                    opp_val = getattr(item, "JvmTypeReference397", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference397", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference397"):
                    opp_val = getattr(item, "JvmTypeReference397", None)
                    
                    setattr(item, "JvmTypeReference397", self)
                    

    @property
    def model_xtype_XFunctionTypeRef402(self):
        return self.__model_xtype_XFunctionTypeRef402

    @model_xtype_XFunctionTypeRef402.setter
    def model_xtype_XFunctionTypeRef402(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XFunctionTypeRef__model_xtype_XFunctionTypeRef402", None)
        self.__model_xtype_XFunctionTypeRef402 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmType403"):
                opp_val = getattr(old_value, "JvmType403", None)
                if opp_val == self:
                    setattr(old_value, "JvmType403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmType403"):
                opp_val = getattr(value, "JvmType403", None)
                setattr(value, "JvmType403", self)

    @property
    def model_xtype_XFunctionTypeRef399(self):
        return self.__model_xtype_XFunctionTypeRef399

    @model_xtype_XFunctionTypeRef399.setter
    def model_xtype_XFunctionTypeRef399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XFunctionTypeRef__model_xtype_XFunctionTypeRef399", None)
        self.__model_xtype_XFunctionTypeRef399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference400"):
                opp_val = getattr(old_value, "JvmTypeReference400", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference400"):
                opp_val = getattr(value, "JvmTypeReference400", None)
                setattr(value, "JvmTypeReference400", self)

class model_xtype_XImportSection:

    pass
class model_xtype_XComputedTypeReference(JvmSpecializedTypeReference):

    def __init__(self, typeProvider: str):
        self.typeProvider = typeProvider
        
    @property
    def typeProvider(self) -> str:
        return self.__typeProvider

    @typeProvider.setter
    def typeProvider(self, typeProvider: str):
        self.__typeProvider = typeProvider

class model_xannotation_XAnnotationElementValuePair:

    pass
class XAnnotationElementValuePair:

    pass
class XVariableDeclaration:

    pass
class model_ss_XtendVariableDeclaration(XVariableDeclaration):

    def __init__(self, extension: bool):
        self.extension = extension
        
    @property
    def extension(self) -> bool:
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension

class model_ss_CreateExtensionInfo:

    def __init__(self, name: str, model_ss_CreateExtensionInfo: "XExpression" = None):
        self.name = name
        self.model_ss_CreateExtensionInfo = model_ss_CreateExtensionInfo
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ss_CreateExtensionInfo(self):
        return self.__model_ss_CreateExtensionInfo

    @model_ss_CreateExtensionInfo.setter
    def model_ss_CreateExtensionInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_CreateExtensionInfo__model_ss_CreateExtensionInfo", None)
        self.__model_ss_CreateExtensionInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression349"):
                opp_val = getattr(old_value, "XExpression349", None)
                if opp_val == self:
                    setattr(old_value, "XExpression349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression349"):
                opp_val = getattr(value, "XExpression349", None)
                setattr(value, "XExpression349", self)

class RichStringElseIf:

    pass
class model_ss_RichStringElseIf:

    pass
class XForEachExpression:

    pass
class model_ss_RichStringForLoop(XForEachExpression):

    pass
class XStringLiteral:

    pass
class model_ss_RichStringLiteral(XStringLiteral):

    pass
class XBlockExpression:

    pass
class model_ss_RichString(XBlockExpression):

    pass
class CreateExtensionInfo:

    pass
class XtendParameter:

    pass
class XtendMember:

    pass
class model_ss_XtendEnumLiteral(XtendMember):

    def __init__(self, name: str, ss362: "model_ss_XtendTypeDeclaration"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_ss_XtendField(XtendMember):

    def __init__(self, name: str, model_ss_XtendField: "JvmTypeReference" = None, model_ss_XtendField321: "XExpression" = None, ss362: "model_ss_XtendTypeDeclaration"):
        self.name = name
        self.model_ss_XtendField = model_ss_XtendField
        self.model_ss_XtendField321 = model_ss_XtendField321
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ss_XtendField321(self):
        return self.__model_ss_XtendField321

    @model_ss_XtendField321.setter
    def model_ss_XtendField321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendField__model_ss_XtendField321", None)
        self.__model_ss_XtendField321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression322"):
                opp_val = getattr(old_value, "XExpression322", None)
                if opp_val == self:
                    setattr(old_value, "XExpression322", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression322"):
                opp_val = getattr(value, "XExpression322", None)
                setattr(value, "XExpression322", self)

    @property
    def model_ss_XtendField(self):
        return self.__model_ss_XtendField

    @model_ss_XtendField.setter
    def model_ss_XtendField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendField__model_ss_XtendField", None)
        self.__model_ss_XtendField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference319"):
                opp_val = getattr(old_value, "JvmTypeReference319", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference319"):
                opp_val = getattr(value, "JvmTypeReference319", None)
                setattr(value, "JvmTypeReference319", self)

    def isExtension(self) -> bool:
        # TODO: Implement isExtension method
        pass

class model_ss_XtendTypeDeclaration(XtendMember):

    def __init__(self, name: str, XtendMember: set["XtendMember"] = None, ss362: "model_ss_XtendTypeDeclaration"):
        self.name = name
        self.XtendMember = XtendMember if XtendMember is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def XtendMember(self):
        return self.__XtendMember

    @XtendMember.setter
    def XtendMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendTypeDeclaration__XtendMember", None)
        self.__XtendMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ss362"):
                    opp_val = getattr(item, "ss362", None)
                    
                    if opp_val == self:
                        setattr(item, "ss362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ss362"):
                    opp_val = getattr(item, "ss362", None)
                    
                    setattr(item, "ss362", self)
                    

class model_ss_XtendEvent(XtendMember):

    def __init__(self, name: str, model_ss_XtendEvent: "JvmTypeReference" = None, model_ss_XtendEvent382: "XExpression" = None, ss362: "model_ss_XtendTypeDeclaration"):
        self.name = name
        self.model_ss_XtendEvent = model_ss_XtendEvent
        self.model_ss_XtendEvent382 = model_ss_XtendEvent382
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ss_XtendEvent(self):
        return self.__model_ss_XtendEvent

    @model_ss_XtendEvent.setter
    def model_ss_XtendEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendEvent__model_ss_XtendEvent", None)
        self.__model_ss_XtendEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference380"):
                opp_val = getattr(old_value, "JvmTypeReference380", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference380"):
                opp_val = getattr(value, "JvmTypeReference380", None)
                setattr(value, "JvmTypeReference380", self)

    @property
    def model_ss_XtendEvent382(self):
        return self.__model_ss_XtendEvent382

    @model_ss_XtendEvent382.setter
    def model_ss_XtendEvent382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendEvent__model_ss_XtendEvent382", None)
        self.__model_ss_XtendEvent382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression383"):
                opp_val = getattr(old_value, "XExpression383", None)
                if opp_val == self:
                    setattr(old_value, "XExpression383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression383"):
                opp_val = getattr(value, "XExpression383", None)
                setattr(value, "XExpression383", self)

    def isExtension(self) -> bool:
        # TODO: Implement isExtension method
        pass

class model_ss_XtendConstructor(XtendMember):

    pass
class model_ss_XtendFunction(XtendMember):

    def __init__(self, name: str, model_ss_XtendFunction: "XExpression" = None, model_ss_XtendFunction306: "JvmTypeReference" = None, model_ss_XtendFunction309: set["XtendParameter"] = None, model_ss_XtendFunction311: "CreateExtensionInfo" = None, model_ss_XtendFunction313: set["JvmTypeParameter"] = None, model_ss_XtendFunction316: set["JvmTypeReference"] = None, ss362: "model_ss_XtendTypeDeclaration"):
        self.name = name
        self.model_ss_XtendFunction = model_ss_XtendFunction
        self.model_ss_XtendFunction306 = model_ss_XtendFunction306
        self.model_ss_XtendFunction309 = model_ss_XtendFunction309 if model_ss_XtendFunction309 is not None else set()
        self.model_ss_XtendFunction311 = model_ss_XtendFunction311
        self.model_ss_XtendFunction313 = model_ss_XtendFunction313 if model_ss_XtendFunction313 is not None else set()
        self.model_ss_XtendFunction316 = model_ss_XtendFunction316 if model_ss_XtendFunction316 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ss_XtendFunction(self):
        return self.__model_ss_XtendFunction

    @model_ss_XtendFunction.setter
    def model_ss_XtendFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction", None)
        self.__model_ss_XtendFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression304"):
                opp_val = getattr(old_value, "XExpression304", None)
                if opp_val == self:
                    setattr(old_value, "XExpression304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression304"):
                opp_val = getattr(value, "XExpression304", None)
                setattr(value, "XExpression304", self)

    @property
    def model_ss_XtendFunction316(self):
        return self.__model_ss_XtendFunction316

    @model_ss_XtendFunction316.setter
    def model_ss_XtendFunction316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction316", None)
        self.__model_ss_XtendFunction316 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference317"):
                    opp_val = getattr(item, "JvmTypeReference317", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference317", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference317"):
                    opp_val = getattr(item, "JvmTypeReference317", None)
                    
                    setattr(item, "JvmTypeReference317", self)
                    

    @property
    def model_ss_XtendFunction306(self):
        return self.__model_ss_XtendFunction306

    @model_ss_XtendFunction306.setter
    def model_ss_XtendFunction306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction306", None)
        self.__model_ss_XtendFunction306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference307"):
                opp_val = getattr(old_value, "JvmTypeReference307", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference307"):
                opp_val = getattr(value, "JvmTypeReference307", None)
                setattr(value, "JvmTypeReference307", self)

    @property
    def model_ss_XtendFunction313(self):
        return self.__model_ss_XtendFunction313

    @model_ss_XtendFunction313.setter
    def model_ss_XtendFunction313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction313", None)
        self.__model_ss_XtendFunction313 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeParameter314"):
                    opp_val = getattr(item, "JvmTypeParameter314", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeParameter314", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeParameter314"):
                    opp_val = getattr(item, "JvmTypeParameter314", None)
                    
                    setattr(item, "JvmTypeParameter314", self)
                    

    @property
    def model_ss_XtendFunction311(self):
        return self.__model_ss_XtendFunction311

    @model_ss_XtendFunction311.setter
    def model_ss_XtendFunction311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction311", None)
        self.__model_ss_XtendFunction311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CreateExtensionInfo"):
                opp_val = getattr(old_value, "CreateExtensionInfo", None)
                if opp_val == self:
                    setattr(old_value, "CreateExtensionInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CreateExtensionInfo"):
                opp_val = getattr(value, "CreateExtensionInfo", None)
                setattr(value, "CreateExtensionInfo", self)

    @property
    def model_ss_XtendFunction309(self):
        return self.__model_ss_XtendFunction309

    @model_ss_XtendFunction309.setter
    def model_ss_XtendFunction309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction309", None)
        self.__model_ss_XtendFunction309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XtendParameter"):
                    opp_val = getattr(item, "XtendParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "XtendParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XtendParameter"):
                    opp_val = getattr(item, "XtendParameter", None)
                    
                    setattr(item, "XtendParameter", self)
                    

    def isOverride(self) -> bool:
        # TODO: Implement isOverride method
        pass

    def isAbstract(self) -> bool:
        # TODO: Implement isAbstract method
        pass

    def isDispatch(self) -> bool:
        # TODO: Implement isDispatch method
        pass

class XtendAnnotationTarget:

    pass
class model_ss_XtendParameter(XtendAnnotationTarget):

    def __init__(self, name: str, varArg: bool, extension: bool, model_ss_XtendParameter: "JvmTypeReference" = None, XtendAnnotationTarget: "model_ss_XtendMember"):
        self.name = name
        self.varArg = varArg
        self.extension = extension
        self.model_ss_XtendParameter = model_ss_XtendParameter
        
    @property
    def extension(self) -> bool:
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension

    @property
    def varArg(self) -> bool:
        return self.__varArg

    @varArg.setter
    def varArg(self, varArg: bool):
        self.__varArg = varArg

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_ss_XtendParameter(self):
        return self.__model_ss_XtendParameter

    @model_ss_XtendParameter.setter
    def model_ss_XtendParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendParameter__model_ss_XtendParameter", None)
        self.__model_ss_XtendParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference324"):
                opp_val = getattr(old_value, "JvmTypeReference324", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference324"):
                opp_val = getattr(value, "JvmTypeReference324", None)
                setattr(value, "JvmTypeReference324", self)

class model_ss_XtendMember(XtendAnnotationTarget):

    def __init__(self, modifiers: str, model_ss_XtendMember: "XtendAnnotationTarget" = None, XtendTypeDeclaration302: "XtendTypeDeclaration" = None, XtendAnnotationTarget: "model_ss_XtendMember"):
        self.modifiers = modifiers
        self.model_ss_XtendMember = model_ss_XtendMember
        self.XtendTypeDeclaration302 = XtendTypeDeclaration302
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def XtendTypeDeclaration302(self):
        return self.__XtendTypeDeclaration302

    @XtendTypeDeclaration302.setter
    def XtendTypeDeclaration302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendMember__XtendTypeDeclaration302", None)
        self.__XtendTypeDeclaration302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ss"):
                opp_val = getattr(old_value, "ss", None)
                if opp_val == self:
                    setattr(old_value, "ss", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ss"):
                opp_val = getattr(value, "ss", None)
                setattr(value, "ss", self)

    @property
    def model_ss_XtendMember(self):
        return self.__model_ss_XtendMember

    @model_ss_XtendMember.setter
    def model_ss_XtendMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendMember__model_ss_XtendMember", None)
        self.__model_ss_XtendMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XtendAnnotationTarget"):
                opp_val = getattr(old_value, "XtendAnnotationTarget", None)
                if opp_val == self:
                    setattr(old_value, "XtendAnnotationTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XtendAnnotationTarget"):
                opp_val = getattr(value, "XtendAnnotationTarget", None)
                setattr(value, "XtendAnnotationTarget", self)

    def isFinal(self) -> bool:
        # TODO: Implement isFinal method
        pass

    def isStatic(self) -> bool:
        # TODO: Implement isStatic method
        pass

    def getDeclaredVisibility(self) -> str:
        # TODO: Implement getDeclaredVisibility method
        pass

    def getVisibility(self) -> str:
        # TODO: Implement getVisibility method
        pass

class XAnnotation:

    pass
class model_ss_XtendAnnotationTarget(ABC):

    pass
class ss_model_EObject:

    pass
class model_ss_XtendFile:

    def __init__(self, package: str, model_ss_XtendFile: "XImportSection1" = None, model_ss_XtendFile285: set["XtendTypeDeclaration"] = None, model_ss_XtendFile287: set["ss_model_EObject"] = None, model_ss_XtendFile289: "XExportSection" = None):
        self.package = package
        self.model_ss_XtendFile = model_ss_XtendFile
        self.model_ss_XtendFile285 = model_ss_XtendFile285 if model_ss_XtendFile285 is not None else set()
        self.model_ss_XtendFile287 = model_ss_XtendFile287 if model_ss_XtendFile287 is not None else set()
        self.model_ss_XtendFile289 = model_ss_XtendFile289
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def model_ss_XtendFile289(self):
        return self.__model_ss_XtendFile289

    @model_ss_XtendFile289.setter
    def model_ss_XtendFile289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile289", None)
        self.__model_ss_XtendFile289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExportSection290"):
                opp_val = getattr(old_value, "XExportSection290", None)
                if opp_val == self:
                    setattr(old_value, "XExportSection290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExportSection290"):
                opp_val = getattr(value, "XExportSection290", None)
                setattr(value, "XExportSection290", self)

    @property
    def model_ss_XtendFile287(self):
        return self.__model_ss_XtendFile287

    @model_ss_XtendFile287.setter
    def model_ss_XtendFile287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile287", None)
        self.__model_ss_XtendFile287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ss_model_EObject"):
                    opp_val = getattr(item, "ss_model_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "ss_model_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ss_model_EObject"):
                    opp_val = getattr(item, "ss_model_EObject", None)
                    
                    setattr(item, "ss_model_EObject", self)
                    

    @property
    def model_ss_XtendFile(self):
        return self.__model_ss_XtendFile

    @model_ss_XtendFile.setter
    def model_ss_XtendFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile", None)
        self.__model_ss_XtendFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XImportSection1283"):
                opp_val = getattr(old_value, "XImportSection1283", None)
                if opp_val == self:
                    setattr(old_value, "XImportSection1283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XImportSection1283"):
                opp_val = getattr(value, "XImportSection1283", None)
                setattr(value, "XImportSection1283", self)

    @property
    def model_ss_XtendFile285(self):
        return self.__model_ss_XtendFile285

    @model_ss_XtendFile285.setter
    def model_ss_XtendFile285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile285", None)
        self.__model_ss_XtendFile285 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XtendTypeDeclaration"):
                    opp_val = getattr(item, "XtendTypeDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "XtendTypeDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XtendTypeDeclaration"):
                    opp_val = getattr(item, "XtendTypeDeclaration", None)
                    
                    setattr(item, "XtendTypeDeclaration", self)
                    

class XtendTypeDeclaration:

    pass
class model_ss_XtendDelegate(XtendTypeDeclaration):

    pass
class model_ss_XtendAnnotationType(XtendTypeDeclaration):

    pass
class model_ss_XtendClass(XtendTypeDeclaration):

    def __init__(self, model_ss_XtendClass: "JvmTypeReference" = None, model_ss_XtendClass294: set["JvmTypeReference"] = None, model_ss_XtendClass297: set["JvmTypeParameter"] = None, XtendTypeDeclaration: "model_ss_XtendFile", ss: "model_ss_XtendMember"):
        self.model_ss_XtendClass = model_ss_XtendClass
        self.model_ss_XtendClass294 = model_ss_XtendClass294 if model_ss_XtendClass294 is not None else set()
        self.model_ss_XtendClass297 = model_ss_XtendClass297 if model_ss_XtendClass297 is not None else set()
        
    @property
    def model_ss_XtendClass297(self):
        return self.__model_ss_XtendClass297

    @model_ss_XtendClass297.setter
    def model_ss_XtendClass297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendClass__model_ss_XtendClass297", None)
        self.__model_ss_XtendClass297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeParameter298"):
                    opp_val = getattr(item, "JvmTypeParameter298", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeParameter298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeParameter298"):
                    opp_val = getattr(item, "JvmTypeParameter298", None)
                    
                    setattr(item, "JvmTypeParameter298", self)
                    

    @property
    def model_ss_XtendClass294(self):
        return self.__model_ss_XtendClass294

    @model_ss_XtendClass294.setter
    def model_ss_XtendClass294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendClass__model_ss_XtendClass294", None)
        self.__model_ss_XtendClass294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference295"):
                    opp_val = getattr(item, "JvmTypeReference295", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference295"):
                    opp_val = getattr(item, "JvmTypeReference295", None)
                    
                    setattr(item, "JvmTypeReference295", self)
                    

    @property
    def model_ss_XtendClass(self):
        return self.__model_ss_XtendClass

    @model_ss_XtendClass.setter
    def model_ss_XtendClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendClass__model_ss_XtendClass", None)
        self.__model_ss_XtendClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference292"):
                opp_val = getattr(old_value, "JvmTypeReference292", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference292"):
                opp_val = getattr(value, "JvmTypeReference292", None)
                setattr(value, "JvmTypeReference292", self)

    def isAbstract(self) -> bool:
        # TODO: Implement isAbstract method
        pass

class model_ss_XtendInterface(XtendTypeDeclaration):

    pass
class model_ss_XtendEnum(XtendTypeDeclaration):

    pass
class XObjectLiteralPart:

    pass
class model_xbase_XObjectLiteralPart:

    def __init__(self, name: str, model_xbase_XObjectLiteralPart: "XExpression" = None):
        self.name = name
        self.model_xbase_XObjectLiteralPart = model_xbase_XObjectLiteralPart
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_xbase_XObjectLiteralPart(self):
        return self.__model_xbase_XObjectLiteralPart

    @model_xbase_XObjectLiteralPart.setter
    def model_xbase_XObjectLiteralPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XObjectLiteralPart__model_xbase_XObjectLiteralPart", None)
        self.__model_xbase_XObjectLiteralPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression279"):
                opp_val = getattr(old_value, "XExpression279", None)
                if opp_val == self:
                    setattr(old_value, "XExpression279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression279"):
                opp_val = getattr(value, "XExpression279", None)
                setattr(value, "XExpression279", self)

class model_xbase_XCatchClause:

    pass
class XCatchClause:

    pass
class XAbstractWhileExpression:

    pass
class model_xbase_XWhileExpression(XAbstractWhileExpression):

    pass
class model_xbase_XDoWhileExpression(XAbstractWhileExpression):

    pass
class XCollectionLiteral:

    pass
class model_xbase_XSetLiteral(XCollectionLiteral):

    pass
class model_xbase_XListLiteral(XCollectionLiteral):

    pass
class JvmConstructor:

    pass
class XAbstractFeatureCall:

    pass
class model_xbase_XFeatureCall(XAbstractFeatureCall):

    def __init__(self, explicitOperationCall: bool, typeLiteral: bool, packageFragment: bool, indexedOperation: bool, model_xbase_XFeatureCall: set["XExpression"] = None, model_xbase_XFeatureCall155: "XExpression" = None):
        self.explicitOperationCall = explicitOperationCall
        self.typeLiteral = typeLiteral
        self.packageFragment = packageFragment
        self.indexedOperation = indexedOperation
        self.model_xbase_XFeatureCall = model_xbase_XFeatureCall if model_xbase_XFeatureCall is not None else set()
        self.model_xbase_XFeatureCall155 = model_xbase_XFeatureCall155
        
    @property
    def typeLiteral(self) -> bool:
        return self.__typeLiteral

    @typeLiteral.setter
    def typeLiteral(self, typeLiteral: bool):
        self.__typeLiteral = typeLiteral

    @property
    def explicitOperationCall(self) -> bool:
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall

    @property
    def indexedOperation(self) -> bool:
        return self.__indexedOperation

    @indexedOperation.setter
    def indexedOperation(self, indexedOperation: bool):
        self.__indexedOperation = indexedOperation

    @property
    def packageFragment(self) -> bool:
        return self.__packageFragment

    @packageFragment.setter
    def packageFragment(self, packageFragment: bool):
        self.__packageFragment = packageFragment

    @property
    def model_xbase_XFeatureCall155(self):
        return self.__model_xbase_XFeatureCall155

    @model_xbase_XFeatureCall155.setter
    def model_xbase_XFeatureCall155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFeatureCall__model_xbase_XFeatureCall155", None)
        self.__model_xbase_XFeatureCall155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression156"):
                opp_val = getattr(old_value, "XExpression156", None)
                if opp_val == self:
                    setattr(old_value, "XExpression156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression156"):
                opp_val = getattr(value, "XExpression156", None)
                setattr(value, "XExpression156", self)

    @property
    def model_xbase_XFeatureCall(self):
        return self.__model_xbase_XFeatureCall

    @model_xbase_XFeatureCall.setter
    def model_xbase_XFeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFeatureCall__model_xbase_XFeatureCall", None)
        self.__model_xbase_XFeatureCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression153"):
                    opp_val = getattr(item, "XExpression153", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression153"):
                    opp_val = getattr(item, "XExpression153", None)
                    
                    setattr(item, "XExpression153", self)
                    

class model_xbase_XPrefixOperation(XAbstractFeatureCall):

    pass
class model_xbase_XIndexOperation(XAbstractFeatureCall):

    pass
class model_xbase_XUnaryOperation(XAbstractFeatureCall):

    pass
class model_xbase_XAssignment(XAbstractFeatureCall):

    def __init__(self, explicitStatic: bool, model_xbase_XAssignment: "XExpression" = None, model_xbase_XAssignment245: "XExpression" = None):
        self.explicitStatic = explicitStatic
        self.model_xbase_XAssignment = model_xbase_XAssignment
        self.model_xbase_XAssignment245 = model_xbase_XAssignment245
        
    @property
    def explicitStatic(self) -> bool:
        return self.__explicitStatic

    @explicitStatic.setter
    def explicitStatic(self, explicitStatic: bool):
        self.__explicitStatic = explicitStatic

    @property
    def model_xbase_XAssignment245(self):
        return self.__model_xbase_XAssignment245

    @model_xbase_XAssignment245.setter
    def model_xbase_XAssignment245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAssignment__model_xbase_XAssignment245", None)
        self.__model_xbase_XAssignment245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression246"):
                opp_val = getattr(old_value, "XExpression246", None)
                if opp_val == self:
                    setattr(old_value, "XExpression246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression246"):
                opp_val = getattr(value, "XExpression246", None)
                setattr(value, "XExpression246", self)

    @property
    def model_xbase_XAssignment(self):
        return self.__model_xbase_XAssignment

    @model_xbase_XAssignment.setter
    def model_xbase_XAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAssignment__model_xbase_XAssignment", None)
        self.__model_xbase_XAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression243"):
                opp_val = getattr(old_value, "XExpression243", None)
                if opp_val == self:
                    setattr(old_value, "XExpression243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression243"):
                opp_val = getattr(value, "XExpression243", None)
                setattr(value, "XExpression243", self)

class model_xbase_XBinaryOperation(XAbstractFeatureCall):

    pass
class model_xbase_XMemberFeatureCall1(XAbstractFeatureCall):

    def __init__(self, explicitOperationCall: bool, explicitStatic: bool, nullSafe: bool, typeLiteral: bool, staticWithDeclaringType: bool, packageFragment: bool, indexedOperation: bool, model_xbase_XMemberFeatureCall1: "XExpression" = None, model_xbase_XMemberFeatureCall1150: set["XExpression"] = None):
        self.explicitOperationCall = explicitOperationCall
        self.explicitStatic = explicitStatic
        self.nullSafe = nullSafe
        self.typeLiteral = typeLiteral
        self.staticWithDeclaringType = staticWithDeclaringType
        self.packageFragment = packageFragment
        self.indexedOperation = indexedOperation
        self.model_xbase_XMemberFeatureCall1 = model_xbase_XMemberFeatureCall1
        self.model_xbase_XMemberFeatureCall1150 = model_xbase_XMemberFeatureCall1150 if model_xbase_XMemberFeatureCall1150 is not None else set()
        
    @property
    def typeLiteral(self) -> bool:
        return self.__typeLiteral

    @typeLiteral.setter
    def typeLiteral(self, typeLiteral: bool):
        self.__typeLiteral = typeLiteral

    @property
    def staticWithDeclaringType(self) -> bool:
        return self.__staticWithDeclaringType

    @staticWithDeclaringType.setter
    def staticWithDeclaringType(self, staticWithDeclaringType: bool):
        self.__staticWithDeclaringType = staticWithDeclaringType

    @property
    def packageFragment(self) -> bool:
        return self.__packageFragment

    @packageFragment.setter
    def packageFragment(self, packageFragment: bool):
        self.__packageFragment = packageFragment

    @property
    def explicitStatic(self) -> bool:
        return self.__explicitStatic

    @explicitStatic.setter
    def explicitStatic(self, explicitStatic: bool):
        self.__explicitStatic = explicitStatic

    @property
    def nullSafe(self) -> bool:
        return self.__nullSafe

    @nullSafe.setter
    def nullSafe(self, nullSafe: bool):
        self.__nullSafe = nullSafe

    @property
    def indexedOperation(self) -> bool:
        return self.__indexedOperation

    @indexedOperation.setter
    def indexedOperation(self, indexedOperation: bool):
        self.__indexedOperation = indexedOperation

    @property
    def explicitOperationCall(self) -> bool:
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall

    @property
    def model_xbase_XMemberFeatureCall1(self):
        return self.__model_xbase_XMemberFeatureCall1

    @model_xbase_XMemberFeatureCall1.setter
    def model_xbase_XMemberFeatureCall1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XMemberFeatureCall1__model_xbase_XMemberFeatureCall1", None)
        self.__model_xbase_XMemberFeatureCall1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression148"):
                opp_val = getattr(old_value, "XExpression148", None)
                if opp_val == self:
                    setattr(old_value, "XExpression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression148"):
                opp_val = getattr(value, "XExpression148", None)
                setattr(value, "XExpression148", self)

    @property
    def model_xbase_XMemberFeatureCall1150(self):
        return self.__model_xbase_XMemberFeatureCall1150

    @model_xbase_XMemberFeatureCall1150.setter
    def model_xbase_XMemberFeatureCall1150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XMemberFeatureCall1__model_xbase_XMemberFeatureCall1150", None)
        self.__model_xbase_XMemberFeatureCall1150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression151"):
                    opp_val = getattr(item, "XExpression151", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression151"):
                    opp_val = getattr(item, "XExpression151", None)
                    
                    setattr(item, "XExpression151", self)
                    

class model_xbase_XPostfixOperation(XAbstractFeatureCall):

    pass
class model_xbase_XMemberFeatureCall(XAbstractFeatureCall):

    def __init__(self, nullSafe: bool, explicitOperationCall: bool, explicitStatic: bool, typeLiteral: bool, staticWithDeclaringType: bool, packageFragment: bool, indexedOperation: bool, model_xbase_XMemberFeatureCall: "XExpression" = None, model_xbase_XMemberFeatureCall145: set["XExpression"] = None):
        self.nullSafe = nullSafe
        self.explicitOperationCall = explicitOperationCall
        self.explicitStatic = explicitStatic
        self.typeLiteral = typeLiteral
        self.staticWithDeclaringType = staticWithDeclaringType
        self.packageFragment = packageFragment
        self.indexedOperation = indexedOperation
        self.model_xbase_XMemberFeatureCall = model_xbase_XMemberFeatureCall
        self.model_xbase_XMemberFeatureCall145 = model_xbase_XMemberFeatureCall145 if model_xbase_XMemberFeatureCall145 is not None else set()
        
    @property
    def packageFragment(self) -> bool:
        return self.__packageFragment

    @packageFragment.setter
    def packageFragment(self, packageFragment: bool):
        self.__packageFragment = packageFragment

    @property
    def staticWithDeclaringType(self) -> bool:
        return self.__staticWithDeclaringType

    @staticWithDeclaringType.setter
    def staticWithDeclaringType(self, staticWithDeclaringType: bool):
        self.__staticWithDeclaringType = staticWithDeclaringType

    @property
    def explicitOperationCall(self) -> bool:
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall

    @property
    def nullSafe(self) -> bool:
        return self.__nullSafe

    @nullSafe.setter
    def nullSafe(self, nullSafe: bool):
        self.__nullSafe = nullSafe

    @property
    def indexedOperation(self) -> bool:
        return self.__indexedOperation

    @indexedOperation.setter
    def indexedOperation(self, indexedOperation: bool):
        self.__indexedOperation = indexedOperation

    @property
    def explicitStatic(self) -> bool:
        return self.__explicitStatic

    @explicitStatic.setter
    def explicitStatic(self, explicitStatic: bool):
        self.__explicitStatic = explicitStatic

    @property
    def typeLiteral(self) -> bool:
        return self.__typeLiteral

    @typeLiteral.setter
    def typeLiteral(self, typeLiteral: bool):
        self.__typeLiteral = typeLiteral

    @property
    def model_xbase_XMemberFeatureCall(self):
        return self.__model_xbase_XMemberFeatureCall

    @model_xbase_XMemberFeatureCall.setter
    def model_xbase_XMemberFeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XMemberFeatureCall__model_xbase_XMemberFeatureCall", None)
        self.__model_xbase_XMemberFeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression143"):
                opp_val = getattr(old_value, "XExpression143", None)
                if opp_val == self:
                    setattr(old_value, "XExpression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression143"):
                opp_val = getattr(value, "XExpression143", None)
                setattr(value, "XExpression143", self)

    @property
    def model_xbase_XMemberFeatureCall145(self):
        return self.__model_xbase_XMemberFeatureCall145

    @model_xbase_XMemberFeatureCall145.setter
    def model_xbase_XMemberFeatureCall145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XMemberFeatureCall__model_xbase_XMemberFeatureCall145", None)
        self.__model_xbase_XMemberFeatureCall145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression146"):
                    opp_val = getattr(item, "XExpression146", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression146"):
                    opp_val = getattr(item, "XExpression146", None)
                    
                    setattr(item, "XExpression146", self)
                    

class model_xbase_XCasePart:

    pass
class XCasePart:

    pass
class types_JvmIdentifiableElement:

    pass
class xbase_XExpression:

    pass
class model_xbase_XClosure(xbase_XExpression, types_JvmIdentifiableElement):

    def __init__(self, explicitSyntax: bool, name: str, operator: bool, exported: bool, model_xbase_XClosure: set["JvmFormalParameter"] = None, model_xbase_XClosure174: "XExpression" = None, model_xbase_XClosure177: "JvmFormalParameter" = None, model_xbase_XClosure180: "JvmTypeReference" = None, model_xbase_XClosure183: set["JvmTypeParameter"] = None):
        self.explicitSyntax = explicitSyntax
        self.name = name
        self.operator = operator
        self.exported = exported
        self.model_xbase_XClosure = model_xbase_XClosure if model_xbase_XClosure is not None else set()
        self.model_xbase_XClosure174 = model_xbase_XClosure174
        self.model_xbase_XClosure177 = model_xbase_XClosure177
        self.model_xbase_XClosure180 = model_xbase_XClosure180
        self.model_xbase_XClosure183 = model_xbase_XClosure183 if model_xbase_XClosure183 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

    @property
    def operator(self) -> bool:
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator

    @property
    def explicitSyntax(self) -> bool:
        return self.__explicitSyntax

    @explicitSyntax.setter
    def explicitSyntax(self, explicitSyntax: bool):
        self.__explicitSyntax = explicitSyntax

    @property
    def model_xbase_XClosure177(self):
        return self.__model_xbase_XClosure177

    @model_xbase_XClosure177.setter
    def model_xbase_XClosure177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure177", None)
        self.__model_xbase_XClosure177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmFormalParameter178"):
                opp_val = getattr(old_value, "JvmFormalParameter178", None)
                if opp_val == self:
                    setattr(old_value, "JvmFormalParameter178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmFormalParameter178"):
                opp_val = getattr(value, "JvmFormalParameter178", None)
                setattr(value, "JvmFormalParameter178", self)

    @property
    def model_xbase_XClosure(self):
        return self.__model_xbase_XClosure

    @model_xbase_XClosure.setter
    def model_xbase_XClosure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure", None)
        self.__model_xbase_XClosure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmFormalParameter172"):
                    opp_val = getattr(item, "JvmFormalParameter172", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmFormalParameter172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmFormalParameter172"):
                    opp_val = getattr(item, "JvmFormalParameter172", None)
                    
                    setattr(item, "JvmFormalParameter172", self)
                    

    @property
    def model_xbase_XClosure180(self):
        return self.__model_xbase_XClosure180

    @model_xbase_XClosure180.setter
    def model_xbase_XClosure180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure180", None)
        self.__model_xbase_XClosure180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference181"):
                opp_val = getattr(old_value, "JvmTypeReference181", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference181"):
                opp_val = getattr(value, "JvmTypeReference181", None)
                setattr(value, "JvmTypeReference181", self)

    @property
    def model_xbase_XClosure174(self):
        return self.__model_xbase_XClosure174

    @model_xbase_XClosure174.setter
    def model_xbase_XClosure174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure174", None)
        self.__model_xbase_XClosure174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression175"):
                opp_val = getattr(old_value, "XExpression175", None)
                if opp_val == self:
                    setattr(old_value, "XExpression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression175"):
                opp_val = getattr(value, "XExpression175", None)
                setattr(value, "XExpression175", self)

    @property
    def model_xbase_XClosure183(self):
        return self.__model_xbase_XClosure183

    @model_xbase_XClosure183.setter
    def model_xbase_XClosure183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure183", None)
        self.__model_xbase_XClosure183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeParameter184"):
                    opp_val = getattr(item, "JvmTypeParameter184", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeParameter184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeParameter184"):
                    opp_val = getattr(item, "JvmTypeParameter184", None)
                    
                    setattr(item, "JvmTypeParameter184", self)
                    

    def getFormalParameters(self) -> str:
        # TODO: Implement getFormalParameters method
        pass

class model_xbase_XVariableDeclaration(xbase_XExpression, types_JvmIdentifiableElement):

    def __init__(self, name: str, writeable: bool, exported: bool, model_xbase_XVariableDeclaration: "JvmTypeReference" = None, model_xbase_XVariableDeclaration128: "XExpression" = None):
        self.name = name
        self.writeable = writeable
        self.exported = exported
        self.model_xbase_XVariableDeclaration = model_xbase_XVariableDeclaration
        self.model_xbase_XVariableDeclaration128 = model_xbase_XVariableDeclaration128
        
    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

    @property
    def writeable(self) -> bool:
        return self.__writeable

    @writeable.setter
    def writeable(self, writeable: bool):
        self.__writeable = writeable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_xbase_XVariableDeclaration(self):
        return self.__model_xbase_XVariableDeclaration

    @model_xbase_XVariableDeclaration.setter
    def model_xbase_XVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XVariableDeclaration__model_xbase_XVariableDeclaration", None)
        self.__model_xbase_XVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference126"):
                opp_val = getattr(old_value, "JvmTypeReference126", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference126"):
                opp_val = getattr(value, "JvmTypeReference126", None)
                setattr(value, "JvmTypeReference126", self)

    @property
    def model_xbase_XVariableDeclaration128(self):
        return self.__model_xbase_XVariableDeclaration128

    @model_xbase_XVariableDeclaration128.setter
    def model_xbase_XVariableDeclaration128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XVariableDeclaration__model_xbase_XVariableDeclaration128", None)
        self.__model_xbase_XVariableDeclaration128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression129"):
                opp_val = getattr(old_value, "XExpression129", None)
                if opp_val == self:
                    setattr(old_value, "XExpression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression129"):
                opp_val = getattr(value, "XExpression129", None)
                setattr(value, "XExpression129", self)

class model_xbase_XSwitchExpression(xbase_XExpression, types_JvmIdentifiableElement):

    def __init__(self, localVarName: str, model_xbase_XSwitchExpression: "XExpression" = None, model_xbase_XSwitchExpression111: set["XCasePart"] = None, model_xbase_XSwitchExpression113: "XExpression" = None):
        self.localVarName = localVarName
        self.model_xbase_XSwitchExpression = model_xbase_XSwitchExpression
        self.model_xbase_XSwitchExpression111 = model_xbase_XSwitchExpression111 if model_xbase_XSwitchExpression111 is not None else set()
        self.model_xbase_XSwitchExpression113 = model_xbase_XSwitchExpression113
        
    @property
    def localVarName(self) -> str:
        return self.__localVarName

    @localVarName.setter
    def localVarName(self, localVarName: str):
        self.__localVarName = localVarName

    @property
    def model_xbase_XSwitchExpression113(self):
        return self.__model_xbase_XSwitchExpression113

    @model_xbase_XSwitchExpression113.setter
    def model_xbase_XSwitchExpression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XSwitchExpression__model_xbase_XSwitchExpression113", None)
        self.__model_xbase_XSwitchExpression113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression114"):
                opp_val = getattr(old_value, "XExpression114", None)
                if opp_val == self:
                    setattr(old_value, "XExpression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression114"):
                opp_val = getattr(value, "XExpression114", None)
                setattr(value, "XExpression114", self)

    @property
    def model_xbase_XSwitchExpression111(self):
        return self.__model_xbase_XSwitchExpression111

    @model_xbase_XSwitchExpression111.setter
    def model_xbase_XSwitchExpression111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XSwitchExpression__model_xbase_XSwitchExpression111", None)
        self.__model_xbase_XSwitchExpression111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XCasePart"):
                    opp_val = getattr(item, "XCasePart", None)
                    
                    if opp_val == self:
                        setattr(item, "XCasePart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XCasePart"):
                    opp_val = getattr(item, "XCasePart", None)
                    
                    setattr(item, "XCasePart", self)
                    

    @property
    def model_xbase_XSwitchExpression(self):
        return self.__model_xbase_XSwitchExpression

    @model_xbase_XSwitchExpression.setter
    def model_xbase_XSwitchExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XSwitchExpression__model_xbase_XSwitchExpression", None)
        self.__model_xbase_XSwitchExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression109"):
                opp_val = getattr(old_value, "XExpression109", None)
                if opp_val == self:
                    setattr(old_value, "XExpression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression109"):
                opp_val = getattr(value, "XExpression109", None)
                setattr(value, "XExpression109", self)

class model_xbase_XExpression(ABC):

    pass
class JvmAnnotationReference:

    pass
class JvmOperation:

    pass
class model_types_JvmAnnotationValue:

    def __init__(self, model_types_JvmAnnotationValue: "JvmOperation" = None, model_types_JvmAnnotationValue83: "XExpression" = None):
        self.model_types_JvmAnnotationValue = model_types_JvmAnnotationValue
        self.model_types_JvmAnnotationValue83 = model_types_JvmAnnotationValue83
        
    @property
    def model_types_JvmAnnotationValue(self):
        return self.__model_types_JvmAnnotationValue

    @model_types_JvmAnnotationValue.setter
    def model_types_JvmAnnotationValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmAnnotationValue__model_types_JvmAnnotationValue", None)
        self.__model_types_JvmAnnotationValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmOperation"):
                opp_val = getattr(old_value, "JvmOperation", None)
                if opp_val == self:
                    setattr(old_value, "JvmOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmOperation"):
                opp_val = getattr(value, "JvmOperation", None)
                setattr(value, "JvmOperation", self)

    @property
    def model_types_JvmAnnotationValue83(self):
        return self.__model_types_JvmAnnotationValue83

    @model_types_JvmAnnotationValue83.setter
    def model_types_JvmAnnotationValue83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmAnnotationValue__model_types_JvmAnnotationValue83", None)
        self.__model_types_JvmAnnotationValue83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression84"):
                opp_val = getattr(old_value, "XExpression84", None)
                if opp_val == self:
                    setattr(old_value, "XExpression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression84"):
                opp_val = getattr(value, "XExpression84", None)
                setattr(value, "XExpression84", self)

    def getValueName(self) -> str:
        # TODO: Implement getValueName method
        pass

class JvmAnnotationType:

    pass
class model_types_JvmAnnotationReference:

    pass
class JvmAnnotationValue:

    pass
class model_types_JvmLongAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_types_JvmShortAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_types_JvmFloatAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> float:
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values

class model_types_JvmBooleanAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: bool, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> bool:
        return self.__values

    @values.setter
    def values(self, values: bool):
        self.__values = values

class model_types_JvmEnumAnnotationValue(JvmAnnotationValue):

    pass
class model_types_JvmDoubleAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> float:
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values

class model_types_JvmCharAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_types_JvmCustomAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_types_JvmAnnotationAnnotationValue(JvmAnnotationValue):

    pass
class model_types_JvmTypeAnnotationValue(JvmAnnotationValue):

    pass
class model_types_JvmStringAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class model_types_JvmIntAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: int, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> int:
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values

class model_types_JvmByteAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue77: "model_types_JvmAnnotationReference", JvmAnnotationValue: "model_types_JvmOperation"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class JvmFormalParameter:

    pass
class model_ss_XtendFormalParameter(JvmFormalParameter):

    def __init__(self, extension: bool, JvmFormalParameter178: "model_xbase_XClosure", JvmFormalParameter172: "model_xbase_XClosure", JvmFormalParameter: "model_types_JvmExecutable", JvmFormalParameter215: "model_xbase_XForEachExpression", JvmFormalParameter273: "model_xbase_XFunctionDeclaration", JvmFormalParameter241: "model_xbase_XCatchClause"):
        self.extension = extension
        
    @property
    def extension(self) -> bool:
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension

class JvmExecutable:

    pass
class model_types_JvmOperation(JvmExecutable):

    def __init__(self, static: bool, final: bool, abstract: bool, default: bool, native: bool, strictFloatingPoint: bool, synchronized: bool, model_types_JvmOperation61: "JvmAnnotationValue" = None, model_types_JvmOperation: "JvmTypeReference" = None, model_types_JvmOperation63: "XExpression" = None, model_types_JvmOperation66: "XExpression" = None):
        self.static = static
        self.final = final
        self.abstract = abstract
        self.default = default
        self.native = native
        self.strictFloatingPoint = strictFloatingPoint
        self.synchronized = synchronized
        self.model_types_JvmOperation61 = model_types_JvmOperation61
        self.model_types_JvmOperation = model_types_JvmOperation
        self.model_types_JvmOperation63 = model_types_JvmOperation63
        self.model_types_JvmOperation66 = model_types_JvmOperation66
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def strictFloatingPoint(self) -> bool:
        return self.__strictFloatingPoint

    @strictFloatingPoint.setter
    def strictFloatingPoint(self, strictFloatingPoint: bool):
        self.__strictFloatingPoint = strictFloatingPoint

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def model_types_JvmOperation(self):
        return self.__model_types_JvmOperation

    @model_types_JvmOperation.setter
    def model_types_JvmOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation", None)
        self.__model_types_JvmOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference59"):
                opp_val = getattr(old_value, "JvmTypeReference59", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference59"):
                opp_val = getattr(value, "JvmTypeReference59", None)
                setattr(value, "JvmTypeReference59", self)

    @property
    def model_types_JvmOperation66(self):
        return self.__model_types_JvmOperation66

    @model_types_JvmOperation66.setter
    def model_types_JvmOperation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation66", None)
        self.__model_types_JvmOperation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression67"):
                opp_val = getattr(old_value, "XExpression67", None)
                if opp_val == self:
                    setattr(old_value, "XExpression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression67"):
                opp_val = getattr(value, "XExpression67", None)
                setattr(value, "XExpression67", self)

    @property
    def model_types_JvmOperation61(self):
        return self.__model_types_JvmOperation61

    @model_types_JvmOperation61.setter
    def model_types_JvmOperation61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation61", None)
        self.__model_types_JvmOperation61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmAnnotationValue"):
                opp_val = getattr(old_value, "JvmAnnotationValue", None)
                if opp_val == self:
                    setattr(old_value, "JvmAnnotationValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmAnnotationValue"):
                opp_val = getattr(value, "JvmAnnotationValue", None)
                setattr(value, "JvmAnnotationValue", self)

    @property
    def model_types_JvmOperation63(self):
        return self.__model_types_JvmOperation63

    @model_types_JvmOperation63.setter
    def model_types_JvmOperation63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation63", None)
        self.__model_types_JvmOperation63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression64"):
                opp_val = getattr(old_value, "XExpression64", None)
                if opp_val == self:
                    setattr(old_value, "XExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression64"):
                opp_val = getattr(value, "XExpression64", None)
                setattr(value, "XExpression64", self)

class model_types_JvmConstructor(JvmExecutable):

    pass
class XExpression:

    pass
class model_ss_RichStringIf(XExpression):

    pass
class model_xbase_XNumberLiteral(XExpression):

    def __init__(self, value: str, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_xbase_XFunctionDeclaration(XExpression):

    def __init__(self, name: str, model_xbase_XFunctionDeclaration: "XExpression" = None, model_xbase_XFunctionDeclaration269: "JvmTypeReference" = None, model_xbase_XFunctionDeclaration272: set["JvmFormalParameter"] = None, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.name = name
        self.model_xbase_XFunctionDeclaration = model_xbase_XFunctionDeclaration
        self.model_xbase_XFunctionDeclaration269 = model_xbase_XFunctionDeclaration269
        self.model_xbase_XFunctionDeclaration272 = model_xbase_XFunctionDeclaration272 if model_xbase_XFunctionDeclaration272 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_xbase_XFunctionDeclaration269(self):
        return self.__model_xbase_XFunctionDeclaration269

    @model_xbase_XFunctionDeclaration269.setter
    def model_xbase_XFunctionDeclaration269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFunctionDeclaration__model_xbase_XFunctionDeclaration269", None)
        self.__model_xbase_XFunctionDeclaration269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference270"):
                opp_val = getattr(old_value, "JvmTypeReference270", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference270"):
                opp_val = getattr(value, "JvmTypeReference270", None)
                setattr(value, "JvmTypeReference270", self)

    @property
    def model_xbase_XFunctionDeclaration272(self):
        return self.__model_xbase_XFunctionDeclaration272

    @model_xbase_XFunctionDeclaration272.setter
    def model_xbase_XFunctionDeclaration272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFunctionDeclaration__model_xbase_XFunctionDeclaration272", None)
        self.__model_xbase_XFunctionDeclaration272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmFormalParameter273"):
                    opp_val = getattr(item, "JvmFormalParameter273", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmFormalParameter273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmFormalParameter273"):
                    opp_val = getattr(item, "JvmFormalParameter273", None)
                    
                    setattr(item, "JvmFormalParameter273", self)
                    

    @property
    def model_xbase_XFunctionDeclaration(self):
        return self.__model_xbase_XFunctionDeclaration

    @model_xbase_XFunctionDeclaration.setter
    def model_xbase_XFunctionDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFunctionDeclaration__model_xbase_XFunctionDeclaration", None)
        self.__model_xbase_XFunctionDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression267"):
                opp_val = getattr(old_value, "XExpression267", None)
                if opp_val == self:
                    setattr(old_value, "XExpression267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression267"):
                opp_val = getattr(value, "XExpression267", None)
                setattr(value, "XExpression267", self)

class model_xbase_XObjectLiteral(XExpression):

    pass
class model_xbase_XAbstractFeatureCall(XExpression):

    def __init__(self, invalidFeatureIssueCode: str, validFeature: bool, model_xbase_XAbstractFeatureCall: "JvmIdentifiableElement" = None, model_xbase_XAbstractFeatureCall134: set["JvmTypeReference"] = None, model_xbase_XAbstractFeatureCall137: "XExpression" = None, model_xbase_XAbstractFeatureCall140: "XExpression" = None, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.invalidFeatureIssueCode = invalidFeatureIssueCode
        self.validFeature = validFeature
        self.model_xbase_XAbstractFeatureCall = model_xbase_XAbstractFeatureCall
        self.model_xbase_XAbstractFeatureCall134 = model_xbase_XAbstractFeatureCall134 if model_xbase_XAbstractFeatureCall134 is not None else set()
        self.model_xbase_XAbstractFeatureCall137 = model_xbase_XAbstractFeatureCall137
        self.model_xbase_XAbstractFeatureCall140 = model_xbase_XAbstractFeatureCall140
        
    @property
    def invalidFeatureIssueCode(self) -> str:
        return self.__invalidFeatureIssueCode

    @invalidFeatureIssueCode.setter
    def invalidFeatureIssueCode(self, invalidFeatureIssueCode: str):
        self.__invalidFeatureIssueCode = invalidFeatureIssueCode

    @property
    def validFeature(self) -> bool:
        return self.__validFeature

    @validFeature.setter
    def validFeature(self, validFeature: bool):
        self.__validFeature = validFeature

    @property
    def model_xbase_XAbstractFeatureCall137(self):
        return self.__model_xbase_XAbstractFeatureCall137

    @model_xbase_XAbstractFeatureCall137.setter
    def model_xbase_XAbstractFeatureCall137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall137", None)
        self.__model_xbase_XAbstractFeatureCall137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression138"):
                opp_val = getattr(old_value, "XExpression138", None)
                if opp_val == self:
                    setattr(old_value, "XExpression138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression138"):
                opp_val = getattr(value, "XExpression138", None)
                setattr(value, "XExpression138", self)

    @property
    def model_xbase_XAbstractFeatureCall134(self):
        return self.__model_xbase_XAbstractFeatureCall134

    @model_xbase_XAbstractFeatureCall134.setter
    def model_xbase_XAbstractFeatureCall134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall134", None)
        self.__model_xbase_XAbstractFeatureCall134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference135"):
                    opp_val = getattr(item, "JvmTypeReference135", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference135"):
                    opp_val = getattr(item, "JvmTypeReference135", None)
                    
                    setattr(item, "JvmTypeReference135", self)
                    

    @property
    def model_xbase_XAbstractFeatureCall(self):
        return self.__model_xbase_XAbstractFeatureCall

    @model_xbase_XAbstractFeatureCall.setter
    def model_xbase_XAbstractFeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall", None)
        self.__model_xbase_XAbstractFeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmIdentifiableElement"):
                opp_val = getattr(old_value, "JvmIdentifiableElement", None)
                if opp_val == self:
                    setattr(old_value, "JvmIdentifiableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmIdentifiableElement"):
                opp_val = getattr(value, "JvmIdentifiableElement", None)
                setattr(value, "JvmIdentifiableElement", self)

    @property
    def model_xbase_XAbstractFeatureCall140(self):
        return self.__model_xbase_XAbstractFeatureCall140

    @model_xbase_XAbstractFeatureCall140.setter
    def model_xbase_XAbstractFeatureCall140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall140", None)
        self.__model_xbase_XAbstractFeatureCall140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression141"):
                opp_val = getattr(old_value, "XExpression141", None)
                if opp_val == self:
                    setattr(old_value, "XExpression141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression141"):
                opp_val = getattr(value, "XExpression141", None)
                setattr(value, "XExpression141", self)

    def getActualReceiver(self) -> str:
        # TODO: Implement getActualReceiver method
        pass

    def getConcreteSyntaxFeatureName(self) -> str:
        # TODO: Implement getConcreteSyntaxFeatureName method
        pass

    def isPackageFragment(self) -> bool:
        # TODO: Implement isPackageFragment method
        pass

    def getExplicitArguments(self) -> str:
        # TODO: Implement getExplicitArguments method
        pass

    def isExtension(self) -> bool:
        # TODO: Implement isExtension method
        pass

    def isTypeLiteral(self) -> bool:
        # TODO: Implement isTypeLiteral method
        pass

    def getActualArguments(self) -> str:
        # TODO: Implement getActualArguments method
        pass

    def isStatic(self) -> bool:
        # TODO: Implement isStatic method
        pass

    def isExplicitOperationCallOrBuilderSyntax(self) -> bool:
        # TODO: Implement isExplicitOperationCallOrBuilderSyntax method
        pass

class model_xannotation_XAnnotation(XExpression):

    pass
class model_xbase_XReturnExpression(XExpression):

    pass
class model_xbase_XIfExpression(XExpression):

    pass
class model_xbase_XTryCatchFinallyExpression(XExpression):

    pass
class model_xbase_XTernaryOperation(XExpression):

    pass
class model_xbase_XForEachExpression(XExpression):

    pass
class model_xbase_XVariableDeclarationList(XExpression):

    def __init__(self, writeable: bool, exported: bool, model_xbase_XVariableDeclarationList: set["XExpression"] = None, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.writeable = writeable
        self.exported = exported
        self.model_xbase_XVariableDeclarationList = model_xbase_XVariableDeclarationList if model_xbase_XVariableDeclarationList is not None else set()
        
    @property
    def writeable(self) -> bool:
        return self.__writeable

    @writeable.setter
    def writeable(self, writeable: bool):
        self.__writeable = writeable

    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

    @property
    def model_xbase_XVariableDeclarationList(self):
        return self.__model_xbase_XVariableDeclarationList

    @model_xbase_XVariableDeclarationList.setter
    def model_xbase_XVariableDeclarationList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XVariableDeclarationList__model_xbase_XVariableDeclarationList", None)
        self.__model_xbase_XVariableDeclarationList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression131"):
                    opp_val = getattr(item, "XExpression131", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression131"):
                    opp_val = getattr(item, "XExpression131", None)
                    
                    setattr(item, "XExpression131", self)
                    

class model_xbase_XAbstractWhileExpression(XExpression):

    pass
class model_xbase_XCastedExpression(XExpression):

    pass
class model_xbase_XTypeLiteral(XExpression):

    def __init__(self, arrayDimensions: str, model_xbase_XTypeLiteral: "JvmType" = None, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.arrayDimensions = arrayDimensions
        self.model_xbase_XTypeLiteral = model_xbase_XTypeLiteral
        
    @property
    def arrayDimensions(self) -> str:
        return self.__arrayDimensions

    @arrayDimensions.setter
    def arrayDimensions(self, arrayDimensions: str):
        self.__arrayDimensions = arrayDimensions

    @property
    def model_xbase_XTypeLiteral(self):
        return self.__model_xbase_XTypeLiteral

    @model_xbase_XTypeLiteral.setter
    def model_xbase_XTypeLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XTypeLiteral__model_xbase_XTypeLiteral", None)
        self.__model_xbase_XTypeLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmType222"):
                opp_val = getattr(old_value, "JvmType222", None)
                if opp_val == self:
                    setattr(old_value, "JvmType222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmType222"):
                opp_val = getattr(value, "JvmType222", None)
                setattr(value, "JvmType222", self)

class model_xbase_XBlockExpression(XExpression):

    pass
class model_xbase_XKeyValuePair(XExpression):

    def __init__(self, key1: str, model_xbase_XKeyValuePair: "XExpression" = None, model_xbase_XKeyValuePair169: "XExpression" = None, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.key1 = key1
        self.model_xbase_XKeyValuePair = model_xbase_XKeyValuePair
        self.model_xbase_XKeyValuePair169 = model_xbase_XKeyValuePair169
        
    @property
    def key1(self) -> str:
        return self.__key1

    @key1.setter
    def key1(self, key1: str):
        self.__key1 = key1

    @property
    def model_xbase_XKeyValuePair(self):
        return self.__model_xbase_XKeyValuePair

    @model_xbase_XKeyValuePair.setter
    def model_xbase_XKeyValuePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XKeyValuePair__model_xbase_XKeyValuePair", None)
        self.__model_xbase_XKeyValuePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression167"):
                opp_val = getattr(old_value, "XExpression167", None)
                if opp_val == self:
                    setattr(old_value, "XExpression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression167"):
                opp_val = getattr(value, "XExpression167", None)
                setattr(value, "XExpression167", self)

    @property
    def model_xbase_XKeyValuePair169(self):
        return self.__model_xbase_XKeyValuePair169

    @model_xbase_XKeyValuePair169.setter
    def model_xbase_XKeyValuePair169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XKeyValuePair__model_xbase_XKeyValuePair169", None)
        self.__model_xbase_XKeyValuePair169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression170"):
                opp_val = getattr(old_value, "XExpression170", None)
                if opp_val == self:
                    setattr(old_value, "XExpression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression170"):
                opp_val = getattr(value, "XExpression170", None)
                setattr(value, "XExpression170", self)

class model_xbase_XCollectionLiteral(XExpression):

    pass
class model_xbase_XThrowExpression(XExpression):

    pass
class model_xbase_XInstanceOfExpression(XExpression):

    pass
class model_xbase_XContinueExpression(XExpression):

    pass
class model_xbase_XConstructorCall(XExpression):

    def __init__(self, invalidFeatureIssueCode: str, validFeature: bool, model_xbase_XConstructorCall: "JvmConstructor" = None, model_xbase_XConstructorCall159: set["XExpression"] = None, model_xbase_XConstructorCall162: set["JvmTypeReference"] = None, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.invalidFeatureIssueCode = invalidFeatureIssueCode
        self.validFeature = validFeature
        self.model_xbase_XConstructorCall = model_xbase_XConstructorCall
        self.model_xbase_XConstructorCall159 = model_xbase_XConstructorCall159 if model_xbase_XConstructorCall159 is not None else set()
        self.model_xbase_XConstructorCall162 = model_xbase_XConstructorCall162 if model_xbase_XConstructorCall162 is not None else set()
        
    @property
    def invalidFeatureIssueCode(self) -> str:
        return self.__invalidFeatureIssueCode

    @invalidFeatureIssueCode.setter
    def invalidFeatureIssueCode(self, invalidFeatureIssueCode: str):
        self.__invalidFeatureIssueCode = invalidFeatureIssueCode

    @property
    def validFeature(self) -> bool:
        return self.__validFeature

    @validFeature.setter
    def validFeature(self, validFeature: bool):
        self.__validFeature = validFeature

    @property
    def model_xbase_XConstructorCall162(self):
        return self.__model_xbase_XConstructorCall162

    @model_xbase_XConstructorCall162.setter
    def model_xbase_XConstructorCall162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XConstructorCall__model_xbase_XConstructorCall162", None)
        self.__model_xbase_XConstructorCall162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference163"):
                    opp_val = getattr(item, "JvmTypeReference163", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference163"):
                    opp_val = getattr(item, "JvmTypeReference163", None)
                    
                    setattr(item, "JvmTypeReference163", self)
                    

    @property
    def model_xbase_XConstructorCall159(self):
        return self.__model_xbase_XConstructorCall159

    @model_xbase_XConstructorCall159.setter
    def model_xbase_XConstructorCall159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XConstructorCall__model_xbase_XConstructorCall159", None)
        self.__model_xbase_XConstructorCall159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression160"):
                    opp_val = getattr(item, "XExpression160", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression160"):
                    opp_val = getattr(item, "XExpression160", None)
                    
                    setattr(item, "XExpression160", self)
                    

    @property
    def model_xbase_XConstructorCall(self):
        return self.__model_xbase_XConstructorCall

    @model_xbase_XConstructorCall.setter
    def model_xbase_XConstructorCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XConstructorCall__model_xbase_XConstructorCall", None)
        self.__model_xbase_XConstructorCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmConstructor"):
                opp_val = getattr(old_value, "JvmConstructor", None)
                if opp_val == self:
                    setattr(old_value, "JvmConstructor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmConstructor"):
                opp_val = getattr(value, "JvmConstructor", None)
                setattr(value, "JvmConstructor", self)

class model_xbase_XForLoopExpression(XExpression):

    pass
class model_xbase_XArrayLiteral(XExpression):

    pass
class model_xbase_XStringLiteral(XExpression):

    def __init__(self, value: str, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_xbase_XBooleanLiteral(XExpression):

    def __init__(self, isTrue: bool, XExpression344: "model_ss_RichStringElseIf", XExpression250: "model_xbase_XPrefixOperation", XExpression104: "model_xbase_XIfExpression", XExpression238: "model_xbase_XCatchClause", XExpression334: "model_ss_RichStringIf", XExpression254: "model_xbase_XTernaryOperation", XExpression156: "model_xbase_XFeatureCall", XExpression304: "model_ss_XtendFunction", XExpression189: "model_xbase_XCastedExpression", XExpression196: "model_xbase_XUnaryOperation", XExpression267: "model_xbase_XFunctionDeclaration", XExpression246: "model_xbase_XAssignment", XExpression347: "model_ss_RichStringElseIf", XExpression114: "model_xbase_XSwitchExpression", XExpression141: "model_xbase_XAbstractFeatureCall", XExpression151: "model_xbase_XMemberFeatureCall1", XExpression252: "model_xbase_XPostfixOperation", XExpression194: "model_xbase_XBinaryOperation", XExpression116: "model_xbase_XCasePart", XExpression175: "model_xbase_XClosure", XExpression138: "model_xbase_XAbstractFeatureCall", XExpression57: "model_types_JvmConstructor", XExpression143: "model_xbase_XMemberFeatureCall", XExpression160: "model_xbase_XConstructorCall", XExpression201: "model_xbase_XForLoopExpression", XExpression220: "model_xbase_XAbstractWhileExpression", XExpression217: "model_xbase_XAbstractWhileExpression", XExpression131: "model_xbase_XVariableDeclarationList", XExpression392: "model_xannotation_XAnnotationElementValuePair", XExpression109: "model_xbase_XSwitchExpression", XExpression80: "model_types_JvmAnnotationReference", XExpression227: "model_xbase_XInstanceOfExpression", XExpression: "model_types_JvmField", XExpression198: "model_xbase_XForLoopExpression", XExpression337: "model_ss_RichStringIf", XExpression390: "model_xannotation_XAnnotation", XExpression48: "model_types_JvmField", XExpression153: "model_xbase_XFeatureCall", XExpression265: "model_xbase_XIndexOperation", XExpression248: "model_xbase_XReturnExpression", XExpression262: "model_xbase_XIndexOperation", XExpression279: "model_xbase_XObjectLiteralPart", XExpression326: "model_ss_RichStringForLoop", XExpression383: "model_ss_XtendEvent", XExpression243: "model_xbase_XAssignment", XExpression329: "model_ss_RichStringForLoop", XExpression119: "model_xbase_XCasePart", XExpression204: "model_xbase_XForLoopExpression", XExpression257: "model_xbase_XTernaryOperation", XExpression72: "model_types_JvmFormalParameter", XExpression231: "model_xbase_XTryCatchFinallyExpression", XExpression342: "model_ss_RichStringIf", XExpression431: "model_richstring_PrintedExpression", XExpression332: "model_ss_RichStringForLoop", XExpression207: "model_xbase_XForLoopExpression", XExpression167: "model_xbase_XKeyValuePair", XExpression351: "model_ss_XtendConstructor", XExpression64: "model_types_JvmOperation", XExpression101: "model_xbase_XIfExpression", XExpression170: "model_xbase_XKeyValuePair", XExpression229: "model_xbase_XThrowExpression", XExpression148: "model_xbase_XMemberFeatureCall1", XExpression67: "model_types_JvmOperation", XExpression146: "model_xbase_XMemberFeatureCall", XExpression84: "model_types_JvmAnnotationValue", XExpression129: "model_xbase_XVariableDeclaration", XExpression165: "model_xbase_XCollectionLiteral", XExpression191: "model_xbase_XBinaryOperation", XExpression212: "model_xbase_XForEachExpression", XExpression51: "model_types_JvmField", XExpression124: "model_xbase_XBlockExpression", XExpression281: "model_xbase_XArrayLiteral", XExpression322: "model_ss_XtendField", XExpression260: "model_xbase_XTernaryOperation", XExpression209: "model_xbase_XForEachExpression", XExpression234: "model_xbase_XTryCatchFinallyExpression", XExpression107: "model_xbase_XIfExpression", XExpression349: "model_ss_CreateExtensionInfo"):
        self.isTrue = isTrue
        
    @property
    def isTrue(self) -> bool:
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue

class model_xbase_XNullLiteral(XExpression):

    pass
class model_xbase_XBreakExpression(XExpression):

    pass
class types_JvmFeature:

    pass
class JvmFeature:

    pass
class model_types_JvmField(JvmFeature):

    def __init__(self, final: bool, volatile: bool, transient: bool, static: bool, model_types_JvmField: "JvmTypeReference" = None, model_types_JvmField50: "XExpression" = None, model_types_JvmField45: "XExpression" = None, model_types_JvmField47: "XExpression" = None):
        self.final = final
        self.volatile = volatile
        self.transient = transient
        self.static = static
        self.model_types_JvmField = model_types_JvmField
        self.model_types_JvmField50 = model_types_JvmField50
        self.model_types_JvmField45 = model_types_JvmField45
        self.model_types_JvmField47 = model_types_JvmField47
        
    @property
    def volatile(self) -> bool:
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def transient(self) -> bool:
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient

    @property
    def model_types_JvmField47(self):
        return self.__model_types_JvmField47

    @model_types_JvmField47.setter
    def model_types_JvmField47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField47", None)
        self.__model_types_JvmField47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression48"):
                opp_val = getattr(old_value, "XExpression48", None)
                if opp_val == self:
                    setattr(old_value, "XExpression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression48"):
                opp_val = getattr(value, "XExpression48", None)
                setattr(value, "XExpression48", self)

    @property
    def model_types_JvmField(self):
        return self.__model_types_JvmField

    @model_types_JvmField.setter
    def model_types_JvmField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField", None)
        self.__model_types_JvmField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference43"):
                opp_val = getattr(old_value, "JvmTypeReference43", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference43"):
                opp_val = getattr(value, "JvmTypeReference43", None)
                setattr(value, "JvmTypeReference43", self)

    @property
    def model_types_JvmField45(self):
        return self.__model_types_JvmField45

    @model_types_JvmField45.setter
    def model_types_JvmField45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField45", None)
        self.__model_types_JvmField45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression"):
                opp_val = getattr(old_value, "XExpression", None)
                if opp_val == self:
                    setattr(old_value, "XExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression"):
                opp_val = getattr(value, "XExpression", None)
                setattr(value, "XExpression", self)

    @property
    def model_types_JvmField50(self):
        return self.__model_types_JvmField50

    @model_types_JvmField50.setter
    def model_types_JvmField50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField50", None)
        self.__model_types_JvmField50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression51"):
                opp_val = getattr(old_value, "XExpression51", None)
                if opp_val == self:
                    setattr(old_value, "XExpression51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression51"):
                opp_val = getattr(value, "XExpression51", None)
                setattr(value, "XExpression51", self)

class types_JvmTypeReference:

    pass
class JvmAnnotationTarget:

    pass
class model_types_JvmFormalParameter(JvmAnnotationTarget):

    def __init__(self, name: str, varArg: bool, model_types_JvmFormalParameter: "JvmTypeReference" = None, model_types_JvmFormalParameter71: "XExpression" = None, JvmAnnotationTarget: "model_types_JvmMember"):
        self.name = name
        self.varArg = varArg
        self.model_types_JvmFormalParameter = model_types_JvmFormalParameter
        self.model_types_JvmFormalParameter71 = model_types_JvmFormalParameter71
        
    @property
    def varArg(self) -> bool:
        return self.__varArg

    @varArg.setter
    def varArg(self, varArg: bool):
        self.__varArg = varArg

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_types_JvmFormalParameter(self):
        return self.__model_types_JvmFormalParameter

    @model_types_JvmFormalParameter.setter
    def model_types_JvmFormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmFormalParameter__model_types_JvmFormalParameter", None)
        self.__model_types_JvmFormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference69"):
                opp_val = getattr(old_value, "JvmTypeReference69", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference69"):
                opp_val = getattr(value, "JvmTypeReference69", None)
                setattr(value, "JvmTypeReference69", self)

    @property
    def model_types_JvmFormalParameter71(self):
        return self.__model_types_JvmFormalParameter71

    @model_types_JvmFormalParameter71.setter
    def model_types_JvmFormalParameter71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmFormalParameter__model_types_JvmFormalParameter71", None)
        self.__model_types_JvmFormalParameter71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression72"):
                opp_val = getattr(old_value, "XExpression72", None)
                if opp_val == self:
                    setattr(old_value, "XExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression72"):
                opp_val = getattr(value, "XExpression72", None)
                setattr(value, "XExpression72", self)

class model_types_JvmMember(JvmAnnotationTarget):

    def __init__(self, modifiers: str, visibility: str, simpleName: str, identifier: str, JvmDeclaredType: "JvmDeclaredType" = None, model_types_JvmMember: "JvmAnnotationTarget" = None, JvmAnnotationTarget: "model_types_JvmMember"):
        self.modifiers = modifiers
        self.visibility = visibility
        self.simpleName = simpleName
        self.identifier = identifier
        self.JvmDeclaredType = JvmDeclaredType
        self.model_types_JvmMember = model_types_JvmMember
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def model_types_JvmMember(self):
        return self.__model_types_JvmMember

    @model_types_JvmMember.setter
    def model_types_JvmMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmMember__model_types_JvmMember", None)
        self.__model_types_JvmMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmAnnotationTarget"):
                opp_val = getattr(old_value, "JvmAnnotationTarget", None)
                if opp_val == self:
                    setattr(old_value, "JvmAnnotationTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmAnnotationTarget"):
                opp_val = getattr(value, "JvmAnnotationTarget", None)
                setattr(value, "JvmAnnotationTarget", self)

    @property
    def JvmDeclaredType(self):
        return self.__JvmDeclaredType

    @JvmDeclaredType.setter
    def JvmDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmMember__JvmDeclaredType", None)
        self.__JvmDeclaredType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types40"):
                opp_val = getattr(old_value, "types40", None)
                if opp_val == self:
                    setattr(old_value, "types40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types40"):
                opp_val = getattr(value, "types40", None)
                setattr(value, "types40", self)

    def internalSetIdentifier(self, identifier: str):
        # TODO: Implement internalSetIdentifier method
        pass

class JvmCompoundTypeReference:

    pass
class model_types_JvmSynonymTypeReference(JvmCompoundTypeReference):

    pass
class model_types_JvmMultiTypeReference(JvmCompoundTypeReference):

    pass
class JvmParameterizedTypeReference:

    pass
class types_JvmTypeParameterDeclarator:

    pass
class model_types_JvmExecutable(types_JvmFeature, types_JvmTypeParameterDeclarator):

    def __init__(self, varArgs: bool, model_types_JvmExecutable: set["JvmFormalParameter"] = None, model_types_JvmExecutable54: set["JvmTypeReference"] = None):
        self.varArgs = varArgs
        self.model_types_JvmExecutable = model_types_JvmExecutable if model_types_JvmExecutable is not None else set()
        self.model_types_JvmExecutable54 = model_types_JvmExecutable54 if model_types_JvmExecutable54 is not None else set()
        
    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def model_types_JvmExecutable(self):
        return self.__model_types_JvmExecutable

    @model_types_JvmExecutable.setter
    def model_types_JvmExecutable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmExecutable__model_types_JvmExecutable", None)
        self.__model_types_JvmExecutable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmFormalParameter"):
                    opp_val = getattr(item, "JvmFormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmFormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmFormalParameter"):
                    opp_val = getattr(item, "JvmFormalParameter", None)
                    
                    setattr(item, "JvmFormalParameter", self)
                    

    @property
    def model_types_JvmExecutable54(self):
        return self.__model_types_JvmExecutable54

    @model_types_JvmExecutable54.setter
    def model_types_JvmExecutable54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmExecutable__model_types_JvmExecutable54", None)
        self.__model_types_JvmExecutable54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference55"):
                    opp_val = getattr(item, "JvmTypeReference55", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference55"):
                    opp_val = getattr(item, "JvmTypeReference55", None)
                    
                    setattr(item, "JvmTypeReference55", self)
                    

class types_JvmDeclaredType:

    pass
class model_types_JvmGenericType(types_JvmDeclaredType, types_JvmTypeParameterDeclarator):

    def __init__(self, interface: bool, strictFloatingPoint: bool, model_types_JvmGenericType29: set["JvmParameterizedTypeReference"] = None, model_types_JvmGenericType: "JvmParameterizedTypeReference" = None):
        self.interface = interface
        self.strictFloatingPoint = strictFloatingPoint
        self.model_types_JvmGenericType29 = model_types_JvmGenericType29 if model_types_JvmGenericType29 is not None else set()
        self.model_types_JvmGenericType = model_types_JvmGenericType
        
    @property
    def strictFloatingPoint(self) -> bool:
        return self.__strictFloatingPoint

    @strictFloatingPoint.setter
    def strictFloatingPoint(self, strictFloatingPoint: bool):
        self.__strictFloatingPoint = strictFloatingPoint

    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def model_types_JvmGenericType(self):
        return self.__model_types_JvmGenericType

    @model_types_JvmGenericType.setter
    def model_types_JvmGenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmGenericType__model_types_JvmGenericType", None)
        self.__model_types_JvmGenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmParameterizedTypeReference"):
                opp_val = getattr(old_value, "JvmParameterizedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "JvmParameterizedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmParameterizedTypeReference"):
                opp_val = getattr(value, "JvmParameterizedTypeReference", None)
                setattr(value, "JvmParameterizedTypeReference", self)

    @property
    def model_types_JvmGenericType29(self):
        return self.__model_types_JvmGenericType29

    @model_types_JvmGenericType29.setter
    def model_types_JvmGenericType29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmGenericType__model_types_JvmGenericType29", None)
        self.__model_types_JvmGenericType29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmParameterizedTypeReference30"):
                    opp_val = getattr(item, "JvmParameterizedTypeReference30", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmParameterizedTypeReference30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmParameterizedTypeReference30"):
                    opp_val = getattr(item, "JvmParameterizedTypeReference30", None)
                    
                    setattr(item, "JvmParameterizedTypeReference30", self)
                    

    def getDeclaredConstructors(self):
        # TODO: Implement getDeclaredConstructors method
        pass

    def getExtendedInterfaces(self):
        # TODO: Implement getExtendedInterfaces method
        pass

    def isInstantiateable(self) -> bool:
        # TODO: Implement isInstantiateable method
        pass

    def getExtendedClass(self) -> str:
        # TODO: Implement getExtendedClass method
        pass

class JvmField:

    pass
class model_types_JvmEnumerationLiteral(JvmField):

    def __init__(self):
        
    def getEnumType(self) -> str:
        # TODO: Implement getEnumType method
        pass

class JvmEnumerationLiteral:

    pass
class model_types_JvmTypeReference(ABC):

    def __init__(self):
        
    def getIdentifier(self) -> str:
        # TODO: Implement getIdentifier method
        pass

    def getSimpleName(self) -> str:
        # TODO: Implement getSimpleName method
        pass

    def accept(self, visitor: str, parameter: str):
        # TODO: Implement accept method
        pass

    def getQualifiedName(self, innerClassDelimiter: str) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def accept(self, visitor: str):
        # TODO: Implement accept method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

class JvmTypeParameter:

    pass
class model_types_JvmTypeParameterDeclarator(ABC):

    pass
class JvmTypeParameterDeclarator:

    pass
class types_JvmConstraintOwner:

    pass
class model_types_JvmWildcardTypeReference(types_JvmConstraintOwner, types_JvmTypeReference):

    pass
class JvmMember:

    pass
class model_types_JvmFeature(JvmMember):

    def __init__(self, types15: "model_types_JvmDeclaredType"):
        
    def isStatic(self) -> bool:
        # TODO: Implement isStatic method
        pass

class JvmDeclaredType:

    pass
class model_types_JvmEnumerationType(JvmDeclaredType):

    pass
class model_types_JvmAnnotationType(JvmDeclaredType):

    pass
class JvmConstraintOwner:

    pass
class model_types_JvmTypeConstraint(ABC):

    def __init__(self, model_types_JvmTypeConstraint: "JvmTypeReference" = None, JvmConstraintOwner: "JvmConstraintOwner" = None):
        self.model_types_JvmTypeConstraint = model_types_JvmTypeConstraint
        self.JvmConstraintOwner = JvmConstraintOwner
        
    @property
    def JvmConstraintOwner(self):
        return self.__JvmConstraintOwner

    @JvmConstraintOwner.setter
    def JvmConstraintOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmTypeConstraint__JvmConstraintOwner", None)
        self.__JvmConstraintOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types25"):
                opp_val = getattr(old_value, "types25", None)
                if opp_val == self:
                    setattr(old_value, "types25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types25"):
                opp_val = getattr(value, "types25", None)
                setattr(value, "types25", self)

    @property
    def model_types_JvmTypeConstraint(self):
        return self.__model_types_JvmTypeConstraint

    @model_types_JvmTypeConstraint.setter
    def model_types_JvmTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmTypeConstraint__model_types_JvmTypeConstraint", None)
        self.__model_types_JvmTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference23"):
                opp_val = getattr(old_value, "JvmTypeReference23", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference23"):
                opp_val = getattr(value, "JvmTypeReference23", None)
                setattr(value, "JvmTypeReference23", self)

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getIdentifier(self) -> str:
        # TODO: Implement getIdentifier method
        pass

    def getSimpleName(self) -> str:
        # TODO: Implement getSimpleName method
        pass

    def getQualifiedName(self, innerClassDelimiter: str) -> str:
        # TODO: Implement getQualifiedName method
        pass

class JvmTypeConstraint:

    pass
class model_types_JvmLowerBound(JvmTypeConstraint):

    pass
class model_types_JvmUpperBound(JvmTypeConstraint):

    pass
class model_types_JvmConstraintOwner(ABC):

    pass
class JvmComponentType:

    pass
class model_types_JvmPrimitiveType(JvmComponentType):

    def __init__(self, simpleName: str, types12: "model_types_JvmArrayType"):
        self.simpleName = simpleName
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

class JvmArrayType:

    pass
class JvmType:

    pass
class model_types_JvmComponentType(JvmType):

    pass
class model_types_JvmVoid(JvmType):

    pass
class model_types_JvmNoModule:

    pass
class JvmTypeReference:

    pass
class model_types_JvmDelegateTypeReference(JvmTypeReference):

    pass
class model_types_JvmAnyTypeReference(JvmTypeReference):

    pass
class model_types_JvmSpecializedTypeReference(JvmTypeReference):

    pass
class model_types_JvmParameterizedTypeReference(JvmTypeReference):

    pass
class model_types_JvmCompoundTypeReference(JvmTypeReference):

    pass
class model_types_JvmGenericArrayTypeReference(JvmTypeReference):

    def __init__(self, model_types_JvmGenericArrayTypeReference: "JvmTypeReference" = None, JvmTypeReference99: "model_types_JvmCompoundTypeReference", JvmTypeReference36: "model_types_JvmGenericArrayTypeReference", JvmTypeReference369: "model_ss_XtendDelegate", JvmTypeReference135: "model_xbase_XAbstractFeatureCall", JvmTypeReference186: "model_xbase_XCastedExpression", JvmTypeReference292: "model_ss_XtendClass", JvmTypeReference224: "model_xbase_XInstanceOfExpression", JvmTypeReference126: "model_xbase_XVariableDeclaration", JvmTypeReference360: "model_ss_XtendConstructor", JvmTypeReference400: "model_xtype_XFunctionTypeRef", JvmTypeReference69: "model_types_JvmFormalParameter", JvmTypeReference319: "model_ss_XtendField", JvmTypeReference: "model_types_JvmDeclaredType", JvmTypeReference59: "model_types_JvmOperation", JvmTypeReference23: "model_types_JvmTypeConstraint", JvmTypeReference94: "model_types_JvmSpecializedTypeReference", JvmTypeReference181: "model_xbase_XClosure", JvmTypeReference122: "model_xbase_XCasePart", JvmTypeReference163: "model_xbase_XConstructorCall", JvmTypeReference92: "model_types_JvmDelegateTypeReference", JvmTypeReference364: "model_ss_XtendInterface", JvmTypeReference380: "model_ss_XtendEvent", JvmTypeReference397: "model_xtype_XFunctionTypeRef", JvmTypeReference295: "model_ss_XtendClass", JvmTypeReference270: "model_xbase_XFunctionDeclaration", JvmTypeReference324: "model_ss_XtendParameter", JvmTypeReference317: "model_ss_XtendFunction", JvmTypeReference307: "model_ss_XtendFunction", JvmTypeReference32: "model_types_JvmParameterizedTypeReference", JvmTypeReference378: "model_ss_XtendDelegate", JvmTypeReference55: "model_types_JvmExecutable", JvmTypeReference86: "model_types_JvmTypeAnnotationValue", JvmTypeReference43: "model_types_JvmField"):
        self.model_types_JvmGenericArrayTypeReference = model_types_JvmGenericArrayTypeReference
        
    @property
    def model_types_JvmGenericArrayTypeReference(self):
        return self.__model_types_JvmGenericArrayTypeReference

    @model_types_JvmGenericArrayTypeReference.setter
    def model_types_JvmGenericArrayTypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmGenericArrayTypeReference__model_types_JvmGenericArrayTypeReference", None)
        self.__model_types_JvmGenericArrayTypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference36"):
                opp_val = getattr(old_value, "JvmTypeReference36", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference36"):
                opp_val = getattr(value, "JvmTypeReference36", None)
                setattr(value, "JvmTypeReference36", self)

    def getDimensions(self) -> int:
        # TODO: Implement getDimensions method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

class model_types_JvmUnknownTypeReference(JvmTypeReference):

    def __init__(self, qualifiedName: str, JvmTypeReference99: "model_types_JvmCompoundTypeReference", JvmTypeReference36: "model_types_JvmGenericArrayTypeReference", JvmTypeReference369: "model_ss_XtendDelegate", JvmTypeReference135: "model_xbase_XAbstractFeatureCall", JvmTypeReference186: "model_xbase_XCastedExpression", JvmTypeReference292: "model_ss_XtendClass", JvmTypeReference224: "model_xbase_XInstanceOfExpression", JvmTypeReference126: "model_xbase_XVariableDeclaration", JvmTypeReference360: "model_ss_XtendConstructor", JvmTypeReference400: "model_xtype_XFunctionTypeRef", JvmTypeReference69: "model_types_JvmFormalParameter", JvmTypeReference319: "model_ss_XtendField", JvmTypeReference: "model_types_JvmDeclaredType", JvmTypeReference59: "model_types_JvmOperation", JvmTypeReference23: "model_types_JvmTypeConstraint", JvmTypeReference94: "model_types_JvmSpecializedTypeReference", JvmTypeReference181: "model_xbase_XClosure", JvmTypeReference122: "model_xbase_XCasePart", JvmTypeReference163: "model_xbase_XConstructorCall", JvmTypeReference92: "model_types_JvmDelegateTypeReference", JvmTypeReference364: "model_ss_XtendInterface", JvmTypeReference380: "model_ss_XtendEvent", JvmTypeReference397: "model_xtype_XFunctionTypeRef", JvmTypeReference295: "model_ss_XtendClass", JvmTypeReference270: "model_xbase_XFunctionDeclaration", JvmTypeReference324: "model_ss_XtendParameter", JvmTypeReference317: "model_ss_XtendFunction", JvmTypeReference307: "model_ss_XtendFunction", JvmTypeReference32: "model_types_JvmParameterizedTypeReference", JvmTypeReference378: "model_ss_XtendDelegate", JvmTypeReference55: "model_types_JvmExecutable", JvmTypeReference86: "model_types_JvmTypeAnnotationValue", JvmTypeReference43: "model_types_JvmField"):
        self.qualifiedName = qualifiedName
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class types_JvmComponentType:

    pass
class model_types_JvmTypeParameter(types_JvmConstraintOwner, types_JvmComponentType):

    def __init__(self, name: str, JvmTypeParameterDeclarator: "JvmTypeParameterDeclarator" = None):
        self.name = name
        self.JvmTypeParameterDeclarator = JvmTypeParameterDeclarator
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JvmTypeParameterDeclarator(self):
        return self.__JvmTypeParameterDeclarator

    @JvmTypeParameterDeclarator.setter
    def JvmTypeParameterDeclarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmTypeParameter__JvmTypeParameterDeclarator", None)
        self.__JvmTypeParameterDeclarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types17"):
                opp_val = getattr(old_value, "types17", None)
                if opp_val == self:
                    setattr(old_value, "types17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types17"):
                opp_val = getattr(value, "types17", None)
                setattr(value, "types17", self)

class types_JvmMember:

    pass
class model_types_JvmDeclaredType(types_JvmComponentType, types_JvmMember):

    def __init__(self, abstract: bool, static: bool, final: bool, packageName: str, exported: bool, model_types_JvmDeclaredType: set["JvmTypeReference"] = None, JvmMember: set["JvmMember"] = None):
        self.abstract = abstract
        self.static = static
        self.final = final
        self.packageName = packageName
        self.exported = exported
        self.model_types_JvmDeclaredType = model_types_JvmDeclaredType if model_types_JvmDeclaredType is not None else set()
        self.JvmMember = JvmMember if JvmMember is not None else set()
        
    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def final(self) -> bool:
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def model_types_JvmDeclaredType(self):
        return self.__model_types_JvmDeclaredType

    @model_types_JvmDeclaredType.setter
    def model_types_JvmDeclaredType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmDeclaredType__model_types_JvmDeclaredType", None)
        self.__model_types_JvmDeclaredType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference"):
                    opp_val = getattr(item, "JvmTypeReference", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference"):
                    opp_val = getattr(item, "JvmTypeReference", None)
                    
                    setattr(item, "JvmTypeReference", self)
                    

    @property
    def JvmMember(self):
        return self.__JvmMember

    @JvmMember.setter
    def JvmMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmDeclaredType__JvmMember", None)
        self.__JvmMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types15"):
                    opp_val = getattr(item, "types15", None)
                    
                    if opp_val == self:
                        setattr(item, "types15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types15"):
                    opp_val = getattr(item, "types15", None)
                    
                    setattr(item, "types15", self)
                    

    def getAllFeatures(self):
        # TODO: Implement getAllFeatures method
        pass

    def getDeclaredFields(self):
        # TODO: Implement getDeclaredFields method
        pass

    def getDeclaredOperations(self):
        # TODO: Implement getDeclaredOperations method
        pass

    def findAllFeaturesByName(self, simpleName: str):
        # TODO: Implement findAllFeaturesByName method
        pass

class model_types_JvmArrayType(JvmComponentType):

    def __init__(self, JvmComponentType: "JvmComponentType" = None, types12: "model_types_JvmArrayType"):
        self.JvmComponentType = JvmComponentType
        
    @property
    def JvmComponentType(self):
        return self.__JvmComponentType

    @JvmComponentType.setter
    def JvmComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmArrayType__JvmComponentType", None)
        self.__JvmComponentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types12"):
                opp_val = getattr(old_value, "types12", None)
                if opp_val == self:
                    setattr(old_value, "types12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types12"):
                opp_val = getattr(value, "types12", None)
                setattr(value, "types12", self)

    def getDimensions(self) -> int:
        # TODO: Implement getDimensions method
        pass

class model_types_JvmIdentifiableElement(ABC):

    def __init__(self):
        
    def getIdentifier(self) -> str:
        # TODO: Implement getIdentifier method
        pass

    def isExported(self) -> bool:
        # TODO: Implement isExported method
        pass

    def getQualifiedName(self) -> str:
        # TODO: Implement getQualifiedName method
        pass

    def getSimpleName(self) -> str:
        # TODO: Implement getSimpleName method
        pass

    def getQualifiedName(self, innerClassDelimiter: str) -> str:
        # TODO: Implement getQualifiedName method
        pass

class XExportSection:

    pass
class types_model_EObject:

    pass
class XImportSection1:

    pass
class JvmIdentifiableElement:

    pass
class model_types_JvmAnnotationTarget(JvmIdentifiableElement):

    pass
class model_types_JvmType(JvmIdentifiableElement):

    pass
class model_types_JvmModule(JvmIdentifiableElement):

    def __init__(self, simpleName: str, model_types_JvmModule: "XImportSection1" = None, model_types_JvmModule2: set["types_model_EObject"] = None, model_types_JvmModule4: "XExportSection" = None, JvmIdentifiableElement410: "model_xtype_XImportItem", JvmIdentifiableElement: "model_xbase_XAbstractFeatureCall", JvmIdentifiableElement414: "model_xtype_XExportItem"):
        self.simpleName = simpleName
        self.model_types_JvmModule = model_types_JvmModule
        self.model_types_JvmModule2 = model_types_JvmModule2 if model_types_JvmModule2 is not None else set()
        self.model_types_JvmModule4 = model_types_JvmModule4
        
    @property
    def simpleName(self) -> str:
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName

    @property
    def model_types_JvmModule2(self):
        return self.__model_types_JvmModule2

    @model_types_JvmModule2.setter
    def model_types_JvmModule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmModule__model_types_JvmModule2", None)
        self.__model_types_JvmModule2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_model_EObject"):
                    opp_val = getattr(item, "types_model_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "types_model_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_model_EObject"):
                    opp_val = getattr(item, "types_model_EObject", None)
                    
                    setattr(item, "types_model_EObject", self)
                    

    @property
    def model_types_JvmModule4(self):
        return self.__model_types_JvmModule4

    @model_types_JvmModule4.setter
    def model_types_JvmModule4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmModule__model_types_JvmModule4", None)
        self.__model_types_JvmModule4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExportSection"):
                opp_val = getattr(old_value, "XExportSection", None)
                if opp_val == self:
                    setattr(old_value, "XExportSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExportSection"):
                opp_val = getattr(value, "XExportSection", None)
                setattr(value, "XExportSection", self)

    @property
    def model_types_JvmModule(self):
        return self.__model_types_JvmModule

    @model_types_JvmModule.setter
    def model_types_JvmModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmModule__model_types_JvmModule", None)
        self.__model_types_JvmModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XImportSection1"):
                opp_val = getattr(old_value, "XImportSection1", None)
                if opp_val == self:
                    setattr(old_value, "XImportSection1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XImportSection1"):
                opp_val = getattr(value, "XImportSection1", None)
                setattr(value, "XImportSection1", self)
