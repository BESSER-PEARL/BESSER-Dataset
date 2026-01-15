from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class publication102_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class publication102_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication102_Named(ABC):

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
class publication102_PaperKeyword:

    def __init__(self, weight: int, publication102_PaperKeyword: "publication102_Paper" = None, publication102_PaperKeyword44: "publication102_Keyword" = None):
        self.weight = weight
        self.publication102_PaperKeyword = publication102_PaperKeyword
        self.publication102_PaperKeyword44 = publication102_PaperKeyword44
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def publication102_PaperKeyword(self):
        return self.__publication102_PaperKeyword

    @publication102_PaperKeyword.setter
    def publication102_PaperKeyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_PaperKeyword__publication102_PaperKeyword", None)
        self.__publication102_PaperKeyword = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Paper13"):
                opp_val = getattr(old_value, "publication102_Paper13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Paper13"):
                opp_val = getattr(value, "publication102_Paper13", None)
                if opp_val is None:
                    setattr(value, "publication102_Paper13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication102_PaperKeyword44(self):
        return self.__publication102_PaperKeyword44

    @publication102_PaperKeyword44.setter
    def publication102_PaperKeyword44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_PaperKeyword__publication102_PaperKeyword44", None)
        self.__publication102_PaperKeyword44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Keyword45"):
                opp_val = getattr(old_value, "publication102_Keyword45", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Keyword45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Keyword45"):
                opp_val = getattr(value, "publication102_Keyword45", None)
                setattr(value, "publication102_Keyword45", self)

class Named:

    pass
class publication102_Paragraph(Named, Counted):

    def __init__(self, content: str, publication102_Paragraph: "publication102_Paper" = None, publication102_Paragraph18: set["publication102_ReviewNote"] = None, publication102_Paragraph21: "publication102_Write" = None):
        self.content = content
        self.publication102_Paragraph = publication102_Paragraph
        self.publication102_Paragraph18 = publication102_Paragraph18 if publication102_Paragraph18 is not None else set()
        self.publication102_Paragraph21 = publication102_Paragraph21
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication102_Paragraph18(self):
        return self.__publication102_Paragraph18

    @publication102_Paragraph18.setter
    def publication102_Paragraph18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Paragraph__publication102_Paragraph18", None)
        self.__publication102_Paragraph18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication102_ReviewNote"):
                    opp_val = getattr(item, "publication102_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication102_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication102_ReviewNote"):
                    opp_val = getattr(item, "publication102_ReviewNote", None)
                    
                    setattr(item, "publication102_ReviewNote", self)
                    

    @property
    def publication102_Paragraph21(self):
        return self.__publication102_Paragraph21

    @publication102_Paragraph21.setter
    def publication102_Paragraph21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Paragraph__publication102_Paragraph21", None)
        self.__publication102_Paragraph21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Write20"):
                opp_val = getattr(old_value, "publication102_Write20", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Write20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Write20"):
                opp_val = getattr(value, "publication102_Write20", None)
                setattr(value, "publication102_Write20", self)

    @property
    def publication102_Paragraph(self):
        return self.__publication102_Paragraph

    @publication102_Paragraph.setter
    def publication102_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Paragraph__publication102_Paragraph", None)
        self.__publication102_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Paper"):
                opp_val = getattr(old_value, "publication102_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Paper"):
                opp_val = getattr(value, "publication102_Paper", None)
                if opp_val is None:
                    setattr(value, "publication102_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication102_PublicationStructure(Named):

    pass
class publication102_Keyword(Named):

    def __init__(self, description: str, publication102_Keyword: set["publication102_Paper"] = None, publication102_Keyword42: "publication102_KnowledgeManager" = None, publication102_Keyword45: "publication102_PaperKeyword" = None):
        self.description = description
        self.publication102_Keyword = publication102_Keyword if publication102_Keyword is not None else set()
        self.publication102_Keyword42 = publication102_Keyword42
        self.publication102_Keyword45 = publication102_Keyword45
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication102_Keyword45(self):
        return self.__publication102_Keyword45

    @publication102_Keyword45.setter
    def publication102_Keyword45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Keyword__publication102_Keyword45", None)
        self.__publication102_Keyword45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_PaperKeyword44"):
                opp_val = getattr(old_value, "publication102_PaperKeyword44", None)
                if opp_val == self:
                    setattr(old_value, "publication102_PaperKeyword44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_PaperKeyword44"):
                opp_val = getattr(value, "publication102_PaperKeyword44", None)
                setattr(value, "publication102_PaperKeyword44", self)

    @property
    def publication102_Keyword(self):
        return self.__publication102_Keyword

    @publication102_Keyword.setter
    def publication102_Keyword(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Keyword__publication102_Keyword", None)
        self.__publication102_Keyword = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication102_Paper39"):
                    opp_val = getattr(item, "publication102_Paper39", None)
                    
                    if opp_val == self:
                        setattr(item, "publication102_Paper39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication102_Paper39"):
                    opp_val = getattr(item, "publication102_Paper39", None)
                    
                    setattr(item, "publication102_Paper39", self)
                    

    @property
    def publication102_Keyword42(self):
        return self.__publication102_Keyword42

    @publication102_Keyword42.setter
    def publication102_Keyword42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Keyword__publication102_Keyword42", None)
        self.__publication102_Keyword42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_KnowledgeManager41"):
                opp_val = getattr(old_value, "publication102_KnowledgeManager41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_KnowledgeManager41"):
                opp_val = getattr(value, "publication102_KnowledgeManager41", None)
                if opp_val is None:
                    setattr(value, "publication102_KnowledgeManager41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication102_KnowledgeManager(Named):

    pass
class publication102_Position(Named):

    def __init__(self, description: str, publication102_Position: "publication102_Researcher" = None, publication102_Position34: "publication102_PublicationStructure" = None, publication102_Position37: "publication102_Position" = None, publication102_Position35: "publication102_Position" = None):
        self.description = description
        self.publication102_Position = publication102_Position
        self.publication102_Position34 = publication102_Position34
        self.publication102_Position37 = publication102_Position37
        self.publication102_Position35 = publication102_Position35
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication102_Position34(self):
        return self.__publication102_Position34

    @publication102_Position34.setter
    def publication102_Position34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Position__publication102_Position34", None)
        self.__publication102_Position34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_PublicationStructure33"):
                opp_val = getattr(old_value, "publication102_PublicationStructure33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_PublicationStructure33"):
                opp_val = getattr(value, "publication102_PublicationStructure33", None)
                if opp_val is None:
                    setattr(value, "publication102_PublicationStructure33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication102_Position(self):
        return self.__publication102_Position

    @publication102_Position.setter
    def publication102_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Position__publication102_Position", None)
        self.__publication102_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Researcher7"):
                opp_val = getattr(old_value, "publication102_Researcher7", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Researcher7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Researcher7"):
                opp_val = getattr(value, "publication102_Researcher7", None)
                setattr(value, "publication102_Researcher7", self)

    @property
    def publication102_Position35(self):
        return self.__publication102_Position35

    @publication102_Position35.setter
    def publication102_Position35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Position__publication102_Position35", None)
        self.__publication102_Position35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Position37"):
                opp_val = getattr(old_value, "publication102_Position37", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Position37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Position37"):
                opp_val = getattr(value, "publication102_Position37", None)
                setattr(value, "publication102_Position37", self)

    @property
    def publication102_Position37(self):
        return self.__publication102_Position37

    @publication102_Position37.setter
    def publication102_Position37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Position__publication102_Position37", None)
        self.__publication102_Position37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Position35"):
                opp_val = getattr(old_value, "publication102_Position35", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Position35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Position35"):
                opp_val = getattr(value, "publication102_Position35", None)
                setattr(value, "publication102_Position35", self)

class publication102_ReviewNote(Named):

    def __init__(self, content: str, publication102_ReviewNote: "publication102_Paragraph" = None, publication102_ReviewNote24: "publication102_Review" = None):
        self.content = content
        self.publication102_ReviewNote = publication102_ReviewNote
        self.publication102_ReviewNote24 = publication102_ReviewNote24
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication102_ReviewNote24(self):
        return self.__publication102_ReviewNote24

    @publication102_ReviewNote24.setter
    def publication102_ReviewNote24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_ReviewNote__publication102_ReviewNote24", None)
        self.__publication102_ReviewNote24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Review23"):
                opp_val = getattr(old_value, "publication102_Review23", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Review23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Review23"):
                opp_val = getattr(value, "publication102_Review23", None)
                setattr(value, "publication102_Review23", self)

    @property
    def publication102_ReviewNote(self):
        return self.__publication102_ReviewNote

    @publication102_ReviewNote.setter
    def publication102_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_ReviewNote__publication102_ReviewNote", None)
        self.__publication102_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Paragraph18"):
                opp_val = getattr(old_value, "publication102_Paragraph18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Paragraph18"):
                opp_val = getattr(value, "publication102_Paragraph18", None)
                if opp_val is None:
                    setattr(value, "publication102_Paragraph18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication102_Collaboration:

    def __init__(self, ratio: int, publication102_Collaboration: "publication102_Researcher" = None, publication102_Collaboration47: "publication102_Paper" = None):
        self.ratio = ratio
        self.publication102_Collaboration = publication102_Collaboration
        self.publication102_Collaboration47 = publication102_Collaboration47
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def publication102_Collaboration47(self):
        return self.__publication102_Collaboration47

    @publication102_Collaboration47.setter
    def publication102_Collaboration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Collaboration__publication102_Collaboration47", None)
        self.__publication102_Collaboration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Paper48"):
                opp_val = getattr(old_value, "publication102_Paper48", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Paper48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Paper48"):
                opp_val = getattr(value, "publication102_Paper48", None)
                setattr(value, "publication102_Paper48", self)

    @property
    def publication102_Collaboration(self):
        return self.__publication102_Collaboration

    @publication102_Collaboration.setter
    def publication102_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Collaboration__publication102_Collaboration", None)
        self.__publication102_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Researcher9"):
                opp_val = getattr(old_value, "publication102_Researcher9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Researcher9"):
                opp_val = getattr(value, "publication102_Researcher9", None)
                if opp_val is None:
                    setattr(value, "publication102_Researcher9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication102_Skill:

    def __init__(self, description: str, publication102_Skill: "publication102_Researcher" = None):
        self.description = description
        self.publication102_Skill = publication102_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication102_Skill(self):
        return self.__publication102_Skill

    @publication102_Skill.setter
    def publication102_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Skill__publication102_Skill", None)
        self.__publication102_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Researcher5"):
                opp_val = getattr(old_value, "publication102_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Researcher5"):
                opp_val = getattr(value, "publication102_Researcher5", None)
                if opp_val is None:
                    setattr(value, "publication102_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication102_Paper(Named):

    pass
class publication102_Review(Labelled):

    def __init__(self, date: date, publication102_Review: "publication102_Researcher" = None, publication102_Review23: "publication102_ReviewNote" = None):
        self.date = date
        self.publication102_Review = publication102_Review
        self.publication102_Review23 = publication102_Review23
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def publication102_Review(self):
        return self.__publication102_Review

    @publication102_Review.setter
    def publication102_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Review__publication102_Review", None)
        self.__publication102_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Researcher2"):
                opp_val = getattr(old_value, "publication102_Researcher2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Researcher2"):
                opp_val = getattr(value, "publication102_Researcher2", None)
                if opp_val is None:
                    setattr(value, "publication102_Researcher2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication102_Review23(self):
        return self.__publication102_Review23

    @publication102_Review23.setter
    def publication102_Review23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Review__publication102_Review23", None)
        self.__publication102_Review23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_ReviewNote24"):
                opp_val = getattr(old_value, "publication102_ReviewNote24", None)
                if opp_val == self:
                    setattr(old_value, "publication102_ReviewNote24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_ReviewNote24"):
                opp_val = getattr(value, "publication102_ReviewNote24", None)
                setattr(value, "publication102_ReviewNote24", self)

class publication102_Write(Labelled):

    def __init__(self, timeSpent: int, publication102_Write: "publication102_Researcher" = None, publication102_Write20: "publication102_Paragraph" = None):
        self.timeSpent = timeSpent
        self.publication102_Write = publication102_Write
        self.publication102_Write20 = publication102_Write20
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def publication102_Write20(self):
        return self.__publication102_Write20

    @publication102_Write20.setter
    def publication102_Write20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Write__publication102_Write20", None)
        self.__publication102_Write20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Paragraph21"):
                opp_val = getattr(old_value, "publication102_Paragraph21", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Paragraph21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Paragraph21"):
                opp_val = getattr(value, "publication102_Paragraph21", None)
                setattr(value, "publication102_Paragraph21", self)

    @property
    def publication102_Write(self):
        return self.__publication102_Write

    @publication102_Write.setter
    def publication102_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Write__publication102_Write", None)
        self.__publication102_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Researcher"):
                opp_val = getattr(old_value, "publication102_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Researcher"):
                opp_val = getattr(value, "publication102_Researcher", None)
                if opp_val is None:
                    setattr(value, "publication102_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication102_Researcher:

    def __init__(self, name: str, forName: str, publication102_Researcher: set["publication102_Write"] = None, publication102_Researcher2: set["publication102_Review"] = None, authors: set["publication102_Paper"] = None, publication102_Researcher5: set["publication102_Skill"] = None, publication102_Researcher9: set["publication102_Collaboration"] = None, Researcher: "publication102_Paper" = None, publication102_Researcher7: "publication102_Position" = None, publication102_Researcher26: "publication102_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.publication102_Researcher = publication102_Researcher if publication102_Researcher is not None else set()
        self.publication102_Researcher2 = publication102_Researcher2 if publication102_Researcher2 is not None else set()
        self.authors = authors if authors is not None else set()
        self.publication102_Researcher5 = publication102_Researcher5 if publication102_Researcher5 is not None else set()
        self.publication102_Researcher9 = publication102_Researcher9 if publication102_Researcher9 is not None else set()
        self.Researcher = Researcher
        self.publication102_Researcher7 = publication102_Researcher7
        self.publication102_Researcher26 = publication102_Researcher26
        
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
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__authors", None)
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
    def publication102_Researcher5(self):
        return self.__publication102_Researcher5

    @publication102_Researcher5.setter
    def publication102_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__publication102_Researcher5", None)
        self.__publication102_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication102_Skill"):
                    opp_val = getattr(item, "publication102_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "publication102_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication102_Skill"):
                    opp_val = getattr(item, "publication102_Skill", None)
                    
                    setattr(item, "publication102_Skill", self)
                    

    @property
    def publication102_Researcher(self):
        return self.__publication102_Researcher

    @publication102_Researcher.setter
    def publication102_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__publication102_Researcher", None)
        self.__publication102_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication102_Write"):
                    opp_val = getattr(item, "publication102_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication102_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication102_Write"):
                    opp_val = getattr(item, "publication102_Write", None)
                    
                    setattr(item, "publication102_Write", self)
                    

    @property
    def publication102_Researcher7(self):
        return self.__publication102_Researcher7

    @publication102_Researcher7.setter
    def publication102_Researcher7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__publication102_Researcher7", None)
        self.__publication102_Researcher7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_Position"):
                opp_val = getattr(old_value, "publication102_Position", None)
                if opp_val == self:
                    setattr(old_value, "publication102_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_Position"):
                opp_val = getattr(value, "publication102_Position", None)
                setattr(value, "publication102_Position", self)

    @property
    def publication102_Researcher26(self):
        return self.__publication102_Researcher26

    @publication102_Researcher26.setter
    def publication102_Researcher26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__publication102_Researcher26", None)
        self.__publication102_Researcher26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication102_PublicationStructure"):
                opp_val = getattr(old_value, "publication102_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication102_PublicationStructure"):
                opp_val = getattr(value, "publication102_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication102_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__Researcher", None)
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
    def publication102_Researcher2(self):
        return self.__publication102_Researcher2

    @publication102_Researcher2.setter
    def publication102_Researcher2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__publication102_Researcher2", None)
        self.__publication102_Researcher2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication102_Review"):
                    opp_val = getattr(item, "publication102_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication102_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication102_Review"):
                    opp_val = getattr(item, "publication102_Review", None)
                    
                    setattr(item, "publication102_Review", self)
                    

    @property
    def publication102_Researcher9(self):
        return self.__publication102_Researcher9

    @publication102_Researcher9.setter
    def publication102_Researcher9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication102_Researcher__publication102_Researcher9", None)
        self.__publication102_Researcher9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication102_Collaboration"):
                    opp_val = getattr(item, "publication102_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "publication102_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication102_Collaboration"):
                    opp_val = getattr(item, "publication102_Collaboration", None)
                    
                    setattr(item, "publication102_Collaboration", self)
                    
