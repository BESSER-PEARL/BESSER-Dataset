from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class common_StringValueList:

    pass
class Modifiable:

    pass
class common_StringValue(Modifiable):

    def __init__(self, value: str, common_StringValue: "common_StringValueList" = None):
        self.value = value
        self.common_StringValue = common_StringValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def common_StringValue(self):
        return self.__common_StringValue

    @common_StringValue.setter
    def common_StringValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_StringValue__common_StringValue", None)
        self.__common_StringValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_StringValueList"):
                opp_val = getattr(old_value, "common_StringValueList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_StringValueList"):
                opp_val = getattr(value, "common_StringValueList", None)
                if opp_val is None:
                    setattr(value, "common_StringValueList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class common_DoubleValueMatrix:

    pass
class common_DoubleValue(Modifiable):

    def __init__(self, identifier: str, value: float, common_DoubleValue: "common_DoubleValueList" = None):
        self.identifier = identifier
        self.value = value
        self.common_DoubleValue = common_DoubleValue
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def common_DoubleValue(self):
        return self.__common_DoubleValue

    @common_DoubleValue.setter
    def common_DoubleValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_DoubleValue__common_DoubleValue", None)
        self.__common_DoubleValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_DoubleValueList"):
                opp_val = getattr(old_value, "common_DoubleValueList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_DoubleValueList"):
                opp_val = getattr(value, "common_DoubleValueList", None)
                if opp_val is None:
                    setattr(value, "common_DoubleValueList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class common_DublinCore:

    def __init__(self, publisher: str, coverage: str, contributor: str, relation: str, rights: str, source: str, subject: str, type: str, language: str, bibliographicCitation: str, created: str, license: str, required: str, spatial: str, valid: str, title: str, identifier: str, description: str, creator: str, date: str, format: str, common_DublinCore: "common_Identifiable" = None):
        self.publisher = publisher
        self.coverage = coverage
        self.contributor = contributor
        self.relation = relation
        self.rights = rights
        self.source = source
        self.subject = subject
        self.type = type
        self.language = language
        self.bibliographicCitation = bibliographicCitation
        self.created = created
        self.license = license
        self.required = required
        self.spatial = spatial
        self.valid = valid
        self.title = title
        self.identifier = identifier
        self.description = description
        self.creator = creator
        self.date = date
        self.format = format
        self.common_DublinCore = common_DublinCore
        
    @property
    def valid(self) -> str:
        return self.__valid

    @valid.setter
    def valid(self, valid: str):
        self.__valid = valid

    @property
    def spatial(self) -> str:
        return self.__spatial

    @spatial.setter
    def spatial(self, spatial: str):
        self.__spatial = spatial

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def bibliographicCitation(self) -> str:
        return self.__bibliographicCitation

    @bibliographicCitation.setter
    def bibliographicCitation(self, bibliographicCitation: str):
        self.__bibliographicCitation = bibliographicCitation

    @property
    def created(self) -> str:
        return self.__created

    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def contributor(self) -> str:
        return self.__contributor

    @contributor.setter
    def contributor(self, contributor: str):
        self.__contributor = contributor

    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def rights(self) -> str:
        return self.__rights

    @rights.setter
    def rights(self, rights: str):
        self.__rights = rights

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def coverage(self) -> str:
        return self.__coverage

    @coverage.setter
    def coverage(self, coverage: str):
        self.__coverage = coverage

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def license(self) -> str:
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def creator(self) -> str:
        return self.__creator

    @creator.setter
    def creator(self, creator: str):
        self.__creator = creator

    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def common_DublinCore(self):
        return self.__common_DublinCore

    @common_DublinCore.setter
    def common_DublinCore(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_DublinCore__common_DublinCore", None)
        self.__common_DublinCore = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_Identifiable"):
                opp_val = getattr(old_value, "common_Identifiable", None)
                if opp_val == self:
                    setattr(old_value, "common_Identifiable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_Identifiable"):
                opp_val = getattr(value, "common_Identifiable", None)
                setattr(value, "common_Identifiable", self)

    def populate(self) -> str:
        # TODO: Implement populate method
        pass

class common_DoubleValueList:

    def __init__(self, identifier: str, common_DoubleValueList: set["common_DoubleValue"] = None, common_DoubleValueList3: "common_DoubleValueMatrix" = None):
        self.identifier = identifier
        self.common_DoubleValueList = common_DoubleValueList if common_DoubleValueList is not None else set()
        self.common_DoubleValueList3 = common_DoubleValueList3
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def common_DoubleValueList3(self):
        return self.__common_DoubleValueList3

    @common_DoubleValueList3.setter
    def common_DoubleValueList3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_DoubleValueList__common_DoubleValueList3", None)
        self.__common_DoubleValueList3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_DoubleValueMatrix"):
                opp_val = getattr(old_value, "common_DoubleValueMatrix", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_DoubleValueMatrix"):
                opp_val = getattr(value, "common_DoubleValueMatrix", None)
                if opp_val is None:
                    setattr(value, "common_DoubleValueMatrix", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def common_DoubleValueList(self):
        return self.__common_DoubleValueList

    @common_DoubleValueList.setter
    def common_DoubleValueList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_DoubleValueList__common_DoubleValueList", None)
        self.__common_DoubleValueList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "common_DoubleValue"):
                    opp_val = getattr(item, "common_DoubleValue", None)
                    
                    if opp_val == self:
                        setattr(item, "common_DoubleValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "common_DoubleValue"):
                    opp_val = getattr(item, "common_DoubleValue", None)
                    
                    setattr(item, "common_DoubleValue", self)
                    

class common_IdentifiableFilter:

    pass
class common_Comparable(ABC):

    pass
class common_Identifiable(ABC):

    def __init__(self, uRI: str, typeURI: str, common_Identifiable: "common_DublinCore" = None):
        self.uRI = uRI
        self.typeURI = typeURI
        self.common_Identifiable = common_Identifiable
        
    @property
    def typeURI(self) -> str:
        return self.__typeURI

    @typeURI.setter
    def typeURI(self, typeURI: str):
        self.__typeURI = typeURI

    @property
    def uRI(self) -> str:
        return self.__uRI

    @uRI.setter
    def uRI(self, uRI: str):
        self.__uRI = uRI

    @property
    def common_Identifiable(self):
        return self.__common_Identifiable

    @common_Identifiable.setter
    def common_Identifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_common_Identifiable__common_Identifiable", None)
        self.__common_Identifiable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "common_DublinCore"):
                opp_val = getattr(old_value, "common_DublinCore", None)
                if opp_val == self:
                    setattr(old_value, "common_DublinCore", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "common_DublinCore"):
                opp_val = getattr(value, "common_DublinCore", None)
                setattr(value, "common_DublinCore", self)

    def sane(self) -> bool:
        # TODO: Implement sane method
        pass
