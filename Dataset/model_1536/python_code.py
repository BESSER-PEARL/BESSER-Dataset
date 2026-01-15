from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class publication105_Counted(ABC):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class publication105_Labelled(ABC):

    def __init__(self, lname: str):
        self.lname = lname
        
    @property
    def lname(self) -> str:
        return self.__lname

    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

class Labelled:

    pass
class publication105_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class publication105_Collaboration:

    def __init__(self, ratio: int, publication105_Collaboration: "publication105_Researcher" = None, publication105_Collaboration35: "publication105_Paper" = None):
        self.ratio = ratio
        self.publication105_Collaboration = publication105_Collaboration
        self.publication105_Collaboration35 = publication105_Collaboration35
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def publication105_Collaboration(self):
        return self.__publication105_Collaboration

    @publication105_Collaboration.setter
    def publication105_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Collaboration__publication105_Collaboration", None)
        self.__publication105_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Researcher9"):
                opp_val = getattr(old_value, "publication105_Researcher9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Researcher9"):
                opp_val = getattr(value, "publication105_Researcher9", None)
                if opp_val is None:
                    setattr(value, "publication105_Researcher9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication105_Collaboration35(self):
        return self.__publication105_Collaboration35

    @publication105_Collaboration35.setter
    def publication105_Collaboration35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Collaboration__publication105_Collaboration35", None)
        self.__publication105_Collaboration35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Paper36"):
                opp_val = getattr(old_value, "publication105_Paper36", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Paper36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Paper36"):
                opp_val = getattr(value, "publication105_Paper36", None)
                setattr(value, "publication105_Paper36", self)

class Counted:

    pass
class Named:

    pass
class publication105_PublicationStructure(Named):

    pass
class publication105_Paragraph(Counted, Named):

    def __init__(self, content: str, publication105_Paragraph: "publication105_Paper" = None, publication105_Paragraph16: set["publication105_ReviewNote"] = None, publication105_Paragraph19: "publication105_Write" = None):
        self.content = content
        self.publication105_Paragraph = publication105_Paragraph
        self.publication105_Paragraph16 = publication105_Paragraph16 if publication105_Paragraph16 is not None else set()
        self.publication105_Paragraph19 = publication105_Paragraph19
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication105_Paragraph16(self):
        return self.__publication105_Paragraph16

    @publication105_Paragraph16.setter
    def publication105_Paragraph16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Paragraph__publication105_Paragraph16", None)
        self.__publication105_Paragraph16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication105_ReviewNote"):
                    opp_val = getattr(item, "publication105_ReviewNote", None)
                    
                    if opp_val == self:
                        setattr(item, "publication105_ReviewNote", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication105_ReviewNote"):
                    opp_val = getattr(item, "publication105_ReviewNote", None)
                    
                    setattr(item, "publication105_ReviewNote", self)
                    

    @property
    def publication105_Paragraph19(self):
        return self.__publication105_Paragraph19

    @publication105_Paragraph19.setter
    def publication105_Paragraph19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Paragraph__publication105_Paragraph19", None)
        self.__publication105_Paragraph19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Write18"):
                opp_val = getattr(old_value, "publication105_Write18", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Write18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Write18"):
                opp_val = getattr(value, "publication105_Write18", None)
                setattr(value, "publication105_Write18", self)

    @property
    def publication105_Paragraph(self):
        return self.__publication105_Paragraph

    @publication105_Paragraph.setter
    def publication105_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Paragraph__publication105_Paragraph", None)
        self.__publication105_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Paper"):
                opp_val = getattr(old_value, "publication105_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Paper"):
                opp_val = getattr(value, "publication105_Paper", None)
                if opp_val is None:
                    setattr(value, "publication105_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication105_ReviewNote(Named):

    def __init__(self, content: str, publication105_ReviewNote: "publication105_Paragraph" = None, publication105_ReviewNote22: "publication105_Review" = None):
        self.content = content
        self.publication105_ReviewNote = publication105_ReviewNote
        self.publication105_ReviewNote22 = publication105_ReviewNote22
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def publication105_ReviewNote22(self):
        return self.__publication105_ReviewNote22

    @publication105_ReviewNote22.setter
    def publication105_ReviewNote22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_ReviewNote__publication105_ReviewNote22", None)
        self.__publication105_ReviewNote22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Review21"):
                opp_val = getattr(old_value, "publication105_Review21", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Review21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Review21"):
                opp_val = getattr(value, "publication105_Review21", None)
                setattr(value, "publication105_Review21", self)

    @property
    def publication105_ReviewNote(self):
        return self.__publication105_ReviewNote

    @publication105_ReviewNote.setter
    def publication105_ReviewNote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_ReviewNote__publication105_ReviewNote", None)
        self.__publication105_ReviewNote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Paragraph16"):
                opp_val = getattr(old_value, "publication105_Paragraph16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Paragraph16"):
                opp_val = getattr(value, "publication105_Paragraph16", None)
                if opp_val is None:
                    setattr(value, "publication105_Paragraph16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication105_Position(Named):

    def __init__(self, description: str, publication105_Position: "publication105_Researcher" = None, publication105_Position30: "publication105_PublicationStructure" = None, publication105_Position33: "publication105_Position" = None, publication105_Position31: "publication105_Position" = None):
        self.description = description
        self.publication105_Position = publication105_Position
        self.publication105_Position30 = publication105_Position30
        self.publication105_Position33 = publication105_Position33
        self.publication105_Position31 = publication105_Position31
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication105_Position33(self):
        return self.__publication105_Position33

    @publication105_Position33.setter
    def publication105_Position33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Position__publication105_Position33", None)
        self.__publication105_Position33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Position31"):
                opp_val = getattr(old_value, "publication105_Position31", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Position31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Position31"):
                opp_val = getattr(value, "publication105_Position31", None)
                setattr(value, "publication105_Position31", self)

    @property
    def publication105_Position31(self):
        return self.__publication105_Position31

    @publication105_Position31.setter
    def publication105_Position31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Position__publication105_Position31", None)
        self.__publication105_Position31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Position33"):
                opp_val = getattr(old_value, "publication105_Position33", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Position33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Position33"):
                opp_val = getattr(value, "publication105_Position33", None)
                setattr(value, "publication105_Position33", self)

    @property
    def publication105_Position30(self):
        return self.__publication105_Position30

    @publication105_Position30.setter
    def publication105_Position30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Position__publication105_Position30", None)
        self.__publication105_Position30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_PublicationStructure29"):
                opp_val = getattr(old_value, "publication105_PublicationStructure29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_PublicationStructure29"):
                opp_val = getattr(value, "publication105_PublicationStructure29", None)
                if opp_val is None:
                    setattr(value, "publication105_PublicationStructure29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication105_Position(self):
        return self.__publication105_Position

    @publication105_Position.setter
    def publication105_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Position__publication105_Position", None)
        self.__publication105_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Researcher7"):
                opp_val = getattr(old_value, "publication105_Researcher7", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Researcher7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Researcher7"):
                opp_val = getattr(value, "publication105_Researcher7", None)
                setattr(value, "publication105_Researcher7", self)

class publication105_Skill:

    def __init__(self, description: str, publication105_Skill: "publication105_Researcher" = None):
        self.description = description
        self.publication105_Skill = publication105_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publication105_Skill(self):
        return self.__publication105_Skill

    @publication105_Skill.setter
    def publication105_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Skill__publication105_Skill", None)
        self.__publication105_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Researcher5"):
                opp_val = getattr(old_value, "publication105_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Researcher5"):
                opp_val = getattr(value, "publication105_Researcher5", None)
                if opp_val is None:
                    setattr(value, "publication105_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication105_Paper(Named):

    pass
class publication105_Review(Labelled):

    def __init__(self, date: date, publication105_Review: "publication105_Researcher" = None, publication105_Review21: "publication105_ReviewNote" = None):
        self.date = date
        self.publication105_Review = publication105_Review
        self.publication105_Review21 = publication105_Review21
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def publication105_Review(self):
        return self.__publication105_Review

    @publication105_Review.setter
    def publication105_Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Review__publication105_Review", None)
        self.__publication105_Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Researcher2"):
                opp_val = getattr(old_value, "publication105_Researcher2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Researcher2"):
                opp_val = getattr(value, "publication105_Researcher2", None)
                if opp_val is None:
                    setattr(value, "publication105_Researcher2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication105_Review21(self):
        return self.__publication105_Review21

    @publication105_Review21.setter
    def publication105_Review21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Review__publication105_Review21", None)
        self.__publication105_Review21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_ReviewNote22"):
                opp_val = getattr(old_value, "publication105_ReviewNote22", None)
                if opp_val == self:
                    setattr(old_value, "publication105_ReviewNote22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_ReviewNote22"):
                opp_val = getattr(value, "publication105_ReviewNote22", None)
                setattr(value, "publication105_ReviewNote22", self)

class publication105_Write(Labelled):

    def __init__(self, timeSpent: int, publication105_Write: "publication105_Researcher" = None, publication105_Write18: "publication105_Paragraph" = None):
        self.timeSpent = timeSpent
        self.publication105_Write = publication105_Write
        self.publication105_Write18 = publication105_Write18
        
    @property
    def timeSpent(self) -> int:
        return self.__timeSpent

    @timeSpent.setter
    def timeSpent(self, timeSpent: int):
        self.__timeSpent = timeSpent

    @property
    def publication105_Write18(self):
        return self.__publication105_Write18

    @publication105_Write18.setter
    def publication105_Write18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Write__publication105_Write18", None)
        self.__publication105_Write18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Paragraph19"):
                opp_val = getattr(old_value, "publication105_Paragraph19", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Paragraph19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Paragraph19"):
                opp_val = getattr(value, "publication105_Paragraph19", None)
                setattr(value, "publication105_Paragraph19", self)

    @property
    def publication105_Write(self):
        return self.__publication105_Write

    @publication105_Write.setter
    def publication105_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Write__publication105_Write", None)
        self.__publication105_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Researcher"):
                opp_val = getattr(old_value, "publication105_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Researcher"):
                opp_val = getattr(value, "publication105_Researcher", None)
                if opp_val is None:
                    setattr(value, "publication105_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class publication105_Researcher:

    def __init__(self, name: str, forName: str, publication105_Researcher: set["publication105_Write"] = None, publication105_Researcher2: set["publication105_Review"] = None, authors: set["publication105_Paper"] = None, publication105_Researcher5: set["publication105_Skill"] = None, Researcher: "publication105_Paper" = None, publication105_Researcher7: "publication105_Position" = None, publication105_Researcher9: set["publication105_Collaboration"] = None, publication105_Researcher24: "publication105_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.publication105_Researcher = publication105_Researcher if publication105_Researcher is not None else set()
        self.publication105_Researcher2 = publication105_Researcher2 if publication105_Researcher2 is not None else set()
        self.authors = authors if authors is not None else set()
        self.publication105_Researcher5 = publication105_Researcher5 if publication105_Researcher5 is not None else set()
        self.Researcher = Researcher
        self.publication105_Researcher7 = publication105_Researcher7
        self.publication105_Researcher9 = publication105_Researcher9 if publication105_Researcher9 is not None else set()
        self.publication105_Researcher24 = publication105_Researcher24
        
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
    def publication105_Researcher5(self):
        return self.__publication105_Researcher5

    @publication105_Researcher5.setter
    def publication105_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__publication105_Researcher5", None)
        self.__publication105_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication105_Skill"):
                    opp_val = getattr(item, "publication105_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "publication105_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication105_Skill"):
                    opp_val = getattr(item, "publication105_Skill", None)
                    
                    setattr(item, "publication105_Skill", self)
                    

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__Researcher", None)
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
    def publication105_Researcher9(self):
        return self.__publication105_Researcher9

    @publication105_Researcher9.setter
    def publication105_Researcher9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__publication105_Researcher9", None)
        self.__publication105_Researcher9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication105_Collaboration"):
                    opp_val = getattr(item, "publication105_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "publication105_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication105_Collaboration"):
                    opp_val = getattr(item, "publication105_Collaboration", None)
                    
                    setattr(item, "publication105_Collaboration", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__authors", None)
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
    def publication105_Researcher(self):
        return self.__publication105_Researcher

    @publication105_Researcher.setter
    def publication105_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__publication105_Researcher", None)
        self.__publication105_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication105_Write"):
                    opp_val = getattr(item, "publication105_Write", None)
                    
                    if opp_val == self:
                        setattr(item, "publication105_Write", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication105_Write"):
                    opp_val = getattr(item, "publication105_Write", None)
                    
                    setattr(item, "publication105_Write", self)
                    

    @property
    def publication105_Researcher24(self):
        return self.__publication105_Researcher24

    @publication105_Researcher24.setter
    def publication105_Researcher24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__publication105_Researcher24", None)
        self.__publication105_Researcher24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_PublicationStructure"):
                opp_val = getattr(old_value, "publication105_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_PublicationStructure"):
                opp_val = getattr(value, "publication105_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "publication105_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def publication105_Researcher7(self):
        return self.__publication105_Researcher7

    @publication105_Researcher7.setter
    def publication105_Researcher7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__publication105_Researcher7", None)
        self.__publication105_Researcher7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publication105_Position"):
                opp_val = getattr(old_value, "publication105_Position", None)
                if opp_val == self:
                    setattr(old_value, "publication105_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publication105_Position"):
                opp_val = getattr(value, "publication105_Position", None)
                setattr(value, "publication105_Position", self)

    @property
    def publication105_Researcher2(self):
        return self.__publication105_Researcher2

    @publication105_Researcher2.setter
    def publication105_Researcher2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_publication105_Researcher__publication105_Researcher2", None)
        self.__publication105_Researcher2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "publication105_Review"):
                    opp_val = getattr(item, "publication105_Review", None)
                    
                    if opp_val == self:
                        setattr(item, "publication105_Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "publication105_Review"):
                    opp_val = getattr(item, "publication105_Review", None)
                    
                    setattr(item, "publication105_Review", self)
                    
