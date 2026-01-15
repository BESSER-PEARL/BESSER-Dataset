from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tp5_PublicationStructure:

    pass
class tp5_Paragraph:

    def __init__(self, name: str, id: int, content: str, tp5_Paragraph: "tp5_Paper" = None):
        self.name = name
        self.id = id
        self.content = content
        self.tp5_Paragraph = tp5_Paragraph
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def tp5_Paragraph(self):
        return self.__tp5_Paragraph

    @tp5_Paragraph.setter
    def tp5_Paragraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paragraph__tp5_Paragraph", None)
        self.__tp5_Paragraph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Paper"):
                opp_val = getattr(old_value, "tp5_Paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Paper"):
                opp_val = getattr(value, "tp5_Paper", None)
                if opp_val is None:
                    setattr(value, "tp5_Paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp5_Paper:

    def __init__(self, name: str, Paper: "tp5_Researcher" = None, tp5_Paper15: "tp5_PublicationStructure" = None, tp5_Paper: set["tp5_Paragraph"] = None, res_papers: set["tp5_Researcher"] = None, tp5_Paper10: "tp5_Paper" = None, tp5_Paper8: "tp5_Paper" = None, tp5_Paper24: "tp5_Collaboration" = None):
        self.name = name
        self.Paper = Paper
        self.tp5_Paper15 = tp5_Paper15
        self.tp5_Paper = tp5_Paper if tp5_Paper is not None else set()
        self.res_papers = res_papers if res_papers is not None else set()
        self.tp5_Paper10 = tp5_Paper10
        self.tp5_Paper8 = tp5_Paper8
        self.tp5_Paper24 = tp5_Paper24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def res_papers(self):
        return self.__res_papers

    @res_papers.setter
    def res_papers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__res_papers", None)
        self.__res_papers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Researcher"):
                    opp_val = getattr(item, "Researcher", None)
                    
                    if opp_val == self:
                        setattr(item, "Researcher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Researcher"):
                    opp_val = getattr(item, "Researcher", None)
                    
                    setattr(item, "Researcher", self)
                    

    @property
    def tp5_Paper(self):
        return self.__tp5_Paper

    @tp5_Paper.setter
    def tp5_Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__tp5_Paper", None)
        self.__tp5_Paper = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp5_Paragraph"):
                    opp_val = getattr(item, "tp5_Paragraph", None)
                    
                    if opp_val == self:
                        setattr(item, "tp5_Paragraph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp5_Paragraph"):
                    opp_val = getattr(item, "tp5_Paragraph", None)
                    
                    setattr(item, "tp5_Paragraph", self)
                    

    @property
    def tp5_Paper24(self):
        return self.__tp5_Paper24

    @tp5_Paper24.setter
    def tp5_Paper24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__tp5_Paper24", None)
        self.__tp5_Paper24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Collaboration23"):
                opp_val = getattr(old_value, "tp5_Collaboration23", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Collaboration23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Collaboration23"):
                opp_val = getattr(value, "tp5_Collaboration23", None)
                setattr(value, "tp5_Collaboration23", self)

    @property
    def tp5_Paper8(self):
        return self.__tp5_Paper8

    @tp5_Paper8.setter
    def tp5_Paper8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__tp5_Paper8", None)
        self.__tp5_Paper8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Paper10"):
                opp_val = getattr(old_value, "tp5_Paper10", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Paper10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Paper10"):
                opp_val = getattr(value, "tp5_Paper10", None)
                setattr(value, "tp5_Paper10", self)

    @property
    def tp5_Paper10(self):
        return self.__tp5_Paper10

    @tp5_Paper10.setter
    def tp5_Paper10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__tp5_Paper10", None)
        self.__tp5_Paper10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Paper8"):
                opp_val = getattr(old_value, "tp5_Paper8", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Paper8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Paper8"):
                opp_val = getattr(value, "tp5_Paper8", None)
                setattr(value, "tp5_Paper8", self)

    @property
    def Paper(self):
        return self.__Paper

    @Paper.setter
    def Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__Paper", None)
        self.__Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp5_Paper15(self):
        return self.__tp5_Paper15

    @tp5_Paper15.setter
    def tp5_Paper15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Paper__tp5_Paper15", None)
        self.__tp5_Paper15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_PublicationStructure14"):
                opp_val = getattr(old_value, "tp5_PublicationStructure14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_PublicationStructure14"):
                opp_val = getattr(value, "tp5_PublicationStructure14", None)
                if opp_val is None:
                    setattr(value, "tp5_PublicationStructure14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp5_Researcher:

    def __init__(self, name: str, forName: str, tp5_Researcher: set["tp5_Skill"] = None, tp5_Researcher3: "tp5_Position" = None, tp5_Researcher5: set["tp5_Collaboration"] = None, authors: set["tp5_Paper"] = None, Researcher: "tp5_Paper" = None, tp5_Researcher12: "tp5_PublicationStructure" = None):
        self.name = name
        self.forName = forName
        self.tp5_Researcher = tp5_Researcher if tp5_Researcher is not None else set()
        self.tp5_Researcher3 = tp5_Researcher3
        self.tp5_Researcher5 = tp5_Researcher5 if tp5_Researcher5 is not None else set()
        self.authors = authors if authors is not None else set()
        self.Researcher = Researcher
        self.tp5_Researcher12 = tp5_Researcher12
        
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
    def tp5_Researcher12(self):
        return self.__tp5_Researcher12

    @tp5_Researcher12.setter
    def tp5_Researcher12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Researcher__tp5_Researcher12", None)
        self.__tp5_Researcher12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_PublicationStructure"):
                opp_val = getattr(old_value, "tp5_PublicationStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_PublicationStructure"):
                opp_val = getattr(value, "tp5_PublicationStructure", None)
                if opp_val is None:
                    setattr(value, "tp5_PublicationStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Researcher__authors", None)
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
    def tp5_Researcher5(self):
        return self.__tp5_Researcher5

    @tp5_Researcher5.setter
    def tp5_Researcher5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Researcher__tp5_Researcher5", None)
        self.__tp5_Researcher5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp5_Collaboration"):
                    opp_val = getattr(item, "tp5_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "tp5_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp5_Collaboration"):
                    opp_val = getattr(item, "tp5_Collaboration", None)
                    
                    setattr(item, "tp5_Collaboration", self)
                    

    @property
    def tp5_Researcher3(self):
        return self.__tp5_Researcher3

    @tp5_Researcher3.setter
    def tp5_Researcher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Researcher__tp5_Researcher3", None)
        self.__tp5_Researcher3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Position"):
                opp_val = getattr(old_value, "tp5_Position", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Position"):
                opp_val = getattr(value, "tp5_Position", None)
                setattr(value, "tp5_Position", self)

    @property
    def Researcher(self):
        return self.__Researcher

    @Researcher.setter
    def Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Researcher__Researcher", None)
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
    def tp5_Researcher(self):
        return self.__tp5_Researcher

    @tp5_Researcher.setter
    def tp5_Researcher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Researcher__tp5_Researcher", None)
        self.__tp5_Researcher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tp5_Skill"):
                    opp_val = getattr(item, "tp5_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "tp5_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tp5_Skill"):
                    opp_val = getattr(item, "tp5_Skill", None)
                    
                    setattr(item, "tp5_Skill", self)
                    

class tp5_Collaboration:

    def __init__(self, ratio: int, tp5_Collaboration: "tp5_Researcher" = None, tp5_Collaboration23: "tp5_Paper" = None):
        self.ratio = ratio
        self.tp5_Collaboration = tp5_Collaboration
        self.tp5_Collaboration23 = tp5_Collaboration23
        
    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def tp5_Collaboration(self):
        return self.__tp5_Collaboration

    @tp5_Collaboration.setter
    def tp5_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Collaboration__tp5_Collaboration", None)
        self.__tp5_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Researcher5"):
                opp_val = getattr(old_value, "tp5_Researcher5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Researcher5"):
                opp_val = getattr(value, "tp5_Researcher5", None)
                if opp_val is None:
                    setattr(value, "tp5_Researcher5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tp5_Collaboration23(self):
        return self.__tp5_Collaboration23

    @tp5_Collaboration23.setter
    def tp5_Collaboration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Collaboration__tp5_Collaboration23", None)
        self.__tp5_Collaboration23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Paper24"):
                opp_val = getattr(old_value, "tp5_Paper24", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Paper24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Paper24"):
                opp_val = getattr(value, "tp5_Paper24", None)
                setattr(value, "tp5_Paper24", self)

class tp5_Position:

    def __init__(self, name: str, description: str, tp5_Position: "tp5_Researcher" = None, tp5_Position18: "tp5_PublicationStructure" = None, tp5_Position21: "tp5_Position" = None, tp5_Position19: "tp5_Position" = None):
        self.name = name
        self.description = description
        self.tp5_Position = tp5_Position
        self.tp5_Position18 = tp5_Position18
        self.tp5_Position21 = tp5_Position21
        self.tp5_Position19 = tp5_Position19
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tp5_Position21(self):
        return self.__tp5_Position21

    @tp5_Position21.setter
    def tp5_Position21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Position__tp5_Position21", None)
        self.__tp5_Position21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Position19"):
                opp_val = getattr(old_value, "tp5_Position19", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Position19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Position19"):
                opp_val = getattr(value, "tp5_Position19", None)
                setattr(value, "tp5_Position19", self)

    @property
    def tp5_Position19(self):
        return self.__tp5_Position19

    @tp5_Position19.setter
    def tp5_Position19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Position__tp5_Position19", None)
        self.__tp5_Position19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Position21"):
                opp_val = getattr(old_value, "tp5_Position21", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Position21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Position21"):
                opp_val = getattr(value, "tp5_Position21", None)
                setattr(value, "tp5_Position21", self)

    @property
    def tp5_Position(self):
        return self.__tp5_Position

    @tp5_Position.setter
    def tp5_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Position__tp5_Position", None)
        self.__tp5_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Researcher3"):
                opp_val = getattr(old_value, "tp5_Researcher3", None)
                if opp_val == self:
                    setattr(old_value, "tp5_Researcher3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Researcher3"):
                opp_val = getattr(value, "tp5_Researcher3", None)
                setattr(value, "tp5_Researcher3", self)

    @property
    def tp5_Position18(self):
        return self.__tp5_Position18

    @tp5_Position18.setter
    def tp5_Position18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Position__tp5_Position18", None)
        self.__tp5_Position18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_PublicationStructure17"):
                opp_val = getattr(old_value, "tp5_PublicationStructure17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_PublicationStructure17"):
                opp_val = getattr(value, "tp5_PublicationStructure17", None)
                if opp_val is None:
                    setattr(value, "tp5_PublicationStructure17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tp5_Skill:

    def __init__(self, description: str, tp5_Skill: "tp5_Researcher" = None):
        self.description = description
        self.tp5_Skill = tp5_Skill
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def tp5_Skill(self):
        return self.__tp5_Skill

    @tp5_Skill.setter
    def tp5_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tp5_Skill__tp5_Skill", None)
        self.__tp5_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tp5_Researcher"):
                opp_val = getattr(old_value, "tp5_Researcher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tp5_Researcher"):
                opp_val = getattr(value, "tp5_Researcher", None)
                if opp_val is None:
                    setattr(value, "tp5_Researcher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
