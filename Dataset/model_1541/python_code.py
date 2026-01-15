from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class researchvc_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class researchvc_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class researchvc_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class researchvc_PaperKeyword:

    def __init__(self, weight: int, researchvc_PaperKeyword: "researchvc_Paper" = None, researchvc_PaperKeyword29: "researchvc_Keyword" = None):
        self.weight = weight
        self.researchvc_PaperKeyword = researchvc_PaperKeyword
        self.researchvc_PaperKeyword29 = researchvc_PaperKeyword29
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def researchvc_PaperKeyword(self):
        return self.__researchvc_PaperKeyword

    @researchvc_PaperKeyword.setter
    def researchvc_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_PaperKeyword__researchvc_PaperKeyword", None)
        self.__researchvc_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Paper9"):
                opp_val = getattr(old_value, "researchvc_Paper9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Paper9"):
                opp_val = getattr(value, "researchvc_Paper9", None)
                if opp_val is None:
                    setattr(value, "researchvc_Paper9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchvc_PaperKeyword29(self):
        return self.__researchvc_PaperKeyword29

    @researchvc_PaperKeyword29.setter
    def researchvc_PaperKeyword29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_PaperKeyword__researchvc_PaperKeyword29", None)
        self.__researchvc_PaperKeyword29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Keyword30"):
                opp_val = getattr(old_value, "researchvc_Keyword30", None)
                if opp_val == self:
                    setattr(old_value, "researchvc_Keyword30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Keyword30"):
                opp_val = getattr(value, "researchvc_Keyword30", None)
                setattr(value, "researchvc_Keyword30", self)

class Labelled:

    pass
class Counted:

    pass
class researchvc_Write(Labelled):

    def __init__(self, timeSpent: int, researchvc_Write: "researchvc_Researcher" = None, researchvc_Write16: "researchvc_Paragraph" = None):
        self.timeSpent = timeSpent
        self.researchvc_Write = researchvc_Write
        self.researchvc_Write16 = researchvc_Write16
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def researchvc_Write16(self):
        return self.__researchvc_Write16

    @researchvc_Write16.setter
    def researchvc_Write16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Write__researchvc_Write16", None)
        self.__researchvc_Write16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Paragraph17"):
                opp_val = getattr(old_value, "researchvc_Paragraph17", None)
                if opp_val == self:
                    setattr(old_value, "researchvc_Paragraph17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Paragraph17"):
                opp_val = getattr(value, "researchvc_Paragraph17", None)
                setattr(value, "researchvc_Paragraph17", self)

    @property
    def researchvc_Write(self):
        return self.__researchvc_Write

    @researchvc_Write.setter
    def researchvc_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Write__researchvc_Write", None)
        self.__researchvc_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Researcher"):
                opp_val = getattr(old_value, "researchvc_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Researcher"):
                opp_val = getattr(value, "researchvc_Researcher", None)
                if opp_val is None:
                    setattr(value, "researchvc_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class researchvc_Researcher:

    def __init__(self, name: str, forName: str, researchvc_Researcher: set["researchvc_Write"] = None, researchvc_Researcher2: set["researchvc_Review"] = None, authors: set["researchvc_Paper"] = None, researchvc_Researcher5: set["researchvc_Skill"] = None, Researcher: "researchvc_Paper" = None, researchvc_Researcher22: "researchvc_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.researchvc_Researcher = researchvc_Researcher if researchvc_Researcher is not None else set()
        self.researchvc_Researcher2 = researchvc_Researcher2 if researchvc_Researcher2 is not None else set()
        self.authors = authors if authors is not None else set()
        self.researchvc_Researcher5 = researchvc_Researcher5 if researchvc_Researcher5 is not None else set()
        self.Researcher = Researcher
        self.researchvc_Researcher22 = researchvc_Researcher22
        
    @property
    def forName(self) -> str:
        return self.__forName

    @forName.setter
    def forName(self, forName: str):
        self.__forName = forName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def researchvc_Researcher5(self):
        return self.__researchvc_Researcher5

    @researchvc_Researcher5.setter
    def researchvc_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Researcher__researchvc_Researcher5", None)
        self.__researchvc_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchvc_Skill"):
                    opp_val = getattr(item, "researchvc_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "researchvc_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchvc_Skill"):
                    opp_val = getattr(item, "researchvc_Skill", None)
                    
                    setattr(item, "researchvc_Skill", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Researcher__Researcher", None)
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
    def researchvc_Researcher2(self):
        return self.__researchvc_Researcher2

    @researchvc_Researcher2.setter
    def researchvc_Researcher2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Researcher__researchvc_Researcher2", None)
        self.__researchvc_Researcher2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchvc_Review"):
                    opp_val = getattr(item, "researchvc_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "researchvc_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchvc_Review"):
                    opp_val = getattr(item, "researchvc_Review", None)
                    
                    setattr(item, "researchvc_Review", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Researcher__authors", None)
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
    def researchvc_Researcher(self):
        return self.__researchvc_Researcher

    @researchvc_Researcher.setter
    def researchvc_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Researcher__researchvc_Researcher", None)
        self.__researchvc_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchvc_Write"):
                    opp_val = getattr(item, "researchvc_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "researchvc_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchvc_Write"):
                    opp_val = getattr(item, "researchvc_Write", None)
                    
                    setattr(item, "researchvc_Write", self)
                    

    @property
    def researchvc_Researcher22(self):
        return self.__researchvc_Researcher22

    @researchvc_Researcher22.setter
    def researchvc_Researcher22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Researcher__researchvc_Researcher22", None)
        self.__researchvc_Researcher22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_PublicationStructure"):
                opp_val = getattr(old_value, "researchvc_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_PublicationStructure"):
                opp_val = getattr(value, "researchvc_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "researchvc_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class researchvc_Paragraph(Counted, Named):

    def __init__(self, content: str, researchvc_Paragraph: "researchvc_Paper" = None, researchvc_Paragraph14: set["researchvc_ReviewNote"] = None, researchvc_Paragraph17: "researchvc_Write" = None):
        self.content = content
        self.researchvc_Paragraph = researchvc_Paragraph
        self.researchvc_Paragraph14 = researchvc_Paragraph14 if researchvc_Paragraph14 is not None else set()
        self.researchvc_Paragraph17 = researchvc_Paragraph17
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def researchvc_Paragraph14(self):
        return self.__researchvc_Paragraph14

    @researchvc_Paragraph14.setter
    def researchvc_Paragraph14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Paragraph__researchvc_Paragraph14", None)
        self.__researchvc_Paragraph14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "researchvc_ReviewNote"):
                    opp_val = getattr(item, "researchvc_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "researchvc_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "researchvc_ReviewNote"):
                    opp_val = getattr(item, "researchvc_ReviewNote", None)
                    
                    setattr(item, "researchvc_ReviewNote", self)
                    

    @property
    def researchvc_Paragraph(self):
        return self.__researchvc_Paragraph

    @researchvc_Paragraph.setter
    def researchvc_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Paragraph__researchvc_Paragraph", None)
        self.__researchvc_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Paper"):
                opp_val = getattr(old_value, "researchvc_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Paper"):
                opp_val = getattr(value, "researchvc_Paper", None)
                if opp_val is None:
                    setattr(value, "researchvc_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchvc_Paragraph17(self):
        return self.__researchvc_Paragraph17

    @researchvc_Paragraph17.setter
    def researchvc_Paragraph17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Paragraph__researchvc_Paragraph17", None)
        self.__researchvc_Paragraph17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Write16"):
                opp_val = getattr(old_value, "researchvc_Write16", None)
                if opp_val == self:
                    setattr(old_value, "researchvc_Write16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Write16"):
                opp_val = getattr(value, "researchvc_Write16", None)
                setattr(value, "researchvc_Write16", self)

class researchvc_Keyword(Named):

    def __init__(self, word: str, researchvc_Keyword: "researchvc_PublicationStructure" = None, researchvc_Keyword30: "researchvc_PaperKeyword" = None):
        self.word = word
        self.researchvc_Keyword = researchvc_Keyword
        self.researchvc_Keyword30 = researchvc_Keyword30
        
    @property
    def word(self) -> str:
        return self.__word

    @word.setter
    def word(self, word: str):
        self.__word = word

    @property
    def researchvc_Keyword(self):
        return self.__researchvc_Keyword

    @researchvc_Keyword.setter
    def researchvc_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Keyword__researchvc_Keyword", None)
        self.__researchvc_Keyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_PublicationStructure27"):
                opp_val = getattr(old_value, "researchvc_PublicationStructure27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_PublicationStructure27"):
                opp_val = getattr(value, "researchvc_PublicationStructure27", None)
                if opp_val is None:
                    setattr(value, "researchvc_PublicationStructure27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchvc_Keyword30(self):
        return self.__researchvc_Keyword30

    @researchvc_Keyword30.setter
    def researchvc_Keyword30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Keyword__researchvc_Keyword30", None)
        self.__researchvc_Keyword30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_PaperKeyword29"):
                opp_val = getattr(old_value, "researchvc_PaperKeyword29", None)
                if opp_val == self:
                    setattr(old_value, "researchvc_PaperKeyword29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_PaperKeyword29"):
                opp_val = getattr(value, "researchvc_PaperKeyword29", None)
                setattr(value, "researchvc_PaperKeyword29", self)

class researchvc_ReviewNote(Named):

    def __init__(self, content: str, researchvc_ReviewNote: "researchvc_Paragraph" = None, researchvc_ReviewNote20: "researchvc_Review" = None):
        self.content = content
        self.researchvc_ReviewNote = researchvc_ReviewNote
        self.researchvc_ReviewNote20 = researchvc_ReviewNote20
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def researchvc_ReviewNote(self):
        return self.__researchvc_ReviewNote

    @researchvc_ReviewNote.setter
    def researchvc_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_ReviewNote__researchvc_ReviewNote", None)
        self.__researchvc_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Paragraph14"):
                opp_val = getattr(old_value, "researchvc_Paragraph14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Paragraph14"):
                opp_val = getattr(value, "researchvc_Paragraph14", None)
                if opp_val is None:
                    setattr(value, "researchvc_Paragraph14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def researchvc_ReviewNote20(self):
        return self.__researchvc_ReviewNote20

    @researchvc_ReviewNote20.setter
    def researchvc_ReviewNote20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_ReviewNote__researchvc_ReviewNote20", None)
        self.__researchvc_ReviewNote20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Review19"):
                opp_val = getattr(old_value, "researchvc_Review19", None)
                if opp_val == self:
                    setattr(old_value, "researchvc_Review19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Review19"):
                opp_val = getattr(value, "researchvc_Review19", None)
                setattr(value, "researchvc_Review19", self)

class researchvc_PublicationStructure(Named):

    pass
class researchvc_Skill:

    def __init__(self, description: str, researchvc_Skill: "researchvc_Researcher" = None):
        self.description = description
        self.researchvc_Skill = researchvc_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def researchvc_Skill(self):
        return self.__researchvc_Skill

    @researchvc_Skill.setter
    def researchvc_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Skill__researchvc_Skill", None)
        self.__researchvc_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Researcher5"):
                opp_val = getattr(old_value, "researchvc_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Researcher5"):
                opp_val = getattr(value, "researchvc_Researcher5", None)
                if opp_val is None:
                    setattr(value, "researchvc_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class researchvc_Paper(Named):

    pass
class researchvc_Review(Labelled):

    def __init__(self, date: date, researchvc_Review: "researchvc_Researcher" = None, researchvc_Review19: "researchvc_ReviewNote" = None):
        self.date = date
        self.researchvc_Review = researchvc_Review
        self.researchvc_Review19 = researchvc_Review19
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def researchvc_Review19(self):
        return self.__researchvc_Review19

    @researchvc_Review19.setter
    def researchvc_Review19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Review__researchvc_Review19", None)
        self.__researchvc_Review19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_ReviewNote20"):
                opp_val = getattr(old_value, "researchvc_ReviewNote20", None)
                if opp_val == self:
                    setattr(old_value, "researchvc_ReviewNote20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_ReviewNote20"):
                opp_val = getattr(value, "researchvc_ReviewNote20", None)
                setattr(value, "researchvc_ReviewNote20", self)

    @property
    def researchvc_Review(self):
        return self.__researchvc_Review

    @researchvc_Review.setter
    def researchvc_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_researchvc_Review__researchvc_Review", None)
        self.__researchvc_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "researchvc_Researcher2"):
                opp_val = getattr(old_value, "researchvc_Researcher2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "researchvc_Researcher2"):
                opp_val = getattr(value, "researchvc_Researcher2", None)
                if opp_val is None:
                    setattr(value, "researchvc_Researcher2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
