from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RuleResult(Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
class NumberingStyle(Enum):
    ARABIC = "ARABIC"
    ROMAN = "ROMAN"
    LATIN = "LATIN"


############################################
# Definition of Classes
############################################

class doc_builder_PropertyEntry:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class builder_PropertyEntry:

    pass
class doc_book_BookContainer(ABC):

    def __init__(self, numberingStyle: str, doc_book_BookContainer: set["Content"] = None, doc_book_BookContainer15: set["BookSection"] = None):
        self.numberingStyle = numberingStyle
        self.doc_book_BookContainer = doc_book_BookContainer if doc_book_BookContainer is not None else set()
        self.doc_book_BookContainer15 = doc_book_BookContainer15 if doc_book_BookContainer15 is not None else set()
        
    @property
    def numberingStyle(self) -> str:
        return self.__numberingStyle

    @numberingStyle.setter
    def numberingStyle(self, numberingStyle: str):
        self.__numberingStyle = numberingStyle

    @property
    def doc_book_BookContainer15(self):
        return self.__doc_book_BookContainer15

    @doc_book_BookContainer15.setter
    def doc_book_BookContainer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_book_BookContainer__doc_book_BookContainer15", None)
        self.__doc_book_BookContainer15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BookSection"):
                    opp_val = getattr(item, "BookSection", None)
                    
                    if opp_val == self:
                        setattr(item, "BookSection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BookSection"):
                    opp_val = getattr(item, "BookSection", None)
                    
                    setattr(item, "BookSection", self)
                    

    @property
    def doc_book_BookContainer(self):
        return self.__doc_book_BookContainer

    @doc_book_BookContainer.setter
    def doc_book_BookContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_book_BookContainer__doc_book_BookContainer", None)
        self.__doc_book_BookContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Content13"):
                    opp_val = getattr(item, "Content13", None)
                    
                    if opp_val == self:
                        setattr(item, "Content13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Content13"):
                    opp_val = getattr(item, "Content13", None)
                    
                    setattr(item, "Content13", self)
                    

class Map:

    pass
class doc_builder_BookBuilder(Map):

    def __init__(self, title: str, version: str, license: str, copyrightMarker: str, doc_builder_BookBuilder: set["Author"] = None, doc_builder_BookBuilder19: set["Copyright"] = None, doc_builder_BookBuilder22: set["builder_PropertyEntry"] = None):
        self.title = title
        self.version = version
        self.license = license
        self.copyrightMarker = copyrightMarker
        self.doc_builder_BookBuilder = doc_builder_BookBuilder if doc_builder_BookBuilder is not None else set()
        self.doc_builder_BookBuilder19 = doc_builder_BookBuilder19 if doc_builder_BookBuilder19 is not None else set()
        self.doc_builder_BookBuilder22 = doc_builder_BookBuilder22 if doc_builder_BookBuilder22 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def license(self) -> str:
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license

    @property
    def copyrightMarker(self) -> str:
        return self.__copyrightMarker

    @copyrightMarker.setter
    def copyrightMarker(self, copyrightMarker: str):
        self.__copyrightMarker = copyrightMarker

    @property
    def doc_builder_BookBuilder(self):
        return self.__doc_builder_BookBuilder

    @doc_builder_BookBuilder.setter
    def doc_builder_BookBuilder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_builder_BookBuilder__doc_builder_BookBuilder", None)
        self.__doc_builder_BookBuilder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author17"):
                    opp_val = getattr(item, "Author17", None)
                    
                    if opp_val == self:
                        setattr(item, "Author17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author17"):
                    opp_val = getattr(item, "Author17", None)
                    
                    setattr(item, "Author17", self)
                    

    @property
    def doc_builder_BookBuilder19(self):
        return self.__doc_builder_BookBuilder19

    @doc_builder_BookBuilder19.setter
    def doc_builder_BookBuilder19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_builder_BookBuilder__doc_builder_BookBuilder19", None)
        self.__doc_builder_BookBuilder19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Copyright20"):
                    opp_val = getattr(item, "Copyright20", None)
                    
                    if opp_val == self:
                        setattr(item, "Copyright20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Copyright20"):
                    opp_val = getattr(item, "Copyright20", None)
                    
                    setattr(item, "Copyright20", self)
                    

    @property
    def doc_builder_BookBuilder22(self):
        return self.__doc_builder_BookBuilder22

    @doc_builder_BookBuilder22.setter
    def doc_builder_BookBuilder22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_builder_BookBuilder__doc_builder_BookBuilder22", None)
        self.__doc_builder_BookBuilder22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "builder_PropertyEntry"):
                    opp_val = getattr(item, "builder_PropertyEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "builder_PropertyEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "builder_PropertyEntry"):
                    opp_val = getattr(item, "builder_PropertyEntry", None)
                    
                    setattr(item, "builder_PropertyEntry", self)
                    

class BookSection:

    pass
class doc_fragment_Author:

    def __init__(self, name: str, ref: str, id: str):
        self.name = name
        self.ref = ref
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class doc_fragment_Content(ABC):

    pass
class Copyright:

    pass
class BookContainer:

    pass
class doc_book_BookSection(BookContainer):

    def __init__(self, id: str, number: int, fullNumber: str, title: str):
        self.id = id
        self.number = number
        self.fullNumber = fullNumber
        self.title = title
        
    @property
    def fullNumber(self) -> str:
        return self.__fullNumber

    @fullNumber.setter
    def fullNumber(self, fullNumber: str):
        self.__fullNumber = fullNumber

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class doc_book_Book(BookContainer):

    def __init__(self, title: str, version: str, copyrightMarker: str, copyrightText: str, doc_book_Book: set["Author"] = None, doc_book_Book11: set["Copyright"] = None):
        self.title = title
        self.version = version
        self.copyrightMarker = copyrightMarker
        self.copyrightText = copyrightText
        self.doc_book_Book = doc_book_Book if doc_book_Book is not None else set()
        self.doc_book_Book11 = doc_book_Book11 if doc_book_Book11 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def copyrightMarker(self) -> str:
        return self.__copyrightMarker

    @copyrightMarker.setter
    def copyrightMarker(self, copyrightMarker: str):
        self.__copyrightMarker = copyrightMarker

    @property
    def copyrightText(self) -> str:
        return self.__copyrightText

    @copyrightText.setter
    def copyrightText(self, copyrightText: str):
        self.__copyrightText = copyrightText

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def doc_book_Book(self):
        return self.__doc_book_Book

    @doc_book_Book.setter
    def doc_book_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_book_Book__doc_book_Book", None)
        self.__doc_book_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author9"):
                    opp_val = getattr(item, "Author9", None)
                    
                    if opp_val == self:
                        setattr(item, "Author9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author9"):
                    opp_val = getattr(item, "Author9", None)
                    
                    setattr(item, "Author9", self)
                    

    @property
    def doc_book_Book11(self):
        return self.__doc_book_Book11

    @doc_book_Book11.setter
    def doc_book_Book11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_book_Book__doc_book_Book11", None)
        self.__doc_book_Book11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Copyright"):
                    opp_val = getattr(item, "Copyright", None)
                    
                    if opp_val == self:
                        setattr(item, "Copyright", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Copyright"):
                    opp_val = getattr(item, "Copyright", None)
                    
                    setattr(item, "Copyright", self)
                    

class Author:

    pass
class doc_fragment_Copyright:

    def __init__(self, year: int, doc_fragment_Copyright: set["Author"] = None):
        self.year = year
        self.doc_fragment_Copyright = doc_fragment_Copyright if doc_fragment_Copyright is not None else set()
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def doc_fragment_Copyright(self):
        return self.__doc_fragment_Copyright

    @doc_fragment_Copyright.setter
    def doc_fragment_Copyright(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_fragment_Copyright__doc_fragment_Copyright", None)
        self.__doc_fragment_Copyright = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    setattr(item, "Author", self)
                    

class doc_fragment_Container(ABC):

    def __init__(self, content: str, doc_fragment_Container: set["Content"] = None, doc_fragment_Container6: set["Section"] = None):
        self.content = content
        self.doc_fragment_Container = doc_fragment_Container if doc_fragment_Container is not None else set()
        self.doc_fragment_Container6 = doc_fragment_Container6 if doc_fragment_Container6 is not None else set()
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def doc_fragment_Container6(self):
        return self.__doc_fragment_Container6

    @doc_fragment_Container6.setter
    def doc_fragment_Container6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_fragment_Container__doc_fragment_Container6", None)
        self.__doc_fragment_Container6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Section"):
                    opp_val = getattr(item, "Section", None)
                    
                    if opp_val == self:
                        setattr(item, "Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Section"):
                    opp_val = getattr(item, "Section", None)
                    
                    setattr(item, "Section", self)
                    

    @property
    def doc_fragment_Container(self):
        return self.__doc_fragment_Container

    @doc_fragment_Container.setter
    def doc_fragment_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_fragment_Container__doc_fragment_Container", None)
        self.__doc_fragment_Container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Content"):
                    opp_val = getattr(item, "Content", None)
                    
                    if opp_val == self:
                        setattr(item, "Content", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Content"):
                    opp_val = getattr(item, "Content", None)
                    
                    setattr(item, "Content", self)
                    

class Section:

    pass
class Content:

    pass
class doc_fragment_PlainTextContent(Content):

    def __init__(self, value: str, Content13: "doc_book_BookContainer", Content: "doc_fragment_Container"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ResourceFactory:

    pass
class doc_map_ExtensionMappingEntry:

    def __init__(self, extension: str, doc_map_ExtensionMappingEntry: "ResourceFactory" = None):
        self.extension = extension
        self.doc_map_ExtensionMappingEntry = doc_map_ExtensionMappingEntry
        
    @property
    def extension(self) -> str:
        return self.__extension

    @extension.setter
    def extension(self, extension: str):
        self.__extension = extension

    @property
    def doc_map_ExtensionMappingEntry(self):
        return self.__doc_map_ExtensionMappingEntry

    @doc_map_ExtensionMappingEntry.setter
    def doc_map_ExtensionMappingEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_map_ExtensionMappingEntry__doc_map_ExtensionMappingEntry", None)
        self.__doc_map_ExtensionMappingEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceFactory"):
                opp_val = getattr(old_value, "ResourceFactory", None)
                if opp_val == self:
                    setattr(old_value, "ResourceFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceFactory"):
                opp_val = getattr(value, "ResourceFactory", None)
                setattr(value, "ResourceFactory", self)

class doc_map_ResourceFactory:

    def __init__(self, className: str):
        self.className = className
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

class Container:

    pass
class doc_fragment_Section(Container):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class doc_fragment_Fragment(Container):

    pass
class doc_map_MapContainer(ABC):

    def __init__(self, numberingStyle: str, doc_map_MapContainer: set["MapElement"] = None):
        self.numberingStyle = numberingStyle
        self.doc_map_MapContainer = doc_map_MapContainer if doc_map_MapContainer is not None else set()
        
    @property
    def numberingStyle(self) -> str:
        return self.__numberingStyle

    @numberingStyle.setter
    def numberingStyle(self, numberingStyle: str):
        self.__numberingStyle = numberingStyle

    @property
    def doc_map_MapContainer(self):
        return self.__doc_map_MapContainer

    @doc_map_MapContainer.setter
    def doc_map_MapContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_map_MapContainer__doc_map_MapContainer", None)
        self.__doc_map_MapContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MapElement"):
                    opp_val = getattr(item, "MapElement", None)
                    
                    if opp_val == self:
                        setattr(item, "MapElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MapElement"):
                    opp_val = getattr(item, "MapElement", None)
                    
                    setattr(item, "MapElement", self)
                    

class fragment_Content:

    pass
class NameRule:

    pass
class doc_map_MapElement(ABC):

    def __init__(self):
        
    def visit(self, visitor: str):
        # TODO: Implement visit method
        pass

class PatternRule:

    pass
class doc_map_ExcludePatternRule(PatternRule):

    def __init__(self):
        
    def checkRule(self, name: str) -> str:
        # TODO: Implement checkRule method
        pass

class doc_map_IncludePatternRule(PatternRule):

    def __init__(self):
        
    def checkRule(self, name: str) -> str:
        # TODO: Implement checkRule method
        pass

class doc_map_PatternRule(NameRule):

    def __init__(self, pattern: str, NameRule: "doc_map_Feature"):
        self.pattern = pattern
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

class doc_map_NameRule(ABC):

    def __init__(self):
        
    def checkRule(self, name: str) -> str:
        # TODO: Implement checkRule method
        pass

class MapContainer:

    pass
class doc_map_Map(MapContainer):

    def __init__(self, doc_map_Map: set["ExtensionMappingEntry"] = None):
        self.doc_map_Map = doc_map_Map if doc_map_Map is not None else set()
        
    @property
    def doc_map_Map(self):
        return self.__doc_map_Map

    @doc_map_Map.setter
    def doc_map_Map(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_map_Map__doc_map_Map", None)
        self.__doc_map_Map = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionMappingEntry"):
                    opp_val = getattr(item, "ExtensionMappingEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionMappingEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionMappingEntry"):
                    opp_val = getattr(item, "ExtensionMappingEntry", None)
                    
                    setattr(item, "ExtensionMappingEntry", self)
                    

    def visit(self, visitor: str):
        # TODO: Implement visit method
        pass

class map_MapElement:

    pass
class doc_map_ContentGenerator(fragment_Content, map_MapElement):

    pass
class map_MapContainer:

    pass
class doc_map_MapSection(map_MapElement, map_MapContainer):

    def __init__(self, title: str, id: str):
        self.title = title
        self.id = id
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Import:

    pass
class doc_map_Feature(Import):

    def __init__(self, featureId: str, createSection: bool, doc_map_Feature: set["NameRule"] = None):
        self.featureId = featureId
        self.createSection = createSection
        self.doc_map_Feature = doc_map_Feature if doc_map_Feature is not None else set()
        
    @property
    def featureId(self) -> str:
        return self.__featureId

    @featureId.setter
    def featureId(self, featureId: str):
        self.__featureId = featureId

    @property
    def createSection(self) -> bool:
        return self.__createSection

    @createSection.setter
    def createSection(self, createSection: bool):
        self.__createSection = createSection

    @property
    def doc_map_Feature(self):
        return self.__doc_map_Feature

    @doc_map_Feature.setter
    def doc_map_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doc_map_Feature__doc_map_Feature", None)
        self.__doc_map_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NameRule"):
                    opp_val = getattr(item, "NameRule", None)
                    
                    if opp_val == self:
                        setattr(item, "NameRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NameRule"):
                    opp_val = getattr(item, "NameRule", None)
                    
                    setattr(item, "NameRule", self)
                    

class doc_map_File(Import):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class MapElement:

    pass
class doc_map_Import(MapElement):

    pass
class ExtensionMappingEntry:

    pass
class doc_Test:

    pass