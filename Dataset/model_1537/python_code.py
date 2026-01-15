from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class publication103_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class publication103_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication103_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class publication103_PublicationStructure(Named):

    pass
class Labelled:

    pass
class publication103_ReviewNote(Named):

    def __init__(self, content: str, publication103_ReviewNote: "publication103_Paragraph" = None, publication103_ReviewNote22: "publication103_Review" = None):
        self.content = content
        self.publication103_ReviewNote = publication103_ReviewNote
        self.publication103_ReviewNote22 = publication103_ReviewNote22
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication103_ReviewNote22(self):
        return self.__publication103_ReviewNote22

    @publication103_ReviewNote22.setter
    def publication103_ReviewNote22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_ReviewNote__publication103_ReviewNote22", None)
        self.__publication103_ReviewNote22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Review21"):
                opp_val = getattr(old_value, "publication103_Review21", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Review21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Review21"):
                opp_val = getattr(value, "publication103_Review21", None)
                setattr(value, "publication103_Review21", self)

    @property
    def publication103_ReviewNote(self):
        return self.__publication103_ReviewNote

    @publication103_ReviewNote.setter
    def publication103_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_ReviewNote__publication103_ReviewNote", None)
        self.__publication103_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Paragraph16"):
                opp_val = getattr(old_value, "publication103_Paragraph16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Paragraph16"):
                opp_val = getattr(value, "publication103_Paragraph16", None)
                if opp_val is None:
                    setattr(value, "publication103_Paragraph16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Counted:

    pass
class publication103_Paragraph(Named, Counted):

    def __init__(self, content: str, publication103_Paragraph16: set["publication103_ReviewNote"] = None, publication103_Paragraph: "publication103_Paper" = None, publication103_Paragraph19: "publication103_Write" = None):
        self.content = content
        self.publication103_Paragraph16 = publication103_Paragraph16 if publication103_Paragraph16 is not None else set()
        self.publication103_Paragraph = publication103_Paragraph
        self.publication103_Paragraph19 = publication103_Paragraph19
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication103_Paragraph16(self):
        return self.__publication103_Paragraph16

    @publication103_Paragraph16.setter
    def publication103_Paragraph16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Paragraph__publication103_Paragraph16", None)
        self.__publication103_Paragraph16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication103_ReviewNote"):
                    opp_val = getattr(item, "publication103_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication103_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication103_ReviewNote"):
                    opp_val = getattr(item, "publication103_ReviewNote", None)
                    
                    setattr(item, "publication103_ReviewNote", self)
                    

    @property
    def publication103_Paragraph19(self):
        return self.__publication103_Paragraph19

    @publication103_Paragraph19.setter
    def publication103_Paragraph19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Paragraph__publication103_Paragraph19", None)
        self.__publication103_Paragraph19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Write18"):
                opp_val = getattr(old_value, "publication103_Write18", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Write18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Write18"):
                opp_val = getattr(value, "publication103_Write18", None)
                setattr(value, "publication103_Write18", self)

    @property
    def publication103_Paragraph(self):
        return self.__publication103_Paragraph

    @publication103_Paragraph.setter
    def publication103_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Paragraph__publication103_Paragraph", None)
        self.__publication103_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Paper"):
                opp_val = getattr(old_value, "publication103_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Paper"):
                opp_val = getattr(value, "publication103_Paper", None)
                if opp_val is None:
                    setattr(value, "publication103_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication103_Researcher:

    def __init__(self, name: str, forName: str, publication103_Researcher: set["publication103_Write"] = None, publication103_Researcher2: set["publication103_Review"] = None, authors: set["publication103_Paper"] = None, publication103_Researcher5: set["publication103_Skill"] = None, publication103_Researcher7: "publication103_Position" = None, publication103_Researcher9: set["publication103_Collaboration"] = None, Researcher: "publication103_Paper" = None, publication103_Researcher24: "publication103_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.publication103_Researcher = publication103_Researcher if publication103_Researcher is not None else set()
        self.publication103_Researcher2 = publication103_Researcher2 if publication103_Researcher2 is not None else set()
        self.authors = authors if authors is not None else set()
        self.publication103_Researcher5 = publication103_Researcher5 if publication103_Researcher5 is not None else set()
        self.publication103_Researcher7 = publication103_Researcher7
        self.publication103_Researcher9 = publication103_Researcher9 if publication103_Researcher9 is not None else set()
        self.Researcher = Researcher
        self.publication103_Researcher24 = publication103_Researcher24
        
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
        old_value = getattr(self, f"_publication103_Researcher__authors", None)
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
    def publication103_Researcher24(self):
        return self.__publication103_Researcher24

    @publication103_Researcher24.setter
    def publication103_Researcher24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__publication103_Researcher24", None)
        self.__publication103_Researcher24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_PublicationStructure"):
                opp_val = getattr(old_value, "publication103_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_PublicationStructure"):
                opp_val = getattr(value, "publication103_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication103_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication103_Researcher(self):
        return self.__publication103_Researcher

    @publication103_Researcher.setter
    def publication103_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__publication103_Researcher", None)
        self.__publication103_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication103_Write"):
                    opp_val = getattr(item, "publication103_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication103_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication103_Write"):
                    opp_val = getattr(item, "publication103_Write", None)
                    
                    setattr(item, "publication103_Write", self)
                    

    @property
    def publication103_Researcher2(self):
        return self.__publication103_Researcher2

    @publication103_Researcher2.setter
    def publication103_Researcher2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__publication103_Researcher2", None)
        self.__publication103_Researcher2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication103_Review"):
                    opp_val = getattr(item, "publication103_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication103_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication103_Review"):
                    opp_val = getattr(item, "publication103_Review", None)
                    
                    setattr(item, "publication103_Review", self)
                    

    @property
    def publication103_Researcher7(self):
        return self.__publication103_Researcher7

    @publication103_Researcher7.setter
    def publication103_Researcher7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__publication103_Researcher7", None)
        self.__publication103_Researcher7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Position"):
                opp_val = getattr(old_value, "publication103_Position", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Position"):
                opp_val = getattr(value, "publication103_Position", None)
                setattr(value, "publication103_Position", self)

    @property
    def publication103_Researcher5(self):
        return self.__publication103_Researcher5

    @publication103_Researcher5.setter
    def publication103_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__publication103_Researcher5", None)
        self.__publication103_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication103_Skill"):
                    opp_val = getattr(item, "publication103_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "publication103_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication103_Skill"):
                    opp_val = getattr(item, "publication103_Skill", None)
                    
                    setattr(item, "publication103_Skill", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__Researcher", None)
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
    def publication103_Researcher9(self):
        return self.__publication103_Researcher9

    @publication103_Researcher9.setter
    def publication103_Researcher9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Researcher__publication103_Researcher9", None)
        self.__publication103_Researcher9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication103_Collaboration"):
                    opp_val = getattr(item, "publication103_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "publication103_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication103_Collaboration"):
                    opp_val = getattr(item, "publication103_Collaboration", None)
                    
                    setattr(item, "publication103_Collaboration", self)
                    

class publication103_Collaboration:

    def __init__(self, ratio: int, publication103_Collaboration: "publication103_Researcher" = None, publication103_Collaboration35: "publication103_Paper" = None):
        self.ratio = ratio
        self.publication103_Collaboration = publication103_Collaboration
        self.publication103_Collaboration35 = publication103_Collaboration35
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def publication103_Collaboration(self):
        return self.__publication103_Collaboration

    @publication103_Collaboration.setter
    def publication103_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Collaboration__publication103_Collaboration", None)
        self.__publication103_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Researcher9"):
                opp_val = getattr(old_value, "publication103_Researcher9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Researcher9"):
                opp_val = getattr(value, "publication103_Researcher9", None)
                if opp_val is None:
                    setattr(value, "publication103_Researcher9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication103_Collaboration35(self):
        return self.__publication103_Collaboration35

    @publication103_Collaboration35.setter
    def publication103_Collaboration35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Collaboration__publication103_Collaboration35", None)
        self.__publication103_Collaboration35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Paper36"):
                opp_val = getattr(old_value, "publication103_Paper36", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Paper36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Paper36"):
                opp_val = getattr(value, "publication103_Paper36", None)
                setattr(value, "publication103_Paper36", self)

class publication103_Position(Named):

    def __init__(self, description: str, publication103_Position: "publication103_Researcher" = None, publication103_Position30: "publication103_PublicationStructure" = None, publication103_Position33: "publication103_Position" = None, publication103_Position31: "publication103_Position" = None):
        self.description = description
        self.publication103_Position = publication103_Position
        self.publication103_Position30 = publication103_Position30
        self.publication103_Position33 = publication103_Position33
        self.publication103_Position31 = publication103_Position31
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication103_Position(self):
        return self.__publication103_Position

    @publication103_Position.setter
    def publication103_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Position__publication103_Position", None)
        self.__publication103_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Researcher7"):
                opp_val = getattr(old_value, "publication103_Researcher7", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Researcher7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Researcher7"):
                opp_val = getattr(value, "publication103_Researcher7", None)
                setattr(value, "publication103_Researcher7", self)

    @property
    def publication103_Position31(self):
        return self.__publication103_Position31

    @publication103_Position31.setter
    def publication103_Position31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Position__publication103_Position31", None)
        self.__publication103_Position31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Position33"):
                opp_val = getattr(old_value, "publication103_Position33", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Position33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Position33"):
                opp_val = getattr(value, "publication103_Position33", None)
                setattr(value, "publication103_Position33", self)

    @property
    def publication103_Position30(self):
        return self.__publication103_Position30

    @publication103_Position30.setter
    def publication103_Position30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Position__publication103_Position30", None)
        self.__publication103_Position30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_PublicationStructure29"):
                opp_val = getattr(old_value, "publication103_PublicationStructure29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_PublicationStructure29"):
                opp_val = getattr(value, "publication103_PublicationStructure29", None)
                if opp_val is None:
                    setattr(value, "publication103_PublicationStructure29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication103_Position33(self):
        return self.__publication103_Position33

    @publication103_Position33.setter
    def publication103_Position33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Position__publication103_Position33", None)
        self.__publication103_Position33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Position31"):
                opp_val = getattr(old_value, "publication103_Position31", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Position31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Position31"):
                opp_val = getattr(value, "publication103_Position31", None)
                setattr(value, "publication103_Position31", self)

class publication103_Skill:

    def __init__(self, description: str, publication103_Skill: "publication103_Researcher" = None):
        self.description = description
        self.publication103_Skill = publication103_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication103_Skill(self):
        return self.__publication103_Skill

    @publication103_Skill.setter
    def publication103_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Skill__publication103_Skill", None)
        self.__publication103_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Researcher5"):
                opp_val = getattr(old_value, "publication103_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Researcher5"):
                opp_val = getattr(value, "publication103_Researcher5", None)
                if opp_val is None:
                    setattr(value, "publication103_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication103_Paper(Named):

    pass
class publication103_Review(Labelled):

    def __init__(self, date: date, publication103_Review: "publication103_Researcher" = None, publication103_Review21: "publication103_ReviewNote" = None):
        self.date = date
        self.publication103_Review = publication103_Review
        self.publication103_Review21 = publication103_Review21
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def publication103_Review(self):
        return self.__publication103_Review

    @publication103_Review.setter
    def publication103_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Review__publication103_Review", None)
        self.__publication103_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Researcher2"):
                opp_val = getattr(old_value, "publication103_Researcher2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Researcher2"):
                opp_val = getattr(value, "publication103_Researcher2", None)
                if opp_val is None:
                    setattr(value, "publication103_Researcher2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication103_Review21(self):
        return self.__publication103_Review21

    @publication103_Review21.setter
    def publication103_Review21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Review__publication103_Review21", None)
        self.__publication103_Review21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_ReviewNote22"):
                opp_val = getattr(old_value, "publication103_ReviewNote22", None)
                if opp_val == self:
                    setattr(old_value, "publication103_ReviewNote22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_ReviewNote22"):
                opp_val = getattr(value, "publication103_ReviewNote22", None)
                setattr(value, "publication103_ReviewNote22", self)

class publication103_Write(Labelled):

    def __init__(self, timeSpent: int, publication103_Write: "publication103_Researcher" = None, publication103_Write18: "publication103_Paragraph" = None):
        self.timeSpent = timeSpent
        self.publication103_Write = publication103_Write
        self.publication103_Write18 = publication103_Write18
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def publication103_Write18(self):
        return self.__publication103_Write18

    @publication103_Write18.setter
    def publication103_Write18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Write__publication103_Write18", None)
        self.__publication103_Write18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Paragraph19"):
                opp_val = getattr(old_value, "publication103_Paragraph19", None)
                if opp_val == self:
                    setattr(old_value, "publication103_Paragraph19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Paragraph19"):
                opp_val = getattr(value, "publication103_Paragraph19", None)
                setattr(value, "publication103_Paragraph19", self)

    @property
    def publication103_Write(self):
        return self.__publication103_Write

    @publication103_Write.setter
    def publication103_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication103_Write__publication103_Write", None)
        self.__publication103_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication103_Researcher"):
                opp_val = getattr(old_value, "publication103_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication103_Researcher"):
                opp_val = getattr(value, "publication103_Researcher", None)
                if opp_val is None:
                    setattr(value, "publication103_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
