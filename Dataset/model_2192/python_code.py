from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Factory:

    pass
class article_ImageFactory(Factory):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class article_TreeNodeProperty:

    def __init__(self, key: str, valueImage: str, value: str, article_TreeNodeProperty: "article_TreeNode" = None, article_TreeNodeProperty44: "article_TreeNodeProperty" = None, article_TreeNodeProperty42: set["article_TreeNodeProperty"] = None):
        self.key = key
        self.valueImage = valueImage
        self.value = value
        self.article_TreeNodeProperty = article_TreeNodeProperty
        self.article_TreeNodeProperty44 = article_TreeNodeProperty44
        self.article_TreeNodeProperty42 = article_TreeNodeProperty42 if article_TreeNodeProperty42 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def valueImage(self) -> str:
        return self.__valueImage

    @valueImage.setter
    def valueImage(self, valueImage: str):
        self.__valueImage = valueImage

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def article_TreeNodeProperty(self):
        return self.__article_TreeNodeProperty

    @article_TreeNodeProperty.setter
    def article_TreeNodeProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_TreeNodeProperty__article_TreeNodeProperty", None)
        self.__article_TreeNodeProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_TreeNode41"):
                opp_val = getattr(old_value, "article_TreeNode41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_TreeNode41"):
                opp_val = getattr(value, "article_TreeNode41", None)
                if opp_val is None:
                    setattr(value, "article_TreeNode41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def article_TreeNodeProperty42(self):
        return self.__article_TreeNodeProperty42

    @article_TreeNodeProperty42.setter
    def article_TreeNodeProperty42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_TreeNodeProperty__article_TreeNodeProperty42", None)
        self.__article_TreeNodeProperty42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "article_TreeNodeProperty44"):
                    opp_val = getattr(item, "article_TreeNodeProperty44", None)
                    
                    if opp_val == self:
                        setattr(item, "article_TreeNodeProperty44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "article_TreeNodeProperty44"):
                    opp_val = getattr(item, "article_TreeNodeProperty44", None)
                    
                    setattr(item, "article_TreeNodeProperty44", self)
                    

    @property
    def article_TreeNodeProperty44(self):
        return self.__article_TreeNodeProperty44

    @article_TreeNodeProperty44.setter
    def article_TreeNodeProperty44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_TreeNodeProperty__article_TreeNodeProperty44", None)
        self.__article_TreeNodeProperty44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_TreeNodeProperty42"):
                opp_val = getattr(old_value, "article_TreeNodeProperty42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_TreeNodeProperty42"):
                opp_val = getattr(value, "article_TreeNodeProperty42", None)
                if opp_val is None:
                    setattr(value, "article_TreeNodeProperty42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Formatter:

    pass
class article_TreeFormatter(Formatter):

    def __init__(self, expanded: str, selected: str, file: str, expandTo: int):
        self.expanded = expanded
        self.selected = selected
        self.file = file
        self.expandTo = expandTo
        
    @property
    def selected(self) -> str:
        return self.__selected

    @selected.setter
    def selected(self, selected: str):
        self.__selected = selected

    @property
    def expanded(self) -> str:
        return self.__expanded

    @expanded.setter
    def expanded(self, expanded: str):
        self.__expanded = expanded

    @property
    def expandTo(self) -> int:
        return self.__expandTo

    @expandTo.setter
    def expandTo(self, expandTo: int):
        self.__expandTo = expandTo

    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class article_HtmlFormatter(Formatter):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class article_XmlFormatter(Formatter):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class article_ImageFormatter(Formatter):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class article_JavaFormatter(Formatter):

    pass
class ExternalArticle:

    pass
class article_PluginResource(ExternalArticle):

    pass
class article_TreeNode:

    def __init__(self, xmi_ID: str, image: str, label: str, article_TreeNode: "article_TreeNode" = None, article_TreeNode38: set["article_TreeNode"] = None, article_TreeNode41: set["article_TreeNodeProperty"] = None):
        self.xmi_ID = xmi_ID
        self.image = image
        self.label = label
        self.article_TreeNode = article_TreeNode
        self.article_TreeNode38 = article_TreeNode38 if article_TreeNode38 is not None else set()
        self.article_TreeNode41 = article_TreeNode41 if article_TreeNode41 is not None else set()
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def xmi_ID(self) -> str:
        return self.__xmi_ID

    @xmi_ID.setter
    def xmi_ID(self, xmi_ID: str):
        self.__xmi_ID = xmi_ID

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def article_TreeNode(self):
        return self.__article_TreeNode

    @article_TreeNode.setter
    def article_TreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_TreeNode__article_TreeNode", None)
        self.__article_TreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_TreeNode38"):
                opp_val = getattr(old_value, "article_TreeNode38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_TreeNode38"):
                opp_val = getattr(value, "article_TreeNode38", None)
                if opp_val is None:
                    setattr(value, "article_TreeNode38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def article_TreeNode38(self):
        return self.__article_TreeNode38

    @article_TreeNode38.setter
    def article_TreeNode38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_TreeNode__article_TreeNode38", None)
        self.__article_TreeNode38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "article_TreeNode"):
                    opp_val = getattr(item, "article_TreeNode", None)
                    
                    if opp_val == self:
                        setattr(item, "article_TreeNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "article_TreeNode"):
                    opp_val = getattr(item, "article_TreeNode", None)
                    
                    setattr(item, "article_TreeNode", self)
                    

    @property
    def article_TreeNode41(self):
        return self.__article_TreeNode41

    @article_TreeNode41.setter
    def article_TreeNode41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_TreeNode__article_TreeNode41", None)
        self.__article_TreeNode41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "article_TreeNodeProperty"):
                    opp_val = getattr(item, "article_TreeNodeProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "article_TreeNodeProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "article_TreeNodeProperty"):
                    opp_val = getattr(item, "article_TreeNodeProperty", None)
                    
                    setattr(item, "article_TreeNodeProperty", self)
                    

class Article:

    pass
class article_ExternalArticle(Article):

    def __init__(self, url: str):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class Category:

    pass
class article_Javadoc(Category):

    pass
class article_ExtensionPoint:

    def __init__(self, name: str, extensionPoints: "article_Plugin" = None, ExtensionPoint: "article_Plugin" = None):
        self.name = name
        self.extensionPoints = extensionPoints
        self.ExtensionPoint = ExtensionPoint
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ExtensionPoint(self):
        return self.__ExtensionPoint

    @ExtensionPoint.setter
    def ExtensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_ExtensionPoint__ExtensionPoint", None)
        self.__ExtensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plugin32"):
                opp_val = getattr(old_value, "plugin32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plugin32"):
                opp_val = getattr(value, "plugin32", None)
                if opp_val is None:
                    setattr(value, "plugin32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extensionPoints(self):
        return self.__extensionPoints

    @extensionPoints.setter
    def extensionPoints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_ExtensionPoint__extensionPoints", None)
        self.__extensionPoints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Plugin35"):
                opp_val = getattr(old_value, "Plugin35", None)
                if opp_val == self:
                    setattr(old_value, "Plugin35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Plugin35"):
                opp_val = getattr(value, "Plugin35", None)
                setattr(value, "Plugin35", self)

class article_Schemadoc(Category):

    pass
class article_BodyElement(ABC):

    def __init__(self, tag: str, BodyElement: "article_BodyElementContainer" = None, elements: "article_BodyElementContainer" = None):
        self.tag = tag
        self.BodyElement = BodyElement
        self.elements = elements
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_BodyElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BodyElementContainer"):
                opp_val = getattr(old_value, "BodyElementContainer", None)
                if opp_val == self:
                    setattr(old_value, "BodyElementContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BodyElementContainer"):
                opp_val = getattr(value, "BodyElementContainer", None)
                setattr(value, "BodyElementContainer", self)

    @property
    def BodyElement(self):
        return self.__BodyElement

    @BodyElement.setter
    def BodyElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_BodyElement__BodyElement", None)
        self.__BodyElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class article_BodyElementContainer(ABC):

    pass
class article_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class article_JavaPackage:

    def __init__(self, name: str, JavaPackage: "article_Plugin" = None, packages: "article_Plugin" = None):
        self.name = name
        self.JavaPackage = JavaPackage
        self.packages = packages
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def JavaPackage(self):
        return self.__JavaPackage

    @JavaPackage.setter
    def JavaPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_JavaPackage__JavaPackage", None)
        self.__JavaPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plugin"):
                opp_val = getattr(old_value, "plugin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plugin"):
                opp_val = getattr(value, "plugin", None)
                if opp_val is None:
                    setattr(value, "plugin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def packages(self):
        return self.__packages

    @packages.setter
    def packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_JavaPackage__packages", None)
        self.__packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Plugin"):
                opp_val = getattr(old_value, "Plugin", None)
                if opp_val == self:
                    setattr(old_value, "Plugin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Plugin"):
                opp_val = getattr(value, "Plugin", None)
                setattr(value, "Plugin", self)

class ExternalTarget:

    pass
class article_SourceCode(ExternalTarget):

    pass
class LinkTarget:

    pass
class article_ExternalTarget(LinkTarget):

    def __init__(self, url: str):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class article_StructuralElement(LinkTarget):

    def __init__(self, doc: str, title: str, StructuralElement: "article_StructuralElement" = None, parent: set["article_StructuralElement"] = None, StructuralElement18: "article_StructuralElement" = None, children: "article_StructuralElement" = None, article_StructuralElement: "article_Documentation" = None):
        self.doc = doc
        self.title = title
        self.StructuralElement = StructuralElement
        self.parent = parent if parent is not None else set()
        self.StructuralElement18 = StructuralElement18
        self.children = children
        self.article_StructuralElement = article_StructuralElement
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def article_StructuralElement(self):
        return self.__article_StructuralElement

    @article_StructuralElement.setter
    def article_StructuralElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_StructuralElement__article_StructuralElement", None)
        self.__article_StructuralElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_Documentation20"):
                opp_val = getattr(old_value, "article_Documentation20", None)
                if opp_val == self:
                    setattr(old_value, "article_Documentation20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_Documentation20"):
                opp_val = getattr(value, "article_Documentation20", None)
                setattr(value, "article_Documentation20", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_StructuralElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StructuralElement"):
                    opp_val = getattr(item, "StructuralElement", None)
                    
                    if opp_val == self:
                        setattr(item, "StructuralElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StructuralElement"):
                    opp_val = getattr(item, "StructuralElement", None)
                    
                    setattr(item, "StructuralElement", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_StructuralElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StructuralElement18"):
                opp_val = getattr(old_value, "StructuralElement18", None)
                if opp_val == self:
                    setattr(old_value, "StructuralElement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StructuralElement18"):
                opp_val = getattr(value, "StructuralElement18", None)
                setattr(value, "StructuralElement18", self)

    @property
    def StructuralElement(self):
        return self.__StructuralElement

    @StructuralElement.setter
    def StructuralElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_StructuralElement__StructuralElement", None)
        self.__StructuralElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StructuralElement18(self):
        return self.__StructuralElement18

    @StructuralElement18.setter
    def StructuralElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_StructuralElement__StructuralElement18", None)
        self.__StructuralElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

class article_JavaElement(LinkTarget):

    def __init__(self, classFile: str):
        self.classFile = classFile
        
    @property
    def classFile(self) -> str:
        return self.__classFile

    @classFile.setter
    def classFile(self, classFile: str):
        self.__classFile = classFile

class BodyElement:

    pass
class article_Key(BodyElement):

    pass
class article_Selection(BodyElement):

    pass
class article_Toc(BodyElement):

    def __init__(self, levels: int):
        self.levels = levels
        
    @property
    def levels(self) -> int:
        return self.__levels

    @levels.setter
    def levels(self, levels: int):
        self.__levels = levels

class article_Link(BodyElement):

    pass
class article_Image(BodyElement):

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class article_Text(BodyElement):

    pass
class article_Excel(BodyElement):

    pass
class article_Embedding(BodyElement):

    pass
class article_Diagram(BodyElement):

    pass
class article_Formatter(ABC):

    pass
class EmbeddableElement:

    pass
class article_Factory(EmbeddableElement):

    pass
class article_Snippet(EmbeddableElement):

    def __init__(self, title: str, titleImage: str, Snippet: "article_Callout" = None, snippet: set["article_Callout"] = None, snippet11: "article_Formatter" = None, snippet13: "article_Description" = None, Snippet37: "article_Formatter" = None, Snippet46: "article_Description" = None):
        self.title = title
        self.titleImage = titleImage
        self.Snippet = Snippet
        self.snippet = snippet if snippet is not None else set()
        self.snippet11 = snippet11
        self.snippet13 = snippet13
        self.Snippet37 = Snippet37
        self.Snippet46 = Snippet46
        
    @property
    def titleImage(self) -> str:
        return self.__titleImage

    @titleImage.setter
    def titleImage(self, titleImage: str):
        self.__titleImage = titleImage

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Snippet46(self):
        return self.__Snippet46

    @Snippet46.setter
    def Snippet46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Snippet__Snippet46", None)
        self.__Snippet46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description"):
                opp_val = getattr(old_value, "description", None)
                if opp_val == self:
                    setattr(old_value, "description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description"):
                opp_val = getattr(value, "description", None)
                setattr(value, "description", self)

    @property
    def snippet(self):
        return self.__snippet

    @snippet.setter
    def snippet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Snippet__snippet", None)
        self.__snippet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Callout"):
                    opp_val = getattr(item, "Callout", None)
                    
                    if opp_val == self:
                        setattr(item, "Callout", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Callout"):
                    opp_val = getattr(item, "Callout", None)
                    
                    setattr(item, "Callout", self)
                    

    @property
    def snippet11(self):
        return self.__snippet11

    @snippet11.setter
    def snippet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Snippet__snippet11", None)
        self.__snippet11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Formatter"):
                opp_val = getattr(old_value, "Formatter", None)
                if opp_val == self:
                    setattr(old_value, "Formatter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Formatter"):
                opp_val = getattr(value, "Formatter", None)
                setattr(value, "Formatter", self)

    @property
    def Snippet37(self):
        return self.__Snippet37

    @Snippet37.setter
    def Snippet37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Snippet__Snippet37", None)
        self.__Snippet37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formatter"):
                opp_val = getattr(old_value, "formatter", None)
                if opp_val == self:
                    setattr(old_value, "formatter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formatter"):
                opp_val = getattr(value, "formatter", None)
                setattr(value, "formatter", self)

    @property
    def snippet13(self):
        return self.__snippet13

    @snippet13.setter
    def snippet13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Snippet__snippet13", None)
        self.__snippet13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Description"):
                opp_val = getattr(old_value, "Description", None)
                if opp_val == self:
                    setattr(old_value, "Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Description"):
                opp_val = getattr(value, "Description", None)
                setattr(value, "Description", self)

    @property
    def Snippet(self):
        return self.__Snippet

    @Snippet.setter
    def Snippet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Snippet__Snippet", None)
        self.__Snippet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "callouts"):
                opp_val = getattr(old_value, "callouts", None)
                if opp_val == self:
                    setattr(old_value, "callouts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "callouts"):
                opp_val = getattr(value, "callouts", None)
                setattr(value, "callouts", self)

class BodyElementContainer:

    pass
class article_Description(BodyElementContainer):

    pass
class article_Callout(BodyElementContainer):

    pass
class Identifiable:

    pass
class article_LinkTarget(Identifiable):

    def __init__(self, defaultLabel: str, tooltip: str, article_LinkTarget: "article_Link" = None):
        self.defaultLabel = defaultLabel
        self.tooltip = tooltip
        self.article_LinkTarget = article_LinkTarget
        
    @property
    def defaultLabel(self) -> str:
        return self.__defaultLabel

    @defaultLabel.setter
    def defaultLabel(self, defaultLabel: str):
        self.__defaultLabel = defaultLabel

    @property
    def tooltip(self) -> str:
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, tooltip: str):
        self.__tooltip = tooltip

    @property
    def article_LinkTarget(self):
        return self.__article_LinkTarget

    @article_LinkTarget.setter
    def article_LinkTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_LinkTarget__article_LinkTarget", None)
        self.__article_LinkTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_Link"):
                opp_val = getattr(old_value, "article_Link", None)
                if opp_val == self:
                    setattr(old_value, "article_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_Link"):
                opp_val = getattr(value, "article_Link", None)
                setattr(value, "article_Link", self)

    def linkFrom(self, source: StructuralElement) -> str:
        # TODO: Implement linkFrom method
        pass

class article_Section(BodyElementContainer, LinkTarget):

    pass
class Chapter:

    pass
class article_Article(Chapter):

    pass
class Body:

    pass
class article_Chapter(Body):

    pass
class article_Category(Body):

    pass
class article_EmbeddableElement(Identifiable):

    def __init__(self, doc: str, EmbeddableElement: "article_Documentation" = None, embeddableElements: "article_Documentation" = None, article_EmbeddableElement: "article_Embedding" = None):
        self.doc = doc
        self.EmbeddableElement = EmbeddableElement
        self.embeddableElements = embeddableElements
        self.article_EmbeddableElement = article_EmbeddableElement
        
    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def embeddableElements(self):
        return self.__embeddableElements

    @embeddableElements.setter
    def embeddableElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_EmbeddableElement__embeddableElements", None)
        self.__embeddableElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Documentation23"):
                opp_val = getattr(old_value, "Documentation23", None)
                if opp_val == self:
                    setattr(old_value, "Documentation23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Documentation23"):
                opp_val = getattr(value, "Documentation23", None)
                setattr(value, "Documentation23", self)

    @property
    def article_EmbeddableElement(self):
        return self.__article_EmbeddableElement

    @article_EmbeddableElement.setter
    def article_EmbeddableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_EmbeddableElement__article_EmbeddableElement", None)
        self.__article_EmbeddableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_Embedding"):
                opp_val = getattr(old_value, "article_Embedding", None)
                if opp_val == self:
                    setattr(old_value, "article_Embedding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_Embedding"):
                opp_val = getattr(value, "article_Embedding", None)
                setattr(value, "article_Embedding", self)

    @property
    def EmbeddableElement(self):
        return self.__EmbeddableElement

    @EmbeddableElement.setter
    def EmbeddableElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_EmbeddableElement__EmbeddableElement", None)
        self.__EmbeddableElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentation"):
                opp_val = getattr(old_value, "documentation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentation"):
                opp_val = getattr(value, "documentation", None)
                if opp_val is None:
                    setattr(value, "documentation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class article_Context:

    def __init__(self, baseFolder: str, project: str, root: str, Context: "article_Documentation" = None, context: set["article_Documentation"] = None):
        self.baseFolder = baseFolder
        self.project = project
        self.root = root
        self.Context = Context
        self.context = context if context is not None else set()
        
    @property
    def baseFolder(self) -> str:
        return self.__baseFolder

    @baseFolder.setter
    def baseFolder(self, baseFolder: str):
        self.__baseFolder = baseFolder

    @property
    def root(self) -> str:
        return self.__root

    @root.setter
    def root(self, root: str):
        self.__root = root

    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def Context(self):
        return self.__Context

    @Context.setter
    def Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Context__Context", None)
        self.__Context = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documentations"):
                opp_val = getattr(old_value, "documentations", None)
                if opp_val == self:
                    setattr(old_value, "documentations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documentations"):
                opp_val = getattr(value, "documentations", None)
                setattr(value, "documentations", self)

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Context__context", None)
        self.__context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Documentation"):
                    opp_val = getattr(item, "Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Documentation"):
                    opp_val = getattr(item, "Documentation", None)
                    
                    setattr(item, "Documentation", self)
                    

class StructuralElement:

    pass
class article_Body(BodyElementContainer, StructuralElement):

    pass
class article_Documentation(StructuralElement):

    def __init__(self, project: str, article_Documentation: "article_Documentation" = None, article_Documentation2: set["article_Documentation"] = None, article_Documentation5: set["article_Plugin"] = None, documentations: "article_Context" = None, documentation: set["article_EmbeddableElement"] = None, Documentation: "article_Context" = None, Documentation23: "article_EmbeddableElement" = None, article_Documentation20: "article_StructuralElement" = None):
        self.project = project
        self.article_Documentation = article_Documentation
        self.article_Documentation2 = article_Documentation2 if article_Documentation2 is not None else set()
        self.article_Documentation5 = article_Documentation5 if article_Documentation5 is not None else set()
        self.documentations = documentations
        self.documentation = documentation if documentation is not None else set()
        self.Documentation = Documentation
        self.Documentation23 = Documentation23
        self.article_Documentation20 = article_Documentation20
        
    @property
    def project(self) -> str:
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project

    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__documentation", None)
        self.__documentation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmbeddableElement"):
                    opp_val = getattr(item, "EmbeddableElement", None)
                    
                    if opp_val == self:
                        setattr(item, "EmbeddableElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmbeddableElement"):
                    opp_val = getattr(item, "EmbeddableElement", None)
                    
                    setattr(item, "EmbeddableElement", self)
                    

    @property
    def documentations(self):
        return self.__documentations

    @documentations.setter
    def documentations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__documentations", None)
        self.__documentations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Context"):
                opp_val = getattr(old_value, "Context", None)
                if opp_val == self:
                    setattr(old_value, "Context", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Context"):
                opp_val = getattr(value, "Context", None)
                setattr(value, "Context", self)

    @property
    def article_Documentation5(self):
        return self.__article_Documentation5

    @article_Documentation5.setter
    def article_Documentation5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__article_Documentation5", None)
        self.__article_Documentation5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "article_Plugin"):
                    opp_val = getattr(item, "article_Plugin", None)
                    
                    if opp_val == self:
                        setattr(item, "article_Plugin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "article_Plugin"):
                    opp_val = getattr(item, "article_Plugin", None)
                    
                    setattr(item, "article_Plugin", self)
                    

    @property
    def article_Documentation2(self):
        return self.__article_Documentation2

    @article_Documentation2.setter
    def article_Documentation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__article_Documentation2", None)
        self.__article_Documentation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "article_Documentation"):
                    opp_val = getattr(item, "article_Documentation", None)
                    
                    if opp_val == self:
                        setattr(item, "article_Documentation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "article_Documentation"):
                    opp_val = getattr(item, "article_Documentation", None)
                    
                    setattr(item, "article_Documentation", self)
                    

    @property
    def Documentation(self):
        return self.__Documentation

    @Documentation.setter
    def Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__Documentation", None)
        self.__Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "context"):
                opp_val = getattr(old_value, "context", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "context"):
                opp_val = getattr(value, "context", None)
                if opp_val is None:
                    setattr(value, "context", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Documentation23(self):
        return self.__Documentation23

    @Documentation23.setter
    def Documentation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__Documentation23", None)
        self.__Documentation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "embeddableElements"):
                opp_val = getattr(old_value, "embeddableElements", None)
                if opp_val == self:
                    setattr(old_value, "embeddableElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "embeddableElements"):
                opp_val = getattr(value, "embeddableElements", None)
                setattr(value, "embeddableElements", self)

    @property
    def article_Documentation(self):
        return self.__article_Documentation

    @article_Documentation.setter
    def article_Documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__article_Documentation", None)
        self.__article_Documentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_Documentation2"):
                opp_val = getattr(old_value, "article_Documentation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_Documentation2"):
                opp_val = getattr(value, "article_Documentation2", None)
                if opp_val is None:
                    setattr(value, "article_Documentation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def article_Documentation20(self):
        return self.__article_Documentation20

    @article_Documentation20.setter
    def article_Documentation20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Documentation__article_Documentation20", None)
        self.__article_Documentation20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_StructuralElement"):
                opp_val = getattr(old_value, "article_StructuralElement", None)
                if opp_val == self:
                    setattr(old_value, "article_StructuralElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_StructuralElement"):
                opp_val = getattr(value, "article_StructuralElement", None)
                setattr(value, "article_StructuralElement", self)

class article_Plugin:

    def __init__(self, name: str, label: str, article_Plugin: "article_Documentation" = None, plugin: set["article_JavaPackage"] = None, Plugin35: "article_ExtensionPoint" = None, plugin32: set["article_ExtensionPoint"] = None, Plugin: "article_JavaPackage" = None):
        self.name = name
        self.label = label
        self.article_Plugin = article_Plugin
        self.plugin = plugin if plugin is not None else set()
        self.Plugin35 = Plugin35
        self.plugin32 = plugin32 if plugin32 is not None else set()
        self.Plugin = Plugin
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def plugin(self):
        return self.__plugin

    @plugin.setter
    def plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Plugin__plugin", None)
        self.__plugin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaPackage"):
                    opp_val = getattr(item, "JavaPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaPackage"):
                    opp_val = getattr(item, "JavaPackage", None)
                    
                    setattr(item, "JavaPackage", self)
                    

    @property
    def plugin32(self):
        return self.__plugin32

    @plugin32.setter
    def plugin32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Plugin__plugin32", None)
        self.__plugin32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionPoint"):
                    opp_val = getattr(item, "ExtensionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionPoint"):
                    opp_val = getattr(item, "ExtensionPoint", None)
                    
                    setattr(item, "ExtensionPoint", self)
                    

    @property
    def Plugin(self):
        return self.__Plugin

    @Plugin.setter
    def Plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Plugin__Plugin", None)
        self.__Plugin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "packages"):
                opp_val = getattr(old_value, "packages", None)
                if opp_val == self:
                    setattr(old_value, "packages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "packages"):
                opp_val = getattr(value, "packages", None)
                setattr(value, "packages", self)

    @property
    def article_Plugin(self):
        return self.__article_Plugin

    @article_Plugin.setter
    def article_Plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Plugin__article_Plugin", None)
        self.__article_Plugin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "article_Documentation5"):
                opp_val = getattr(old_value, "article_Documentation5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "article_Documentation5"):
                opp_val = getattr(value, "article_Documentation5", None)
                if opp_val is None:
                    setattr(value, "article_Documentation5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Plugin35(self):
        return self.__Plugin35

    @Plugin35.setter
    def Plugin35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_article_Plugin__Plugin35", None)
        self.__Plugin35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensionPoints"):
                opp_val = getattr(old_value, "extensionPoints", None)
                if opp_val == self:
                    setattr(old_value, "extensionPoints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensionPoints"):
                opp_val = getattr(value, "extensionPoints", None)
                setattr(value, "extensionPoints", self)
