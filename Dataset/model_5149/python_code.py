from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TRules(Enum):
    none = "none"
    groups = "groups"
    rows = "rows"
    cols = "cols"
    all = "all"
class ValignType(Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"
    baseline = "baseline"
class Shape(Enum):
    rect = "rect"
    circle = "circle"
    poly = "poly"
    default = "default"
class AlignType(Enum):
    left = "left"
    center = "center"
    right = "right"
    justify = "justify"
    char = "char"
class StyleSheet(Enum):
    Requirement = "Requirement"
    Indent = "Indent"
    Note = "Note"
    NonNumbered = "NonNumbered"
    BackgroundAqua = "BackgroundAqua"
    BackgroundLime = "BackgroundLime"
    BackgroundPink = "BackgroundPink"
    BackgroundYellow = "BackgroundYellow"
class ImageKind(Enum):
    applicationPostscript = "applicationPostscript"
    applicationPdf = "applicationPdf"
    applicationPng = "applicationPng"
    applicationSvgXml = "applicationSvgXml"
    applicationJpeg = "applicationJpeg"
    imageGif = "imageGif"
class ObjectName(Enum):
    constructedElement = "constructedElement"
    footnote = "footnote"
    requirementRef = "requirementRef"
    externalSpecRef = "externalSpecRef"
    staticModelRef = "staticModelRef"
    subjectAreaRef = "subjectAreaRef"
    classRef = "classRef"
    stateRef = "stateRef"
    transitionRef = "transitionRef"
    attributeRef = "attributeRef"
    associationEndRef = "associationEndRef"
    triggerEventRef = "triggerEventRef"
    applicationRoleRef = "applicationRoleRef"
    interactionRef = "interactionRef"
    vocabularyModelRef = "vocabularyModelRef"
    conceptDomainRef = "conceptDomainRef"
    figureRef = "figureRef"
    tableRef = "tableRef"
    itemName = "itemName"
    annotationRef = "annotationRef"
    artifactGroupRef = "artifactGroupRef"
    packageRef = "packageRef"
    domainAnalysisModelRef = "domainAnalysisModelRef"
    domainInstanceExampleRef = "domainInstanceExampleRef"
    glossaryRef = "glossaryRef"
    glossaryTermRef = "glossaryTermRef"
    storyboardRef = "storyboardRef"
    freehandDocumentRef = "freehandDocumentRef"
    publicationRef = "publicationRef"
    datatypeModelRef = "datatypeModelRef"
    datatypeRef = "datatypeRef"
    propertyRef = "propertyRef"
    vocabularyCodeSystemRef = "vocabularyCodeSystemRef"
    vocabularyCodeRef = "vocabularyCodeRef"
    vocabularyValueSetRef = "vocabularyValueSetRef"
    testScenarioRef = "testScenarioRef"
    testCaseRef = "testCaseRef"
class MediaType(Enum):
    textPlain = "textPlain"
    textHtml = "textHtml"
    applicationPdf = "applicationPdf"
    textXml = "textXml"
    textRtf = "textRtf"
    applicationMsword = "applicationMsword"
    audioMpeg = "audioMpeg"
    imagePng = "imagePng"
    imageGif = "imageGif"
    imageJpeg = "imageJpeg"
    videoMpeg = "videoMpeg"
class ParamName(Enum):
    linkToEnd = "linkToEnd"
    withinClassName = "withinClassName"
    relationshipName = "relationshipName"
    attributeName = "attributeName"
    className = "className"
    supplierBindingArgumentDatatype = "supplierBindingArgumentDatatype"
    datatypeName = "datatypeName"
    conversionDatatype = "conversionDatatype"
    propertyName = "propertyName"
    termName = "termName"
    stateName = "stateName"
    stateTransitionName = "stateTransitionName"
    subjectAreaName = "subjectAreaName"
    codeSystemId = "codeSystemId"
    code = "code"
    constructType = "constructType"
    id = "id"
    item = "item"
    annotationKind = "annotationKind"
    root = "root"
    domain = "domain"
    realmNamespace = "realmNamespace"
    version = "version"
    artifact = "artifact"
    subArtifact = "subArtifact"
    name = "name"
    artifactName = "artifactName"
    group = "group"
class TFrame(Enum):
    void = "void"
    above = "above"
    below = "below"
    hsides = "hsides"
    lhs = "lhs"
    rhs = "rhs"
    vsides = "vsides"
    box = "box"
    border = "border"
class MifClassType(Enum):
    inserted = "inserted"
    deleted = "deleted"
    changed = "changed"


############################################
# Definition of Classes
############################################

class xhtml_Tbody:

    def __init__(self, align: str, char: str, charoff: str, class: str, lang: str, style: str, valign: str, xhtml_Tbody: "xhtml_Table" = None, xhtml_Tbody409: set["xhtml_Tr"] = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.lang = lang
        self.style = style
        self.valign = valign
        self.xhtml_Tbody = xhtml_Tbody
        self.xhtml_Tbody409 = xhtml_Tbody409 if xhtml_Tbody409 is not None else set()
        
    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def xhtml_Tbody(self):
        return self.__xhtml_Tbody

    @xhtml_Tbody.setter
    def xhtml_Tbody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tbody__xhtml_Tbody", None)
        self.__xhtml_Tbody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table405"):
                opp_val = getattr(old_value, "xhtml_Table405", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table405"):
                opp_val = getattr(value, "xhtml_Table405", None)
                if opp_val is None:
                    setattr(value, "xhtml_Table405", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tbody409(self):
        return self.__xhtml_Tbody409

    @xhtml_Tbody409.setter
    def xhtml_Tbody409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tbody__xhtml_Tbody409", None)
        self.__xhtml_Tbody409 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tr410"):
                    opp_val = getattr(item, "xhtml_Tr410", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tr410", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tr410"):
                    opp_val = getattr(item, "xhtml_Tr410", None)
                    
                    setattr(item, "xhtml_Tr410", self)
                    

class xhtml_Tfoot:

    def __init__(self, class: str, lang: str, style: str, valign: str, align: str, char: str, charoff: str, xhtml_Tfoot: "xhtml_Table" = None, xhtml_Tfoot412: set["xhtml_Tr"] = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.valign = valign
        self.align = align
        self.char = char
        self.charoff = charoff
        self.xhtml_Tfoot = xhtml_Tfoot
        self.xhtml_Tfoot412 = xhtml_Tfoot412 if xhtml_Tfoot412 is not None else set()
        
    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Tfoot(self):
        return self.__xhtml_Tfoot

    @xhtml_Tfoot.setter
    def xhtml_Tfoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tfoot__xhtml_Tfoot", None)
        self.__xhtml_Tfoot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table403"):
                opp_val = getattr(old_value, "xhtml_Table403", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Table403", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table403"):
                opp_val = getattr(value, "xhtml_Table403", None)
                setattr(value, "xhtml_Table403", self)

    @property
    def xhtml_Tfoot412(self):
        return self.__xhtml_Tfoot412

    @xhtml_Tfoot412.setter
    def xhtml_Tfoot412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tfoot__xhtml_Tfoot412", None)
        self.__xhtml_Tfoot412 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tr413"):
                    opp_val = getattr(item, "xhtml_Tr413", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tr413", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tr413"):
                    opp_val = getattr(item, "xhtml_Tr413", None)
                    
                    setattr(item, "xhtml_Tr413", self)
                    

class xhtml_Thead:

    def __init__(self, style: str, valign: str, align: str, char: str, charoff: str, class: str, lang: str, xhtml_Thead: "xhtml_Table" = None, xhtml_Thead415: set["xhtml_Tr"] = None):
        self.style = style
        self.valign = valign
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.lang = lang
        self.xhtml_Thead = xhtml_Thead
        self.xhtml_Thead415 = xhtml_Thead415 if xhtml_Thead415 is not None else set()
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def xhtml_Thead415(self):
        return self.__xhtml_Thead415

    @xhtml_Thead415.setter
    def xhtml_Thead415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Thead__xhtml_Thead415", None)
        self.__xhtml_Thead415 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tr416"):
                    opp_val = getattr(item, "xhtml_Tr416", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tr416", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tr416"):
                    opp_val = getattr(item, "xhtml_Tr416", None)
                    
                    setattr(item, "xhtml_Tr416", self)
                    

    @property
    def xhtml_Thead(self):
        return self.__xhtml_Thead

    @xhtml_Thead.setter
    def xhtml_Thead(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Thead__xhtml_Thead", None)
        self.__xhtml_Thead = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table401"):
                opp_val = getattr(old_value, "xhtml_Table401", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Table401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table401"):
                opp_val = getattr(value, "xhtml_Table401", None)
                setattr(value, "xhtml_Table401", self)

class xhtml_Tr:

    def __init__(self, group: str, valign: str, align: str, char: str, charoff: str, class: str, lang: str, style: str, xhtml_Tr: "xhtml_Table" = None, xhtml_Tr410: "xhtml_Tbody" = None, xhtml_Tr413: "xhtml_Tfoot" = None, xhtml_Tr418: set["xhtml_Th"] = None, xhtml_Tr416: "xhtml_Thead" = None, xhtml_Tr420: set["xhtml_Td"] = None):
        self.group = group
        self.valign = valign
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Tr = xhtml_Tr
        self.xhtml_Tr410 = xhtml_Tr410
        self.xhtml_Tr413 = xhtml_Tr413
        self.xhtml_Tr418 = xhtml_Tr418 if xhtml_Tr418 is not None else set()
        self.xhtml_Tr416 = xhtml_Tr416
        self.xhtml_Tr420 = xhtml_Tr420 if xhtml_Tr420 is not None else set()
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Tr(self):
        return self.__xhtml_Tr

    @xhtml_Tr.setter
    def xhtml_Tr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tr__xhtml_Tr", None)
        self.__xhtml_Tr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table407"):
                opp_val = getattr(old_value, "xhtml_Table407", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table407"):
                opp_val = getattr(value, "xhtml_Table407", None)
                if opp_val is None:
                    setattr(value, "xhtml_Table407", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tr410(self):
        return self.__xhtml_Tr410

    @xhtml_Tr410.setter
    def xhtml_Tr410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tr__xhtml_Tr410", None)
        self.__xhtml_Tr410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Tbody409"):
                opp_val = getattr(old_value, "xhtml_Tbody409", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Tbody409"):
                opp_val = getattr(value, "xhtml_Tbody409", None)
                if opp_val is None:
                    setattr(value, "xhtml_Tbody409", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tr418(self):
        return self.__xhtml_Tr418

    @xhtml_Tr418.setter
    def xhtml_Tr418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tr__xhtml_Tr418", None)
        self.__xhtml_Tr418 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Th"):
                    opp_val = getattr(item, "xhtml_Th", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Th", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Th"):
                    opp_val = getattr(item, "xhtml_Th", None)
                    
                    setattr(item, "xhtml_Th", self)
                    

    @property
    def xhtml_Tr420(self):
        return self.__xhtml_Tr420

    @xhtml_Tr420.setter
    def xhtml_Tr420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tr__xhtml_Tr420", None)
        self.__xhtml_Tr420 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Td"):
                    opp_val = getattr(item, "xhtml_Td", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Td", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Td"):
                    opp_val = getattr(item, "xhtml_Td", None)
                    
                    setattr(item, "xhtml_Td", self)
                    

    @property
    def xhtml_Tr413(self):
        return self.__xhtml_Tr413

    @xhtml_Tr413.setter
    def xhtml_Tr413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tr__xhtml_Tr413", None)
        self.__xhtml_Tr413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Tfoot412"):
                opp_val = getattr(old_value, "xhtml_Tfoot412", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Tfoot412"):
                opp_val = getattr(value, "xhtml_Tfoot412", None)
                if opp_val is None:
                    setattr(value, "xhtml_Tfoot412", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tr416(self):
        return self.__xhtml_Tr416

    @xhtml_Tr416.setter
    def xhtml_Tr416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tr__xhtml_Tr416", None)
        self.__xhtml_Tr416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Thead415"):
                opp_val = getattr(old_value, "xhtml_Thead415", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Thead415"):
                opp_val = getattr(value, "xhtml_Thead415", None)
                if opp_val is None:
                    setattr(value, "xhtml_Thead415", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_PreContent:

    def __init__(self, mixed: str, group: str, xhtml_PreContent: set["xhtml_A"] = None, xhtml_PreContent333: set["xhtml_Tt"] = None, xhtml_PreContent348: set["xhtml_Em"] = None, xhtml_PreContent351: set["xhtml_Strong"] = None, xhtml_PreContent354: set["xhtml_Dfn"] = None, xhtml_PreContent336: set["xhtml_I"] = None, xhtml_PreContent339: set["xhtml_B"] = None, xhtml_PreContent342: set["xhtml_Big"] = None, xhtml_PreContent345: set["xhtml_Small"] = None, xhtml_PreContent369: set["xhtml_Var"] = None, xhtml_PreContent372: set["xhtml_Cite"] = None, xhtml_PreContent375: set["xhtml_Abbr"] = None, xhtml_PreContent357: set["xhtml_Code"] = None, xhtml_PreContent360: set["xhtml_Q"] = None, xhtml_PreContent363: set["xhtml_Samp"] = None, xhtml_PreContent366: set["xhtml_Kbd"] = None, xhtml_PreContent384: set["xhtml_Sup"] = None, xhtml_PreContent387: set["xhtml_Br"] = None, xhtml_PreContent390: set["xhtml_Span"] = None, xhtml_PreContent378: set["xhtml_Acronym"] = None, xhtml_PreContent381: set["xhtml_Sub"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_PreContent = xhtml_PreContent if xhtml_PreContent is not None else set()
        self.xhtml_PreContent333 = xhtml_PreContent333 if xhtml_PreContent333 is not None else set()
        self.xhtml_PreContent348 = xhtml_PreContent348 if xhtml_PreContent348 is not None else set()
        self.xhtml_PreContent351 = xhtml_PreContent351 if xhtml_PreContent351 is not None else set()
        self.xhtml_PreContent354 = xhtml_PreContent354 if xhtml_PreContent354 is not None else set()
        self.xhtml_PreContent336 = xhtml_PreContent336 if xhtml_PreContent336 is not None else set()
        self.xhtml_PreContent339 = xhtml_PreContent339 if xhtml_PreContent339 is not None else set()
        self.xhtml_PreContent342 = xhtml_PreContent342 if xhtml_PreContent342 is not None else set()
        self.xhtml_PreContent345 = xhtml_PreContent345 if xhtml_PreContent345 is not None else set()
        self.xhtml_PreContent369 = xhtml_PreContent369 if xhtml_PreContent369 is not None else set()
        self.xhtml_PreContent372 = xhtml_PreContent372 if xhtml_PreContent372 is not None else set()
        self.xhtml_PreContent375 = xhtml_PreContent375 if xhtml_PreContent375 is not None else set()
        self.xhtml_PreContent357 = xhtml_PreContent357 if xhtml_PreContent357 is not None else set()
        self.xhtml_PreContent360 = xhtml_PreContent360 if xhtml_PreContent360 is not None else set()
        self.xhtml_PreContent363 = xhtml_PreContent363 if xhtml_PreContent363 is not None else set()
        self.xhtml_PreContent366 = xhtml_PreContent366 if xhtml_PreContent366 is not None else set()
        self.xhtml_PreContent384 = xhtml_PreContent384 if xhtml_PreContent384 is not None else set()
        self.xhtml_PreContent387 = xhtml_PreContent387 if xhtml_PreContent387 is not None else set()
        self.xhtml_PreContent390 = xhtml_PreContent390 if xhtml_PreContent390 is not None else set()
        self.xhtml_PreContent378 = xhtml_PreContent378 if xhtml_PreContent378 is not None else set()
        self.xhtml_PreContent381 = xhtml_PreContent381 if xhtml_PreContent381 is not None else set()
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xhtml_PreContent375(self):
        return self.__xhtml_PreContent375

    @xhtml_PreContent375.setter
    def xhtml_PreContent375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent375", None)
        self.__xhtml_PreContent375 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Abbr376"):
                    opp_val = getattr(item, "xhtml_Abbr376", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Abbr376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Abbr376"):
                    opp_val = getattr(item, "xhtml_Abbr376", None)
                    
                    setattr(item, "xhtml_Abbr376", self)
                    

    @property
    def xhtml_PreContent390(self):
        return self.__xhtml_PreContent390

    @xhtml_PreContent390.setter
    def xhtml_PreContent390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent390", None)
        self.__xhtml_PreContent390 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Span391"):
                    opp_val = getattr(item, "xhtml_Span391", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Span391", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Span391"):
                    opp_val = getattr(item, "xhtml_Span391", None)
                    
                    setattr(item, "xhtml_Span391", self)
                    

    @property
    def xhtml_PreContent378(self):
        return self.__xhtml_PreContent378

    @xhtml_PreContent378.setter
    def xhtml_PreContent378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent378", None)
        self.__xhtml_PreContent378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Acronym379"):
                    opp_val = getattr(item, "xhtml_Acronym379", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Acronym379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Acronym379"):
                    opp_val = getattr(item, "xhtml_Acronym379", None)
                    
                    setattr(item, "xhtml_Acronym379", self)
                    

    @property
    def xhtml_PreContent354(self):
        return self.__xhtml_PreContent354

    @xhtml_PreContent354.setter
    def xhtml_PreContent354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent354", None)
        self.__xhtml_PreContent354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dfn355"):
                    opp_val = getattr(item, "xhtml_Dfn355", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dfn355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dfn355"):
                    opp_val = getattr(item, "xhtml_Dfn355", None)
                    
                    setattr(item, "xhtml_Dfn355", self)
                    

    @property
    def xhtml_PreContent384(self):
        return self.__xhtml_PreContent384

    @xhtml_PreContent384.setter
    def xhtml_PreContent384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent384", None)
        self.__xhtml_PreContent384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sup385"):
                    opp_val = getattr(item, "xhtml_Sup385", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sup385", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sup385"):
                    opp_val = getattr(item, "xhtml_Sup385", None)
                    
                    setattr(item, "xhtml_Sup385", self)
                    

    @property
    def xhtml_PreContent387(self):
        return self.__xhtml_PreContent387

    @xhtml_PreContent387.setter
    def xhtml_PreContent387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent387", None)
        self.__xhtml_PreContent387 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Br388"):
                    opp_val = getattr(item, "xhtml_Br388", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Br388", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Br388"):
                    opp_val = getattr(item, "xhtml_Br388", None)
                    
                    setattr(item, "xhtml_Br388", self)
                    

    @property
    def xhtml_PreContent351(self):
        return self.__xhtml_PreContent351

    @xhtml_PreContent351.setter
    def xhtml_PreContent351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent351", None)
        self.__xhtml_PreContent351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Strong352"):
                    opp_val = getattr(item, "xhtml_Strong352", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Strong352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Strong352"):
                    opp_val = getattr(item, "xhtml_Strong352", None)
                    
                    setattr(item, "xhtml_Strong352", self)
                    

    @property
    def xhtml_PreContent348(self):
        return self.__xhtml_PreContent348

    @xhtml_PreContent348.setter
    def xhtml_PreContent348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent348", None)
        self.__xhtml_PreContent348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Em349"):
                    opp_val = getattr(item, "xhtml_Em349", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Em349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Em349"):
                    opp_val = getattr(item, "xhtml_Em349", None)
                    
                    setattr(item, "xhtml_Em349", self)
                    

    @property
    def xhtml_PreContent339(self):
        return self.__xhtml_PreContent339

    @xhtml_PreContent339.setter
    def xhtml_PreContent339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent339", None)
        self.__xhtml_PreContent339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_B340"):
                    opp_val = getattr(item, "xhtml_B340", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_B340", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_B340"):
                    opp_val = getattr(item, "xhtml_B340", None)
                    
                    setattr(item, "xhtml_B340", self)
                    

    @property
    def xhtml_PreContent360(self):
        return self.__xhtml_PreContent360

    @xhtml_PreContent360.setter
    def xhtml_PreContent360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent360", None)
        self.__xhtml_PreContent360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Q361"):
                    opp_val = getattr(item, "xhtml_Q361", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Q361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Q361"):
                    opp_val = getattr(item, "xhtml_Q361", None)
                    
                    setattr(item, "xhtml_Q361", self)
                    

    @property
    def xhtml_PreContent363(self):
        return self.__xhtml_PreContent363

    @xhtml_PreContent363.setter
    def xhtml_PreContent363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent363", None)
        self.__xhtml_PreContent363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Samp364"):
                    opp_val = getattr(item, "xhtml_Samp364", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Samp364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Samp364"):
                    opp_val = getattr(item, "xhtml_Samp364", None)
                    
                    setattr(item, "xhtml_Samp364", self)
                    

    @property
    def xhtml_PreContent333(self):
        return self.__xhtml_PreContent333

    @xhtml_PreContent333.setter
    def xhtml_PreContent333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent333", None)
        self.__xhtml_PreContent333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tt334"):
                    opp_val = getattr(item, "xhtml_Tt334", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tt334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tt334"):
                    opp_val = getattr(item, "xhtml_Tt334", None)
                    
                    setattr(item, "xhtml_Tt334", self)
                    

    @property
    def xhtml_PreContent342(self):
        return self.__xhtml_PreContent342

    @xhtml_PreContent342.setter
    def xhtml_PreContent342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent342", None)
        self.__xhtml_PreContent342 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Big343"):
                    opp_val = getattr(item, "xhtml_Big343", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Big343", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Big343"):
                    opp_val = getattr(item, "xhtml_Big343", None)
                    
                    setattr(item, "xhtml_Big343", self)
                    

    @property
    def xhtml_PreContent(self):
        return self.__xhtml_PreContent

    @xhtml_PreContent.setter
    def xhtml_PreContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent", None)
        self.__xhtml_PreContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_A331"):
                    opp_val = getattr(item, "xhtml_A331", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_A331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_A331"):
                    opp_val = getattr(item, "xhtml_A331", None)
                    
                    setattr(item, "xhtml_A331", self)
                    

    @property
    def xhtml_PreContent369(self):
        return self.__xhtml_PreContent369

    @xhtml_PreContent369.setter
    def xhtml_PreContent369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent369", None)
        self.__xhtml_PreContent369 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Var370"):
                    opp_val = getattr(item, "xhtml_Var370", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Var370", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Var370"):
                    opp_val = getattr(item, "xhtml_Var370", None)
                    
                    setattr(item, "xhtml_Var370", self)
                    

    @property
    def xhtml_PreContent366(self):
        return self.__xhtml_PreContent366

    @xhtml_PreContent366.setter
    def xhtml_PreContent366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent366", None)
        self.__xhtml_PreContent366 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Kbd367"):
                    opp_val = getattr(item, "xhtml_Kbd367", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Kbd367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Kbd367"):
                    opp_val = getattr(item, "xhtml_Kbd367", None)
                    
                    setattr(item, "xhtml_Kbd367", self)
                    

    @property
    def xhtml_PreContent357(self):
        return self.__xhtml_PreContent357

    @xhtml_PreContent357.setter
    def xhtml_PreContent357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent357", None)
        self.__xhtml_PreContent357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Code358"):
                    opp_val = getattr(item, "xhtml_Code358", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Code358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Code358"):
                    opp_val = getattr(item, "xhtml_Code358", None)
                    
                    setattr(item, "xhtml_Code358", self)
                    

    @property
    def xhtml_PreContent372(self):
        return self.__xhtml_PreContent372

    @xhtml_PreContent372.setter
    def xhtml_PreContent372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent372", None)
        self.__xhtml_PreContent372 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Cite373"):
                    opp_val = getattr(item, "xhtml_Cite373", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Cite373", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Cite373"):
                    opp_val = getattr(item, "xhtml_Cite373", None)
                    
                    setattr(item, "xhtml_Cite373", self)
                    

    @property
    def xhtml_PreContent336(self):
        return self.__xhtml_PreContent336

    @xhtml_PreContent336.setter
    def xhtml_PreContent336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent336", None)
        self.__xhtml_PreContent336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_I337"):
                    opp_val = getattr(item, "xhtml_I337", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_I337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_I337"):
                    opp_val = getattr(item, "xhtml_I337", None)
                    
                    setattr(item, "xhtml_I337", self)
                    

    @property
    def xhtml_PreContent381(self):
        return self.__xhtml_PreContent381

    @xhtml_PreContent381.setter
    def xhtml_PreContent381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent381", None)
        self.__xhtml_PreContent381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sub382"):
                    opp_val = getattr(item, "xhtml_Sub382", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sub382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sub382"):
                    opp_val = getattr(item, "xhtml_Sub382", None)
                    
                    setattr(item, "xhtml_Sub382", self)
                    

    @property
    def xhtml_PreContent345(self):
        return self.__xhtml_PreContent345

    @xhtml_PreContent345.setter
    def xhtml_PreContent345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_PreContent__xhtml_PreContent345", None)
        self.__xhtml_PreContent345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Small346"):
                    opp_val = getattr(item, "xhtml_Small346", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Small346", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Small346"):
                    opp_val = getattr(item, "xhtml_Small346", None)
                    
                    setattr(item, "xhtml_Small346", self)
                    

class PreContent:

    pass
class xhtml_Param:

    def __init__(self, name: str, value: str, xhtml_Param: "xhtml_Object" = None):
        self.name = name
        self.value = value
        self.xhtml_Param = xhtml_Param
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xhtml_Param(self):
        return self.__xhtml_Param

    @xhtml_Param.setter
    def xhtml_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Param__xhtml_Param", None)
        self.__xhtml_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object231"):
                opp_val = getattr(old_value, "xhtml_Object231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object231"):
                opp_val = getattr(value, "xhtml_Object231", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Inline:

    def __init__(self, mixed: str, inline: str, xhtml_Inline174: set["xhtml_Img"] = None, xhtml_Inline177: set["xhtml_Tt"] = None, xhtml_Inline180: set["xhtml_I"] = None, xhtml_Inline: set["xhtml_A"] = None, xhtml_Inline165: set["xhtml_Br"] = None, xhtml_Inline168: set["xhtml_Span"] = None, xhtml_Inline171: set["xhtml_Object"] = None, xhtml_Inline198: set["xhtml_Dfn"] = None, xhtml_Inline201: set["xhtml_Code"] = None, xhtml_Inline204: set["xhtml_Q"] = None, xhtml_Inline183: set["xhtml_B"] = None, xhtml_Inline186: set["xhtml_Big"] = None, xhtml_Inline189: set["xhtml_Small"] = None, xhtml_Inline192: set["xhtml_Em"] = None, xhtml_Inline195: set["xhtml_Strong"] = None, xhtml_Inline219: set["xhtml_Abbr"] = None, xhtml_Inline222: set["xhtml_Acronym"] = None, xhtml_Inline225: set["xhtml_Sub"] = None, xhtml_Inline228: set["xhtml_Sup"] = None, xhtml_Inline207: set["xhtml_Samp"] = None, xhtml_Inline210: set["xhtml_Kbd"] = None, xhtml_Inline213: set["xhtml_Var"] = None, xhtml_Inline216: set["xhtml_Cite"] = None):
        self.mixed = mixed
        self.inline = inline
        self.xhtml_Inline174 = xhtml_Inline174 if xhtml_Inline174 is not None else set()
        self.xhtml_Inline177 = xhtml_Inline177 if xhtml_Inline177 is not None else set()
        self.xhtml_Inline180 = xhtml_Inline180 if xhtml_Inline180 is not None else set()
        self.xhtml_Inline = xhtml_Inline if xhtml_Inline is not None else set()
        self.xhtml_Inline165 = xhtml_Inline165 if xhtml_Inline165 is not None else set()
        self.xhtml_Inline168 = xhtml_Inline168 if xhtml_Inline168 is not None else set()
        self.xhtml_Inline171 = xhtml_Inline171 if xhtml_Inline171 is not None else set()
        self.xhtml_Inline198 = xhtml_Inline198 if xhtml_Inline198 is not None else set()
        self.xhtml_Inline201 = xhtml_Inline201 if xhtml_Inline201 is not None else set()
        self.xhtml_Inline204 = xhtml_Inline204 if xhtml_Inline204 is not None else set()
        self.xhtml_Inline183 = xhtml_Inline183 if xhtml_Inline183 is not None else set()
        self.xhtml_Inline186 = xhtml_Inline186 if xhtml_Inline186 is not None else set()
        self.xhtml_Inline189 = xhtml_Inline189 if xhtml_Inline189 is not None else set()
        self.xhtml_Inline192 = xhtml_Inline192 if xhtml_Inline192 is not None else set()
        self.xhtml_Inline195 = xhtml_Inline195 if xhtml_Inline195 is not None else set()
        self.xhtml_Inline219 = xhtml_Inline219 if xhtml_Inline219 is not None else set()
        self.xhtml_Inline222 = xhtml_Inline222 if xhtml_Inline222 is not None else set()
        self.xhtml_Inline225 = xhtml_Inline225 if xhtml_Inline225 is not None else set()
        self.xhtml_Inline228 = xhtml_Inline228 if xhtml_Inline228 is not None else set()
        self.xhtml_Inline207 = xhtml_Inline207 if xhtml_Inline207 is not None else set()
        self.xhtml_Inline210 = xhtml_Inline210 if xhtml_Inline210 is not None else set()
        self.xhtml_Inline213 = xhtml_Inline213 if xhtml_Inline213 is not None else set()
        self.xhtml_Inline216 = xhtml_Inline216 if xhtml_Inline216 is not None else set()
        
    @property
    def inline(self) -> str:
        return self.__inline

    @inline.setter
    def inline(self, inline: str):
        self.__inline = inline

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def xhtml_Inline201(self):
        return self.__xhtml_Inline201

    @xhtml_Inline201.setter
    def xhtml_Inline201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline201", None)
        self.__xhtml_Inline201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Code202"):
                    opp_val = getattr(item, "xhtml_Code202", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Code202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Code202"):
                    opp_val = getattr(item, "xhtml_Code202", None)
                    
                    setattr(item, "xhtml_Code202", self)
                    

    @property
    def xhtml_Inline198(self):
        return self.__xhtml_Inline198

    @xhtml_Inline198.setter
    def xhtml_Inline198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline198", None)
        self.__xhtml_Inline198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dfn199"):
                    opp_val = getattr(item, "xhtml_Dfn199", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dfn199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dfn199"):
                    opp_val = getattr(item, "xhtml_Dfn199", None)
                    
                    setattr(item, "xhtml_Dfn199", self)
                    

    @property
    def xhtml_Inline213(self):
        return self.__xhtml_Inline213

    @xhtml_Inline213.setter
    def xhtml_Inline213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline213", None)
        self.__xhtml_Inline213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Var214"):
                    opp_val = getattr(item, "xhtml_Var214", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Var214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Var214"):
                    opp_val = getattr(item, "xhtml_Var214", None)
                    
                    setattr(item, "xhtml_Var214", self)
                    

    @property
    def xhtml_Inline186(self):
        return self.__xhtml_Inline186

    @xhtml_Inline186.setter
    def xhtml_Inline186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline186", None)
        self.__xhtml_Inline186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Big187"):
                    opp_val = getattr(item, "xhtml_Big187", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Big187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Big187"):
                    opp_val = getattr(item, "xhtml_Big187", None)
                    
                    setattr(item, "xhtml_Big187", self)
                    

    @property
    def xhtml_Inline(self):
        return self.__xhtml_Inline

    @xhtml_Inline.setter
    def xhtml_Inline(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline", None)
        self.__xhtml_Inline = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_A163"):
                    opp_val = getattr(item, "xhtml_A163", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_A163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_A163"):
                    opp_val = getattr(item, "xhtml_A163", None)
                    
                    setattr(item, "xhtml_A163", self)
                    

    @property
    def xhtml_Inline189(self):
        return self.__xhtml_Inline189

    @xhtml_Inline189.setter
    def xhtml_Inline189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline189", None)
        self.__xhtml_Inline189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Small190"):
                    opp_val = getattr(item, "xhtml_Small190", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Small190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Small190"):
                    opp_val = getattr(item, "xhtml_Small190", None)
                    
                    setattr(item, "xhtml_Small190", self)
                    

    @property
    def xhtml_Inline222(self):
        return self.__xhtml_Inline222

    @xhtml_Inline222.setter
    def xhtml_Inline222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline222", None)
        self.__xhtml_Inline222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Acronym223"):
                    opp_val = getattr(item, "xhtml_Acronym223", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Acronym223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Acronym223"):
                    opp_val = getattr(item, "xhtml_Acronym223", None)
                    
                    setattr(item, "xhtml_Acronym223", self)
                    

    @property
    def xhtml_Inline225(self):
        return self.__xhtml_Inline225

    @xhtml_Inline225.setter
    def xhtml_Inline225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline225", None)
        self.__xhtml_Inline225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sub226"):
                    opp_val = getattr(item, "xhtml_Sub226", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sub226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sub226"):
                    opp_val = getattr(item, "xhtml_Sub226", None)
                    
                    setattr(item, "xhtml_Sub226", self)
                    

    @property
    def xhtml_Inline174(self):
        return self.__xhtml_Inline174

    @xhtml_Inline174.setter
    def xhtml_Inline174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline174", None)
        self.__xhtml_Inline174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Img175"):
                    opp_val = getattr(item, "xhtml_Img175", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Img175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Img175"):
                    opp_val = getattr(item, "xhtml_Img175", None)
                    
                    setattr(item, "xhtml_Img175", self)
                    

    @property
    def xhtml_Inline195(self):
        return self.__xhtml_Inline195

    @xhtml_Inline195.setter
    def xhtml_Inline195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline195", None)
        self.__xhtml_Inline195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Strong196"):
                    opp_val = getattr(item, "xhtml_Strong196", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Strong196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Strong196"):
                    opp_val = getattr(item, "xhtml_Strong196", None)
                    
                    setattr(item, "xhtml_Strong196", self)
                    

    @property
    def xhtml_Inline183(self):
        return self.__xhtml_Inline183

    @xhtml_Inline183.setter
    def xhtml_Inline183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline183", None)
        self.__xhtml_Inline183 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_B184"):
                    opp_val = getattr(item, "xhtml_B184", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_B184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_B184"):
                    opp_val = getattr(item, "xhtml_B184", None)
                    
                    setattr(item, "xhtml_B184", self)
                    

    @property
    def xhtml_Inline168(self):
        return self.__xhtml_Inline168

    @xhtml_Inline168.setter
    def xhtml_Inline168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline168", None)
        self.__xhtml_Inline168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Span169"):
                    opp_val = getattr(item, "xhtml_Span169", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Span169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Span169"):
                    opp_val = getattr(item, "xhtml_Span169", None)
                    
                    setattr(item, "xhtml_Span169", self)
                    

    @property
    def xhtml_Inline210(self):
        return self.__xhtml_Inline210

    @xhtml_Inline210.setter
    def xhtml_Inline210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline210", None)
        self.__xhtml_Inline210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Kbd211"):
                    opp_val = getattr(item, "xhtml_Kbd211", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Kbd211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Kbd211"):
                    opp_val = getattr(item, "xhtml_Kbd211", None)
                    
                    setattr(item, "xhtml_Kbd211", self)
                    

    @property
    def xhtml_Inline165(self):
        return self.__xhtml_Inline165

    @xhtml_Inline165.setter
    def xhtml_Inline165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline165", None)
        self.__xhtml_Inline165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Br166"):
                    opp_val = getattr(item, "xhtml_Br166", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Br166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Br166"):
                    opp_val = getattr(item, "xhtml_Br166", None)
                    
                    setattr(item, "xhtml_Br166", self)
                    

    @property
    def xhtml_Inline216(self):
        return self.__xhtml_Inline216

    @xhtml_Inline216.setter
    def xhtml_Inline216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline216", None)
        self.__xhtml_Inline216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Cite217"):
                    opp_val = getattr(item, "xhtml_Cite217", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Cite217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Cite217"):
                    opp_val = getattr(item, "xhtml_Cite217", None)
                    
                    setattr(item, "xhtml_Cite217", self)
                    

    @property
    def xhtml_Inline192(self):
        return self.__xhtml_Inline192

    @xhtml_Inline192.setter
    def xhtml_Inline192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline192", None)
        self.__xhtml_Inline192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Em193"):
                    opp_val = getattr(item, "xhtml_Em193", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Em193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Em193"):
                    opp_val = getattr(item, "xhtml_Em193", None)
                    
                    setattr(item, "xhtml_Em193", self)
                    

    @property
    def xhtml_Inline228(self):
        return self.__xhtml_Inline228

    @xhtml_Inline228.setter
    def xhtml_Inline228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline228", None)
        self.__xhtml_Inline228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sup229"):
                    opp_val = getattr(item, "xhtml_Sup229", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sup229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sup229"):
                    opp_val = getattr(item, "xhtml_Sup229", None)
                    
                    setattr(item, "xhtml_Sup229", self)
                    

    @property
    def xhtml_Inline171(self):
        return self.__xhtml_Inline171

    @xhtml_Inline171.setter
    def xhtml_Inline171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline171", None)
        self.__xhtml_Inline171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Object172"):
                    opp_val = getattr(item, "xhtml_Object172", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Object172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Object172"):
                    opp_val = getattr(item, "xhtml_Object172", None)
                    
                    setattr(item, "xhtml_Object172", self)
                    

    @property
    def xhtml_Inline180(self):
        return self.__xhtml_Inline180

    @xhtml_Inline180.setter
    def xhtml_Inline180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline180", None)
        self.__xhtml_Inline180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_I181"):
                    opp_val = getattr(item, "xhtml_I181", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_I181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_I181"):
                    opp_val = getattr(item, "xhtml_I181", None)
                    
                    setattr(item, "xhtml_I181", self)
                    

    @property
    def xhtml_Inline204(self):
        return self.__xhtml_Inline204

    @xhtml_Inline204.setter
    def xhtml_Inline204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline204", None)
        self.__xhtml_Inline204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Q205"):
                    opp_val = getattr(item, "xhtml_Q205", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Q205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Q205"):
                    opp_val = getattr(item, "xhtml_Q205", None)
                    
                    setattr(item, "xhtml_Q205", self)
                    

    @property
    def xhtml_Inline207(self):
        return self.__xhtml_Inline207

    @xhtml_Inline207.setter
    def xhtml_Inline207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline207", None)
        self.__xhtml_Inline207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Samp208"):
                    opp_val = getattr(item, "xhtml_Samp208", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Samp208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Samp208"):
                    opp_val = getattr(item, "xhtml_Samp208", None)
                    
                    setattr(item, "xhtml_Samp208", self)
                    

    @property
    def xhtml_Inline177(self):
        return self.__xhtml_Inline177

    @xhtml_Inline177.setter
    def xhtml_Inline177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline177", None)
        self.__xhtml_Inline177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tt178"):
                    opp_val = getattr(item, "xhtml_Tt178", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tt178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tt178"):
                    opp_val = getattr(item, "xhtml_Tt178", None)
                    
                    setattr(item, "xhtml_Tt178", self)
                    

    @property
    def xhtml_Inline219(self):
        return self.__xhtml_Inline219

    @xhtml_Inline219.setter
    def xhtml_Inline219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Inline__xhtml_Inline219", None)
        self.__xhtml_Inline219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Abbr220"):
                    opp_val = getattr(item, "xhtml_Abbr220", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Abbr220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Abbr220"):
                    opp_val = getattr(item, "xhtml_Abbr220", None)
                    
                    setattr(item, "xhtml_Abbr220", self)
                    

class xhtml_Flow:

    def __init__(self, mixed: str, group: str, xhtml_Flow: set["xhtml_P"] = None, xhtml_Flow68: set["xhtml_Div"] = None, xhtml_Flow71: set["xhtml_Ul"] = None, xhtml_Flow74: set["xhtml_Ol"] = None, xhtml_Flow77: set["xhtml_Dl"] = None, xhtml_Flow80: set["xhtml_Pre"] = None, xhtml_Flow83: set["xhtml_Hr"] = None, xhtml_Flow86: set["xhtml_Blockquote"] = None, xhtml_Flow92: set["xhtml_A"] = None, xhtml_Flow94: set["xhtml_Br"] = None, xhtml_Flow97: set["xhtml_Span"] = None, xhtml_Flow100: set["xhtml_Object"] = None, xhtml_Flow103: set["xhtml_Img"] = None, xhtml_Flow106: set["xhtml_Tt"] = None, xhtml_Flow89: set["xhtml_Table"] = None, xhtml_Flow112: set["xhtml_B"] = None, xhtml_Flow115: set["xhtml_Big"] = None, xhtml_Flow118: set["xhtml_Small"] = None, xhtml_Flow133: set["xhtml_Q"] = None, xhtml_Flow136: set["xhtml_Samp"] = None, xhtml_Flow139: set["xhtml_Kbd"] = None, xhtml_Flow109: set["xhtml_I"] = None, xhtml_Flow121: set["xhtml_Em"] = None, xhtml_Flow124: set["xhtml_Strong"] = None, xhtml_Flow127: set["xhtml_Dfn"] = None, xhtml_Flow130: set["xhtml_Code"] = None, xhtml_Flow154: set["xhtml_Sub"] = None, xhtml_Flow157: set["xhtml_Sup"] = None, xhtml_Flow142: set["xhtml_Var"] = None, xhtml_Flow145: set["xhtml_Cite"] = None, xhtml_Flow148: set["xhtml_Abbr"] = None, xhtml_Flow151: set["xhtml_Acronym"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_Flow = xhtml_Flow if xhtml_Flow is not None else set()
        self.xhtml_Flow68 = xhtml_Flow68 if xhtml_Flow68 is not None else set()
        self.xhtml_Flow71 = xhtml_Flow71 if xhtml_Flow71 is not None else set()
        self.xhtml_Flow74 = xhtml_Flow74 if xhtml_Flow74 is not None else set()
        self.xhtml_Flow77 = xhtml_Flow77 if xhtml_Flow77 is not None else set()
        self.xhtml_Flow80 = xhtml_Flow80 if xhtml_Flow80 is not None else set()
        self.xhtml_Flow83 = xhtml_Flow83 if xhtml_Flow83 is not None else set()
        self.xhtml_Flow86 = xhtml_Flow86 if xhtml_Flow86 is not None else set()
        self.xhtml_Flow92 = xhtml_Flow92 if xhtml_Flow92 is not None else set()
        self.xhtml_Flow94 = xhtml_Flow94 if xhtml_Flow94 is not None else set()
        self.xhtml_Flow97 = xhtml_Flow97 if xhtml_Flow97 is not None else set()
        self.xhtml_Flow100 = xhtml_Flow100 if xhtml_Flow100 is not None else set()
        self.xhtml_Flow103 = xhtml_Flow103 if xhtml_Flow103 is not None else set()
        self.xhtml_Flow106 = xhtml_Flow106 if xhtml_Flow106 is not None else set()
        self.xhtml_Flow89 = xhtml_Flow89 if xhtml_Flow89 is not None else set()
        self.xhtml_Flow112 = xhtml_Flow112 if xhtml_Flow112 is not None else set()
        self.xhtml_Flow115 = xhtml_Flow115 if xhtml_Flow115 is not None else set()
        self.xhtml_Flow118 = xhtml_Flow118 if xhtml_Flow118 is not None else set()
        self.xhtml_Flow133 = xhtml_Flow133 if xhtml_Flow133 is not None else set()
        self.xhtml_Flow136 = xhtml_Flow136 if xhtml_Flow136 is not None else set()
        self.xhtml_Flow139 = xhtml_Flow139 if xhtml_Flow139 is not None else set()
        self.xhtml_Flow109 = xhtml_Flow109 if xhtml_Flow109 is not None else set()
        self.xhtml_Flow121 = xhtml_Flow121 if xhtml_Flow121 is not None else set()
        self.xhtml_Flow124 = xhtml_Flow124 if xhtml_Flow124 is not None else set()
        self.xhtml_Flow127 = xhtml_Flow127 if xhtml_Flow127 is not None else set()
        self.xhtml_Flow130 = xhtml_Flow130 if xhtml_Flow130 is not None else set()
        self.xhtml_Flow154 = xhtml_Flow154 if xhtml_Flow154 is not None else set()
        self.xhtml_Flow157 = xhtml_Flow157 if xhtml_Flow157 is not None else set()
        self.xhtml_Flow142 = xhtml_Flow142 if xhtml_Flow142 is not None else set()
        self.xhtml_Flow145 = xhtml_Flow145 if xhtml_Flow145 is not None else set()
        self.xhtml_Flow148 = xhtml_Flow148 if xhtml_Flow148 is not None else set()
        self.xhtml_Flow151 = xhtml_Flow151 if xhtml_Flow151 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_Flow86(self):
        return self.__xhtml_Flow86

    @xhtml_Flow86.setter
    def xhtml_Flow86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow86", None)
        self.__xhtml_Flow86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Blockquote87"):
                    opp_val = getattr(item, "xhtml_Blockquote87", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Blockquote87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Blockquote87"):
                    opp_val = getattr(item, "xhtml_Blockquote87", None)
                    
                    setattr(item, "xhtml_Blockquote87", self)
                    

    @property
    def xhtml_Flow139(self):
        return self.__xhtml_Flow139

    @xhtml_Flow139.setter
    def xhtml_Flow139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow139", None)
        self.__xhtml_Flow139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Kbd140"):
                    opp_val = getattr(item, "xhtml_Kbd140", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Kbd140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Kbd140"):
                    opp_val = getattr(item, "xhtml_Kbd140", None)
                    
                    setattr(item, "xhtml_Kbd140", self)
                    

    @property
    def xhtml_Flow80(self):
        return self.__xhtml_Flow80

    @xhtml_Flow80.setter
    def xhtml_Flow80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow80", None)
        self.__xhtml_Flow80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Pre81"):
                    opp_val = getattr(item, "xhtml_Pre81", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Pre81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Pre81"):
                    opp_val = getattr(item, "xhtml_Pre81", None)
                    
                    setattr(item, "xhtml_Pre81", self)
                    

    @property
    def xhtml_Flow(self):
        return self.__xhtml_Flow

    @xhtml_Flow.setter
    def xhtml_Flow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow", None)
        self.__xhtml_Flow = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_P66"):
                    opp_val = getattr(item, "xhtml_P66", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_P66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_P66"):
                    opp_val = getattr(item, "xhtml_P66", None)
                    
                    setattr(item, "xhtml_P66", self)
                    

    @property
    def xhtml_Flow136(self):
        return self.__xhtml_Flow136

    @xhtml_Flow136.setter
    def xhtml_Flow136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow136", None)
        self.__xhtml_Flow136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Samp137"):
                    opp_val = getattr(item, "xhtml_Samp137", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Samp137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Samp137"):
                    opp_val = getattr(item, "xhtml_Samp137", None)
                    
                    setattr(item, "xhtml_Samp137", self)
                    

    @property
    def xhtml_Flow121(self):
        return self.__xhtml_Flow121

    @xhtml_Flow121.setter
    def xhtml_Flow121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow121", None)
        self.__xhtml_Flow121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Em122"):
                    opp_val = getattr(item, "xhtml_Em122", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Em122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Em122"):
                    opp_val = getattr(item, "xhtml_Em122", None)
                    
                    setattr(item, "xhtml_Em122", self)
                    

    @property
    def xhtml_Flow133(self):
        return self.__xhtml_Flow133

    @xhtml_Flow133.setter
    def xhtml_Flow133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow133", None)
        self.__xhtml_Flow133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Q134"):
                    opp_val = getattr(item, "xhtml_Q134", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Q134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Q134"):
                    opp_val = getattr(item, "xhtml_Q134", None)
                    
                    setattr(item, "xhtml_Q134", self)
                    

    @property
    def xhtml_Flow68(self):
        return self.__xhtml_Flow68

    @xhtml_Flow68.setter
    def xhtml_Flow68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow68", None)
        self.__xhtml_Flow68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Div69"):
                    opp_val = getattr(item, "xhtml_Div69", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Div69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Div69"):
                    opp_val = getattr(item, "xhtml_Div69", None)
                    
                    setattr(item, "xhtml_Div69", self)
                    

    @property
    def xhtml_Flow92(self):
        return self.__xhtml_Flow92

    @xhtml_Flow92.setter
    def xhtml_Flow92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow92", None)
        self.__xhtml_Flow92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_A"):
                    opp_val = getattr(item, "xhtml_A", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_A"):
                    opp_val = getattr(item, "xhtml_A", None)
                    
                    setattr(item, "xhtml_A", self)
                    

    @property
    def xhtml_Flow151(self):
        return self.__xhtml_Flow151

    @xhtml_Flow151.setter
    def xhtml_Flow151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow151", None)
        self.__xhtml_Flow151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Acronym152"):
                    opp_val = getattr(item, "xhtml_Acronym152", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Acronym152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Acronym152"):
                    opp_val = getattr(item, "xhtml_Acronym152", None)
                    
                    setattr(item, "xhtml_Acronym152", self)
                    

    @property
    def xhtml_Flow89(self):
        return self.__xhtml_Flow89

    @xhtml_Flow89.setter
    def xhtml_Flow89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow89", None)
        self.__xhtml_Flow89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Table90"):
                    opp_val = getattr(item, "xhtml_Table90", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Table90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Table90"):
                    opp_val = getattr(item, "xhtml_Table90", None)
                    
                    setattr(item, "xhtml_Table90", self)
                    

    @property
    def xhtml_Flow100(self):
        return self.__xhtml_Flow100

    @xhtml_Flow100.setter
    def xhtml_Flow100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow100", None)
        self.__xhtml_Flow100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Object101"):
                    opp_val = getattr(item, "xhtml_Object101", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Object101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Object101"):
                    opp_val = getattr(item, "xhtml_Object101", None)
                    
                    setattr(item, "xhtml_Object101", self)
                    

    @property
    def xhtml_Flow118(self):
        return self.__xhtml_Flow118

    @xhtml_Flow118.setter
    def xhtml_Flow118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow118", None)
        self.__xhtml_Flow118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Small119"):
                    opp_val = getattr(item, "xhtml_Small119", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Small119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Small119"):
                    opp_val = getattr(item, "xhtml_Small119", None)
                    
                    setattr(item, "xhtml_Small119", self)
                    

    @property
    def xhtml_Flow142(self):
        return self.__xhtml_Flow142

    @xhtml_Flow142.setter
    def xhtml_Flow142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow142", None)
        self.__xhtml_Flow142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Var143"):
                    opp_val = getattr(item, "xhtml_Var143", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Var143", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Var143"):
                    opp_val = getattr(item, "xhtml_Var143", None)
                    
                    setattr(item, "xhtml_Var143", self)
                    

    @property
    def xhtml_Flow94(self):
        return self.__xhtml_Flow94

    @xhtml_Flow94.setter
    def xhtml_Flow94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow94", None)
        self.__xhtml_Flow94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Br95"):
                    opp_val = getattr(item, "xhtml_Br95", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Br95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Br95"):
                    opp_val = getattr(item, "xhtml_Br95", None)
                    
                    setattr(item, "xhtml_Br95", self)
                    

    @property
    def xhtml_Flow148(self):
        return self.__xhtml_Flow148

    @xhtml_Flow148.setter
    def xhtml_Flow148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow148", None)
        self.__xhtml_Flow148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Abbr149"):
                    opp_val = getattr(item, "xhtml_Abbr149", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Abbr149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Abbr149"):
                    opp_val = getattr(item, "xhtml_Abbr149", None)
                    
                    setattr(item, "xhtml_Abbr149", self)
                    

    @property
    def xhtml_Flow77(self):
        return self.__xhtml_Flow77

    @xhtml_Flow77.setter
    def xhtml_Flow77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow77", None)
        self.__xhtml_Flow77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dl78"):
                    opp_val = getattr(item, "xhtml_Dl78", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dl78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dl78"):
                    opp_val = getattr(item, "xhtml_Dl78", None)
                    
                    setattr(item, "xhtml_Dl78", self)
                    

    @property
    def xhtml_Flow109(self):
        return self.__xhtml_Flow109

    @xhtml_Flow109.setter
    def xhtml_Flow109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow109", None)
        self.__xhtml_Flow109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_I110"):
                    opp_val = getattr(item, "xhtml_I110", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_I110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_I110"):
                    opp_val = getattr(item, "xhtml_I110", None)
                    
                    setattr(item, "xhtml_I110", self)
                    

    @property
    def xhtml_Flow130(self):
        return self.__xhtml_Flow130

    @xhtml_Flow130.setter
    def xhtml_Flow130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow130", None)
        self.__xhtml_Flow130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Code131"):
                    opp_val = getattr(item, "xhtml_Code131", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Code131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Code131"):
                    opp_val = getattr(item, "xhtml_Code131", None)
                    
                    setattr(item, "xhtml_Code131", self)
                    

    @property
    def xhtml_Flow97(self):
        return self.__xhtml_Flow97

    @xhtml_Flow97.setter
    def xhtml_Flow97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow97", None)
        self.__xhtml_Flow97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Span98"):
                    opp_val = getattr(item, "xhtml_Span98", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Span98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Span98"):
                    opp_val = getattr(item, "xhtml_Span98", None)
                    
                    setattr(item, "xhtml_Span98", self)
                    

    @property
    def xhtml_Flow83(self):
        return self.__xhtml_Flow83

    @xhtml_Flow83.setter
    def xhtml_Flow83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow83", None)
        self.__xhtml_Flow83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Hr84"):
                    opp_val = getattr(item, "xhtml_Hr84", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Hr84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Hr84"):
                    opp_val = getattr(item, "xhtml_Hr84", None)
                    
                    setattr(item, "xhtml_Hr84", self)
                    

    @property
    def xhtml_Flow74(self):
        return self.__xhtml_Flow74

    @xhtml_Flow74.setter
    def xhtml_Flow74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow74", None)
        self.__xhtml_Flow74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Ol75"):
                    opp_val = getattr(item, "xhtml_Ol75", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Ol75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Ol75"):
                    opp_val = getattr(item, "xhtml_Ol75", None)
                    
                    setattr(item, "xhtml_Ol75", self)
                    

    @property
    def xhtml_Flow112(self):
        return self.__xhtml_Flow112

    @xhtml_Flow112.setter
    def xhtml_Flow112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow112", None)
        self.__xhtml_Flow112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_B113"):
                    opp_val = getattr(item, "xhtml_B113", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_B113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_B113"):
                    opp_val = getattr(item, "xhtml_B113", None)
                    
                    setattr(item, "xhtml_B113", self)
                    

    @property
    def xhtml_Flow154(self):
        return self.__xhtml_Flow154

    @xhtml_Flow154.setter
    def xhtml_Flow154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow154", None)
        self.__xhtml_Flow154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sub155"):
                    opp_val = getattr(item, "xhtml_Sub155", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sub155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sub155"):
                    opp_val = getattr(item, "xhtml_Sub155", None)
                    
                    setattr(item, "xhtml_Sub155", self)
                    

    @property
    def xhtml_Flow106(self):
        return self.__xhtml_Flow106

    @xhtml_Flow106.setter
    def xhtml_Flow106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow106", None)
        self.__xhtml_Flow106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tt107"):
                    opp_val = getattr(item, "xhtml_Tt107", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tt107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tt107"):
                    opp_val = getattr(item, "xhtml_Tt107", None)
                    
                    setattr(item, "xhtml_Tt107", self)
                    

    @property
    def xhtml_Flow71(self):
        return self.__xhtml_Flow71

    @xhtml_Flow71.setter
    def xhtml_Flow71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow71", None)
        self.__xhtml_Flow71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Ul72"):
                    opp_val = getattr(item, "xhtml_Ul72", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Ul72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Ul72"):
                    opp_val = getattr(item, "xhtml_Ul72", None)
                    
                    setattr(item, "xhtml_Ul72", self)
                    

    @property
    def xhtml_Flow124(self):
        return self.__xhtml_Flow124

    @xhtml_Flow124.setter
    def xhtml_Flow124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow124", None)
        self.__xhtml_Flow124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Strong125"):
                    opp_val = getattr(item, "xhtml_Strong125", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Strong125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Strong125"):
                    opp_val = getattr(item, "xhtml_Strong125", None)
                    
                    setattr(item, "xhtml_Strong125", self)
                    

    @property
    def xhtml_Flow157(self):
        return self.__xhtml_Flow157

    @xhtml_Flow157.setter
    def xhtml_Flow157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow157", None)
        self.__xhtml_Flow157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sup158"):
                    opp_val = getattr(item, "xhtml_Sup158", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sup158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sup158"):
                    opp_val = getattr(item, "xhtml_Sup158", None)
                    
                    setattr(item, "xhtml_Sup158", self)
                    

    @property
    def xhtml_Flow103(self):
        return self.__xhtml_Flow103

    @xhtml_Flow103.setter
    def xhtml_Flow103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow103", None)
        self.__xhtml_Flow103 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Img104"):
                    opp_val = getattr(item, "xhtml_Img104", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Img104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Img104"):
                    opp_val = getattr(item, "xhtml_Img104", None)
                    
                    setattr(item, "xhtml_Img104", self)
                    

    @property
    def xhtml_Flow115(self):
        return self.__xhtml_Flow115

    @xhtml_Flow115.setter
    def xhtml_Flow115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow115", None)
        self.__xhtml_Flow115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Big116"):
                    opp_val = getattr(item, "xhtml_Big116", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Big116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Big116"):
                    opp_val = getattr(item, "xhtml_Big116", None)
                    
                    setattr(item, "xhtml_Big116", self)
                    

    @property
    def xhtml_Flow127(self):
        return self.__xhtml_Flow127

    @xhtml_Flow127.setter
    def xhtml_Flow127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow127", None)
        self.__xhtml_Flow127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dfn128"):
                    opp_val = getattr(item, "xhtml_Dfn128", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dfn128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dfn128"):
                    opp_val = getattr(item, "xhtml_Dfn128", None)
                    
                    setattr(item, "xhtml_Dfn128", self)
                    

    @property
    def xhtml_Flow145(self):
        return self.__xhtml_Flow145

    @xhtml_Flow145.setter
    def xhtml_Flow145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Flow__xhtml_Flow145", None)
        self.__xhtml_Flow145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Cite146"):
                    opp_val = getattr(item, "xhtml_Cite146", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Cite146", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Cite146"):
                    opp_val = getattr(item, "xhtml_Cite146", None)
                    
                    setattr(item, "xhtml_Cite146", self)
                    

class Flow:

    pass
class xhtml_Th(Flow):

    def __init__(self, colspan: str, lang: str, rowspan: str, style: str, valign: str, align: str, char: str, charoff: str, class: str, xhtml_Th: "xhtml_Tr" = None):
        self.colspan = colspan
        self.lang = lang
        self.rowspan = rowspan
        self.style = style
        self.valign = valign
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.xhtml_Th = xhtml_Th
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Th(self):
        return self.__xhtml_Th

    @xhtml_Th.setter
    def xhtml_Th(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Th__xhtml_Th", None)
        self.__xhtml_Th = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Tr418"):
                opp_val = getattr(old_value, "xhtml_Tr418", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Tr418"):
                opp_val = getattr(value, "xhtml_Tr418", None)
                if opp_val is None:
                    setattr(value, "xhtml_Tr418", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Td(Flow):

    def __init__(self, colspan: str, lang: str, rowspan: str, style: str, valign: str, align: str, char: str, charoff: str, class: str, xhtml_Td: "xhtml_Tr" = None):
        self.colspan = colspan
        self.lang = lang
        self.rowspan = rowspan
        self.style = style
        self.valign = valign
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.xhtml_Td = xhtml_Td
        
    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def rowspan(self) -> str:
        return self.__rowspan

    @rowspan.setter
    def rowspan(self, rowspan: str):
        self.__rowspan = rowspan

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def colspan(self) -> str:
        return self.__colspan

    @colspan.setter
    def colspan(self, colspan: str):
        self.__colspan = colspan

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def xhtml_Td(self):
        return self.__xhtml_Td

    @xhtml_Td.setter
    def xhtml_Td(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Td__xhtml_Td", None)
        self.__xhtml_Td = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Tr420"):
                opp_val = getattr(old_value, "xhtml_Tr420", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Tr420"):
                opp_val = getattr(value, "xhtml_Tr420", None)
                if opp_val is None:
                    setattr(value, "xhtml_Tr420", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Ins(Flow):

    pass
class xhtml_Li(Flow):

    def __init__(self, class: str, lang: str, style: str, xhtml_Li: "xhtml_Ol" = None, xhtml_Li423: "xhtml_Ul" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Li = xhtml_Li
        self.xhtml_Li423 = xhtml_Li423
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Li423(self):
        return self.__xhtml_Li423

    @xhtml_Li423.setter
    def xhtml_Li423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Li__xhtml_Li423", None)
        self.__xhtml_Li423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Ul422"):
                opp_val = getattr(old_value, "xhtml_Ul422", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Ul422"):
                opp_val = getattr(value, "xhtml_Ul422", None)
                if opp_val is None:
                    setattr(value, "xhtml_Ul422", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Li(self):
        return self.__xhtml_Li

    @xhtml_Li.setter
    def xhtml_Li(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Li__xhtml_Li", None)
        self.__xhtml_Li = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Ol329"):
                opp_val = getattr(old_value, "xhtml_Ol329", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Ol329"):
                opp_val = getattr(value, "xhtml_Ol329", None)
                if opp_val is None:
                    setattr(value, "xhtml_Ol329", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Del(Flow):

    pass
class xhtml_Dd(Flow):

    def __init__(self, lang: str, style: str, class: str, xhtml_Dd: "xhtml_Dl" = None):
        self.lang = lang
        self.style = style
        self.class = class
        self.xhtml_Dd = xhtml_Dd
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Dd(self):
        return self.__xhtml_Dd

    @xhtml_Dd.setter
    def xhtml_Dd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dd__xhtml_Dd", None)
        self.__xhtml_Dd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Dl64"):
                opp_val = getattr(old_value, "xhtml_Dl64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Dl64"):
                opp_val = getattr(value, "xhtml_Dl64", None)
                if opp_val is None:
                    setattr(value, "xhtml_Dl64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Colgroup:

    def __init__(self, align: str, char: str, charoff: str, class: str, lang: str, span: str, style: str, valign: str, width: str, xhtml_Colgroup: set["xhtml_Col"] = None, xhtml_Colgroup399: "xhtml_Table" = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.lang = lang
        self.span = span
        self.style = style
        self.valign = valign
        self.width = width
        self.xhtml_Colgroup = xhtml_Colgroup if xhtml_Colgroup is not None else set()
        self.xhtml_Colgroup399 = xhtml_Colgroup399
        
    @property
    def span(self) -> str:
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Colgroup399(self):
        return self.__xhtml_Colgroup399

    @xhtml_Colgroup399.setter
    def xhtml_Colgroup399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Colgroup__xhtml_Colgroup399", None)
        self.__xhtml_Colgroup399 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table398"):
                opp_val = getattr(old_value, "xhtml_Table398", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table398"):
                opp_val = getattr(value, "xhtml_Table398", None)
                if opp_val is None:
                    setattr(value, "xhtml_Table398", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Colgroup(self):
        return self.__xhtml_Colgroup

    @xhtml_Colgroup.setter
    def xhtml_Colgroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Colgroup__xhtml_Colgroup", None)
        self.__xhtml_Colgroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Col"):
                    opp_val = getattr(item, "xhtml_Col", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Col", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Col"):
                    opp_val = getattr(item, "xhtml_Col", None)
                    
                    setattr(item, "xhtml_Col", self)
                    

class xhtml_Col:

    def __init__(self, align: str, char: str, charoff: str, class: str, lang: str, span: str, style: str, valign: str, width: str, xhtml_Col: "xhtml_Colgroup" = None, xhtml_Col396: "xhtml_Table" = None):
        self.align = align
        self.char = char
        self.charoff = charoff
        self.class = class
        self.lang = lang
        self.span = span
        self.style = style
        self.valign = valign
        self.width = width
        self.xhtml_Col = xhtml_Col
        self.xhtml_Col396 = xhtml_Col396
        
    @property
    def span(self) -> str:
        return self.__span

    @span.setter
    def span(self, span: str):
        self.__span = span

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def charoff(self) -> str:
        return self.__charoff

    @charoff.setter
    def charoff(self, charoff: str):
        self.__charoff = charoff

    @property
    def xhtml_Col(self):
        return self.__xhtml_Col

    @xhtml_Col.setter
    def xhtml_Col(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Col__xhtml_Col", None)
        self.__xhtml_Col = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Colgroup"):
                opp_val = getattr(old_value, "xhtml_Colgroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Colgroup"):
                opp_val = getattr(value, "xhtml_Colgroup", None)
                if opp_val is None:
                    setattr(value, "xhtml_Colgroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Col396(self):
        return self.__xhtml_Col396

    @xhtml_Col396.setter
    def xhtml_Col396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Col__xhtml_Col396", None)
        self.__xhtml_Col396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table395"):
                opp_val = getattr(old_value, "xhtml_Table395", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table395"):
                opp_val = getattr(value, "xhtml_Table395", None)
                if opp_val is None:
                    setattr(value, "xhtml_Table395", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Ol:

    def __init__(self, lang: str, style: str, li: str, class: str, xhtml_Ol: "xhtml_Block" = None, xhtml_Ol75: "xhtml_Flow" = None, xhtml_Ol243: "xhtml_Object" = None, xhtml_Ol329: set["xhtml_Li"] = None):
        self.lang = lang
        self.style = style
        self.li = li
        self.class = class
        self.xhtml_Ol = xhtml_Ol
        self.xhtml_Ol75 = xhtml_Ol75
        self.xhtml_Ol243 = xhtml_Ol243
        self.xhtml_Ol329 = xhtml_Ol329 if xhtml_Ol329 is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def li(self) -> str:
        return self.__li

    @li.setter
    def li(self, li: str):
        self.__li = li

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Ol(self):
        return self.__xhtml_Ol

    @xhtml_Ol.setter
    def xhtml_Ol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ol__xhtml_Ol", None)
        self.__xhtml_Ol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block49"):
                opp_val = getattr(old_value, "xhtml_Block49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block49"):
                opp_val = getattr(value, "xhtml_Block49", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Ol243(self):
        return self.__xhtml_Ol243

    @xhtml_Ol243.setter
    def xhtml_Ol243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ol__xhtml_Ol243", None)
        self.__xhtml_Ol243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object242"):
                opp_val = getattr(old_value, "xhtml_Object242", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object242"):
                opp_val = getattr(value, "xhtml_Object242", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object242", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Ol75(self):
        return self.__xhtml_Ol75

    @xhtml_Ol75.setter
    def xhtml_Ol75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ol__xhtml_Ol75", None)
        self.__xhtml_Ol75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow74"):
                opp_val = getattr(old_value, "xhtml_Flow74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow74"):
                opp_val = getattr(value, "xhtml_Flow74", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Ol329(self):
        return self.__xhtml_Ol329

    @xhtml_Ol329.setter
    def xhtml_Ol329(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ol__xhtml_Ol329", None)
        self.__xhtml_Ol329 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Li"):
                    opp_val = getattr(item, "xhtml_Li", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Li", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Li"):
                    opp_val = getattr(item, "xhtml_Li", None)
                    
                    setattr(item, "xhtml_Li", self)
                    

class Block:

    pass
class xhtml_Table:

    def __init__(self, border: str, cellpadding: str, cellspacing: str, class: str, frame: str, hl7Id: str, lang: str, rules: str, style: str, width: str, xhtml_Table: "xhtml_Block" = None, xhtml_Table90: "xhtml_Flow" = None, xhtml_Table258: "xhtml_Object" = None, xhtml_Table393: "xhtml_Caption" = None, xhtml_Table407: set["xhtml_Tr"] = None, xhtml_Table395: set["xhtml_Col"] = None, xhtml_Table398: set["xhtml_Colgroup"] = None, xhtml_Table401: "xhtml_Thead" = None, xhtml_Table403: "xhtml_Tfoot" = None, xhtml_Table405: set["xhtml_Tbody"] = None):
        self.border = border
        self.cellpadding = cellpadding
        self.cellspacing = cellspacing
        self.class = class
        self.frame = frame
        self.hl7Id = hl7Id
        self.lang = lang
        self.rules = rules
        self.style = style
        self.width = width
        self.xhtml_Table = xhtml_Table
        self.xhtml_Table90 = xhtml_Table90
        self.xhtml_Table258 = xhtml_Table258
        self.xhtml_Table393 = xhtml_Table393
        self.xhtml_Table407 = xhtml_Table407 if xhtml_Table407 is not None else set()
        self.xhtml_Table395 = xhtml_Table395 if xhtml_Table395 is not None else set()
        self.xhtml_Table398 = xhtml_Table398 if xhtml_Table398 is not None else set()
        self.xhtml_Table401 = xhtml_Table401
        self.xhtml_Table403 = xhtml_Table403
        self.xhtml_Table405 = xhtml_Table405 if xhtml_Table405 is not None else set()
        
    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def hl7Id(self) -> str:
        return self.__hl7Id

    @hl7Id.setter
    def hl7Id(self, hl7Id: str):
        self.__hl7Id = hl7Id

    @property
    def rules(self) -> str:
        return self.__rules

    @rules.setter
    def rules(self, rules: str):
        self.__rules = rules

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def cellspacing(self) -> str:
        return self.__cellspacing

    @cellspacing.setter
    def cellspacing(self, cellspacing: str):
        self.__cellspacing = cellspacing

    @property
    def frame(self) -> str:
        return self.__frame

    @frame.setter
    def frame(self, frame: str):
        self.__frame = frame

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def cellpadding(self) -> str:
        return self.__cellpadding

    @cellpadding.setter
    def cellpadding(self, cellpadding: str):
        self.__cellpadding = cellpadding

    @property
    def xhtml_Table393(self):
        return self.__xhtml_Table393

    @xhtml_Table393.setter
    def xhtml_Table393(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table393", None)
        self.__xhtml_Table393 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Caption"):
                opp_val = getattr(old_value, "xhtml_Caption", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Caption", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Caption"):
                opp_val = getattr(value, "xhtml_Caption", None)
                setattr(value, "xhtml_Caption", self)

    @property
    def xhtml_Table398(self):
        return self.__xhtml_Table398

    @xhtml_Table398.setter
    def xhtml_Table398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table398", None)
        self.__xhtml_Table398 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Colgroup399"):
                    opp_val = getattr(item, "xhtml_Colgroup399", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Colgroup399", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Colgroup399"):
                    opp_val = getattr(item, "xhtml_Colgroup399", None)
                    
                    setattr(item, "xhtml_Colgroup399", self)
                    

    @property
    def xhtml_Table403(self):
        return self.__xhtml_Table403

    @xhtml_Table403.setter
    def xhtml_Table403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table403", None)
        self.__xhtml_Table403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Tfoot"):
                opp_val = getattr(old_value, "xhtml_Tfoot", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Tfoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Tfoot"):
                opp_val = getattr(value, "xhtml_Tfoot", None)
                setattr(value, "xhtml_Tfoot", self)

    @property
    def xhtml_Table401(self):
        return self.__xhtml_Table401

    @xhtml_Table401.setter
    def xhtml_Table401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table401", None)
        self.__xhtml_Table401 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Thead"):
                opp_val = getattr(old_value, "xhtml_Thead", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Thead", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Thead"):
                opp_val = getattr(value, "xhtml_Thead", None)
                setattr(value, "xhtml_Thead", self)

    @property
    def xhtml_Table90(self):
        return self.__xhtml_Table90

    @xhtml_Table90.setter
    def xhtml_Table90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table90", None)
        self.__xhtml_Table90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow89"):
                opp_val = getattr(old_value, "xhtml_Flow89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow89"):
                opp_val = getattr(value, "xhtml_Flow89", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Table(self):
        return self.__xhtml_Table

    @xhtml_Table.setter
    def xhtml_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table", None)
        self.__xhtml_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block59"):
                opp_val = getattr(old_value, "xhtml_Block59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block59"):
                opp_val = getattr(value, "xhtml_Block59", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Table258(self):
        return self.__xhtml_Table258

    @xhtml_Table258.setter
    def xhtml_Table258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table258", None)
        self.__xhtml_Table258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object257"):
                opp_val = getattr(old_value, "xhtml_Object257", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object257"):
                opp_val = getattr(value, "xhtml_Object257", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object257", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Table407(self):
        return self.__xhtml_Table407

    @xhtml_Table407.setter
    def xhtml_Table407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table407", None)
        self.__xhtml_Table407 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tr"):
                    opp_val = getattr(item, "xhtml_Tr", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tr"):
                    opp_val = getattr(item, "xhtml_Tr", None)
                    
                    setattr(item, "xhtml_Tr", self)
                    

    @property
    def xhtml_Table405(self):
        return self.__xhtml_Table405

    @xhtml_Table405.setter
    def xhtml_Table405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table405", None)
        self.__xhtml_Table405 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tbody"):
                    opp_val = getattr(item, "xhtml_Tbody", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tbody", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tbody"):
                    opp_val = getattr(item, "xhtml_Tbody", None)
                    
                    setattr(item, "xhtml_Tbody", self)
                    

    @property
    def xhtml_Table395(self):
        return self.__xhtml_Table395

    @xhtml_Table395.setter
    def xhtml_Table395(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Table__xhtml_Table395", None)
        self.__xhtml_Table395 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Col396"):
                    opp_val = getattr(item, "xhtml_Col396", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Col396", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Col396"):
                    opp_val = getattr(item, "xhtml_Col396", None)
                    
                    setattr(item, "xhtml_Col396", self)
                    

class xhtml_Blockquote(Block):

    def __init__(self, cite: str, lang: str, style: str, class: str, xhtml_Blockquote: "xhtml_Block" = None, xhtml_Blockquote87: "xhtml_Flow" = None, xhtml_Blockquote255: "xhtml_Object" = None):
        self.cite = cite
        self.lang = lang
        self.style = style
        self.class = class
        self.xhtml_Blockquote = xhtml_Blockquote
        self.xhtml_Blockquote87 = xhtml_Blockquote87
        self.xhtml_Blockquote255 = xhtml_Blockquote255
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def cite(self) -> str:
        return self.__cite

    @cite.setter
    def cite(self, cite: str):
        self.__cite = cite

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Blockquote255(self):
        return self.__xhtml_Blockquote255

    @xhtml_Blockquote255.setter
    def xhtml_Blockquote255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Blockquote__xhtml_Blockquote255", None)
        self.__xhtml_Blockquote255 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object254"):
                opp_val = getattr(old_value, "xhtml_Object254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object254"):
                opp_val = getattr(value, "xhtml_Object254", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Blockquote(self):
        return self.__xhtml_Blockquote

    @xhtml_Blockquote.setter
    def xhtml_Blockquote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Blockquote__xhtml_Blockquote", None)
        self.__xhtml_Blockquote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block57"):
                opp_val = getattr(old_value, "xhtml_Block57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block57"):
                opp_val = getattr(value, "xhtml_Block57", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Blockquote87(self):
        return self.__xhtml_Blockquote87

    @xhtml_Blockquote87.setter
    def xhtml_Blockquote87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Blockquote__xhtml_Blockquote87", None)
        self.__xhtml_Blockquote87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow86"):
                opp_val = getattr(old_value, "xhtml_Flow86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow86"):
                opp_val = getattr(value, "xhtml_Flow86", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Hr:

    def __init__(self, class: str, lang: str, style: str, xhtml_Hr: "xhtml_Block" = None, xhtml_Hr84: "xhtml_Flow" = None, xhtml_Hr252: "xhtml_Object" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Hr = xhtml_Hr
        self.xhtml_Hr84 = xhtml_Hr84
        self.xhtml_Hr252 = xhtml_Hr252
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Hr(self):
        return self.__xhtml_Hr

    @xhtml_Hr.setter
    def xhtml_Hr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Hr__xhtml_Hr", None)
        self.__xhtml_Hr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block55"):
                opp_val = getattr(old_value, "xhtml_Block55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block55"):
                opp_val = getattr(value, "xhtml_Block55", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Hr252(self):
        return self.__xhtml_Hr252

    @xhtml_Hr252.setter
    def xhtml_Hr252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Hr__xhtml_Hr252", None)
        self.__xhtml_Hr252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object251"):
                opp_val = getattr(old_value, "xhtml_Object251", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object251"):
                opp_val = getattr(value, "xhtml_Object251", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object251", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Hr84(self):
        return self.__xhtml_Hr84

    @xhtml_Hr84.setter
    def xhtml_Hr84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Hr__xhtml_Hr84", None)
        self.__xhtml_Hr84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow83"):
                opp_val = getattr(old_value, "xhtml_Flow83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow83"):
                opp_val = getattr(value, "xhtml_Flow83", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Pre(PreContent):

    def __init__(self, class: str, lang: str, space: str, style: str, xhtml_Pre: "xhtml_Block" = None, xhtml_Pre81: "xhtml_Flow" = None, xhtml_Pre249: "xhtml_Object" = None):
        self.class = class
        self.lang = lang
        self.space = space
        self.style = style
        self.xhtml_Pre = xhtml_Pre
        self.xhtml_Pre81 = xhtml_Pre81
        self.xhtml_Pre249 = xhtml_Pre249
        
    @property
    def space(self) -> str:
        return self.__space

    @space.setter
    def space(self, space: str):
        self.__space = space

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Pre(self):
        return self.__xhtml_Pre

    @xhtml_Pre.setter
    def xhtml_Pre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Pre__xhtml_Pre", None)
        self.__xhtml_Pre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block53"):
                opp_val = getattr(old_value, "xhtml_Block53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block53"):
                opp_val = getattr(value, "xhtml_Block53", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Pre249(self):
        return self.__xhtml_Pre249

    @xhtml_Pre249.setter
    def xhtml_Pre249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Pre__xhtml_Pre249", None)
        self.__xhtml_Pre249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object248"):
                opp_val = getattr(old_value, "xhtml_Object248", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object248"):
                opp_val = getattr(value, "xhtml_Object248", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object248", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Pre81(self):
        return self.__xhtml_Pre81

    @xhtml_Pre81.setter
    def xhtml_Pre81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Pre__xhtml_Pre81", None)
        self.__xhtml_Pre81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow80"):
                opp_val = getattr(old_value, "xhtml_Flow80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow80"):
                opp_val = getattr(value, "xhtml_Flow80", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Dl:

    def __init__(self, group: str, class: str, lang: str, style: str, xhtml_Dl: "xhtml_Block" = None, xhtml_Dl62: set["xhtml_Dt"] = None, xhtml_Dl64: set["xhtml_Dd"] = None, xhtml_Dl78: "xhtml_Flow" = None, xhtml_Dl246: "xhtml_Object" = None):
        self.group = group
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Dl = xhtml_Dl
        self.xhtml_Dl62 = xhtml_Dl62 if xhtml_Dl62 is not None else set()
        self.xhtml_Dl64 = xhtml_Dl64 if xhtml_Dl64 is not None else set()
        self.xhtml_Dl78 = xhtml_Dl78
        self.xhtml_Dl246 = xhtml_Dl246
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_Dl64(self):
        return self.__xhtml_Dl64

    @xhtml_Dl64.setter
    def xhtml_Dl64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dl__xhtml_Dl64", None)
        self.__xhtml_Dl64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dd"):
                    opp_val = getattr(item, "xhtml_Dd", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dd"):
                    opp_val = getattr(item, "xhtml_Dd", None)
                    
                    setattr(item, "xhtml_Dd", self)
                    

    @property
    def xhtml_Dl78(self):
        return self.__xhtml_Dl78

    @xhtml_Dl78.setter
    def xhtml_Dl78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dl__xhtml_Dl78", None)
        self.__xhtml_Dl78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow77"):
                opp_val = getattr(old_value, "xhtml_Flow77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow77"):
                opp_val = getattr(value, "xhtml_Flow77", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Dl62(self):
        return self.__xhtml_Dl62

    @xhtml_Dl62.setter
    def xhtml_Dl62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dl__xhtml_Dl62", None)
        self.__xhtml_Dl62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dt"):
                    opp_val = getattr(item, "xhtml_Dt", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dt"):
                    opp_val = getattr(item, "xhtml_Dt", None)
                    
                    setattr(item, "xhtml_Dt", self)
                    

    @property
    def xhtml_Dl246(self):
        return self.__xhtml_Dl246

    @xhtml_Dl246.setter
    def xhtml_Dl246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dl__xhtml_Dl246", None)
        self.__xhtml_Dl246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object245"):
                opp_val = getattr(old_value, "xhtml_Object245", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object245"):
                opp_val = getattr(value, "xhtml_Object245", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object245", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Dl(self):
        return self.__xhtml_Dl

    @xhtml_Dl.setter
    def xhtml_Dl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dl__xhtml_Dl", None)
        self.__xhtml_Dl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block51"):
                opp_val = getattr(old_value, "xhtml_Block51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block51"):
                opp_val = getattr(value, "xhtml_Block51", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Ul:

    def __init__(self, lang: str, style: str, li: str, class: str, xhtml_Ul: "xhtml_Block" = None, xhtml_Ul72: "xhtml_Flow" = None, xhtml_Ul240: "xhtml_Object" = None, xhtml_Ul422: set["xhtml_Li"] = None):
        self.lang = lang
        self.style = style
        self.li = li
        self.class = class
        self.xhtml_Ul = xhtml_Ul
        self.xhtml_Ul72 = xhtml_Ul72
        self.xhtml_Ul240 = xhtml_Ul240
        self.xhtml_Ul422 = xhtml_Ul422 if xhtml_Ul422 is not None else set()
        
    @property
    def li(self) -> str:
        return self.__li

    @li.setter
    def li(self, li: str):
        self.__li = li

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Ul422(self):
        return self.__xhtml_Ul422

    @xhtml_Ul422.setter
    def xhtml_Ul422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ul__xhtml_Ul422", None)
        self.__xhtml_Ul422 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Li423"):
                    opp_val = getattr(item, "xhtml_Li423", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Li423", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Li423"):
                    opp_val = getattr(item, "xhtml_Li423", None)
                    
                    setattr(item, "xhtml_Li423", self)
                    

    @property
    def xhtml_Ul(self):
        return self.__xhtml_Ul

    @xhtml_Ul.setter
    def xhtml_Ul(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ul__xhtml_Ul", None)
        self.__xhtml_Ul = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block47"):
                opp_val = getattr(old_value, "xhtml_Block47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block47"):
                opp_val = getattr(value, "xhtml_Block47", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Ul240(self):
        return self.__xhtml_Ul240

    @xhtml_Ul240.setter
    def xhtml_Ul240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ul__xhtml_Ul240", None)
        self.__xhtml_Ul240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object239"):
                opp_val = getattr(old_value, "xhtml_Object239", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object239"):
                opp_val = getattr(value, "xhtml_Object239", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object239", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Ul72(self):
        return self.__xhtml_Ul72

    @xhtml_Ul72.setter
    def xhtml_Ul72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Ul__xhtml_Ul72", None)
        self.__xhtml_Ul72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow71"):
                opp_val = getattr(old_value, "xhtml_Flow71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow71"):
                opp_val = getattr(value, "xhtml_Flow71", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Div(Flow):

    def __init__(self, class: str, hl7Id: str, lang: str, title: str, style: str, xhtml_Div: "xhtml_Block" = None, xhtml_Div69: "xhtml_Flow" = None, xhtml_Div237: "xhtml_Object" = None):
        self.class = class
        self.hl7Id = hl7Id
        self.lang = lang
        self.title = title
        self.style = style
        self.xhtml_Div = xhtml_Div
        self.xhtml_Div69 = xhtml_Div69
        self.xhtml_Div237 = xhtml_Div237
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def hl7Id(self) -> str:
        return self.__hl7Id

    @hl7Id.setter
    def hl7Id(self, hl7Id: str):
        self.__hl7Id = hl7Id

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Div69(self):
        return self.__xhtml_Div69

    @xhtml_Div69.setter
    def xhtml_Div69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Div__xhtml_Div69", None)
        self.__xhtml_Div69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow68"):
                opp_val = getattr(old_value, "xhtml_Flow68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow68"):
                opp_val = getattr(value, "xhtml_Flow68", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Div(self):
        return self.__xhtml_Div

    @xhtml_Div.setter
    def xhtml_Div(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Div__xhtml_Div", None)
        self.__xhtml_Div = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block45"):
                opp_val = getattr(old_value, "xhtml_Block45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block45"):
                opp_val = getattr(value, "xhtml_Block45", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Div237(self):
        return self.__xhtml_Div237

    @xhtml_Div237.setter
    def xhtml_Div237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Div__xhtml_Div237", None)
        self.__xhtml_Div237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object236"):
                opp_val = getattr(old_value, "xhtml_Object236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object236"):
                opp_val = getattr(value, "xhtml_Object236", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Block:

    def __init__(self, mixed: str, block: str, xhtml_Block: set["xhtml_P"] = None, xhtml_Block45: set["xhtml_Div"] = None, xhtml_Block47: set["xhtml_Ul"] = None, xhtml_Block49: set["xhtml_Ol"] = None, xhtml_Block51: set["xhtml_Dl"] = None, xhtml_Block53: set["xhtml_Pre"] = None, xhtml_Block55: set["xhtml_Hr"] = None, xhtml_Block57: set["xhtml_Blockquote"] = None, xhtml_Block59: set["xhtml_Table"] = None):
        self.mixed = mixed
        self.block = block
        self.xhtml_Block = xhtml_Block if xhtml_Block is not None else set()
        self.xhtml_Block45 = xhtml_Block45 if xhtml_Block45 is not None else set()
        self.xhtml_Block47 = xhtml_Block47 if xhtml_Block47 is not None else set()
        self.xhtml_Block49 = xhtml_Block49 if xhtml_Block49 is not None else set()
        self.xhtml_Block51 = xhtml_Block51 if xhtml_Block51 is not None else set()
        self.xhtml_Block53 = xhtml_Block53 if xhtml_Block53 is not None else set()
        self.xhtml_Block55 = xhtml_Block55 if xhtml_Block55 is not None else set()
        self.xhtml_Block57 = xhtml_Block57 if xhtml_Block57 is not None else set()
        self.xhtml_Block59 = xhtml_Block59 if xhtml_Block59 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def block(self) -> str:
        return self.__block

    @block.setter
    def block(self, block: str):
        self.__block = block

    @property
    def xhtml_Block45(self):
        return self.__xhtml_Block45

    @xhtml_Block45.setter
    def xhtml_Block45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block45", None)
        self.__xhtml_Block45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Div"):
                    opp_val = getattr(item, "xhtml_Div", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Div", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Div"):
                    opp_val = getattr(item, "xhtml_Div", None)
                    
                    setattr(item, "xhtml_Div", self)
                    

    @property
    def xhtml_Block55(self):
        return self.__xhtml_Block55

    @xhtml_Block55.setter
    def xhtml_Block55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block55", None)
        self.__xhtml_Block55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Hr"):
                    opp_val = getattr(item, "xhtml_Hr", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Hr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Hr"):
                    opp_val = getattr(item, "xhtml_Hr", None)
                    
                    setattr(item, "xhtml_Hr", self)
                    

    @property
    def xhtml_Block59(self):
        return self.__xhtml_Block59

    @xhtml_Block59.setter
    def xhtml_Block59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block59", None)
        self.__xhtml_Block59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Table"):
                    opp_val = getattr(item, "xhtml_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Table"):
                    opp_val = getattr(item, "xhtml_Table", None)
                    
                    setattr(item, "xhtml_Table", self)
                    

    @property
    def xhtml_Block57(self):
        return self.__xhtml_Block57

    @xhtml_Block57.setter
    def xhtml_Block57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block57", None)
        self.__xhtml_Block57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Blockquote"):
                    opp_val = getattr(item, "xhtml_Blockquote", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Blockquote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Blockquote"):
                    opp_val = getattr(item, "xhtml_Blockquote", None)
                    
                    setattr(item, "xhtml_Blockquote", self)
                    

    @property
    def xhtml_Block53(self):
        return self.__xhtml_Block53

    @xhtml_Block53.setter
    def xhtml_Block53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block53", None)
        self.__xhtml_Block53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Pre"):
                    opp_val = getattr(item, "xhtml_Pre", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Pre", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Pre"):
                    opp_val = getattr(item, "xhtml_Pre", None)
                    
                    setattr(item, "xhtml_Pre", self)
                    

    @property
    def xhtml_Block47(self):
        return self.__xhtml_Block47

    @xhtml_Block47.setter
    def xhtml_Block47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block47", None)
        self.__xhtml_Block47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Ul"):
                    opp_val = getattr(item, "xhtml_Ul", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Ul", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Ul"):
                    opp_val = getattr(item, "xhtml_Ul", None)
                    
                    setattr(item, "xhtml_Ul", self)
                    

    @property
    def xhtml_Block49(self):
        return self.__xhtml_Block49

    @xhtml_Block49.setter
    def xhtml_Block49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block49", None)
        self.__xhtml_Block49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Ol"):
                    opp_val = getattr(item, "xhtml_Ol", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Ol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Ol"):
                    opp_val = getattr(item, "xhtml_Ol", None)
                    
                    setattr(item, "xhtml_Ol", self)
                    

    @property
    def xhtml_Block(self):
        return self.__xhtml_Block

    @xhtml_Block.setter
    def xhtml_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block", None)
        self.__xhtml_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_P"):
                    opp_val = getattr(item, "xhtml_P", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_P", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_P"):
                    opp_val = getattr(item, "xhtml_P", None)
                    
                    setattr(item, "xhtml_P", self)
                    

    @property
    def xhtml_Block51(self):
        return self.__xhtml_Block51

    @xhtml_Block51.setter
    def xhtml_Block51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Block__xhtml_Block51", None)
        self.__xhtml_Block51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dl"):
                    opp_val = getattr(item, "xhtml_Dl", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dl"):
                    opp_val = getattr(item, "xhtml_Dl", None)
                    
                    setattr(item, "xhtml_Dl", self)
                    

class xhtml_Object:

    def __init__(self, mixed: str, group: str, hl7Id: str, name: str, xhtml_Object: "xhtml_AContent" = None, xhtml_Object101: "xhtml_Flow" = None, xhtml_Object172: "xhtml_Inline" = None, xhtml_Object231: set["xhtml_Param"] = None, xhtml_Object248: set["xhtml_Pre"] = None, xhtml_Object251: set["xhtml_Hr"] = None, xhtml_Object254: set["xhtml_Blockquote"] = None, xhtml_Object233: set["xhtml_P"] = None, xhtml_Object236: set["xhtml_Div"] = None, xhtml_Object239: set["xhtml_Ul"] = None, xhtml_Object242: set["xhtml_Ol"] = None, xhtml_Object245: set["xhtml_Dl"] = None, xhtml_Object270: "xhtml_Object" = None, xhtml_Object268: set["xhtml_Object"] = None, xhtml_Object272: set["xhtml_Img"] = None, xhtml_Object275: set["xhtml_Tt"] = None, xhtml_Object257: set["xhtml_Table"] = None, xhtml_Object260: set["xhtml_A"] = None, xhtml_Object263: set["xhtml_Br"] = None, xhtml_Object266: set["xhtml_Span"] = None, xhtml_Object287: set["xhtml_Small"] = None, xhtml_Object290: set["xhtml_Em"] = None, xhtml_Object293: set["xhtml_Strong"] = None, xhtml_Object278: set["xhtml_I"] = None, xhtml_Object281: set["xhtml_B"] = None, xhtml_Object284: set["xhtml_Big"] = None, xhtml_Object305: set["xhtml_Samp"] = None, xhtml_Object308: set["xhtml_Kbd"] = None, xhtml_Object311: set["xhtml_Var"] = None, xhtml_Object296: set["xhtml_Dfn"] = None, xhtml_Object299: set["xhtml_Code"] = None, xhtml_Object302: set["xhtml_Q"] = None, xhtml_Object314: set["xhtml_Cite"] = None, xhtml_Object317: set["xhtml_Abbr"] = None, xhtml_Object320: set["xhtml_Acronym"] = None, xhtml_Object323: set["xhtml_Sub"] = None, xhtml_Object326: set["xhtml_Sup"] = None):
        self.mixed = mixed
        self.group = group
        self.hl7Id = hl7Id
        self.name = name
        self.xhtml_Object = xhtml_Object
        self.xhtml_Object101 = xhtml_Object101
        self.xhtml_Object172 = xhtml_Object172
        self.xhtml_Object231 = xhtml_Object231 if xhtml_Object231 is not None else set()
        self.xhtml_Object248 = xhtml_Object248 if xhtml_Object248 is not None else set()
        self.xhtml_Object251 = xhtml_Object251 if xhtml_Object251 is not None else set()
        self.xhtml_Object254 = xhtml_Object254 if xhtml_Object254 is not None else set()
        self.xhtml_Object233 = xhtml_Object233 if xhtml_Object233 is not None else set()
        self.xhtml_Object236 = xhtml_Object236 if xhtml_Object236 is not None else set()
        self.xhtml_Object239 = xhtml_Object239 if xhtml_Object239 is not None else set()
        self.xhtml_Object242 = xhtml_Object242 if xhtml_Object242 is not None else set()
        self.xhtml_Object245 = xhtml_Object245 if xhtml_Object245 is not None else set()
        self.xhtml_Object270 = xhtml_Object270
        self.xhtml_Object268 = xhtml_Object268 if xhtml_Object268 is not None else set()
        self.xhtml_Object272 = xhtml_Object272 if xhtml_Object272 is not None else set()
        self.xhtml_Object275 = xhtml_Object275 if xhtml_Object275 is not None else set()
        self.xhtml_Object257 = xhtml_Object257 if xhtml_Object257 is not None else set()
        self.xhtml_Object260 = xhtml_Object260 if xhtml_Object260 is not None else set()
        self.xhtml_Object263 = xhtml_Object263 if xhtml_Object263 is not None else set()
        self.xhtml_Object266 = xhtml_Object266 if xhtml_Object266 is not None else set()
        self.xhtml_Object287 = xhtml_Object287 if xhtml_Object287 is not None else set()
        self.xhtml_Object290 = xhtml_Object290 if xhtml_Object290 is not None else set()
        self.xhtml_Object293 = xhtml_Object293 if xhtml_Object293 is not None else set()
        self.xhtml_Object278 = xhtml_Object278 if xhtml_Object278 is not None else set()
        self.xhtml_Object281 = xhtml_Object281 if xhtml_Object281 is not None else set()
        self.xhtml_Object284 = xhtml_Object284 if xhtml_Object284 is not None else set()
        self.xhtml_Object305 = xhtml_Object305 if xhtml_Object305 is not None else set()
        self.xhtml_Object308 = xhtml_Object308 if xhtml_Object308 is not None else set()
        self.xhtml_Object311 = xhtml_Object311 if xhtml_Object311 is not None else set()
        self.xhtml_Object296 = xhtml_Object296 if xhtml_Object296 is not None else set()
        self.xhtml_Object299 = xhtml_Object299 if xhtml_Object299 is not None else set()
        self.xhtml_Object302 = xhtml_Object302 if xhtml_Object302 is not None else set()
        self.xhtml_Object314 = xhtml_Object314 if xhtml_Object314 is not None else set()
        self.xhtml_Object317 = xhtml_Object317 if xhtml_Object317 is not None else set()
        self.xhtml_Object320 = xhtml_Object320 if xhtml_Object320 is not None else set()
        self.xhtml_Object323 = xhtml_Object323 if xhtml_Object323 is not None else set()
        self.xhtml_Object326 = xhtml_Object326 if xhtml_Object326 is not None else set()
        
    @property
    def hl7Id(self) -> str:
        return self.__hl7Id

    @hl7Id.setter
    def hl7Id(self, hl7Id: str):
        self.__hl7Id = hl7Id

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_Object305(self):
        return self.__xhtml_Object305

    @xhtml_Object305.setter
    def xhtml_Object305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object305", None)
        self.__xhtml_Object305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Samp306"):
                    opp_val = getattr(item, "xhtml_Samp306", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Samp306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Samp306"):
                    opp_val = getattr(item, "xhtml_Samp306", None)
                    
                    setattr(item, "xhtml_Samp306", self)
                    

    @property
    def xhtml_Object257(self):
        return self.__xhtml_Object257

    @xhtml_Object257.setter
    def xhtml_Object257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object257", None)
        self.__xhtml_Object257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Table258"):
                    opp_val = getattr(item, "xhtml_Table258", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Table258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Table258"):
                    opp_val = getattr(item, "xhtml_Table258", None)
                    
                    setattr(item, "xhtml_Table258", self)
                    

    @property
    def xhtml_Object323(self):
        return self.__xhtml_Object323

    @xhtml_Object323.setter
    def xhtml_Object323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object323", None)
        self.__xhtml_Object323 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sub324"):
                    opp_val = getattr(item, "xhtml_Sub324", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sub324", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sub324"):
                    opp_val = getattr(item, "xhtml_Sub324", None)
                    
                    setattr(item, "xhtml_Sub324", self)
                    

    @property
    def xhtml_Object266(self):
        return self.__xhtml_Object266

    @xhtml_Object266.setter
    def xhtml_Object266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object266", None)
        self.__xhtml_Object266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Span267"):
                    opp_val = getattr(item, "xhtml_Span267", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Span267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Span267"):
                    opp_val = getattr(item, "xhtml_Span267", None)
                    
                    setattr(item, "xhtml_Span267", self)
                    

    @property
    def xhtml_Object287(self):
        return self.__xhtml_Object287

    @xhtml_Object287.setter
    def xhtml_Object287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object287", None)
        self.__xhtml_Object287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Small288"):
                    opp_val = getattr(item, "xhtml_Small288", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Small288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Small288"):
                    opp_val = getattr(item, "xhtml_Small288", None)
                    
                    setattr(item, "xhtml_Small288", self)
                    

    @property
    def xhtml_Object239(self):
        return self.__xhtml_Object239

    @xhtml_Object239.setter
    def xhtml_Object239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object239", None)
        self.__xhtml_Object239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Ul240"):
                    opp_val = getattr(item, "xhtml_Ul240", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Ul240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Ul240"):
                    opp_val = getattr(item, "xhtml_Ul240", None)
                    
                    setattr(item, "xhtml_Ul240", self)
                    

    @property
    def xhtml_Object308(self):
        return self.__xhtml_Object308

    @xhtml_Object308.setter
    def xhtml_Object308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object308", None)
        self.__xhtml_Object308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Kbd309"):
                    opp_val = getattr(item, "xhtml_Kbd309", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Kbd309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Kbd309"):
                    opp_val = getattr(item, "xhtml_Kbd309", None)
                    
                    setattr(item, "xhtml_Kbd309", self)
                    

    @property
    def xhtml_Object284(self):
        return self.__xhtml_Object284

    @xhtml_Object284.setter
    def xhtml_Object284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object284", None)
        self.__xhtml_Object284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Big285"):
                    opp_val = getattr(item, "xhtml_Big285", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Big285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Big285"):
                    opp_val = getattr(item, "xhtml_Big285", None)
                    
                    setattr(item, "xhtml_Big285", self)
                    

    @property
    def xhtml_Object302(self):
        return self.__xhtml_Object302

    @xhtml_Object302.setter
    def xhtml_Object302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object302", None)
        self.__xhtml_Object302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Q303"):
                    opp_val = getattr(item, "xhtml_Q303", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Q303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Q303"):
                    opp_val = getattr(item, "xhtml_Q303", None)
                    
                    setattr(item, "xhtml_Q303", self)
                    

    @property
    def xhtml_Object317(self):
        return self.__xhtml_Object317

    @xhtml_Object317.setter
    def xhtml_Object317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object317", None)
        self.__xhtml_Object317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Abbr318"):
                    opp_val = getattr(item, "xhtml_Abbr318", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Abbr318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Abbr318"):
                    opp_val = getattr(item, "xhtml_Abbr318", None)
                    
                    setattr(item, "xhtml_Abbr318", self)
                    

    @property
    def xhtml_Object326(self):
        return self.__xhtml_Object326

    @xhtml_Object326.setter
    def xhtml_Object326(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object326", None)
        self.__xhtml_Object326 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sup327"):
                    opp_val = getattr(item, "xhtml_Sup327", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sup327", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sup327"):
                    opp_val = getattr(item, "xhtml_Sup327", None)
                    
                    setattr(item, "xhtml_Sup327", self)
                    

    @property
    def xhtml_Object231(self):
        return self.__xhtml_Object231

    @xhtml_Object231.setter
    def xhtml_Object231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object231", None)
        self.__xhtml_Object231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Param"):
                    opp_val = getattr(item, "xhtml_Param", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Param"):
                    opp_val = getattr(item, "xhtml_Param", None)
                    
                    setattr(item, "xhtml_Param", self)
                    

    @property
    def xhtml_Object293(self):
        return self.__xhtml_Object293

    @xhtml_Object293.setter
    def xhtml_Object293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object293", None)
        self.__xhtml_Object293 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Strong294"):
                    opp_val = getattr(item, "xhtml_Strong294", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Strong294", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Strong294"):
                    opp_val = getattr(item, "xhtml_Strong294", None)
                    
                    setattr(item, "xhtml_Strong294", self)
                    

    @property
    def xhtml_Object101(self):
        return self.__xhtml_Object101

    @xhtml_Object101.setter
    def xhtml_Object101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object101", None)
        self.__xhtml_Object101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow100"):
                opp_val = getattr(old_value, "xhtml_Flow100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow100"):
                opp_val = getattr(value, "xhtml_Flow100", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Object236(self):
        return self.__xhtml_Object236

    @xhtml_Object236.setter
    def xhtml_Object236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object236", None)
        self.__xhtml_Object236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Div237"):
                    opp_val = getattr(item, "xhtml_Div237", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Div237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Div237"):
                    opp_val = getattr(item, "xhtml_Div237", None)
                    
                    setattr(item, "xhtml_Div237", self)
                    

    @property
    def xhtml_Object172(self):
        return self.__xhtml_Object172

    @xhtml_Object172.setter
    def xhtml_Object172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object172", None)
        self.__xhtml_Object172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline171"):
                opp_val = getattr(old_value, "xhtml_Inline171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline171"):
                opp_val = getattr(value, "xhtml_Inline171", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Object263(self):
        return self.__xhtml_Object263

    @xhtml_Object263.setter
    def xhtml_Object263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object263", None)
        self.__xhtml_Object263 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Br264"):
                    opp_val = getattr(item, "xhtml_Br264", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Br264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Br264"):
                    opp_val = getattr(item, "xhtml_Br264", None)
                    
                    setattr(item, "xhtml_Br264", self)
                    

    @property
    def xhtml_Object290(self):
        return self.__xhtml_Object290

    @xhtml_Object290.setter
    def xhtml_Object290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object290", None)
        self.__xhtml_Object290 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Em291"):
                    opp_val = getattr(item, "xhtml_Em291", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Em291", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Em291"):
                    opp_val = getattr(item, "xhtml_Em291", None)
                    
                    setattr(item, "xhtml_Em291", self)
                    

    @property
    def xhtml_Object278(self):
        return self.__xhtml_Object278

    @xhtml_Object278.setter
    def xhtml_Object278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object278", None)
        self.__xhtml_Object278 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_I279"):
                    opp_val = getattr(item, "xhtml_I279", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_I279", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_I279"):
                    opp_val = getattr(item, "xhtml_I279", None)
                    
                    setattr(item, "xhtml_I279", self)
                    

    @property
    def xhtml_Object270(self):
        return self.__xhtml_Object270

    @xhtml_Object270.setter
    def xhtml_Object270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object270", None)
        self.__xhtml_Object270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object268"):
                opp_val = getattr(old_value, "xhtml_Object268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object268"):
                opp_val = getattr(value, "xhtml_Object268", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Object299(self):
        return self.__xhtml_Object299

    @xhtml_Object299.setter
    def xhtml_Object299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object299", None)
        self.__xhtml_Object299 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Code300"):
                    opp_val = getattr(item, "xhtml_Code300", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Code300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Code300"):
                    opp_val = getattr(item, "xhtml_Code300", None)
                    
                    setattr(item, "xhtml_Code300", self)
                    

    @property
    def xhtml_Object242(self):
        return self.__xhtml_Object242

    @xhtml_Object242.setter
    def xhtml_Object242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object242", None)
        self.__xhtml_Object242 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Ol243"):
                    opp_val = getattr(item, "xhtml_Ol243", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Ol243", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Ol243"):
                    opp_val = getattr(item, "xhtml_Ol243", None)
                    
                    setattr(item, "xhtml_Ol243", self)
                    

    @property
    def xhtml_Object281(self):
        return self.__xhtml_Object281

    @xhtml_Object281.setter
    def xhtml_Object281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object281", None)
        self.__xhtml_Object281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_B282"):
                    opp_val = getattr(item, "xhtml_B282", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_B282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_B282"):
                    opp_val = getattr(item, "xhtml_B282", None)
                    
                    setattr(item, "xhtml_B282", self)
                    

    @property
    def xhtml_Object296(self):
        return self.__xhtml_Object296

    @xhtml_Object296.setter
    def xhtml_Object296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object296", None)
        self.__xhtml_Object296 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dfn297"):
                    opp_val = getattr(item, "xhtml_Dfn297", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dfn297", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dfn297"):
                    opp_val = getattr(item, "xhtml_Dfn297", None)
                    
                    setattr(item, "xhtml_Dfn297", self)
                    

    @property
    def xhtml_Object320(self):
        return self.__xhtml_Object320

    @xhtml_Object320.setter
    def xhtml_Object320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object320", None)
        self.__xhtml_Object320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Acronym321"):
                    opp_val = getattr(item, "xhtml_Acronym321", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Acronym321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Acronym321"):
                    opp_val = getattr(item, "xhtml_Acronym321", None)
                    
                    setattr(item, "xhtml_Acronym321", self)
                    

    @property
    def xhtml_Object254(self):
        return self.__xhtml_Object254

    @xhtml_Object254.setter
    def xhtml_Object254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object254", None)
        self.__xhtml_Object254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Blockquote255"):
                    opp_val = getattr(item, "xhtml_Blockquote255", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Blockquote255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Blockquote255"):
                    opp_val = getattr(item, "xhtml_Blockquote255", None)
                    
                    setattr(item, "xhtml_Blockquote255", self)
                    

    @property
    def xhtml_Object311(self):
        return self.__xhtml_Object311

    @xhtml_Object311.setter
    def xhtml_Object311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object311", None)
        self.__xhtml_Object311 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Var312"):
                    opp_val = getattr(item, "xhtml_Var312", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Var312", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Var312"):
                    opp_val = getattr(item, "xhtml_Var312", None)
                    
                    setattr(item, "xhtml_Var312", self)
                    

    @property
    def xhtml_Object275(self):
        return self.__xhtml_Object275

    @xhtml_Object275.setter
    def xhtml_Object275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object275", None)
        self.__xhtml_Object275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tt276"):
                    opp_val = getattr(item, "xhtml_Tt276", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tt276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tt276"):
                    opp_val = getattr(item, "xhtml_Tt276", None)
                    
                    setattr(item, "xhtml_Tt276", self)
                    

    @property
    def xhtml_Object260(self):
        return self.__xhtml_Object260

    @xhtml_Object260.setter
    def xhtml_Object260(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object260", None)
        self.__xhtml_Object260 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_A261"):
                    opp_val = getattr(item, "xhtml_A261", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_A261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_A261"):
                    opp_val = getattr(item, "xhtml_A261", None)
                    
                    setattr(item, "xhtml_A261", self)
                    

    @property
    def xhtml_Object272(self):
        return self.__xhtml_Object272

    @xhtml_Object272.setter
    def xhtml_Object272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object272", None)
        self.__xhtml_Object272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Img273"):
                    opp_val = getattr(item, "xhtml_Img273", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Img273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Img273"):
                    opp_val = getattr(item, "xhtml_Img273", None)
                    
                    setattr(item, "xhtml_Img273", self)
                    

    @property
    def xhtml_Object251(self):
        return self.__xhtml_Object251

    @xhtml_Object251.setter
    def xhtml_Object251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object251", None)
        self.__xhtml_Object251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Hr252"):
                    opp_val = getattr(item, "xhtml_Hr252", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Hr252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Hr252"):
                    opp_val = getattr(item, "xhtml_Hr252", None)
                    
                    setattr(item, "xhtml_Hr252", self)
                    

    @property
    def xhtml_Object(self):
        return self.__xhtml_Object

    @xhtml_Object.setter
    def xhtml_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object", None)
        self.__xhtml_Object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent4"):
                opp_val = getattr(old_value, "xhtml_AContent4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent4"):
                opp_val = getattr(value, "xhtml_AContent4", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Object248(self):
        return self.__xhtml_Object248

    @xhtml_Object248.setter
    def xhtml_Object248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object248", None)
        self.__xhtml_Object248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Pre249"):
                    opp_val = getattr(item, "xhtml_Pre249", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Pre249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Pre249"):
                    opp_val = getattr(item, "xhtml_Pre249", None)
                    
                    setattr(item, "xhtml_Pre249", self)
                    

    @property
    def xhtml_Object233(self):
        return self.__xhtml_Object233

    @xhtml_Object233.setter
    def xhtml_Object233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object233", None)
        self.__xhtml_Object233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_P234"):
                    opp_val = getattr(item, "xhtml_P234", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_P234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_P234"):
                    opp_val = getattr(item, "xhtml_P234", None)
                    
                    setattr(item, "xhtml_P234", self)
                    

    @property
    def xhtml_Object314(self):
        return self.__xhtml_Object314

    @xhtml_Object314.setter
    def xhtml_Object314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object314", None)
        self.__xhtml_Object314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Cite315"):
                    opp_val = getattr(item, "xhtml_Cite315", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Cite315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Cite315"):
                    opp_val = getattr(item, "xhtml_Cite315", None)
                    
                    setattr(item, "xhtml_Cite315", self)
                    

    @property
    def xhtml_Object268(self):
        return self.__xhtml_Object268

    @xhtml_Object268.setter
    def xhtml_Object268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object268", None)
        self.__xhtml_Object268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Object270"):
                    opp_val = getattr(item, "xhtml_Object270", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Object270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Object270"):
                    opp_val = getattr(item, "xhtml_Object270", None)
                    
                    setattr(item, "xhtml_Object270", self)
                    

    @property
    def xhtml_Object245(self):
        return self.__xhtml_Object245

    @xhtml_Object245.setter
    def xhtml_Object245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Object__xhtml_Object245", None)
        self.__xhtml_Object245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dl246"):
                    opp_val = getattr(item, "xhtml_Dl246", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dl246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dl246"):
                    opp_val = getattr(item, "xhtml_Dl246", None)
                    
                    setattr(item, "xhtml_Dl246", self)
                    

class xhtml_Img:

    def __init__(self, lang: str, src: str, style: str, width: str, alt: str, class: str, height: str, hl7Id: str, imageType: str, xhtml_Img: "xhtml_AContent" = None, xhtml_Img104: "xhtml_Flow" = None, xhtml_Img161: "xhtml_Img" = None, xhtml_Img159: "xhtml_Img" = None, xhtml_Img175: "xhtml_Inline" = None, xhtml_Img273: "xhtml_Object" = None):
        self.lang = lang
        self.src = src
        self.style = style
        self.width = width
        self.alt = alt
        self.class = class
        self.height = height
        self.hl7Id = hl7Id
        self.imageType = imageType
        self.xhtml_Img = xhtml_Img
        self.xhtml_Img104 = xhtml_Img104
        self.xhtml_Img161 = xhtml_Img161
        self.xhtml_Img159 = xhtml_Img159
        self.xhtml_Img175 = xhtml_Img175
        self.xhtml_Img273 = xhtml_Img273
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def hl7Id(self) -> str:
        return self.__hl7Id

    @hl7Id.setter
    def hl7Id(self, hl7Id: str):
        self.__hl7Id = hl7Id

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def imageType(self) -> str:
        return self.__imageType

    @imageType.setter
    def imageType(self, imageType: str):
        self.__imageType = imageType

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def alt(self) -> str:
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Img161(self):
        return self.__xhtml_Img161

    @xhtml_Img161.setter
    def xhtml_Img161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Img__xhtml_Img161", None)
        self.__xhtml_Img161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Img159"):
                opp_val = getattr(old_value, "xhtml_Img159", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Img159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Img159"):
                opp_val = getattr(value, "xhtml_Img159", None)
                setattr(value, "xhtml_Img159", self)

    @property
    def xhtml_Img104(self):
        return self.__xhtml_Img104

    @xhtml_Img104.setter
    def xhtml_Img104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Img__xhtml_Img104", None)
        self.__xhtml_Img104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow103"):
                opp_val = getattr(old_value, "xhtml_Flow103", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow103"):
                opp_val = getattr(value, "xhtml_Flow103", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow103", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Img159(self):
        return self.__xhtml_Img159

    @xhtml_Img159.setter
    def xhtml_Img159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Img__xhtml_Img159", None)
        self.__xhtml_Img159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Img161"):
                opp_val = getattr(old_value, "xhtml_Img161", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Img161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Img161"):
                opp_val = getattr(value, "xhtml_Img161", None)
                setattr(value, "xhtml_Img161", self)

    @property
    def xhtml_Img175(self):
        return self.__xhtml_Img175

    @xhtml_Img175.setter
    def xhtml_Img175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Img__xhtml_Img175", None)
        self.__xhtml_Img175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline174"):
                opp_val = getattr(old_value, "xhtml_Inline174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline174"):
                opp_val = getattr(value, "xhtml_Inline174", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Img273(self):
        return self.__xhtml_Img273

    @xhtml_Img273.setter
    def xhtml_Img273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Img__xhtml_Img273", None)
        self.__xhtml_Img273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object272"):
                opp_val = getattr(old_value, "xhtml_Object272", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object272"):
                opp_val = getattr(value, "xhtml_Object272", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object272", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Img(self):
        return self.__xhtml_Img

    @xhtml_Img.setter
    def xhtml_Img(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Img__xhtml_Img", None)
        self.__xhtml_Img = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent6"):
                opp_val = getattr(old_value, "xhtml_AContent6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent6"):
                opp_val = getattr(value, "xhtml_AContent6", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Br:

    def __init__(self, class: str, style: str, xhtml_Br: "xhtml_AContent" = None, xhtml_Br95: "xhtml_Flow" = None, xhtml_Br166: "xhtml_Inline" = None, xhtml_Br264: "xhtml_Object" = None, xhtml_Br388: "xhtml_PreContent" = None):
        self.class = class
        self.style = style
        self.xhtml_Br = xhtml_Br
        self.xhtml_Br95 = xhtml_Br95
        self.xhtml_Br166 = xhtml_Br166
        self.xhtml_Br264 = xhtml_Br264
        self.xhtml_Br388 = xhtml_Br388
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Br95(self):
        return self.__xhtml_Br95

    @xhtml_Br95.setter
    def xhtml_Br95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Br__xhtml_Br95", None)
        self.__xhtml_Br95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow94"):
                opp_val = getattr(old_value, "xhtml_Flow94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow94"):
                opp_val = getattr(value, "xhtml_Flow94", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Br388(self):
        return self.__xhtml_Br388

    @xhtml_Br388.setter
    def xhtml_Br388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Br__xhtml_Br388", None)
        self.__xhtml_Br388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent387"):
                opp_val = getattr(old_value, "xhtml_PreContent387", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent387"):
                opp_val = getattr(value, "xhtml_PreContent387", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent387", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Br(self):
        return self.__xhtml_Br

    @xhtml_Br.setter
    def xhtml_Br(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Br__xhtml_Br", None)
        self.__xhtml_Br = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent"):
                opp_val = getattr(old_value, "xhtml_AContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent"):
                opp_val = getattr(value, "xhtml_AContent", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Br264(self):
        return self.__xhtml_Br264

    @xhtml_Br264.setter
    def xhtml_Br264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Br__xhtml_Br264", None)
        self.__xhtml_Br264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object263"):
                opp_val = getattr(old_value, "xhtml_Object263", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object263"):
                opp_val = getattr(value, "xhtml_Object263", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object263", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Br166(self):
        return self.__xhtml_Br166

    @xhtml_Br166.setter
    def xhtml_Br166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Br__xhtml_Br166", None)
        self.__xhtml_Br166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline165"):
                opp_val = getattr(old_value, "xhtml_Inline165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline165"):
                opp_val = getattr(value, "xhtml_Inline165", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_AContent:

    def __init__(self, mixed: str, group: str, xhtml_AContent: set["xhtml_Br"] = None, xhtml_AContent2: set["xhtml_Span"] = None, xhtml_AContent6: set["xhtml_Img"] = None, xhtml_AContent8: set["xhtml_Tt"] = None, xhtml_AContent10: set["xhtml_I"] = None, xhtml_AContent12: set["xhtml_B"] = None, xhtml_AContent14: set["xhtml_Big"] = None, xhtml_AContent16: set["xhtml_Small"] = None, xhtml_AContent4: set["xhtml_Object"] = None, xhtml_AContent18: set["xhtml_Em"] = None, xhtml_AContent20: set["xhtml_Strong"] = None, xhtml_AContent22: set["xhtml_Dfn"] = None, xhtml_AContent24: set["xhtml_Code"] = None, xhtml_AContent26: set["xhtml_Q"] = None, xhtml_AContent28: set["xhtml_Samp"] = None, xhtml_AContent30: set["xhtml_Kbd"] = None, xhtml_AContent32: set["xhtml_Var"] = None, xhtml_AContent34: set["xhtml_Cite"] = None, xhtml_AContent36: set["xhtml_Abbr"] = None, xhtml_AContent38: set["xhtml_Acronym"] = None, xhtml_AContent40: set["xhtml_Sub"] = None, xhtml_AContent42: set["xhtml_Sup"] = None):
        self.mixed = mixed
        self.group = group
        self.xhtml_AContent = xhtml_AContent if xhtml_AContent is not None else set()
        self.xhtml_AContent2 = xhtml_AContent2 if xhtml_AContent2 is not None else set()
        self.xhtml_AContent6 = xhtml_AContent6 if xhtml_AContent6 is not None else set()
        self.xhtml_AContent8 = xhtml_AContent8 if xhtml_AContent8 is not None else set()
        self.xhtml_AContent10 = xhtml_AContent10 if xhtml_AContent10 is not None else set()
        self.xhtml_AContent12 = xhtml_AContent12 if xhtml_AContent12 is not None else set()
        self.xhtml_AContent14 = xhtml_AContent14 if xhtml_AContent14 is not None else set()
        self.xhtml_AContent16 = xhtml_AContent16 if xhtml_AContent16 is not None else set()
        self.xhtml_AContent4 = xhtml_AContent4 if xhtml_AContent4 is not None else set()
        self.xhtml_AContent18 = xhtml_AContent18 if xhtml_AContent18 is not None else set()
        self.xhtml_AContent20 = xhtml_AContent20 if xhtml_AContent20 is not None else set()
        self.xhtml_AContent22 = xhtml_AContent22 if xhtml_AContent22 is not None else set()
        self.xhtml_AContent24 = xhtml_AContent24 if xhtml_AContent24 is not None else set()
        self.xhtml_AContent26 = xhtml_AContent26 if xhtml_AContent26 is not None else set()
        self.xhtml_AContent28 = xhtml_AContent28 if xhtml_AContent28 is not None else set()
        self.xhtml_AContent30 = xhtml_AContent30 if xhtml_AContent30 is not None else set()
        self.xhtml_AContent32 = xhtml_AContent32 if xhtml_AContent32 is not None else set()
        self.xhtml_AContent34 = xhtml_AContent34 if xhtml_AContent34 is not None else set()
        self.xhtml_AContent36 = xhtml_AContent36 if xhtml_AContent36 is not None else set()
        self.xhtml_AContent38 = xhtml_AContent38 if xhtml_AContent38 is not None else set()
        self.xhtml_AContent40 = xhtml_AContent40 if xhtml_AContent40 is not None else set()
        self.xhtml_AContent42 = xhtml_AContent42 if xhtml_AContent42 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def xhtml_AContent26(self):
        return self.__xhtml_AContent26

    @xhtml_AContent26.setter
    def xhtml_AContent26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent26", None)
        self.__xhtml_AContent26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Q"):
                    opp_val = getattr(item, "xhtml_Q", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Q", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Q"):
                    opp_val = getattr(item, "xhtml_Q", None)
                    
                    setattr(item, "xhtml_Q", self)
                    

    @property
    def xhtml_AContent4(self):
        return self.__xhtml_AContent4

    @xhtml_AContent4.setter
    def xhtml_AContent4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent4", None)
        self.__xhtml_AContent4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Object"):
                    opp_val = getattr(item, "xhtml_Object", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Object", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Object"):
                    opp_val = getattr(item, "xhtml_Object", None)
                    
                    setattr(item, "xhtml_Object", self)
                    

    @property
    def xhtml_AContent36(self):
        return self.__xhtml_AContent36

    @xhtml_AContent36.setter
    def xhtml_AContent36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent36", None)
        self.__xhtml_AContent36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Abbr"):
                    opp_val = getattr(item, "xhtml_Abbr", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Abbr", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Abbr"):
                    opp_val = getattr(item, "xhtml_Abbr", None)
                    
                    setattr(item, "xhtml_Abbr", self)
                    

    @property
    def xhtml_AContent22(self):
        return self.__xhtml_AContent22

    @xhtml_AContent22.setter
    def xhtml_AContent22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent22", None)
        self.__xhtml_AContent22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Dfn"):
                    opp_val = getattr(item, "xhtml_Dfn", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Dfn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Dfn"):
                    opp_val = getattr(item, "xhtml_Dfn", None)
                    
                    setattr(item, "xhtml_Dfn", self)
                    

    @property
    def xhtml_AContent12(self):
        return self.__xhtml_AContent12

    @xhtml_AContent12.setter
    def xhtml_AContent12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent12", None)
        self.__xhtml_AContent12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_B"):
                    opp_val = getattr(item, "xhtml_B", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_B"):
                    opp_val = getattr(item, "xhtml_B", None)
                    
                    setattr(item, "xhtml_B", self)
                    

    @property
    def xhtml_AContent30(self):
        return self.__xhtml_AContent30

    @xhtml_AContent30.setter
    def xhtml_AContent30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent30", None)
        self.__xhtml_AContent30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Kbd"):
                    opp_val = getattr(item, "xhtml_Kbd", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Kbd", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Kbd"):
                    opp_val = getattr(item, "xhtml_Kbd", None)
                    
                    setattr(item, "xhtml_Kbd", self)
                    

    @property
    def xhtml_AContent6(self):
        return self.__xhtml_AContent6

    @xhtml_AContent6.setter
    def xhtml_AContent6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent6", None)
        self.__xhtml_AContent6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Img"):
                    opp_val = getattr(item, "xhtml_Img", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Img", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Img"):
                    opp_val = getattr(item, "xhtml_Img", None)
                    
                    setattr(item, "xhtml_Img", self)
                    

    @property
    def xhtml_AContent42(self):
        return self.__xhtml_AContent42

    @xhtml_AContent42.setter
    def xhtml_AContent42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent42", None)
        self.__xhtml_AContent42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sup"):
                    opp_val = getattr(item, "xhtml_Sup", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sup"):
                    opp_val = getattr(item, "xhtml_Sup", None)
                    
                    setattr(item, "xhtml_Sup", self)
                    

    @property
    def xhtml_AContent10(self):
        return self.__xhtml_AContent10

    @xhtml_AContent10.setter
    def xhtml_AContent10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent10", None)
        self.__xhtml_AContent10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_I"):
                    opp_val = getattr(item, "xhtml_I", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_I", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_I"):
                    opp_val = getattr(item, "xhtml_I", None)
                    
                    setattr(item, "xhtml_I", self)
                    

    @property
    def xhtml_AContent(self):
        return self.__xhtml_AContent

    @xhtml_AContent.setter
    def xhtml_AContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent", None)
        self.__xhtml_AContent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Br"):
                    opp_val = getattr(item, "xhtml_Br", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Br", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Br"):
                    opp_val = getattr(item, "xhtml_Br", None)
                    
                    setattr(item, "xhtml_Br", self)
                    

    @property
    def xhtml_AContent20(self):
        return self.__xhtml_AContent20

    @xhtml_AContent20.setter
    def xhtml_AContent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent20", None)
        self.__xhtml_AContent20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Strong"):
                    opp_val = getattr(item, "xhtml_Strong", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Strong", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Strong"):
                    opp_val = getattr(item, "xhtml_Strong", None)
                    
                    setattr(item, "xhtml_Strong", self)
                    

    @property
    def xhtml_AContent14(self):
        return self.__xhtml_AContent14

    @xhtml_AContent14.setter
    def xhtml_AContent14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent14", None)
        self.__xhtml_AContent14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Big"):
                    opp_val = getattr(item, "xhtml_Big", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Big", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Big"):
                    opp_val = getattr(item, "xhtml_Big", None)
                    
                    setattr(item, "xhtml_Big", self)
                    

    @property
    def xhtml_AContent38(self):
        return self.__xhtml_AContent38

    @xhtml_AContent38.setter
    def xhtml_AContent38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent38", None)
        self.__xhtml_AContent38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Acronym"):
                    opp_val = getattr(item, "xhtml_Acronym", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Acronym", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Acronym"):
                    opp_val = getattr(item, "xhtml_Acronym", None)
                    
                    setattr(item, "xhtml_Acronym", self)
                    

    @property
    def xhtml_AContent40(self):
        return self.__xhtml_AContent40

    @xhtml_AContent40.setter
    def xhtml_AContent40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent40", None)
        self.__xhtml_AContent40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Sub"):
                    opp_val = getattr(item, "xhtml_Sub", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Sub", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Sub"):
                    opp_val = getattr(item, "xhtml_Sub", None)
                    
                    setattr(item, "xhtml_Sub", self)
                    

    @property
    def xhtml_AContent8(self):
        return self.__xhtml_AContent8

    @xhtml_AContent8.setter
    def xhtml_AContent8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent8", None)
        self.__xhtml_AContent8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Tt"):
                    opp_val = getattr(item, "xhtml_Tt", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Tt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Tt"):
                    opp_val = getattr(item, "xhtml_Tt", None)
                    
                    setattr(item, "xhtml_Tt", self)
                    

    @property
    def xhtml_AContent34(self):
        return self.__xhtml_AContent34

    @xhtml_AContent34.setter
    def xhtml_AContent34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent34", None)
        self.__xhtml_AContent34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Cite"):
                    opp_val = getattr(item, "xhtml_Cite", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Cite", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Cite"):
                    opp_val = getattr(item, "xhtml_Cite", None)
                    
                    setattr(item, "xhtml_Cite", self)
                    

    @property
    def xhtml_AContent32(self):
        return self.__xhtml_AContent32

    @xhtml_AContent32.setter
    def xhtml_AContent32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent32", None)
        self.__xhtml_AContent32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Var"):
                    opp_val = getattr(item, "xhtml_Var", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Var", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Var"):
                    opp_val = getattr(item, "xhtml_Var", None)
                    
                    setattr(item, "xhtml_Var", self)
                    

    @property
    def xhtml_AContent2(self):
        return self.__xhtml_AContent2

    @xhtml_AContent2.setter
    def xhtml_AContent2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent2", None)
        self.__xhtml_AContent2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Span"):
                    opp_val = getattr(item, "xhtml_Span", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Span", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Span"):
                    opp_val = getattr(item, "xhtml_Span", None)
                    
                    setattr(item, "xhtml_Span", self)
                    

    @property
    def xhtml_AContent28(self):
        return self.__xhtml_AContent28

    @xhtml_AContent28.setter
    def xhtml_AContent28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent28", None)
        self.__xhtml_AContent28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Samp"):
                    opp_val = getattr(item, "xhtml_Samp", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Samp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Samp"):
                    opp_val = getattr(item, "xhtml_Samp", None)
                    
                    setattr(item, "xhtml_Samp", self)
                    

    @property
    def xhtml_AContent18(self):
        return self.__xhtml_AContent18

    @xhtml_AContent18.setter
    def xhtml_AContent18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent18", None)
        self.__xhtml_AContent18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Em"):
                    opp_val = getattr(item, "xhtml_Em", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Em", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Em"):
                    opp_val = getattr(item, "xhtml_Em", None)
                    
                    setattr(item, "xhtml_Em", self)
                    

    @property
    def xhtml_AContent24(self):
        return self.__xhtml_AContent24

    @xhtml_AContent24.setter
    def xhtml_AContent24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent24", None)
        self.__xhtml_AContent24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Code"):
                    opp_val = getattr(item, "xhtml_Code", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Code", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Code"):
                    opp_val = getattr(item, "xhtml_Code", None)
                    
                    setattr(item, "xhtml_Code", self)
                    

    @property
    def xhtml_AContent16(self):
        return self.__xhtml_AContent16

    @xhtml_AContent16.setter
    def xhtml_AContent16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_AContent__xhtml_AContent16", None)
        self.__xhtml_AContent16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xhtml_Small"):
                    opp_val = getattr(item, "xhtml_Small", None)
                    
                    if opp_val == self:
                        setattr(item, "xhtml_Small", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xhtml_Small"):
                    opp_val = getattr(item, "xhtml_Small", None)
                    
                    setattr(item, "xhtml_Small", self)
                    

class Inline:

    pass
class xhtml_Kbd(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Kbd: "xhtml_AContent" = None, xhtml_Kbd140: "xhtml_Flow" = None, xhtml_Kbd211: "xhtml_Inline" = None, xhtml_Kbd309: "xhtml_Object" = None, xhtml_Kbd367: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Kbd = xhtml_Kbd
        self.xhtml_Kbd140 = xhtml_Kbd140
        self.xhtml_Kbd211 = xhtml_Kbd211
        self.xhtml_Kbd309 = xhtml_Kbd309
        self.xhtml_Kbd367 = xhtml_Kbd367
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Kbd140(self):
        return self.__xhtml_Kbd140

    @xhtml_Kbd140.setter
    def xhtml_Kbd140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Kbd__xhtml_Kbd140", None)
        self.__xhtml_Kbd140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow139"):
                opp_val = getattr(old_value, "xhtml_Flow139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow139"):
                opp_val = getattr(value, "xhtml_Flow139", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Kbd367(self):
        return self.__xhtml_Kbd367

    @xhtml_Kbd367.setter
    def xhtml_Kbd367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Kbd__xhtml_Kbd367", None)
        self.__xhtml_Kbd367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent366"):
                opp_val = getattr(old_value, "xhtml_PreContent366", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent366"):
                opp_val = getattr(value, "xhtml_PreContent366", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent366", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Kbd211(self):
        return self.__xhtml_Kbd211

    @xhtml_Kbd211.setter
    def xhtml_Kbd211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Kbd__xhtml_Kbd211", None)
        self.__xhtml_Kbd211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline210"):
                opp_val = getattr(old_value, "xhtml_Inline210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline210"):
                opp_val = getattr(value, "xhtml_Inline210", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Kbd309(self):
        return self.__xhtml_Kbd309

    @xhtml_Kbd309.setter
    def xhtml_Kbd309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Kbd__xhtml_Kbd309", None)
        self.__xhtml_Kbd309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object308"):
                opp_val = getattr(old_value, "xhtml_Object308", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object308"):
                opp_val = getattr(value, "xhtml_Object308", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object308", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Kbd(self):
        return self.__xhtml_Kbd

    @xhtml_Kbd.setter
    def xhtml_Kbd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Kbd__xhtml_Kbd", None)
        self.__xhtml_Kbd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent30"):
                opp_val = getattr(old_value, "xhtml_AContent30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent30"):
                opp_val = getattr(value, "xhtml_AContent30", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Tt(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Tt: "xhtml_AContent" = None, xhtml_Tt107: "xhtml_Flow" = None, xhtml_Tt178: "xhtml_Inline" = None, xhtml_Tt276: "xhtml_Object" = None, xhtml_Tt334: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Tt = xhtml_Tt
        self.xhtml_Tt107 = xhtml_Tt107
        self.xhtml_Tt178 = xhtml_Tt178
        self.xhtml_Tt276 = xhtml_Tt276
        self.xhtml_Tt334 = xhtml_Tt334
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Tt(self):
        return self.__xhtml_Tt

    @xhtml_Tt.setter
    def xhtml_Tt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tt__xhtml_Tt", None)
        self.__xhtml_Tt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent8"):
                opp_val = getattr(old_value, "xhtml_AContent8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent8"):
                opp_val = getattr(value, "xhtml_AContent8", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tt334(self):
        return self.__xhtml_Tt334

    @xhtml_Tt334.setter
    def xhtml_Tt334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tt__xhtml_Tt334", None)
        self.__xhtml_Tt334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent333"):
                opp_val = getattr(old_value, "xhtml_PreContent333", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent333"):
                opp_val = getattr(value, "xhtml_PreContent333", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent333", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tt178(self):
        return self.__xhtml_Tt178

    @xhtml_Tt178.setter
    def xhtml_Tt178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tt__xhtml_Tt178", None)
        self.__xhtml_Tt178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline177"):
                opp_val = getattr(old_value, "xhtml_Inline177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline177"):
                opp_val = getattr(value, "xhtml_Inline177", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tt107(self):
        return self.__xhtml_Tt107

    @xhtml_Tt107.setter
    def xhtml_Tt107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tt__xhtml_Tt107", None)
        self.__xhtml_Tt107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow106"):
                opp_val = getattr(old_value, "xhtml_Flow106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow106"):
                opp_val = getattr(value, "xhtml_Flow106", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Tt276(self):
        return self.__xhtml_Tt276

    @xhtml_Tt276.setter
    def xhtml_Tt276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Tt__xhtml_Tt276", None)
        self.__xhtml_Tt276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object275"):
                opp_val = getattr(old_value, "xhtml_Object275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object275"):
                opp_val = getattr(value, "xhtml_Object275", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Cite(Inline):

    def __init__(self, class: str, style: str, lang: str, xhtml_Cite: "xhtml_AContent" = None, xhtml_Cite146: "xhtml_Flow" = None, xhtml_Cite217: "xhtml_Inline" = None, xhtml_Cite315: "xhtml_Object" = None, xhtml_Cite373: "xhtml_PreContent" = None):
        self.class = class
        self.style = style
        self.lang = lang
        self.xhtml_Cite = xhtml_Cite
        self.xhtml_Cite146 = xhtml_Cite146
        self.xhtml_Cite217 = xhtml_Cite217
        self.xhtml_Cite315 = xhtml_Cite315
        self.xhtml_Cite373 = xhtml_Cite373
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Cite217(self):
        return self.__xhtml_Cite217

    @xhtml_Cite217.setter
    def xhtml_Cite217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Cite__xhtml_Cite217", None)
        self.__xhtml_Cite217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline216"):
                opp_val = getattr(old_value, "xhtml_Inline216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline216"):
                opp_val = getattr(value, "xhtml_Inline216", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Cite(self):
        return self.__xhtml_Cite

    @xhtml_Cite.setter
    def xhtml_Cite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Cite__xhtml_Cite", None)
        self.__xhtml_Cite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent34"):
                opp_val = getattr(old_value, "xhtml_AContent34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent34"):
                opp_val = getattr(value, "xhtml_AContent34", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Cite146(self):
        return self.__xhtml_Cite146

    @xhtml_Cite146.setter
    def xhtml_Cite146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Cite__xhtml_Cite146", None)
        self.__xhtml_Cite146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow145"):
                opp_val = getattr(old_value, "xhtml_Flow145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow145"):
                opp_val = getattr(value, "xhtml_Flow145", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Cite315(self):
        return self.__xhtml_Cite315

    @xhtml_Cite315.setter
    def xhtml_Cite315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Cite__xhtml_Cite315", None)
        self.__xhtml_Cite315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object314"):
                opp_val = getattr(old_value, "xhtml_Object314", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object314"):
                opp_val = getattr(value, "xhtml_Object314", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object314", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Cite373(self):
        return self.__xhtml_Cite373

    @xhtml_Cite373.setter
    def xhtml_Cite373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Cite__xhtml_Cite373", None)
        self.__xhtml_Cite373 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent372"):
                opp_val = getattr(old_value, "xhtml_PreContent372", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent372"):
                opp_val = getattr(value, "xhtml_PreContent372", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent372", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Strong(Inline):

    def __init__(self, lang: str, style: str, class: str, xhtml_Strong: "xhtml_AContent" = None, xhtml_Strong125: "xhtml_Flow" = None, xhtml_Strong196: "xhtml_Inline" = None, xhtml_Strong294: "xhtml_Object" = None, xhtml_Strong352: "xhtml_PreContent" = None):
        self.lang = lang
        self.style = style
        self.class = class
        self.xhtml_Strong = xhtml_Strong
        self.xhtml_Strong125 = xhtml_Strong125
        self.xhtml_Strong196 = xhtml_Strong196
        self.xhtml_Strong294 = xhtml_Strong294
        self.xhtml_Strong352 = xhtml_Strong352
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Strong125(self):
        return self.__xhtml_Strong125

    @xhtml_Strong125.setter
    def xhtml_Strong125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Strong__xhtml_Strong125", None)
        self.__xhtml_Strong125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow124"):
                opp_val = getattr(old_value, "xhtml_Flow124", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow124"):
                opp_val = getattr(value, "xhtml_Flow124", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow124", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Strong294(self):
        return self.__xhtml_Strong294

    @xhtml_Strong294.setter
    def xhtml_Strong294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Strong__xhtml_Strong294", None)
        self.__xhtml_Strong294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object293"):
                opp_val = getattr(old_value, "xhtml_Object293", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object293"):
                opp_val = getattr(value, "xhtml_Object293", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object293", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Strong352(self):
        return self.__xhtml_Strong352

    @xhtml_Strong352.setter
    def xhtml_Strong352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Strong__xhtml_Strong352", None)
        self.__xhtml_Strong352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent351"):
                opp_val = getattr(old_value, "xhtml_PreContent351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent351"):
                opp_val = getattr(value, "xhtml_PreContent351", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Strong(self):
        return self.__xhtml_Strong

    @xhtml_Strong.setter
    def xhtml_Strong(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Strong__xhtml_Strong", None)
        self.__xhtml_Strong = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent20"):
                opp_val = getattr(old_value, "xhtml_AContent20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent20"):
                opp_val = getattr(value, "xhtml_AContent20", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Strong196(self):
        return self.__xhtml_Strong196

    @xhtml_Strong196.setter
    def xhtml_Strong196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Strong__xhtml_Strong196", None)
        self.__xhtml_Strong196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline195"):
                opp_val = getattr(old_value, "xhtml_Inline195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline195"):
                opp_val = getattr(value, "xhtml_Inline195", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Acronym(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Acronym: "xhtml_AContent" = None, xhtml_Acronym152: "xhtml_Flow" = None, xhtml_Acronym223: "xhtml_Inline" = None, xhtml_Acronym321: "xhtml_Object" = None, xhtml_Acronym379: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Acronym = xhtml_Acronym
        self.xhtml_Acronym152 = xhtml_Acronym152
        self.xhtml_Acronym223 = xhtml_Acronym223
        self.xhtml_Acronym321 = xhtml_Acronym321
        self.xhtml_Acronym379 = xhtml_Acronym379
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Acronym(self):
        return self.__xhtml_Acronym

    @xhtml_Acronym.setter
    def xhtml_Acronym(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Acronym__xhtml_Acronym", None)
        self.__xhtml_Acronym = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent38"):
                opp_val = getattr(old_value, "xhtml_AContent38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent38"):
                opp_val = getattr(value, "xhtml_AContent38", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Acronym223(self):
        return self.__xhtml_Acronym223

    @xhtml_Acronym223.setter
    def xhtml_Acronym223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Acronym__xhtml_Acronym223", None)
        self.__xhtml_Acronym223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline222"):
                opp_val = getattr(old_value, "xhtml_Inline222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline222"):
                opp_val = getattr(value, "xhtml_Inline222", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Acronym321(self):
        return self.__xhtml_Acronym321

    @xhtml_Acronym321.setter
    def xhtml_Acronym321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Acronym__xhtml_Acronym321", None)
        self.__xhtml_Acronym321 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object320"):
                opp_val = getattr(old_value, "xhtml_Object320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object320"):
                opp_val = getattr(value, "xhtml_Object320", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Acronym379(self):
        return self.__xhtml_Acronym379

    @xhtml_Acronym379.setter
    def xhtml_Acronym379(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Acronym__xhtml_Acronym379", None)
        self.__xhtml_Acronym379 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent378"):
                opp_val = getattr(old_value, "xhtml_PreContent378", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent378"):
                opp_val = getattr(value, "xhtml_PreContent378", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent378", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Acronym152(self):
        return self.__xhtml_Acronym152

    @xhtml_Acronym152.setter
    def xhtml_Acronym152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Acronym__xhtml_Acronym152", None)
        self.__xhtml_Acronym152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow151"):
                opp_val = getattr(old_value, "xhtml_Flow151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow151"):
                opp_val = getattr(value, "xhtml_Flow151", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Small(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Small: "xhtml_AContent" = None, xhtml_Small119: "xhtml_Flow" = None, xhtml_Small190: "xhtml_Inline" = None, xhtml_Small288: "xhtml_Object" = None, xhtml_Small346: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Small = xhtml_Small
        self.xhtml_Small119 = xhtml_Small119
        self.xhtml_Small190 = xhtml_Small190
        self.xhtml_Small288 = xhtml_Small288
        self.xhtml_Small346 = xhtml_Small346
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Small288(self):
        return self.__xhtml_Small288

    @xhtml_Small288.setter
    def xhtml_Small288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Small__xhtml_Small288", None)
        self.__xhtml_Small288 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object287"):
                opp_val = getattr(old_value, "xhtml_Object287", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object287"):
                opp_val = getattr(value, "xhtml_Object287", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object287", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Small190(self):
        return self.__xhtml_Small190

    @xhtml_Small190.setter
    def xhtml_Small190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Small__xhtml_Small190", None)
        self.__xhtml_Small190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline189"):
                opp_val = getattr(old_value, "xhtml_Inline189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline189"):
                opp_val = getattr(value, "xhtml_Inline189", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Small119(self):
        return self.__xhtml_Small119

    @xhtml_Small119.setter
    def xhtml_Small119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Small__xhtml_Small119", None)
        self.__xhtml_Small119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow118"):
                opp_val = getattr(old_value, "xhtml_Flow118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow118"):
                opp_val = getattr(value, "xhtml_Flow118", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Small346(self):
        return self.__xhtml_Small346

    @xhtml_Small346.setter
    def xhtml_Small346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Small__xhtml_Small346", None)
        self.__xhtml_Small346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent345"):
                opp_val = getattr(old_value, "xhtml_PreContent345", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent345"):
                opp_val = getattr(value, "xhtml_PreContent345", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent345", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Small(self):
        return self.__xhtml_Small

    @xhtml_Small.setter
    def xhtml_Small(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Small__xhtml_Small", None)
        self.__xhtml_Small = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent16"):
                opp_val = getattr(old_value, "xhtml_AContent16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent16"):
                opp_val = getattr(value, "xhtml_AContent16", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Dt(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Dt: "xhtml_Dl" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Dt = xhtml_Dt
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Dt(self):
        return self.__xhtml_Dt

    @xhtml_Dt.setter
    def xhtml_Dt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dt__xhtml_Dt", None)
        self.__xhtml_Dt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Dl62"):
                opp_val = getattr(old_value, "xhtml_Dl62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Dl62"):
                opp_val = getattr(value, "xhtml_Dl62", None)
                if opp_val is None:
                    setattr(value, "xhtml_Dl62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Caption(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Caption: "xhtml_Table" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Caption = xhtml_Caption
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Caption(self):
        return self.__xhtml_Caption

    @xhtml_Caption.setter
    def xhtml_Caption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Caption__xhtml_Caption", None)
        self.__xhtml_Caption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Table393"):
                opp_val = getattr(old_value, "xhtml_Table393", None)
                if opp_val == self:
                    setattr(old_value, "xhtml_Table393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Table393"):
                opp_val = getattr(value, "xhtml_Table393", None)
                setattr(value, "xhtml_Table393", self)

class xhtml_Samp(Inline):

    def __init__(self, lang: str, style: str, class: str, xhtml_Samp: "xhtml_AContent" = None, xhtml_Samp137: "xhtml_Flow" = None, xhtml_Samp208: "xhtml_Inline" = None, xhtml_Samp306: "xhtml_Object" = None, xhtml_Samp364: "xhtml_PreContent" = None):
        self.lang = lang
        self.style = style
        self.class = class
        self.xhtml_Samp = xhtml_Samp
        self.xhtml_Samp137 = xhtml_Samp137
        self.xhtml_Samp208 = xhtml_Samp208
        self.xhtml_Samp306 = xhtml_Samp306
        self.xhtml_Samp364 = xhtml_Samp364
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Samp137(self):
        return self.__xhtml_Samp137

    @xhtml_Samp137.setter
    def xhtml_Samp137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Samp__xhtml_Samp137", None)
        self.__xhtml_Samp137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow136"):
                opp_val = getattr(old_value, "xhtml_Flow136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow136"):
                opp_val = getattr(value, "xhtml_Flow136", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Samp364(self):
        return self.__xhtml_Samp364

    @xhtml_Samp364.setter
    def xhtml_Samp364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Samp__xhtml_Samp364", None)
        self.__xhtml_Samp364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent363"):
                opp_val = getattr(old_value, "xhtml_PreContent363", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent363"):
                opp_val = getattr(value, "xhtml_PreContent363", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent363", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Samp208(self):
        return self.__xhtml_Samp208

    @xhtml_Samp208.setter
    def xhtml_Samp208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Samp__xhtml_Samp208", None)
        self.__xhtml_Samp208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline207"):
                opp_val = getattr(old_value, "xhtml_Inline207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline207"):
                opp_val = getattr(value, "xhtml_Inline207", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Samp(self):
        return self.__xhtml_Samp

    @xhtml_Samp.setter
    def xhtml_Samp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Samp__xhtml_Samp", None)
        self.__xhtml_Samp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent28"):
                opp_val = getattr(old_value, "xhtml_AContent28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent28"):
                opp_val = getattr(value, "xhtml_AContent28", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Samp306(self):
        return self.__xhtml_Samp306

    @xhtml_Samp306.setter
    def xhtml_Samp306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Samp__xhtml_Samp306", None)
        self.__xhtml_Samp306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object305"):
                opp_val = getattr(old_value, "xhtml_Object305", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object305"):
                opp_val = getattr(value, "xhtml_Object305", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object305", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Big(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Big: "xhtml_AContent" = None, xhtml_Big116: "xhtml_Flow" = None, xhtml_Big187: "xhtml_Inline" = None, xhtml_Big285: "xhtml_Object" = None, xhtml_Big343: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Big = xhtml_Big
        self.xhtml_Big116 = xhtml_Big116
        self.xhtml_Big187 = xhtml_Big187
        self.xhtml_Big285 = xhtml_Big285
        self.xhtml_Big343 = xhtml_Big343
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Big343(self):
        return self.__xhtml_Big343

    @xhtml_Big343.setter
    def xhtml_Big343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Big__xhtml_Big343", None)
        self.__xhtml_Big343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent342"):
                opp_val = getattr(old_value, "xhtml_PreContent342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent342"):
                opp_val = getattr(value, "xhtml_PreContent342", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Big116(self):
        return self.__xhtml_Big116

    @xhtml_Big116.setter
    def xhtml_Big116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Big__xhtml_Big116", None)
        self.__xhtml_Big116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow115"):
                opp_val = getattr(old_value, "xhtml_Flow115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow115"):
                opp_val = getattr(value, "xhtml_Flow115", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Big285(self):
        return self.__xhtml_Big285

    @xhtml_Big285.setter
    def xhtml_Big285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Big__xhtml_Big285", None)
        self.__xhtml_Big285 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object284"):
                opp_val = getattr(old_value, "xhtml_Object284", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object284"):
                opp_val = getattr(value, "xhtml_Object284", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object284", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Big187(self):
        return self.__xhtml_Big187

    @xhtml_Big187.setter
    def xhtml_Big187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Big__xhtml_Big187", None)
        self.__xhtml_Big187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline186"):
                opp_val = getattr(old_value, "xhtml_Inline186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline186"):
                opp_val = getattr(value, "xhtml_Inline186", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Big(self):
        return self.__xhtml_Big

    @xhtml_Big.setter
    def xhtml_Big(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Big__xhtml_Big", None)
        self.__xhtml_Big = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent14"):
                opp_val = getattr(old_value, "xhtml_AContent14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent14"):
                opp_val = getattr(value, "xhtml_AContent14", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Sup(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Sup: "xhtml_AContent" = None, xhtml_Sup158: "xhtml_Flow" = None, xhtml_Sup229: "xhtml_Inline" = None, xhtml_Sup327: "xhtml_Object" = None, xhtml_Sup385: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Sup = xhtml_Sup
        self.xhtml_Sup158 = xhtml_Sup158
        self.xhtml_Sup229 = xhtml_Sup229
        self.xhtml_Sup327 = xhtml_Sup327
        self.xhtml_Sup385 = xhtml_Sup385
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Sup229(self):
        return self.__xhtml_Sup229

    @xhtml_Sup229.setter
    def xhtml_Sup229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sup__xhtml_Sup229", None)
        self.__xhtml_Sup229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline228"):
                opp_val = getattr(old_value, "xhtml_Inline228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline228"):
                opp_val = getattr(value, "xhtml_Inline228", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline228", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sup(self):
        return self.__xhtml_Sup

    @xhtml_Sup.setter
    def xhtml_Sup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sup__xhtml_Sup", None)
        self.__xhtml_Sup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent42"):
                opp_val = getattr(old_value, "xhtml_AContent42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent42"):
                opp_val = getattr(value, "xhtml_AContent42", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sup327(self):
        return self.__xhtml_Sup327

    @xhtml_Sup327.setter
    def xhtml_Sup327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sup__xhtml_Sup327", None)
        self.__xhtml_Sup327 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object326"):
                opp_val = getattr(old_value, "xhtml_Object326", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object326"):
                opp_val = getattr(value, "xhtml_Object326", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object326", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sup158(self):
        return self.__xhtml_Sup158

    @xhtml_Sup158.setter
    def xhtml_Sup158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sup__xhtml_Sup158", None)
        self.__xhtml_Sup158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow157"):
                opp_val = getattr(old_value, "xhtml_Flow157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow157"):
                opp_val = getattr(value, "xhtml_Flow157", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sup385(self):
        return self.__xhtml_Sup385

    @xhtml_Sup385.setter
    def xhtml_Sup385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sup__xhtml_Sup385", None)
        self.__xhtml_Sup385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent384"):
                opp_val = getattr(old_value, "xhtml_PreContent384", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent384"):
                opp_val = getattr(value, "xhtml_PreContent384", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent384", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_I(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_I: "xhtml_AContent" = None, xhtml_I110: "xhtml_Flow" = None, xhtml_I181: "xhtml_Inline" = None, xhtml_I279: "xhtml_Object" = None, xhtml_I337: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_I = xhtml_I
        self.xhtml_I110 = xhtml_I110
        self.xhtml_I181 = xhtml_I181
        self.xhtml_I279 = xhtml_I279
        self.xhtml_I337 = xhtml_I337
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_I110(self):
        return self.__xhtml_I110

    @xhtml_I110.setter
    def xhtml_I110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_I__xhtml_I110", None)
        self.__xhtml_I110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow109"):
                opp_val = getattr(old_value, "xhtml_Flow109", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow109"):
                opp_val = getattr(value, "xhtml_Flow109", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow109", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_I337(self):
        return self.__xhtml_I337

    @xhtml_I337.setter
    def xhtml_I337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_I__xhtml_I337", None)
        self.__xhtml_I337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent336"):
                opp_val = getattr(old_value, "xhtml_PreContent336", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent336"):
                opp_val = getattr(value, "xhtml_PreContent336", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent336", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_I279(self):
        return self.__xhtml_I279

    @xhtml_I279.setter
    def xhtml_I279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_I__xhtml_I279", None)
        self.__xhtml_I279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object278"):
                opp_val = getattr(old_value, "xhtml_Object278", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object278"):
                opp_val = getattr(value, "xhtml_Object278", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object278", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_I(self):
        return self.__xhtml_I

    @xhtml_I.setter
    def xhtml_I(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_I__xhtml_I", None)
        self.__xhtml_I = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent10"):
                opp_val = getattr(old_value, "xhtml_AContent10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent10"):
                opp_val = getattr(value, "xhtml_AContent10", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_I181(self):
        return self.__xhtml_I181

    @xhtml_I181.setter
    def xhtml_I181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_I__xhtml_I181", None)
        self.__xhtml_I181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline180"):
                opp_val = getattr(old_value, "xhtml_Inline180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline180"):
                opp_val = getattr(value, "xhtml_Inline180", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Em(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Em: "xhtml_AContent" = None, xhtml_Em122: "xhtml_Flow" = None, xhtml_Em193: "xhtml_Inline" = None, xhtml_Em291: "xhtml_Object" = None, xhtml_Em349: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Em = xhtml_Em
        self.xhtml_Em122 = xhtml_Em122
        self.xhtml_Em193 = xhtml_Em193
        self.xhtml_Em291 = xhtml_Em291
        self.xhtml_Em349 = xhtml_Em349
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Em349(self):
        return self.__xhtml_Em349

    @xhtml_Em349.setter
    def xhtml_Em349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Em__xhtml_Em349", None)
        self.__xhtml_Em349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent348"):
                opp_val = getattr(old_value, "xhtml_PreContent348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent348"):
                opp_val = getattr(value, "xhtml_PreContent348", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Em122(self):
        return self.__xhtml_Em122

    @xhtml_Em122.setter
    def xhtml_Em122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Em__xhtml_Em122", None)
        self.__xhtml_Em122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow121"):
                opp_val = getattr(old_value, "xhtml_Flow121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow121"):
                opp_val = getattr(value, "xhtml_Flow121", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Em193(self):
        return self.__xhtml_Em193

    @xhtml_Em193.setter
    def xhtml_Em193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Em__xhtml_Em193", None)
        self.__xhtml_Em193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline192"):
                opp_val = getattr(old_value, "xhtml_Inline192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline192"):
                opp_val = getattr(value, "xhtml_Inline192", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Em291(self):
        return self.__xhtml_Em291

    @xhtml_Em291.setter
    def xhtml_Em291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Em__xhtml_Em291", None)
        self.__xhtml_Em291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object290"):
                opp_val = getattr(old_value, "xhtml_Object290", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object290"):
                opp_val = getattr(value, "xhtml_Object290", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object290", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Em(self):
        return self.__xhtml_Em

    @xhtml_Em.setter
    def xhtml_Em(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Em__xhtml_Em", None)
        self.__xhtml_Em = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent18"):
                opp_val = getattr(old_value, "xhtml_AContent18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent18"):
                opp_val = getattr(value, "xhtml_AContent18", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_P(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_P: "xhtml_Block" = None, xhtml_P66: "xhtml_Flow" = None, xhtml_P234: "xhtml_Object" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_P = xhtml_P
        self.xhtml_P66 = xhtml_P66
        self.xhtml_P234 = xhtml_P234
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_P66(self):
        return self.__xhtml_P66

    @xhtml_P66.setter
    def xhtml_P66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_P__xhtml_P66", None)
        self.__xhtml_P66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow"):
                opp_val = getattr(old_value, "xhtml_Flow", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow"):
                opp_val = getattr(value, "xhtml_Flow", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_P234(self):
        return self.__xhtml_P234

    @xhtml_P234.setter
    def xhtml_P234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_P__xhtml_P234", None)
        self.__xhtml_P234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object233"):
                opp_val = getattr(old_value, "xhtml_Object233", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object233"):
                opp_val = getattr(value, "xhtml_Object233", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object233", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_P(self):
        return self.__xhtml_P

    @xhtml_P.setter
    def xhtml_P(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_P__xhtml_P", None)
        self.__xhtml_P = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Block"):
                opp_val = getattr(old_value, "xhtml_Block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Block"):
                opp_val = getattr(value, "xhtml_Block", None)
                if opp_val is None:
                    setattr(value, "xhtml_Block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_B(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_B: "xhtml_AContent" = None, xhtml_B113: "xhtml_Flow" = None, xhtml_B184: "xhtml_Inline" = None, xhtml_B282: "xhtml_Object" = None, xhtml_B340: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_B = xhtml_B
        self.xhtml_B113 = xhtml_B113
        self.xhtml_B184 = xhtml_B184
        self.xhtml_B282 = xhtml_B282
        self.xhtml_B340 = xhtml_B340
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_B282(self):
        return self.__xhtml_B282

    @xhtml_B282.setter
    def xhtml_B282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_B__xhtml_B282", None)
        self.__xhtml_B282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object281"):
                opp_val = getattr(old_value, "xhtml_Object281", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object281"):
                opp_val = getattr(value, "xhtml_Object281", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object281", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_B340(self):
        return self.__xhtml_B340

    @xhtml_B340.setter
    def xhtml_B340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_B__xhtml_B340", None)
        self.__xhtml_B340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent339"):
                opp_val = getattr(old_value, "xhtml_PreContent339", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent339"):
                opp_val = getattr(value, "xhtml_PreContent339", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent339", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_B184(self):
        return self.__xhtml_B184

    @xhtml_B184.setter
    def xhtml_B184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_B__xhtml_B184", None)
        self.__xhtml_B184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline183"):
                opp_val = getattr(old_value, "xhtml_Inline183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline183"):
                opp_val = getattr(value, "xhtml_Inline183", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_B(self):
        return self.__xhtml_B

    @xhtml_B.setter
    def xhtml_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_B__xhtml_B", None)
        self.__xhtml_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent12"):
                opp_val = getattr(old_value, "xhtml_AContent12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent12"):
                opp_val = getattr(value, "xhtml_AContent12", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_B113(self):
        return self.__xhtml_B113

    @xhtml_B113.setter
    def xhtml_B113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_B__xhtml_B113", None)
        self.__xhtml_B113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow112"):
                opp_val = getattr(old_value, "xhtml_Flow112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow112"):
                opp_val = getattr(value, "xhtml_Flow112", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Dfn(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Dfn: "xhtml_AContent" = None, xhtml_Dfn128: "xhtml_Flow" = None, xhtml_Dfn199: "xhtml_Inline" = None, xhtml_Dfn297: "xhtml_Object" = None, xhtml_Dfn355: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Dfn = xhtml_Dfn
        self.xhtml_Dfn128 = xhtml_Dfn128
        self.xhtml_Dfn199 = xhtml_Dfn199
        self.xhtml_Dfn297 = xhtml_Dfn297
        self.xhtml_Dfn355 = xhtml_Dfn355
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Dfn297(self):
        return self.__xhtml_Dfn297

    @xhtml_Dfn297.setter
    def xhtml_Dfn297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dfn__xhtml_Dfn297", None)
        self.__xhtml_Dfn297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object296"):
                opp_val = getattr(old_value, "xhtml_Object296", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object296"):
                opp_val = getattr(value, "xhtml_Object296", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object296", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Dfn(self):
        return self.__xhtml_Dfn

    @xhtml_Dfn.setter
    def xhtml_Dfn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dfn__xhtml_Dfn", None)
        self.__xhtml_Dfn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent22"):
                opp_val = getattr(old_value, "xhtml_AContent22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent22"):
                opp_val = getattr(value, "xhtml_AContent22", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Dfn355(self):
        return self.__xhtml_Dfn355

    @xhtml_Dfn355.setter
    def xhtml_Dfn355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dfn__xhtml_Dfn355", None)
        self.__xhtml_Dfn355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent354"):
                opp_val = getattr(old_value, "xhtml_PreContent354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent354"):
                opp_val = getattr(value, "xhtml_PreContent354", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Dfn128(self):
        return self.__xhtml_Dfn128

    @xhtml_Dfn128.setter
    def xhtml_Dfn128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dfn__xhtml_Dfn128", None)
        self.__xhtml_Dfn128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow127"):
                opp_val = getattr(old_value, "xhtml_Flow127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow127"):
                opp_val = getattr(value, "xhtml_Flow127", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Dfn199(self):
        return self.__xhtml_Dfn199

    @xhtml_Dfn199.setter
    def xhtml_Dfn199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Dfn__xhtml_Dfn199", None)
        self.__xhtml_Dfn199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline198"):
                opp_val = getattr(old_value, "xhtml_Inline198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline198"):
                opp_val = getattr(value, "xhtml_Inline198", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Sub(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Sub: "xhtml_AContent" = None, xhtml_Sub155: "xhtml_Flow" = None, xhtml_Sub226: "xhtml_Inline" = None, xhtml_Sub324: "xhtml_Object" = None, xhtml_Sub382: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Sub = xhtml_Sub
        self.xhtml_Sub155 = xhtml_Sub155
        self.xhtml_Sub226 = xhtml_Sub226
        self.xhtml_Sub324 = xhtml_Sub324
        self.xhtml_Sub382 = xhtml_Sub382
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Sub226(self):
        return self.__xhtml_Sub226

    @xhtml_Sub226.setter
    def xhtml_Sub226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sub__xhtml_Sub226", None)
        self.__xhtml_Sub226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline225"):
                opp_val = getattr(old_value, "xhtml_Inline225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline225"):
                opp_val = getattr(value, "xhtml_Inline225", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sub(self):
        return self.__xhtml_Sub

    @xhtml_Sub.setter
    def xhtml_Sub(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sub__xhtml_Sub", None)
        self.__xhtml_Sub = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent40"):
                opp_val = getattr(old_value, "xhtml_AContent40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent40"):
                opp_val = getattr(value, "xhtml_AContent40", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sub155(self):
        return self.__xhtml_Sub155

    @xhtml_Sub155.setter
    def xhtml_Sub155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sub__xhtml_Sub155", None)
        self.__xhtml_Sub155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow154"):
                opp_val = getattr(old_value, "xhtml_Flow154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow154"):
                opp_val = getattr(value, "xhtml_Flow154", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sub382(self):
        return self.__xhtml_Sub382

    @xhtml_Sub382.setter
    def xhtml_Sub382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sub__xhtml_Sub382", None)
        self.__xhtml_Sub382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent381"):
                opp_val = getattr(old_value, "xhtml_PreContent381", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent381"):
                opp_val = getattr(value, "xhtml_PreContent381", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent381", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Sub324(self):
        return self.__xhtml_Sub324

    @xhtml_Sub324.setter
    def xhtml_Sub324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Sub__xhtml_Sub324", None)
        self.__xhtml_Sub324 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object323"):
                opp_val = getattr(old_value, "xhtml_Object323", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object323"):
                opp_val = getattr(value, "xhtml_Object323", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object323", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Span(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Span: "xhtml_AContent" = None, xhtml_Span98: "xhtml_Flow" = None, xhtml_Span169: "xhtml_Inline" = None, xhtml_Span267: "xhtml_Object" = None, xhtml_Span391: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Span = xhtml_Span
        self.xhtml_Span98 = xhtml_Span98
        self.xhtml_Span169 = xhtml_Span169
        self.xhtml_Span267 = xhtml_Span267
        self.xhtml_Span391 = xhtml_Span391
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def xhtml_Span98(self):
        return self.__xhtml_Span98

    @xhtml_Span98.setter
    def xhtml_Span98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Span__xhtml_Span98", None)
        self.__xhtml_Span98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow97"):
                opp_val = getattr(old_value, "xhtml_Flow97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow97"):
                opp_val = getattr(value, "xhtml_Flow97", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Span391(self):
        return self.__xhtml_Span391

    @xhtml_Span391.setter
    def xhtml_Span391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Span__xhtml_Span391", None)
        self.__xhtml_Span391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent390"):
                opp_val = getattr(old_value, "xhtml_PreContent390", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent390"):
                opp_val = getattr(value, "xhtml_PreContent390", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent390", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Span169(self):
        return self.__xhtml_Span169

    @xhtml_Span169.setter
    def xhtml_Span169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Span__xhtml_Span169", None)
        self.__xhtml_Span169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline168"):
                opp_val = getattr(old_value, "xhtml_Inline168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline168"):
                opp_val = getattr(value, "xhtml_Inline168", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Span(self):
        return self.__xhtml_Span

    @xhtml_Span.setter
    def xhtml_Span(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Span__xhtml_Span", None)
        self.__xhtml_Span = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent2"):
                opp_val = getattr(old_value, "xhtml_AContent2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent2"):
                opp_val = getattr(value, "xhtml_AContent2", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Span267(self):
        return self.__xhtml_Span267

    @xhtml_Span267.setter
    def xhtml_Span267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Span__xhtml_Span267", None)
        self.__xhtml_Span267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object266"):
                opp_val = getattr(old_value, "xhtml_Object266", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object266"):
                opp_val = getattr(value, "xhtml_Object266", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object266", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Var(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Var: "xhtml_AContent" = None, xhtml_Var143: "xhtml_Flow" = None, xhtml_Var214: "xhtml_Inline" = None, xhtml_Var312: "xhtml_Object" = None, xhtml_Var370: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Var = xhtml_Var
        self.xhtml_Var143 = xhtml_Var143
        self.xhtml_Var214 = xhtml_Var214
        self.xhtml_Var312 = xhtml_Var312
        self.xhtml_Var370 = xhtml_Var370
        
    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Var370(self):
        return self.__xhtml_Var370

    @xhtml_Var370.setter
    def xhtml_Var370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Var__xhtml_Var370", None)
        self.__xhtml_Var370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent369"):
                opp_val = getattr(old_value, "xhtml_PreContent369", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent369"):
                opp_val = getattr(value, "xhtml_PreContent369", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent369", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Var143(self):
        return self.__xhtml_Var143

    @xhtml_Var143.setter
    def xhtml_Var143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Var__xhtml_Var143", None)
        self.__xhtml_Var143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow142"):
                opp_val = getattr(old_value, "xhtml_Flow142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow142"):
                opp_val = getattr(value, "xhtml_Flow142", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Var(self):
        return self.__xhtml_Var

    @xhtml_Var.setter
    def xhtml_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Var__xhtml_Var", None)
        self.__xhtml_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent32"):
                opp_val = getattr(old_value, "xhtml_AContent32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent32"):
                opp_val = getattr(value, "xhtml_AContent32", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Var312(self):
        return self.__xhtml_Var312

    @xhtml_Var312.setter
    def xhtml_Var312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Var__xhtml_Var312", None)
        self.__xhtml_Var312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object311"):
                opp_val = getattr(old_value, "xhtml_Object311", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object311"):
                opp_val = getattr(value, "xhtml_Object311", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object311", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Var214(self):
        return self.__xhtml_Var214

    @xhtml_Var214.setter
    def xhtml_Var214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Var__xhtml_Var214", None)
        self.__xhtml_Var214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline213"):
                opp_val = getattr(old_value, "xhtml_Inline213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline213"):
                opp_val = getattr(value, "xhtml_Inline213", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Q(Inline):

    def __init__(self, cite1: str, class: str, lang: str, style: str, xhtml_Q: "xhtml_AContent" = None, xhtml_Q134: "xhtml_Flow" = None, xhtml_Q205: "xhtml_Inline" = None, xhtml_Q303: "xhtml_Object" = None, xhtml_Q361: "xhtml_PreContent" = None):
        self.cite1 = cite1
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Q = xhtml_Q
        self.xhtml_Q134 = xhtml_Q134
        self.xhtml_Q205 = xhtml_Q205
        self.xhtml_Q303 = xhtml_Q303
        self.xhtml_Q361 = xhtml_Q361
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def cite1(self) -> str:
        return self.__cite1

    @cite1.setter
    def cite1(self, cite1: str):
        self.__cite1 = cite1

    @property
    def xhtml_Q303(self):
        return self.__xhtml_Q303

    @xhtml_Q303.setter
    def xhtml_Q303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Q__xhtml_Q303", None)
        self.__xhtml_Q303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object302"):
                opp_val = getattr(old_value, "xhtml_Object302", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object302"):
                opp_val = getattr(value, "xhtml_Object302", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object302", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Q361(self):
        return self.__xhtml_Q361

    @xhtml_Q361.setter
    def xhtml_Q361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Q__xhtml_Q361", None)
        self.__xhtml_Q361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent360"):
                opp_val = getattr(old_value, "xhtml_PreContent360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent360"):
                opp_val = getattr(value, "xhtml_PreContent360", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Q(self):
        return self.__xhtml_Q

    @xhtml_Q.setter
    def xhtml_Q(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Q__xhtml_Q", None)
        self.__xhtml_Q = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent26"):
                opp_val = getattr(old_value, "xhtml_AContent26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent26"):
                opp_val = getattr(value, "xhtml_AContent26", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Q205(self):
        return self.__xhtml_Q205

    @xhtml_Q205.setter
    def xhtml_Q205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Q__xhtml_Q205", None)
        self.__xhtml_Q205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline204"):
                opp_val = getattr(old_value, "xhtml_Inline204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline204"):
                opp_val = getattr(value, "xhtml_Inline204", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Q134(self):
        return self.__xhtml_Q134

    @xhtml_Q134.setter
    def xhtml_Q134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Q__xhtml_Q134", None)
        self.__xhtml_Q134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow133"):
                opp_val = getattr(old_value, "xhtml_Flow133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow133"):
                opp_val = getattr(value, "xhtml_Flow133", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Code(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Code: "xhtml_AContent" = None, xhtml_Code131: "xhtml_Flow" = None, xhtml_Code202: "xhtml_Inline" = None, xhtml_Code300: "xhtml_Object" = None, xhtml_Code358: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Code = xhtml_Code
        self.xhtml_Code131 = xhtml_Code131
        self.xhtml_Code202 = xhtml_Code202
        self.xhtml_Code300 = xhtml_Code300
        self.xhtml_Code358 = xhtml_Code358
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def xhtml_Code(self):
        return self.__xhtml_Code

    @xhtml_Code.setter
    def xhtml_Code(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Code__xhtml_Code", None)
        self.__xhtml_Code = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent24"):
                opp_val = getattr(old_value, "xhtml_AContent24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent24"):
                opp_val = getattr(value, "xhtml_AContent24", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Code358(self):
        return self.__xhtml_Code358

    @xhtml_Code358.setter
    def xhtml_Code358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Code__xhtml_Code358", None)
        self.__xhtml_Code358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent357"):
                opp_val = getattr(old_value, "xhtml_PreContent357", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent357"):
                opp_val = getattr(value, "xhtml_PreContent357", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent357", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Code131(self):
        return self.__xhtml_Code131

    @xhtml_Code131.setter
    def xhtml_Code131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Code__xhtml_Code131", None)
        self.__xhtml_Code131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow130"):
                opp_val = getattr(old_value, "xhtml_Flow130", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow130"):
                opp_val = getattr(value, "xhtml_Flow130", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow130", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Code300(self):
        return self.__xhtml_Code300

    @xhtml_Code300.setter
    def xhtml_Code300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Code__xhtml_Code300", None)
        self.__xhtml_Code300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object299"):
                opp_val = getattr(old_value, "xhtml_Object299", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object299"):
                opp_val = getattr(value, "xhtml_Object299", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object299", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Code202(self):
        return self.__xhtml_Code202

    @xhtml_Code202.setter
    def xhtml_Code202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Code__xhtml_Code202", None)
        self.__xhtml_Code202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline201"):
                opp_val = getattr(old_value, "xhtml_Inline201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline201"):
                opp_val = getattr(value, "xhtml_Inline201", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class xhtml_Abbr(Inline):

    def __init__(self, class: str, lang: str, style: str, xhtml_Abbr: "xhtml_AContent" = None, xhtml_Abbr149: "xhtml_Flow" = None, xhtml_Abbr220: "xhtml_Inline" = None, xhtml_Abbr318: "xhtml_Object" = None, xhtml_Abbr376: "xhtml_PreContent" = None):
        self.class = class
        self.lang = lang
        self.style = style
        self.xhtml_Abbr = xhtml_Abbr
        self.xhtml_Abbr149 = xhtml_Abbr149
        self.xhtml_Abbr220 = xhtml_Abbr220
        self.xhtml_Abbr318 = xhtml_Abbr318
        self.xhtml_Abbr376 = xhtml_Abbr376
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def xhtml_Abbr220(self):
        return self.__xhtml_Abbr220

    @xhtml_Abbr220.setter
    def xhtml_Abbr220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Abbr__xhtml_Abbr220", None)
        self.__xhtml_Abbr220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline219"):
                opp_val = getattr(old_value, "xhtml_Inline219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline219"):
                opp_val = getattr(value, "xhtml_Inline219", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Abbr(self):
        return self.__xhtml_Abbr

    @xhtml_Abbr.setter
    def xhtml_Abbr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Abbr__xhtml_Abbr", None)
        self.__xhtml_Abbr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_AContent36"):
                opp_val = getattr(old_value, "xhtml_AContent36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_AContent36"):
                opp_val = getattr(value, "xhtml_AContent36", None)
                if opp_val is None:
                    setattr(value, "xhtml_AContent36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Abbr149(self):
        return self.__xhtml_Abbr149

    @xhtml_Abbr149.setter
    def xhtml_Abbr149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Abbr__xhtml_Abbr149", None)
        self.__xhtml_Abbr149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow148"):
                opp_val = getattr(old_value, "xhtml_Flow148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow148"):
                opp_val = getattr(value, "xhtml_Flow148", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Abbr376(self):
        return self.__xhtml_Abbr376

    @xhtml_Abbr376.setter
    def xhtml_Abbr376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Abbr__xhtml_Abbr376", None)
        self.__xhtml_Abbr376 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent375"):
                opp_val = getattr(old_value, "xhtml_PreContent375", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent375"):
                opp_val = getattr(value, "xhtml_PreContent375", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent375", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_Abbr318(self):
        return self.__xhtml_Abbr318

    @xhtml_Abbr318.setter
    def xhtml_Abbr318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_Abbr__xhtml_Abbr318", None)
        self.__xhtml_Abbr318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object317"):
                opp_val = getattr(old_value, "xhtml_Object317", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object317"):
                opp_val = getattr(value, "xhtml_Object317", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object317", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AContent:

    pass
class xhtml_A(AContent):

    def __init__(self, class: str, coords: str, href: str, lang: str, name: str, shape: str, style: str, type: str, xhtml_A: "xhtml_Flow" = None, xhtml_A163: "xhtml_Inline" = None, xhtml_A261: "xhtml_Object" = None, xhtml_A331: "xhtml_PreContent" = None):
        self.class = class
        self.coords = coords
        self.href = href
        self.lang = lang
        self.name = name
        self.shape = shape
        self.style = style
        self.type = type
        self.xhtml_A = xhtml_A
        self.xhtml_A163 = xhtml_A163
        self.xhtml_A261 = xhtml_A261
        self.xhtml_A331 = xhtml_A331
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def coords(self) -> str:
        return self.__coords

    @coords.setter
    def coords(self, coords: str):
        self.__coords = coords

    @property
    def xhtml_A261(self):
        return self.__xhtml_A261

    @xhtml_A261.setter
    def xhtml_A261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_A__xhtml_A261", None)
        self.__xhtml_A261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Object260"):
                opp_val = getattr(old_value, "xhtml_Object260", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Object260"):
                opp_val = getattr(value, "xhtml_Object260", None)
                if opp_val is None:
                    setattr(value, "xhtml_Object260", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_A163(self):
        return self.__xhtml_A163

    @xhtml_A163.setter
    def xhtml_A163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_A__xhtml_A163", None)
        self.__xhtml_A163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Inline"):
                opp_val = getattr(old_value, "xhtml_Inline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Inline"):
                opp_val = getattr(value, "xhtml_Inline", None)
                if opp_val is None:
                    setattr(value, "xhtml_Inline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_A331(self):
        return self.__xhtml_A331

    @xhtml_A331.setter
    def xhtml_A331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_A__xhtml_A331", None)
        self.__xhtml_A331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_PreContent"):
                opp_val = getattr(old_value, "xhtml_PreContent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_PreContent"):
                opp_val = getattr(value, "xhtml_PreContent", None)
                if opp_val is None:
                    setattr(value, "xhtml_PreContent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xhtml_A(self):
        return self.__xhtml_A

    @xhtml_A.setter
    def xhtml_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xhtml_A__xhtml_A", None)
        self.__xhtml_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xhtml_Flow92"):
                opp_val = getattr(old_value, "xhtml_Flow92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xhtml_Flow92"):
                opp_val = getattr(value, "xhtml_Flow92", None)
                if opp_val is None:
                    setattr(value, "xhtml_Flow92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
