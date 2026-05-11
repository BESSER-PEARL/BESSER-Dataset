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

class IfConditionStart:

    pass
class Line:

    pass
class RichString:

    pass
class model_richstring_ProcessedRichString:

    pass
class model_xtype_XExportItem:

    def __init__(self, alias: str, model_xtype_XExportItem: "JvmIdentifiableElement" = None):
        self.alias = alias
        self.model_xtype_XExportItem = model_xtype_XExportItem
        
        pass
    @property
    def alias(self):
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
            if hasattr(old_value, "JvmIdentifiableElement408"):
                opp_val = getattr(old_value, "JvmIdentifiableElement408", None)
                if opp_val == self:
                    setattr(old_value, "JvmIdentifiableElement408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmIdentifiableElement408"):
                opp_val = getattr(value, "JvmIdentifiableElement408", None)
                setattr(value, "JvmIdentifiableElement408", self)

class EndIf:

    pass
class ElseIfCondition:

    pass
class ElseStart:

    pass
class RichStringIf:

    pass
class ForLoopStart:

    pass
class ForLoopEnd:

    pass
class RichStringForLoop:

    pass
class Literal:

    pass
class model_richstring_LineBreak(Literal):

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
class model_richstring_EndIf(LinePart):

    pass
class model_richstring_IfConditionStart(LinePart):

    pass
class model_richstring_Literal(LinePart):

    def __init__(self, offset: int, length: int, model_richstring_Literal: "RichStringLiteral" = None, LinePart: "model_richstring_Line" = None):
        self.offset = offset
        self.length = length
        self.model_richstring_Literal = model_richstring_Literal
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def offset(self):
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

class model_richstring_PrintedExpression(LinePart):

    pass
class model_richstring_ElseStart(LinePart):

    pass
class model_richstring_ForLoopEnd(LinePart):

    pass
class model_richstring_Line:

    pass
class XImportDeclaration1:

    pass
class model_xtype_XImportSection1:

    pass
class model_xtype_XImportDeclaration:

    def __init__(self, extension: bool, static: bool, importedNamespace: str, wildcard: bool, model_xtype_XImportDeclaration: "JvmDeclaredType" = None):
        self.extension = extension
        self.static = static
        self.importedNamespace = importedNamespace
        self.wildcard = wildcard
        self.model_xtype_XImportDeclaration = model_xtype_XImportDeclaration
        
        pass
    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def wildcard(self):
        return self.__wildcard

    @wildcard.setter
    def wildcard(self, wildcard: bool):
        self.__wildcard = wildcard


    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


    @property
    def importedNamespace(self):
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace


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
            if hasattr(old_value, "JvmDeclaredType400"):
                opp_val = getattr(old_value, "JvmDeclaredType400", None)
                if opp_val == self:
                    setattr(old_value, "JvmDeclaredType400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmDeclaredType400"):
                opp_val = getattr(value, "JvmDeclaredType400", None)
                setattr(value, "JvmDeclaredType400", self)

    def getImportedTypeName(self) :
        # TODO: Implement getImportedTypeName method
        pass

class XImportDeclaration:

    pass
class XExportItem:

    pass
class model_xtype_XExportDeclaration:

    def __init__(self, alias: str, wildcard: bool, importURI: str, model_xtype_XExportDeclaration: set["XExportItem"] = None):
        self.alias = alias
        self.wildcard = wildcard
        self.importURI = importURI
        self.model_xtype_XExportDeclaration = model_xtype_XExportDeclaration if model_xtype_XExportDeclaration is not None else set()
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def importURI(self):
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI


    @property
    def wildcard(self):
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
                    

class XExportDeclaration:

    pass
class model_xtype_XExportSection:

    pass
class model_xtype_XImportItem:

    def __init__(self, alias: str, model_xtype_XImportItem: "JvmIdentifiableElement" = None):
        self.alias = alias
        self.model_xtype_XImportItem = model_xtype_XImportItem
        
        pass
    @property
    def alias(self):
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
            if hasattr(old_value, "JvmIdentifiableElement404"):
                opp_val = getattr(old_value, "JvmIdentifiableElement404", None)
                if opp_val == self:
                    setattr(old_value, "JvmIdentifiableElement404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmIdentifiableElement404"):
                opp_val = getattr(value, "JvmIdentifiableElement404", None)
                setattr(value, "JvmIdentifiableElement404", self)

class XImportItem:

    pass
class model_xtype_XImportDeclaration1:

    def __init__(self, alias: str, importURI: str, model_xtype_XImportDeclaration1: set["XImportItem"] = None):
        self.alias = alias
        self.importURI = importURI
        self.model_xtype_XImportDeclaration1 = model_xtype_XImportDeclaration1 if model_xtype_XImportDeclaration1 is not None else set()
        
        pass
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def importURI(self):
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
                    

    def isWildcard(self) :
        # TODO: Implement isWildcard method
        pass

class XAnnotationElementValuePair:

    pass
class model_xtype_XImportSection:

    pass
class JvmSpecializedTypeReference:

    pass
class model_xtype_XComputedTypeReference(JvmSpecializedTypeReference):

    def __init__(self, typeProvider: str):
        self.typeProvider = typeProvider
        
        pass
    @property
    def typeProvider(self):
        return self.__typeProvider

    @typeProvider.setter
    def typeProvider(self, typeProvider: str):
        self.__typeProvider = typeProvider


class model_xtype_XFunctionTypeRef(JvmSpecializedTypeReference):

    def __init__(self, instanceContext: bool, model_xtype_XFunctionTypeRef: set["JvmTypeReference"] = None, model_xtype_XFunctionTypeRef393: "JvmTypeReference" = None, model_xtype_XFunctionTypeRef396: "JvmType" = None):
        self.instanceContext = instanceContext
        self.model_xtype_XFunctionTypeRef = model_xtype_XFunctionTypeRef if model_xtype_XFunctionTypeRef is not None else set()
        self.model_xtype_XFunctionTypeRef393 = model_xtype_XFunctionTypeRef393
        self.model_xtype_XFunctionTypeRef396 = model_xtype_XFunctionTypeRef396
        
        pass
    @property
    def instanceContext(self):
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
                if hasattr(item, "JvmTypeReference391"):
                    opp_val = getattr(item, "JvmTypeReference391", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference391", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference391"):
                    opp_val = getattr(item, "JvmTypeReference391", None)
                    
                    setattr(item, "JvmTypeReference391", self)
                    

    @property
    def model_xtype_XFunctionTypeRef393(self):
        return self.__model_xtype_XFunctionTypeRef393

    @model_xtype_XFunctionTypeRef393.setter
    def model_xtype_XFunctionTypeRef393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XFunctionTypeRef__model_xtype_XFunctionTypeRef393", None)
        self.__model_xtype_XFunctionTypeRef393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference394"):
                opp_val = getattr(old_value, "JvmTypeReference394", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference394", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference394"):
                opp_val = getattr(value, "JvmTypeReference394", None)
                setattr(value, "JvmTypeReference394", self)

    @property
    def model_xtype_XFunctionTypeRef396(self):
        return self.__model_xtype_XFunctionTypeRef396

    @model_xtype_XFunctionTypeRef396.setter
    def model_xtype_XFunctionTypeRef396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xtype_XFunctionTypeRef__model_xtype_XFunctionTypeRef396", None)
        self.__model_xtype_XFunctionTypeRef396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmType397"):
                opp_val = getattr(old_value, "JvmType397", None)
                if opp_val == self:
                    setattr(old_value, "JvmType397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmType397"):
                opp_val = getattr(value, "JvmType397", None)
                setattr(value, "JvmType397", self)

class model_xannotation_XAnnotationElementValuePair:

    pass
class XVariableDeclaration:

    pass
class model_ss_XtendVariableDeclaration(XVariableDeclaration):

    def __init__(self, extension: bool):
        self.extension = extension
        
        pass
    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


class model_ss_CreateExtensionInfo:

    def __init__(self, name: str, model_ss_CreateExtensionInfo: "XExpression" = None):
        self.name = name
        self.model_ss_CreateExtensionInfo = model_ss_CreateExtensionInfo
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "XExpression343"):
                opp_val = getattr(old_value, "XExpression343", None)
                if opp_val == self:
                    setattr(old_value, "XExpression343", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression343"):
                opp_val = getattr(value, "XExpression343", None)
                setattr(value, "XExpression343", self)

class model_ss_RichStringElseIf:

    pass
class RichStringElseIf:

    pass
class XBlockExpression:

    pass
class model_ss_RichString(XBlockExpression):

    pass
class XForEachExpression:

    pass
class model_ss_RichStringForLoop(XForEachExpression):

    pass
class XStringLiteral:

    pass
class model_ss_RichStringLiteral(XStringLiteral):

    pass
class CreateExtensionInfo:

    pass
class XtendParameter:

    pass
class XtendMember:

    pass
class model_ss_XtendEvent(XtendMember):

    def __init__(self, name: str, model_ss_XtendEvent: "JvmTypeReference" = None, model_ss_XtendEvent376: "XExpression" = None, XtendMember: "model_ss_XtendTypeDeclaration" = None):
        self.name = name
        self.model_ss_XtendEvent = model_ss_XtendEvent
        self.model_ss_XtendEvent376 = model_ss_XtendEvent376
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "JvmTypeReference374"):
                opp_val = getattr(old_value, "JvmTypeReference374", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference374"):
                opp_val = getattr(value, "JvmTypeReference374", None)
                setattr(value, "JvmTypeReference374", self)

    @property
    def model_ss_XtendEvent376(self):
        return self.__model_ss_XtendEvent376

    @model_ss_XtendEvent376.setter
    def model_ss_XtendEvent376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendEvent__model_ss_XtendEvent376", None)
        self.__model_ss_XtendEvent376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression377"):
                opp_val = getattr(old_value, "XExpression377", None)
                if opp_val == self:
                    setattr(old_value, "XExpression377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression377"):
                opp_val = getattr(value, "XExpression377", None)
                setattr(value, "XExpression377", self)

    def isExtension(self) :
        # TODO: Implement isExtension method
        pass

class model_ss_XtendTypeDeclaration(XtendMember):

    def __init__(self, name: str, declaringType356: set["XtendMember"] = None, XtendMember: "model_ss_XtendTypeDeclaration" = None):
        self.name = name
        self.declaringType356 = declaringType356 if declaringType356 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def declaringType356(self):
        return self.__declaringType356

    @declaringType356.setter
    def declaringType356(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendTypeDeclaration__declaringType356", None)
        self.__declaringType356 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XtendMember"):
                    opp_val = getattr(item, "XtendMember", None)
                    
                    if opp_val == self:
                        setattr(item, "XtendMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XtendMember"):
                    opp_val = getattr(item, "XtendMember", None)
                    
                    setattr(item, "XtendMember", self)
                    

class model_ss_XtendConstructor(XtendMember):

    pass
class model_ss_XtendEnumLiteral(XtendMember):

    def __init__(self, name: str, XtendMember: "model_ss_XtendTypeDeclaration" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class model_ss_XtendField(XtendMember):

    def __init__(self, name: str, model_ss_XtendField: "JvmTypeReference" = None, model_ss_XtendField315: "XExpression" = None, XtendMember: "model_ss_XtendTypeDeclaration" = None):
        self.name = name
        self.model_ss_XtendField = model_ss_XtendField
        self.model_ss_XtendField315 = model_ss_XtendField315
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model_ss_XtendField315(self):
        return self.__model_ss_XtendField315

    @model_ss_XtendField315.setter
    def model_ss_XtendField315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendField__model_ss_XtendField315", None)
        self.__model_ss_XtendField315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression316"):
                opp_val = getattr(old_value, "XExpression316", None)
                if opp_val == self:
                    setattr(old_value, "XExpression316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression316"):
                opp_val = getattr(value, "XExpression316", None)
                setattr(value, "XExpression316", self)

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
            if hasattr(old_value, "JvmTypeReference313"):
                opp_val = getattr(old_value, "JvmTypeReference313", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference313"):
                opp_val = getattr(value, "JvmTypeReference313", None)
                setattr(value, "JvmTypeReference313", self)

    def isExtension(self) :
        # TODO: Implement isExtension method
        pass

class model_ss_XtendFunction(XtendMember):

    def __init__(self, name: str, model_ss_XtendFunction310: set["JvmTypeReference"] = None, model_ss_XtendFunction300: "JvmTypeReference" = None, model_ss_XtendFunction: "XExpression" = None, model_ss_XtendFunction307: set["JvmTypeParameter"] = None, model_ss_XtendFunction303: set["XtendParameter"] = None, model_ss_XtendFunction305: "CreateExtensionInfo" = None, XtendMember: "model_ss_XtendTypeDeclaration" = None):
        self.name = name
        self.model_ss_XtendFunction310 = model_ss_XtendFunction310 if model_ss_XtendFunction310 is not None else set()
        self.model_ss_XtendFunction300 = model_ss_XtendFunction300
        self.model_ss_XtendFunction = model_ss_XtendFunction
        self.model_ss_XtendFunction307 = model_ss_XtendFunction307 if model_ss_XtendFunction307 is not None else set()
        self.model_ss_XtendFunction303 = model_ss_XtendFunction303 if model_ss_XtendFunction303 is not None else set()
        self.model_ss_XtendFunction305 = model_ss_XtendFunction305
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model_ss_XtendFunction303(self):
        return self.__model_ss_XtendFunction303

    @model_ss_XtendFunction303.setter
    def model_ss_XtendFunction303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction303", None)
        self.__model_ss_XtendFunction303 = value if value is not None else set()
        
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
                    

    @property
    def model_ss_XtendFunction307(self):
        return self.__model_ss_XtendFunction307

    @model_ss_XtendFunction307.setter
    def model_ss_XtendFunction307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction307", None)
        self.__model_ss_XtendFunction307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeParameter308"):
                    opp_val = getattr(item, "JvmTypeParameter308", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeParameter308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeParameter308"):
                    opp_val = getattr(item, "JvmTypeParameter308", None)
                    
                    setattr(item, "JvmTypeParameter308", self)
                    

    @property
    def model_ss_XtendFunction300(self):
        return self.__model_ss_XtendFunction300

    @model_ss_XtendFunction300.setter
    def model_ss_XtendFunction300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction300", None)
        self.__model_ss_XtendFunction300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference301"):
                opp_val = getattr(old_value, "JvmTypeReference301", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference301"):
                opp_val = getattr(value, "JvmTypeReference301", None)
                setattr(value, "JvmTypeReference301", self)

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
            if hasattr(old_value, "XExpression298"):
                opp_val = getattr(old_value, "XExpression298", None)
                if opp_val == self:
                    setattr(old_value, "XExpression298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression298"):
                opp_val = getattr(value, "XExpression298", None)
                setattr(value, "XExpression298", self)

    @property
    def model_ss_XtendFunction310(self):
        return self.__model_ss_XtendFunction310

    @model_ss_XtendFunction310.setter
    def model_ss_XtendFunction310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction310", None)
        self.__model_ss_XtendFunction310 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference311"):
                    opp_val = getattr(item, "JvmTypeReference311", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference311", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference311"):
                    opp_val = getattr(item, "JvmTypeReference311", None)
                    
                    setattr(item, "JvmTypeReference311", self)
                    

    @property
    def model_ss_XtendFunction305(self):
        return self.__model_ss_XtendFunction305

    @model_ss_XtendFunction305.setter
    def model_ss_XtendFunction305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFunction__model_ss_XtendFunction305", None)
        self.__model_ss_XtendFunction305 = value
        
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

    def isAbstract(self) :
        # TODO: Implement isAbstract method
        pass

    def isOverride(self) :
        # TODO: Implement isOverride method
        pass

    def isDispatch(self) :
        # TODO: Implement isDispatch method
        pass

class XtendAnnotationTarget:

    pass
class model_ss_XtendParameter(XtendAnnotationTarget):

    def __init__(self, name: str, varArg: bool, extension: bool, model_ss_XtendParameter: "JvmTypeReference" = None, XtendAnnotationTarget: "model_ss_XtendMember" = None):
        self.name = name
        self.varArg = varArg
        self.extension = extension
        self.model_ss_XtendParameter = model_ss_XtendParameter
        
        pass
    @property
    def varArg(self):
        return self.__varArg

    @varArg.setter
    def varArg(self, varArg: bool):
        self.__varArg = varArg


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


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
            if hasattr(old_value, "JvmTypeReference318"):
                opp_val = getattr(old_value, "JvmTypeReference318", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference318"):
                opp_val = getattr(value, "JvmTypeReference318", None)
                setattr(value, "JvmTypeReference318", self)

class model_ss_XtendMember(XtendAnnotationTarget):

    def __init__(self, modifiers: str, model_ss_XtendMember: "XtendAnnotationTarget" = None, members295: "XtendTypeDeclaration" = None, XtendAnnotationTarget: "model_ss_XtendMember" = None):
        self.modifiers = modifiers
        self.model_ss_XtendMember = model_ss_XtendMember
        self.members295 = members295
        
        pass
    @property
    def modifiers(self):
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers


    @property
    def members295(self):
        return self.__members295

    @members295.setter
    def members295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendMember__members295", None)
        self.__members295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XtendTypeDeclaration296"):
                opp_val = getattr(old_value, "XtendTypeDeclaration296", None)
                if opp_val == self:
                    setattr(old_value, "XtendTypeDeclaration296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XtendTypeDeclaration296"):
                opp_val = getattr(value, "XtendTypeDeclaration296", None)
                setattr(value, "XtendTypeDeclaration296", self)

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

    def isFinal(self) :
        # TODO: Implement isFinal method
        pass

    def getVisibility(self) :
        # TODO: Implement getVisibility method
        pass

    def getDeclaredVisibility(self) :
        # TODO: Implement getDeclaredVisibility method
        pass

    def isStatic(self) :
        # TODO: Implement isStatic method
        pass

class XAnnotation:

    pass
class model_ss_XtendAnnotationTarget(ABC):

    pass
class XObjectLiteralPart:

    pass
class ss_model_EObject:

    pass
class XtendTypeDeclaration:

    pass
class model_ss_XtendEnum(XtendTypeDeclaration):

    pass
class model_ss_XtendInterface(XtendTypeDeclaration):

    pass
class model_ss_XtendAnnotationType(XtendTypeDeclaration):

    pass
class model_ss_XtendDelegate(XtendTypeDeclaration):

    pass
class model_ss_XtendClass(XtendTypeDeclaration):

    def __init__(self, model_ss_XtendClass290: set["JvmTypeParameter"] = None, model_ss_XtendClass: "JvmTypeReference" = None, model_ss_XtendClass287: set["JvmTypeReference"] = None, XtendTypeDeclaration: "model_ss_XtendFile" = None, XtendTypeDeclaration296: "model_ss_XtendMember" = None):
        self.model_ss_XtendClass290 = model_ss_XtendClass290 if model_ss_XtendClass290 is not None else set()
        self.model_ss_XtendClass = model_ss_XtendClass
        self.model_ss_XtendClass287 = model_ss_XtendClass287 if model_ss_XtendClass287 is not None else set()
        
        pass
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
            if hasattr(old_value, "JvmTypeReference285"):
                opp_val = getattr(old_value, "JvmTypeReference285", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference285"):
                opp_val = getattr(value, "JvmTypeReference285", None)
                setattr(value, "JvmTypeReference285", self)

    @property
    def model_ss_XtendClass290(self):
        return self.__model_ss_XtendClass290

    @model_ss_XtendClass290.setter
    def model_ss_XtendClass290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendClass__model_ss_XtendClass290", None)
        self.__model_ss_XtendClass290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeParameter291"):
                    opp_val = getattr(item, "JvmTypeParameter291", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeParameter291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeParameter291"):
                    opp_val = getattr(item, "JvmTypeParameter291", None)
                    
                    setattr(item, "JvmTypeParameter291", self)
                    

    @property
    def model_ss_XtendClass287(self):
        return self.__model_ss_XtendClass287

    @model_ss_XtendClass287.setter
    def model_ss_XtendClass287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendClass__model_ss_XtendClass287", None)
        self.__model_ss_XtendClass287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference288"):
                    opp_val = getattr(item, "JvmTypeReference288", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference288"):
                    opp_val = getattr(item, "JvmTypeReference288", None)
                    
                    setattr(item, "JvmTypeReference288", self)
                    

    def isAbstract(self) :
        # TODO: Implement isAbstract method
        pass

class model_ss_XtendFile:

    def __init__(self, package: str, model_ss_XtendFile: "XImportSection1" = None, model_ss_XtendFile278: set["XtendTypeDeclaration"] = None, model_ss_XtendFile280: set["ss_model_EObject"] = None, model_ss_XtendFile282: "XExportSection" = None):
        self.package = package
        self.model_ss_XtendFile = model_ss_XtendFile
        self.model_ss_XtendFile278 = model_ss_XtendFile278 if model_ss_XtendFile278 is not None else set()
        self.model_ss_XtendFile280 = model_ss_XtendFile280 if model_ss_XtendFile280 is not None else set()
        self.model_ss_XtendFile282 = model_ss_XtendFile282
        
        pass
    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package


    @property
    def model_ss_XtendFile280(self):
        return self.__model_ss_XtendFile280

    @model_ss_XtendFile280.setter
    def model_ss_XtendFile280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile280", None)
        self.__model_ss_XtendFile280 = value if value is not None else set()
        
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
            if hasattr(old_value, "XImportSection1276"):
                opp_val = getattr(old_value, "XImportSection1276", None)
                if opp_val == self:
                    setattr(old_value, "XImportSection1276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XImportSection1276"):
                opp_val = getattr(value, "XImportSection1276", None)
                setattr(value, "XImportSection1276", self)

    @property
    def model_ss_XtendFile278(self):
        return self.__model_ss_XtendFile278

    @model_ss_XtendFile278.setter
    def model_ss_XtendFile278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile278", None)
        self.__model_ss_XtendFile278 = value if value is not None else set()
        
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
                    

    @property
    def model_ss_XtendFile282(self):
        return self.__model_ss_XtendFile282

    @model_ss_XtendFile282.setter
    def model_ss_XtendFile282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ss_XtendFile__model_ss_XtendFile282", None)
        self.__model_ss_XtendFile282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExportSection283"):
                opp_val = getattr(old_value, "XExportSection283", None)
                if opp_val == self:
                    setattr(old_value, "XExportSection283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExportSection283"):
                opp_val = getattr(value, "XExportSection283", None)
                setattr(value, "XExportSection283", self)

class model_xbase_XObjectLiteralPart:

    def __init__(self, name: str, model_xbase_XObjectLiteralPart: "XExpression" = None):
        self.name = name
        self.model_xbase_XObjectLiteralPart = model_xbase_XObjectLiteralPart
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "XExpression272"):
                opp_val = getattr(old_value, "XExpression272", None)
                if opp_val == self:
                    setattr(old_value, "XExpression272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression272"):
                opp_val = getattr(value, "XExpression272", None)
                setattr(value, "XExpression272", self)

class model_xbase_XCatchClause:

    pass
class XCatchClause:

    pass
class XAbstractWhileExpression:

    pass
class model_xbase_XDoWhileExpression(XAbstractWhileExpression):

    pass
class model_xbase_XWhileExpression(XAbstractWhileExpression):

    pass
class XCollectionLiteral:

    pass
class model_xbase_XListLiteral(XCollectionLiteral):

    pass
class model_xbase_XSetLiteral(XCollectionLiteral):

    pass
class JvmConstructor:

    pass
class XAbstractFeatureCall:

    pass
class model_xbase_XPrefixOperation(XAbstractFeatureCall):

    pass
class model_xbase_XUnaryOperation(XAbstractFeatureCall):

    pass
class model_xbase_XAssignment(XAbstractFeatureCall):

    def __init__(self, explicitStatic: bool, model_xbase_XAssignment: "XExpression" = None, model_xbase_XAssignment238: "XExpression" = None):
        self.explicitStatic = explicitStatic
        self.model_xbase_XAssignment = model_xbase_XAssignment
        self.model_xbase_XAssignment238 = model_xbase_XAssignment238
        
        pass
    @property
    def explicitStatic(self):
        return self.__explicitStatic

    @explicitStatic.setter
    def explicitStatic(self, explicitStatic: bool):
        self.__explicitStatic = explicitStatic


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
            if hasattr(old_value, "XExpression236"):
                opp_val = getattr(old_value, "XExpression236", None)
                if opp_val == self:
                    setattr(old_value, "XExpression236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression236"):
                opp_val = getattr(value, "XExpression236", None)
                setattr(value, "XExpression236", self)

    @property
    def model_xbase_XAssignment238(self):
        return self.__model_xbase_XAssignment238

    @model_xbase_XAssignment238.setter
    def model_xbase_XAssignment238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAssignment__model_xbase_XAssignment238", None)
        self.__model_xbase_XAssignment238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression239"):
                opp_val = getattr(old_value, "XExpression239", None)
                if opp_val == self:
                    setattr(old_value, "XExpression239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression239"):
                opp_val = getattr(value, "XExpression239", None)
                setattr(value, "XExpression239", self)

class model_xbase_XFeatureCall(XAbstractFeatureCall):

    def __init__(self, explicitOperationCall: bool, typeLiteral: bool, packageFragment: bool, indexedOperation: bool, model_xbase_XFeatureCall: set["XExpression"] = None, model_xbase_XFeatureCall148: "XExpression" = None):
        self.explicitOperationCall = explicitOperationCall
        self.typeLiteral = typeLiteral
        self.packageFragment = packageFragment
        self.indexedOperation = indexedOperation
        self.model_xbase_XFeatureCall = model_xbase_XFeatureCall if model_xbase_XFeatureCall is not None else set()
        self.model_xbase_XFeatureCall148 = model_xbase_XFeatureCall148
        
        pass
    @property
    def typeLiteral(self):
        return self.__typeLiteral

    @typeLiteral.setter
    def typeLiteral(self, typeLiteral: bool):
        self.__typeLiteral = typeLiteral


    @property
    def packageFragment(self):
        return self.__packageFragment

    @packageFragment.setter
    def packageFragment(self, packageFragment: bool):
        self.__packageFragment = packageFragment


    @property
    def explicitOperationCall(self):
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall


    @property
    def indexedOperation(self):
        return self.__indexedOperation

    @indexedOperation.setter
    def indexedOperation(self, indexedOperation: bool):
        self.__indexedOperation = indexedOperation


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
                    

    @property
    def model_xbase_XFeatureCall148(self):
        return self.__model_xbase_XFeatureCall148

    @model_xbase_XFeatureCall148.setter
    def model_xbase_XFeatureCall148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFeatureCall__model_xbase_XFeatureCall148", None)
        self.__model_xbase_XFeatureCall148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression149"):
                opp_val = getattr(old_value, "XExpression149", None)
                if opp_val == self:
                    setattr(old_value, "XExpression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression149"):
                opp_val = getattr(value, "XExpression149", None)
                setattr(value, "XExpression149", self)

class model_xbase_XPostfixOperation(XAbstractFeatureCall):

    pass
class model_xbase_XMemberFeatureCall1(XAbstractFeatureCall):

    def __init__(self, explicitOperationCall: bool, explicitStatic: bool, nullSafe: bool, typeLiteral: bool, staticWithDeclaringType: bool, packageFragment: bool, indexedOperation: bool, model_xbase_XMemberFeatureCall1143: set["XExpression"] = None, model_xbase_XMemberFeatureCall1: "XExpression" = None):
        self.explicitOperationCall = explicitOperationCall
        self.explicitStatic = explicitStatic
        self.nullSafe = nullSafe
        self.typeLiteral = typeLiteral
        self.staticWithDeclaringType = staticWithDeclaringType
        self.packageFragment = packageFragment
        self.indexedOperation = indexedOperation
        self.model_xbase_XMemberFeatureCall1143 = model_xbase_XMemberFeatureCall1143 if model_xbase_XMemberFeatureCall1143 is not None else set()
        self.model_xbase_XMemberFeatureCall1 = model_xbase_XMemberFeatureCall1
        
        pass
    @property
    def explicitStatic(self):
        return self.__explicitStatic

    @explicitStatic.setter
    def explicitStatic(self, explicitStatic: bool):
        self.__explicitStatic = explicitStatic


    @property
    def explicitOperationCall(self):
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall


    @property
    def staticWithDeclaringType(self):
        return self.__staticWithDeclaringType

    @staticWithDeclaringType.setter
    def staticWithDeclaringType(self, staticWithDeclaringType: bool):
        self.__staticWithDeclaringType = staticWithDeclaringType


    @property
    def typeLiteral(self):
        return self.__typeLiteral

    @typeLiteral.setter
    def typeLiteral(self, typeLiteral: bool):
        self.__typeLiteral = typeLiteral


    @property
    def indexedOperation(self):
        return self.__indexedOperation

    @indexedOperation.setter
    def indexedOperation(self, indexedOperation: bool):
        self.__indexedOperation = indexedOperation


    @property
    def packageFragment(self):
        return self.__packageFragment

    @packageFragment.setter
    def packageFragment(self, packageFragment: bool):
        self.__packageFragment = packageFragment


    @property
    def nullSafe(self):
        return self.__nullSafe

    @nullSafe.setter
    def nullSafe(self, nullSafe: bool):
        self.__nullSafe = nullSafe


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
            if hasattr(old_value, "XExpression141"):
                opp_val = getattr(old_value, "XExpression141", None)
                if opp_val == self:
                    setattr(old_value, "XExpression141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression141"):
                opp_val = getattr(value, "XExpression141", None)
                setattr(value, "XExpression141", self)

    @property
    def model_xbase_XMemberFeatureCall1143(self):
        return self.__model_xbase_XMemberFeatureCall1143

    @model_xbase_XMemberFeatureCall1143.setter
    def model_xbase_XMemberFeatureCall1143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XMemberFeatureCall1__model_xbase_XMemberFeatureCall1143", None)
        self.__model_xbase_XMemberFeatureCall1143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression144"):
                    opp_val = getattr(item, "XExpression144", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression144"):
                    opp_val = getattr(item, "XExpression144", None)
                    
                    setattr(item, "XExpression144", self)
                    

class model_xbase_XIndexOperation(XAbstractFeatureCall):

    pass
class model_xbase_XBinaryOperation(XAbstractFeatureCall):

    pass
class model_xbase_XMemberFeatureCall(XAbstractFeatureCall):

    def __init__(self, explicitOperationCall: bool, explicitStatic: bool, nullSafe: bool, typeLiteral: bool, staticWithDeclaringType: bool, packageFragment: bool, indexedOperation: bool, model_xbase_XMemberFeatureCall: "XExpression" = None, model_xbase_XMemberFeatureCall138: set["XExpression"] = None):
        self.explicitOperationCall = explicitOperationCall
        self.explicitStatic = explicitStatic
        self.nullSafe = nullSafe
        self.typeLiteral = typeLiteral
        self.staticWithDeclaringType = staticWithDeclaringType
        self.packageFragment = packageFragment
        self.indexedOperation = indexedOperation
        self.model_xbase_XMemberFeatureCall = model_xbase_XMemberFeatureCall
        self.model_xbase_XMemberFeatureCall138 = model_xbase_XMemberFeatureCall138 if model_xbase_XMemberFeatureCall138 is not None else set()
        
        pass
    @property
    def packageFragment(self):
        return self.__packageFragment

    @packageFragment.setter
    def packageFragment(self, packageFragment: bool):
        self.__packageFragment = packageFragment


    @property
    def typeLiteral(self):
        return self.__typeLiteral

    @typeLiteral.setter
    def typeLiteral(self, typeLiteral: bool):
        self.__typeLiteral = typeLiteral


    @property
    def indexedOperation(self):
        return self.__indexedOperation

    @indexedOperation.setter
    def indexedOperation(self, indexedOperation: bool):
        self.__indexedOperation = indexedOperation


    @property
    def staticWithDeclaringType(self):
        return self.__staticWithDeclaringType

    @staticWithDeclaringType.setter
    def staticWithDeclaringType(self, staticWithDeclaringType: bool):
        self.__staticWithDeclaringType = staticWithDeclaringType


    @property
    def explicitStatic(self):
        return self.__explicitStatic

    @explicitStatic.setter
    def explicitStatic(self, explicitStatic: bool):
        self.__explicitStatic = explicitStatic


    @property
    def explicitOperationCall(self):
        return self.__explicitOperationCall

    @explicitOperationCall.setter
    def explicitOperationCall(self, explicitOperationCall: bool):
        self.__explicitOperationCall = explicitOperationCall


    @property
    def nullSafe(self):
        return self.__nullSafe

    @nullSafe.setter
    def nullSafe(self, nullSafe: bool):
        self.__nullSafe = nullSafe


    @property
    def model_xbase_XMemberFeatureCall138(self):
        return self.__model_xbase_XMemberFeatureCall138

    @model_xbase_XMemberFeatureCall138.setter
    def model_xbase_XMemberFeatureCall138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XMemberFeatureCall__model_xbase_XMemberFeatureCall138", None)
        self.__model_xbase_XMemberFeatureCall138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XExpression139"):
                    opp_val = getattr(item, "XExpression139", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression139"):
                    opp_val = getattr(item, "XExpression139", None)
                    
                    setattr(item, "XExpression139", self)
                    

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
            if hasattr(old_value, "XExpression136"):
                opp_val = getattr(old_value, "XExpression136", None)
                if opp_val == self:
                    setattr(old_value, "XExpression136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression136"):
                opp_val = getattr(value, "XExpression136", None)
                setattr(value, "XExpression136", self)

class model_xbase_XExpression(ABC):

    pass
class model_xbase_XCasePart:

    pass
class XCasePart:

    pass
class types_JvmIdentifiableElement:

    pass
class xbase_XExpression:

    pass
class model_xbase_XVariableDeclaration(xbase_XExpression, types_JvmIdentifiableElement):

    def __init__(self, name: str, writeable: bool, exported: bool, model_xbase_XVariableDeclaration: "JvmTypeReference" = None, model_xbase_XVariableDeclaration121: "XExpression" = None):
        self.name = name
        self.writeable = writeable
        self.exported = exported
        self.model_xbase_XVariableDeclaration = model_xbase_XVariableDeclaration
        self.model_xbase_XVariableDeclaration121 = model_xbase_XVariableDeclaration121
        
        pass
    @property
    def writeable(self):
        return self.__writeable

    @writeable.setter
    def writeable(self, writeable: bool):
        self.__writeable = writeable


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def exported(self):
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported


    @property
    def model_xbase_XVariableDeclaration121(self):
        return self.__model_xbase_XVariableDeclaration121

    @model_xbase_XVariableDeclaration121.setter
    def model_xbase_XVariableDeclaration121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XVariableDeclaration__model_xbase_XVariableDeclaration121", None)
        self.__model_xbase_XVariableDeclaration121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression122"):
                opp_val = getattr(old_value, "XExpression122", None)
                if opp_val == self:
                    setattr(old_value, "XExpression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression122"):
                opp_val = getattr(value, "XExpression122", None)
                setattr(value, "XExpression122", self)

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
            if hasattr(old_value, "JvmTypeReference119"):
                opp_val = getattr(old_value, "JvmTypeReference119", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference119"):
                opp_val = getattr(value, "JvmTypeReference119", None)
                setattr(value, "JvmTypeReference119", self)

class model_xbase_XClosure(xbase_XExpression, types_JvmIdentifiableElement):

    def __init__(self, explicitSyntax: bool, name: str, operator: bool, exported: bool, model_xbase_XClosure: set["JvmFormalParameter"] = None, model_xbase_XClosure167: "XExpression" = None, model_xbase_XClosure170: "JvmFormalParameter" = None, model_xbase_XClosure173: "JvmTypeReference" = None, model_xbase_XClosure176: set["JvmTypeParameter"] = None):
        self.explicitSyntax = explicitSyntax
        self.name = name
        self.operator = operator
        self.exported = exported
        self.model_xbase_XClosure = model_xbase_XClosure if model_xbase_XClosure is not None else set()
        self.model_xbase_XClosure167 = model_xbase_XClosure167
        self.model_xbase_XClosure170 = model_xbase_XClosure170
        self.model_xbase_XClosure173 = model_xbase_XClosure173
        self.model_xbase_XClosure176 = model_xbase_XClosure176 if model_xbase_XClosure176 is not None else set()
        
        pass
    @property
    def exported(self):
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def explicitSyntax(self):
        return self.__explicitSyntax

    @explicitSyntax.setter
    def explicitSyntax(self, explicitSyntax: bool):
        self.__explicitSyntax = explicitSyntax


    @property
    def model_xbase_XClosure167(self):
        return self.__model_xbase_XClosure167

    @model_xbase_XClosure167.setter
    def model_xbase_XClosure167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure167", None)
        self.__model_xbase_XClosure167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression168"):
                opp_val = getattr(old_value, "XExpression168", None)
                if opp_val == self:
                    setattr(old_value, "XExpression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression168"):
                opp_val = getattr(value, "XExpression168", None)
                setattr(value, "XExpression168", self)

    @property
    def model_xbase_XClosure170(self):
        return self.__model_xbase_XClosure170

    @model_xbase_XClosure170.setter
    def model_xbase_XClosure170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure170", None)
        self.__model_xbase_XClosure170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmFormalParameter171"):
                opp_val = getattr(old_value, "JvmFormalParameter171", None)
                if opp_val == self:
                    setattr(old_value, "JvmFormalParameter171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmFormalParameter171"):
                opp_val = getattr(value, "JvmFormalParameter171", None)
                setattr(value, "JvmFormalParameter171", self)

    @property
    def model_xbase_XClosure173(self):
        return self.__model_xbase_XClosure173

    @model_xbase_XClosure173.setter
    def model_xbase_XClosure173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure173", None)
        self.__model_xbase_XClosure173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference174"):
                opp_val = getattr(old_value, "JvmTypeReference174", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference174"):
                opp_val = getattr(value, "JvmTypeReference174", None)
                setattr(value, "JvmTypeReference174", self)

    @property
    def model_xbase_XClosure176(self):
        return self.__model_xbase_XClosure176

    @model_xbase_XClosure176.setter
    def model_xbase_XClosure176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XClosure__model_xbase_XClosure176", None)
        self.__model_xbase_XClosure176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeParameter177"):
                    opp_val = getattr(item, "JvmTypeParameter177", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeParameter177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeParameter177"):
                    opp_val = getattr(item, "JvmTypeParameter177", None)
                    
                    setattr(item, "JvmTypeParameter177", self)
                    

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
                if hasattr(item, "JvmFormalParameter165"):
                    opp_val = getattr(item, "JvmFormalParameter165", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmFormalParameter165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmFormalParameter165"):
                    opp_val = getattr(item, "JvmFormalParameter165", None)
                    
                    setattr(item, "JvmFormalParameter165", self)
                    

    def getFormalParameters(self) :
        # TODO: Implement getFormalParameters method
        pass

class model_xbase_XSwitchExpression(xbase_XExpression, types_JvmIdentifiableElement):

    def __init__(self, localVarName: str, model_xbase_XSwitchExpression: "XExpression" = None, model_xbase_XSwitchExpression104: set["XCasePart"] = None, model_xbase_XSwitchExpression106: "XExpression" = None):
        self.localVarName = localVarName
        self.model_xbase_XSwitchExpression = model_xbase_XSwitchExpression
        self.model_xbase_XSwitchExpression104 = model_xbase_XSwitchExpression104 if model_xbase_XSwitchExpression104 is not None else set()
        self.model_xbase_XSwitchExpression106 = model_xbase_XSwitchExpression106
        
        pass
    @property
    def localVarName(self):
        return self.__localVarName

    @localVarName.setter
    def localVarName(self, localVarName: str):
        self.__localVarName = localVarName


    @property
    def model_xbase_XSwitchExpression104(self):
        return self.__model_xbase_XSwitchExpression104

    @model_xbase_XSwitchExpression104.setter
    def model_xbase_XSwitchExpression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XSwitchExpression__model_xbase_XSwitchExpression104", None)
        self.__model_xbase_XSwitchExpression104 = value if value is not None else set()
        
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
    def model_xbase_XSwitchExpression106(self):
        return self.__model_xbase_XSwitchExpression106

    @model_xbase_XSwitchExpression106.setter
    def model_xbase_XSwitchExpression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XSwitchExpression__model_xbase_XSwitchExpression106", None)
        self.__model_xbase_XSwitchExpression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression107"):
                opp_val = getattr(old_value, "XExpression107", None)
                if opp_val == self:
                    setattr(old_value, "XExpression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression107"):
                opp_val = getattr(value, "XExpression107", None)
                setattr(value, "XExpression107", self)

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
            if hasattr(old_value, "XExpression102"):
                opp_val = getattr(old_value, "XExpression102", None)
                if opp_val == self:
                    setattr(old_value, "XExpression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression102"):
                opp_val = getattr(value, "XExpression102", None)
                setattr(value, "XExpression102", self)

class JvmTypeParameterDeclarator:

    pass
class types_JvmConstraintOwner:

    pass
class JvmMember:

    pass
class JvmTypeReference:

    pass
class model_types_JvmSpecializedTypeReference(JvmTypeReference):

    pass
class model_types_JvmCompoundTypeReference(JvmTypeReference):

    pass
class model_types_JvmUnknownTypeReference(JvmTypeReference):

    def __init__(self, qualifiedName: str, JvmTypeReference128: "model_xbase_XAbstractFeatureCall" = None, JvmTypeReference358: "model_ss_XtendInterface" = None, JvmTypeReference85: "model_types_JvmDelegateTypeReference" = None, JvmTypeReference374: "model_ss_XtendEvent" = None, JvmTypeReference156: "model_xbase_XConstructorCall" = None, JvmTypeReference311: "model_ss_XtendFunction" = None, JvmTypeReference: "model_types_JvmDeclaredType" = None, JvmTypeReference62: "model_types_JvmFormalParameter" = None, JvmTypeReference52: "model_types_JvmOperation" = None, JvmTypeReference119: "model_xbase_XVariableDeclaration" = None, JvmTypeReference26: "model_types_JvmParameterizedTypeReference" = None, JvmTypeReference18: "model_types_JvmTypeConstraint" = None, JvmTypeReference363: "model_ss_XtendDelegate" = None, JvmTypeReference372: "model_ss_XtendDelegate" = None, JvmTypeReference174: "model_xbase_XClosure" = None, JvmTypeReference92: "model_types_JvmCompoundTypeReference" = None, JvmTypeReference285: "model_ss_XtendClass" = None, JvmTypeReference87: "model_types_JvmSpecializedTypeReference" = None, JvmTypeReference354: "model_ss_XtendConstructor" = None, JvmTypeReference79: "model_types_JvmTypeAnnotationValue" = None, JvmTypeReference36: "model_types_JvmField" = None, JvmTypeReference48: "model_types_JvmExecutable" = None, JvmTypeReference301: "model_ss_XtendFunction" = None, JvmTypeReference313: "model_ss_XtendField" = None, JvmTypeReference179: "model_xbase_XCastedExpression" = None, JvmTypeReference30: "model_types_JvmGenericArrayTypeReference" = None, JvmTypeReference394: "model_xtype_XFunctionTypeRef" = None, JvmTypeReference318: "model_ss_XtendParameter" = None, JvmTypeReference391: "model_xtype_XFunctionTypeRef" = None, JvmTypeReference115: "model_xbase_XCasePart" = None, JvmTypeReference217: "model_xbase_XInstanceOfExpression" = None, JvmTypeReference263: "model_xbase_XFunctionDeclaration" = None, JvmTypeReference288: "model_ss_XtendClass" = None):
        self.qualifiedName = qualifiedName
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


class types_JvmComponentType:

    pass
class model_types_JvmTypeParameter(types_JvmConstraintOwner, types_JvmComponentType):

    def __init__(self, name: str, typeParameters: "JvmTypeParameterDeclarator" = None):
        self.name = name
        self.typeParameters = typeParameters
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def typeParameters(self):
        return self.__typeParameters

    @typeParameters.setter
    def typeParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmTypeParameter__typeParameters", None)
        self.__typeParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeParameterDeclarator"):
                opp_val = getattr(old_value, "JvmTypeParameterDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeParameterDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeParameterDeclarator"):
                opp_val = getattr(value, "JvmTypeParameterDeclarator", None)
                setattr(value, "JvmTypeParameterDeclarator", self)

class types_JvmMember:

    pass
class model_types_JvmDeclaredType(types_JvmMember, types_JvmComponentType):

    def __init__(self, abstract: bool, static: bool, final: bool, packageName: str, exported: bool, model_types_JvmDeclaredType: set["JvmTypeReference"] = None, declaringType: set["JvmMember"] = None):
        self.abstract = abstract
        self.static = static
        self.final = final
        self.packageName = packageName
        self.exported = exported
        self.model_types_JvmDeclaredType = model_types_JvmDeclaredType if model_types_JvmDeclaredType is not None else set()
        self.declaringType = declaringType if declaringType is not None else set()
        
        pass
    @property
    def packageName(self):
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def exported(self):
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


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
    def declaringType(self):
        return self.__declaringType

    @declaringType.setter
    def declaringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmDeclaredType__declaringType", None)
        self.__declaringType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmMember"):
                    opp_val = getattr(item, "JvmMember", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmMember"):
                    opp_val = getattr(item, "JvmMember", None)
                    
                    setattr(item, "JvmMember", self)
                    

    def getDeclaredFields(self):
        # TODO: Implement getDeclaredFields method
        pass

    def getDeclaredOperations(self):
        # TODO: Implement getDeclaredOperations method
        pass

    def getAllFeatures(self):
        # TODO: Implement getAllFeatures method
        pass

    def findAllFeaturesByName(self, model_simpleName):
        # TODO: Implement findAllFeaturesByName method
        pass

class JvmComponentType:

    pass
class model_types_JvmArrayType(JvmComponentType):

    def __init__(self, arrayType: "JvmComponentType" = None, JvmComponentType: "model_types_JvmArrayType" = None):
        self.arrayType = arrayType
        
        pass
    @property
    def arrayType(self):
        return self.__arrayType

    @arrayType.setter
    def arrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmArrayType__arrayType", None)
        self.__arrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmComponentType"):
                opp_val = getattr(old_value, "JvmComponentType", None)
                if opp_val == self:
                    setattr(old_value, "JvmComponentType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmComponentType"):
                opp_val = getattr(value, "JvmComponentType", None)
                setattr(value, "JvmComponentType", self)

    def getDimensions(self) :
        # TODO: Implement getDimensions method
        pass

class model_types_JvmPrimitiveType(JvmComponentType):

    def __init__(self, simpleName: str, JvmComponentType: "model_types_JvmArrayType" = None):
        self.simpleName = simpleName
        
        pass
    @property
    def simpleName(self):
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
class XExportSection:

    pass
class types_model_EObject:

    pass
class XImportSection1:

    pass
class JvmIdentifiableElement:

    pass
class model_types_JvmType(JvmIdentifiableElement):

    pass
class model_types_JvmModule(JvmIdentifiableElement):

    def __init__(self, simpleName: str, model_types_JvmModule: "XImportSection1" = None, model_types_JvmModule2: set["types_model_EObject"] = None, model_types_JvmModule4: "XExportSection" = None, JvmIdentifiableElement: "model_xbase_XAbstractFeatureCall" = None, JvmIdentifiableElement404: "model_xtype_XImportItem" = None, JvmIdentifiableElement408: "model_xtype_XExportItem" = None):
        self.simpleName = simpleName
        self.model_types_JvmModule = model_types_JvmModule
        self.model_types_JvmModule2 = model_types_JvmModule2 if model_types_JvmModule2 is not None else set()
        self.model_types_JvmModule4 = model_types_JvmModule4
        
        pass
    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


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
                    

class model_types_JvmIdentifiableElement(ABC):

    def __init__(self):
        
        pass
    def getIdentifier(self) :
        # TODO: Implement getIdentifier method
        pass

    def getSimpleName(self) :
        # TODO: Implement getSimpleName method
        pass

    def isExported(self) :
        # TODO: Implement isExported method
        pass

    def getQualifiedName(self, model_innerClassDelimiter) :
        # TODO: Implement getQualifiedName method
        pass

class model_types_JvmDelegateTypeReference(JvmTypeReference):

    pass
class JvmAnnotationValue:

    pass
class model_types_JvmAnnotationAnnotationValue(JvmAnnotationValue):

    pass
class model_types_JvmFloatAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values


class model_types_JvmStringAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class model_types_JvmCharAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class model_types_JvmDoubleAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: float, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: float):
        self.__values = values


class model_types_JvmShortAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class model_types_JvmEnumAnnotationValue(JvmAnnotationValue):

    pass
class model_types_JvmCustomAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class model_types_JvmLongAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class model_types_JvmTypeAnnotationValue(JvmAnnotationValue):

    pass
class model_types_JvmByteAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: str, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class model_types_JvmBooleanAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: bool, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: bool):
        self.__values = values


class model_types_JvmIntAnnotationValue(JvmAnnotationValue):

    def __init__(self, values: int, JvmAnnotationValue: "model_types_JvmOperation" = None, JvmAnnotationValue70: "model_types_JvmAnnotationReference" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: int):
        self.__values = values


class JvmOperation:

    pass
class model_types_JvmAnnotationValue:

    def __init__(self, model_types_JvmAnnotationValue: "JvmOperation" = None, model_types_JvmAnnotationValue76: "XExpression" = None):
        self.model_types_JvmAnnotationValue = model_types_JvmAnnotationValue
        self.model_types_JvmAnnotationValue76 = model_types_JvmAnnotationValue76
        
        pass
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
    def model_types_JvmAnnotationValue76(self):
        return self.__model_types_JvmAnnotationValue76

    @model_types_JvmAnnotationValue76.setter
    def model_types_JvmAnnotationValue76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmAnnotationValue__model_types_JvmAnnotationValue76", None)
        self.__model_types_JvmAnnotationValue76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression77"):
                opp_val = getattr(old_value, "XExpression77", None)
                if opp_val == self:
                    setattr(old_value, "XExpression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression77"):
                opp_val = getattr(value, "XExpression77", None)
                setattr(value, "XExpression77", self)

    def getValueName(self) :
        # TODO: Implement getValueName method
        pass

class JvmAnnotationType:

    pass
class model_types_JvmAnnotationReference:

    pass
class JvmAnnotationReference:

    pass
class model_types_JvmAnnotationTarget(JvmIdentifiableElement):

    pass
class JvmAnnotationTarget:

    pass
class model_types_JvmFormalParameter(JvmAnnotationTarget):

    def __init__(self, name: str, varArg: bool, model_types_JvmFormalParameter: "JvmTypeReference" = None, model_types_JvmFormalParameter64: "XExpression" = None, JvmAnnotationTarget: "model_types_JvmMember" = None):
        self.name = name
        self.varArg = varArg
        self.model_types_JvmFormalParameter = model_types_JvmFormalParameter
        self.model_types_JvmFormalParameter64 = model_types_JvmFormalParameter64
        
        pass
    @property
    def varArg(self):
        return self.__varArg

    @varArg.setter
    def varArg(self, varArg: bool):
        self.__varArg = varArg


    @property
    def name(self):
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
            if hasattr(old_value, "JvmTypeReference62"):
                opp_val = getattr(old_value, "JvmTypeReference62", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference62"):
                opp_val = getattr(value, "JvmTypeReference62", None)
                setattr(value, "JvmTypeReference62", self)

    @property
    def model_types_JvmFormalParameter64(self):
        return self.__model_types_JvmFormalParameter64

    @model_types_JvmFormalParameter64.setter
    def model_types_JvmFormalParameter64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmFormalParameter__model_types_JvmFormalParameter64", None)
        self.__model_types_JvmFormalParameter64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression65"):
                opp_val = getattr(old_value, "XExpression65", None)
                if opp_val == self:
                    setattr(old_value, "XExpression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression65"):
                opp_val = getattr(value, "XExpression65", None)
                setattr(value, "XExpression65", self)

class model_types_JvmMember(JvmAnnotationTarget):

    def __init__(self, modifiers: str, visibility: str, simpleName: str, identifier: str, model_types_JvmMember: "JvmAnnotationTarget" = None, members: "JvmDeclaredType" = None, JvmAnnotationTarget: "model_types_JvmMember" = None):
        self.modifiers = modifiers
        self.visibility = visibility
        self.simpleName = simpleName
        self.identifier = identifier
        self.model_types_JvmMember = model_types_JvmMember
        self.members = members
        
        pass
    @property
    def modifiers(self):
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers


    @property
    def simpleName(self):
        return self.__simpleName

    @simpleName.setter
    def simpleName(self, simpleName: str):
        self.__simpleName = simpleName


    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def identifier(self):
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
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmMember__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmDeclaredType"):
                opp_val = getattr(old_value, "JvmDeclaredType", None)
                if opp_val == self:
                    setattr(old_value, "JvmDeclaredType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmDeclaredType"):
                opp_val = getattr(value, "JvmDeclaredType", None)
                setattr(value, "JvmDeclaredType", self)

    def internalSetIdentifier(self, model_identifier):
        # TODO: Implement internalSetIdentifier method
        pass

class JvmCompoundTypeReference:

    pass
class model_types_JvmSynonymTypeReference(JvmCompoundTypeReference):

    pass
class model_types_JvmMultiTypeReference(JvmCompoundTypeReference):

    pass
class JvmExecutable:

    pass
class model_types_JvmOperation(JvmExecutable):

    def __init__(self, static: bool, final: bool, abstract: bool, synchronized: bool, default: bool, native: bool, strictFloatingPoint: bool, model_types_JvmOperation56: "XExpression" = None, model_types_JvmOperation59: "XExpression" = None, model_types_JvmOperation: "JvmTypeReference" = None, model_types_JvmOperation54: "JvmAnnotationValue" = None):
        self.static = static
        self.final = final
        self.abstract = abstract
        self.synchronized = synchronized
        self.default = default
        self.native = native
        self.strictFloatingPoint = strictFloatingPoint
        self.model_types_JvmOperation56 = model_types_JvmOperation56
        self.model_types_JvmOperation59 = model_types_JvmOperation59
        self.model_types_JvmOperation = model_types_JvmOperation
        self.model_types_JvmOperation54 = model_types_JvmOperation54
        
        pass
    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract


    @property
    def strictFloatingPoint(self):
        return self.__strictFloatingPoint

    @strictFloatingPoint.setter
    def strictFloatingPoint(self, strictFloatingPoint: bool):
        self.__strictFloatingPoint = strictFloatingPoint


    @property
    def native(self):
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native


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
            if hasattr(old_value, "JvmTypeReference52"):
                opp_val = getattr(old_value, "JvmTypeReference52", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference52"):
                opp_val = getattr(value, "JvmTypeReference52", None)
                setattr(value, "JvmTypeReference52", self)

    @property
    def model_types_JvmOperation56(self):
        return self.__model_types_JvmOperation56

    @model_types_JvmOperation56.setter
    def model_types_JvmOperation56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation56", None)
        self.__model_types_JvmOperation56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression57"):
                opp_val = getattr(old_value, "XExpression57", None)
                if opp_val == self:
                    setattr(old_value, "XExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression57"):
                opp_val = getattr(value, "XExpression57", None)
                setattr(value, "XExpression57", self)

    @property
    def model_types_JvmOperation54(self):
        return self.__model_types_JvmOperation54

    @model_types_JvmOperation54.setter
    def model_types_JvmOperation54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation54", None)
        self.__model_types_JvmOperation54 = value
        
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
    def model_types_JvmOperation59(self):
        return self.__model_types_JvmOperation59

    @model_types_JvmOperation59.setter
    def model_types_JvmOperation59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmOperation__model_types_JvmOperation59", None)
        self.__model_types_JvmOperation59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression60"):
                opp_val = getattr(old_value, "XExpression60", None)
                if opp_val == self:
                    setattr(old_value, "XExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression60"):
                opp_val = getattr(value, "XExpression60", None)
                setattr(value, "XExpression60", self)

class model_types_JvmConstructor(JvmExecutable):

    pass
class JvmFormalParameter:

    pass
class model_ss_XtendFormalParameter(JvmFormalParameter):

    def __init__(self, extension: bool, JvmFormalParameter266: "model_xbase_XFunctionDeclaration" = None, JvmFormalParameter: "model_types_JvmExecutable" = None, JvmFormalParameter234: "model_xbase_XCatchClause" = None, JvmFormalParameter208: "model_xbase_XForEachExpression" = None, JvmFormalParameter171: "model_xbase_XClosure" = None, JvmFormalParameter165: "model_xbase_XClosure" = None):
        self.extension = extension
        
        pass
    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, extension: bool):
        self.__extension = extension


class types_JvmFeature:

    pass
class XExpression:

    pass
class model_xbase_XNumberLiteral(XExpression):

    def __init__(self, value: str, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class model_xbase_XForEachExpression(XExpression):

    pass
class model_xbase_XKeyValuePair(XExpression):

    def __init__(self, key1: str, model_xbase_XKeyValuePair: "XExpression" = None, model_xbase_XKeyValuePair162: "XExpression" = None, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.key1 = key1
        self.model_xbase_XKeyValuePair = model_xbase_XKeyValuePair
        self.model_xbase_XKeyValuePair162 = model_xbase_XKeyValuePair162
        
        pass
    @property
    def key1(self):
        return self.__key1

    @key1.setter
    def key1(self, key1: str):
        self.__key1 = key1


    @property
    def model_xbase_XKeyValuePair162(self):
        return self.__model_xbase_XKeyValuePair162

    @model_xbase_XKeyValuePair162.setter
    def model_xbase_XKeyValuePair162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XKeyValuePair__model_xbase_XKeyValuePair162", None)
        self.__model_xbase_XKeyValuePair162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression163"):
                opp_val = getattr(old_value, "XExpression163", None)
                if opp_val == self:
                    setattr(old_value, "XExpression163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression163"):
                opp_val = getattr(value, "XExpression163", None)
                setattr(value, "XExpression163", self)

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
            if hasattr(old_value, "XExpression160"):
                opp_val = getattr(old_value, "XExpression160", None)
                if opp_val == self:
                    setattr(old_value, "XExpression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression160"):
                opp_val = getattr(value, "XExpression160", None)
                setattr(value, "XExpression160", self)

class model_xbase_XThrowExpression(XExpression):

    pass
class model_xbase_XTernaryOperation(XExpression):

    pass
class model_xbase_XAbstractFeatureCall(XExpression):

    def __init__(self, invalidFeatureIssueCode: str, validFeature: bool, model_xbase_XAbstractFeatureCall: "JvmIdentifiableElement" = None, model_xbase_XAbstractFeatureCall127: set["JvmTypeReference"] = None, model_xbase_XAbstractFeatureCall130: "XExpression" = None, model_xbase_XAbstractFeatureCall133: "XExpression" = None, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.invalidFeatureIssueCode = invalidFeatureIssueCode
        self.validFeature = validFeature
        self.model_xbase_XAbstractFeatureCall = model_xbase_XAbstractFeatureCall
        self.model_xbase_XAbstractFeatureCall127 = model_xbase_XAbstractFeatureCall127 if model_xbase_XAbstractFeatureCall127 is not None else set()
        self.model_xbase_XAbstractFeatureCall130 = model_xbase_XAbstractFeatureCall130
        self.model_xbase_XAbstractFeatureCall133 = model_xbase_XAbstractFeatureCall133
        
        pass
    @property
    def invalidFeatureIssueCode(self):
        return self.__invalidFeatureIssueCode

    @invalidFeatureIssueCode.setter
    def invalidFeatureIssueCode(self, invalidFeatureIssueCode: str):
        self.__invalidFeatureIssueCode = invalidFeatureIssueCode


    @property
    def validFeature(self):
        return self.__validFeature

    @validFeature.setter
    def validFeature(self, validFeature: bool):
        self.__validFeature = validFeature


    @property
    def model_xbase_XAbstractFeatureCall130(self):
        return self.__model_xbase_XAbstractFeatureCall130

    @model_xbase_XAbstractFeatureCall130.setter
    def model_xbase_XAbstractFeatureCall130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall130", None)
        self.__model_xbase_XAbstractFeatureCall130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression131"):
                opp_val = getattr(old_value, "XExpression131", None)
                if opp_val == self:
                    setattr(old_value, "XExpression131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression131"):
                opp_val = getattr(value, "XExpression131", None)
                setattr(value, "XExpression131", self)

    @property
    def model_xbase_XAbstractFeatureCall133(self):
        return self.__model_xbase_XAbstractFeatureCall133

    @model_xbase_XAbstractFeatureCall133.setter
    def model_xbase_XAbstractFeatureCall133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall133", None)
        self.__model_xbase_XAbstractFeatureCall133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression134"):
                opp_val = getattr(old_value, "XExpression134", None)
                if opp_val == self:
                    setattr(old_value, "XExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression134"):
                opp_val = getattr(value, "XExpression134", None)
                setattr(value, "XExpression134", self)

    @property
    def model_xbase_XAbstractFeatureCall127(self):
        return self.__model_xbase_XAbstractFeatureCall127

    @model_xbase_XAbstractFeatureCall127.setter
    def model_xbase_XAbstractFeatureCall127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XAbstractFeatureCall__model_xbase_XAbstractFeatureCall127", None)
        self.__model_xbase_XAbstractFeatureCall127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference128"):
                    opp_val = getattr(item, "JvmTypeReference128", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference128"):
                    opp_val = getattr(item, "JvmTypeReference128", None)
                    
                    setattr(item, "JvmTypeReference128", self)
                    

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

    def isExtension(self) :
        # TODO: Implement isExtension method
        pass

    def getActualArguments(self) :
        # TODO: Implement getActualArguments method
        pass

    def isTypeLiteral(self) :
        # TODO: Implement isTypeLiteral method
        pass

    def isPackageFragment(self) :
        # TODO: Implement isPackageFragment method
        pass

    def isExplicitOperationCallOrBuilderSyntax(self) :
        # TODO: Implement isExplicitOperationCallOrBuilderSyntax method
        pass

    def getExplicitArguments(self) :
        # TODO: Implement getExplicitArguments method
        pass

    def getActualReceiver(self) :
        # TODO: Implement getActualReceiver method
        pass

    def isStatic(self) :
        # TODO: Implement isStatic method
        pass

    def getConcreteSyntaxFeatureName(self) :
        # TODO: Implement getConcreteSyntaxFeatureName method
        pass

class model_xbase_XIfExpression(XExpression):

    pass
class model_xbase_XBooleanLiteral(XExpression):

    def __init__(self, isTrue: bool, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.isTrue = isTrue
        
        pass
    @property
    def isTrue(self):
        return self.__isTrue

    @isTrue.setter
    def isTrue(self, isTrue: bool):
        self.__isTrue = isTrue


class model_ss_RichStringIf(XExpression):

    pass
class model_xbase_XReturnExpression(XExpression):

    pass
class model_xbase_XCastedExpression(XExpression):

    pass
class model_xbase_XArrayLiteral(XExpression):

    pass
class model_xbase_XStringLiteral(XExpression):

    def __init__(self, value: str, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class model_xbase_XVariableDeclarationList(XExpression):

    def __init__(self, writeable: bool, exported: bool, model_xbase_XVariableDeclarationList: set["XExpression"] = None, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.writeable = writeable
        self.exported = exported
        self.model_xbase_XVariableDeclarationList = model_xbase_XVariableDeclarationList if model_xbase_XVariableDeclarationList is not None else set()
        
        pass
    @property
    def exported(self):
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported


    @property
    def writeable(self):
        return self.__writeable

    @writeable.setter
    def writeable(self, writeable: bool):
        self.__writeable = writeable


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
                if hasattr(item, "XExpression124"):
                    opp_val = getattr(item, "XExpression124", None)
                    
                    if opp_val == self:
                        setattr(item, "XExpression124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XExpression124"):
                    opp_val = getattr(item, "XExpression124", None)
                    
                    setattr(item, "XExpression124", self)
                    

class model_xbase_XForLoopExpression(XExpression):

    pass
class model_xannotation_XAnnotation(XExpression):

    pass
class model_xbase_XObjectLiteral(XExpression):

    pass
class model_xbase_XAbstractWhileExpression(XExpression):

    pass
class model_xbase_XBlockExpression(XExpression):

    pass
class model_xbase_XTypeLiteral(XExpression):

    def __init__(self, arrayDimensions: str, model_xbase_XTypeLiteral: "JvmType" = None, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.arrayDimensions = arrayDimensions
        self.model_xbase_XTypeLiteral = model_xbase_XTypeLiteral
        
        pass
    @property
    def arrayDimensions(self):
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
            if hasattr(old_value, "JvmType215"):
                opp_val = getattr(old_value, "JvmType215", None)
                if opp_val == self:
                    setattr(old_value, "JvmType215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmType215"):
                opp_val = getattr(value, "JvmType215", None)
                setattr(value, "JvmType215", self)

class model_xbase_XBreakExpression(XExpression):

    pass
class model_xbase_XCollectionLiteral(XExpression):

    pass
class model_xbase_XConstructorCall(XExpression):

    def __init__(self, invalidFeatureIssueCode: str, validFeature: bool, model_xbase_XConstructorCall: "JvmConstructor" = None, model_xbase_XConstructorCall152: set["XExpression"] = None, model_xbase_XConstructorCall155: set["JvmTypeReference"] = None, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.invalidFeatureIssueCode = invalidFeatureIssueCode
        self.validFeature = validFeature
        self.model_xbase_XConstructorCall = model_xbase_XConstructorCall
        self.model_xbase_XConstructorCall152 = model_xbase_XConstructorCall152 if model_xbase_XConstructorCall152 is not None else set()
        self.model_xbase_XConstructorCall155 = model_xbase_XConstructorCall155 if model_xbase_XConstructorCall155 is not None else set()
        
        pass
    @property
    def validFeature(self):
        return self.__validFeature

    @validFeature.setter
    def validFeature(self, validFeature: bool):
        self.__validFeature = validFeature


    @property
    def invalidFeatureIssueCode(self):
        return self.__invalidFeatureIssueCode

    @invalidFeatureIssueCode.setter
    def invalidFeatureIssueCode(self, invalidFeatureIssueCode: str):
        self.__invalidFeatureIssueCode = invalidFeatureIssueCode


    @property
    def model_xbase_XConstructorCall155(self):
        return self.__model_xbase_XConstructorCall155

    @model_xbase_XConstructorCall155.setter
    def model_xbase_XConstructorCall155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XConstructorCall__model_xbase_XConstructorCall155", None)
        self.__model_xbase_XConstructorCall155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference156"):
                    opp_val = getattr(item, "JvmTypeReference156", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference156"):
                    opp_val = getattr(item, "JvmTypeReference156", None)
                    
                    setattr(item, "JvmTypeReference156", self)
                    

    @property
    def model_xbase_XConstructorCall152(self):
        return self.__model_xbase_XConstructorCall152

    @model_xbase_XConstructorCall152.setter
    def model_xbase_XConstructorCall152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XConstructorCall__model_xbase_XConstructorCall152", None)
        self.__model_xbase_XConstructorCall152 = value if value is not None else set()
        
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

class model_xbase_XNullLiteral(XExpression):

    pass
class model_xbase_XInstanceOfExpression(XExpression):

    pass
class model_xbase_XContinueExpression(XExpression):

    pass
class model_xbase_XFunctionDeclaration(XExpression):

    def __init__(self, name: str, model_xbase_XFunctionDeclaration: "XExpression" = None, model_xbase_XFunctionDeclaration262: "JvmTypeReference" = None, model_xbase_XFunctionDeclaration265: set["JvmFormalParameter"] = None, XExpression146: "model_xbase_XFeatureCall" = None, XExpression149: "model_xbase_XFeatureCall" = None, XExpression102: "model_xbase_XSwitchExpression" = None, XExpression60: "model_types_JvmOperation" = None, XExpression94: "model_xbase_XIfExpression" = None, XExpression100: "model_xbase_XIfExpression" = None, XExpression163: "model_xbase_XKeyValuePair" = None, XExpression231: "model_xbase_XCatchClause" = None, XExpression112: "model_xbase_XCasePart" = None, XExpression345: "model_ss_XtendConstructor" = None, XExpression117: "model_xbase_XBlockExpression" = None, XExpression247: "model_xbase_XTernaryOperation" = None, XExpression191: "model_xbase_XForLoopExpression" = None, XExpression122: "model_xbase_XVariableDeclaration" = None, XExpression272: "model_xbase_XObjectLiteralPart" = None, XExpression189: "model_xbase_XUnaryOperation" = None, XExpression250: "model_xbase_XTernaryOperation" = None, XExpression160: "model_xbase_XKeyValuePair" = None, XExpression253: "model_xbase_XTernaryOperation" = None, XExpression109: "model_xbase_XCasePart" = None, XExpression136: "model_xbase_XMemberFeatureCall" = None, XExpression336: "model_ss_RichStringIf" = None, XExpression274: "model_xbase_XArrayLiteral" = None, XExpression41: "model_types_JvmField" = None, XExpression184: "model_xbase_XBinaryOperation" = None, XExpression220: "model_xbase_XInstanceOfExpression" = None, XExpression65: "model_types_JvmFormalParameter" = None, XExpression77: "model_types_JvmAnnotationValue" = None, XExpression131: "model_xbase_XAbstractFeatureCall" = None, XExpression239: "model_xbase_XAssignment" = None, XExpression328: "model_ss_RichStringIf" = None, XExpression168: "model_xbase_XClosure" = None, XExpression236: "model_xbase_XAssignment" = None, XExpression97: "model_xbase_XIfExpression" = None, XExpression50: "model_types_JvmConstructor" = None, XExpression44: "model_types_JvmField" = None, XExpression227: "model_xbase_XTryCatchFinallyExpression" = None, XExpression316: "model_ss_XtendField" = None, XExpression200: "model_xbase_XForLoopExpression" = None, XExpression73: "model_types_JvmAnnotationReference" = None, XExpression: "model_types_JvmField" = None, XExpression205: "model_xbase_XForEachExpression" = None, XExpression341: "model_ss_RichStringElseIf" = None, XExpression153: "model_xbase_XConstructorCall" = None, XExpression323: "model_ss_RichStringForLoop" = None, XExpression224: "model_xbase_XTryCatchFinallyExpression" = None, XExpression343: "model_ss_CreateExtensionInfo" = None, XExpression245: "model_xbase_XPostfixOperation" = None, XExpression377: "model_ss_XtendEvent" = None, XExpression124: "model_xbase_XVariableDeclarationList" = None, XExpression320: "model_ss_RichStringForLoop" = None, XExpression107: "model_xbase_XSwitchExpression" = None, XExpression420: "model_richstring_PrintedExpression" = None, XExpression144: "model_xbase_XMemberFeatureCall1" = None, XExpression197: "model_xbase_XForLoopExpression" = None, XExpression258: "model_xbase_XIndexOperation" = None, XExpression386: "model_xannotation_XAnnotationElementValuePair" = None, XExpression326: "model_ss_RichStringForLoop" = None, XExpression338: "model_ss_RichStringElseIf" = None, XExpression255: "model_xbase_XIndexOperation" = None, XExpression182: "model_xbase_XCastedExpression" = None, XExpression222: "model_xbase_XThrowExpression" = None, XExpression243: "model_xbase_XPrefixOperation" = None, XExpression57: "model_types_JvmOperation" = None, XExpression194: "model_xbase_XForLoopExpression" = None, XExpression260: "model_xbase_XFunctionDeclaration" = None, XExpression134: "model_xbase_XAbstractFeatureCall" = None, XExpression139: "model_xbase_XMemberFeatureCall" = None, XExpression202: "model_xbase_XForEachExpression" = None, XExpression187: "model_xbase_XBinaryOperation" = None, XExpression158: "model_xbase_XCollectionLiteral" = None, XExpression298: "model_ss_XtendFunction" = None, XExpression384: "model_xannotation_XAnnotation" = None, XExpression241: "model_xbase_XReturnExpression" = None, XExpression210: "model_xbase_XAbstractWhileExpression" = None, XExpression141: "model_xbase_XMemberFeatureCall1" = None, XExpression331: "model_ss_RichStringIf" = None, XExpression213: "model_xbase_XAbstractWhileExpression" = None):
        self.name = name
        self.model_xbase_XFunctionDeclaration = model_xbase_XFunctionDeclaration
        self.model_xbase_XFunctionDeclaration262 = model_xbase_XFunctionDeclaration262
        self.model_xbase_XFunctionDeclaration265 = model_xbase_XFunctionDeclaration265 if model_xbase_XFunctionDeclaration265 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "XExpression260"):
                opp_val = getattr(old_value, "XExpression260", None)
                if opp_val == self:
                    setattr(old_value, "XExpression260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression260"):
                opp_val = getattr(value, "XExpression260", None)
                setattr(value, "XExpression260", self)

    @property
    def model_xbase_XFunctionDeclaration262(self):
        return self.__model_xbase_XFunctionDeclaration262

    @model_xbase_XFunctionDeclaration262.setter
    def model_xbase_XFunctionDeclaration262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFunctionDeclaration__model_xbase_XFunctionDeclaration262", None)
        self.__model_xbase_XFunctionDeclaration262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmTypeReference263"):
                opp_val = getattr(old_value, "JvmTypeReference263", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference263"):
                opp_val = getattr(value, "JvmTypeReference263", None)
                setattr(value, "JvmTypeReference263", self)

    @property
    def model_xbase_XFunctionDeclaration265(self):
        return self.__model_xbase_XFunctionDeclaration265

    @model_xbase_XFunctionDeclaration265.setter
    def model_xbase_XFunctionDeclaration265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_xbase_XFunctionDeclaration__model_xbase_XFunctionDeclaration265", None)
        self.__model_xbase_XFunctionDeclaration265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmFormalParameter266"):
                    opp_val = getattr(item, "JvmFormalParameter266", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmFormalParameter266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmFormalParameter266"):
                    opp_val = getattr(item, "JvmFormalParameter266", None)
                    
                    setattr(item, "JvmFormalParameter266", self)
                    

class model_xbase_XTryCatchFinallyExpression(XExpression):

    pass
class JvmFeature:

    pass
class model_types_JvmField(JvmFeature):

    def __init__(self, static: bool, final: bool, volatile: bool, transient: bool, model_types_JvmField: "JvmTypeReference" = None, model_types_JvmField38: "XExpression" = None, model_types_JvmField40: "XExpression" = None, model_types_JvmField43: "XExpression" = None):
        self.static = static
        self.final = final
        self.volatile = volatile
        self.transient = transient
        self.model_types_JvmField = model_types_JvmField
        self.model_types_JvmField38 = model_types_JvmField38
        self.model_types_JvmField40 = model_types_JvmField40
        self.model_types_JvmField43 = model_types_JvmField43
        
        pass
    @property
    def volatile(self):
        return self.__volatile

    @volatile.setter
    def volatile(self, volatile: bool):
        self.__volatile = volatile


    @property
    def transient(self):
        return self.__transient

    @transient.setter
    def transient(self, transient: bool):
        self.__transient = transient


    @property
    def static(self):
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static


    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, final: bool):
        self.__final = final


    @property
    def model_types_JvmField43(self):
        return self.__model_types_JvmField43

    @model_types_JvmField43.setter
    def model_types_JvmField43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField43", None)
        self.__model_types_JvmField43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression44"):
                opp_val = getattr(old_value, "XExpression44", None)
                if opp_val == self:
                    setattr(old_value, "XExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression44"):
                opp_val = getattr(value, "XExpression44", None)
                setattr(value, "XExpression44", self)

    @property
    def model_types_JvmField40(self):
        return self.__model_types_JvmField40

    @model_types_JvmField40.setter
    def model_types_JvmField40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField40", None)
        self.__model_types_JvmField40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XExpression41"):
                opp_val = getattr(old_value, "XExpression41", None)
                if opp_val == self:
                    setattr(old_value, "XExpression41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XExpression41"):
                opp_val = getattr(value, "XExpression41", None)
                setattr(value, "XExpression41", self)

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
            if hasattr(old_value, "JvmTypeReference36"):
                opp_val = getattr(old_value, "JvmTypeReference36", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference36"):
                opp_val = getattr(value, "JvmTypeReference36", None)
                setattr(value, "JvmTypeReference36", self)

    @property
    def model_types_JvmField38(self):
        return self.__model_types_JvmField38

    @model_types_JvmField38.setter
    def model_types_JvmField38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmField__model_types_JvmField38", None)
        self.__model_types_JvmField38 = value
        
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

class model_types_JvmFeature(JvmMember):

    def __init__(self, JvmMember: "model_types_JvmDeclaredType" = None):
        
        pass
    def isStatic(self) :
        # TODO: Implement isStatic method
        pass

class model_types_JvmTypeReference(ABC):

    def __init__(self):
        
        pass
    def getQualifiedName(self, model_innerClassDelimiter) :
        # TODO: Implement getQualifiedName method
        pass

    def getIdentifier(self) :
        # TODO: Implement getIdentifier method
        pass

    def getType(self) :
        # TODO: Implement getType method
        pass

    def getSimpleName(self) :
        # TODO: Implement getSimpleName method
        pass

    def accept(self, model_visitor):
        # TODO: Implement accept method
        pass

class model_types_JvmAnyTypeReference(JvmTypeReference):

    pass
class types_JvmTypeReference:

    pass
class model_types_JvmWildcardTypeReference(types_JvmTypeReference, types_JvmConstraintOwner):

    pass
class model_types_JvmGenericArrayTypeReference(JvmTypeReference):

    def __init__(self, model_types_JvmGenericArrayTypeReference: "JvmTypeReference" = None, JvmTypeReference128: "model_xbase_XAbstractFeatureCall" = None, JvmTypeReference358: "model_ss_XtendInterface" = None, JvmTypeReference85: "model_types_JvmDelegateTypeReference" = None, JvmTypeReference374: "model_ss_XtendEvent" = None, JvmTypeReference156: "model_xbase_XConstructorCall" = None, JvmTypeReference311: "model_ss_XtendFunction" = None, JvmTypeReference: "model_types_JvmDeclaredType" = None, JvmTypeReference62: "model_types_JvmFormalParameter" = None, JvmTypeReference52: "model_types_JvmOperation" = None, JvmTypeReference119: "model_xbase_XVariableDeclaration" = None, JvmTypeReference26: "model_types_JvmParameterizedTypeReference" = None, JvmTypeReference18: "model_types_JvmTypeConstraint" = None, JvmTypeReference363: "model_ss_XtendDelegate" = None, JvmTypeReference372: "model_ss_XtendDelegate" = None, JvmTypeReference174: "model_xbase_XClosure" = None, JvmTypeReference92: "model_types_JvmCompoundTypeReference" = None, JvmTypeReference285: "model_ss_XtendClass" = None, JvmTypeReference87: "model_types_JvmSpecializedTypeReference" = None, JvmTypeReference354: "model_ss_XtendConstructor" = None, JvmTypeReference79: "model_types_JvmTypeAnnotationValue" = None, JvmTypeReference36: "model_types_JvmField" = None, JvmTypeReference48: "model_types_JvmExecutable" = None, JvmTypeReference301: "model_ss_XtendFunction" = None, JvmTypeReference313: "model_ss_XtendField" = None, JvmTypeReference179: "model_xbase_XCastedExpression" = None, JvmTypeReference30: "model_types_JvmGenericArrayTypeReference" = None, JvmTypeReference394: "model_xtype_XFunctionTypeRef" = None, JvmTypeReference318: "model_ss_XtendParameter" = None, JvmTypeReference391: "model_xtype_XFunctionTypeRef" = None, JvmTypeReference115: "model_xbase_XCasePart" = None, JvmTypeReference217: "model_xbase_XInstanceOfExpression" = None, JvmTypeReference263: "model_xbase_XFunctionDeclaration" = None, JvmTypeReference288: "model_ss_XtendClass" = None):
        self.model_types_JvmGenericArrayTypeReference = model_types_JvmGenericArrayTypeReference
        
        pass
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
            if hasattr(old_value, "JvmTypeReference30"):
                opp_val = getattr(old_value, "JvmTypeReference30", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference30"):
                opp_val = getattr(value, "JvmTypeReference30", None)
                setattr(value, "JvmTypeReference30", self)

    def getType(self) :
        # TODO: Implement getType method
        pass

    def getDimensions(self) :
        # TODO: Implement getDimensions method
        pass

class model_types_JvmParameterizedTypeReference(JvmTypeReference):

    pass
class JvmConstraintOwner:

    pass
class model_types_JvmTypeConstraint(ABC):

    def __init__(self, constraints: "JvmConstraintOwner" = None, model_types_JvmTypeConstraint: "JvmTypeReference" = None):
        self.constraints = constraints
        self.model_types_JvmTypeConstraint = model_types_JvmTypeConstraint
        
        pass
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
            if hasattr(old_value, "JvmTypeReference18"):
                opp_val = getattr(old_value, "JvmTypeReference18", None)
                if opp_val == self:
                    setattr(old_value, "JvmTypeReference18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmTypeReference18"):
                opp_val = getattr(value, "JvmTypeReference18", None)
                setattr(value, "JvmTypeReference18", self)

    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmTypeConstraint__constraints", None)
        self.__constraints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JvmConstraintOwner"):
                opp_val = getattr(old_value, "JvmConstraintOwner", None)
                if opp_val == self:
                    setattr(old_value, "JvmConstraintOwner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JvmConstraintOwner"):
                opp_val = getattr(value, "JvmConstraintOwner", None)
                setattr(value, "JvmConstraintOwner", self)

    def getQualifiedName(self, model_innerClassDelimiter) :
        # TODO: Implement getQualifiedName method
        pass

    def getSimpleName(self) :
        # TODO: Implement getSimpleName method
        pass

    def getIdentifier(self) :
        # TODO: Implement getIdentifier method
        pass

class JvmTypeConstraint:

    pass
class model_types_JvmConstraintOwner(ABC):

    pass
class JvmParameterizedTypeReference:

    pass
class JvmTypeParameter:

    pass
class types_JvmTypeParameterDeclarator:

    pass
class model_types_JvmExecutable(types_JvmFeature, types_JvmTypeParameterDeclarator):

    def __init__(self, varArgs: bool, model_types_JvmExecutable: set["JvmFormalParameter"] = None, model_types_JvmExecutable47: set["JvmTypeReference"] = None):
        self.varArgs = varArgs
        self.model_types_JvmExecutable = model_types_JvmExecutable if model_types_JvmExecutable is not None else set()
        self.model_types_JvmExecutable47 = model_types_JvmExecutable47 if model_types_JvmExecutable47 is not None else set()
        
        pass
    @property
    def varArgs(self):
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
    def model_types_JvmExecutable47(self):
        return self.__model_types_JvmExecutable47

    @model_types_JvmExecutable47.setter
    def model_types_JvmExecutable47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmExecutable__model_types_JvmExecutable47", None)
        self.__model_types_JvmExecutable47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmTypeReference48"):
                    opp_val = getattr(item, "JvmTypeReference48", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmTypeReference48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmTypeReference48"):
                    opp_val = getattr(item, "JvmTypeReference48", None)
                    
                    setattr(item, "JvmTypeReference48", self)
                    

class types_JvmDeclaredType:

    pass
class model_types_JvmGenericType(types_JvmTypeParameterDeclarator, types_JvmDeclaredType):

    def __init__(self, interface: bool, strictFloatingPoint: bool, model_types_JvmGenericType: "JvmParameterizedTypeReference" = None, model_types_JvmGenericType23: set["JvmParameterizedTypeReference"] = None):
        self.interface = interface
        self.strictFloatingPoint = strictFloatingPoint
        self.model_types_JvmGenericType = model_types_JvmGenericType
        self.model_types_JvmGenericType23 = model_types_JvmGenericType23 if model_types_JvmGenericType23 is not None else set()
        
        pass
    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface


    @property
    def strictFloatingPoint(self):
        return self.__strictFloatingPoint

    @strictFloatingPoint.setter
    def strictFloatingPoint(self, strictFloatingPoint: bool):
        self.__strictFloatingPoint = strictFloatingPoint


    @property
    def model_types_JvmGenericType23(self):
        return self.__model_types_JvmGenericType23

    @model_types_JvmGenericType23.setter
    def model_types_JvmGenericType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_types_JvmGenericType__model_types_JvmGenericType23", None)
        self.__model_types_JvmGenericType23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JvmParameterizedTypeReference24"):
                    opp_val = getattr(item, "JvmParameterizedTypeReference24", None)
                    
                    if opp_val == self:
                        setattr(item, "JvmParameterizedTypeReference24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JvmParameterizedTypeReference24"):
                    opp_val = getattr(item, "JvmParameterizedTypeReference24", None)
                    
                    setattr(item, "JvmParameterizedTypeReference24", self)
                    

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

    def getDeclaredConstructors(self):
        # TODO: Implement getDeclaredConstructors method
        pass

    def getExtendedInterfaces(self):
        # TODO: Implement getExtendedInterfaces method
        pass

    def isInstantiateable(self) :
        # TODO: Implement isInstantiateable method
        pass

    def getExtendedClass(self) :
        # TODO: Implement getExtendedClass method
        pass

class JvmField:

    pass
class model_types_JvmEnumerationLiteral(JvmField):

    def __init__(self):
        
        pass
    def getEnumType(self) :
        # TODO: Implement getEnumType method
        pass

class JvmEnumerationLiteral:

    pass
class JvmDeclaredType:

    pass
class model_types_JvmEnumerationType(JvmDeclaredType):

    pass
class model_types_JvmAnnotationType(JvmDeclaredType):

    pass
class model_types_JvmLowerBound(JvmTypeConstraint):

    pass
class model_types_JvmUpperBound(JvmTypeConstraint):

    pass
class model_types_JvmTypeParameterDeclarator(ABC):

    pass