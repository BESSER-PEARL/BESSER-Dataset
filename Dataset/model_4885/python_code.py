from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConflictResolution(Enum):
    keep = "keep"
    update = "update"
    replace = "replace"
    fail = "fail"
class FilterAdviceOperation(Enum):
    AND = "AND"
    OR = "OR"
    REPLACE = "REPLACE"
class SplitStyle(Enum):
    unquoted = "unquoted"
    quoted = "quoted"
    groups = "groups"
class Disposition(Enum):
    required = "required"
    desired = "desired"
    unbiassed = "unbiassed"
    undesired = "undesired"
    rejected = "rejected"


############################################
# Definition of Classes
############################################

class SinglePropertyFilter:

    pass
class build_filter_SimplePatternFIlter(SinglePropertyFilter):

    pass
class build_filter_RegexpFilter(SinglePropertyFilter):

    pass
class FilterGroup:

    pass
class build_filter_OrFilter(FilterGroup):

    pass
class build_filter_AndFilter(FilterGroup):

    pass
class build_filter_IFilter(ABC):

    def __init__(self):
        
    def match(self, matched: str, properties: PropertyScope) -> bool:
        # TODO: Implement match method
        pass

class build_command_AdviceGroup:

    pass
class IFilter:

    pass
class build_filter_SinglePropertyFilter(IFilter):

    def __init__(self, property: str, IFilter: "build_command_FilterAdvice", IFilter94: "build_command_FilterAdvice", IFilter98: "build_filter_FilterGroup"):
        self.property = property
        
    @property
    def property(self) -> str:
        return self.__property

    @property.setter
    def property(self, property: str):
        self.__property = property

class build_filter_OSGiBasedFilter(IFilter):

    pass
class build_filter_FilterGroup(IFilter):

    pass
class build_command_ContextNodeSelector(ABC):

    pass
class BuildUnitCommand:

    pass
class build_command_InvokeCommand(BuildUnitCommand):

    def __init__(self, action: str):
        self.action = action
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

class build_command_ImportCommand(BuildUnitCommand):

    pass
class ContextNodeSelector:

    pass
class build_command_IAdvise(ABC):

    pass
class command_build_PropertyScope:

    pass
class build_command_BuildUnitCommand(ABC):

    pass
class ResolutionOptions:

    pass
class build_command_IUnitRequest(ABC):

    def __init__(self, name: str, nameSpace: str, range: str, build_command_IUnitRequest: "ResolutionOptions" = None):
        self.name = name
        self.nameSpace = nameSpace
        self.range = range
        self.build_command_IUnitRequest = build_command_IUnitRequest
        
    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nameSpace(self) -> str:
        return self.__nameSpace

    @nameSpace.setter
    def nameSpace(self, nameSpace: str):
        self.__nameSpace = nameSpace

    @property
    def build_command_IUnitRequest(self):
        return self.__build_command_IUnitRequest

    @build_command_IUnitRequest.setter
    def build_command_IUnitRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_command_IUnitRequest__build_command_IUnitRequest", None)
        self.__build_command_IUnitRequest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResolutionOptions"):
                opp_val = getattr(old_value, "ResolutionOptions", None)
                if opp_val == self:
                    setattr(old_value, "ResolutionOptions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResolutionOptions"):
                opp_val = getattr(value, "ResolutionOptions", None)
                setattr(value, "ResolutionOptions", self)

class build_properties_Match:

    def __init__(self, pattern: str, replacement: str, quotePattern: bool):
        self.pattern = pattern
        self.replacement = replacement
        self.quotePattern = quotePattern
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def replacement(self) -> str:
        return self.__replacement

    @replacement.setter
    def replacement(self, replacement: str):
        self.__replacement = replacement

    @property
    def quotePattern(self) -> bool:
        return self.__quotePattern

    @quotePattern.setter
    def quotePattern(self, quotePattern: bool):
        self.__quotePattern = quotePattern

class Match:

    pass
class AdviceGroup:

    pass
class build_command_NewInstanceAdvice(AdviceGroup):

    def __init__(self, clazz: str):
        self.clazz = clazz
        
    @property
    def clazz(self) -> str:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz

class IFunction:

    pass
class build_properties_Format(IFunction):

    def __init__(self, formatString: str):
        self.formatString = formatString
        
    @property
    def formatString(self) -> str:
        return self.__formatString

    @formatString.setter
    def formatString(self, formatString: str):
        self.__formatString = formatString

class build_properties_Split(IFunction):

    def __init__(self, pattern: str, style: str, limit: int):
        self.pattern = pattern
        self.style = style
        self.limit = limit
        
    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def limit(self) -> int:
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

class build_properties_PropertyRef(IFunction):

    pass
class build_properties_IExpr(ABC):

    def __init__(self):
        
    def eval(self, scope: PropertyScope) -> str:
        # TODO: Implement eval method
        pass

class build_materializer_IMaterializer(ABC):

    pass
class build_resolver_IResolutionContext(ABC):

    pass
class resolver_IEFSBasedAccess:

    pass
class resolver_DefaultResolver:

    pass
class build_resolver_EFSResolver(resolver_DefaultResolver, resolver_IEFSBasedAccess):

    pass
class EFSResolver:

    pass
class build_resolver_WorspaceResolver(EFSResolver):

    pass
class IMetaDataTranslator:

    pass
class build_resolver_IEFSBasedAccess(ABC):

    def __init__(self):
        
    def getFileStore(self) -> str:
        # TODO: Implement getFileStore method
        pass

class build_resolver_IMetaDataTranslator(ABC):

    def __init__(self):
        
    def resolve(self, resolver: str) -> str:
        # TODO: Implement resolve method
        pass

class build_properties_replace(IFunction):

    pass
class build_properties_toLower(IFunction):

    pass
class build_properties_ToUpper(IFunction):

    pass
class ResolverGroup:

    pass
class build_resolver_FirstChoice(ResolverGroup):

    pass
class build_resolver_ILocation(ABC):

    pass
class build_resolver_IResourceMap(ABC):

    def __init__(self):
        
    def lookup(self, request: str) -> str:
        # TODO: Implement lookup method
        pass

class IExpr:

    pass
class build_properties_IFunction(IExpr):

    pass
class build_properties_Literal(IExpr):

    def __init__(self, value: str, IExpr75: "build_properties_IFunction", IExpr: "build_resolver_IResolver"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class build_resolver_IResolver(ABC):

    def __init__(self, failOnError: bool, filter: str, build_resolver_IResolver: "IExpr" = None):
        self.failOnError = failOnError
        self.filter = filter
        self.build_resolver_IResolver = build_resolver_IResolver
        
    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def failOnError(self) -> bool:
        return self.__failOnError

    @failOnError.setter
    def failOnError(self, failOnError: bool):
        self.__failOnError = failOnError

    @property
    def build_resolver_IResolver(self):
        return self.__build_resolver_IResolver

    @build_resolver_IResolver.setter
    def build_resolver_IResolver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_resolver_IResolver__build_resolver_IResolver", None)
        self.__build_resolver_IResolver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IExpr"):
                opp_val = getattr(old_value, "IExpr", None)
                if opp_val == self:
                    setattr(old_value, "IExpr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IExpr"):
                opp_val = getattr(value, "IExpr", None)
                setattr(value, "IExpr", self)

    def resolve(self, IResolutionContext: str) -> str:
        # TODO: Implement resolve method
        pass

class build_runtime_IExtension(ABC):

    pass
class IMetaDataTranslatorFactory:

    pass
class IExtension:

    pass
class build_runtime_MetaDataTranslatorFactoryExtension(IExtension):

    pass
class build_runtime_IHumanSelectable(IExtension):

    def __init__(self, label: str, typeName: str):
        self.label = label
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class runtime_build_IUpToDatePolicy:

    pass
class IHumanSelectable:

    pass
class build_runtime_MaterializerExtension(IHumanSelectable):

    pass
class build_runtime_ResolverExtension(IHumanSelectable):

    pass
class build_runtime_UpToDateExtension(IHumanSelectable):

    pass
class ResolverExtension:

    pass
class MetaDataTranslatorFactoryExtension:

    pass
class MaterializerExtension:

    pass
class UpToDateExtension:

    pass
class build_runtime_BuildRuntime:

    pass
class build_resolver_IMetaDataTranslatorFactory(ABC):

    def __init__(self):
        
    def getTranslator(self, resolver: str, nameSpace: str) -> str:
        # TODO: Implement getTranslator method
        pass

class build_resolver_BestChoice(ResolverGroup):

    pass
class IMaterializer:

    pass
class build_materializer_P2Materializer(IMaterializer):

    pass
class build_materializer_FileSystemMaterializer(IMaterializer):

    pass
class build_materializer_WorkspaceMaterializer(IMaterializer):

    pass
class build_context_ImportOptions(ABC):

    def __init__(self, suffix: str, location: str, conflictResolution: str, resourcePath: str, unpack: bool, expand: bool, build_context_ImportOptions: "IMaterializer" = None):
        self.suffix = suffix
        self.location = location
        self.conflictResolution = conflictResolution
        self.resourcePath = resourcePath
        self.unpack = unpack
        self.expand = expand
        self.build_context_ImportOptions = build_context_ImportOptions
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def expand(self) -> bool:
        return self.__expand

    @expand.setter
    def expand(self, expand: bool):
        self.__expand = expand

    @property
    def unpack(self) -> bool:
        return self.__unpack

    @unpack.setter
    def unpack(self, unpack: bool):
        self.__unpack = unpack

    @property
    def conflictResolution(self) -> str:
        return self.__conflictResolution

    @conflictResolution.setter
    def conflictResolution(self, conflictResolution: str):
        self.__conflictResolution = conflictResolution

    @property
    def suffix(self) -> str:
        return self.__suffix

    @suffix.setter
    def suffix(self, suffix: str):
        self.__suffix = suffix

    @property
    def resourcePath(self) -> str:
        return self.__resourcePath

    @resourcePath.setter
    def resourcePath(self, resourcePath: str):
        self.__resourcePath = resourcePath

    @property
    def build_context_ImportOptions(self):
        return self.__build_context_ImportOptions

    @build_context_ImportOptions.setter
    def build_context_ImportOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_context_ImportOptions__build_context_ImportOptions", None)
        self.__build_context_ImportOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IMaterializer"):
                opp_val = getattr(old_value, "IMaterializer", None)
                if opp_val == self:
                    setattr(old_value, "IMaterializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IMaterializer"):
                opp_val = getattr(value, "IMaterializer", None)
                setattr(value, "IMaterializer", self)

class build_context_ResolutionOptions(ABC):

    def __init__(self, source: str, mutable: str, branchTagPath: str, timestamp: str, revision: str, resolverFilter: str, filterGroups: bool, overlayPath: str, includeParts: str, excludeParts: str, prune: bool):
        self.source = source
        self.mutable = mutable
        self.branchTagPath = branchTagPath
        self.timestamp = timestamp
        self.revision = revision
        self.resolverFilter = resolverFilter
        self.filterGroups = filterGroups
        self.overlayPath = overlayPath
        self.includeParts = includeParts
        self.excludeParts = excludeParts
        self.prune = prune
        
    @property
    def includeParts(self) -> str:
        return self.__includeParts

    @includeParts.setter
    def includeParts(self, includeParts: str):
        self.__includeParts = includeParts

    @property
    def overlayPath(self) -> str:
        return self.__overlayPath

    @overlayPath.setter
    def overlayPath(self, overlayPath: str):
        self.__overlayPath = overlayPath

    @property
    def revision(self) -> str:
        return self.__revision

    @revision.setter
    def revision(self, revision: str):
        self.__revision = revision

    @property
    def excludeParts(self) -> str:
        return self.__excludeParts

    @excludeParts.setter
    def excludeParts(self, excludeParts: str):
        self.__excludeParts = excludeParts

    @property
    def filterGroups(self) -> bool:
        return self.__filterGroups

    @filterGroups.setter
    def filterGroups(self, filterGroups: bool):
        self.__filterGroups = filterGroups

    @property
    def prune(self) -> bool:
        return self.__prune

    @prune.setter
    def prune(self, prune: bool):
        self.__prune = prune

    @property
    def resolverFilter(self) -> str:
        return self.__resolverFilter

    @resolverFilter.setter
    def resolverFilter(self, resolverFilter: str):
        self.__resolverFilter = resolverFilter

    @property
    def mutable(self) -> str:
        return self.__mutable

    @mutable.setter
    def mutable(self, mutable: str):
        self.__mutable = mutable

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def branchTagPath(self) -> str:
        return self.__branchTagPath

    @branchTagPath.setter
    def branchTagPath(self, branchTagPath: str):
        self.__branchTagPath = branchTagPath

class ImportOptions:

    pass
class context_build_ICapability:

    pass
class context_build_IRequiredCapability:

    pass
class build_context_IResolution(ABC):

    pass
class IResolver:

    pass
class build_resolver_P2Resolver(IResolver):

    def __init__(self, IResolver69: "build_runtime_ResolverExtension", IResolver: "build_context_IBuildContext", IResolver84: "build_command_BuildUnitCommand", IResolver72: "build_resolver_ResolverGroup"):
        
    def resolve(self, IResolutionContext: str) -> str:
        # TODO: Implement resolve method
        pass

class build_resolver_ResolverGroup(IResolver):

    pass
class build_resolver_DefaultResolver(IResolver):

    pass
class context_build_IBuildUnit:

    pass
class IResolution:

    pass
class IUnitRequest:

    pass
class build_context_IBuildContext(ABC):

    pass
class build_IGenericUnit(ABC):

    pass
class build_PropertyScope(ABC):

    def __init__(self, unsetProperties: str, build_PropertyScope: "build_StringProperties" = None):
        self.unsetProperties = unsetProperties
        self.build_PropertyScope = build_PropertyScope
        
    @property
    def unsetProperties(self) -> str:
        return self.__unsetProperties

    @unsetProperties.setter
    def unsetProperties(self, unsetProperties: str):
        self.__unsetProperties = unsetProperties

    @property
    def build_PropertyScope(self):
        return self.__build_PropertyScope

    @build_PropertyScope.setter
    def build_PropertyScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_PropertyScope__build_PropertyScope", None)
        self.__build_PropertyScope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_StringProperties"):
                opp_val = getattr(old_value, "build_StringProperties", None)
                if opp_val == self:
                    setattr(old_value, "build_StringProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_StringProperties"):
                opp_val = getattr(value, "build_StringProperties", None)
                setattr(value, "build_StringProperties", self)

class build_StringProperties:

    def __init__(self, key: str, value: str, immutable: bool, build_StringProperties: "build_PropertyScope" = None):
        self.key = key
        self.value = value
        self.immutable = immutable
        self.build_StringProperties = build_StringProperties
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def immutable(self) -> bool:
        return self.__immutable

    @immutable.setter
    def immutable(self, immutable: bool):
        self.__immutable = immutable

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def build_StringProperties(self):
        return self.__build_StringProperties

    @build_StringProperties.setter
    def build_StringProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_StringProperties__build_StringProperties", None)
        self.__build_StringProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_PropertyScope"):
                opp_val = getattr(old_value, "build_PropertyScope", None)
                if opp_val == self:
                    setattr(old_value, "build_PropertyScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_PropertyScope"):
                opp_val = getattr(value, "build_PropertyScope", None)
                setattr(value, "build_PropertyScope", self)

class IClosure:

    pass
class IActionResult:

    pass
class build_ResultingPathGroup(IActionResult):

    pass
class build_IResultingParts(IActionResult):

    pass
class IRequirement:

    pass
class build_Requirement(IRequirement):

    pass
class build_PartRequirement(IRequirement):

    pass
class build_IRequirement(ABC):

    def __init__(self, memberName: str, alias: str, contributor: bool, filter: str, includePattern: str, excludePattern: str, build_IRequirement: "build_IPrerequisites" = None):
        self.memberName = memberName
        self.alias = alias
        self.contributor = contributor
        self.filter = filter
        self.includePattern = includePattern
        self.excludePattern = excludePattern
        self.build_IRequirement = build_IRequirement
        
    @property
    def memberName(self) -> str:
        return self.__memberName

    @memberName.setter
    def memberName(self, memberName: str):
        self.__memberName = memberName

    @property
    def includePattern(self) -> str:
        return self.__includePattern

    @includePattern.setter
    def includePattern(self, includePattern: str):
        self.__includePattern = includePattern

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def excludePattern(self) -> str:
        return self.__excludePattern

    @excludePattern.setter
    def excludePattern(self, excludePattern: str):
        self.__excludePattern = excludePattern

    @property
    def contributor(self) -> bool:
        return self.__contributor

    @contributor.setter
    def contributor(self, contributor: bool):
        self.__contributor = contributor

    @property
    def build_IRequirement(self):
        return self.__build_IRequirement

    @build_IRequirement.setter
    def build_IRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IRequirement__build_IRequirement", None)
        self.__build_IRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IPrerequisites"):
                opp_val = getattr(old_value, "build_IPrerequisites", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IPrerequisites"):
                opp_val = getattr(value, "build_IPrerequisites", None)
                if opp_val is None:
                    setattr(value, "build_IPrerequisites", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IAdvise:

    pass
class build_command_VersionAdvice(IAdvise):

    def __init__(self, version: str, IAdvise87: "build_command_BuildUnitCommand", IAdvise45: "build_context_IBuildContext", IAdvise96: "build_command_AdviceGroup", IAdvise: "build_IClosure"):
        self.version = version
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

class build_command_VersionRangeAdvice(IAdvise):

    def __init__(self, versionRange: str, IAdvise87: "build_command_BuildUnitCommand", IAdvise45: "build_context_IBuildContext", IAdvise96: "build_command_AdviceGroup", IAdvise: "build_IClosure"):
        self.versionRange = versionRange
        
    @property
    def versionRange(self) -> str:
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange

class build_command_PropertyAdvice(IAdvise):

    pass
class build_command_StringAdvice(IAdvise):

    def __init__(self, value: str, IAdvise87: "build_command_BuildUnitCommand", IAdvise45: "build_context_IBuildContext", IAdvise96: "build_command_AdviceGroup", IAdvise: "build_IClosure"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class build_command_BooleanAdvice(IAdvise):

    def __init__(self, value: bool, IAdvise87: "build_command_BuildUnitCommand", IAdvise45: "build_context_IBuildContext", IAdvise96: "build_command_AdviceGroup", IAdvise: "build_IClosure"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class build_command_UnsetAdvice(IAdvise):

    pass
class build_command_FilterAdvice(IAdvise):

    def __init__(self, filterOp: str, build_command_FilterAdvice: "IFilter" = None, build_command_FilterAdvice93: "IFilter" = None, IAdvise87: "build_command_BuildUnitCommand", IAdvise45: "build_context_IBuildContext", IAdvise96: "build_command_AdviceGroup", IAdvise: "build_IClosure"):
        self.filterOp = filterOp
        self.build_command_FilterAdvice = build_command_FilterAdvice
        self.build_command_FilterAdvice93 = build_command_FilterAdvice93
        
    @property
    def filterOp(self) -> str:
        return self.__filterOp

    @filterOp.setter
    def filterOp(self, filterOp: str):
        self.__filterOp = filterOp

    @property
    def build_command_FilterAdvice93(self):
        return self.__build_command_FilterAdvice93

    @build_command_FilterAdvice93.setter
    def build_command_FilterAdvice93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_command_FilterAdvice__build_command_FilterAdvice93", None)
        self.__build_command_FilterAdvice93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IFilter94"):
                opp_val = getattr(old_value, "IFilter94", None)
                if opp_val == self:
                    setattr(old_value, "IFilter94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IFilter94"):
                opp_val = getattr(value, "IFilter94", None)
                setattr(value, "IFilter94", self)

    @property
    def build_command_FilterAdvice(self):
        return self.__build_command_FilterAdvice

    @build_command_FilterAdvice.setter
    def build_command_FilterAdvice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_command_FilterAdvice__build_command_FilterAdvice", None)
        self.__build_command_FilterAdvice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IFilter"):
                opp_val = getattr(old_value, "IFilter", None)
                if opp_val == self:
                    setattr(old_value, "IFilter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IFilter"):
                opp_val = getattr(value, "IFilter", None)
                setattr(value, "IFilter", self)

class IPrerequisites:

    pass
class build_IUpToDatePolicy(ABC):

    pass
class build_IActionResult(ABC):

    pass
class IClosurePart:

    pass
class build_IProducedPart(IClosurePart):

    pass
class build_IPartGroup(IClosurePart):

    pass
class build_IActionPart(IClosurePart):

    pass
class build_IPathGroup(ABC):

    def __init__(self, basePath: str, paths: str, build_IPathGroup: "build_IArtifactsPart" = None, build_IPathGroup25: "build_IProducedPart" = None, build_IPathGroup32: "build_ResultingPathGroup" = None, build_IPathGroup37: "build_IGenericUnit" = None):
        self.basePath = basePath
        self.paths = paths
        self.build_IPathGroup = build_IPathGroup
        self.build_IPathGroup25 = build_IPathGroup25
        self.build_IPathGroup32 = build_IPathGroup32
        self.build_IPathGroup37 = build_IPathGroup37
        
    @property
    def basePath(self) -> str:
        return self.__basePath

    @basePath.setter
    def basePath(self, basePath: str):
        self.__basePath = basePath

    @property
    def paths(self) -> str:
        return self.__paths

    @paths.setter
    def paths(self, paths: str):
        self.__paths = paths

    @property
    def build_IPathGroup37(self):
        return self.__build_IPathGroup37

    @build_IPathGroup37.setter
    def build_IPathGroup37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IPathGroup__build_IPathGroup37", None)
        self.__build_IPathGroup37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IGenericUnit"):
                opp_val = getattr(old_value, "build_IGenericUnit", None)
                if opp_val == self:
                    setattr(old_value, "build_IGenericUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IGenericUnit"):
                opp_val = getattr(value, "build_IGenericUnit", None)
                setattr(value, "build_IGenericUnit", self)

    @property
    def build_IPathGroup(self):
        return self.__build_IPathGroup

    @build_IPathGroup.setter
    def build_IPathGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IPathGroup__build_IPathGroup", None)
        self.__build_IPathGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IArtifactsPart"):
                opp_val = getattr(old_value, "build_IArtifactsPart", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IArtifactsPart"):
                opp_val = getattr(value, "build_IArtifactsPart", None)
                if opp_val is None:
                    setattr(value, "build_IArtifactsPart", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_IPathGroup25(self):
        return self.__build_IPathGroup25

    @build_IPathGroup25.setter
    def build_IPathGroup25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IPathGroup__build_IPathGroup25", None)
        self.__build_IPathGroup25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IProducedPart"):
                opp_val = getattr(old_value, "build_IProducedPart", None)
                if opp_val == self:
                    setattr(old_value, "build_IProducedPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IProducedPart"):
                opp_val = getattr(value, "build_IProducedPart", None)
                setattr(value, "build_IProducedPart", self)

    @property
    def build_IPathGroup32(self):
        return self.__build_IPathGroup32

    @build_IPathGroup32.setter
    def build_IPathGroup32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IPathGroup__build_IPathGroup32", None)
        self.__build_IPathGroup32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_ResultingPathGroup"):
                opp_val = getattr(old_value, "build_ResultingPathGroup", None)
                if opp_val == self:
                    setattr(old_value, "build_ResultingPathGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_ResultingPathGroup"):
                opp_val = getattr(value, "build_ResultingPathGroup", None)
                setattr(value, "build_ResultingPathGroup", self)

class IBuildPart:

    pass
class build_IPrerequisites(IBuildPart):

    def __init__(self, alias: str, rebasePath: str, build_IPrerequisites: set["build_IRequirement"] = None):
        self.alias = alias
        self.rebasePath = rebasePath
        self.build_IPrerequisites = build_IPrerequisites if build_IPrerequisites is not None else set()
        
    @property
    def rebasePath(self) -> str:
        return self.__rebasePath

    @rebasePath.setter
    def rebasePath(self, rebasePath: str):
        self.__rebasePath = rebasePath

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def build_IPrerequisites(self):
        return self.__build_IPrerequisites

    @build_IPrerequisites.setter
    def build_IPrerequisites(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IPrerequisites__build_IPrerequisites", None)
        self.__build_IPrerequisites = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IRequirement"):
                    opp_val = getattr(item, "build_IRequirement", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IRequirement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IRequirement"):
                    opp_val = getattr(item, "build_IRequirement", None)
                    
                    setattr(item, "build_IRequirement", self)
                    

class build_IClosurePart(IBuildPart, IClosure):

    pass
class build_IArtifactsPart(IBuildPart):

    pass
class build_IProvidedCapability(ABC):

    pass
class build_ICapability(ABC):

    def __init__(self, namespace: str, name: str, version: str, build_ICapability: "build_IBuildUnit" = None):
        self.namespace = namespace
        self.name = name
        self.version = version
        self.build_ICapability = build_ICapability
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def build_ICapability(self):
        return self.__build_ICapability

    @build_ICapability.setter
    def build_ICapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_ICapability__build_ICapability", None)
        self.__build_ICapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnit9"):
                opp_val = getattr(old_value, "build_IBuildUnit9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnit9"):
                opp_val = getattr(value, "build_IBuildUnit9", None)
                if opp_val is None:
                    setattr(value, "build_IBuildUnit9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def satisfies(self, required: str) -> bool:
        # TODO: Implement satisfies method
        pass

class build_IRequiredCapability(ABC):

    def __init__(self, namespace: str, name: str, range: str, filter: str, build_IRequiredCapability: "build_IBuildUnit" = None, build_IRequiredCapability4: "build_IBuildUnit" = None, build_IRequiredCapability7: "build_IBuildUnit" = None, build_IRequiredCapability30: "build_Requirement" = None):
        self.namespace = namespace
        self.name = name
        self.range = range
        self.filter = filter
        self.build_IRequiredCapability = build_IRequiredCapability
        self.build_IRequiredCapability4 = build_IRequiredCapability4
        self.build_IRequiredCapability7 = build_IRequiredCapability7
        self.build_IRequiredCapability30 = build_IRequiredCapability30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def build_IRequiredCapability30(self):
        return self.__build_IRequiredCapability30

    @build_IRequiredCapability30.setter
    def build_IRequiredCapability30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IRequiredCapability__build_IRequiredCapability30", None)
        self.__build_IRequiredCapability30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_Requirement"):
                opp_val = getattr(old_value, "build_Requirement", None)
                if opp_val == self:
                    setattr(old_value, "build_Requirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_Requirement"):
                opp_val = getattr(value, "build_Requirement", None)
                setattr(value, "build_Requirement", self)

    @property
    def build_IRequiredCapability7(self):
        return self.__build_IRequiredCapability7

    @build_IRequiredCapability7.setter
    def build_IRequiredCapability7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IRequiredCapability__build_IRequiredCapability7", None)
        self.__build_IRequiredCapability7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnit6"):
                opp_val = getattr(old_value, "build_IBuildUnit6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnit6"):
                opp_val = getattr(value, "build_IBuildUnit6", None)
                if opp_val is None:
                    setattr(value, "build_IBuildUnit6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_IRequiredCapability(self):
        return self.__build_IRequiredCapability

    @build_IRequiredCapability.setter
    def build_IRequiredCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IRequiredCapability__build_IRequiredCapability", None)
        self.__build_IRequiredCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnit"):
                opp_val = getattr(old_value, "build_IBuildUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnit"):
                opp_val = getattr(value, "build_IBuildUnit", None)
                if opp_val is None:
                    setattr(value, "build_IBuildUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def build_IRequiredCapability4(self):
        return self.__build_IRequiredCapability4

    @build_IRequiredCapability4.setter
    def build_IRequiredCapability4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IRequiredCapability__build_IRequiredCapability4", None)
        self.__build_IRequiredCapability4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnit3"):
                opp_val = getattr(old_value, "build_IBuildUnit3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnit3"):
                opp_val = getattr(value, "build_IBuildUnit3", None)
                if opp_val is None:
                    setattr(value, "build_IBuildUnit3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class build_IBuildPart(ABC):

    def __init__(self, name: str, IBuildPart: "build_IBuildUnit" = None, buildPart: set["build_PartCapability"] = None, parts: "build_IBuildUnit" = None, build_IBuildPart: "build_PartRequirement" = None, IBuildPart34: "build_PartCapability" = None):
        self.name = name
        self.IBuildPart = IBuildPart
        self.buildPart = buildPart if buildPart is not None else set()
        self.parts = parts
        self.build_IBuildPart = build_IBuildPart
        self.IBuildPart34 = IBuildPart34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def IBuildPart(self):
        return self.__IBuildPart

    @IBuildPart.setter
    def IBuildPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildPart__IBuildPart", None)
        self.__IBuildPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "buildUnit"):
                opp_val = getattr(old_value, "buildUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "buildUnit"):
                opp_val = getattr(value, "buildUnit", None)
                if opp_val is None:
                    setattr(value, "buildUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parts(self):
        return self.__parts

    @parts.setter
    def parts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildPart__parts", None)
        self.__parts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IBuildUnit"):
                opp_val = getattr(old_value, "IBuildUnit", None)
                if opp_val == self:
                    setattr(old_value, "IBuildUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IBuildUnit"):
                opp_val = getattr(value, "IBuildUnit", None)
                setattr(value, "IBuildUnit", self)

    @property
    def build_IBuildPart(self):
        return self.__build_IBuildPart

    @build_IBuildPart.setter
    def build_IBuildPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildPart__build_IBuildPart", None)
        self.__build_IBuildPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_PartRequirement"):
                opp_val = getattr(old_value, "build_PartRequirement", None)
                if opp_val == self:
                    setattr(old_value, "build_PartRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_PartRequirement"):
                opp_val = getattr(value, "build_PartRequirement", None)
                setattr(value, "build_PartRequirement", self)

    @property
    def buildPart(self):
        return self.__buildPart

    @buildPart.setter
    def buildPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildPart__buildPart", None)
        self.__buildPart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PartCapability"):
                    opp_val = getattr(item, "PartCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "PartCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PartCapability"):
                    opp_val = getattr(item, "PartCapability", None)
                    
                    setattr(item, "PartCapability", self)
                    

    @property
    def IBuildPart34(self):
        return self.__IBuildPart34

    @IBuildPart34.setter
    def IBuildPart34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildPart__IBuildPart34", None)
        self.__IBuildPart34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publishedCapabilities"):
                opp_val = getattr(old_value, "publishedCapabilities", None)
                if opp_val == self:
                    setattr(old_value, "publishedCapabilities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publishedCapabilities"):
                opp_val = getattr(value, "publishedCapabilities", None)
                setattr(value, "publishedCapabilities", self)

class IGenericUnit:

    pass
class PropertyScope:

    pass
class build_IClosure(IPrerequisites, PropertyScope):

    def __init__(self, executeOnce: bool, build_IClosure: set["IAdvise"] = None):
        self.executeOnce = executeOnce
        self.build_IClosure = build_IClosure if build_IClosure is not None else set()
        
    @property
    def executeOnce(self) -> bool:
        return self.__executeOnce

    @executeOnce.setter
    def executeOnce(self, executeOnce: bool):
        self.__executeOnce = executeOnce

    @property
    def build_IClosure(self):
        return self.__build_IClosure

    @build_IClosure.setter
    def build_IClosure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IClosure__build_IClosure", None)
        self.__build_IClosure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IAdvise"):
                    opp_val = getattr(item, "IAdvise", None)
                    
                    if opp_val == self:
                        setattr(item, "IAdvise", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IAdvise"):
                    opp_val = getattr(item, "IAdvise", None)
                    
                    setattr(item, "IAdvise", self)
                    

class ICapability:

    pass
class build_PartCapability(ICapability):

    pass
class build_IBuildUnit(ICapability, PropertyScope, IGenericUnit):

    def __init__(self, filter: str, circularityAllowed: bool, instanceLocation: str, buildUnit: set["build_IBuildPart"] = None, build_IBuildUnit: set["build_IRequiredCapability"] = None, build_IBuildUnit3: set["build_IRequiredCapability"] = None, build_IBuildUnit6: set["build_IRequiredCapability"] = None, build_IBuildUnit9: set["build_ICapability"] = None, build_IBuildUnit12: "build_IBuildUnit" = None, build_IBuildUnit10: "build_IBuildUnit" = None, build_IBuildUnit14: set["build_PartCapability"] = None, IBuildUnit: "build_IBuildPart" = None):
        self.filter = filter
        self.circularityAllowed = circularityAllowed
        self.instanceLocation = instanceLocation
        self.buildUnit = buildUnit if buildUnit is not None else set()
        self.build_IBuildUnit = build_IBuildUnit if build_IBuildUnit is not None else set()
        self.build_IBuildUnit3 = build_IBuildUnit3 if build_IBuildUnit3 is not None else set()
        self.build_IBuildUnit6 = build_IBuildUnit6 if build_IBuildUnit6 is not None else set()
        self.build_IBuildUnit9 = build_IBuildUnit9 if build_IBuildUnit9 is not None else set()
        self.build_IBuildUnit12 = build_IBuildUnit12
        self.build_IBuildUnit10 = build_IBuildUnit10
        self.build_IBuildUnit14 = build_IBuildUnit14 if build_IBuildUnit14 is not None else set()
        self.IBuildUnit = IBuildUnit
        
    @property
    def instanceLocation(self) -> str:
        return self.__instanceLocation

    @instanceLocation.setter
    def instanceLocation(self, instanceLocation: str):
        self.__instanceLocation = instanceLocation

    @property
    def circularityAllowed(self) -> bool:
        return self.__circularityAllowed

    @circularityAllowed.setter
    def circularityAllowed(self, circularityAllowed: bool):
        self.__circularityAllowed = circularityAllowed

    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def build_IBuildUnit9(self):
        return self.__build_IBuildUnit9

    @build_IBuildUnit9.setter
    def build_IBuildUnit9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit9", None)
        self.__build_IBuildUnit9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_ICapability"):
                    opp_val = getattr(item, "build_ICapability", None)
                    
                    if opp_val == self:
                        setattr(item, "build_ICapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_ICapability"):
                    opp_val = getattr(item, "build_ICapability", None)
                    
                    setattr(item, "build_ICapability", self)
                    

    @property
    def build_IBuildUnit14(self):
        return self.__build_IBuildUnit14

    @build_IBuildUnit14.setter
    def build_IBuildUnit14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit14", None)
        self.__build_IBuildUnit14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_PartCapability"):
                    opp_val = getattr(item, "build_PartCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "build_PartCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_PartCapability"):
                    opp_val = getattr(item, "build_PartCapability", None)
                    
                    setattr(item, "build_PartCapability", self)
                    

    @property
    def build_IBuildUnit10(self):
        return self.__build_IBuildUnit10

    @build_IBuildUnit10.setter
    def build_IBuildUnit10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit10", None)
        self.__build_IBuildUnit10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnit12"):
                opp_val = getattr(old_value, "build_IBuildUnit12", None)
                if opp_val == self:
                    setattr(old_value, "build_IBuildUnit12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnit12"):
                opp_val = getattr(value, "build_IBuildUnit12", None)
                setattr(value, "build_IBuildUnit12", self)

    @property
    def build_IBuildUnit12(self):
        return self.__build_IBuildUnit12

    @build_IBuildUnit12.setter
    def build_IBuildUnit12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit12", None)
        self.__build_IBuildUnit12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "build_IBuildUnit10"):
                opp_val = getattr(old_value, "build_IBuildUnit10", None)
                if opp_val == self:
                    setattr(old_value, "build_IBuildUnit10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "build_IBuildUnit10"):
                opp_val = getattr(value, "build_IBuildUnit10", None)
                setattr(value, "build_IBuildUnit10", self)

    @property
    def build_IBuildUnit3(self):
        return self.__build_IBuildUnit3

    @build_IBuildUnit3.setter
    def build_IBuildUnit3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit3", None)
        self.__build_IBuildUnit3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IRequiredCapability4"):
                    opp_val = getattr(item, "build_IRequiredCapability4", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IRequiredCapability4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IRequiredCapability4"):
                    opp_val = getattr(item, "build_IRequiredCapability4", None)
                    
                    setattr(item, "build_IRequiredCapability4", self)
                    

    @property
    def IBuildUnit(self):
        return self.__IBuildUnit

    @IBuildUnit.setter
    def IBuildUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__IBuildUnit", None)
        self.__IBuildUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parts"):
                opp_val = getattr(old_value, "parts", None)
                if opp_val == self:
                    setattr(old_value, "parts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parts"):
                opp_val = getattr(value, "parts", None)
                setattr(value, "parts", self)

    @property
    def buildUnit(self):
        return self.__buildUnit

    @buildUnit.setter
    def buildUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__buildUnit", None)
        self.__buildUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IBuildPart"):
                    opp_val = getattr(item, "IBuildPart", None)
                    
                    if opp_val == self:
                        setattr(item, "IBuildPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IBuildPart"):
                    opp_val = getattr(item, "IBuildPart", None)
                    
                    setattr(item, "IBuildPart", self)
                    

    @property
    def build_IBuildUnit(self):
        return self.__build_IBuildUnit

    @build_IBuildUnit.setter
    def build_IBuildUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit", None)
        self.__build_IBuildUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IRequiredCapability"):
                    opp_val = getattr(item, "build_IRequiredCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IRequiredCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IRequiredCapability"):
                    opp_val = getattr(item, "build_IRequiredCapability", None)
                    
                    setattr(item, "build_IRequiredCapability", self)
                    

    @property
    def build_IBuildUnit6(self):
        return self.__build_IBuildUnit6

    @build_IBuildUnit6.setter
    def build_IBuildUnit6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_build_IBuildUnit__build_IBuildUnit6", None)
        self.__build_IBuildUnit6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "build_IRequiredCapability7"):
                    opp_val = getattr(item, "build_IRequiredCapability7", None)
                    
                    if opp_val == self:
                        setattr(item, "build_IRequiredCapability7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "build_IRequiredCapability7"):
                    opp_val = getattr(item, "build_IRequiredCapability7", None)
                    
                    setattr(item, "build_IRequiredCapability7", self)
                    
