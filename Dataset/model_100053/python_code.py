from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class research_team_TypeCollaboration:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class research_team_Partner:

    def __init__(self, name: str, country: str, category: str, partners: set["research_team_Collaboration"] = None):
        self.name = name
        self.country = country
        self.category = category
        self.partners = partners if partners is not None else set()
        
        pass
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def partners(self):
        return self.__partners

    @partners.setter
    def partners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Partner__partners", None)
        self.__partners = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Collaboration28"):
                    opp_val = getattr(item, "Collaboration28", None)
                    
                    if opp_val == self:
                        setattr(item, "Collaboration28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Collaboration28"):
                    opp_val = getattr(item, "Collaboration28", None)
                    
                    setattr(item, "Collaboration28", self)
                    

class research_team_CallForPaper:

    def __init__(self, title: str, category: str, deadline: str, url: str):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.url = url
        
        pass
    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, deadline: str):
        self.__deadline = deadline


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


class research_team_Section:

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class Publication:

    pass
class research_team_PhDThesis(Publication):

    pass
class research_team_Misc(Publication):

    pass
class research_team_InProceedings(Publication):

    pass
class research_team_MasterThesis(Publication):

    pass
class research_team_Article(Publication):

    pass
class research_team_Paper:

    def __init__(self, title: str, url4pdf: str, state: str, Paper: "research_team_Person" = None, research_team_Paper: "research_team_Publication" = None, publishedAs: set["research_team_Publication"] = None, paper: set["research_team_Person"] = None):
        self.title = title
        self.url4pdf = url4pdf
        self.state = state
        self.Paper = Paper
        self.research_team_Paper = research_team_Paper
        self.publishedAs = publishedAs if publishedAs is not None else set()
        self.paper = paper if paper is not None else set()
        
        pass
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def url4pdf(self):
        return self.__url4pdf

    @url4pdf.setter
    def url4pdf(self, url4pdf: str):
        self.__url4pdf = url4pdf


    @property
    def research_team_Paper(self):
        return self.__research_team_Paper

    @research_team_Paper.setter
    def research_team_Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Paper__research_team_Paper", None)
        self.__research_team_Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Publication"):
                opp_val = getattr(old_value, "research_team_Publication", None)
                if opp_val == self:
                    setattr(old_value, "research_team_Publication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Publication"):
                opp_val = getattr(value, "research_team_Publication", None)
                setattr(value, "research_team_Publication", self)

    @property
    def publishedAs(self):
        return self.__publishedAs

    @publishedAs.setter
    def publishedAs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Paper__publishedAs", None)
        self.__publishedAs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Publication22"):
                    opp_val = getattr(item, "Publication22", None)
                    
                    if opp_val == self:
                        setattr(item, "Publication22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Publication22"):
                    opp_val = getattr(item, "Publication22", None)
                    
                    setattr(item, "Publication22", self)
                    

    @property
    def paper(self):
        return self.__paper

    @paper.setter
    def paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Paper__paper", None)
        self.__paper = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person24"):
                    opp_val = getattr(item, "Person24", None)
                    
                    if opp_val == self:
                        setattr(item, "Person24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person24"):
                    opp_val = getattr(item, "Person24", None)
                    
                    setattr(item, "Person24", self)
                    

    @property
    def Paper(self):
        return self.__Paper

    @Paper.setter
    def Paper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Paper__Paper", None)
        self.__Paper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_team_Seminar:

    def __init__(self, title: str, abstract: str, place: str, dateFrom: str, dateUntil: str, url4slides: str, Seminar: "research_team_Person" = None, seminars: set["research_team_Person"] = None):
        self.title = title
        self.abstract = abstract
        self.place = place
        self.dateFrom = dateFrom
        self.dateUntil = dateUntil
        self.url4slides = url4slides
        self.Seminar = Seminar
        self.seminars = seminars if seminars is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def dateUntil(self):
        return self.__dateUntil

    @dateUntil.setter
    def dateUntil(self, dateUntil: str):
        self.__dateUntil = dateUntil


    @property
    def dateFrom(self):
        return self.__dateFrom

    @dateFrom.setter
    def dateFrom(self, dateFrom: str):
        self.__dateFrom = dateFrom


    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, place: str):
        self.__place = place


    @property
    def url4slides(self):
        return self.__url4slides

    @url4slides.setter
    def url4slides(self, url4slides: str):
        self.__url4slides = url4slides


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def Seminar(self):
        return self.__Seminar

    @Seminar.setter
    def Seminar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Seminar__Seminar", None)
        self.__Seminar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers"):
                opp_val = getattr(old_value, "speakers", None)
                if opp_val == self:
                    setattr(old_value, "speakers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers"):
                opp_val = getattr(value, "speakers", None)
                setattr(value, "speakers", self)

    @property
    def seminars(self):
        return self.__seminars

    @seminars.setter
    def seminars(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Seminar__seminars", None)
        self.__seminars = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

class research_team_Software:

    def __init__(self, website: str, title: str, description: str, Software: "research_team_Person" = None, soft: set["research_team_Person"] = None):
        self.website = website
        self.title = title
        self.description = description
        self.Software = Software
        self.soft = soft if soft is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, website: str):
        self.__website = website


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def soft(self):
        return self.__soft

    @soft.setter
    def soft(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Software__soft", None)
        self.__soft = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person26"):
                    opp_val = getattr(item, "Person26", None)
                    
                    if opp_val == self:
                        setattr(item, "Person26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person26"):
                    opp_val = getattr(item, "Person26", None)
                    
                    setattr(item, "Person26", self)
                    

    @property
    def Software(self):
        return self.__Software

    @Software.setter
    def Software(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Software__Software", None)
        self.__Software = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "developers"):
                opp_val = getattr(old_value, "developers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "developers"):
                opp_val = getattr(value, "developers", None)
                if opp_val is None:
                    setattr(value, "developers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_team_Publication:

    def __init__(self, Publication: "research_team_Team" = None, mainReferences: "research_team_Team" = None, research_team_Publication: "research_team_Paper" = None, Publication22: "research_team_Paper" = None):
        self.Publication = Publication
        self.mainReferences = mainReferences
        self.research_team_Publication = research_team_Publication
        self.Publication22 = Publication22
        
        pass
    @property
    def research_team_Publication(self):
        return self.__research_team_Publication

    @research_team_Publication.setter
    def research_team_Publication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Publication__research_team_Publication", None)
        self.__research_team_Publication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Paper"):
                opp_val = getattr(old_value, "research_team_Paper", None)
                if opp_val == self:
                    setattr(old_value, "research_team_Paper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Paper"):
                opp_val = getattr(value, "research_team_Paper", None)
                setattr(value, "research_team_Paper", self)

    @property
    def Publication22(self):
        return self.__Publication22

    @Publication22.setter
    def Publication22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Publication__Publication22", None)
        self.__Publication22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publishedAs"):
                opp_val = getattr(old_value, "publishedAs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publishedAs"):
                opp_val = getattr(value, "publishedAs", None)
                if opp_val is None:
                    setattr(value, "publishedAs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mainReferences(self):
        return self.__mainReferences

    @mainReferences.setter
    def mainReferences(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Publication__mainReferences", None)
        self.__mainReferences = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Team"):
                opp_val = getattr(old_value, "Team", None)
                if opp_val == self:
                    setattr(old_value, "Team", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Team"):
                opp_val = getattr(value, "Team", None)
                setattr(value, "Team", self)

    @property
    def Publication(self):
        return self.__Publication

    @Publication.setter
    def Publication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Publication__Publication", None)
        self.__Publication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team"):
                opp_val = getattr(old_value, "team", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team"):
                opp_val = getattr(value, "team", None)
                if opp_val is None:
                    setattr(value, "team", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getBibtex(self) :
        # TODO: Implement getBibtex method
        pass

    def getEndnote(self) :
        # TODO: Implement getEndnote method
        pass

class research_team_Collaboration:

    def __init__(self, website: str, title: str, status: str, from_: str, until: str, research_team_Collaboration: "research_team_Team" = None, research_team_Collaboration16: "research_team_Person" = None, Collaboration: "research_team_OpenPosition" = None, Collaboration28: "research_team_Partner" = None):
        self.website = website
        self.title = title
        self.status = status
        self.from_ = from_
        self.until = until
        self.research_team_Collaboration = research_team_Collaboration
        self.research_team_Collaboration16 = research_team_Collaboration16
        self.Collaboration = Collaboration
        self.Collaboration28 = Collaboration28
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_


    @property
    def until(self):
        return self.__until

    @until.setter
    def until(self, until: str):
        self.__until = until


    @property
    def website(self):
        return self.__website

    @website.setter
    def website(self, website: str):
        self.__website = website


    @property
    def Collaboration(self):
        return self.__Collaboration

    @Collaboration.setter
    def Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Collaboration__Collaboration", None)
        self.__Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "openPositions"):
                opp_val = getattr(old_value, "openPositions", None)
                if opp_val == self:
                    setattr(old_value, "openPositions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "openPositions"):
                opp_val = getattr(value, "openPositions", None)
                setattr(value, "openPositions", self)

    @property
    def Collaboration28(self):
        return self.__Collaboration28

    @Collaboration28.setter
    def Collaboration28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Collaboration__Collaboration28", None)
        self.__Collaboration28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partners"):
                opp_val = getattr(old_value, "partners", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partners"):
                opp_val = getattr(value, "partners", None)
                if opp_val is None:
                    setattr(value, "partners", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_team_Collaboration(self):
        return self.__research_team_Collaboration

    @research_team_Collaboration.setter
    def research_team_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Collaboration__research_team_Collaboration", None)
        self.__research_team_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Team9"):
                opp_val = getattr(old_value, "research_team_Team9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Team9"):
                opp_val = getattr(value, "research_team_Team9", None)
                if opp_val is None:
                    setattr(value, "research_team_Team9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_team_Collaboration16(self):
        return self.__research_team_Collaboration16

    @research_team_Collaboration16.setter
    def research_team_Collaboration16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Collaboration__research_team_Collaboration16", None)
        self.__research_team_Collaboration16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Person15"):
                opp_val = getattr(old_value, "research_team_Person15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Person15"):
                opp_val = getattr(value, "research_team_Person15", None)
                if opp_val is None:
                    setattr(value, "research_team_Person15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class research_team_OpenPosition:

    def __init__(self, status: str, mission: str, duration: str, research_team_OpenPosition: "research_team_Team" = None, openPositions: "research_team_Collaboration" = None):
        self.status = status
        self.mission = mission
        self.duration = duration
        self.research_team_OpenPosition = research_team_OpenPosition
        self.openPositions = openPositions
        
        pass
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def mission(self):
        return self.__mission

    @mission.setter
    def mission(self, mission: str):
        self.__mission = mission


    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration


    @property
    def research_team_OpenPosition(self):
        return self.__research_team_OpenPosition

    @research_team_OpenPosition.setter
    def research_team_OpenPosition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_OpenPosition__research_team_OpenPosition", None)
        self.__research_team_OpenPosition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Team7"):
                opp_val = getattr(old_value, "research_team_Team7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Team7"):
                opp_val = getattr(value, "research_team_Team7", None)
                if opp_val is None:
                    setattr(value, "research_team_Team7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def openPositions(self):
        return self.__openPositions

    @openPositions.setter
    def openPositions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_OpenPosition__openPositions", None)
        self.__openPositions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Collaboration"):
                opp_val = getattr(old_value, "Collaboration", None)
                if opp_val == self:
                    setattr(old_value, "Collaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Collaboration"):
                opp_val = getattr(value, "Collaboration", None)
                setattr(value, "Collaboration", self)

class research_team_Person:

    def __init__(self, name: str, firstname: str, affiliation: str, phone: str, mail: str, research_team_Person: "research_team_Team" = None, research_team_Person5: "research_team_Team" = None, developers: set["research_team_Software"] = None, speakers: "research_team_Seminar" = None, author: set["research_team_Paper"] = None, research_team_Person15: set["research_team_Collaboration"] = None, Person: "research_team_Seminar" = None, Person24: "research_team_Paper" = None, Person26: "research_team_Software" = None):
        self.name = name
        self.firstname = firstname
        self.affiliation = affiliation
        self.phone = phone
        self.mail = mail
        self.research_team_Person = research_team_Person
        self.research_team_Person5 = research_team_Person5
        self.developers = developers if developers is not None else set()
        self.speakers = speakers
        self.author = author if author is not None else set()
        self.research_team_Person15 = research_team_Person15 if research_team_Person15 is not None else set()
        self.Person = Person
        self.Person24 = Person24
        self.Person26 = Person26
        
        pass
    @property
    def affiliation(self):
        return self.__affiliation

    @affiliation.setter
    def affiliation(self, affiliation: str):
        self.__affiliation = affiliation


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


    @property
    def mail(self):
        return self.__mail

    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    @property
    def research_team_Person15(self):
        return self.__research_team_Person15

    @research_team_Person15.setter
    def research_team_Person15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__research_team_Person15", None)
        self.__research_team_Person15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_team_Collaboration16"):
                    opp_val = getattr(item, "research_team_Collaboration16", None)
                    
                    if opp_val == self:
                        setattr(item, "research_team_Collaboration16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_team_Collaboration16"):
                    opp_val = getattr(item, "research_team_Collaboration16", None)
                    
                    setattr(item, "research_team_Collaboration16", self)
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seminars"):
                opp_val = getattr(old_value, "seminars", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seminars"):
                opp_val = getattr(value, "seminars", None)
                if opp_val is None:
                    setattr(value, "seminars", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def research_team_Person(self):
        return self.__research_team_Person

    @research_team_Person.setter
    def research_team_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__research_team_Person", None)
        self.__research_team_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Team2"):
                opp_val = getattr(old_value, "research_team_Team2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Team2"):
                opp_val = getattr(value, "research_team_Team2", None)
                if opp_val is None:
                    setattr(value, "research_team_Team2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person26(self):
        return self.__Person26

    @Person26.setter
    def Person26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__Person26", None)
        self.__Person26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soft"):
                opp_val = getattr(old_value, "soft", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soft"):
                opp_val = getattr(value, "soft", None)
                if opp_val is None:
                    setattr(value, "soft", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def speakers(self):
        return self.__speakers

    @speakers.setter
    def speakers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__speakers", None)
        self.__speakers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Seminar"):
                opp_val = getattr(old_value, "Seminar", None)
                if opp_val == self:
                    setattr(old_value, "Seminar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Seminar"):
                opp_val = getattr(value, "Seminar", None)
                setattr(value, "Seminar", self)

    @property
    def research_team_Person5(self):
        return self.__research_team_Person5

    @research_team_Person5.setter
    def research_team_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__research_team_Person5", None)
        self.__research_team_Person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Team4"):
                opp_val = getattr(old_value, "research_team_Team4", None)
                if opp_val == self:
                    setattr(old_value, "research_team_Team4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Team4"):
                opp_val = getattr(value, "research_team_Team4", None)
                setattr(value, "research_team_Team4", self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__author", None)
        self.__author = value if value is not None else set()
        
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
    def Person24(self):
        return self.__Person24

    @Person24.setter
    def Person24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__Person24", None)
        self.__Person24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paper"):
                opp_val = getattr(old_value, "paper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paper"):
                opp_val = getattr(value, "paper", None)
                if opp_val is None:
                    setattr(value, "paper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def developers(self):
        return self.__developers

    @developers.setter
    def developers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Person__developers", None)
        self.__developers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Software"):
                    opp_val = getattr(item, "Software", None)
                    
                    if opp_val == self:
                        setattr(item, "Software", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Software"):
                    opp_val = getattr(item, "Software", None)
                    
                    setattr(item, "Software", self)
                    

class research_team_ActivityReport:

    pass
class research_team_Team:

    def __init__(self, name: str, meaning: str, status: str, urlPage: str, research_team_Team: set["research_team_ActivityReport"] = None, research_team_Team2: set["research_team_Person"] = None, research_team_Team4: "research_team_Person" = None, research_team_Team7: set["research_team_OpenPosition"] = None, research_team_Team9: set["research_team_Collaboration"] = None, team: set["research_team_Publication"] = None, Team: "research_team_Publication" = None):
        self.name = name
        self.meaning = meaning
        self.status = status
        self.urlPage = urlPage
        self.research_team_Team = research_team_Team if research_team_Team is not None else set()
        self.research_team_Team2 = research_team_Team2 if research_team_Team2 is not None else set()
        self.research_team_Team4 = research_team_Team4
        self.research_team_Team7 = research_team_Team7 if research_team_Team7 is not None else set()
        self.research_team_Team9 = research_team_Team9 if research_team_Team9 is not None else set()
        self.team = team if team is not None else set()
        self.Team = Team
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def meaning(self):
        return self.__meaning

    @meaning.setter
    def meaning(self, meaning: str):
        self.__meaning = meaning


    @property
    def urlPage(self):
        return self.__urlPage

    @urlPage.setter
    def urlPage(self, urlPage: str):
        self.__urlPage = urlPage


    @property
    def research_team_Team2(self):
        return self.__research_team_Team2

    @research_team_Team2.setter
    def research_team_Team2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__research_team_Team2", None)
        self.__research_team_Team2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_team_Person"):
                    opp_val = getattr(item, "research_team_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "research_team_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_team_Person"):
                    opp_val = getattr(item, "research_team_Person", None)
                    
                    setattr(item, "research_team_Person", self)
                    

    @property
    def research_team_Team4(self):
        return self.__research_team_Team4

    @research_team_Team4.setter
    def research_team_Team4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__research_team_Team4", None)
        self.__research_team_Team4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "research_team_Person5"):
                opp_val = getattr(old_value, "research_team_Person5", None)
                if opp_val == self:
                    setattr(old_value, "research_team_Person5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "research_team_Person5"):
                opp_val = getattr(value, "research_team_Person5", None)
                setattr(value, "research_team_Person5", self)

    @property
    def Team(self):
        return self.__Team

    @Team.setter
    def Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__Team", None)
        self.__Team = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mainReferences"):
                opp_val = getattr(old_value, "mainReferences", None)
                if opp_val == self:
                    setattr(old_value, "mainReferences", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mainReferences"):
                opp_val = getattr(value, "mainReferences", None)
                setattr(value, "mainReferences", self)

    @property
    def research_team_Team(self):
        return self.__research_team_Team

    @research_team_Team.setter
    def research_team_Team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__research_team_Team", None)
        self.__research_team_Team = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_team_ActivityReport"):
                    opp_val = getattr(item, "research_team_ActivityReport", None)
                    
                    if opp_val == self:
                        setattr(item, "research_team_ActivityReport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_team_ActivityReport"):
                    opp_val = getattr(item, "research_team_ActivityReport", None)
                    
                    setattr(item, "research_team_ActivityReport", self)
                    

    @property
    def research_team_Team9(self):
        return self.__research_team_Team9

    @research_team_Team9.setter
    def research_team_Team9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__research_team_Team9", None)
        self.__research_team_Team9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_team_Collaboration"):
                    opp_val = getattr(item, "research_team_Collaboration", None)
                    
                    if opp_val == self:
                        setattr(item, "research_team_Collaboration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_team_Collaboration"):
                    opp_val = getattr(item, "research_team_Collaboration", None)
                    
                    setattr(item, "research_team_Collaboration", self)
                    

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__team", None)
        self.__team = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Publication"):
                    opp_val = getattr(item, "Publication", None)
                    
                    if opp_val == self:
                        setattr(item, "Publication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Publication"):
                    opp_val = getattr(item, "Publication", None)
                    
                    setattr(item, "Publication", self)
                    

    @property
    def research_team_Team7(self):
        return self.__research_team_Team7

    @research_team_Team7.setter
    def research_team_Team7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_research_team_Team__research_team_Team7", None)
        self.__research_team_Team7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "research_team_OpenPosition"):
                    opp_val = getattr(item, "research_team_OpenPosition", None)
                    
                    if opp_val == self:
                        setattr(item, "research_team_OpenPosition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "research_team_OpenPosition"):
                    opp_val = getattr(item, "research_team_OpenPosition", None)
                    
                    setattr(item, "research_team_OpenPosition", self)
                    
