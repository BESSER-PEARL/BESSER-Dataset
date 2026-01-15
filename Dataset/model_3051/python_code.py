from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class megal_QueryStatement:

    pass
class megal_QueryEntry(ABC):

    pass
class QueryEntry:

    pass
class megal_QueryPos(QueryEntry):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class megal_QueryEntity(QueryEntry):

    pass
class megal_QueryString(QueryEntry):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class megal_QueryReference(QueryEntry):

    pass
class megal_QueryParam(QueryEntry):

    def __init__(self, name: str, megal_QueryParam: "megal_MegalEntityType" = None, megal_QueryParam68: "megal_QueryReference" = None):
        self.name = name
        self.megal_QueryParam = megal_QueryParam
        self.megal_QueryParam68 = megal_QueryParam68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def megal_QueryParam(self):
        return self.__megal_QueryParam

    @megal_QueryParam.setter
    def megal_QueryParam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_QueryParam__megal_QueryParam", None)
        self.__megal_QueryParam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntityType66"):
                opp_val = getattr(old_value, "megal_MegalEntityType66", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntityType66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntityType66"):
                opp_val = getattr(value, "megal_MegalEntityType66", None)
                setattr(value, "megal_MegalEntityType66", self)

    @property
    def megal_QueryParam68(self):
        return self.__megal_QueryParam68

    @megal_QueryParam68.setter
    def megal_QueryParam68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_QueryParam__megal_QueryParam68", None)
        self.__megal_QueryParam68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_QueryReference"):
                opp_val = getattr(old_value, "megal_QueryReference", None)
                if opp_val == self:
                    setattr(old_value, "megal_QueryReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_QueryReference"):
                opp_val = getattr(value, "megal_QueryReference", None)
                setattr(value, "megal_QueryReference", self)

class MegalNamed:

    pass
class megal_MegalEntityType(MegalNamed):

    pass
class megal_MegalEntity(MegalNamed):

    def __init__(self, many: bool, megal_MegalEntity13: "megal_MegalLink" = None, megal_MegalEntity16: "megal_MegalLink" = None, megal_MegalEntity20: "megal_MegalRelationship" = None, megal_MegalEntity23: "megal_MegalRelationship" = None, megal_MegalEntity25: "megal_MegalPair" = None, megal_MegalEntity28: "megal_MegalPair" = None, megal_MegalEntity: "megal_MegalLink" = None, megal_MegalEntity47: "megal_MegalEntityType" = None, megal_MegalEntity51: "megal_MegalEntity" = None, megal_MegalEntity49: set["megal_MegalEntity"] = None, megal_MegalEntity31: "megal_MegalPair" = None, megal_MegalEntity42: "megal_MegalRelationshipType" = None, megal_MegalEntity45: "megal_MegalRelationshipType" = None, megal_MegalEntity70: "megal_QueryEntity" = None):
        self.many = many
        self.megal_MegalEntity13 = megal_MegalEntity13
        self.megal_MegalEntity16 = megal_MegalEntity16
        self.megal_MegalEntity20 = megal_MegalEntity20
        self.megal_MegalEntity23 = megal_MegalEntity23
        self.megal_MegalEntity25 = megal_MegalEntity25
        self.megal_MegalEntity28 = megal_MegalEntity28
        self.megal_MegalEntity = megal_MegalEntity
        self.megal_MegalEntity47 = megal_MegalEntity47
        self.megal_MegalEntity51 = megal_MegalEntity51
        self.megal_MegalEntity49 = megal_MegalEntity49 if megal_MegalEntity49 is not None else set()
        self.megal_MegalEntity31 = megal_MegalEntity31
        self.megal_MegalEntity42 = megal_MegalEntity42
        self.megal_MegalEntity45 = megal_MegalEntity45
        self.megal_MegalEntity70 = megal_MegalEntity70
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def megal_MegalEntity13(self):
        return self.__megal_MegalEntity13

    @megal_MegalEntity13.setter
    def megal_MegalEntity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity13", None)
        self.__megal_MegalEntity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalLink12"):
                opp_val = getattr(old_value, "megal_MegalLink12", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalLink12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalLink12"):
                opp_val = getattr(value, "megal_MegalLink12", None)
                setattr(value, "megal_MegalLink12", self)

    @property
    def megal_MegalEntity31(self):
        return self.__megal_MegalEntity31

    @megal_MegalEntity31.setter
    def megal_MegalEntity31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity31", None)
        self.__megal_MegalEntity31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalPair30"):
                opp_val = getattr(old_value, "megal_MegalPair30", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalPair30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalPair30"):
                opp_val = getattr(value, "megal_MegalPair30", None)
                setattr(value, "megal_MegalPair30", self)

    @property
    def megal_MegalEntity51(self):
        return self.__megal_MegalEntity51

    @megal_MegalEntity51.setter
    def megal_MegalEntity51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity51", None)
        self.__megal_MegalEntity51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntity49"):
                opp_val = getattr(old_value, "megal_MegalEntity49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntity49"):
                opp_val = getattr(value, "megal_MegalEntity49", None)
                if opp_val is None:
                    setattr(value, "megal_MegalEntity49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def megal_MegalEntity28(self):
        return self.__megal_MegalEntity28

    @megal_MegalEntity28.setter
    def megal_MegalEntity28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity28", None)
        self.__megal_MegalEntity28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalPair27"):
                opp_val = getattr(old_value, "megal_MegalPair27", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalPair27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalPair27"):
                opp_val = getattr(value, "megal_MegalPair27", None)
                setattr(value, "megal_MegalPair27", self)

    @property
    def megal_MegalEntity45(self):
        return self.__megal_MegalEntity45

    @megal_MegalEntity45.setter
    def megal_MegalEntity45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity45", None)
        self.__megal_MegalEntity45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalRelationshipType44"):
                opp_val = getattr(old_value, "megal_MegalRelationshipType44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalRelationshipType44"):
                opp_val = getattr(value, "megal_MegalRelationshipType44", None)
                if opp_val is None:
                    setattr(value, "megal_MegalRelationshipType44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def megal_MegalEntity25(self):
        return self.__megal_MegalEntity25

    @megal_MegalEntity25.setter
    def megal_MegalEntity25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity25", None)
        self.__megal_MegalEntity25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalPair"):
                opp_val = getattr(old_value, "megal_MegalPair", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalPair", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalPair"):
                opp_val = getattr(value, "megal_MegalPair", None)
                setattr(value, "megal_MegalPair", self)

    @property
    def megal_MegalEntity70(self):
        return self.__megal_MegalEntity70

    @megal_MegalEntity70.setter
    def megal_MegalEntity70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity70", None)
        self.__megal_MegalEntity70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_QueryEntity"):
                opp_val = getattr(old_value, "megal_QueryEntity", None)
                if opp_val == self:
                    setattr(old_value, "megal_QueryEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_QueryEntity"):
                opp_val = getattr(value, "megal_QueryEntity", None)
                setattr(value, "megal_QueryEntity", self)

    @property
    def megal_MegalEntity42(self):
        return self.__megal_MegalEntity42

    @megal_MegalEntity42.setter
    def megal_MegalEntity42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity42", None)
        self.__megal_MegalEntity42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalRelationshipType41"):
                opp_val = getattr(old_value, "megal_MegalRelationshipType41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalRelationshipType41"):
                opp_val = getattr(value, "megal_MegalRelationshipType41", None)
                if opp_val is None:
                    setattr(value, "megal_MegalRelationshipType41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def megal_MegalEntity23(self):
        return self.__megal_MegalEntity23

    @megal_MegalEntity23.setter
    def megal_MegalEntity23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity23", None)
        self.__megal_MegalEntity23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalRelationship22"):
                opp_val = getattr(old_value, "megal_MegalRelationship22", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalRelationship22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalRelationship22"):
                opp_val = getattr(value, "megal_MegalRelationship22", None)
                setattr(value, "megal_MegalRelationship22", self)

    @property
    def megal_MegalEntity47(self):
        return self.__megal_MegalEntity47

    @megal_MegalEntity47.setter
    def megal_MegalEntity47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity47", None)
        self.__megal_MegalEntity47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntityType48"):
                opp_val = getattr(old_value, "megal_MegalEntityType48", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntityType48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntityType48"):
                opp_val = getattr(value, "megal_MegalEntityType48", None)
                setattr(value, "megal_MegalEntityType48", self)

    @property
    def megal_MegalEntity(self):
        return self.__megal_MegalEntity

    @megal_MegalEntity.setter
    def megal_MegalEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity", None)
        self.__megal_MegalEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalLink10"):
                opp_val = getattr(old_value, "megal_MegalLink10", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalLink10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalLink10"):
                opp_val = getattr(value, "megal_MegalLink10", None)
                setattr(value, "megal_MegalLink10", self)

    @property
    def megal_MegalEntity20(self):
        return self.__megal_MegalEntity20

    @megal_MegalEntity20.setter
    def megal_MegalEntity20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity20", None)
        self.__megal_MegalEntity20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalRelationship19"):
                opp_val = getattr(old_value, "megal_MegalRelationship19", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalRelationship19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalRelationship19"):
                opp_val = getattr(value, "megal_MegalRelationship19", None)
                setattr(value, "megal_MegalRelationship19", self)

    @property
    def megal_MegalEntity16(self):
        return self.__megal_MegalEntity16

    @megal_MegalEntity16.setter
    def megal_MegalEntity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity16", None)
        self.__megal_MegalEntity16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalLink15"):
                opp_val = getattr(old_value, "megal_MegalLink15", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalLink15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalLink15"):
                opp_val = getattr(value, "megal_MegalLink15", None)
                setattr(value, "megal_MegalLink15", self)

    @property
    def megal_MegalEntity49(self):
        return self.__megal_MegalEntity49

    @megal_MegalEntity49.setter
    def megal_MegalEntity49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalEntity__megal_MegalEntity49", None)
        self.__megal_MegalEntity49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "megal_MegalEntity51"):
                    opp_val = getattr(item, "megal_MegalEntity51", None)
                    
                    if opp_val == self:
                        setattr(item, "megal_MegalEntity51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "megal_MegalEntity51"):
                    opp_val = getattr(item, "megal_MegalEntity51", None)
                    
                    setattr(item, "megal_MegalEntity51", self)
                    

class MegalElement:

    pass
class megal_MegalLink(MegalElement):

    def __init__(self, to: str, megal_MegalLink12: "megal_MegalEntity" = None, megal_MegalLink15: "megal_MegalEntity" = None, megal_MegalLink: "megal_MegalFile" = None, megal_MegalLink10: "megal_MegalEntity" = None):
        self.to = to
        self.megal_MegalLink12 = megal_MegalLink12
        self.megal_MegalLink15 = megal_MegalLink15
        self.megal_MegalLink = megal_MegalLink
        self.megal_MegalLink10 = megal_MegalLink10
        
    @property
    def to(self) -> str:
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def megal_MegalLink10(self):
        return self.__megal_MegalLink10

    @megal_MegalLink10.setter
    def megal_MegalLink10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalLink__megal_MegalLink10", None)
        self.__megal_MegalLink10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntity"):
                opp_val = getattr(old_value, "megal_MegalEntity", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntity"):
                opp_val = getattr(value, "megal_MegalEntity", None)
                setattr(value, "megal_MegalEntity", self)

    @property
    def megal_MegalLink12(self):
        return self.__megal_MegalLink12

    @megal_MegalLink12.setter
    def megal_MegalLink12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalLink__megal_MegalLink12", None)
        self.__megal_MegalLink12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntity13"):
                opp_val = getattr(old_value, "megal_MegalEntity13", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntity13"):
                opp_val = getattr(value, "megal_MegalEntity13", None)
                setattr(value, "megal_MegalEntity13", self)

    @property
    def megal_MegalLink15(self):
        return self.__megal_MegalLink15

    @megal_MegalLink15.setter
    def megal_MegalLink15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalLink__megal_MegalLink15", None)
        self.__megal_MegalLink15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntity16"):
                opp_val = getattr(old_value, "megal_MegalEntity16", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntity16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntity16"):
                opp_val = getattr(value, "megal_MegalEntity16", None)
                setattr(value, "megal_MegalEntity16", self)

    @property
    def megal_MegalLink(self):
        return self.__megal_MegalLink

    @megal_MegalLink.setter
    def megal_MegalLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalLink__megal_MegalLink", None)
        self.__megal_MegalLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalFile5"):
                opp_val = getattr(old_value, "megal_MegalFile5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalFile5"):
                opp_val = getattr(value, "megal_MegalFile5", None)
                if opp_val is None:
                    setattr(value, "megal_MegalFile5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class megal_MegalDeclaration(MegalElement):

    pass
class megal_MegalFile(MegalElement):

    def __init__(self, name: str, megal_MegalFile: set["megal_MegalDeclaration"] = None, megal_MegalFile5: set["megal_MegalLink"] = None, megal_MegalFile8: "megal_MegalFile" = None, megal_MegalFile6: set["megal_MegalFile"] = None):
        self.name = name
        self.megal_MegalFile = megal_MegalFile if megal_MegalFile is not None else set()
        self.megal_MegalFile5 = megal_MegalFile5 if megal_MegalFile5 is not None else set()
        self.megal_MegalFile8 = megal_MegalFile8
        self.megal_MegalFile6 = megal_MegalFile6 if megal_MegalFile6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def megal_MegalFile(self):
        return self.__megal_MegalFile

    @megal_MegalFile.setter
    def megal_MegalFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalFile__megal_MegalFile", None)
        self.__megal_MegalFile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "megal_MegalDeclaration"):
                    opp_val = getattr(item, "megal_MegalDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "megal_MegalDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "megal_MegalDeclaration"):
                    opp_val = getattr(item, "megal_MegalDeclaration", None)
                    
                    setattr(item, "megal_MegalDeclaration", self)
                    

    @property
    def megal_MegalFile8(self):
        return self.__megal_MegalFile8

    @megal_MegalFile8.setter
    def megal_MegalFile8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalFile__megal_MegalFile8", None)
        self.__megal_MegalFile8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalFile6"):
                opp_val = getattr(old_value, "megal_MegalFile6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalFile6"):
                opp_val = getattr(value, "megal_MegalFile6", None)
                if opp_val is None:
                    setattr(value, "megal_MegalFile6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def megal_MegalFile5(self):
        return self.__megal_MegalFile5

    @megal_MegalFile5.setter
    def megal_MegalFile5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalFile__megal_MegalFile5", None)
        self.__megal_MegalFile5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "megal_MegalLink"):
                    opp_val = getattr(item, "megal_MegalLink", None)
                    
                    if opp_val == self:
                        setattr(item, "megal_MegalLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "megal_MegalLink"):
                    opp_val = getattr(item, "megal_MegalLink", None)
                    
                    setattr(item, "megal_MegalLink", self)
                    

    @property
    def megal_MegalFile6(self):
        return self.__megal_MegalFile6

    @megal_MegalFile6.setter
    def megal_MegalFile6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalFile__megal_MegalFile6", None)
        self.__megal_MegalFile6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "megal_MegalFile8"):
                    opp_val = getattr(item, "megal_MegalFile8", None)
                    
                    if opp_val == self:
                        setattr(item, "megal_MegalFile8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "megal_MegalFile8"):
                    opp_val = getattr(item, "megal_MegalFile8", None)
                    
                    setattr(item, "megal_MegalFile8", self)
                    

class megal_MegalElement(ABC):

    pass
class megal_Selection:

    pass
class megal_MegalAnnotation:

    def __init__(self, key: str, megal_MegalAnnotation: "megal_Selection" = None, megal_MegalAnnotation2: "megal_MegalElement" = None):
        self.key = key
        self.megal_MegalAnnotation = megal_MegalAnnotation
        self.megal_MegalAnnotation2 = megal_MegalAnnotation2
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def megal_MegalAnnotation2(self):
        return self.__megal_MegalAnnotation2

    @megal_MegalAnnotation2.setter
    def megal_MegalAnnotation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalAnnotation__megal_MegalAnnotation2", None)
        self.__megal_MegalAnnotation2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalElement"):
                opp_val = getattr(old_value, "megal_MegalElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalElement"):
                opp_val = getattr(value, "megal_MegalElement", None)
                if opp_val is None:
                    setattr(value, "megal_MegalElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def megal_MegalAnnotation(self):
        return self.__megal_MegalAnnotation

    @megal_MegalAnnotation.setter
    def megal_MegalAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalAnnotation__megal_MegalAnnotation", None)
        self.__megal_MegalAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_Selection"):
                opp_val = getattr(old_value, "megal_Selection", None)
                if opp_val == self:
                    setattr(old_value, "megal_Selection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_Selection"):
                opp_val = getattr(value, "megal_Selection", None)
                setattr(value, "megal_Selection", self)

class megal_MegalRelationshipType(MegalNamed):

    def __init__(self, leftBoth: bool, rightBoth: bool, leftMany: bool, rightMany: bool, megal_MegalRelationshipType: "megal_MegalRelationship" = None, megal_MegalRelationshipType35: "megal_MegalEntityType" = None, megal_MegalRelationshipType38: "megal_MegalEntityType" = None, megal_MegalRelationshipType41: set["megal_MegalEntity"] = None, megal_MegalRelationshipType44: set["megal_MegalEntity"] = None, megal_MegalRelationshipType61: "megal_QueryStatement" = None):
        self.leftBoth = leftBoth
        self.rightBoth = rightBoth
        self.leftMany = leftMany
        self.rightMany = rightMany
        self.megal_MegalRelationshipType = megal_MegalRelationshipType
        self.megal_MegalRelationshipType35 = megal_MegalRelationshipType35
        self.megal_MegalRelationshipType38 = megal_MegalRelationshipType38
        self.megal_MegalRelationshipType41 = megal_MegalRelationshipType41 if megal_MegalRelationshipType41 is not None else set()
        self.megal_MegalRelationshipType44 = megal_MegalRelationshipType44 if megal_MegalRelationshipType44 is not None else set()
        self.megal_MegalRelationshipType61 = megal_MegalRelationshipType61
        
    @property
    def leftMany(self) -> bool:
        return self.__leftMany

    @leftMany.setter
    def leftMany(self, leftMany: bool):
        self.__leftMany = leftMany

    @property
    def rightBoth(self) -> bool:
        return self.__rightBoth

    @rightBoth.setter
    def rightBoth(self, rightBoth: bool):
        self.__rightBoth = rightBoth

    @property
    def leftBoth(self) -> bool:
        return self.__leftBoth

    @leftBoth.setter
    def leftBoth(self, leftBoth: bool):
        self.__leftBoth = leftBoth

    @property
    def rightMany(self) -> bool:
        return self.__rightMany

    @rightMany.setter
    def rightMany(self, rightMany: bool):
        self.__rightMany = rightMany

    @property
    def megal_MegalRelationshipType61(self):
        return self.__megal_MegalRelationshipType61

    @megal_MegalRelationshipType61.setter
    def megal_MegalRelationshipType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalRelationshipType__megal_MegalRelationshipType61", None)
        self.__megal_MegalRelationshipType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_QueryStatement60"):
                opp_val = getattr(old_value, "megal_QueryStatement60", None)
                if opp_val == self:
                    setattr(old_value, "megal_QueryStatement60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_QueryStatement60"):
                opp_val = getattr(value, "megal_QueryStatement60", None)
                setattr(value, "megal_QueryStatement60", self)

    @property
    def megal_MegalRelationshipType38(self):
        return self.__megal_MegalRelationshipType38

    @megal_MegalRelationshipType38.setter
    def megal_MegalRelationshipType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalRelationshipType__megal_MegalRelationshipType38", None)
        self.__megal_MegalRelationshipType38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntityType39"):
                opp_val = getattr(old_value, "megal_MegalEntityType39", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntityType39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntityType39"):
                opp_val = getattr(value, "megal_MegalEntityType39", None)
                setattr(value, "megal_MegalEntityType39", self)

    @property
    def megal_MegalRelationshipType35(self):
        return self.__megal_MegalRelationshipType35

    @megal_MegalRelationshipType35.setter
    def megal_MegalRelationshipType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalRelationshipType__megal_MegalRelationshipType35", None)
        self.__megal_MegalRelationshipType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalEntityType36"):
                opp_val = getattr(old_value, "megal_MegalEntityType36", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalEntityType36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalEntityType36"):
                opp_val = getattr(value, "megal_MegalEntityType36", None)
                setattr(value, "megal_MegalEntityType36", self)

    @property
    def megal_MegalRelationshipType44(self):
        return self.__megal_MegalRelationshipType44

    @megal_MegalRelationshipType44.setter
    def megal_MegalRelationshipType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalRelationshipType__megal_MegalRelationshipType44", None)
        self.__megal_MegalRelationshipType44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "megal_MegalEntity45"):
                    opp_val = getattr(item, "megal_MegalEntity45", None)
                    
                    if opp_val == self:
                        setattr(item, "megal_MegalEntity45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "megal_MegalEntity45"):
                    opp_val = getattr(item, "megal_MegalEntity45", None)
                    
                    setattr(item, "megal_MegalEntity45", self)
                    

    @property
    def megal_MegalRelationshipType41(self):
        return self.__megal_MegalRelationshipType41

    @megal_MegalRelationshipType41.setter
    def megal_MegalRelationshipType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalRelationshipType__megal_MegalRelationshipType41", None)
        self.__megal_MegalRelationshipType41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "megal_MegalEntity42"):
                    opp_val = getattr(item, "megal_MegalEntity42", None)
                    
                    if opp_val == self:
                        setattr(item, "megal_MegalEntity42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "megal_MegalEntity42"):
                    opp_val = getattr(item, "megal_MegalEntity42", None)
                    
                    setattr(item, "megal_MegalEntity42", self)
                    

    @property
    def megal_MegalRelationshipType(self):
        return self.__megal_MegalRelationshipType

    @megal_MegalRelationshipType.setter
    def megal_MegalRelationshipType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_megal_MegalRelationshipType__megal_MegalRelationshipType", None)
        self.__megal_MegalRelationshipType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "megal_MegalRelationship"):
                opp_val = getattr(old_value, "megal_MegalRelationship", None)
                if opp_val == self:
                    setattr(old_value, "megal_MegalRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "megal_MegalRelationship"):
                opp_val = getattr(value, "megal_MegalRelationship", None)
                setattr(value, "megal_MegalRelationship", self)

class MegalDeclaration:

    pass
class megal_MegalNamed(MegalDeclaration):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class megal_MegalPair(MegalDeclaration):

    pass
class megal_MegalRelationship(MegalDeclaration):

    pass