from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OpenModeKind(Enum):
    Append = "Append"
    OverWrite = "OverWrite"
class VisibilityKind(Enum):
    Private = "Private"
    Protected = "Protected"
    Public = "Public"


############################################
# Definition of Classes
############################################

class Documentation:

    pass
class mtl_ModuleElementDocumentation(Documentation):

    pass
class mtl_ModuleDocumentation(Documentation):

    def __init__(self, author: str, version: str, since: str):
        self.author = author
        self.version = version
        self.since = since
        
    @property
    def since(self) -> str:
        return self.__since

    @since.setter
    def since(self, since: str):
        self.__since = since

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

class mtl_DocumentedElement(ABC):

    def __init__(self, deprecated: bool, DocumentedElement: "mtl_Documentation" = None, documentedElement: "mtl_Documentation" = None):
        self.deprecated = deprecated
        self.DocumentedElement = DocumentedElement
        self.documentedElement = documentedElement
        
    @property
    def deprecated(self) -> bool:
        return self.__deprecated

    @deprecated.setter
    def deprecated(self, deprecated: bool):
        self.__deprecated = deprecated

    @property
    def documentedElement(self):
        return self.__documentedElement

    @documentedElement.setter
    def documentedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_DocumentedElement__documentedElement", None)
        self.__documentedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation"):
                opp_val = getattr(old_value, "Documentation", None)
                if opp_val == self:
                    setattr(old_value, "Documentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation"):
                opp_val = getattr(value, "Documentation", None)
                setattr(value, "Documentation", self)

    @property
    def DocumentedElement(self):
        return self.__DocumentedElement

    @DocumentedElement.setter
    def DocumentedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_DocumentedElement__DocumentedElement", None)
        self.__DocumentedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation"):
                opp_val = getattr(old_value, "documentation", None)
                if opp_val == self:
                    setattr(old_value, "documentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation"):
                opp_val = getattr(value, "documentation", None)
                setattr(value, "documentation", self)

class Comment:

    pass
class mtl_ParameterDocumentation(Comment):

    pass
class mtl_Documentation(Comment):

    pass
class mtl_CommentBody:

    def __init__(self, startPosition: int, endPosition: int, value: str, mtl_CommentBody: "mtl_Comment" = None):
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.value = value
        self.mtl_CommentBody = mtl_CommentBody
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def endPosition(self) -> int:
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: int):
        self.__endPosition = endPosition

    @property
    def startPosition(self) -> int:
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition

    @property
    def mtl_CommentBody(self):
        return self.__mtl_CommentBody

    @mtl_CommentBody.setter
    def mtl_CommentBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_CommentBody__mtl_CommentBody", None)
        self.__mtl_CommentBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_Comment"):
                opp_val = getattr(old_value, "mtl_Comment", None)
                if opp_val == self:
                    setattr(old_value, "mtl_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_Comment"):
                opp_val = getattr(value, "mtl_Comment", None)
                setattr(value, "mtl_Comment", self)

class mtl_EPackage:

    pass
class mtl_EClassifier:

    pass
class ASTNode:

    pass
class mtl_InitSection(ASTNode):

    pass
class TemplateExpression:

    pass
class mtl_MacroInvocation(TemplateExpression):

    pass
class mtl_QueryInvocation(TemplateExpression):

    pass
class mtl_Block(TemplateExpression):

    pass
class OCLExpression:

    pass
class mtl_TemplateExpression(OCLExpression):

    pass
class utilities_ASTNode:

    pass
class ENamedElement:

    pass
class mtl_TemplateInvocation(TemplateExpression):

    def __init__(self, super: bool, mtl_TemplateInvocation: "mtl_Template" = None, mtl_TemplateInvocation28: set["OCLExpression"] = None, mtl_TemplateInvocation31: "OCLExpression" = None, mtl_TemplateInvocation34: "OCLExpression" = None, mtl_TemplateInvocation37: "OCLExpression" = None):
        self.super = super
        self.mtl_TemplateInvocation = mtl_TemplateInvocation
        self.mtl_TemplateInvocation28 = mtl_TemplateInvocation28 if mtl_TemplateInvocation28 is not None else set()
        self.mtl_TemplateInvocation31 = mtl_TemplateInvocation31
        self.mtl_TemplateInvocation34 = mtl_TemplateInvocation34
        self.mtl_TemplateInvocation37 = mtl_TemplateInvocation37
        
    @property
    def super(self) -> bool:
        return self.__super

    @super.setter
    def super(self, super: bool):
        self.__super = super

    @property
    def mtl_TemplateInvocation37(self):
        return self.__mtl_TemplateInvocation37

    @mtl_TemplateInvocation37.setter
    def mtl_TemplateInvocation37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_TemplateInvocation__mtl_TemplateInvocation37", None)
        self.__mtl_TemplateInvocation37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression38"):
                opp_val = getattr(old_value, "OCLExpression38", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression38"):
                opp_val = getattr(value, "OCLExpression38", None)
                setattr(value, "OCLExpression38", self)

    @property
    def mtl_TemplateInvocation(self):
        return self.__mtl_TemplateInvocation

    @mtl_TemplateInvocation.setter
    def mtl_TemplateInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_TemplateInvocation__mtl_TemplateInvocation", None)
        self.__mtl_TemplateInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_Template26"):
                opp_val = getattr(old_value, "mtl_Template26", None)
                if opp_val == self:
                    setattr(old_value, "mtl_Template26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_Template26"):
                opp_val = getattr(value, "mtl_Template26", None)
                setattr(value, "mtl_Template26", self)

    @property
    def mtl_TemplateInvocation28(self):
        return self.__mtl_TemplateInvocation28

    @mtl_TemplateInvocation28.setter
    def mtl_TemplateInvocation28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_TemplateInvocation__mtl_TemplateInvocation28", None)
        self.__mtl_TemplateInvocation28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCLExpression29"):
                    opp_val = getattr(item, "OCLExpression29", None)
                    
                    if opp_val == self:
                        setattr(item, "OCLExpression29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCLExpression29"):
                    opp_val = getattr(item, "OCLExpression29", None)
                    
                    setattr(item, "OCLExpression29", self)
                    

    @property
    def mtl_TemplateInvocation34(self):
        return self.__mtl_TemplateInvocation34

    @mtl_TemplateInvocation34.setter
    def mtl_TemplateInvocation34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_TemplateInvocation__mtl_TemplateInvocation34", None)
        self.__mtl_TemplateInvocation34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression35"):
                opp_val = getattr(old_value, "OCLExpression35", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression35"):
                opp_val = getattr(value, "OCLExpression35", None)
                setattr(value, "OCLExpression35", self)

    @property
    def mtl_TemplateInvocation31(self):
        return self.__mtl_TemplateInvocation31

    @mtl_TemplateInvocation31.setter
    def mtl_TemplateInvocation31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_TemplateInvocation__mtl_TemplateInvocation31", None)
        self.__mtl_TemplateInvocation31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression32"):
                opp_val = getattr(old_value, "OCLExpression32", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression32"):
                opp_val = getattr(value, "OCLExpression32", None)
                setattr(value, "OCLExpression32", self)

class ModuleElement:

    pass
class mtl_Comment(ModuleElement):

    pass
class Block:

    pass
class mtl_FileBlock(Block):

    def __init__(self, openMode: str, mtl_FileBlock: "OCLExpression" = None, mtl_FileBlock89: "OCLExpression" = None, mtl_FileBlock92: "OCLExpression" = None):
        self.openMode = openMode
        self.mtl_FileBlock = mtl_FileBlock
        self.mtl_FileBlock89 = mtl_FileBlock89
        self.mtl_FileBlock92 = mtl_FileBlock92
        
    @property
    def openMode(self) -> str:
        return self.__openMode

    @openMode.setter
    def openMode(self, openMode: str):
        self.__openMode = openMode

    @property
    def mtl_FileBlock89(self):
        return self.__mtl_FileBlock89

    @mtl_FileBlock89.setter
    def mtl_FileBlock89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_FileBlock__mtl_FileBlock89", None)
        self.__mtl_FileBlock89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression90"):
                opp_val = getattr(old_value, "OCLExpression90", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression90"):
                opp_val = getattr(value, "OCLExpression90", None)
                setattr(value, "OCLExpression90", self)

    @property
    def mtl_FileBlock(self):
        return self.__mtl_FileBlock

    @mtl_FileBlock.setter
    def mtl_FileBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_FileBlock__mtl_FileBlock", None)
        self.__mtl_FileBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression87"):
                opp_val = getattr(old_value, "OCLExpression87", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression87"):
                opp_val = getattr(value, "OCLExpression87", None)
                setattr(value, "OCLExpression87", self)

    @property
    def mtl_FileBlock92(self):
        return self.__mtl_FileBlock92

    @mtl_FileBlock92.setter
    def mtl_FileBlock92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_FileBlock__mtl_FileBlock92", None)
        self.__mtl_FileBlock92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression93"):
                opp_val = getattr(old_value, "OCLExpression93", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression93"):
                opp_val = getattr(value, "OCLExpression93", None)
                setattr(value, "OCLExpression93", self)

class mtl_LetBlock(Block):

    pass
class mtl_IfBlock(Block):

    pass
class mtl_TraceBlock(Block):

    pass
class mtl_ProtectedAreaBlock(Block):

    pass
class mtl_ForBlock(Block):

    pass
class Variable:

    pass
class mtl_ModuleElement(utilities_ASTNode, ENamedElement):

    def __init__(self, visibility: str, mtl_ModuleElement: "mtl_Module" = None):
        self.visibility = visibility
        self.mtl_ModuleElement = mtl_ModuleElement
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def mtl_ModuleElement(self):
        return self.__mtl_ModuleElement

    @mtl_ModuleElement.setter
    def mtl_ModuleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_ModuleElement__mtl_ModuleElement", None)
        self.__mtl_ModuleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_Module8"):
                opp_val = getattr(old_value, "mtl_Module8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_Module8"):
                opp_val = getattr(value, "mtl_Module8", None)
                if opp_val is None:
                    setattr(value, "mtl_Module8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mtl_TypedModel:

    pass
class DocumentedElement:

    pass
class mtl_Template(Block, ModuleElement, DocumentedElement):

    def __init__(self, main: bool, mtl_Template: "mtl_Template" = None, mtl_Template14: set["mtl_Template"] = None, mtl_Template17: set["Variable"] = None, mtl_Template20: "OCLExpression" = None, mtl_Template23: "OCLExpression" = None, mtl_Template26: "mtl_TemplateInvocation" = None):
        self.main = main
        self.mtl_Template = mtl_Template
        self.mtl_Template14 = mtl_Template14 if mtl_Template14 is not None else set()
        self.mtl_Template17 = mtl_Template17 if mtl_Template17 is not None else set()
        self.mtl_Template20 = mtl_Template20
        self.mtl_Template23 = mtl_Template23
        self.mtl_Template26 = mtl_Template26
        
    @property
    def main(self) -> bool:
        return self.__main

    @main.setter
    def main(self, main: bool):
        self.__main = main

    @property
    def mtl_Template26(self):
        return self.__mtl_Template26

    @mtl_Template26.setter
    def mtl_Template26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Template__mtl_Template26", None)
        self.__mtl_Template26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_TemplateInvocation"):
                opp_val = getattr(old_value, "mtl_TemplateInvocation", None)
                if opp_val == self:
                    setattr(old_value, "mtl_TemplateInvocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_TemplateInvocation"):
                opp_val = getattr(value, "mtl_TemplateInvocation", None)
                setattr(value, "mtl_TemplateInvocation", self)

    @property
    def mtl_Template20(self):
        return self.__mtl_Template20

    @mtl_Template20.setter
    def mtl_Template20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Template__mtl_Template20", None)
        self.__mtl_Template20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression21"):
                opp_val = getattr(old_value, "OCLExpression21", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression21"):
                opp_val = getattr(value, "OCLExpression21", None)
                setattr(value, "OCLExpression21", self)

    @property
    def mtl_Template23(self):
        return self.__mtl_Template23

    @mtl_Template23.setter
    def mtl_Template23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Template__mtl_Template23", None)
        self.__mtl_Template23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpression24"):
                opp_val = getattr(old_value, "OCLExpression24", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpression24"):
                opp_val = getattr(value, "OCLExpression24", None)
                setattr(value, "OCLExpression24", self)

    @property
    def mtl_Template14(self):
        return self.__mtl_Template14

    @mtl_Template14.setter
    def mtl_Template14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Template__mtl_Template14", None)
        self.__mtl_Template14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtl_Template"):
                    opp_val = getattr(item, "mtl_Template", None)
                    
                    if opp_val == self:
                        setattr(item, "mtl_Template", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtl_Template"):
                    opp_val = getattr(item, "mtl_Template", None)
                    
                    setattr(item, "mtl_Template", self)
                    

    @property
    def mtl_Template(self):
        return self.__mtl_Template

    @mtl_Template.setter
    def mtl_Template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Template__mtl_Template", None)
        self.__mtl_Template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_Template14"):
                opp_val = getattr(old_value, "mtl_Template14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_Template14"):
                opp_val = getattr(value, "mtl_Template14", None)
                if opp_val is None:
                    setattr(value, "mtl_Template14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mtl_Template17(self):
        return self.__mtl_Template17

    @mtl_Template17.setter
    def mtl_Template17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Template__mtl_Template17", None)
        self.__mtl_Template17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable18"):
                    opp_val = getattr(item, "Variable18", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable18"):
                    opp_val = getattr(item, "Variable18", None)
                    
                    setattr(item, "Variable18", self)
                    

class mtl_Macro(Block, ModuleElement, DocumentedElement):

    pass
class mtl_Query(ModuleElement, DocumentedElement):

    pass
class EPackage:

    pass
class mtl_Module(DocumentedElement, EPackage):

    def __init__(self, startHeaderPosition: int, endHeaderPosition: int, mtl_Module: set["mtl_TypedModel"] = None, mtl_Module3: "mtl_Module" = None, mtl_Module1: set["mtl_Module"] = None, mtl_Module6: "mtl_Module" = None, mtl_Module4: set["mtl_Module"] = None, mtl_Module8: set["mtl_ModuleElement"] = None):
        self.startHeaderPosition = startHeaderPosition
        self.endHeaderPosition = endHeaderPosition
        self.mtl_Module = mtl_Module if mtl_Module is not None else set()
        self.mtl_Module3 = mtl_Module3
        self.mtl_Module1 = mtl_Module1 if mtl_Module1 is not None else set()
        self.mtl_Module6 = mtl_Module6
        self.mtl_Module4 = mtl_Module4 if mtl_Module4 is not None else set()
        self.mtl_Module8 = mtl_Module8 if mtl_Module8 is not None else set()
        
    @property
    def startHeaderPosition(self) -> int:
        return self.__startHeaderPosition

    @startHeaderPosition.setter
    def startHeaderPosition(self, startHeaderPosition: int):
        self.__startHeaderPosition = startHeaderPosition

    @property
    def endHeaderPosition(self) -> int:
        return self.__endHeaderPosition

    @endHeaderPosition.setter
    def endHeaderPosition(self, endHeaderPosition: int):
        self.__endHeaderPosition = endHeaderPosition

    @property
    def mtl_Module1(self):
        return self.__mtl_Module1

    @mtl_Module1.setter
    def mtl_Module1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Module__mtl_Module1", None)
        self.__mtl_Module1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtl_Module3"):
                    opp_val = getattr(item, "mtl_Module3", None)
                    
                    if opp_val == self:
                        setattr(item, "mtl_Module3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtl_Module3"):
                    opp_val = getattr(item, "mtl_Module3", None)
                    
                    setattr(item, "mtl_Module3", self)
                    

    @property
    def mtl_Module6(self):
        return self.__mtl_Module6

    @mtl_Module6.setter
    def mtl_Module6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Module__mtl_Module6", None)
        self.__mtl_Module6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_Module4"):
                opp_val = getattr(old_value, "mtl_Module4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_Module4"):
                opp_val = getattr(value, "mtl_Module4", None)
                if opp_val is None:
                    setattr(value, "mtl_Module4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mtl_Module8(self):
        return self.__mtl_Module8

    @mtl_Module8.setter
    def mtl_Module8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Module__mtl_Module8", None)
        self.__mtl_Module8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtl_ModuleElement"):
                    opp_val = getattr(item, "mtl_ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "mtl_ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtl_ModuleElement"):
                    opp_val = getattr(item, "mtl_ModuleElement", None)
                    
                    setattr(item, "mtl_ModuleElement", self)
                    

    @property
    def mtl_Module(self):
        return self.__mtl_Module

    @mtl_Module.setter
    def mtl_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Module__mtl_Module", None)
        self.__mtl_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtl_TypedModel"):
                    opp_val = getattr(item, "mtl_TypedModel", None)
                    
                    if opp_val == self:
                        setattr(item, "mtl_TypedModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtl_TypedModel"):
                    opp_val = getattr(item, "mtl_TypedModel", None)
                    
                    setattr(item, "mtl_TypedModel", self)
                    

    @property
    def mtl_Module4(self):
        return self.__mtl_Module4

    @mtl_Module4.setter
    def mtl_Module4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Module__mtl_Module4", None)
        self.__mtl_Module4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mtl_Module6"):
                    opp_val = getattr(item, "mtl_Module6", None)
                    
                    if opp_val == self:
                        setattr(item, "mtl_Module6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mtl_Module6"):
                    opp_val = getattr(item, "mtl_Module6", None)
                    
                    setattr(item, "mtl_Module6", self)
                    

    @property
    def mtl_Module3(self):
        return self.__mtl_Module3

    @mtl_Module3.setter
    def mtl_Module3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mtl_Module__mtl_Module3", None)
        self.__mtl_Module3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mtl_Module1"):
                opp_val = getattr(old_value, "mtl_Module1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mtl_Module1"):
                opp_val = getattr(value, "mtl_Module1", None)
                if opp_val is None:
                    setattr(value, "mtl_Module1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
