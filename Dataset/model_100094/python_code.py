from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BuildType(Enum):
    N = "N"
    I = "I"
    S = "S"
    R = "R"
    M = "M"


############################################
# Definition of Classes
############################################

class releng_Promotion:

    def __init__(self, buildType: str, promotions: "releng_BuildJob" = None, releng_Promotion: "releng_Repository" = None, releng_Promotion11: set["releng_Criterion"] = None, Promotion: "releng_BuildJob" = None):
        self.buildType = buildType
        self.promotions = promotions
        self.releng_Promotion = releng_Promotion
        self.releng_Promotion11 = releng_Promotion11 if releng_Promotion11 is not None else set()
        self.Promotion = Promotion
        
        pass
    @property
    def buildType(self):
        return self.__buildType

    @buildType.setter
    def buildType(self, buildType: str):
        self.__buildType = buildType


    @property
    def Promotion(self):
        return self.__Promotion

    @Promotion.setter
    def Promotion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Promotion__Promotion", None)
        self.__Promotion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build"):
                opp_val = getattr(old_value, "build", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build"):
                opp_val = getattr(value, "build", None)
                if opp_val is None:
                    setattr(value, "build", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def releng_Promotion11(self):
        return self.__releng_Promotion11

    @releng_Promotion11.setter
    def releng_Promotion11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Promotion__releng_Promotion11", None)
        self.__releng_Promotion11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "releng_Criterion"):
                    opp_val = getattr(item, "releng_Criterion", None)
                    
                    if opp_val == self:
                        setattr(item, "releng_Criterion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "releng_Criterion"):
                    opp_val = getattr(item, "releng_Criterion", None)
                    
                    setattr(item, "releng_Criterion", self)
                    

    @property
    def promotions(self):
        return self.__promotions

    @promotions.setter
    def promotions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Promotion__promotions", None)
        self.__promotions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BuildJob"):
                opp_val = getattr(old_value, "BuildJob", None)
                if opp_val == self:
                    setattr(old_value, "BuildJob", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BuildJob"):
                opp_val = getattr(value, "BuildJob", None)
                setattr(value, "BuildJob", self)

    @property
    def releng_Promotion(self):
        return self.__releng_Promotion

    @releng_Promotion.setter
    def releng_Promotion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Promotion__releng_Promotion", None)
        self.__releng_Promotion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_Repository9"):
                opp_val = getattr(old_value, "releng_Repository9", None)
                if opp_val == self:
                    setattr(old_value, "releng_Repository9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_Repository9"):
                opp_val = getattr(value, "releng_Repository9", None)
                setattr(value, "releng_Repository9", self)

class Repository:

    pass
class releng_CompositeRepository(Repository):

    pass
class releng_Criterion:

    def __init__(self, description: str, releng_Criterion: "releng_Promotion" = None):
        self.description = description
        self.releng_Criterion = releng_Criterion
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def releng_Criterion(self):
        return self.__releng_Criterion

    @releng_Criterion.setter
    def releng_Criterion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Criterion__releng_Criterion", None)
        self.__releng_Criterion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_Promotion11"):
                opp_val = getattr(old_value, "releng_Promotion11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_Promotion11"):
                opp_val = getattr(value, "releng_Promotion11", None)
                if opp_val is None:
                    setattr(value, "releng_Promotion11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class releng_Repository:

    def __init__(self, location: str, releng_Repository: "releng_Server" = None, releng_Repository9: "releng_Promotion" = None, releng_Repository13: "releng_CompositeRepository" = None, releng_Repository5: "releng_BuildJob" = None):
        self.location = location
        self.releng_Repository = releng_Repository
        self.releng_Repository9 = releng_Repository9
        self.releng_Repository13 = releng_Repository13
        self.releng_Repository5 = releng_Repository5
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def releng_Repository(self):
        return self.__releng_Repository

    @releng_Repository.setter
    def releng_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Repository__releng_Repository", None)
        self.__releng_Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_Server2"):
                opp_val = getattr(old_value, "releng_Server2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_Server2"):
                opp_val = getattr(value, "releng_Server2", None)
                if opp_val is None:
                    setattr(value, "releng_Server2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def releng_Repository13(self):
        return self.__releng_Repository13

    @releng_Repository13.setter
    def releng_Repository13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Repository__releng_Repository13", None)
        self.__releng_Repository13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_CompositeRepository"):
                opp_val = getattr(old_value, "releng_CompositeRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_CompositeRepository"):
                opp_val = getattr(value, "releng_CompositeRepository", None)
                if opp_val is None:
                    setattr(value, "releng_CompositeRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def releng_Repository5(self):
        return self.__releng_Repository5

    @releng_Repository5.setter
    def releng_Repository5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Repository__releng_Repository5", None)
        self.__releng_Repository5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_BuildJob4"):
                opp_val = getattr(old_value, "releng_BuildJob4", None)
                if opp_val == self:
                    setattr(old_value, "releng_BuildJob4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_BuildJob4"):
                opp_val = getattr(value, "releng_BuildJob4", None)
                setattr(value, "releng_BuildJob4", self)

    @property
    def releng_Repository9(self):
        return self.__releng_Repository9

    @releng_Repository9.setter
    def releng_Repository9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Repository__releng_Repository9", None)
        self.__releng_Repository9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_Promotion"):
                opp_val = getattr(old_value, "releng_Promotion", None)
                if opp_val == self:
                    setattr(old_value, "releng_Promotion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_Promotion"):
                opp_val = getattr(value, "releng_Promotion", None)
                setattr(value, "releng_Promotion", self)

class releng_BuildJob:

    def __init__(self, name: str, sourceBranch: str, buckminsterComponent: str, types: str, releng_BuildJob: "releng_Server" = None, BuildJob: "releng_Promotion" = None, releng_BuildJob4: "releng_Repository" = None, build: set["releng_Promotion"] = None):
        self.name = name
        self.sourceBranch = sourceBranch
        self.buckminsterComponent = buckminsterComponent
        self.types = types
        self.releng_BuildJob = releng_BuildJob
        self.BuildJob = BuildJob
        self.releng_BuildJob4 = releng_BuildJob4
        self.build = build if build is not None else set()
        
        pass
    @property
    def sourceBranch(self):
        return self.__sourceBranch

    @sourceBranch.setter
    def sourceBranch(self, sourceBranch: str):
        self.__sourceBranch = sourceBranch


    @property
    def buckminsterComponent(self):
        return self.__buckminsterComponent

    @buckminsterComponent.setter
    def buckminsterComponent(self, buckminsterComponent: str):
        self.__buckminsterComponent = buckminsterComponent


    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def build(self):
        return self.__build

    @build.setter
    def build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_BuildJob__build", None)
        self.__build = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Promotion"):
                    opp_val = getattr(item, "Promotion", None)
                    
                    if opp_val == self:
                        setattr(item, "Promotion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Promotion"):
                    opp_val = getattr(item, "Promotion", None)
                    
                    setattr(item, "Promotion", self)
                    

    @property
    def releng_BuildJob4(self):
        return self.__releng_BuildJob4

    @releng_BuildJob4.setter
    def releng_BuildJob4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_BuildJob__releng_BuildJob4", None)
        self.__releng_BuildJob4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_Repository5"):
                opp_val = getattr(old_value, "releng_Repository5", None)
                if opp_val == self:
                    setattr(old_value, "releng_Repository5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_Repository5"):
                opp_val = getattr(value, "releng_Repository5", None)
                setattr(value, "releng_Repository5", self)

    @property
    def releng_BuildJob(self):
        return self.__releng_BuildJob

    @releng_BuildJob.setter
    def releng_BuildJob(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_BuildJob__releng_BuildJob", None)
        self.__releng_BuildJob = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "releng_Server"):
                opp_val = getattr(old_value, "releng_Server", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "releng_Server"):
                opp_val = getattr(value, "releng_Server", None)
                if opp_val is None:
                    setattr(value, "releng_Server", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BuildJob(self):
        return self.__BuildJob

    @BuildJob.setter
    def BuildJob(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_BuildJob__BuildJob", None)
        self.__BuildJob = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "promotions"):
                opp_val = getattr(old_value, "promotions", None)
                if opp_val == self:
                    setattr(old_value, "promotions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "promotions"):
                opp_val = getattr(value, "promotions", None)
                setattr(value, "promotions", self)

class releng_Server:

    def __init__(self, name: str, releng_Server: set["releng_BuildJob"] = None, releng_Server2: set["releng_Repository"] = None):
        self.name = name
        self.releng_Server = releng_Server if releng_Server is not None else set()
        self.releng_Server2 = releng_Server2 if releng_Server2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def releng_Server2(self):
        return self.__releng_Server2

    @releng_Server2.setter
    def releng_Server2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Server__releng_Server2", None)
        self.__releng_Server2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "releng_Repository"):
                    opp_val = getattr(item, "releng_Repository", None)
                    
                    if opp_val == self:
                        setattr(item, "releng_Repository", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "releng_Repository"):
                    opp_val = getattr(item, "releng_Repository", None)
                    
                    setattr(item, "releng_Repository", self)
                    

    @property
    def releng_Server(self):
        return self.__releng_Server

    @releng_Server.setter
    def releng_Server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_releng_Server__releng_Server", None)
        self.__releng_Server = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "releng_BuildJob"):
                    opp_val = getattr(item, "releng_BuildJob", None)
                    
                    if opp_val == self:
                        setattr(item, "releng_BuildJob", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "releng_BuildJob"):
                    opp_val = getattr(item, "releng_BuildJob", None)
                    
                    setattr(item, "releng_BuildJob", self)
                    
