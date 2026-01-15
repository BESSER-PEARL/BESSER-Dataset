from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class researchva_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class researchva_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class researchva_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Labelled:

    pass
class Counted:

    pass
class Named:

    pass
class researchva_Paragraph(Counted, Named):

    def __init__(self, content: str, researchva_Paragraph: "researchva_Paper" = None, researchva_Paragraph12: set["researchva_ReviewNote"] = None, researchva_Paragraph15: "researchva_Write" = None):
        self.content = content
        self.researchva_Paragraph = researchva_Paragraph
        self.researchva_Paragraph12 = researchva_Paragraph12 if researchva_Paragraph12 is not None else set()
        self.researchva_Paragraph15 = researchva_Paragraph15
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def researchva_Paragraph(self):
        return self.__researchva_Paragraph

    @researchva_Paragraph.setter
    def researchva_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Paragraph__researchva_Paragraph", None)
        self.__researchva_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Paper"):
                opp_val = getattr(old_value, "researchva_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Paper"):
                opp_val = getattr(value, "researchva_Paper", None)
                if opp_val is None:
                    setattr(value, "researchva_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchva_Paragraph15(self):
        return self.__researchva_Paragraph15

    @researchva_Paragraph15.setter
    def researchva_Paragraph15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Paragraph__researchva_Paragraph15", None)
        self.__researchva_Paragraph15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Write14"):
                opp_val = getattr(old_value, "researchva_Write14", None)
                if opp_val == self:
                    setattr(old_value, "researchva_Write14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Write14"):
                opp_val = getattr(value, "researchva_Write14", None)
                setattr(value, "researchva_Write14", self)

    @property
    def researchva_Paragraph12(self):
        return self.__researchva_Paragraph12

    @researchva_Paragraph12.setter
    def researchva_Paragraph12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Paragraph__researchva_Paragraph12", None)
        self.__researchva_Paragraph12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchva_ReviewNote"):
                    opp_val = getattr(item, "researchva_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "researchva_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchva_ReviewNote"):
                    opp_val = getattr(item, "researchva_ReviewNote", None)
                    
                    setattr(item, "researchva_ReviewNote", self)
                    

class researchva_ReviewNote(Named):

    def __init__(self, content: str, researchva_ReviewNote: "researchva_Paragraph" = None, researchva_ReviewNote18: "researchva_Review" = None):
        self.content = content
        self.researchva_ReviewNote = researchva_ReviewNote
        self.researchva_ReviewNote18 = researchva_ReviewNote18
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def researchva_ReviewNote18(self):
        return self.__researchva_ReviewNote18

    @researchva_ReviewNote18.setter
    def researchva_ReviewNote18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_ReviewNote__researchva_ReviewNote18", None)
        self.__researchva_ReviewNote18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Review17"):
                opp_val = getattr(old_value, "researchva_Review17", None)
                if opp_val == self:
                    setattr(old_value, "researchva_Review17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Review17"):
                opp_val = getattr(value, "researchva_Review17", None)
                setattr(value, "researchva_Review17", self)

    @property
    def researchva_ReviewNote(self):
        return self.__researchva_ReviewNote

    @researchva_ReviewNote.setter
    def researchva_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_ReviewNote__researchva_ReviewNote", None)
        self.__researchva_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Paragraph12"):
                opp_val = getattr(old_value, "researchva_Paragraph12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Paragraph12"):
                opp_val = getattr(value, "researchva_Paragraph12", None)
                if opp_val is None:
                    setattr(value, "researchva_Paragraph12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class researchva_Keyword(Named):

    def __init__(self, word: str, researchva_Keyword: "researchva_PublicationStructure" = None):
        self.word = word
        self.researchva_Keyword = researchva_Keyword
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def researchva_Keyword(self):
        return self.__researchva_Keyword

    @researchva_Keyword.setter
    def researchva_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Keyword__researchva_Keyword", None)
        self.__researchva_Keyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_PublicationStructure25"):
                opp_val = getattr(old_value, "researchva_PublicationStructure25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_PublicationStructure25"):
                opp_val = getattr(value, "researchva_PublicationStructure25", None)
                if opp_val is None:
                    setattr(value, "researchva_PublicationStructure25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class researchva_PublicationStructure(Named):

    pass
class researchva_Skill:

    def __init__(self, description: str, researchva_Skill: "researchva_Researcher" = None):
        self.description = description
        self.researchva_Skill = researchva_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def researchva_Skill(self):
        return self.__researchva_Skill

    @researchva_Skill.setter
    def researchva_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Skill__researchva_Skill", None)
        self.__researchva_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Researcher5"):
                opp_val = getattr(old_value, "researchva_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Researcher5"):
                opp_val = getattr(value, "researchva_Researcher5", None)
                if opp_val is None:
                    setattr(value, "researchva_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class researchva_Paper(Named):

    pass
class researchva_Review(Labelled):

    def __init__(self, date: date, researchva_Review: "researchva_Researcher" = None, researchva_Review17: "researchva_ReviewNote" = None):
        self.date = date
        self.researchva_Review = researchva_Review
        self.researchva_Review17 = researchva_Review17
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def researchva_Review17(self):
        return self.__researchva_Review17

    @researchva_Review17.setter
    def researchva_Review17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Review__researchva_Review17", None)
        self.__researchva_Review17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_ReviewNote18"):
                opp_val = getattr(old_value, "researchva_ReviewNote18", None)
                if opp_val == self:
                    setattr(old_value, "researchva_ReviewNote18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_ReviewNote18"):
                opp_val = getattr(value, "researchva_ReviewNote18", None)
                setattr(value, "researchva_ReviewNote18", self)

    @property
    def researchva_Review(self):
        return self.__researchva_Review

    @researchva_Review.setter
    def researchva_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Review__researchva_Review", None)
        self.__researchva_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Researcher2"):
                opp_val = getattr(old_value, "researchva_Researcher2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Researcher2"):
                opp_val = getattr(value, "researchva_Researcher2", None)
                if opp_val is None:
                    setattr(value, "researchva_Researcher2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class researchva_Write(Labelled):

    def __init__(self, timeSpent: int, researchva_Write: "researchva_Researcher" = None, researchva_Write14: "researchva_Paragraph" = None):
        self.timeSpent = timeSpent
        self.researchva_Write = researchva_Write
        self.researchva_Write14 = researchva_Write14
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def researchva_Write(self):
        return self.__researchva_Write

    @researchva_Write.setter
    def researchva_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Write__researchva_Write", None)
        self.__researchva_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Researcher"):
                opp_val = getattr(old_value, "researchva_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Researcher"):
                opp_val = getattr(value, "researchva_Researcher", None)
                if opp_val is None:
                    setattr(value, "researchva_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchva_Write14(self):
        return self.__researchva_Write14

    @researchva_Write14.setter
    def researchva_Write14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Write__researchva_Write14", None)
        self.__researchva_Write14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_Paragraph15"):
                opp_val = getattr(old_value, "researchva_Paragraph15", None)
                if opp_val == self:
                    setattr(old_value, "researchva_Paragraph15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_Paragraph15"):
                opp_val = getattr(value, "researchva_Paragraph15", None)
                setattr(value, "researchva_Paragraph15", self)

class researchva_Researcher:

    def __init__(self, name: str, forName: str, researchva_Researcher: set["researchva_Write"] = None, researchva_Researcher2: set["researchva_Review"] = None, authors: set["researchva_Paper"] = None, researchva_Researcher5: set["researchva_Skill"] = None, Researcher: "researchva_Paper" = None, researchva_Researcher20: "researchva_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.researchva_Researcher = researchva_Researcher if researchva_Researcher is not None else set()
        self.researchva_Researcher2 = researchva_Researcher2 if researchva_Researcher2 is not None else set()
        self.authors = authors if authors is not None else set()
        self.researchva_Researcher5 = researchva_Researcher5 if researchva_Researcher5 is not None else set()
        self.Researcher = Researcher
        self.researchva_Researcher20 = researchva_Researcher20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Researcher__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Paper"):
                    opp_val = getattr(item, "Paper", None)
                    
                    if opp_val == self:
                        setattr(item, "Paper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Paper"):
                    opp_val = getattr(item, "Paper", None)
                    
                    setattr(item, "Paper", self)
                    

    @property
    def researchva_Researcher5(self):
        return self.__researchva_Researcher5

    @researchva_Researcher5.setter
    def researchva_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Researcher__researchva_Researcher5", None)
        self.__researchva_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchva_Skill"):
                    opp_val = getattr(item, "researchva_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "researchva_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchva_Skill"):
                    opp_val = getattr(item, "researchva_Skill", None)
                    
                    setattr(item, "researchva_Skill", self)
                    

    @property
    def researchva_Researcher(self):
        return self.__researchva_Researcher

    @researchva_Researcher.setter
    def researchva_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Researcher__researchva_Researcher", None)
        self.__researchva_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchva_Write"):
                    opp_val = getattr(item, "researchva_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "researchva_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchva_Write"):
                    opp_val = getattr(item, "researchva_Write", None)
                    
                    setattr(item, "researchva_Write", self)
                    

    @property
    def researchva_Researcher20(self):
        return self.__researchva_Researcher20

    @researchva_Researcher20.setter
    def researchva_Researcher20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Researcher__researchva_Researcher20", None)
        self.__researchva_Researcher20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchva_PublicationStructure"):
                opp_val = getattr(old_value, "researchva_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchva_PublicationStructure"):
                opp_val = getattr(value, "researchva_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "researchva_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Researcher__Researcher", None)
        self.__Researcher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "res_papers"):
                opp_val = getattr(old_value, "res_papers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "res_papers"):
                opp_val = getattr(value, "res_papers", None)
                if opp_val is None:
                    setattr(value, "res_papers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchva_Researcher2(self):
        return self.__researchva_Researcher2

    @researchva_Researcher2.setter
    def researchva_Researcher2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchva_Researcher__researchva_Researcher2", None)
        self.__researchva_Researcher2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchva_Review"):
                    opp_val = getattr(item, "researchva_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "researchva_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchva_Review"):
                    opp_val = getattr(item, "researchva_Review", None)
                    
                    setattr(item, "researchva_Review", self)
                    
