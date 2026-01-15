from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sourceanalysator_Library:

    pass
class sourceanalysator_Hyperlink:

    def __init__(self, url: str, Hyperlink: "sourceanalysator_Source" = None, hyperlink: set["sourceanalysator_Source"] = None, sourceanalysator_Hyperlink: "sourceanalysator_Library" = None):
        self.url = url
        self.Hyperlink = Hyperlink
        self.hyperlink = hyperlink if hyperlink is not None else set()
        self.sourceanalysator_Hyperlink = sourceanalysator_Hyperlink
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def hyperlink(self):
        return self.__hyperlink

    @hyperlink.setter
    def hyperlink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_Hyperlink__hyperlink", None)
        self.__hyperlink = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Source14"):
                    opp_val = getattr(item, "Source14", None)
                    
                    if opp_val == self:
                        setattr(item, "Source14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Source14"):
                    opp_val = getattr(item, "Source14", None)
                    
                    setattr(item, "Source14", self)
                    

    @property
    def Hyperlink(self):
        return self.__Hyperlink

    @Hyperlink.setter
    def Hyperlink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_Hyperlink__Hyperlink", None)
        self.__Hyperlink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources5"):
                opp_val = getattr(old_value, "sources5", None)
                if opp_val == self:
                    setattr(old_value, "sources5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources5"):
                opp_val = getattr(value, "sources5", None)
                setattr(value, "sources5", self)

    @property
    def sourceanalysator_Hyperlink(self):
        return self.__sourceanalysator_Hyperlink

    @sourceanalysator_Hyperlink.setter
    def sourceanalysator_Hyperlink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_Hyperlink__sourceanalysator_Hyperlink", None)
        self.__sourceanalysator_Hyperlink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceanalysator_Library10"):
                opp_val = getattr(old_value, "sourceanalysator_Library10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceanalysator_Library10"):
                opp_val = getattr(value, "sourceanalysator_Library10", None)
                if opp_val is None:
                    setattr(value, "sourceanalysator_Library10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sourceanalysator_Article:

    def __init__(self, title: str, localFile: str, Article: "sourceanalysator_Source" = None, sourceanalysator_Article: "sourceanalysator_Library" = None, article: set["sourceanalysator_Source"] = None):
        self.title = title
        self.localFile = localFile
        self.Article = Article
        self.sourceanalysator_Article = sourceanalysator_Article
        self.article = article if article is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def localFile(self) -> str:
        return self.__localFile

    @localFile.setter
    def localFile(self, localFile: str):
        self.__localFile = localFile

    @property
    def article(self):
        return self.__article

    @article.setter
    def article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_Article__article", None)
        self.__article = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Source12"):
                    opp_val = getattr(item, "Source12", None)
                    
                    if opp_val == self:
                        setattr(item, "Source12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Source12"):
                    opp_val = getattr(item, "Source12", None)
                    
                    setattr(item, "Source12", self)
                    

    @property
    def Article(self):
        return self.__Article

    @Article.setter
    def Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_Article__Article", None)
        self.__Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources3"):
                opp_val = getattr(old_value, "sources3", None)
                if opp_val == self:
                    setattr(old_value, "sources3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources3"):
                opp_val = getattr(value, "sources3", None)
                setattr(value, "sources3", self)

    @property
    def sourceanalysator_Article(self):
        return self.__sourceanalysator_Article

    @sourceanalysator_Article.setter
    def sourceanalysator_Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_Article__sourceanalysator_Article", None)
        self.__sourceanalysator_Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceanalysator_Library8"):
                opp_val = getattr(old_value, "sourceanalysator_Library8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceanalysator_Library8"):
                opp_val = getattr(value, "sourceanalysator_Library8", None)
                if opp_val is None:
                    setattr(value, "sourceanalysator_Library8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sourceanalysator_Source:

    pass
class sourceanalysator_GeneralSource:

    def __init__(self, name: str, aliases: str, dontCount: bool, generalSource: set["sourceanalysator_Source"] = None, GeneralSource: "sourceanalysator_Source" = None, sourceanalysator_GeneralSource: "sourceanalysator_Library" = None):
        self.name = name
        self.aliases = aliases
        self.dontCount = dontCount
        self.generalSource = generalSource if generalSource is not None else set()
        self.GeneralSource = GeneralSource
        self.sourceanalysator_GeneralSource = sourceanalysator_GeneralSource
        
    @property
    def aliases(self) -> str:
        return self.__aliases

    @aliases.setter
    def aliases(self, aliases: str):
        self.__aliases = aliases

    @property
    def dontCount(self) -> bool:
        return self.__dontCount

    @dontCount.setter
    def dontCount(self, dontCount: bool):
        self.__dontCount = dontCount

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def GeneralSource(self):
        return self.__GeneralSource

    @GeneralSource.setter
    def GeneralSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_GeneralSource__GeneralSource", None)
        self.__GeneralSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if opp_val == self:
                    setattr(old_value, "sources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                setattr(value, "sources", self)

    @property
    def sourceanalysator_GeneralSource(self):
        return self.__sourceanalysator_GeneralSource

    @sourceanalysator_GeneralSource.setter
    def sourceanalysator_GeneralSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_GeneralSource__sourceanalysator_GeneralSource", None)
        self.__sourceanalysator_GeneralSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceanalysator_Library"):
                opp_val = getattr(old_value, "sourceanalysator_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceanalysator_Library"):
                opp_val = getattr(value, "sourceanalysator_Library", None)
                if opp_val is None:
                    setattr(value, "sourceanalysator_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generalSource(self):
        return self.__generalSource

    @generalSource.setter
    def generalSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourceanalysator_GeneralSource__generalSource", None)
        self.__generalSource = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    if opp_val == self:
                        setattr(item, "Source", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    setattr(item, "Source", self)
                    
