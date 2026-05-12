from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DocType(Enum):
    BPM_TASK = "BPM_TASK"
    VAACLIPSE_VIEW = "VAACLIPSE_VIEW"
    UI = "UI"
    ENTITY = "ENTITY"
    DTO = "DTO"
    BPM_PROCESS = "BPM_PROCESS"


############################################
# Definition of Classes
############################################

class RichStringTableRow:

    pass
class RichStringElseIf:

    pass
class RichStringMarkup:

    pass
class luniferadoc_richstring_RichStringChapter(RichStringMarkup):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class luniferadoc_richstring_RichStringH4(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringSkype(RichStringMarkup):

    def __init__(self, target: str, luniferadoc_richstring_RichStringSkype: "richstring_luniferadoc_XExpression" = None):
        self.target = target
        self.luniferadoc_richstring_RichStringSkype = luniferadoc_richstring_RichStringSkype
        
        pass
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def luniferadoc_richstring_RichStringSkype(self):
        return self.__luniferadoc_richstring_RichStringSkype

    @luniferadoc_richstring_RichStringSkype.setter
    def luniferadoc_richstring_RichStringSkype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringSkype__luniferadoc_richstring_RichStringSkype", None)
        self.__luniferadoc_richstring_RichStringSkype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression64"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression64", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression64"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression64", None)
                setattr(value, "richstring_luniferadoc_XExpression64", self)

class luniferadoc_richstring_RichStringBold(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringMovie(RichStringMarkup):

    def __init__(self, src: str, width: str, height: str, type: str, luniferadoc_richstring_RichStringMovie: "richstring_luniferadoc_XExpression" = None):
        self.src = src
        self.width = width
        self.height = height
        self.type = type
        self.luniferadoc_richstring_RichStringMovie = luniferadoc_richstring_RichStringMovie
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def luniferadoc_richstring_RichStringMovie(self):
        return self.__luniferadoc_richstring_RichStringMovie

    @luniferadoc_richstring_RichStringMovie.setter
    def luniferadoc_richstring_RichStringMovie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringMovie__luniferadoc_richstring_RichStringMovie", None)
        self.__luniferadoc_richstring_RichStringMovie = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression66"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression66", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression66"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression66", None)
                setattr(value, "richstring_luniferadoc_XExpression66", self)

class luniferadoc_richstring_RichStringH5(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringURL(RichStringMarkup):

    def __init__(self, location: str, luniferadoc_richstring_RichStringURL: "richstring_luniferadoc_XExpression" = None):
        self.location = location
        self.luniferadoc_richstring_RichStringURL = luniferadoc_richstring_RichStringURL
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def luniferadoc_richstring_RichStringURL(self):
        return self.__luniferadoc_richstring_RichStringURL

    @luniferadoc_richstring_RichStringURL.setter
    def luniferadoc_richstring_RichStringURL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringURL__luniferadoc_richstring_RichStringURL", None)
        self.__luniferadoc_richstring_RichStringURL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression58"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression58", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression58"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression58", None)
                setattr(value, "richstring_luniferadoc_XExpression58", self)

class luniferadoc_richstring_RichStringSubsection(RichStringMarkup):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class luniferadoc_richstring_RichStringTable(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringItalic(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringH6(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringImg(RichStringMarkup):

    def __init__(self, src: str, alt: str, width: str, height: str, luniferadoc_richstring_RichStringImg: "richstring_luniferadoc_XExpression" = None):
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height
        self.luniferadoc_richstring_RichStringImg = luniferadoc_richstring_RichStringImg
        
        pass
    @property
    def alt(self):
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def luniferadoc_richstring_RichStringImg(self):
        return self.__luniferadoc_richstring_RichStringImg

    @luniferadoc_richstring_RichStringImg.setter
    def luniferadoc_richstring_RichStringImg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringImg__luniferadoc_richstring_RichStringImg", None)
        self.__luniferadoc_richstring_RichStringImg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression60"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression60", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression60"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression60", None)
                setattr(value, "richstring_luniferadoc_XExpression60", self)

class luniferadoc_richstring_RichStringUnderline(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringSection(RichStringMarkup):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class luniferadoc_richstring_RichStringMailto(RichStringMarkup):

    def __init__(self, email: str, luniferadoc_richstring_RichStringMailto: "richstring_luniferadoc_XExpression" = None):
        self.email = email
        self.luniferadoc_richstring_RichStringMailto = luniferadoc_richstring_RichStringMailto
        
        pass
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def luniferadoc_richstring_RichStringMailto(self):
        return self.__luniferadoc_richstring_RichStringMailto

    @luniferadoc_richstring_RichStringMailto.setter
    def luniferadoc_richstring_RichStringMailto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringMailto__luniferadoc_richstring_RichStringMailto", None)
        self.__luniferadoc_richstring_RichStringMailto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression62"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression62", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression62"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression62", None)
                setattr(value, "richstring_luniferadoc_XExpression62", self)

class luniferadoc_richstring_RichStringRef(RichStringMarkup):

    def __init__(self, refId: str):
        self.refId = refId
        
        pass
    @property
    def refId(self):
        return self.__refId

    @refId.setter
    def refId(self, refId: str):
        self.__refId = refId


class luniferadoc_richstring_RichStringH2(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringH3(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringH1(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringExample(RichStringMarkup):

    pass
class XForLoopExpression:

    pass
class luniferadoc_richstring_RichStringForLoop(XForLoopExpression):

    pass
class XStringLiteral:

    pass
class luniferadoc_richstring_RichStringLiteral(XStringLiteral):

    pass
class XBlockExpression:

    pass
class luniferadoc_richstring_RichString(XBlockExpression):

    pass
class XExpression:

    pass
class luniferadoc_richstring_RichStringMarkup(XExpression):

    def __init__(self, id: str, styleClass: str, luniferadoc_richstring_RichStringMarkup: "richstring_luniferadoc_XExpression" = None):
        self.id = id
        self.styleClass = styleClass
        self.luniferadoc_richstring_RichStringMarkup = luniferadoc_richstring_RichStringMarkup
        
        pass
    @property
    def styleClass(self):
        return self.__styleClass

    @styleClass.setter
    def styleClass(self, styleClass: str):
        self.__styleClass = styleClass


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def luniferadoc_richstring_RichStringMarkup(self):
        return self.__luniferadoc_richstring_RichStringMarkup

    @luniferadoc_richstring_RichStringMarkup.setter
    def luniferadoc_richstring_RichStringMarkup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringMarkup__luniferadoc_richstring_RichStringMarkup", None)
        self.__luniferadoc_richstring_RichStringMarkup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression56"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression56", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression56"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression56", None)
                setattr(value, "richstring_luniferadoc_XExpression56", self)

class luniferadoc_richstring_RichStringIf(XExpression):

    pass
class document_luniferadoc_XImportDeclaration:

    pass
class richstring_luniferadoc_XExpression:

    pass
class luniferadoc_richstring_RichStringElseIf:

    pass
class luniferadoc_document_VaaclipseViewDescription:

    pass
class VaaclipseViewDescription:

    pass
class document_luniferadoc_DocumentInclude:

    pass
class LuniferaDocLayout:

    pass
class luniferadoc_document_UILayout(LuniferaDocLayout):

    pass
class luniferadoc_document_VaaclipseViewLayout(LuniferaDocLayout):

    pass
class luniferadoc_document_BPMProcessLayout(LuniferaDocLayout):

    pass
class luniferadoc_document_EntityLayout(LuniferaDocLayout):

    pass
class luniferadoc_document_DTOLayout(LuniferaDocLayout):

    pass
class luniferadoc_document_BPMHumanTaskLayout(LuniferaDocLayout):

    pass
class luniferadoc_document_GeneralDocument(LuniferaDocLayout):

    pass
class luniferadoc_document_UIDescription:

    pass
class UIDescription:

    pass
class luniferadoc_document_BPMProcessDescription:

    pass
class BPMProcessDescription:

    pass
class luniferadoc_document_DTOProperty:

    def __init__(self, name: str, luniferadoc_document_DTOProperty: "RichString" = None):
        self.name = name
        self.luniferadoc_document_DTOProperty = luniferadoc_document_DTOProperty
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def luniferadoc_document_DTOProperty(self):
        return self.__luniferadoc_document_DTOProperty

    @luniferadoc_document_DTOProperty.setter
    def luniferadoc_document_DTOProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_DTOProperty__luniferadoc_document_DTOProperty", None)
        self.__luniferadoc_document_DTOProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RichString15"):
                opp_val = getattr(old_value, "RichString15", None)
                if opp_val == self:
                    setattr(old_value, "RichString15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RichString15"):
                opp_val = getattr(value, "RichString15", None)
                setattr(value, "RichString15", self)

class luniferadoc_document_BPMHumanTaskDescription:

    pass
class BPMHumanTaskDescription:

    pass
class DTODescription:

    pass
class DTOProperty:

    pass
class luniferadoc_document_DTOProperties:

    pass
class luniferadoc_document_DTODescription:

    pass
class DTOProperties:

    pass
class EntityFields:

    pass
class EntityDescription:

    pass
class NamedDocument:

    pass
class luniferadoc_document_LuniferaDocLayout(NamedDocument):

    pass
class luniferadoc_document_LuniferaDocDocument(NamedDocument):

    pass
class luniferadoc_document_EntityField:

    def __init__(self, name: str, type: str, length: int, pk: bool, nullable: bool, luniferadoc_document_EntityField: "RichString" = None):
        self.name = name
        self.type = type
        self.length = length
        self.pk = pk
        self.nullable = nullable
        self.luniferadoc_document_EntityField = luniferadoc_document_EntityField
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def pk(self):
        return self.__pk

    @pk.setter
    def pk(self, pk: bool):
        self.__pk = pk


    @property
    def luniferadoc_document_EntityField(self):
        return self.__luniferadoc_document_EntityField

    @luniferadoc_document_EntityField.setter
    def luniferadoc_document_EntityField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_EntityField__luniferadoc_document_EntityField", None)
        self.__luniferadoc_document_EntityField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RichString7"):
                opp_val = getattr(old_value, "RichString7", None)
                if opp_val == self:
                    setattr(old_value, "RichString7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RichString7"):
                opp_val = getattr(value, "RichString7", None)
                setattr(value, "RichString7", self)

class EntityField:

    pass
class luniferadoc_document_EntityFields:

    pass
class RichString:

    pass
class luniferadoc_document_EntityDescription:

    pass
class LuniferaDocDocument:

    pass
class luniferadoc_document_BPMHumanTaskDocument(LuniferaDocDocument):

    def __init__(self, task: str, luniferadoc_document_BPMHumanTaskDocument: "BPMHumanTaskDescription" = None, LuniferaDocDocument: "luniferadoc_DocumentInclude" = None):
        self.task = task
        self.luniferadoc_document_BPMHumanTaskDocument = luniferadoc_document_BPMHumanTaskDocument
        
        pass
    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, task: str):
        self.__task = task


    @property
    def luniferadoc_document_BPMHumanTaskDocument(self):
        return self.__luniferadoc_document_BPMHumanTaskDocument

    @luniferadoc_document_BPMHumanTaskDocument.setter
    def luniferadoc_document_BPMHumanTaskDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_BPMHumanTaskDocument__luniferadoc_document_BPMHumanTaskDocument", None)
        self.__luniferadoc_document_BPMHumanTaskDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMHumanTaskDescription"):
                opp_val = getattr(old_value, "BPMHumanTaskDescription", None)
                if opp_val == self:
                    setattr(old_value, "BPMHumanTaskDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMHumanTaskDescription"):
                opp_val = getattr(value, "BPMHumanTaskDescription", None)
                setattr(value, "BPMHumanTaskDescription", self)

class luniferadoc_document_DTODocument(LuniferaDocDocument):

    def __init__(self, dtoClass: str, luniferadoc_document_DTODocument10: "DTOProperties" = None, luniferadoc_document_DTODocument: "DTODescription" = None, LuniferaDocDocument: "luniferadoc_DocumentInclude" = None):
        self.dtoClass = dtoClass
        self.luniferadoc_document_DTODocument10 = luniferadoc_document_DTODocument10
        self.luniferadoc_document_DTODocument = luniferadoc_document_DTODocument
        
        pass
    @property
    def dtoClass(self):
        return self.__dtoClass

    @dtoClass.setter
    def dtoClass(self, dtoClass: str):
        self.__dtoClass = dtoClass


    @property
    def luniferadoc_document_DTODocument10(self):
        return self.__luniferadoc_document_DTODocument10

    @luniferadoc_document_DTODocument10.setter
    def luniferadoc_document_DTODocument10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_DTODocument__luniferadoc_document_DTODocument10", None)
        self.__luniferadoc_document_DTODocument10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DTOProperties"):
                opp_val = getattr(old_value, "DTOProperties", None)
                if opp_val == self:
                    setattr(old_value, "DTOProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DTOProperties"):
                opp_val = getattr(value, "DTOProperties", None)
                setattr(value, "DTOProperties", self)

    @property
    def luniferadoc_document_DTODocument(self):
        return self.__luniferadoc_document_DTODocument

    @luniferadoc_document_DTODocument.setter
    def luniferadoc_document_DTODocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_DTODocument__luniferadoc_document_DTODocument", None)
        self.__luniferadoc_document_DTODocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DTODescription"):
                opp_val = getattr(old_value, "DTODescription", None)
                if opp_val == self:
                    setattr(old_value, "DTODescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DTODescription"):
                opp_val = getattr(value, "DTODescription", None)
                setattr(value, "DTODescription", self)

class luniferadoc_document_UIDocument(LuniferaDocDocument):

    def __init__(self, ui: str, luniferadoc_document_UIDocument: "UIDescription" = None, LuniferaDocDocument: "luniferadoc_DocumentInclude" = None):
        self.ui = ui
        self.luniferadoc_document_UIDocument = luniferadoc_document_UIDocument
        
        pass
    @property
    def ui(self):
        return self.__ui

    @ui.setter
    def ui(self, ui: str):
        self.__ui = ui


    @property
    def luniferadoc_document_UIDocument(self):
        return self.__luniferadoc_document_UIDocument

    @luniferadoc_document_UIDocument.setter
    def luniferadoc_document_UIDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_UIDocument__luniferadoc_document_UIDocument", None)
        self.__luniferadoc_document_UIDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UIDescription"):
                opp_val = getattr(old_value, "UIDescription", None)
                if opp_val == self:
                    setattr(old_value, "UIDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UIDescription"):
                opp_val = getattr(value, "UIDescription", None)
                setattr(value, "UIDescription", self)

class luniferadoc_document_EntityDocument(LuniferaDocDocument):

    def __init__(self, entityClass: str, luniferadoc_document_EntityDocument: "EntityDescription" = None, luniferadoc_document_EntityDocument3: "EntityFields" = None, LuniferaDocDocument: "luniferadoc_DocumentInclude" = None):
        self.entityClass = entityClass
        self.luniferadoc_document_EntityDocument = luniferadoc_document_EntityDocument
        self.luniferadoc_document_EntityDocument3 = luniferadoc_document_EntityDocument3
        
        pass
    @property
    def entityClass(self):
        return self.__entityClass

    @entityClass.setter
    def entityClass(self, entityClass: str):
        self.__entityClass = entityClass


    @property
    def luniferadoc_document_EntityDocument3(self):
        return self.__luniferadoc_document_EntityDocument3

    @luniferadoc_document_EntityDocument3.setter
    def luniferadoc_document_EntityDocument3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_EntityDocument__luniferadoc_document_EntityDocument3", None)
        self.__luniferadoc_document_EntityDocument3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityFields"):
                opp_val = getattr(old_value, "EntityFields", None)
                if opp_val == self:
                    setattr(old_value, "EntityFields", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityFields"):
                opp_val = getattr(value, "EntityFields", None)
                setattr(value, "EntityFields", self)

    @property
    def luniferadoc_document_EntityDocument(self):
        return self.__luniferadoc_document_EntityDocument

    @luniferadoc_document_EntityDocument.setter
    def luniferadoc_document_EntityDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_EntityDocument__luniferadoc_document_EntityDocument", None)
        self.__luniferadoc_document_EntityDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityDescription"):
                opp_val = getattr(old_value, "EntityDescription", None)
                if opp_val == self:
                    setattr(old_value, "EntityDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityDescription"):
                opp_val = getattr(value, "EntityDescription", None)
                setattr(value, "EntityDescription", self)

class luniferadoc_document_VaaclipseViewDocument(LuniferaDocDocument):

    def __init__(self, view: str, luniferadoc_document_VaaclipseViewDocument: "VaaclipseViewDescription" = None, LuniferaDocDocument: "luniferadoc_DocumentInclude" = None):
        self.view = view
        self.luniferadoc_document_VaaclipseViewDocument = luniferadoc_document_VaaclipseViewDocument
        
        pass
    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, view: str):
        self.__view = view


    @property
    def luniferadoc_document_VaaclipseViewDocument(self):
        return self.__luniferadoc_document_VaaclipseViewDocument

    @luniferadoc_document_VaaclipseViewDocument.setter
    def luniferadoc_document_VaaclipseViewDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_VaaclipseViewDocument__luniferadoc_document_VaaclipseViewDocument", None)
        self.__luniferadoc_document_VaaclipseViewDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VaaclipseViewDescription"):
                opp_val = getattr(old_value, "VaaclipseViewDescription", None)
                if opp_val == self:
                    setattr(old_value, "VaaclipseViewDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VaaclipseViewDescription"):
                opp_val = getattr(value, "VaaclipseViewDescription", None)
                setattr(value, "VaaclipseViewDescription", self)

class luniferadoc_document_BPMProcessDocument(LuniferaDocDocument):

    def __init__(self, process: str, luniferadoc_document_BPMProcessDocument: "BPMProcessDescription" = None, LuniferaDocDocument: "luniferadoc_DocumentInclude" = None):
        self.process = process
        self.luniferadoc_document_BPMProcessDocument = luniferadoc_document_BPMProcessDocument
        
        pass
    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, process: str):
        self.__process = process


    @property
    def luniferadoc_document_BPMProcessDocument(self):
        return self.__luniferadoc_document_BPMProcessDocument

    @luniferadoc_document_BPMProcessDocument.setter
    def luniferadoc_document_BPMProcessDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_document_BPMProcessDocument__luniferadoc_document_BPMProcessDocument", None)
        self.__luniferadoc_document_BPMProcessDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BPMProcessDescription"):
                opp_val = getattr(old_value, "BPMProcessDescription", None)
                if opp_val == self:
                    setattr(old_value, "BPMProcessDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BPMProcessDescription"):
                opp_val = getattr(value, "BPMProcessDescription", None)
                setattr(value, "BPMProcessDescription", self)

class luniferadoc_DocumentInclude:

    def __init__(self, varName: str, luniferadoc_DocumentInclude: "LuniferaDocDocument" = None):
        self.varName = varName
        self.luniferadoc_DocumentInclude = luniferadoc_DocumentInclude
        
        pass
    @property
    def varName(self):
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName


    @property
    def luniferadoc_DocumentInclude(self):
        return self.__luniferadoc_DocumentInclude

    @luniferadoc_DocumentInclude.setter
    def luniferadoc_DocumentInclude(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_DocumentInclude__luniferadoc_DocumentInclude", None)
        self.__luniferadoc_DocumentInclude = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LuniferaDocDocument"):
                opp_val = getattr(old_value, "LuniferaDocDocument", None)
                if opp_val == self:
                    setattr(old_value, "LuniferaDocDocument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LuniferaDocDocument"):
                opp_val = getattr(value, "LuniferaDocDocument", None)
                setattr(value, "LuniferaDocDocument", self)

class luniferadoc_NamedDocument(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class luniferadoc_richstring_RichStringOrderedList(RichStringMarkup):

    pass
class RichStringListElement:

    pass
class luniferadoc_richstring_RichStringList(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringSpan(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringListElement(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringTaskRef(RichStringMarkup):

    pass
class BPMProcessDocument:

    pass
class luniferadoc_richstring_RichStringProcessRef(RichStringMarkup):

    pass
class DTODocument:

    pass
class luniferadoc_richstring_RichStringDTORef(RichStringMarkup):

    pass
class EntityDocument:

    pass
class UIDocument:

    pass
class luniferadoc_richstring_RichStringUIRef(RichStringMarkup):

    pass
class VaaclipseViewDocument:

    pass
class luniferadoc_richstring_RichStringViewRef(RichStringMarkup):

    pass
class BPMHumanTaskDocument:

    pass
class RichStringTableData:

    pass
class luniferadoc_richstring_RichStringTableRow(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringEntityRef(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringStartProcess(RichStringMarkup):

    def __init__(self, processId: str):
        self.processId = processId
        
        pass
    @property
    def processId(self):
        return self.__processId

    @processId.setter
    def processId(self, processId: str):
        self.__processId = processId


class luniferadoc_richstring_RichStringOpenView(RichStringMarkup):

    def __init__(self, viewId: str):
        self.viewId = viewId
        
        pass
    @property
    def viewId(self):
        return self.__viewId

    @viewId.setter
    def viewId(self, viewId: str):
        self.__viewId = viewId


class luniferadoc_richstring_RichStringTableData(RichStringMarkup):

    pass
class luniferadoc_richstring_RichStringCode(RichStringMarkup):

    def __init__(self, lang: str, luniferadoc_richstring_RichStringCode: "richstring_luniferadoc_XExpression" = None):
        self.lang = lang
        self.luniferadoc_richstring_RichStringCode = luniferadoc_richstring_RichStringCode
        
        pass
    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang


    @property
    def luniferadoc_richstring_RichStringCode(self):
        return self.__luniferadoc_richstring_RichStringCode

    @luniferadoc_richstring_RichStringCode.setter
    def luniferadoc_richstring_RichStringCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_luniferadoc_richstring_RichStringCode__luniferadoc_richstring_RichStringCode", None)
        self.__luniferadoc_richstring_RichStringCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "richstring_luniferadoc_XExpression68"):
                opp_val = getattr(old_value, "richstring_luniferadoc_XExpression68", None)
                if opp_val == self:
                    setattr(old_value, "richstring_luniferadoc_XExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "richstring_luniferadoc_XExpression68"):
                opp_val = getattr(value, "richstring_luniferadoc_XExpression68", None)
                setattr(value, "richstring_luniferadoc_XExpression68", self)
