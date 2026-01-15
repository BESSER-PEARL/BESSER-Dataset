from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class generatedplugin_Plugin:

    pass
class generatedplugin_StemCategory:

    def __init__(self, id: str, name: str, parentId: str, generatedplugin_StemCategory: "generatedplugin_Extension" = None):
        self.id = id
        self.name = name
        self.parentId = parentId
        self.generatedplugin_StemCategory = generatedplugin_StemCategory
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def parentId(self) -> str:
        return self.__parentId

    @parentId.setter
    def parentId(self, parentId: str):
        self.__parentId = parentId

    @property
    def generatedplugin_StemCategory(self):
        return self.__generatedplugin_StemCategory

    @generatedplugin_StemCategory.setter
    def generatedplugin_StemCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_generatedplugin_StemCategory__generatedplugin_StemCategory", None)
        self.__generatedplugin_StemCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedplugin_Extension"):
                opp_val = getattr(old_value, "generatedplugin_Extension", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedplugin_Extension"):
                opp_val = getattr(value, "generatedplugin_Extension", None)
                if opp_val is None:
                    setattr(value, "generatedplugin_Extension", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class generatedplugin_Extension:

    def __init__(self, point: str, generatedplugin_Extension: set["generatedplugin_StemCategory"] = None, generatedplugin_Extension2: set["generatedplugin_DublinCore"] = None, generatedplugin_Extension4: "generatedplugin_Plugin" = None):
        self.point = point
        self.generatedplugin_Extension = generatedplugin_Extension if generatedplugin_Extension is not None else set()
        self.generatedplugin_Extension2 = generatedplugin_Extension2 if generatedplugin_Extension2 is not None else set()
        self.generatedplugin_Extension4 = generatedplugin_Extension4
        
    @property
    def point(self) -> str:
        return self.__point

    @point.setter
    def point(self, point: str):
        self.__point = point

    @property
    def generatedplugin_Extension(self):
        return self.__generatedplugin_Extension

    @generatedplugin_Extension.setter
    def generatedplugin_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_generatedplugin_Extension__generatedplugin_Extension", None)
        self.__generatedplugin_Extension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "generatedplugin_StemCategory"):
                    opp_val = getattr(item, "generatedplugin_StemCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "generatedplugin_StemCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "generatedplugin_StemCategory"):
                    opp_val = getattr(item, "generatedplugin_StemCategory", None)
                    
                    setattr(item, "generatedplugin_StemCategory", self)
                    

    @property
    def generatedplugin_Extension2(self):
        return self.__generatedplugin_Extension2

    @generatedplugin_Extension2.setter
    def generatedplugin_Extension2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_generatedplugin_Extension__generatedplugin_Extension2", None)
        self.__generatedplugin_Extension2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "generatedplugin_DublinCore"):
                    opp_val = getattr(item, "generatedplugin_DublinCore", None)
                    
                    if opp_val == self:
                        setattr(item, "generatedplugin_DublinCore", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "generatedplugin_DublinCore"):
                    opp_val = getattr(item, "generatedplugin_DublinCore", None)
                    
                    setattr(item, "generatedplugin_DublinCore", self)
                    

    @property
    def generatedplugin_Extension4(self):
        return self.__generatedplugin_Extension4

    @generatedplugin_Extension4.setter
    def generatedplugin_Extension4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_generatedplugin_Extension__generatedplugin_Extension4", None)
        self.__generatedplugin_Extension4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedplugin_Plugin"):
                opp_val = getattr(old_value, "generatedplugin_Plugin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedplugin_Plugin"):
                opp_val = getattr(value, "generatedplugin_Plugin", None)
                if opp_val is None:
                    setattr(value, "generatedplugin_Plugin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class generatedplugin_DublinCore:

    def __init__(self, bibliographicCitation: str, contributor: str, coverage: str, created: str, creator: str, date: str, description: str, format: str, identifier: str, categoryId: str, license: str, publisher: str, relation: str, requires: str, rights: str, source: str, spatial: str, subject: str, language: str, title: str, type: str, valid: str, generatedplugin_DublinCore: "generatedplugin_Extension" = None):
        self.bibliographicCitation = bibliographicCitation
        self.contributor = contributor
        self.coverage = coverage
        self.created = created
        self.creator = creator
        self.date = date
        self.description = description
        self.format = format
        self.identifier = identifier
        self.categoryId = categoryId
        self.license = license
        self.publisher = publisher
        self.relation = relation
        self.requires = requires
        self.rights = rights
        self.source = source
        self.spatial = spatial
        self.subject = subject
        self.language = language
        self.title = title
        self.type = type
        self.valid = valid
        self.generatedplugin_DublinCore = generatedplugin_DublinCore
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def license(self) -> str:
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license

    @property
    def coverage(self) -> str:
        return self.__coverage

    @coverage.setter
    def coverage(self, coverage: str):
        self.__coverage = coverage

    @property
    def contributor(self) -> str:
        return self.__contributor

    @contributor.setter
    def contributor(self, contributor: str):
        self.__contributor = contributor

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def categoryId(self) -> str:
        return self.__categoryId

    @categoryId.setter
    def categoryId(self, categoryId: str):
        self.__categoryId = categoryId

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def spatial(self) -> str:
        return self.__spatial

    @spatial.setter
    def spatial(self, spatial: str):
        self.__spatial = spatial

    @property
    def rights(self) -> str:
        return self.__rights

    @rights.setter
    def rights(self, rights: str):
        self.__rights = rights

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def requires(self) -> str:
        return self.__requires

    @requires.setter
    def requires(self, requires: str):
        self.__requires = requires

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def valid(self) -> str:
        return self.__valid

    @valid.setter
    def valid(self, valid: str):
        self.__valid = valid

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def creator(self) -> str:
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator

    @property
    def bibliographicCitation(self) -> str:
        return self.__bibliographicCitation

    @bibliographicCitation.setter
    def bibliographicCitation(self, bibliographicCitation: str):
        self.__bibliographicCitation = bibliographicCitation

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def generatedplugin_DublinCore(self):
        return self.__generatedplugin_DublinCore

    @generatedplugin_DublinCore.setter
    def generatedplugin_DublinCore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_generatedplugin_DublinCore__generatedplugin_DublinCore", None)
        self.__generatedplugin_DublinCore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedplugin_Extension2"):
                opp_val = getattr(old_value, "generatedplugin_Extension2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedplugin_Extension2"):
                opp_val = getattr(value, "generatedplugin_Extension2", None)
                if opp_val is None:
                    setattr(value, "generatedplugin_Extension2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
