from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MergeConflictStrategy(Enum):
    Default = "Default"
    UseWorkspace = "UseWorkspace"
    UseSCM = "UseSCM"
    Fail = "Fail"
class TriState(Enum):
    Default = "Default"
    True = "True"
    False = "False"
class BranchPointType(Enum):
    Latest = "Latest"
    Tag = "Tag"
    Timestamp = "Timestamp"
    Revision = "Revision"


############################################
# Definition of Classes
############################################

class BuilderCallFacade:

    pass
class build_IEffectiveFacade(ABC):

    pass
class BuildCallSingle:

    pass
class build_BuildCallOnReferencedRequirement(BuildCallSingle):

    pass
class build_BuildCallOnDeclaredRequirement(BuildCallSingle):

    pass
class BuilderCall:

    pass
class build_BuildCallSingle(BuilderCall):

    pass
class build_BuildCallMultiple(BuilderCall):

    pass
class build_BWithExpression:

    pass
class BuilderInputDecorator:

    pass
class build_BuilderInputContextDecorator(BuilderInputDecorator):

    pass
class build_BuilderInputGroup(BuilderInputDecorator):

    pass
class build_BuilderInputCondition(BuilderInputDecorator):

    pass
class BParameterDeclaration:

    pass
class BuildCallMultiple:

    pass
class build_BuildCallOnSelectedRequirements(BuildCallMultiple):

    pass
class build_Branch:

    def __init__(self, name: str, documentation: str, branchPointType: str, mergeStrategy: str, checkout: str, acceptDirty: str, update: str, replace: str, build_Branch236: set["build_BNamePredicate"] = None, build_Branch239: set["build_BNamePredicate"] = None, build_Branch242: "build_BExpression" = None, build_Branch: "build_Repository" = None):
        self.name = name
        self.documentation = documentation
        self.branchPointType = branchPointType
        self.mergeStrategy = mergeStrategy
        self.checkout = checkout
        self.acceptDirty = acceptDirty
        self.update = update
        self.replace = replace
        self.build_Branch236 = build_Branch236 if build_Branch236 is not None else set()
        self.build_Branch239 = build_Branch239 if build_Branch239 is not None else set()
        self.build_Branch242 = build_Branch242
        self.build_Branch = build_Branch
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def checkout(self) -> str:
        return self.__checkout

    @checkout.setter
    def checkout(self, checkout: str):
        self.__checkout = checkout

    @property
    def branchPointType(self) -> str:
        return self.__branchPointType

    @branchPointType.setter
    def branchPointType(self, branchPointType: str):
        self.__branchPointType = branchPointType

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def replace(self) -> str:
        return self.__replace

    @replace.setter
    def replace(self, replace: str):
        self.__replace = replace

    @property
    def acceptDirty(self) -> str:
        return self.__acceptDirty

    @acceptDirty.setter
    def acceptDirty(self, acceptDirty: str):
        self.__acceptDirty = acceptDirty

    @property
    def update(self) -> str:
        return self.__update

    @update.setter
    def update(self, update: str):
        self.__update = update

    @property
    def mergeStrategy(self) -> str:
        return self.__mergeStrategy

    @mergeStrategy.setter
    def mergeStrategy(self, mergeStrategy: str):
        self.__mergeStrategy = mergeStrategy

    @property
    def build_Branch242(self):
        return self.__build_Branch242

    @build_Branch242.setter
    def build_Branch242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Branch__build_Branch242", None)
        self.__build_Branch242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression243"):
                opp_val = getattr(old_value, "build_BExpression243", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression243"):
                opp_val = getattr(value, "build_BExpression243", None)
                setattr(value, "build_BExpression243", self)

    @property
    def build_Branch236(self):
        return self.__build_Branch236

    @build_Branch236.setter
    def build_Branch236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Branch__build_Branch236", None)
        self.__build_Branch236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BNamePredicate237"):
                    opp_val = getattr(item, "build_BNamePredicate237", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BNamePredicate237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BNamePredicate237"):
                    opp_val = getattr(item, "build_BNamePredicate237", None)
                    
                    setattr(item, "build_BNamePredicate237", self)
                    

    @property
    def build_Branch239(self):
        return self.__build_Branch239

    @build_Branch239.setter
    def build_Branch239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Branch__build_Branch239", None)
        self.__build_Branch239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BNamePredicate240"):
                    opp_val = getattr(item, "build_BNamePredicate240", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BNamePredicate240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BNamePredicate240"):
                    opp_val = getattr(item, "build_BNamePredicate240", None)
                    
                    setattr(item, "build_BNamePredicate240", self)
                    

    @property
    def build_Branch(self):
        return self.__build_Branch

    @build_Branch.setter
    def build_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Branch__build_Branch", None)
        self.__build_Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Repository225"):
                opp_val = getattr(old_value, "build_Repository225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Repository225"):
                opp_val = getattr(value, "build_Repository225", None)
                if opp_val is None:
                    setattr(value, "build_Repository225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def hasValidState(self, chain: str, map: str) -> bool:
        # TODO: Implement hasValidState method
        pass

    def getEffectiveAcceptDirty(self) -> bool:
        # TODO: Implement getEffectiveAcceptDirty method
        pass

    def getEffectiveUpdate(self) -> bool:
        # TODO: Implement getEffectiveUpdate method
        pass

    def getEffectiveCheckout(self) -> bool:
        # TODO: Implement getEffectiveCheckout method
        pass

    def getEffectiveMergeStrategy(self) -> str:
        # TODO: Implement getEffectiveMergeStrategy method
        pass

    def getEffectiveReplace(self) -> bool:
        # TODO: Implement getEffectiveReplace method
        pass

class build_BSwitchExpression:

    pass
class build_BExecutionContext:

    pass
class ResolutionInfo:

    pass
class build_UnitResolutionInfo(ResolutionInfo):

    pass
class IBuildUnitRepository:

    pass
class build_BuildUnitRepository(IBuildUnitRepository):

    def __init__(self):
        
    def resolve(self, requiredCapability: RequiredCapability, options: str, ctx: str) -> str:
        # TODO: Implement resolve method
        pass

    def initialize(self, repository: str, ctx: str, options: str):
        # TODO: Implement initialize method
        pass

class PathGroupPredicate:

    pass
class BInnerContext:

    pass
class build_BuildResultContext(BInnerContext):

    pass
class ITypedValueContainer:

    pass
class build_BuildSet(ITypedValueContainer):

    def __init__(self, valueMap: str, pathIterator: str, build_BuildSet: set["build_PathVector"] = None):
        self.valueMap = valueMap
        self.pathIterator = pathIterator
        self.build_BuildSet = build_BuildSet if build_BuildSet is not None else set()
        
    @property
    def pathIterator(self) -> str:
        return self.__pathIterator

    @pathIterator.setter
    def pathIterator(self, pathIterator: str):
        self.__pathIterator = pathIterator

    @property
    def valueMap(self) -> str:
        return self.__valueMap

    @valueMap.setter
    def valueMap(self, valueMap: str):
        self.__valueMap = valueMap

    @property
    def build_BuildSet(self):
        return self.__build_BuildSet

    @build_BuildSet.setter
    def build_BuildSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildSet__build_BuildSet", None)
        self.__build_BuildSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_PathVector214"):
                    opp_val = getattr(item, "build_PathVector214", None)
                    
                    if opp_val == self:
                        setattr(item, "build_PathVector214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_PathVector214"):
                    opp_val = getattr(item, "build_PathVector214", None)
                    
                    setattr(item, "build_PathVector214", self)
                    

    def merge(self, buildResult: str) -> str:
        # TODO: Implement merge method
        pass

class build_BuilderCallFacade:

    def __init__(self, aliases: str, build_BuilderCallFacade: "build_BuilderCall" = None, build_BuilderCallFacade211: "build_RequiredCapability" = None):
        self.aliases = aliases
        self.build_BuilderCallFacade = build_BuilderCallFacade
        self.build_BuilderCallFacade211 = build_BuilderCallFacade211
        
    @property
    def aliases(self) -> str:
        return self.__aliases

    @aliases.setter
    def aliases(self, aliases: str):
        self.__aliases = aliases

    @property
    def build_BuilderCallFacade211(self):
        return self.__build_BuilderCallFacade211

    @build_BuilderCallFacade211.setter
    def build_BuilderCallFacade211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderCallFacade__build_BuilderCallFacade211", None)
        self.__build_BuilderCallFacade211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_RequiredCapability212"):
                opp_val = getattr(old_value, "build_RequiredCapability212", None)
                if opp_val == self:
                    setattr(old_value, "build_RequiredCapability212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_RequiredCapability212"):
                opp_val = getattr(value, "build_RequiredCapability212", None)
                setattr(value, "build_RequiredCapability212", self)

    @property
    def build_BuilderCallFacade(self):
        return self.__build_BuilderCallFacade

    @build_BuilderCallFacade.setter
    def build_BuilderCallFacade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderCallFacade__build_BuilderCallFacade", None)
        self.__build_BuilderCallFacade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuilderCall209"):
                opp_val = getattr(old_value, "build_BuilderCall209", None)
                if opp_val == self:
                    setattr(old_value, "build_BuilderCall209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuilderCall209"):
                opp_val = getattr(value, "build_BuilderCall209", None)
                setattr(value, "build_BuilderCall209", self)

class CompoundBuildUnitRepository:

    pass
class build_CompoundFirstFoundRepository(CompoundBuildUnitRepository):

    pass
class BuildUnitRepository:

    pass
class build_UnitRepositoryDescription(BuildUnitRepository):

    def __init__(self, evaluatedOptions: str, build_UnitRepositoryDescription: "build_Repository" = None):
        self.evaluatedOptions = evaluatedOptions
        self.build_UnitRepositoryDescription = build_UnitRepositoryDescription
        
    @property
    def evaluatedOptions(self) -> str:
        return self.__evaluatedOptions

    @evaluatedOptions.setter
    def evaluatedOptions(self, evaluatedOptions: str):
        self.__evaluatedOptions = evaluatedOptions

    @property
    def build_UnitRepositoryDescription(self):
        return self.__build_UnitRepositoryDescription

    @build_UnitRepositoryDescription.setter
    def build_UnitRepositoryDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitRepositoryDescription__build_UnitRepositoryDescription", None)
        self.__build_UnitRepositoryDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Repository250"):
                opp_val = getattr(old_value, "build_Repository250", None)
                if opp_val == self:
                    setattr(old_value, "build_Repository250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Repository250"):
                opp_val = getattr(value, "build_Repository250", None)
                setattr(value, "build_Repository250", self)

class build_ExecutionStackRepository(BuildUnitRepository):

    pass
class build_BeeModelRepository(BuildUnitRepository):

    pass
class build_CompoundBuildUnitRepository(BuildUnitRepository):

    pass
class IEffectiveFacade:

    pass
class build_EffectiveBuilderCallFacade(BuilderCallFacade, IEffectiveFacade):

    pass
class build_EffectiveFacade(IEffectiveFacade):

    pass
class build_ResolutionInfo:

    def __init__(self, status: str):
        self.status = status
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

class build_BeeHive:

    def __init__(self, resolutions: str, build_BeeHive: set["build_BeeModel"] = None, build_BeeHive189: "build_BeeHive" = None, build_BeeHive187: "build_BeeHive" = None):
        self.resolutions = resolutions
        self.build_BeeHive = build_BeeHive if build_BeeHive is not None else set()
        self.build_BeeHive189 = build_BeeHive189
        self.build_BeeHive187 = build_BeeHive187
        
    @property
    def resolutions(self) -> str:
        return self.__resolutions

    @resolutions.setter
    def resolutions(self, resolutions: str):
        self.__resolutions = resolutions

    @property
    def build_BeeHive189(self):
        return self.__build_BeeHive189

    @build_BeeHive189.setter
    def build_BeeHive189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeHive__build_BeeHive189", None)
        self.__build_BeeHive189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BeeHive187"):
                opp_val = getattr(old_value, "build_BeeHive187", None)
                if opp_val == self:
                    setattr(old_value, "build_BeeHive187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BeeHive187"):
                opp_val = getattr(value, "build_BeeHive187", None)
                setattr(value, "build_BeeHive187", self)

    @property
    def build_BeeHive(self):
        return self.__build_BeeHive

    @build_BeeHive.setter
    def build_BeeHive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeHive__build_BeeHive", None)
        self.__build_BeeHive = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BeeModel186"):
                    opp_val = getattr(item, "build_BeeModel186", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BeeModel186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BeeModel186"):
                    opp_val = getattr(item, "build_BeeModel186", None)
                    
                    setattr(item, "build_BeeModel186", self)
                    

    @property
    def build_BeeHive187(self):
        return self.__build_BeeHive187

    @build_BeeHive187.setter
    def build_BeeHive187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeHive__build_BeeHive187", None)
        self.__build_BeeHive187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BeeHive189"):
                opp_val = getattr(old_value, "build_BeeHive189", None)
                if opp_val == self:
                    setattr(old_value, "build_BeeHive189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BeeHive189"):
                opp_val = getattr(value, "build_BeeHive189", None)
                setattr(value, "build_BeeHive189", self)

    def getResolvedCapabilityContainer(self, requiredCapability: RequiredCapability) -> IProvidedCapabilityContainer:
        # TODO: Implement getResolvedCapabilityContainer method
        pass

class build_IFunction:

    pass
class EffectiveFacade:

    pass
class build_EffectiveRequirementFacade(EffectiveFacade):

    pass
class build_EffectiveCapabilityFacade(EffectiveFacade):

    pass
class build_EffectiveUnitFacade(EffectiveFacade):

    pass
class build_IProvidedCapabilityContainer(ABC):

    pass
class build_IRequiredCapabilityContainer(ABC):

    pass
class RequiredCapability:

    pass
class build_AliasedRequiredCapability(RequiredCapability):

    def __init__(self, alias: str):
        self.alias = alias
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

class IBuildUnitContainer:

    pass
class BChainedExpression:

    pass
class build_BeeModel(IBuildUnitContainer, BChainedExpression):

    def __init__(self, build_BeeModel: set["build_IType"] = None, build_BeeModel169: set["build_IFunction"] = None, build_BeeModel171: set["build_BConcern"] = None, build_BeeModel174: set["build_BPropertySet"] = None, build_BeeModel177: set["build_Repository"] = None, build_BeeModel180: set["build_FirstFoundUnitProvider"] = None, build_BeeModel183: "build_BPropertySet" = None, build_BeeModel186: "build_BeeHive" = None, build_BeeModel218: "build_BeeModelRepository" = None):
        self.build_BeeModel = build_BeeModel if build_BeeModel is not None else set()
        self.build_BeeModel169 = build_BeeModel169 if build_BeeModel169 is not None else set()
        self.build_BeeModel171 = build_BeeModel171 if build_BeeModel171 is not None else set()
        self.build_BeeModel174 = build_BeeModel174 if build_BeeModel174 is not None else set()
        self.build_BeeModel177 = build_BeeModel177 if build_BeeModel177 is not None else set()
        self.build_BeeModel180 = build_BeeModel180 if build_BeeModel180 is not None else set()
        self.build_BeeModel183 = build_BeeModel183
        self.build_BeeModel186 = build_BeeModel186
        self.build_BeeModel218 = build_BeeModel218
        
    @property
    def build_BeeModel171(self):
        return self.__build_BeeModel171

    @build_BeeModel171.setter
    def build_BeeModel171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel171", None)
        self.__build_BeeModel171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BConcern172"):
                    opp_val = getattr(item, "build_BConcern172", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BConcern172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BConcern172"):
                    opp_val = getattr(item, "build_BConcern172", None)
                    
                    setattr(item, "build_BConcern172", self)
                    

    @property
    def build_BeeModel186(self):
        return self.__build_BeeModel186

    @build_BeeModel186.setter
    def build_BeeModel186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel186", None)
        self.__build_BeeModel186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BeeHive"):
                opp_val = getattr(old_value, "build_BeeHive", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BeeHive"):
                opp_val = getattr(value, "build_BeeHive", None)
                if opp_val is None:
                    setattr(value, "build_BeeHive", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_BeeModel183(self):
        return self.__build_BeeModel183

    @build_BeeModel183.setter
    def build_BeeModel183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel183", None)
        self.__build_BeeModel183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BPropertySet184"):
                opp_val = getattr(old_value, "build_BPropertySet184", None)
                if opp_val == self:
                    setattr(old_value, "build_BPropertySet184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BPropertySet184"):
                opp_val = getattr(value, "build_BPropertySet184", None)
                setattr(value, "build_BPropertySet184", self)

    @property
    def build_BeeModel177(self):
        return self.__build_BeeModel177

    @build_BeeModel177.setter
    def build_BeeModel177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel177", None)
        self.__build_BeeModel177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Repository178"):
                    opp_val = getattr(item, "build_Repository178", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Repository178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Repository178"):
                    opp_val = getattr(item, "build_Repository178", None)
                    
                    setattr(item, "build_Repository178", self)
                    

    @property
    def build_BeeModel169(self):
        return self.__build_BeeModel169

    @build_BeeModel169.setter
    def build_BeeModel169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel169", None)
        self.__build_BeeModel169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IFunction"):
                    opp_val = getattr(item, "build_IFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IFunction"):
                    opp_val = getattr(item, "build_IFunction", None)
                    
                    setattr(item, "build_IFunction", self)
                    

    @property
    def build_BeeModel174(self):
        return self.__build_BeeModel174

    @build_BeeModel174.setter
    def build_BeeModel174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel174", None)
        self.__build_BeeModel174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BPropertySet175"):
                    opp_val = getattr(item, "build_BPropertySet175", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BPropertySet175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BPropertySet175"):
                    opp_val = getattr(item, "build_BPropertySet175", None)
                    
                    setattr(item, "build_BPropertySet175", self)
                    

    @property
    def build_BeeModel(self):
        return self.__build_BeeModel

    @build_BeeModel.setter
    def build_BeeModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel", None)
        self.__build_BeeModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IType167"):
                    opp_val = getattr(item, "build_IType167", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IType167", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IType167"):
                    opp_val = getattr(item, "build_IType167", None)
                    
                    setattr(item, "build_IType167", self)
                    

    @property
    def build_BeeModel218(self):
        return self.__build_BeeModel218

    @build_BeeModel218.setter
    def build_BeeModel218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel218", None)
        self.__build_BeeModel218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BeeModelRepository"):
                opp_val = getattr(old_value, "build_BeeModelRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BeeModelRepository"):
                opp_val = getattr(value, "build_BeeModelRepository", None)
                if opp_val is None:
                    setattr(value, "build_BeeModelRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_BeeModel180(self):
        return self.__build_BeeModel180

    @build_BeeModel180.setter
    def build_BeeModel180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BeeModel__build_BeeModel180", None)
        self.__build_BeeModel180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_FirstFoundUnitProvider181"):
                    opp_val = getattr(item, "build_FirstFoundUnitProvider181", None)
                    
                    if opp_val == self:
                        setattr(item, "build_FirstFoundUnitProvider181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_FirstFoundUnitProvider181"):
                    opp_val = getattr(item, "build_FirstFoundUnitProvider181", None)
                    
                    setattr(item, "build_FirstFoundUnitProvider181", self)
                    

    def getUnitProvider(self) -> str:
        # TODO: Implement getUnitProvider method
        pass

class BFunctionWrapper:

    pass
class BJavaFunction:

    pass
class IBuilder:

    pass
class build_BuilderWrapper(BFunctionWrapper, IBuilder):

    def __init__(self, inputAdvised: bool, outputAdvised: bool, unitTypeAdvised: bool, providesAdvised: bool, defaultPropertiesAdvised: bool, sourceAdvised: bool):
        self.inputAdvised = inputAdvised
        self.outputAdvised = outputAdvised
        self.unitTypeAdvised = unitTypeAdvised
        self.providesAdvised = providesAdvised
        self.defaultPropertiesAdvised = defaultPropertiesAdvised
        self.sourceAdvised = sourceAdvised
        
    @property
    def sourceAdvised(self) -> bool:
        return self.__sourceAdvised

    @sourceAdvised.setter
    def sourceAdvised(self, sourceAdvised: bool):
        self.__sourceAdvised = sourceAdvised

    @property
    def defaultPropertiesAdvised(self) -> bool:
        return self.__defaultPropertiesAdvised

    @defaultPropertiesAdvised.setter
    def defaultPropertiesAdvised(self, defaultPropertiesAdvised: bool):
        self.__defaultPropertiesAdvised = defaultPropertiesAdvised

    @property
    def providesAdvised(self) -> bool:
        return self.__providesAdvised

    @providesAdvised.setter
    def providesAdvised(self, providesAdvised: bool):
        self.__providesAdvised = providesAdvised

    @property
    def unitTypeAdvised(self) -> bool:
        return self.__unitTypeAdvised

    @unitTypeAdvised.setter
    def unitTypeAdvised(self, unitTypeAdvised: bool):
        self.__unitTypeAdvised = unitTypeAdvised

    @property
    def inputAdvised(self) -> bool:
        return self.__inputAdvised

    @inputAdvised.setter
    def inputAdvised(self, inputAdvised: bool):
        self.__inputAdvised = inputAdvised

    @property
    def outputAdvised(self) -> bool:
        return self.__outputAdvised

    @outputAdvised.setter
    def outputAdvised(self, outputAdvised: bool):
        self.__outputAdvised = outputAdvised

class build_BuilderJava(IBuilder, BJavaFunction):

    pass
class B3Function:

    pass
class build_Builder(IBuilder, B3Function):

    pass
class build_BParameterPredicate:

    pass
class build_OutputPredicate(PathGroupPredicate):

    pass
class build_SourcePredicate(PathGroupPredicate):

    pass
class BuildConcernContext:

    pass
class build_BuilderConcernContext(BuildConcernContext):

    def __init__(self, outputAnnotationsRemovals: str, varArgs: bool, matchParameters: bool, removePreCondition: bool, removePostCondition: bool, removePostInputCondition: bool, sourceAnnotationsRemovals: str, build_BuilderConcernContext107: "build_BExpression" = None, build_BuilderConcernContext110: set["build_BuilderInput"] = None, build_BuilderConcernContext: "build_UnitConcernContext" = None, build_BuilderConcernContext135: set["build_ProvidesPredicate"] = None, build_BuilderConcernContext138: "build_BPropertySet" = None, build_BuilderConcernContext141: set["build_SourcePredicate"] = None, build_BuilderConcernContext143: set["build_ConditionalPathVector"] = None, build_BuilderConcernContext113: set["build_InputPredicate"] = None, build_BuilderConcernContext116: set["build_ConditionalPathVector"] = None, build_BuilderConcernContext119: set["build_OutputPredicate"] = None, build_BuilderConcernContext121: "build_BExpression" = None, build_BuilderConcernContext124: set["build_BParameterPredicate"] = None, build_BuilderConcernContext126: "build_BExpression" = None, build_BuilderConcernContext129: "build_BExpression" = None, build_BuilderConcernContext132: "build_BExpression" = None, build_BuilderConcernContext146: "build_BPropertySet" = None):
        self.outputAnnotationsRemovals = outputAnnotationsRemovals
        self.varArgs = varArgs
        self.matchParameters = matchParameters
        self.removePreCondition = removePreCondition
        self.removePostCondition = removePostCondition
        self.removePostInputCondition = removePostInputCondition
        self.sourceAnnotationsRemovals = sourceAnnotationsRemovals
        self.build_BuilderConcernContext107 = build_BuilderConcernContext107
        self.build_BuilderConcernContext110 = build_BuilderConcernContext110 if build_BuilderConcernContext110 is not None else set()
        self.build_BuilderConcernContext = build_BuilderConcernContext
        self.build_BuilderConcernContext135 = build_BuilderConcernContext135 if build_BuilderConcernContext135 is not None else set()
        self.build_BuilderConcernContext138 = build_BuilderConcernContext138
        self.build_BuilderConcernContext141 = build_BuilderConcernContext141 if build_BuilderConcernContext141 is not None else set()
        self.build_BuilderConcernContext143 = build_BuilderConcernContext143 if build_BuilderConcernContext143 is not None else set()
        self.build_BuilderConcernContext113 = build_BuilderConcernContext113 if build_BuilderConcernContext113 is not None else set()
        self.build_BuilderConcernContext116 = build_BuilderConcernContext116 if build_BuilderConcernContext116 is not None else set()
        self.build_BuilderConcernContext119 = build_BuilderConcernContext119 if build_BuilderConcernContext119 is not None else set()
        self.build_BuilderConcernContext121 = build_BuilderConcernContext121
        self.build_BuilderConcernContext124 = build_BuilderConcernContext124 if build_BuilderConcernContext124 is not None else set()
        self.build_BuilderConcernContext126 = build_BuilderConcernContext126
        self.build_BuilderConcernContext129 = build_BuilderConcernContext129
        self.build_BuilderConcernContext132 = build_BuilderConcernContext132
        self.build_BuilderConcernContext146 = build_BuilderConcernContext146
        
    @property
    def removePostInputCondition(self) -> bool:
        return self.__removePostInputCondition

    @removePostInputCondition.setter
    def removePostInputCondition(self, removePostInputCondition: bool):
        self.__removePostInputCondition = removePostInputCondition

    @property
    def removePreCondition(self) -> bool:
        return self.__removePreCondition

    @removePreCondition.setter
    def removePreCondition(self, removePreCondition: bool):
        self.__removePreCondition = removePreCondition

    @property
    def outputAnnotationsRemovals(self) -> str:
        return self.__outputAnnotationsRemovals

    @outputAnnotationsRemovals.setter
    def outputAnnotationsRemovals(self, outputAnnotationsRemovals: str):
        self.__outputAnnotationsRemovals = outputAnnotationsRemovals

    @property
    def matchParameters(self) -> bool:
        return self.__matchParameters

    @matchParameters.setter
    def matchParameters(self, matchParameters: bool):
        self.__matchParameters = matchParameters

    @property
    def varArgs(self) -> bool:
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs

    @property
    def sourceAnnotationsRemovals(self) -> str:
        return self.__sourceAnnotationsRemovals

    @sourceAnnotationsRemovals.setter
    def sourceAnnotationsRemovals(self, sourceAnnotationsRemovals: str):
        self.__sourceAnnotationsRemovals = sourceAnnotationsRemovals

    @property
    def removePostCondition(self) -> bool:
        return self.__removePostCondition

    @removePostCondition.setter
    def removePostCondition(self, removePostCondition: bool):
        self.__removePostCondition = removePostCondition

    @property
    def build_BuilderConcernContext141(self):
        return self.__build_BuilderConcernContext141

    @build_BuilderConcernContext141.setter
    def build_BuilderConcernContext141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext141", None)
        self.__build_BuilderConcernContext141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_SourcePredicate"):
                    opp_val = getattr(item, "build_SourcePredicate", None)
                    
                    if opp_val == self:
                        setattr(item, "build_SourcePredicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_SourcePredicate"):
                    opp_val = getattr(item, "build_SourcePredicate", None)
                    
                    setattr(item, "build_SourcePredicate", self)
                    

    @property
    def build_BuilderConcernContext135(self):
        return self.__build_BuilderConcernContext135

    @build_BuilderConcernContext135.setter
    def build_BuilderConcernContext135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext135", None)
        self.__build_BuilderConcernContext135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_ProvidesPredicate136"):
                    opp_val = getattr(item, "build_ProvidesPredicate136", None)
                    
                    if opp_val == self:
                        setattr(item, "build_ProvidesPredicate136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_ProvidesPredicate136"):
                    opp_val = getattr(item, "build_ProvidesPredicate136", None)
                    
                    setattr(item, "build_ProvidesPredicate136", self)
                    

    @property
    def build_BuilderConcernContext143(self):
        return self.__build_BuilderConcernContext143

    @build_BuilderConcernContext143.setter
    def build_BuilderConcernContext143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext143", None)
        self.__build_BuilderConcernContext143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_ConditionalPathVector144"):
                    opp_val = getattr(item, "build_ConditionalPathVector144", None)
                    
                    if opp_val == self:
                        setattr(item, "build_ConditionalPathVector144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_ConditionalPathVector144"):
                    opp_val = getattr(item, "build_ConditionalPathVector144", None)
                    
                    setattr(item, "build_ConditionalPathVector144", self)
                    

    @property
    def build_BuilderConcernContext121(self):
        return self.__build_BuilderConcernContext121

    @build_BuilderConcernContext121.setter
    def build_BuilderConcernContext121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext121", None)
        self.__build_BuilderConcernContext121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression122"):
                opp_val = getattr(old_value, "build_BExpression122", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression122"):
                opp_val = getattr(value, "build_BExpression122", None)
                setattr(value, "build_BExpression122", self)

    @property
    def build_BuilderConcernContext110(self):
        return self.__build_BuilderConcernContext110

    @build_BuilderConcernContext110.setter
    def build_BuilderConcernContext110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext110", None)
        self.__build_BuilderConcernContext110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BuilderInput111"):
                    opp_val = getattr(item, "build_BuilderInput111", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BuilderInput111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BuilderInput111"):
                    opp_val = getattr(item, "build_BuilderInput111", None)
                    
                    setattr(item, "build_BuilderInput111", self)
                    

    @property
    def build_BuilderConcernContext126(self):
        return self.__build_BuilderConcernContext126

    @build_BuilderConcernContext126.setter
    def build_BuilderConcernContext126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext126", None)
        self.__build_BuilderConcernContext126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression127"):
                opp_val = getattr(old_value, "build_BExpression127", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression127"):
                opp_val = getattr(value, "build_BExpression127", None)
                setattr(value, "build_BExpression127", self)

    @property
    def build_BuilderConcernContext129(self):
        return self.__build_BuilderConcernContext129

    @build_BuilderConcernContext129.setter
    def build_BuilderConcernContext129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext129", None)
        self.__build_BuilderConcernContext129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression130"):
                opp_val = getattr(old_value, "build_BExpression130", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression130"):
                opp_val = getattr(value, "build_BExpression130", None)
                setattr(value, "build_BExpression130", self)

    @property
    def build_BuilderConcernContext116(self):
        return self.__build_BuilderConcernContext116

    @build_BuilderConcernContext116.setter
    def build_BuilderConcernContext116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext116", None)
        self.__build_BuilderConcernContext116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_ConditionalPathVector117"):
                    opp_val = getattr(item, "build_ConditionalPathVector117", None)
                    
                    if opp_val == self:
                        setattr(item, "build_ConditionalPathVector117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_ConditionalPathVector117"):
                    opp_val = getattr(item, "build_ConditionalPathVector117", None)
                    
                    setattr(item, "build_ConditionalPathVector117", self)
                    

    @property
    def build_BuilderConcernContext113(self):
        return self.__build_BuilderConcernContext113

    @build_BuilderConcernContext113.setter
    def build_BuilderConcernContext113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext113", None)
        self.__build_BuilderConcernContext113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_InputPredicate114"):
                    opp_val = getattr(item, "build_InputPredicate114", None)
                    
                    if opp_val == self:
                        setattr(item, "build_InputPredicate114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_InputPredicate114"):
                    opp_val = getattr(item, "build_InputPredicate114", None)
                    
                    setattr(item, "build_InputPredicate114", self)
                    

    @property
    def build_BuilderConcernContext146(self):
        return self.__build_BuilderConcernContext146

    @build_BuilderConcernContext146.setter
    def build_BuilderConcernContext146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext146", None)
        self.__build_BuilderConcernContext146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BPropertySet147"):
                opp_val = getattr(old_value, "build_BPropertySet147", None)
                if opp_val == self:
                    setattr(old_value, "build_BPropertySet147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BPropertySet147"):
                opp_val = getattr(value, "build_BPropertySet147", None)
                setattr(value, "build_BPropertySet147", self)

    @property
    def build_BuilderConcernContext107(self):
        return self.__build_BuilderConcernContext107

    @build_BuilderConcernContext107.setter
    def build_BuilderConcernContext107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext107", None)
        self.__build_BuilderConcernContext107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression108"):
                opp_val = getattr(old_value, "build_BExpression108", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression108"):
                opp_val = getattr(value, "build_BExpression108", None)
                setattr(value, "build_BExpression108", self)

    @property
    def build_BuilderConcernContext138(self):
        return self.__build_BuilderConcernContext138

    @build_BuilderConcernContext138.setter
    def build_BuilderConcernContext138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext138", None)
        self.__build_BuilderConcernContext138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BPropertySet139"):
                opp_val = getattr(old_value, "build_BPropertySet139", None)
                if opp_val == self:
                    setattr(old_value, "build_BPropertySet139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BPropertySet139"):
                opp_val = getattr(value, "build_BPropertySet139", None)
                setattr(value, "build_BPropertySet139", self)

    @property
    def build_BuilderConcernContext132(self):
        return self.__build_BuilderConcernContext132

    @build_BuilderConcernContext132.setter
    def build_BuilderConcernContext132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext132", None)
        self.__build_BuilderConcernContext132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression133"):
                opp_val = getattr(old_value, "build_BExpression133", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression133"):
                opp_val = getattr(value, "build_BExpression133", None)
                setattr(value, "build_BExpression133", self)

    @property
    def build_BuilderConcernContext119(self):
        return self.__build_BuilderConcernContext119

    @build_BuilderConcernContext119.setter
    def build_BuilderConcernContext119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext119", None)
        self.__build_BuilderConcernContext119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_OutputPredicate"):
                    opp_val = getattr(item, "build_OutputPredicate", None)
                    
                    if opp_val == self:
                        setattr(item, "build_OutputPredicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_OutputPredicate"):
                    opp_val = getattr(item, "build_OutputPredicate", None)
                    
                    setattr(item, "build_OutputPredicate", self)
                    

    @property
    def build_BuilderConcernContext124(self):
        return self.__build_BuilderConcernContext124

    @build_BuilderConcernContext124.setter
    def build_BuilderConcernContext124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext124", None)
        self.__build_BuilderConcernContext124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BParameterPredicate"):
                    opp_val = getattr(item, "build_BParameterPredicate", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BParameterPredicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BParameterPredicate"):
                    opp_val = getattr(item, "build_BParameterPredicate", None)
                    
                    setattr(item, "build_BParameterPredicate", self)
                    

    @property
    def build_BuilderConcernContext(self):
        return self.__build_BuilderConcernContext

    @build_BuilderConcernContext.setter
    def build_BuilderConcernContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderConcernContext__build_BuilderConcernContext", None)
        self.__build_BuilderConcernContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitConcernContext"):
                opp_val = getattr(old_value, "build_UnitConcernContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitConcernContext"):
                opp_val = getattr(value, "build_UnitConcernContext", None)
                if opp_val is None:
                    setattr(value, "build_UnitConcernContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CapabilityPredicate:

    pass
class build_UnitNamePredicate(CapabilityPredicate):

    pass
class build_NameSpacePredicate:

    def __init__(self, nameSpace: str):
        self.nameSpace = nameSpace
        
    @property
    def nameSpace(self) -> str:
        return self.__nameSpace

    @nameSpace.setter
    def nameSpace(self, nameSpace: str):
        self.__nameSpace = nameSpace

class BConcernContext:

    pass
class CompoundUnitProvider:

    pass
class build_BestFoundUnitProvider(CompoundUnitProvider):

    pass
class build_IBuildUnitRepository(ABC):

    pass
class build_RepoOption:

    def __init__(self, name: str, build_RepoOption: "build_RepositoryUnitProvider" = None, build_RepoOption228: "build_Repository" = None, build_RepoOption247: "build_BExpression" = None):
        self.name = name
        self.build_RepoOption = build_RepoOption
        self.build_RepoOption228 = build_RepoOption228
        self.build_RepoOption247 = build_RepoOption247
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def build_RepoOption247(self):
        return self.__build_RepoOption247

    @build_RepoOption247.setter
    def build_RepoOption247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RepoOption__build_RepoOption247", None)
        self.__build_RepoOption247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression248"):
                opp_val = getattr(old_value, "build_BExpression248", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression248"):
                opp_val = getattr(value, "build_BExpression248", None)
                setattr(value, "build_BExpression248", self)

    @property
    def build_RepoOption228(self):
        return self.__build_RepoOption228

    @build_RepoOption228.setter
    def build_RepoOption228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RepoOption__build_RepoOption228", None)
        self.__build_RepoOption228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Repository227"):
                opp_val = getattr(old_value, "build_Repository227", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Repository227"):
                opp_val = getattr(value, "build_Repository227", None)
                if opp_val is None:
                    setattr(value, "build_Repository227", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_RepoOption(self):
        return self.__build_RepoOption

    @build_RepoOption.setter
    def build_RepoOption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RepoOption__build_RepoOption", None)
        self.__build_RepoOption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_RepositoryUnitProvider64"):
                opp_val = getattr(old_value, "build_RepositoryUnitProvider64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_RepositoryUnitProvider64"):
                opp_val = getattr(value, "build_RepositoryUnitProvider64", None)
                if opp_val is None:
                    setattr(value, "build_RepositoryUnitProvider64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class build_BNamePredicate:

    pass
class build_PathVector:

    def __init__(self, paths: str, basePath: str, build_PathVector: "build_ConditionalPathVector" = None, build_PathVector149: "build_PathGroupPredicate" = None, build_PathVector214: "build_BuildSet" = None):
        self.paths = paths
        self.basePath = basePath
        self.build_PathVector = build_PathVector
        self.build_PathVector149 = build_PathVector149
        self.build_PathVector214 = build_PathVector214
        
    @property
    def paths(self) -> str:
        return self.__paths

    @paths.setter
    def paths(self, paths: str):
        self.__paths = paths

    @property
    def basePath(self) -> str:
        return self.__basePath

    @basePath.setter
    def basePath(self, basePath: str):
        self.__basePath = basePath

    @property
    def build_PathVector149(self):
        return self.__build_PathVector149

    @build_PathVector149.setter
    def build_PathVector149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_PathVector__build_PathVector149", None)
        self.__build_PathVector149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_PathGroupPredicate"):
                opp_val = getattr(old_value, "build_PathGroupPredicate", None)
                if opp_val == self:
                    setattr(old_value, "build_PathGroupPredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_PathGroupPredicate"):
                opp_val = getattr(value, "build_PathGroupPredicate", None)
                setattr(value, "build_PathGroupPredicate", self)

    @property
    def build_PathVector214(self):
        return self.__build_PathVector214

    @build_PathVector214.setter
    def build_PathVector214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_PathVector__build_PathVector214", None)
        self.__build_PathVector214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildSet"):
                opp_val = getattr(old_value, "build_BuildSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildSet"):
                opp_val = getattr(value, "build_BuildSet", None)
                if opp_val is None:
                    setattr(value, "build_BuildSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_PathVector(self):
        return self.__build_PathVector

    @build_PathVector.setter
    def build_PathVector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_PathVector__build_PathVector", None)
        self.__build_PathVector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_ConditionalPathVector58"):
                opp_val = getattr(old_value, "build_ConditionalPathVector58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_ConditionalPathVector58"):
                opp_val = getattr(value, "build_ConditionalPathVector58", None)
                if opp_val is None:
                    setattr(value, "build_ConditionalPathVector58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def resolve(self, baseUri: str) -> str:
        # TODO: Implement resolve method
        pass

class INamedValue:

    pass
class build_BuilderInputNameDecorator(INamedValue, BuilderInputDecorator):

    pass
class build_Capability(INamedValue):

    def __init__(self, nameSpace: str, build_Capability: "build_BExpression" = None, build_Capability159: "build_IProvidedCapabilityContainer" = None, build_Capability207: "build_EffectiveCapabilityFacade" = None):
        self.nameSpace = nameSpace
        self.build_Capability = build_Capability
        self.build_Capability159 = build_Capability159
        self.build_Capability207 = build_Capability207
        
    @property
    def nameSpace(self) -> str:
        return self.__nameSpace

    @nameSpace.setter
    def nameSpace(self, nameSpace: str):
        self.__nameSpace = nameSpace

    @property
    def build_Capability(self):
        return self.__build_Capability

    @build_Capability.setter
    def build_Capability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Capability__build_Capability", None)
        self.__build_Capability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression53"):
                opp_val = getattr(old_value, "build_BExpression53", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression53"):
                opp_val = getattr(value, "build_BExpression53", None)
                setattr(value, "build_BExpression53", self)

    @property
    def build_Capability207(self):
        return self.__build_Capability207

    @build_Capability207.setter
    def build_Capability207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Capability__build_Capability207", None)
        self.__build_Capability207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_EffectiveCapabilityFacade206"):
                opp_val = getattr(old_value, "build_EffectiveCapabilityFacade206", None)
                if opp_val == self:
                    setattr(old_value, "build_EffectiveCapabilityFacade206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_EffectiveCapabilityFacade206"):
                opp_val = getattr(value, "build_EffectiveCapabilityFacade206", None)
                setattr(value, "build_EffectiveCapabilityFacade206", self)

    @property
    def build_Capability159(self):
        return self.__build_Capability159

    @build_Capability159.setter
    def build_Capability159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Capability__build_Capability159", None)
        self.__build_Capability159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IProvidedCapabilityContainer"):
                opp_val = getattr(old_value, "build_IProvidedCapabilityContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IProvidedCapabilityContainer"):
                opp_val = getattr(value, "build_IProvidedCapabilityContainer", None)
                if opp_val is None:
                    setattr(value, "build_IProvidedCapabilityContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def satisfies(self, requirement: str) -> bool:
        # TODO: Implement satisfies method
        pass

class build_BParameterList:

    pass
class BuilderInput:

    pass
class build_BuilderCall(BuilderInput):

    def __init__(self, builderName: str, build_BuilderCall: "build_BParameterList" = None, build_BuilderCall209: "build_BuilderCallFacade" = None):
        self.builderName = builderName
        self.build_BuilderCall = build_BuilderCall
        self.build_BuilderCall209 = build_BuilderCall209
        
    @property
    def builderName(self) -> str:
        return self.__builderName

    @builderName.setter
    def builderName(self, builderName: str):
        self.__builderName = builderName

    @property
    def build_BuilderCall(self):
        return self.__build_BuilderCall

    @build_BuilderCall.setter
    def build_BuilderCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderCall__build_BuilderCall", None)
        self.__build_BuilderCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BParameterList"):
                opp_val = getattr(old_value, "build_BParameterList", None)
                if opp_val == self:
                    setattr(old_value, "build_BParameterList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BParameterList"):
                opp_val = getattr(value, "build_BParameterList", None)
                setattr(value, "build_BParameterList", self)

    @property
    def build_BuilderCall209(self):
        return self.__build_BuilderCall209

    @build_BuilderCall209.setter
    def build_BuilderCall209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuilderCall__build_BuilderCall209", None)
        self.__build_BuilderCall209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuilderCallFacade"):
                opp_val = getattr(old_value, "build_BuilderCallFacade", None)
                if opp_val == self:
                    setattr(old_value, "build_BuilderCallFacade", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuilderCallFacade"):
                opp_val = getattr(value, "build_BuilderCallFacade", None)
                setattr(value, "build_BuilderCallFacade", self)

class build_BuilderInputDecorator(BuilderInput):

    pass
class UnitProvider:

    pass
class build_DelegatingUnitProvider(UnitProvider):

    pass
class build_SwitchUnitProvider(UnitProvider):

    pass
class build_CompoundUnitProvider(UnitProvider):

    pass
class build_RepositoryUnitProvider(UnitProvider):

    pass
class BExpression:

    pass
class build_BuilderNamePredicate(BExpression):

    pass
class build_PathGroupPredicate(BExpression):

    def __init__(self, build_PathGroupPredicate: "build_PathVector" = None, build_PathGroupPredicate151: "build_BExpression" = None):
        self.build_PathGroupPredicate = build_PathGroupPredicate
        self.build_PathGroupPredicate151 = build_PathGroupPredicate151
        
    @property
    def build_PathGroupPredicate(self):
        return self.__build_PathGroupPredicate

    @build_PathGroupPredicate.setter
    def build_PathGroupPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_PathGroupPredicate__build_PathGroupPredicate", None)
        self.__build_PathGroupPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_PathVector149"):
                opp_val = getattr(old_value, "build_PathVector149", None)
                if opp_val == self:
                    setattr(old_value, "build_PathVector149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_PathVector149"):
                opp_val = getattr(value, "build_PathVector149", None)
                setattr(value, "build_PathVector149", self)

    @property
    def build_PathGroupPredicate151(self):
        return self.__build_PathGroupPredicate151

    @build_PathGroupPredicate151.setter
    def build_PathGroupPredicate151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_PathGroupPredicate__build_PathGroupPredicate151", None)
        self.__build_PathGroupPredicate151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression152"):
                opp_val = getattr(old_value, "build_BExpression152", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression152"):
                opp_val = getattr(value, "build_BExpression152", None)
                setattr(value, "build_BExpression152", self)

    def removeMatching(self, input: str) -> bool:
        # TODO: Implement removeMatching method
        pass

class build_RequiresPredicate(BExpression):

    def __init__(self, meta: bool, build_RequiresPredicate: "build_CapabilityPredicate" = None, build_RequiresPredicate99: "build_UnitConcernContext" = None):
        self.meta = meta
        self.build_RequiresPredicate = build_RequiresPredicate
        self.build_RequiresPredicate99 = build_RequiresPredicate99
        
    @property
    def meta(self) -> bool:
        return self.__meta

    @meta.setter
    def meta(self, meta: bool):
        self.__meta = meta

    @property
    def build_RequiresPredicate(self):
        return self.__build_RequiresPredicate

    @build_RequiresPredicate.setter
    def build_RequiresPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiresPredicate__build_RequiresPredicate", None)
        self.__build_RequiresPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_CapabilityPredicate"):
                opp_val = getattr(old_value, "build_CapabilityPredicate", None)
                if opp_val == self:
                    setattr(old_value, "build_CapabilityPredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_CapabilityPredicate"):
                opp_val = getattr(value, "build_CapabilityPredicate", None)
                setattr(value, "build_CapabilityPredicate", self)

    @property
    def build_RequiresPredicate99(self):
        return self.__build_RequiresPredicate99

    @build_RequiresPredicate99.setter
    def build_RequiresPredicate99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiresPredicate__build_RequiresPredicate99", None)
        self.__build_RequiresPredicate99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitConcernContext98"):
                opp_val = getattr(old_value, "build_UnitConcernContext98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitConcernContext98"):
                opp_val = getattr(value, "build_UnitConcernContext98", None)
                if opp_val is None:
                    setattr(value, "build_UnitConcernContext98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def matches(self, candidate: str) -> bool:
        # TODO: Implement matches method
        pass

class build_CapabilityPredicate(BExpression):

    def __init__(self, versionRange: str, build_CapabilityPredicate78: "build_BNamePredicate" = None, build_CapabilityPredicate80: "build_BNamePredicate" = None, build_CapabilityPredicate: "build_RequiresPredicate" = None, build_CapabilityPredicate105: "build_UnitConcernContext" = None, build_CapabilityPredicate85: "build_ProvidesPredicate" = None, build_CapabilityPredicate89: "build_InputPredicate" = None, build_CapabilityPredicate157: "build_IRequiredCapabilityContainer" = None, build_CapabilityPredicate252: "build_BuildCallOnSelectedRequirements" = None):
        self.versionRange = versionRange
        self.build_CapabilityPredicate78 = build_CapabilityPredicate78
        self.build_CapabilityPredicate80 = build_CapabilityPredicate80
        self.build_CapabilityPredicate = build_CapabilityPredicate
        self.build_CapabilityPredicate105 = build_CapabilityPredicate105
        self.build_CapabilityPredicate85 = build_CapabilityPredicate85
        self.build_CapabilityPredicate89 = build_CapabilityPredicate89
        self.build_CapabilityPredicate157 = build_CapabilityPredicate157
        self.build_CapabilityPredicate252 = build_CapabilityPredicate252
        
    @property
    def versionRange(self) -> str:
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange

    @property
    def build_CapabilityPredicate80(self):
        return self.__build_CapabilityPredicate80

    @build_CapabilityPredicate80.setter
    def build_CapabilityPredicate80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate80", None)
        self.__build_CapabilityPredicate80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BNamePredicate81"):
                opp_val = getattr(old_value, "build_BNamePredicate81", None)
                if opp_val == self:
                    setattr(old_value, "build_BNamePredicate81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BNamePredicate81"):
                opp_val = getattr(value, "build_BNamePredicate81", None)
                setattr(value, "build_BNamePredicate81", self)

    @property
    def build_CapabilityPredicate78(self):
        return self.__build_CapabilityPredicate78

    @build_CapabilityPredicate78.setter
    def build_CapabilityPredicate78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate78", None)
        self.__build_CapabilityPredicate78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BNamePredicate"):
                opp_val = getattr(old_value, "build_BNamePredicate", None)
                if opp_val == self:
                    setattr(old_value, "build_BNamePredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BNamePredicate"):
                opp_val = getattr(value, "build_BNamePredicate", None)
                setattr(value, "build_BNamePredicate", self)

    @property
    def build_CapabilityPredicate85(self):
        return self.__build_CapabilityPredicate85

    @build_CapabilityPredicate85.setter
    def build_CapabilityPredicate85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate85", None)
        self.__build_CapabilityPredicate85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_ProvidesPredicate"):
                opp_val = getattr(old_value, "build_ProvidesPredicate", None)
                if opp_val == self:
                    setattr(old_value, "build_ProvidesPredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_ProvidesPredicate"):
                opp_val = getattr(value, "build_ProvidesPredicate", None)
                setattr(value, "build_ProvidesPredicate", self)

    @property
    def build_CapabilityPredicate105(self):
        return self.__build_CapabilityPredicate105

    @build_CapabilityPredicate105.setter
    def build_CapabilityPredicate105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate105", None)
        self.__build_CapabilityPredicate105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitConcernContext104"):
                opp_val = getattr(old_value, "build_UnitConcernContext104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitConcernContext104"):
                opp_val = getattr(value, "build_UnitConcernContext104", None)
                if opp_val is None:
                    setattr(value, "build_UnitConcernContext104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_CapabilityPredicate157(self):
        return self.__build_CapabilityPredicate157

    @build_CapabilityPredicate157.setter
    def build_CapabilityPredicate157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate157", None)
        self.__build_CapabilityPredicate157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IRequiredCapabilityContainer156"):
                opp_val = getattr(old_value, "build_IRequiredCapabilityContainer156", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IRequiredCapabilityContainer156"):
                opp_val = getattr(value, "build_IRequiredCapabilityContainer156", None)
                if opp_val is None:
                    setattr(value, "build_IRequiredCapabilityContainer156", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_CapabilityPredicate252(self):
        return self.__build_CapabilityPredicate252

    @build_CapabilityPredicate252.setter
    def build_CapabilityPredicate252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate252", None)
        self.__build_CapabilityPredicate252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildCallOnSelectedRequirements"):
                opp_val = getattr(old_value, "build_BuildCallOnSelectedRequirements", None)
                if opp_val == self:
                    setattr(old_value, "build_BuildCallOnSelectedRequirements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildCallOnSelectedRequirements"):
                opp_val = getattr(value, "build_BuildCallOnSelectedRequirements", None)
                setattr(value, "build_BuildCallOnSelectedRequirements", self)

    @property
    def build_CapabilityPredicate(self):
        return self.__build_CapabilityPredicate

    @build_CapabilityPredicate.setter
    def build_CapabilityPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate", None)
        self.__build_CapabilityPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_RequiresPredicate"):
                opp_val = getattr(old_value, "build_RequiresPredicate", None)
                if opp_val == self:
                    setattr(old_value, "build_RequiresPredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_RequiresPredicate"):
                opp_val = getattr(value, "build_RequiresPredicate", None)
                setattr(value, "build_RequiresPredicate", self)

    @property
    def build_CapabilityPredicate89(self):
        return self.__build_CapabilityPredicate89

    @build_CapabilityPredicate89.setter
    def build_CapabilityPredicate89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_CapabilityPredicate__build_CapabilityPredicate89", None)
        self.__build_CapabilityPredicate89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_InputPredicate"):
                opp_val = getattr(old_value, "build_InputPredicate", None)
                if opp_val == self:
                    setattr(old_value, "build_InputPredicate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_InputPredicate"):
                opp_val = getattr(value, "build_InputPredicate", None)
                setattr(value, "build_InputPredicate", self)

    def matches(self, candidate: VersionedCapability) -> bool:
        # TODO: Implement matches method
        pass

    def matches(self, candidate: str) -> bool:
        # TODO: Implement matches method
        pass

    def matches(self, candidate: Capability) -> bool:
        # TODO: Implement matches method
        pass

class build_ProvidesPredicate(BExpression):

    def __init__(self, build_ProvidesPredicate: "build_CapabilityPredicate" = None, build_ProvidesPredicate102: "build_UnitConcernContext" = None, build_ProvidesPredicate136: "build_BuilderConcernContext" = None):
        self.build_ProvidesPredicate = build_ProvidesPredicate
        self.build_ProvidesPredicate102 = build_ProvidesPredicate102
        self.build_ProvidesPredicate136 = build_ProvidesPredicate136
        
    @property
    def build_ProvidesPredicate102(self):
        return self.__build_ProvidesPredicate102

    @build_ProvidesPredicate102.setter
    def build_ProvidesPredicate102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ProvidesPredicate__build_ProvidesPredicate102", None)
        self.__build_ProvidesPredicate102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitConcernContext101"):
                opp_val = getattr(old_value, "build_UnitConcernContext101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitConcernContext101"):
                opp_val = getattr(value, "build_UnitConcernContext101", None)
                if opp_val is None:
                    setattr(value, "build_UnitConcernContext101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_ProvidesPredicate(self):
        return self.__build_ProvidesPredicate

    @build_ProvidesPredicate.setter
    def build_ProvidesPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ProvidesPredicate__build_ProvidesPredicate", None)
        self.__build_ProvidesPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_CapabilityPredicate85"):
                opp_val = getattr(old_value, "build_CapabilityPredicate85", None)
                if opp_val == self:
                    setattr(old_value, "build_CapabilityPredicate85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_CapabilityPredicate85"):
                opp_val = getattr(value, "build_CapabilityPredicate85", None)
                setattr(value, "build_CapabilityPredicate85", self)

    @property
    def build_ProvidesPredicate136(self):
        return self.__build_ProvidesPredicate136

    @build_ProvidesPredicate136.setter
    def build_ProvidesPredicate136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ProvidesPredicate__build_ProvidesPredicate136", None)
        self.__build_ProvidesPredicate136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuilderConcernContext135"):
                opp_val = getattr(old_value, "build_BuilderConcernContext135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuilderConcernContext135"):
                opp_val = getattr(value, "build_BuilderConcernContext135", None)
                if opp_val is None:
                    setattr(value, "build_BuilderConcernContext135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def matches(self, candidate: VersionedCapability) -> bool:
        # TODO: Implement matches method
        pass

    def matches(self, candidate: Capability) -> bool:
        # TODO: Implement matches method
        pass

    def removeMatching(self, input: str) -> bool:
        # TODO: Implement removeMatching method
        pass

class build_InputPredicate(BExpression):

    pass
class build_ImplementsPredicate(BExpression):

    pass
class build_UnitProvider(BExpression):

    def __init__(self, documentation: str, build_UnitProvider: "build_CompoundUnitProvider" = None, build_UnitProvider245: "build_DelegatingUnitProvider" = None):
        self.documentation = documentation
        self.build_UnitProvider = build_UnitProvider
        self.build_UnitProvider245 = build_UnitProvider245
        
    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def build_UnitProvider245(self):
        return self.__build_UnitProvider245

    @build_UnitProvider245.setter
    def build_UnitProvider245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitProvider__build_UnitProvider245", None)
        self.__build_UnitProvider245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_DelegatingUnitProvider"):
                opp_val = getattr(old_value, "build_DelegatingUnitProvider", None)
                if opp_val == self:
                    setattr(old_value, "build_DelegatingUnitProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_DelegatingUnitProvider"):
                opp_val = getattr(value, "build_DelegatingUnitProvider", None)
                setattr(value, "build_DelegatingUnitProvider", self)

    @property
    def build_UnitProvider(self):
        return self.__build_UnitProvider

    @build_UnitProvider.setter
    def build_UnitProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitProvider__build_UnitProvider", None)
        self.__build_UnitProvider = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_CompoundUnitProvider"):
                opp_val = getattr(old_value, "build_CompoundUnitProvider", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_CompoundUnitProvider"):
                opp_val = getattr(value, "build_CompoundUnitProvider", None)
                if opp_val is None:
                    setattr(value, "build_CompoundUnitProvider", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def resolve(self, effectiveRequirement: str) -> str:
        # TODO: Implement resolve method
        pass

    def resolve(self, ctx: str, requiredCapability: str) -> str:
        # TODO: Implement resolve method
        pass

class build_BuilderQuery:

    pass
class build_PathGroup:

    pass
class build_BuilderInput:

    pass
class build_BExpression:

    pass
class IFunction:

    pass
class build_FragmentHost:

    pass
class build_IBuildUnitContainer(ABC):

    pass
class build_FirstFoundUnitProvider(CompoundUnitProvider):

    pass
class build_ConditionalPathVector:

    pass
class Capability:

    pass
class build_VersionedCapability(Capability):

    def __init__(self, version: str):
        self.version = version
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

class build_UnitParameterDeclaration(BParameterDeclaration):

    def __init__(self, build_UnitParameterDeclaration: "build_IBuilder" = None):
        self.build_UnitParameterDeclaration = build_UnitParameterDeclaration
        
    @property
    def build_UnitParameterDeclaration(self):
        return self.__build_UnitParameterDeclaration

    @build_UnitParameterDeclaration.setter
    def build_UnitParameterDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitParameterDeclaration__build_UnitParameterDeclaration", None)
        self.__build_UnitParameterDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuilder40"):
                opp_val = getattr(old_value, "build_IBuilder40", None)
                if opp_val == self:
                    setattr(old_value, "build_IBuilder40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuilder40"):
                opp_val = getattr(value, "build_IBuilder40", None)
                setattr(value, "build_IBuilder40", self)

    def hasCorrectState(self, chain: str, map: str) -> bool:
        # TODO: Implement hasCorrectState method
        pass

class build_BConcern:

    pass
class build_IType:

    pass
class build_RequiredCapability(Capability):

    def __init__(self, versionRange: str, greedy: bool, max: int, min: int, build_RequiredCapability: "build_BuildUnit" = None, build_RequiredCapability154: "build_IRequiredCapabilityContainer" = None, build_RequiredCapability204: "build_EffectiveRequirementFacade" = None, build_RequiredCapability212: "build_BuilderCallFacade" = None, build_RequiredCapability269: "build_FragmentHost" = None, build_RequiredCapability257: "build_BuildCallSingle" = None, build_RequiredCapability259: "build_BuildCallOnDeclaredRequirement" = None, build_RequiredCapability261: "build_BuildCallOnReferencedRequirement" = None):
        self.versionRange = versionRange
        self.greedy = greedy
        self.max = max
        self.min = min
        self.build_RequiredCapability = build_RequiredCapability
        self.build_RequiredCapability154 = build_RequiredCapability154
        self.build_RequiredCapability204 = build_RequiredCapability204
        self.build_RequiredCapability212 = build_RequiredCapability212
        self.build_RequiredCapability269 = build_RequiredCapability269
        self.build_RequiredCapability257 = build_RequiredCapability257
        self.build_RequiredCapability259 = build_RequiredCapability259
        self.build_RequiredCapability261 = build_RequiredCapability261
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def versionRange(self) -> str:
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange

    @property
    def greedy(self) -> bool:
        return self.__greedy

    @greedy.setter
    def greedy(self, greedy: bool):
        self.__greedy = greedy

    @property
    def build_RequiredCapability259(self):
        return self.__build_RequiredCapability259

    @build_RequiredCapability259.setter
    def build_RequiredCapability259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability259", None)
        self.__build_RequiredCapability259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildCallOnDeclaredRequirement"):
                opp_val = getattr(old_value, "build_BuildCallOnDeclaredRequirement", None)
                if opp_val == self:
                    setattr(old_value, "build_BuildCallOnDeclaredRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildCallOnDeclaredRequirement"):
                opp_val = getattr(value, "build_BuildCallOnDeclaredRequirement", None)
                setattr(value, "build_BuildCallOnDeclaredRequirement", self)

    @property
    def build_RequiredCapability204(self):
        return self.__build_RequiredCapability204

    @build_RequiredCapability204.setter
    def build_RequiredCapability204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability204", None)
        self.__build_RequiredCapability204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_EffectiveRequirementFacade203"):
                opp_val = getattr(old_value, "build_EffectiveRequirementFacade203", None)
                if opp_val == self:
                    setattr(old_value, "build_EffectiveRequirementFacade203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_EffectiveRequirementFacade203"):
                opp_val = getattr(value, "build_EffectiveRequirementFacade203", None)
                setattr(value, "build_EffectiveRequirementFacade203", self)

    @property
    def build_RequiredCapability(self):
        return self.__build_RequiredCapability

    @build_RequiredCapability.setter
    def build_RequiredCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability", None)
        self.__build_RequiredCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildUnit2"):
                opp_val = getattr(old_value, "build_BuildUnit2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildUnit2"):
                opp_val = getattr(value, "build_BuildUnit2", None)
                if opp_val is None:
                    setattr(value, "build_BuildUnit2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_RequiredCapability261(self):
        return self.__build_RequiredCapability261

    @build_RequiredCapability261.setter
    def build_RequiredCapability261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability261", None)
        self.__build_RequiredCapability261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildCallOnReferencedRequirement"):
                opp_val = getattr(old_value, "build_BuildCallOnReferencedRequirement", None)
                if opp_val == self:
                    setattr(old_value, "build_BuildCallOnReferencedRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildCallOnReferencedRequirement"):
                opp_val = getattr(value, "build_BuildCallOnReferencedRequirement", None)
                setattr(value, "build_BuildCallOnReferencedRequirement", self)

    @property
    def build_RequiredCapability212(self):
        return self.__build_RequiredCapability212

    @build_RequiredCapability212.setter
    def build_RequiredCapability212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability212", None)
        self.__build_RequiredCapability212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuilderCallFacade211"):
                opp_val = getattr(old_value, "build_BuilderCallFacade211", None)
                if opp_val == self:
                    setattr(old_value, "build_BuilderCallFacade211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuilderCallFacade211"):
                opp_val = getattr(value, "build_BuilderCallFacade211", None)
                setattr(value, "build_BuilderCallFacade211", self)

    @property
    def build_RequiredCapability257(self):
        return self.__build_RequiredCapability257

    @build_RequiredCapability257.setter
    def build_RequiredCapability257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability257", None)
        self.__build_RequiredCapability257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildCallSingle"):
                opp_val = getattr(old_value, "build_BuildCallSingle", None)
                if opp_val == self:
                    setattr(old_value, "build_BuildCallSingle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildCallSingle"):
                opp_val = getattr(value, "build_BuildCallSingle", None)
                setattr(value, "build_BuildCallSingle", self)

    @property
    def build_RequiredCapability154(self):
        return self.__build_RequiredCapability154

    @build_RequiredCapability154.setter
    def build_RequiredCapability154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability154", None)
        self.__build_RequiredCapability154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IRequiredCapabilityContainer"):
                opp_val = getattr(old_value, "build_IRequiredCapabilityContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IRequiredCapabilityContainer"):
                opp_val = getattr(value, "build_IRequiredCapabilityContainer", None)
                if opp_val is None:
                    setattr(value, "build_IRequiredCapabilityContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_RequiredCapability269(self):
        return self.__build_RequiredCapability269

    @build_RequiredCapability269.setter
    def build_RequiredCapability269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_RequiredCapability__build_RequiredCapability269", None)
        self.__build_RequiredCapability269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_FragmentHost268"):
                opp_val = getattr(old_value, "build_FragmentHost268", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_FragmentHost268"):
                opp_val = getattr(value, "build_FragmentHost268", None)
                if opp_val is None:
                    setattr(value, "build_FragmentHost268", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IVarName:

    pass
class IProvidedCapabilityContainer:

    pass
class build_BuildConcernContext(IProvidedCapabilityContainer, BConcernContext):

    def __init__(self, defaultPropertiesRemovals: str, build_BuildConcernContext: "build_BPropertySet" = None):
        self.defaultPropertiesRemovals = defaultPropertiesRemovals
        self.build_BuildConcernContext = build_BuildConcernContext
        
    @property
    def defaultPropertiesRemovals(self) -> str:
        return self.__defaultPropertiesRemovals

    @defaultPropertiesRemovals.setter
    def defaultPropertiesRemovals(self, defaultPropertiesRemovals: str):
        self.__defaultPropertiesRemovals = defaultPropertiesRemovals

    @property
    def build_BuildConcernContext(self):
        return self.__build_BuildConcernContext

    @build_BuildConcernContext.setter
    def build_BuildConcernContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildConcernContext__build_BuildConcernContext", None)
        self.__build_BuildConcernContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BPropertySet75"):
                opp_val = getattr(old_value, "build_BPropertySet75", None)
                if opp_val == self:
                    setattr(old_value, "build_BPropertySet75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BPropertySet75"):
                opp_val = getattr(value, "build_BPropertySet75", None)
                setattr(value, "build_BPropertySet75", self)

class build_IBuilder(IProvidedCapabilityContainer, IFunction):

    def __init__(self, unitType: str, build_IBuilder: "build_BuildUnit" = None, build_IBuilder40: "build_UnitParameterDeclaration" = None, build_IBuilder42: "build_PathGroup" = None, build_IBuilder25: "build_BExpression" = None, build_IBuilder27: "build_BExpression" = None, build_IBuilder30: "build_BuilderInput" = None, build_IBuilder32: "build_PathGroup" = None, build_IBuilder34: "build_BPropertySet" = None, build_IBuilder37: "build_BExpression" = None):
        self.unitType = unitType
        self.build_IBuilder = build_IBuilder
        self.build_IBuilder40 = build_IBuilder40
        self.build_IBuilder42 = build_IBuilder42
        self.build_IBuilder25 = build_IBuilder25
        self.build_IBuilder27 = build_IBuilder27
        self.build_IBuilder30 = build_IBuilder30
        self.build_IBuilder32 = build_IBuilder32
        self.build_IBuilder34 = build_IBuilder34
        self.build_IBuilder37 = build_IBuilder37
        
    @property
    def unitType(self) -> str:
        return self.__unitType

    @unitType.setter
    def unitType(self, unitType: str):
        self.__unitType = unitType

    @property
    def build_IBuilder37(self):
        return self.__build_IBuilder37

    @build_IBuilder37.setter
    def build_IBuilder37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder37", None)
        self.__build_IBuilder37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression38"):
                opp_val = getattr(old_value, "build_BExpression38", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression38"):
                opp_val = getattr(value, "build_BExpression38", None)
                setattr(value, "build_BExpression38", self)

    @property
    def build_IBuilder40(self):
        return self.__build_IBuilder40

    @build_IBuilder40.setter
    def build_IBuilder40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder40", None)
        self.__build_IBuilder40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitParameterDeclaration"):
                opp_val = getattr(old_value, "build_UnitParameterDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "build_UnitParameterDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitParameterDeclaration"):
                opp_val = getattr(value, "build_UnitParameterDeclaration", None)
                setattr(value, "build_UnitParameterDeclaration", self)

    @property
    def build_IBuilder30(self):
        return self.__build_IBuilder30

    @build_IBuilder30.setter
    def build_IBuilder30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder30", None)
        self.__build_IBuilder30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuilderInput"):
                opp_val = getattr(old_value, "build_BuilderInput", None)
                if opp_val == self:
                    setattr(old_value, "build_BuilderInput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuilderInput"):
                opp_val = getattr(value, "build_BuilderInput", None)
                setattr(value, "build_BuilderInput", self)

    @property
    def build_IBuilder34(self):
        return self.__build_IBuilder34

    @build_IBuilder34.setter
    def build_IBuilder34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder34", None)
        self.__build_IBuilder34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BPropertySet35"):
                opp_val = getattr(old_value, "build_BPropertySet35", None)
                if opp_val == self:
                    setattr(old_value, "build_BPropertySet35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BPropertySet35"):
                opp_val = getattr(value, "build_BPropertySet35", None)
                setattr(value, "build_BPropertySet35", self)

    @property
    def build_IBuilder25(self):
        return self.__build_IBuilder25

    @build_IBuilder25.setter
    def build_IBuilder25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder25", None)
        self.__build_IBuilder25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression"):
                opp_val = getattr(old_value, "build_BExpression", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression"):
                opp_val = getattr(value, "build_BExpression", None)
                setattr(value, "build_BExpression", self)

    @property
    def build_IBuilder32(self):
        return self.__build_IBuilder32

    @build_IBuilder32.setter
    def build_IBuilder32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder32", None)
        self.__build_IBuilder32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_PathGroup"):
                opp_val = getattr(old_value, "build_PathGroup", None)
                if opp_val == self:
                    setattr(old_value, "build_PathGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_PathGroup"):
                opp_val = getattr(value, "build_PathGroup", None)
                setattr(value, "build_PathGroup", self)

    @property
    def build_IBuilder27(self):
        return self.__build_IBuilder27

    @build_IBuilder27.setter
    def build_IBuilder27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder27", None)
        self.__build_IBuilder27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression28"):
                opp_val = getattr(old_value, "build_BExpression28", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression28"):
                opp_val = getattr(value, "build_BExpression28", None)
                setattr(value, "build_BExpression28", self)

    @property
    def build_IBuilder(self):
        return self.__build_IBuilder

    @build_IBuilder.setter
    def build_IBuilder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder", None)
        self.__build_IBuilder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildUnit"):
                opp_val = getattr(old_value, "build_BuildUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildUnit"):
                opp_val = getattr(value, "build_BuildUnit", None)
                if opp_val is None:
                    setattr(value, "build_BuildUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_IBuilder42(self):
        return self.__build_IBuilder42

    @build_IBuilder42.setter
    def build_IBuilder42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuilder__build_IBuilder42", None)
        self.__build_IBuilder42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_PathGroup43"):
                opp_val = getattr(old_value, "build_PathGroup43", None)
                if opp_val == self:
                    setattr(old_value, "build_PathGroup43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_PathGroup43"):
                opp_val = getattr(value, "build_PathGroup43", None)
                setattr(value, "build_PathGroup43", self)

class IRequiredCapabilityContainer:

    pass
class build_UnitConcernContext(IRequiredCapabilityContainer, BuildConcernContext):

    def __init__(self, sourceLocation: str, outputLocation: str, build_UnitConcernContext104: set["build_CapabilityPredicate"] = None, build_UnitConcernContext: set["build_BuilderConcernContext"] = None, build_UnitConcernContext95: "build_BExpression" = None, build_UnitConcernContext98: set["build_RequiresPredicate"] = None, build_UnitConcernContext101: set["build_ProvidesPredicate"] = None):
        self.sourceLocation = sourceLocation
        self.outputLocation = outputLocation
        self.build_UnitConcernContext104 = build_UnitConcernContext104 if build_UnitConcernContext104 is not None else set()
        self.build_UnitConcernContext = build_UnitConcernContext if build_UnitConcernContext is not None else set()
        self.build_UnitConcernContext95 = build_UnitConcernContext95
        self.build_UnitConcernContext98 = build_UnitConcernContext98 if build_UnitConcernContext98 is not None else set()
        self.build_UnitConcernContext101 = build_UnitConcernContext101 if build_UnitConcernContext101 is not None else set()
        
    @property
    def outputLocation(self) -> str:
        return self.__outputLocation

    @outputLocation.setter
    def outputLocation(self, outputLocation: str):
        self.__outputLocation = outputLocation

    @property
    def sourceLocation(self) -> str:
        return self.__sourceLocation

    @sourceLocation.setter
    def sourceLocation(self, sourceLocation: str):
        self.__sourceLocation = sourceLocation

    @property
    def build_UnitConcernContext104(self):
        return self.__build_UnitConcernContext104

    @build_UnitConcernContext104.setter
    def build_UnitConcernContext104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitConcernContext__build_UnitConcernContext104", None)
        self.__build_UnitConcernContext104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_CapabilityPredicate105"):
                    opp_val = getattr(item, "build_CapabilityPredicate105", None)
                    
                    if opp_val == self:
                        setattr(item, "build_CapabilityPredicate105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_CapabilityPredicate105"):
                    opp_val = getattr(item, "build_CapabilityPredicate105", None)
                    
                    setattr(item, "build_CapabilityPredicate105", self)
                    

    @property
    def build_UnitConcernContext95(self):
        return self.__build_UnitConcernContext95

    @build_UnitConcernContext95.setter
    def build_UnitConcernContext95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitConcernContext__build_UnitConcernContext95", None)
        self.__build_UnitConcernContext95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression96"):
                opp_val = getattr(old_value, "build_BExpression96", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression96"):
                opp_val = getattr(value, "build_BExpression96", None)
                setattr(value, "build_BExpression96", self)

    @property
    def build_UnitConcernContext(self):
        return self.__build_UnitConcernContext

    @build_UnitConcernContext.setter
    def build_UnitConcernContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitConcernContext__build_UnitConcernContext", None)
        self.__build_UnitConcernContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BuilderConcernContext"):
                    opp_val = getattr(item, "build_BuilderConcernContext", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BuilderConcernContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BuilderConcernContext"):
                    opp_val = getattr(item, "build_BuilderConcernContext", None)
                    
                    setattr(item, "build_BuilderConcernContext", self)
                    

    @property
    def build_UnitConcernContext101(self):
        return self.__build_UnitConcernContext101

    @build_UnitConcernContext101.setter
    def build_UnitConcernContext101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitConcernContext__build_UnitConcernContext101", None)
        self.__build_UnitConcernContext101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_ProvidesPredicate102"):
                    opp_val = getattr(item, "build_ProvidesPredicate102", None)
                    
                    if opp_val == self:
                        setattr(item, "build_ProvidesPredicate102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_ProvidesPredicate102"):
                    opp_val = getattr(item, "build_ProvidesPredicate102", None)
                    
                    setattr(item, "build_ProvidesPredicate102", self)
                    

    @property
    def build_UnitConcernContext98(self):
        return self.__build_UnitConcernContext98

    @build_UnitConcernContext98.setter
    def build_UnitConcernContext98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_UnitConcernContext__build_UnitConcernContext98", None)
        self.__build_UnitConcernContext98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_RequiresPredicate99"):
                    opp_val = getattr(item, "build_RequiresPredicate99", None)
                    
                    if opp_val == self:
                        setattr(item, "build_RequiresPredicate99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_RequiresPredicate99"):
                    opp_val = getattr(item, "build_RequiresPredicate99", None)
                    
                    setattr(item, "build_RequiresPredicate99", self)
                    

class BFunctionContainer:

    pass
class VersionedCapability:

    pass
class build_BuildUnit(IProvidedCapabilityContainer, BFunctionContainer, IRequiredCapabilityContainer, VersionedCapability, IVarName):

    def __init__(self, documentation: str, executionMode: str, sourceLocation: str, outputLocation: str, platformFilter: str, build_BuildUnit6: set["build_BConcern"] = None, build_BuildUnit8: "build_BPropertySet" = None, build_BuildUnit10: set["build_Synchronization"] = None, build_BuildUnit12: set["build_Repository"] = None, build_BuildUnit14: set["build_ContainerConfiguration"] = None, build_BuildUnit16: set["build_BPropertySet"] = None, build_BuildUnit: set["build_IBuilder"] = None, build_BuildUnit2: set["build_RequiredCapability"] = None, build_BuildUnit4: set["build_IType"] = None, build_BuildUnit19: set["build_FirstFoundUnitProvider"] = None, build_BuildUnit21: "build_IBuildUnitContainer" = None, build_BuildUnit23: set["build_FragmentHost"] = None, build_BuildUnit191: "build_EffectiveUnitFacade" = None, build_BuildUnit220: "build_UnitResolutionInfo" = None, build_BuildUnit266: "build_IBuildUnitContainer" = None):
        self.documentation = documentation
        self.executionMode = executionMode
        self.sourceLocation = sourceLocation
        self.outputLocation = outputLocation
        self.platformFilter = platformFilter
        self.build_BuildUnit6 = build_BuildUnit6 if build_BuildUnit6 is not None else set()
        self.build_BuildUnit8 = build_BuildUnit8
        self.build_BuildUnit10 = build_BuildUnit10 if build_BuildUnit10 is not None else set()
        self.build_BuildUnit12 = build_BuildUnit12 if build_BuildUnit12 is not None else set()
        self.build_BuildUnit14 = build_BuildUnit14 if build_BuildUnit14 is not None else set()
        self.build_BuildUnit16 = build_BuildUnit16 if build_BuildUnit16 is not None else set()
        self.build_BuildUnit = build_BuildUnit if build_BuildUnit is not None else set()
        self.build_BuildUnit2 = build_BuildUnit2 if build_BuildUnit2 is not None else set()
        self.build_BuildUnit4 = build_BuildUnit4 if build_BuildUnit4 is not None else set()
        self.build_BuildUnit19 = build_BuildUnit19 if build_BuildUnit19 is not None else set()
        self.build_BuildUnit21 = build_BuildUnit21
        self.build_BuildUnit23 = build_BuildUnit23 if build_BuildUnit23 is not None else set()
        self.build_BuildUnit191 = build_BuildUnit191
        self.build_BuildUnit220 = build_BuildUnit220
        self.build_BuildUnit266 = build_BuildUnit266
        
    @property
    def sourceLocation(self) -> str:
        return self.__sourceLocation

    @sourceLocation.setter
    def sourceLocation(self, sourceLocation: str):
        self.__sourceLocation = sourceLocation

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def outputLocation(self) -> str:
        return self.__outputLocation

    @outputLocation.setter
    def outputLocation(self, outputLocation: str):
        self.__outputLocation = outputLocation

    @property
    def executionMode(self) -> str:
        return self.__executionMode

    @executionMode.setter
    def executionMode(self, executionMode: str):
        self.__executionMode = executionMode

    @property
    def platformFilter(self) -> str:
        return self.__platformFilter

    @platformFilter.setter
    def platformFilter(self, platformFilter: str):
        self.__platformFilter = platformFilter

    @property
    def build_BuildUnit8(self):
        return self.__build_BuildUnit8

    @build_BuildUnit8.setter
    def build_BuildUnit8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit8", None)
        self.__build_BuildUnit8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BPropertySet"):
                opp_val = getattr(old_value, "build_BPropertySet", None)
                if opp_val == self:
                    setattr(old_value, "build_BPropertySet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BPropertySet"):
                opp_val = getattr(value, "build_BPropertySet", None)
                setattr(value, "build_BPropertySet", self)

    @property
    def build_BuildUnit(self):
        return self.__build_BuildUnit

    @build_BuildUnit.setter
    def build_BuildUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit", None)
        self.__build_BuildUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IBuilder"):
                    opp_val = getattr(item, "build_IBuilder", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IBuilder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IBuilder"):
                    opp_val = getattr(item, "build_IBuilder", None)
                    
                    setattr(item, "build_IBuilder", self)
                    

    @property
    def build_BuildUnit220(self):
        return self.__build_BuildUnit220

    @build_BuildUnit220.setter
    def build_BuildUnit220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit220", None)
        self.__build_BuildUnit220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitResolutionInfo"):
                opp_val = getattr(old_value, "build_UnitResolutionInfo", None)
                if opp_val == self:
                    setattr(old_value, "build_UnitResolutionInfo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitResolutionInfo"):
                opp_val = getattr(value, "build_UnitResolutionInfo", None)
                setattr(value, "build_UnitResolutionInfo", self)

    @property
    def build_BuildUnit14(self):
        return self.__build_BuildUnit14

    @build_BuildUnit14.setter
    def build_BuildUnit14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit14", None)
        self.__build_BuildUnit14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_ContainerConfiguration"):
                    opp_val = getattr(item, "build_ContainerConfiguration", None)
                    
                    if opp_val == self:
                        setattr(item, "build_ContainerConfiguration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_ContainerConfiguration"):
                    opp_val = getattr(item, "build_ContainerConfiguration", None)
                    
                    setattr(item, "build_ContainerConfiguration", self)
                    

    @property
    def build_BuildUnit21(self):
        return self.__build_BuildUnit21

    @build_BuildUnit21.setter
    def build_BuildUnit21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit21", None)
        self.__build_BuildUnit21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnitContainer"):
                opp_val = getattr(old_value, "build_IBuildUnitContainer", None)
                if opp_val == self:
                    setattr(old_value, "build_IBuildUnitContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnitContainer"):
                opp_val = getattr(value, "build_IBuildUnitContainer", None)
                setattr(value, "build_IBuildUnitContainer", self)

    @property
    def build_BuildUnit23(self):
        return self.__build_BuildUnit23

    @build_BuildUnit23.setter
    def build_BuildUnit23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit23", None)
        self.__build_BuildUnit23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_FragmentHost"):
                    opp_val = getattr(item, "build_FragmentHost", None)
                    
                    if opp_val == self:
                        setattr(item, "build_FragmentHost", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_FragmentHost"):
                    opp_val = getattr(item, "build_FragmentHost", None)
                    
                    setattr(item, "build_FragmentHost", self)
                    

    @property
    def build_BuildUnit16(self):
        return self.__build_BuildUnit16

    @build_BuildUnit16.setter
    def build_BuildUnit16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit16", None)
        self.__build_BuildUnit16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BPropertySet17"):
                    opp_val = getattr(item, "build_BPropertySet17", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BPropertySet17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BPropertySet17"):
                    opp_val = getattr(item, "build_BPropertySet17", None)
                    
                    setattr(item, "build_BPropertySet17", self)
                    

    @property
    def build_BuildUnit19(self):
        return self.__build_BuildUnit19

    @build_BuildUnit19.setter
    def build_BuildUnit19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit19", None)
        self.__build_BuildUnit19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_FirstFoundUnitProvider"):
                    opp_val = getattr(item, "build_FirstFoundUnitProvider", None)
                    
                    if opp_val == self:
                        setattr(item, "build_FirstFoundUnitProvider", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_FirstFoundUnitProvider"):
                    opp_val = getattr(item, "build_FirstFoundUnitProvider", None)
                    
                    setattr(item, "build_FirstFoundUnitProvider", self)
                    

    @property
    def build_BuildUnit191(self):
        return self.__build_BuildUnit191

    @build_BuildUnit191.setter
    def build_BuildUnit191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit191", None)
        self.__build_BuildUnit191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_EffectiveUnitFacade"):
                opp_val = getattr(old_value, "build_EffectiveUnitFacade", None)
                if opp_val == self:
                    setattr(old_value, "build_EffectiveUnitFacade", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_EffectiveUnitFacade"):
                opp_val = getattr(value, "build_EffectiveUnitFacade", None)
                setattr(value, "build_EffectiveUnitFacade", self)

    @property
    def build_BuildUnit12(self):
        return self.__build_BuildUnit12

    @build_BuildUnit12.setter
    def build_BuildUnit12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit12", None)
        self.__build_BuildUnit12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Repository"):
                    opp_val = getattr(item, "build_Repository", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Repository", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Repository"):
                    opp_val = getattr(item, "build_Repository", None)
                    
                    setattr(item, "build_Repository", self)
                    

    @property
    def build_BuildUnit10(self):
        return self.__build_BuildUnit10

    @build_BuildUnit10.setter
    def build_BuildUnit10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit10", None)
        self.__build_BuildUnit10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Synchronization"):
                    opp_val = getattr(item, "build_Synchronization", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Synchronization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Synchronization"):
                    opp_val = getattr(item, "build_Synchronization", None)
                    
                    setattr(item, "build_Synchronization", self)
                    

    @property
    def build_BuildUnit2(self):
        return self.__build_BuildUnit2

    @build_BuildUnit2.setter
    def build_BuildUnit2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit2", None)
        self.__build_BuildUnit2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_RequiredCapability"):
                    opp_val = getattr(item, "build_RequiredCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "build_RequiredCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_RequiredCapability"):
                    opp_val = getattr(item, "build_RequiredCapability", None)
                    
                    setattr(item, "build_RequiredCapability", self)
                    

    @property
    def build_BuildUnit6(self):
        return self.__build_BuildUnit6

    @build_BuildUnit6.setter
    def build_BuildUnit6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit6", None)
        self.__build_BuildUnit6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_BConcern"):
                    opp_val = getattr(item, "build_BConcern", None)
                    
                    if opp_val == self:
                        setattr(item, "build_BConcern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_BConcern"):
                    opp_val = getattr(item, "build_BConcern", None)
                    
                    setattr(item, "build_BConcern", self)
                    

    @property
    def build_BuildUnit266(self):
        return self.__build_BuildUnit266

    @build_BuildUnit266.setter
    def build_BuildUnit266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit266", None)
        self.__build_BuildUnit266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnitContainer265"):
                opp_val = getattr(old_value, "build_IBuildUnitContainer265", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnitContainer265"):
                opp_val = getattr(value, "build_IBuildUnitContainer265", None)
                if opp_val is None:
                    setattr(value, "build_IBuildUnitContainer265", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_BuildUnit4(self):
        return self.__build_BuildUnit4

    @build_BuildUnit4.setter
    def build_BuildUnit4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_BuildUnit__build_BuildUnit4", None)
        self.__build_BuildUnit4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IType"):
                    opp_val = getattr(item, "build_IType", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IType"):
                    opp_val = getattr(item, "build_IType", None)
                    
                    setattr(item, "build_IType", self)
                    

    def getUnitProvider(self) -> str:
        # TODO: Implement getUnitProvider method
        pass

    def getEffectiveFacade(self, ctx: str) -> str:
        # TODO: Implement getEffectiveFacade method
        pass

class build_ContainerConfiguration:

    def __init__(self, documentation: str, name: str, build_ContainerConfiguration: "build_BuildUnit" = None, build_ContainerConfiguration69: "build_IType" = None, build_ContainerConfiguration72: "build_BExpression" = None):
        self.documentation = documentation
        self.name = name
        self.build_ContainerConfiguration = build_ContainerConfiguration
        self.build_ContainerConfiguration69 = build_ContainerConfiguration69
        self.build_ContainerConfiguration72 = build_ContainerConfiguration72
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def build_ContainerConfiguration69(self):
        return self.__build_ContainerConfiguration69

    @build_ContainerConfiguration69.setter
    def build_ContainerConfiguration69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ContainerConfiguration__build_ContainerConfiguration69", None)
        self.__build_ContainerConfiguration69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IType70"):
                opp_val = getattr(old_value, "build_IType70", None)
                if opp_val == self:
                    setattr(old_value, "build_IType70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IType70"):
                opp_val = getattr(value, "build_IType70", None)
                setattr(value, "build_IType70", self)

    @property
    def build_ContainerConfiguration(self):
        return self.__build_ContainerConfiguration

    @build_ContainerConfiguration.setter
    def build_ContainerConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ContainerConfiguration__build_ContainerConfiguration", None)
        self.__build_ContainerConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildUnit14"):
                opp_val = getattr(old_value, "build_BuildUnit14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildUnit14"):
                opp_val = getattr(value, "build_BuildUnit14", None)
                if opp_val is None:
                    setattr(value, "build_BuildUnit14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_ContainerConfiguration72(self):
        return self.__build_ContainerConfiguration72

    @build_ContainerConfiguration72.setter
    def build_ContainerConfiguration72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ContainerConfiguration__build_ContainerConfiguration72", None)
        self.__build_ContainerConfiguration72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression73"):
                opp_val = getattr(old_value, "build_BExpression73", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression73"):
                opp_val = getattr(value, "build_BExpression73", None)
                setattr(value, "build_BExpression73", self)

class build_Repository(BExpression):

    def __init__(self, name: str, documentation: str, handlerType: str, build_Repository: "build_BuildUnit" = None, build_Repository62: "build_RepositoryUnitProvider" = None, build_Repository178: "build_BeeModel" = None, build_Repository225: set["build_Branch"] = None, build_Repository227: set["build_RepoOption"] = None, build_Repository230: "build_IBuildUnitRepository" = None, build_Repository233: "build_BExpression" = None, build_Repository250: "build_UnitRepositoryDescription" = None):
        self.name = name
        self.documentation = documentation
        self.handlerType = handlerType
        self.build_Repository = build_Repository
        self.build_Repository62 = build_Repository62
        self.build_Repository178 = build_Repository178
        self.build_Repository225 = build_Repository225 if build_Repository225 is not None else set()
        self.build_Repository227 = build_Repository227 if build_Repository227 is not None else set()
        self.build_Repository230 = build_Repository230
        self.build_Repository233 = build_Repository233
        self.build_Repository250 = build_Repository250
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def handlerType(self) -> str:
        return self.__handlerType

    @handlerType.setter
    def handlerType(self, handlerType: str):
        self.__handlerType = handlerType

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def build_Repository(self):
        return self.__build_Repository

    @build_Repository.setter
    def build_Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository", None)
        self.__build_Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BuildUnit12"):
                opp_val = getattr(old_value, "build_BuildUnit12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BuildUnit12"):
                opp_val = getattr(value, "build_BuildUnit12", None)
                if opp_val is None:
                    setattr(value, "build_BuildUnit12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Repository178(self):
        return self.__build_Repository178

    @build_Repository178.setter
    def build_Repository178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository178", None)
        self.__build_Repository178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BeeModel177"):
                opp_val = getattr(old_value, "build_BeeModel177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BeeModel177"):
                opp_val = getattr(value, "build_BeeModel177", None)
                if opp_val is None:
                    setattr(value, "build_BeeModel177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_Repository230(self):
        return self.__build_Repository230

    @build_Repository230.setter
    def build_Repository230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository230", None)
        self.__build_Repository230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnitRepository231"):
                opp_val = getattr(old_value, "build_IBuildUnitRepository231", None)
                if opp_val == self:
                    setattr(old_value, "build_IBuildUnitRepository231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnitRepository231"):
                opp_val = getattr(value, "build_IBuildUnitRepository231", None)
                setattr(value, "build_IBuildUnitRepository231", self)

    @property
    def build_Repository250(self):
        return self.__build_Repository250

    @build_Repository250.setter
    def build_Repository250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository250", None)
        self.__build_Repository250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_UnitRepositoryDescription"):
                opp_val = getattr(old_value, "build_UnitRepositoryDescription", None)
                if opp_val == self:
                    setattr(old_value, "build_UnitRepositoryDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_UnitRepositoryDescription"):
                opp_val = getattr(value, "build_UnitRepositoryDescription", None)
                setattr(value, "build_UnitRepositoryDescription", self)

    @property
    def build_Repository62(self):
        return self.__build_Repository62

    @build_Repository62.setter
    def build_Repository62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository62", None)
        self.__build_Repository62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_RepositoryUnitProvider"):
                opp_val = getattr(old_value, "build_RepositoryUnitProvider", None)
                if opp_val == self:
                    setattr(old_value, "build_RepositoryUnitProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_RepositoryUnitProvider"):
                opp_val = getattr(value, "build_RepositoryUnitProvider", None)
                setattr(value, "build_RepositoryUnitProvider", self)

    @property
    def build_Repository227(self):
        return self.__build_Repository227

    @build_Repository227.setter
    def build_Repository227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository227", None)
        self.__build_Repository227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_RepoOption228"):
                    opp_val = getattr(item, "build_RepoOption228", None)
                    
                    if opp_val == self:
                        setattr(item, "build_RepoOption228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_RepoOption228"):
                    opp_val = getattr(item, "build_RepoOption228", None)
                    
                    setattr(item, "build_RepoOption228", self)
                    

    @property
    def build_Repository233(self):
        return self.__build_Repository233

    @build_Repository233.setter
    def build_Repository233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository233", None)
        self.__build_Repository233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_BExpression234"):
                opp_val = getattr(old_value, "build_BExpression234", None)
                if opp_val == self:
                    setattr(old_value, "build_BExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_BExpression234"):
                opp_val = getattr(value, "build_BExpression234", None)
                setattr(value, "build_BExpression234", self)

    @property
    def build_Repository225(self):
        return self.__build_Repository225

    @build_Repository225.setter
    def build_Repository225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_Repository__build_Repository225", None)
        self.__build_Repository225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_Branch"):
                    opp_val = getattr(item, "build_Branch", None)
                    
                    if opp_val == self:
                        setattr(item, "build_Branch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_Branch"):
                    opp_val = getattr(item, "build_Branch", None)
                    
                    setattr(item, "build_Branch", self)
                    

class build_Synchronization:

    pass
class build_BPropertySet:

    pass