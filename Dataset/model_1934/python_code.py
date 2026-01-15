from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataFormat(Enum):
    CSV = "CSV"
    BAI = "BAI"
    SAI = "SAI"
    VCF_IDX = "VCF_IDX"
    FASTA = "FASTA"
    BWT = "BWT"
    None = "None"
    FASTQ = "FASTQ"
    SAM = "SAM"
    BAM = "BAM"
    VCF = "VCF"
    BCF = "BCF"
    TXT = "TXT"
    DICT = "DICT"
    FAI = "FAI"
    IntervalList = "IntervalList"
class TraversalCriterion(Enum):
    IntervalList = "IntervalList"
    Contig = "Contig"
    Readgroup = "Readgroup"
    Library = "Library"
    Sample = "Sample"
    ReadEnd = "ReadEnd"
    Readpair = "Readpair"
    SplitRead = "SplitRead"
    Locus = "Locus"
    None = "None"
    Read = "Read"
    ReadMappingFlag = "ReadMappingFlag"
class DataCriterion(Enum):
    None = "None"
    Readgroup = "Readgroup"
    Sample = "Sample"
    Library = "Library"


############################################
# Definition of Classes
############################################

class easyflow_Chunk:

    def __init__(self, name: str, tool: str, argument: str, easyflow_Chunk: "easyflow_StringToChunkMap" = None):
        self.name = name
        self.tool = tool
        self.argument = argument
        self.easyflow_Chunk = easyflow_Chunk
        
    @property
    def argument(self) -> str:
        return self.__argument

    @argument.setter
    def argument(self, argument: str):
        self.__argument = argument

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def easyflow_Chunk(self):
        return self.__easyflow_Chunk

    @easyflow_Chunk.setter
    def easyflow_Chunk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Chunk__easyflow_Chunk", None)
        self.__easyflow_Chunk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToChunkMap139"):
                opp_val = getattr(old_value, "easyflow_StringToChunkMap139", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToChunkMap139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToChunkMap139"):
                opp_val = getattr(value, "easyflow_StringToChunkMap139", None)
                setattr(value, "easyflow_StringToChunkMap139", self)

class easyflow_GroupingEvent:

    def __init__(self, dagOut: str, dagIn: str):
        self.dagOut = dagOut
        self.dagIn = dagIn
        
    @property
    def dagOut(self) -> str:
        return self.__dagOut

    @dagOut.setter
    def dagOut(self, dagOut: str):
        self.__dagOut = dagOut

    @property
    def dagIn(self) -> str:
        return self.__dagIn

    @dagIn.setter
    def dagIn(self, dagIn: str):
        self.__dagIn = dagIn

    def applyGroupingCriterion(self, metadata: EasyFlowMetadata) -> str:
        # TODO: Implement applyGroupingCriterion method
        pass

class easyflow_SplittingEvent:

    def __init__(self, traversalCriterion: str, traversalChunks: str, dag: str, processedTask: str, traversalImplDir: str, easyflow_SplittingEvent: "easyflow_Task" = None, easyflow_SplittingEvent124: "easyflow_Task" = None, easyflow_SplittingEvent127: "easyflow_Task" = None):
        self.traversalCriterion = traversalCriterion
        self.traversalChunks = traversalChunks
        self.dag = dag
        self.processedTask = processedTask
        self.traversalImplDir = traversalImplDir
        self.easyflow_SplittingEvent = easyflow_SplittingEvent
        self.easyflow_SplittingEvent124 = easyflow_SplittingEvent124
        self.easyflow_SplittingEvent127 = easyflow_SplittingEvent127
        
    @property
    def processedTask(self) -> str:
        return self.__processedTask

    @processedTask.setter
    def processedTask(self, processedTask: str):
        self.__processedTask = processedTask

    @property
    def traversalCriterion(self) -> str:
        return self.__traversalCriterion

    @traversalCriterion.setter
    def traversalCriterion(self, traversalCriterion: str):
        self.__traversalCriterion = traversalCriterion

    @property
    def traversalImplDir(self) -> str:
        return self.__traversalImplDir

    @traversalImplDir.setter
    def traversalImplDir(self, traversalImplDir: str):
        self.__traversalImplDir = traversalImplDir

    @property
    def dag(self) -> str:
        return self.__dag

    @dag.setter
    def dag(self, dag: str):
        self.__dag = dag

    @property
    def traversalChunks(self) -> str:
        return self.__traversalChunks

    @traversalChunks.setter
    def traversalChunks(self, traversalChunks: str):
        self.__traversalChunks = traversalChunks

    @property
    def easyflow_SplittingEvent(self):
        return self.__easyflow_SplittingEvent

    @easyflow_SplittingEvent.setter
    def easyflow_SplittingEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_SplittingEvent__easyflow_SplittingEvent", None)
        self.__easyflow_SplittingEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task122"):
                opp_val = getattr(old_value, "easyflow_Task122", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Task122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task122"):
                opp_val = getattr(value, "easyflow_Task122", None)
                setattr(value, "easyflow_Task122", self)

    @property
    def easyflow_SplittingEvent124(self):
        return self.__easyflow_SplittingEvent124

    @easyflow_SplittingEvent124.setter
    def easyflow_SplittingEvent124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_SplittingEvent__easyflow_SplittingEvent124", None)
        self.__easyflow_SplittingEvent124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task125"):
                opp_val = getattr(old_value, "easyflow_Task125", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Task125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task125"):
                opp_val = getattr(value, "easyflow_Task125", None)
                setattr(value, "easyflow_Task125", self)

    @property
    def easyflow_SplittingEvent127(self):
        return self.__easyflow_SplittingEvent127

    @easyflow_SplittingEvent127.setter
    def easyflow_SplittingEvent127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_SplittingEvent__easyflow_SplittingEvent127", None)
        self.__easyflow_SplittingEvent127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task128"):
                opp_val = getattr(old_value, "easyflow_Task128", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Task128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task128"):
                opp_val = getattr(value, "easyflow_Task128", None)
                setattr(value, "easyflow_Task128", self)

    def getTraversalImplementation(self, metadata: EasyFlowMetadata) -> ITraversal:
        # TODO: Implement getTraversalImplementation method
        pass

    def applyTraversalCriterion(self, metadata: EasyFlowMetadata):
        # TODO: Implement applyTraversalCriterion method
        pass

    def removePath(self):
        # TODO: Implement removePath method
        pass

    def insertPathToDag(self, chunks: str):
        # TODO: Implement insertPathToDag method
        pass

class Traversal:

    pass
class easyflow_Locus(Traversal):

    def __init__(self):
        
    def readChunks(self):
        # TODO: Implement readChunks method
        pass

class easyflow_ReadEnd(Traversal):

    def __init__(self):
        
    def readChunks(self):
        # TODO: Implement readChunks method
        pass

class easyflow_Contig(Traversal):

    def __init__(self):
        
    def readChunks(self):
        # TODO: Implement readChunks method
        pass

class easyflow_GenericTraversalCriterion(Traversal):

    pass
class easyflow_StringToChunkMap:

    def __init__(self, key: str, easyflow_StringToChunkMap: "easyflow_Traversal" = None, easyflow_StringToChunkMap139: "easyflow_Chunk" = None):
        self.key = key
        self.easyflow_StringToChunkMap = easyflow_StringToChunkMap
        self.easyflow_StringToChunkMap139 = easyflow_StringToChunkMap139
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToChunkMap(self):
        return self.__easyflow_StringToChunkMap

    @easyflow_StringToChunkMap.setter
    def easyflow_StringToChunkMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToChunkMap__easyflow_StringToChunkMap", None)
        self.__easyflow_StringToChunkMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Traversal"):
                opp_val = getattr(old_value, "easyflow_Traversal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Traversal"):
                opp_val = getattr(value, "easyflow_Traversal", None)
                if opp_val is None:
                    setattr(value, "easyflow_Traversal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToChunkMap139(self):
        return self.__easyflow_StringToChunkMap139

    @easyflow_StringToChunkMap139.setter
    def easyflow_StringToChunkMap139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToChunkMap__easyflow_StringToChunkMap139", None)
        self.__easyflow_StringToChunkMap139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Chunk"):
                opp_val = getattr(old_value, "easyflow_Chunk", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Chunk", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Chunk"):
                opp_val = getattr(value, "easyflow_Chunk", None)
                setattr(value, "easyflow_Chunk", self)

class ITraversal:

    pass
class easyflow_Traversal(ITraversal):

    def __init__(self, tarversalCriterion: str, easyflow_Traversal: set["easyflow_StringToChunkMap"] = None):
        self.tarversalCriterion = tarversalCriterion
        self.easyflow_Traversal = easyflow_Traversal if easyflow_Traversal is not None else set()
        
    @property
    def tarversalCriterion(self) -> str:
        return self.__tarversalCriterion

    @tarversalCriterion.setter
    def tarversalCriterion(self, tarversalCriterion: str):
        self.__tarversalCriterion = tarversalCriterion

    @property
    def easyflow_Traversal(self):
        return self.__easyflow_Traversal

    @easyflow_Traversal.setter
    def easyflow_Traversal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Traversal__easyflow_Traversal", None)
        self.__easyflow_Traversal = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToChunkMap"):
                    opp_val = getattr(item, "easyflow_StringToChunkMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToChunkMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToChunkMap"):
                    opp_val = getattr(item, "easyflow_StringToChunkMap", None)
                    
                    setattr(item, "easyflow_StringToChunkMap", self)
                    

class easyflow_ITraversal(ABC):

    def __init__(self, easyflow_ITraversal: "easyflow_Task" = None):
        self.easyflow_ITraversal = easyflow_ITraversal
        
    @property
    def easyflow_ITraversal(self):
        return self.__easyflow_ITraversal

    @easyflow_ITraversal.setter
    def easyflow_ITraversal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_ITraversal__easyflow_ITraversal", None)
        self.__easyflow_ITraversal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task119"):
                opp_val = getattr(old_value, "easyflow_Task119", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Task119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task119"):
                opp_val = getattr(value, "easyflow_Task119", None)
                setattr(value, "easyflow_Task119", self)

    def getChunksAsString(self) -> str:
        # TODO: Implement getChunksAsString method
        pass

    def readChunks(self):
        # TODO: Implement readChunks method
        pass

    def readTemplate(self, fileName: str):
        # TODO: Implement readTemplate method
        pass

    def readChunks(self, fileName: str):
        # TODO: Implement readChunks method
        pass

class easyflow_Job:

    def __init__(self, interpreterOption: str, dependencies: str, targets: str, inputArgs: str, name: str, exe: str, outputArgs: str, genericArgs: str, staticArgs: str, targetPlatform: str, targetPlatformOptions: str, subCmd: str, source: str, easyflow_Job: "easyflow_EasyFlowMetadata" = None):
        self.interpreterOption = interpreterOption
        self.dependencies = dependencies
        self.targets = targets
        self.inputArgs = inputArgs
        self.name = name
        self.exe = exe
        self.outputArgs = outputArgs
        self.genericArgs = genericArgs
        self.staticArgs = staticArgs
        self.targetPlatform = targetPlatform
        self.targetPlatformOptions = targetPlatformOptions
        self.subCmd = subCmd
        self.source = source
        self.easyflow_Job = easyflow_Job
        
    @property
    def staticArgs(self) -> str:
        return self.__staticArgs

    @staticArgs.setter
    def staticArgs(self, staticArgs: str):
        self.__staticArgs = staticArgs

    @property
    def targets(self) -> str:
        return self.__targets

    @targets.setter
    def targets(self, targets: str):
        self.__targets = targets

    @property
    def outputArgs(self) -> str:
        return self.__outputArgs

    @outputArgs.setter
    def outputArgs(self, outputArgs: str):
        self.__outputArgs = outputArgs

    @property
    def genericArgs(self) -> str:
        return self.__genericArgs

    @genericArgs.setter
    def genericArgs(self, genericArgs: str):
        self.__genericArgs = genericArgs

    @property
    def subCmd(self) -> str:
        return self.__subCmd

    @subCmd.setter
    def subCmd(self, subCmd: str):
        self.__subCmd = subCmd

    @property
    def inputArgs(self) -> str:
        return self.__inputArgs

    @inputArgs.setter
    def inputArgs(self, inputArgs: str):
        self.__inputArgs = inputArgs

    @property
    def targetPlatform(self) -> str:
        return self.__targetPlatform

    @targetPlatform.setter
    def targetPlatform(self, targetPlatform: str):
        self.__targetPlatform = targetPlatform

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def targetPlatformOptions(self) -> str:
        return self.__targetPlatformOptions

    @targetPlatformOptions.setter
    def targetPlatformOptions(self, targetPlatformOptions: str):
        self.__targetPlatformOptions = targetPlatformOptions

    @property
    def interpreterOption(self) -> str:
        return self.__interpreterOption

    @interpreterOption.setter
    def interpreterOption(self, interpreterOption: str):
        self.__interpreterOption = interpreterOption

    @property
    def exe(self) -> str:
        return self.__exe

    @exe.setter
    def exe(self, exe: str):
        self.__exe = exe

    @property
    def dependencies(self) -> str:
        return self.__dependencies

    @dependencies.setter
    def dependencies(self, dependencies: str):
        self.__dependencies = dependencies

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def easyflow_Job(self):
        return self.__easyflow_Job

    @easyflow_Job.setter
    def easyflow_Job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Job__easyflow_Job", None)
        self.__easyflow_Job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowMetadata117"):
                opp_val = getattr(old_value, "easyflow_EasyFlowMetadata117", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_EasyFlowMetadata117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowMetadata117"):
                opp_val = getattr(value, "easyflow_EasyFlowMetadata117", None)
                setattr(value, "easyflow_EasyFlowMetadata117", self)

    def writeMakeflowRule(self) -> str:
        # TODO: Implement writeMakeflowRule method
        pass

class EasyFlowMetadata:

    pass
class easyflow_EasyFlowMetadataReader(EasyFlowMetadata):

    def __init__(self, fileName: str):
        self.fileName = fileName
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    def metadataFileReader(self):
        # TODO: Implement metadataFileReader method
        pass

class easyflow_StringToReadgroupMap:

    def __init__(self, key: str, easyflow_StringToReadgroupMap: "easyflow_Group" = None, easyflow_StringToReadgroupMap70: "easyflow_Sample" = None, easyflow_StringToReadgroupMap83: "easyflow_Library" = None, easyflow_StringToReadgroupMap99: "easyflow_Readgroup" = None):
        self.key = key
        self.easyflow_StringToReadgroupMap = easyflow_StringToReadgroupMap
        self.easyflow_StringToReadgroupMap70 = easyflow_StringToReadgroupMap70
        self.easyflow_StringToReadgroupMap83 = easyflow_StringToReadgroupMap83
        self.easyflow_StringToReadgroupMap99 = easyflow_StringToReadgroupMap99
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToReadgroupMap70(self):
        return self.__easyflow_StringToReadgroupMap70

    @easyflow_StringToReadgroupMap70.setter
    def easyflow_StringToReadgroupMap70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToReadgroupMap__easyflow_StringToReadgroupMap70", None)
        self.__easyflow_StringToReadgroupMap70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Sample69"):
                opp_val = getattr(old_value, "easyflow_Sample69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Sample69"):
                opp_val = getattr(value, "easyflow_Sample69", None)
                if opp_val is None:
                    setattr(value, "easyflow_Sample69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToReadgroupMap99(self):
        return self.__easyflow_StringToReadgroupMap99

    @easyflow_StringToReadgroupMap99.setter
    def easyflow_StringToReadgroupMap99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToReadgroupMap__easyflow_StringToReadgroupMap99", None)
        self.__easyflow_StringToReadgroupMap99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Readgroup100"):
                opp_val = getattr(old_value, "easyflow_Readgroup100", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Readgroup100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Readgroup100"):
                opp_val = getattr(value, "easyflow_Readgroup100", None)
                setattr(value, "easyflow_Readgroup100", self)

    @property
    def easyflow_StringToReadgroupMap(self):
        return self.__easyflow_StringToReadgroupMap

    @easyflow_StringToReadgroupMap.setter
    def easyflow_StringToReadgroupMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToReadgroupMap__easyflow_StringToReadgroupMap", None)
        self.__easyflow_StringToReadgroupMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Group58"):
                opp_val = getattr(old_value, "easyflow_Group58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Group58"):
                opp_val = getattr(value, "easyflow_Group58", None)
                if opp_val is None:
                    setattr(value, "easyflow_Group58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToReadgroupMap83(self):
        return self.__easyflow_StringToReadgroupMap83

    @easyflow_StringToReadgroupMap83.setter
    def easyflow_StringToReadgroupMap83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToReadgroupMap__easyflow_StringToReadgroupMap83", None)
        self.__easyflow_StringToReadgroupMap83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Library82"):
                opp_val = getattr(old_value, "easyflow_Library82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Library82"):
                opp_val = getattr(value, "easyflow_Library82", None)
                if opp_val is None:
                    setattr(value, "easyflow_Library82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class easyflow_StringToSampleMap:

    def __init__(self, key: str, easyflow_StringToSampleMap: "easyflow_Group" = None, easyflow_StringToSampleMap72: "easyflow_Readgroup" = None, easyflow_StringToSampleMap77: "easyflow_Library" = None, easyflow_StringToSampleMap96: "easyflow_Sample" = None):
        self.key = key
        self.easyflow_StringToSampleMap = easyflow_StringToSampleMap
        self.easyflow_StringToSampleMap72 = easyflow_StringToSampleMap72
        self.easyflow_StringToSampleMap77 = easyflow_StringToSampleMap77
        self.easyflow_StringToSampleMap96 = easyflow_StringToSampleMap96
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToSampleMap72(self):
        return self.__easyflow_StringToSampleMap72

    @easyflow_StringToSampleMap72.setter
    def easyflow_StringToSampleMap72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToSampleMap__easyflow_StringToSampleMap72", None)
        self.__easyflow_StringToSampleMap72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Readgroup"):
                opp_val = getattr(old_value, "easyflow_Readgroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Readgroup"):
                opp_val = getattr(value, "easyflow_Readgroup", None)
                if opp_val is None:
                    setattr(value, "easyflow_Readgroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToSampleMap(self):
        return self.__easyflow_StringToSampleMap

    @easyflow_StringToSampleMap.setter
    def easyflow_StringToSampleMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToSampleMap__easyflow_StringToSampleMap", None)
        self.__easyflow_StringToSampleMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Group"):
                opp_val = getattr(old_value, "easyflow_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Group"):
                opp_val = getattr(value, "easyflow_Group", None)
                if opp_val is None:
                    setattr(value, "easyflow_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToSampleMap96(self):
        return self.__easyflow_StringToSampleMap96

    @easyflow_StringToSampleMap96.setter
    def easyflow_StringToSampleMap96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToSampleMap__easyflow_StringToSampleMap96", None)
        self.__easyflow_StringToSampleMap96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Sample97"):
                opp_val = getattr(old_value, "easyflow_Sample97", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Sample97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Sample97"):
                opp_val = getattr(value, "easyflow_Sample97", None)
                setattr(value, "easyflow_Sample97", self)

    @property
    def easyflow_StringToSampleMap77(self):
        return self.__easyflow_StringToSampleMap77

    @easyflow_StringToSampleMap77.setter
    def easyflow_StringToSampleMap77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToSampleMap__easyflow_StringToSampleMap77", None)
        self.__easyflow_StringToSampleMap77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Library"):
                opp_val = getattr(old_value, "easyflow_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Library"):
                opp_val = getattr(value, "easyflow_Library", None)
                if opp_val is None:
                    setattr(value, "easyflow_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GroupingCriterion:

    pass
class easyflow_Sample(GroupingCriterion):

    def __init__(self, name: str, easyflow_Sample: set["easyflow_StringToLibraryMap"] = None, easyflow_Sample66: set["easyflow_StringToRecordMap"] = None, easyflow_Sample69: set["easyflow_StringToReadgroupMap"] = None, easyflow_Sample85: "easyflow_Record" = None, easyflow_Sample97: "easyflow_StringToSampleMap" = None):
        self.name = name
        self.easyflow_Sample = easyflow_Sample if easyflow_Sample is not None else set()
        self.easyflow_Sample66 = easyflow_Sample66 if easyflow_Sample66 is not None else set()
        self.easyflow_Sample69 = easyflow_Sample69 if easyflow_Sample69 is not None else set()
        self.easyflow_Sample85 = easyflow_Sample85
        self.easyflow_Sample97 = easyflow_Sample97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def easyflow_Sample85(self):
        return self.__easyflow_Sample85

    @easyflow_Sample85.setter
    def easyflow_Sample85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Sample__easyflow_Sample85", None)
        self.__easyflow_Sample85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Record"):
                opp_val = getattr(old_value, "easyflow_Record", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Record", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Record"):
                opp_val = getattr(value, "easyflow_Record", None)
                setattr(value, "easyflow_Record", self)

    @property
    def easyflow_Sample(self):
        return self.__easyflow_Sample

    @easyflow_Sample.setter
    def easyflow_Sample(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Sample__easyflow_Sample", None)
        self.__easyflow_Sample = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToLibraryMap64"):
                    opp_val = getattr(item, "easyflow_StringToLibraryMap64", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToLibraryMap64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToLibraryMap64"):
                    opp_val = getattr(item, "easyflow_StringToLibraryMap64", None)
                    
                    setattr(item, "easyflow_StringToLibraryMap64", self)
                    

    @property
    def easyflow_Sample97(self):
        return self.__easyflow_Sample97

    @easyflow_Sample97.setter
    def easyflow_Sample97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Sample__easyflow_Sample97", None)
        self.__easyflow_Sample97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToSampleMap96"):
                opp_val = getattr(old_value, "easyflow_StringToSampleMap96", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToSampleMap96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToSampleMap96"):
                opp_val = getattr(value, "easyflow_StringToSampleMap96", None)
                setattr(value, "easyflow_StringToSampleMap96", self)

    @property
    def easyflow_Sample66(self):
        return self.__easyflow_Sample66

    @easyflow_Sample66.setter
    def easyflow_Sample66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Sample__easyflow_Sample66", None)
        self.__easyflow_Sample66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToRecordMap67"):
                    opp_val = getattr(item, "easyflow_StringToRecordMap67", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToRecordMap67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToRecordMap67"):
                    opp_val = getattr(item, "easyflow_StringToRecordMap67", None)
                    
                    setattr(item, "easyflow_StringToRecordMap67", self)
                    

    @property
    def easyflow_Sample69(self):
        return self.__easyflow_Sample69

    @easyflow_Sample69.setter
    def easyflow_Sample69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Sample__easyflow_Sample69", None)
        self.__easyflow_Sample69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToReadgroupMap70"):
                    opp_val = getattr(item, "easyflow_StringToReadgroupMap70", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToReadgroupMap70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToReadgroupMap70"):
                    opp_val = getattr(item, "easyflow_StringToReadgroupMap70", None)
                    
                    setattr(item, "easyflow_StringToReadgroupMap70", self)
                    

class easyflow_Library(GroupingCriterion):

    def __init__(self, name: str, insertSize: int, readLength: int, easyflow_Library91: "easyflow_Record" = None, easyflow_Library: set["easyflow_StringToSampleMap"] = None, easyflow_Library79: set["easyflow_StringToRecordMap"] = None, easyflow_Library82: set["easyflow_StringToReadgroupMap"] = None, easyflow_Library103: "easyflow_StringToLibraryMap" = None):
        self.name = name
        self.insertSize = insertSize
        self.readLength = readLength
        self.easyflow_Library91 = easyflow_Library91
        self.easyflow_Library = easyflow_Library if easyflow_Library is not None else set()
        self.easyflow_Library79 = easyflow_Library79 if easyflow_Library79 is not None else set()
        self.easyflow_Library82 = easyflow_Library82 if easyflow_Library82 is not None else set()
        self.easyflow_Library103 = easyflow_Library103
        
    @property
    def readLength(self) -> int:
        return self.__readLength

    @readLength.setter
    def readLength(self, readLength: int):
        self.__readLength = readLength

    @property
    def insertSize(self) -> int:
        return self.__insertSize

    @insertSize.setter
    def insertSize(self, insertSize: int):
        self.__insertSize = insertSize

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def easyflow_Library91(self):
        return self.__easyflow_Library91

    @easyflow_Library91.setter
    def easyflow_Library91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Library__easyflow_Library91", None)
        self.__easyflow_Library91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Record90"):
                opp_val = getattr(old_value, "easyflow_Record90", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Record90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Record90"):
                opp_val = getattr(value, "easyflow_Record90", None)
                setattr(value, "easyflow_Record90", self)

    @property
    def easyflow_Library82(self):
        return self.__easyflow_Library82

    @easyflow_Library82.setter
    def easyflow_Library82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Library__easyflow_Library82", None)
        self.__easyflow_Library82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToReadgroupMap83"):
                    opp_val = getattr(item, "easyflow_StringToReadgroupMap83", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToReadgroupMap83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToReadgroupMap83"):
                    opp_val = getattr(item, "easyflow_StringToReadgroupMap83", None)
                    
                    setattr(item, "easyflow_StringToReadgroupMap83", self)
                    

    @property
    def easyflow_Library103(self):
        return self.__easyflow_Library103

    @easyflow_Library103.setter
    def easyflow_Library103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Library__easyflow_Library103", None)
        self.__easyflow_Library103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToLibraryMap102"):
                opp_val = getattr(old_value, "easyflow_StringToLibraryMap102", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToLibraryMap102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToLibraryMap102"):
                opp_val = getattr(value, "easyflow_StringToLibraryMap102", None)
                setattr(value, "easyflow_StringToLibraryMap102", self)

    @property
    def easyflow_Library79(self):
        return self.__easyflow_Library79

    @easyflow_Library79.setter
    def easyflow_Library79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Library__easyflow_Library79", None)
        self.__easyflow_Library79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToRecordMap80"):
                    opp_val = getattr(item, "easyflow_StringToRecordMap80", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToRecordMap80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToRecordMap80"):
                    opp_val = getattr(item, "easyflow_StringToRecordMap80", None)
                    
                    setattr(item, "easyflow_StringToRecordMap80", self)
                    

    @property
    def easyflow_Library(self):
        return self.__easyflow_Library

    @easyflow_Library.setter
    def easyflow_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Library__easyflow_Library", None)
        self.__easyflow_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToSampleMap77"):
                    opp_val = getattr(item, "easyflow_StringToSampleMap77", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToSampleMap77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToSampleMap77"):
                    opp_val = getattr(item, "easyflow_StringToSampleMap77", None)
                    
                    setattr(item, "easyflow_StringToSampleMap77", self)
                    

class easyflow_Record(GroupingCriterion):

    def __init__(self, refData: str, fileNames: str, easyflow_Record90: "easyflow_Library" = None, easyflow_Record: "easyflow_Sample" = None, easyflow_Record87: "easyflow_Readgroup" = None, easyflow_Record112: "easyflow_StringToRecordMap" = None):
        self.refData = refData
        self.fileNames = fileNames
        self.easyflow_Record90 = easyflow_Record90
        self.easyflow_Record = easyflow_Record
        self.easyflow_Record87 = easyflow_Record87
        self.easyflow_Record112 = easyflow_Record112
        
    @property
    def fileNames(self) -> str:
        return self.__fileNames

    @fileNames.setter
    def fileNames(self, fileNames: str):
        self.__fileNames = fileNames

    @property
    def refData(self) -> str:
        return self.__refData

    @refData.setter
    def refData(self, refData: str):
        self.__refData = refData

    @property
    def easyflow_Record112(self):
        return self.__easyflow_Record112

    @easyflow_Record112.setter
    def easyflow_Record112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Record__easyflow_Record112", None)
        self.__easyflow_Record112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToRecordMap111"):
                opp_val = getattr(old_value, "easyflow_StringToRecordMap111", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToRecordMap111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToRecordMap111"):
                opp_val = getattr(value, "easyflow_StringToRecordMap111", None)
                setattr(value, "easyflow_StringToRecordMap111", self)

    @property
    def easyflow_Record87(self):
        return self.__easyflow_Record87

    @easyflow_Record87.setter
    def easyflow_Record87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Record__easyflow_Record87", None)
        self.__easyflow_Record87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Readgroup88"):
                opp_val = getattr(old_value, "easyflow_Readgroup88", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Readgroup88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Readgroup88"):
                opp_val = getattr(value, "easyflow_Readgroup88", None)
                setattr(value, "easyflow_Readgroup88", self)

    @property
    def easyflow_Record(self):
        return self.__easyflow_Record

    @easyflow_Record.setter
    def easyflow_Record(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Record__easyflow_Record", None)
        self.__easyflow_Record = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Sample85"):
                opp_val = getattr(old_value, "easyflow_Sample85", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Sample85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Sample85"):
                opp_val = getattr(value, "easyflow_Sample85", None)
                setattr(value, "easyflow_Sample85", self)

    @property
    def easyflow_Record90(self):
        return self.__easyflow_Record90

    @easyflow_Record90.setter
    def easyflow_Record90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Record__easyflow_Record90", None)
        self.__easyflow_Record90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Library91"):
                opp_val = getattr(old_value, "easyflow_Library91", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Library91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Library91"):
                opp_val = getattr(value, "easyflow_Library91", None)
                setattr(value, "easyflow_Library91", self)

class easyflow_Readgroup(GroupingCriterion):

    def __init__(self, name: str, platform: str, platformUnit: str, description: str, easyflow_Readgroup: set["easyflow_StringToSampleMap"] = None, easyflow_Readgroup74: set["easyflow_StringToLibraryMap"] = None, easyflow_Readgroup88: "easyflow_Record" = None, easyflow_Readgroup100: "easyflow_StringToReadgroupMap" = None):
        self.name = name
        self.platform = platform
        self.platformUnit = platformUnit
        self.description = description
        self.easyflow_Readgroup = easyflow_Readgroup if easyflow_Readgroup is not None else set()
        self.easyflow_Readgroup74 = easyflow_Readgroup74 if easyflow_Readgroup74 is not None else set()
        self.easyflow_Readgroup88 = easyflow_Readgroup88
        self.easyflow_Readgroup100 = easyflow_Readgroup100
        
    @property
    def platform(self) -> str:
        return self.__platform

    @platform.setter
    def platform(self, platform: str):
        self.__platform = platform

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def platformUnit(self) -> str:
        return self.__platformUnit

    @platformUnit.setter
    def platformUnit(self, platformUnit: str):
        self.__platformUnit = platformUnit

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def easyflow_Readgroup74(self):
        return self.__easyflow_Readgroup74

    @easyflow_Readgroup74.setter
    def easyflow_Readgroup74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Readgroup__easyflow_Readgroup74", None)
        self.__easyflow_Readgroup74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToLibraryMap75"):
                    opp_val = getattr(item, "easyflow_StringToLibraryMap75", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToLibraryMap75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToLibraryMap75"):
                    opp_val = getattr(item, "easyflow_StringToLibraryMap75", None)
                    
                    setattr(item, "easyflow_StringToLibraryMap75", self)
                    

    @property
    def easyflow_Readgroup100(self):
        return self.__easyflow_Readgroup100

    @easyflow_Readgroup100.setter
    def easyflow_Readgroup100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Readgroup__easyflow_Readgroup100", None)
        self.__easyflow_Readgroup100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToReadgroupMap99"):
                opp_val = getattr(old_value, "easyflow_StringToReadgroupMap99", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToReadgroupMap99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToReadgroupMap99"):
                opp_val = getattr(value, "easyflow_StringToReadgroupMap99", None)
                setattr(value, "easyflow_StringToReadgroupMap99", self)

    @property
    def easyflow_Readgroup88(self):
        return self.__easyflow_Readgroup88

    @easyflow_Readgroup88.setter
    def easyflow_Readgroup88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Readgroup__easyflow_Readgroup88", None)
        self.__easyflow_Readgroup88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Record87"):
                opp_val = getattr(old_value, "easyflow_Record87", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Record87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Record87"):
                opp_val = getattr(value, "easyflow_Record87", None)
                setattr(value, "easyflow_Record87", self)

    @property
    def easyflow_Readgroup(self):
        return self.__easyflow_Readgroup

    @easyflow_Readgroup.setter
    def easyflow_Readgroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Readgroup__easyflow_Readgroup", None)
        self.__easyflow_Readgroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToSampleMap72"):
                    opp_val = getattr(item, "easyflow_StringToSampleMap72", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToSampleMap72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToSampleMap72"):
                    opp_val = getattr(item, "easyflow_StringToSampleMap72", None)
                    
                    setattr(item, "easyflow_StringToSampleMap72", self)
                    

class easyflow_Group(GroupingCriterion):

    def __init__(self, name: str, easyflow_Group60: set["easyflow_StringToLibraryMap"] = None, easyflow_Group62: set["easyflow_StringToRecordMap"] = None, easyflow_Group: set["easyflow_StringToSampleMap"] = None, easyflow_Group58: set["easyflow_StringToReadgroupMap"] = None, easyflow_Group94: "easyflow_StringToGroupMap" = None):
        self.name = name
        self.easyflow_Group60 = easyflow_Group60 if easyflow_Group60 is not None else set()
        self.easyflow_Group62 = easyflow_Group62 if easyflow_Group62 is not None else set()
        self.easyflow_Group = easyflow_Group if easyflow_Group is not None else set()
        self.easyflow_Group58 = easyflow_Group58 if easyflow_Group58 is not None else set()
        self.easyflow_Group94 = easyflow_Group94
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def easyflow_Group60(self):
        return self.__easyflow_Group60

    @easyflow_Group60.setter
    def easyflow_Group60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Group__easyflow_Group60", None)
        self.__easyflow_Group60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToLibraryMap"):
                    opp_val = getattr(item, "easyflow_StringToLibraryMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToLibraryMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToLibraryMap"):
                    opp_val = getattr(item, "easyflow_StringToLibraryMap", None)
                    
                    setattr(item, "easyflow_StringToLibraryMap", self)
                    

    @property
    def easyflow_Group(self):
        return self.__easyflow_Group

    @easyflow_Group.setter
    def easyflow_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Group__easyflow_Group", None)
        self.__easyflow_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToSampleMap"):
                    opp_val = getattr(item, "easyflow_StringToSampleMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToSampleMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToSampleMap"):
                    opp_val = getattr(item, "easyflow_StringToSampleMap", None)
                    
                    setattr(item, "easyflow_StringToSampleMap", self)
                    

    @property
    def easyflow_Group94(self):
        return self.__easyflow_Group94

    @easyflow_Group94.setter
    def easyflow_Group94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Group__easyflow_Group94", None)
        self.__easyflow_Group94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToGroupMap93"):
                opp_val = getattr(old_value, "easyflow_StringToGroupMap93", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToGroupMap93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToGroupMap93"):
                opp_val = getattr(value, "easyflow_StringToGroupMap93", None)
                setattr(value, "easyflow_StringToGroupMap93", self)

    @property
    def easyflow_Group62(self):
        return self.__easyflow_Group62

    @easyflow_Group62.setter
    def easyflow_Group62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Group__easyflow_Group62", None)
        self.__easyflow_Group62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToRecordMap"):
                    opp_val = getattr(item, "easyflow_StringToRecordMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToRecordMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToRecordMap"):
                    opp_val = getattr(item, "easyflow_StringToRecordMap", None)
                    
                    setattr(item, "easyflow_StringToRecordMap", self)
                    

    @property
    def easyflow_Group58(self):
        return self.__easyflow_Group58

    @easyflow_Group58.setter
    def easyflow_Group58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Group__easyflow_Group58", None)
        self.__easyflow_Group58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToReadgroupMap"):
                    opp_val = getattr(item, "easyflow_StringToReadgroupMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToReadgroupMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToReadgroupMap"):
                    opp_val = getattr(item, "easyflow_StringToReadgroupMap", None)
                    
                    setattr(item, "easyflow_StringToReadgroupMap", self)
                    

class easyflow_StringToRecordMap:

    def __init__(self, key: str, easyflow_StringToRecordMap: "easyflow_Group" = None, easyflow_StringToRecordMap67: "easyflow_Sample" = None, easyflow_StringToRecordMap80: "easyflow_Library" = None, easyflow_StringToRecordMap111: "easyflow_Record" = None):
        self.key = key
        self.easyflow_StringToRecordMap = easyflow_StringToRecordMap
        self.easyflow_StringToRecordMap67 = easyflow_StringToRecordMap67
        self.easyflow_StringToRecordMap80 = easyflow_StringToRecordMap80
        self.easyflow_StringToRecordMap111 = easyflow_StringToRecordMap111
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToRecordMap(self):
        return self.__easyflow_StringToRecordMap

    @easyflow_StringToRecordMap.setter
    def easyflow_StringToRecordMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToRecordMap__easyflow_StringToRecordMap", None)
        self.__easyflow_StringToRecordMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Group62"):
                opp_val = getattr(old_value, "easyflow_Group62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Group62"):
                opp_val = getattr(value, "easyflow_Group62", None)
                if opp_val is None:
                    setattr(value, "easyflow_Group62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToRecordMap111(self):
        return self.__easyflow_StringToRecordMap111

    @easyflow_StringToRecordMap111.setter
    def easyflow_StringToRecordMap111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToRecordMap__easyflow_StringToRecordMap111", None)
        self.__easyflow_StringToRecordMap111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Record112"):
                opp_val = getattr(old_value, "easyflow_Record112", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Record112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Record112"):
                opp_val = getattr(value, "easyflow_Record112", None)
                setattr(value, "easyflow_Record112", self)

    @property
    def easyflow_StringToRecordMap67(self):
        return self.__easyflow_StringToRecordMap67

    @easyflow_StringToRecordMap67.setter
    def easyflow_StringToRecordMap67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToRecordMap__easyflow_StringToRecordMap67", None)
        self.__easyflow_StringToRecordMap67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Sample66"):
                opp_val = getattr(old_value, "easyflow_Sample66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Sample66"):
                opp_val = getattr(value, "easyflow_Sample66", None)
                if opp_val is None:
                    setattr(value, "easyflow_Sample66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToRecordMap80(self):
        return self.__easyflow_StringToRecordMap80

    @easyflow_StringToRecordMap80.setter
    def easyflow_StringToRecordMap80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToRecordMap__easyflow_StringToRecordMap80", None)
        self.__easyflow_StringToRecordMap80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Library79"):
                opp_val = getattr(old_value, "easyflow_Library79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Library79"):
                opp_val = getattr(value, "easyflow_Library79", None)
                if opp_val is None:
                    setattr(value, "easyflow_Library79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class easyflow_StringToLibraryMap:

    def __init__(self, key: str, easyflow_StringToLibraryMap: "easyflow_Group" = None, easyflow_StringToLibraryMap75: "easyflow_Readgroup" = None, easyflow_StringToLibraryMap64: "easyflow_Sample" = None, easyflow_StringToLibraryMap102: "easyflow_Library" = None):
        self.key = key
        self.easyflow_StringToLibraryMap = easyflow_StringToLibraryMap
        self.easyflow_StringToLibraryMap75 = easyflow_StringToLibraryMap75
        self.easyflow_StringToLibraryMap64 = easyflow_StringToLibraryMap64
        self.easyflow_StringToLibraryMap102 = easyflow_StringToLibraryMap102
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToLibraryMap64(self):
        return self.__easyflow_StringToLibraryMap64

    @easyflow_StringToLibraryMap64.setter
    def easyflow_StringToLibraryMap64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToLibraryMap__easyflow_StringToLibraryMap64", None)
        self.__easyflow_StringToLibraryMap64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Sample"):
                opp_val = getattr(old_value, "easyflow_Sample", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Sample"):
                opp_val = getattr(value, "easyflow_Sample", None)
                if opp_val is None:
                    setattr(value, "easyflow_Sample", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToLibraryMap(self):
        return self.__easyflow_StringToLibraryMap

    @easyflow_StringToLibraryMap.setter
    def easyflow_StringToLibraryMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToLibraryMap__easyflow_StringToLibraryMap", None)
        self.__easyflow_StringToLibraryMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Group60"):
                opp_val = getattr(old_value, "easyflow_Group60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Group60"):
                opp_val = getattr(value, "easyflow_Group60", None)
                if opp_val is None:
                    setattr(value, "easyflow_Group60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToLibraryMap75(self):
        return self.__easyflow_StringToLibraryMap75

    @easyflow_StringToLibraryMap75.setter
    def easyflow_StringToLibraryMap75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToLibraryMap__easyflow_StringToLibraryMap75", None)
        self.__easyflow_StringToLibraryMap75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Readgroup74"):
                opp_val = getattr(old_value, "easyflow_Readgroup74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Readgroup74"):
                opp_val = getattr(value, "easyflow_Readgroup74", None)
                if opp_val is None:
                    setattr(value, "easyflow_Readgroup74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToLibraryMap102(self):
        return self.__easyflow_StringToLibraryMap102

    @easyflow_StringToLibraryMap102.setter
    def easyflow_StringToLibraryMap102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToLibraryMap__easyflow_StringToLibraryMap102", None)
        self.__easyflow_StringToLibraryMap102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Library103"):
                opp_val = getattr(old_value, "easyflow_Library103", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Library103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Library103"):
                opp_val = getattr(value, "easyflow_Library103", None)
                setattr(value, "easyflow_Library103", self)

class easyflow_Argument:

    def __init__(self, name: str, arg: str, sep: str):
        self.name = name
        self.arg = arg
        self.sep = sep
        
    @property
    def sep(self) -> str:
        return self.__sep

    @sep.setter
    def sep(self, sep: str):
        self.__sep = sep

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arg(self) -> str:
        return self.__arg

    @arg.setter
    def arg(self, arg: str):
        self.__arg = arg

class easyflow_Interpreter:

    def __init__(self, name: str, exe: str, subCmd: str, options: str, easyflow_Interpreter: "easyflow_Tool" = None):
        self.name = name
        self.exe = exe
        self.subCmd = subCmd
        self.options = options
        self.easyflow_Interpreter = easyflow_Interpreter
        
    @property
    def options(self) -> str:
        return self.__options

    @options.setter
    def options(self, options: str):
        self.__options = options

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subCmd(self) -> str:
        return self.__subCmd

    @subCmd.setter
    def subCmd(self, subCmd: str):
        self.__subCmd = subCmd

    @property
    def exe(self) -> str:
        return self.__exe

    @exe.setter
    def exe(self, exe: str):
        self.__exe = exe

    @property
    def easyflow_Interpreter(self):
        return self.__easyflow_Interpreter

    @easyflow_Interpreter.setter
    def easyflow_Interpreter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Interpreter__easyflow_Interpreter", None)
        self.__easyflow_Interpreter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool50"):
                opp_val = getattr(old_value, "easyflow_Tool50", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Tool50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool50"):
                opp_val = getattr(value, "easyflow_Tool50", None)
                setattr(value, "easyflow_Tool50", self)

class easyflow_GroupingCriterion:

    def __init__(self, id: str, easyflow_GroupingCriterion: "easyflow_EasyFlowMetadata" = None, easyflow_GroupingCriterion115: "easyflow_StringToGroupingCriterionMap" = None):
        self.id = id
        self.easyflow_GroupingCriterion = easyflow_GroupingCriterion
        self.easyflow_GroupingCriterion115 = easyflow_GroupingCriterion115
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def easyflow_GroupingCriterion(self):
        return self.__easyflow_GroupingCriterion

    @easyflow_GroupingCriterion.setter
    def easyflow_GroupingCriterion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_GroupingCriterion__easyflow_GroupingCriterion", None)
        self.__easyflow_GroupingCriterion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowMetadata55"):
                opp_val = getattr(old_value, "easyflow_EasyFlowMetadata55", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_EasyFlowMetadata55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowMetadata55"):
                opp_val = getattr(value, "easyflow_EasyFlowMetadata55", None)
                setattr(value, "easyflow_EasyFlowMetadata55", self)

    @property
    def easyflow_GroupingCriterion115(self):
        return self.__easyflow_GroupingCriterion115

    @easyflow_GroupingCriterion115.setter
    def easyflow_GroupingCriterion115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_GroupingCriterion__easyflow_GroupingCriterion115", None)
        self.__easyflow_GroupingCriterion115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToGroupingCriterionMap114"):
                opp_val = getattr(old_value, "easyflow_StringToGroupingCriterionMap114", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToGroupingCriterionMap114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToGroupingCriterionMap114"):
                opp_val = getattr(value, "easyflow_StringToGroupingCriterionMap114", None)
                setattr(value, "easyflow_StringToGroupingCriterionMap114", self)

    def equalsParent(self, map: str) -> bool:
        # TODO: Implement equalsParent method
        pass

    def getLibraryString(self, groupingCriterion: str):
        # TODO: Implement getLibraryString method
        pass

    def getRecordString(self, groupingCriterion: str):
        # TODO: Implement getRecordString method
        pass

    def getMap(self, groupCritMap: str):
        # TODO: Implement getMap method
        pass

    def getUniqueStringForParent(self, parentGroupingCriterion: str):
        # TODO: Implement getUniqueStringForParent method
        pass

    def getKeysForGroupingCriterion(self, group: str, dataCriterion: str):
        # TODO: Implement getKeysForGroupingCriterion method
        pass

    def getSampleString(self, groupingCriterion: str):
        # TODO: Implement getSampleString method
        pass

    def getReadgroupString(self, groupingCriterion: str):
        # TODO: Implement getReadgroupString method
        pass

    def getGroupString(self, groupingCriterion: str):
        # TODO: Implement getGroupString method
        pass

    def getGroupingCriterion(self, key: str, group: str, dataCriterion: str) -> str:
        # TODO: Implement getGroupingCriterion method
        pass

class easyflow_CommandArgument:

    def __init__(self, name: str, arg: str, sep: str, named: bool, required: bool, easyflow_CommandArgument: "easyflow_Tool" = None, easyflow_CommandArgument42: "easyflow_Tool" = None, easyflow_CommandArgument45: "easyflow_Tool" = None, easyflow_CommandArgument48: "easyflow_Tool" = None):
        self.name = name
        self.arg = arg
        self.sep = sep
        self.named = named
        self.required = required
        self.easyflow_CommandArgument = easyflow_CommandArgument
        self.easyflow_CommandArgument42 = easyflow_CommandArgument42
        self.easyflow_CommandArgument45 = easyflow_CommandArgument45
        self.easyflow_CommandArgument48 = easyflow_CommandArgument48
        
    @property
    def sep(self) -> str:
        return self.__sep

    @sep.setter
    def sep(self, sep: str):
        self.__sep = sep

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arg(self) -> str:
        return self.__arg

    @arg.setter
    def arg(self, arg: str):
        self.__arg = arg

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def named(self) -> bool:
        return self.__named

    @named.setter
    def named(self, named: bool):
        self.__named = named

    @property
    def easyflow_CommandArgument45(self):
        return self.__easyflow_CommandArgument45

    @easyflow_CommandArgument45.setter
    def easyflow_CommandArgument45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_CommandArgument__easyflow_CommandArgument45", None)
        self.__easyflow_CommandArgument45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool44"):
                opp_val = getattr(old_value, "easyflow_Tool44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool44"):
                opp_val = getattr(value, "easyflow_Tool44", None)
                if opp_val is None:
                    setattr(value, "easyflow_Tool44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_CommandArgument(self):
        return self.__easyflow_CommandArgument

    @easyflow_CommandArgument.setter
    def easyflow_CommandArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_CommandArgument__easyflow_CommandArgument", None)
        self.__easyflow_CommandArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool"):
                opp_val = getattr(old_value, "easyflow_Tool", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool"):
                opp_val = getattr(value, "easyflow_Tool", None)
                if opp_val is None:
                    setattr(value, "easyflow_Tool", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_CommandArgument48(self):
        return self.__easyflow_CommandArgument48

    @easyflow_CommandArgument48.setter
    def easyflow_CommandArgument48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_CommandArgument__easyflow_CommandArgument48", None)
        self.__easyflow_CommandArgument48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool47"):
                opp_val = getattr(old_value, "easyflow_Tool47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool47"):
                opp_val = getattr(value, "easyflow_Tool47", None)
                if opp_val is None:
                    setattr(value, "easyflow_Tool47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_CommandArgument42(self):
        return self.__easyflow_CommandArgument42

    @easyflow_CommandArgument42.setter
    def easyflow_CommandArgument42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_CommandArgument__easyflow_CommandArgument42", None)
        self.__easyflow_CommandArgument42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool41"):
                opp_val = getattr(old_value, "easyflow_Tool41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool41"):
                opp_val = getattr(value, "easyflow_Tool41", None)
                if opp_val is None:
                    setattr(value, "easyflow_Tool41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def setCmdProperties(self, parameterConfigMap: str):
        # TODO: Implement setCmdProperties method
        pass

    def printStaticArg(self) -> str:
        # TODO: Implement printStaticArg method
        pass

    def printGenericArg(self, generica: str) -> str:
        # TODO: Implement printGenericArg method
        pass

    def printArgument(self, fileName: str) -> str:
        # TODO: Implement printArgument method
        pass

    def setGlobalCmdProperties(self, parameterConfigMap: str):
        # TODO: Implement setGlobalCmdProperties method
        pass

class easyflow_Tool:

    def __init__(self, toolName: str, source: str, subCmd: str, subCmdPrefix: str, type: str, category: str, pattern: str, refData: str, easyflow_Tool: set["easyflow_CommandArgument"] = None, easyflow_Tool41: set["easyflow_CommandArgument"] = None, easyflow_Tool44: set["easyflow_CommandArgument"] = None, easyflow_Tool47: set["easyflow_CommandArgument"] = None, easyflow_Tool50: "easyflow_Interpreter" = None, easyflow_Tool52: "easyflow_Task" = None, easyflow_Tool106: "easyflow_StringToToolMap" = None):
        self.toolName = toolName
        self.source = source
        self.subCmd = subCmd
        self.subCmdPrefix = subCmdPrefix
        self.type = type
        self.category = category
        self.pattern = pattern
        self.refData = refData
        self.easyflow_Tool = easyflow_Tool if easyflow_Tool is not None else set()
        self.easyflow_Tool41 = easyflow_Tool41 if easyflow_Tool41 is not None else set()
        self.easyflow_Tool44 = easyflow_Tool44 if easyflow_Tool44 is not None else set()
        self.easyflow_Tool47 = easyflow_Tool47 if easyflow_Tool47 is not None else set()
        self.easyflow_Tool50 = easyflow_Tool50
        self.easyflow_Tool52 = easyflow_Tool52
        self.easyflow_Tool106 = easyflow_Tool106
        
    @property
    def subCmdPrefix(self) -> str:
        return self.__subCmdPrefix

    @subCmdPrefix.setter
    def subCmdPrefix(self, subCmdPrefix: str):
        self.__subCmdPrefix = subCmdPrefix

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern

    @property
    def toolName(self) -> str:
        return self.__toolName

    @toolName.setter
    def toolName(self, toolName: str):
        self.__toolName = toolName

    @property
    def refData(self) -> str:
        return self.__refData

    @refData.setter
    def refData(self, refData: str):
        self.__refData = refData

    @property
    def subCmd(self) -> str:
        return self.__subCmd

    @subCmd.setter
    def subCmd(self, subCmd: str):
        self.__subCmd = subCmd

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def easyflow_Tool47(self):
        return self.__easyflow_Tool47

    @easyflow_Tool47.setter
    def easyflow_Tool47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool47", None)
        self.__easyflow_Tool47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_CommandArgument48"):
                    opp_val = getattr(item, "easyflow_CommandArgument48", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_CommandArgument48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_CommandArgument48"):
                    opp_val = getattr(item, "easyflow_CommandArgument48", None)
                    
                    setattr(item, "easyflow_CommandArgument48", self)
                    

    @property
    def easyflow_Tool52(self):
        return self.__easyflow_Tool52

    @easyflow_Tool52.setter
    def easyflow_Tool52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool52", None)
        self.__easyflow_Tool52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task53"):
                opp_val = getattr(old_value, "easyflow_Task53", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Task53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task53"):
                opp_val = getattr(value, "easyflow_Task53", None)
                setattr(value, "easyflow_Task53", self)

    @property
    def easyflow_Tool41(self):
        return self.__easyflow_Tool41

    @easyflow_Tool41.setter
    def easyflow_Tool41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool41", None)
        self.__easyflow_Tool41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_CommandArgument42"):
                    opp_val = getattr(item, "easyflow_CommandArgument42", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_CommandArgument42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_CommandArgument42"):
                    opp_val = getattr(item, "easyflow_CommandArgument42", None)
                    
                    setattr(item, "easyflow_CommandArgument42", self)
                    

    @property
    def easyflow_Tool44(self):
        return self.__easyflow_Tool44

    @easyflow_Tool44.setter
    def easyflow_Tool44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool44", None)
        self.__easyflow_Tool44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_CommandArgument45"):
                    opp_val = getattr(item, "easyflow_CommandArgument45", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_CommandArgument45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_CommandArgument45"):
                    opp_val = getattr(item, "easyflow_CommandArgument45", None)
                    
                    setattr(item, "easyflow_CommandArgument45", self)
                    

    @property
    def easyflow_Tool(self):
        return self.__easyflow_Tool

    @easyflow_Tool.setter
    def easyflow_Tool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool", None)
        self.__easyflow_Tool = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_CommandArgument"):
                    opp_val = getattr(item, "easyflow_CommandArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_CommandArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_CommandArgument"):
                    opp_val = getattr(item, "easyflow_CommandArgument", None)
                    
                    setattr(item, "easyflow_CommandArgument", self)
                    

    @property
    def easyflow_Tool106(self):
        return self.__easyflow_Tool106

    @easyflow_Tool106.setter
    def easyflow_Tool106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool106", None)
        self.__easyflow_Tool106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToToolMap105"):
                opp_val = getattr(old_value, "easyflow_StringToToolMap105", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToToolMap105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToToolMap105"):
                opp_val = getattr(value, "easyflow_StringToToolMap105", None)
                setattr(value, "easyflow_StringToToolMap105", self)

    @property
    def easyflow_Tool50(self):
        return self.__easyflow_Tool50

    @easyflow_Tool50.setter
    def easyflow_Tool50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Tool__easyflow_Tool50", None)
        self.__easyflow_Tool50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Interpreter"):
                opp_val = getattr(old_value, "easyflow_Interpreter", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Interpreter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Interpreter"):
                opp_val = getattr(value, "easyflow_Interpreter", None)
                setattr(value, "easyflow_Interpreter", self)

    def applyGlobalOptions(self, globalOptions: str):
        # TODO: Implement applyGlobalOptions method
        pass

    def createJob(self, groupingId: str) -> str:
        # TODO: Implement createJob method
        pass

class easyflow_IWorkflowUtil(ABC):

    def __init__(self):
        
    def getAllTasks(self) -> str:
        # TODO: Implement getAllTasks method
        pass

    def getKeysForGroupingCriterion(self, dataCriterion: str, group: str):
        # TODO: Implement getKeysForGroupingCriterion method
        pass

    def writeDagToDot(self, fileName: str, dag: str):
        # TODO: Implement writeDagToDot method
        pass

    def addTaskListToDAG(self, curTask: str, dag: str, lastTasks: str):
        # TODO: Implement addTaskListToDAG method
        pass

    def getTaskByName(self, tasks: str, taskNames: str):
        # TODO: Implement getTaskByName method
        pass

    def getGroupingCriterion(self, dataCriterion: str, group: str, key: str) -> str:
        # TODO: Implement getGroupingCriterion method
        pass

    def addTaskListToGraph(self, lastTasks: str, graph: str, curTask: str):
        # TODO: Implement addTaskListToGraph method
        pass

    def convertGraphToDag(self, graph: str) -> str:
        # TODO: Implement convertGraphToDag method
        pass

    def convertDagToGraph(self, dag: str, graph: str) -> str:
        # TODO: Implement convertDagToGraph method
        pass

class easyflow_StringToGroupMap:

    def __init__(self, key: str, easyflow_StringToGroupMap: "easyflow_EasyFlowMetadata" = None, easyflow_StringToGroupMap93: "easyflow_Group" = None):
        self.key = key
        self.easyflow_StringToGroupMap = easyflow_StringToGroupMap
        self.easyflow_StringToGroupMap93 = easyflow_StringToGroupMap93
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToGroupMap(self):
        return self.__easyflow_StringToGroupMap

    @easyflow_StringToGroupMap.setter
    def easyflow_StringToGroupMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToGroupMap__easyflow_StringToGroupMap", None)
        self.__easyflow_StringToGroupMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowMetadata32"):
                opp_val = getattr(old_value, "easyflow_EasyFlowMetadata32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowMetadata32"):
                opp_val = getattr(value, "easyflow_EasyFlowMetadata32", None)
                if opp_val is None:
                    setattr(value, "easyflow_EasyFlowMetadata32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToGroupMap93(self):
        return self.__easyflow_StringToGroupMap93

    @easyflow_StringToGroupMap93.setter
    def easyflow_StringToGroupMap93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToGroupMap__easyflow_StringToGroupMap93", None)
        self.__easyflow_StringToGroupMap93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Group94"):
                opp_val = getattr(old_value, "easyflow_Group94", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Group94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Group94"):
                opp_val = getattr(value, "easyflow_Group94", None)
                setattr(value, "easyflow_Group94", self)

class easyflow_StringToTraversalCriterionMap:

    def __init__(self, key: str, value: str, easyflow_StringToTraversalCriterionMap: "easyflow_Task" = None, easyflow_StringToTraversalCriterionMap24: "easyflow_Task" = None):
        self.key = key
        self.value = value
        self.easyflow_StringToTraversalCriterionMap = easyflow_StringToTraversalCriterionMap
        self.easyflow_StringToTraversalCriterionMap24 = easyflow_StringToTraversalCriterionMap24
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def easyflow_StringToTraversalCriterionMap(self):
        return self.__easyflow_StringToTraversalCriterionMap

    @easyflow_StringToTraversalCriterionMap.setter
    def easyflow_StringToTraversalCriterionMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToTraversalCriterionMap__easyflow_StringToTraversalCriterionMap", None)
        self.__easyflow_StringToTraversalCriterionMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task21"):
                opp_val = getattr(old_value, "easyflow_Task21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task21"):
                opp_val = getattr(value, "easyflow_Task21", None)
                if opp_val is None:
                    setattr(value, "easyflow_Task21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToTraversalCriterionMap24(self):
        return self.__easyflow_StringToTraversalCriterionMap24

    @easyflow_StringToTraversalCriterionMap24.setter
    def easyflow_StringToTraversalCriterionMap24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToTraversalCriterionMap__easyflow_StringToTraversalCriterionMap24", None)
        self.__easyflow_StringToTraversalCriterionMap24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task23"):
                opp_val = getattr(old_value, "easyflow_Task23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task23"):
                opp_val = getattr(value, "easyflow_Task23", None)
                if opp_val is None:
                    setattr(value, "easyflow_Task23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class easyflow_StringToGroupingCriterionMap:

    def __init__(self, key: str, easyflow_StringToGroupingCriterionMap: "easyflow_Task" = None, easyflow_StringToGroupingCriterionMap114: "easyflow_GroupingCriterion" = None):
        self.key = key
        self.easyflow_StringToGroupingCriterionMap = easyflow_StringToGroupingCriterionMap
        self.easyflow_StringToGroupingCriterionMap114 = easyflow_StringToGroupingCriterionMap114
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToGroupingCriterionMap(self):
        return self.__easyflow_StringToGroupingCriterionMap

    @easyflow_StringToGroupingCriterionMap.setter
    def easyflow_StringToGroupingCriterionMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToGroupingCriterionMap__easyflow_StringToGroupingCriterionMap", None)
        self.__easyflow_StringToGroupingCriterionMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task19"):
                opp_val = getattr(old_value, "easyflow_Task19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task19"):
                opp_val = getattr(value, "easyflow_Task19", None)
                if opp_val is None:
                    setattr(value, "easyflow_Task19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToGroupingCriterionMap114(self):
        return self.__easyflow_StringToGroupingCriterionMap114

    @easyflow_StringToGroupingCriterionMap114.setter
    def easyflow_StringToGroupingCriterionMap114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToGroupingCriterionMap__easyflow_StringToGroupingCriterionMap114", None)
        self.__easyflow_StringToGroupingCriterionMap114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_GroupingCriterion115"):
                opp_val = getattr(old_value, "easyflow_GroupingCriterion115", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_GroupingCriterion115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_GroupingCriterion115"):
                opp_val = getattr(value, "easyflow_GroupingCriterion115", None)
                setattr(value, "easyflow_GroupingCriterion115", self)

class easyflow_StringToTaskMap:

    def __init__(self, key: str, easyflow_StringToTaskMap: "easyflow_Task" = None, easyflow_StringToTaskMap108: "easyflow_Task" = None):
        self.key = key
        self.easyflow_StringToTaskMap = easyflow_StringToTaskMap
        self.easyflow_StringToTaskMap108 = easyflow_StringToTaskMap108
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToTaskMap(self):
        return self.__easyflow_StringToTaskMap

    @easyflow_StringToTaskMap.setter
    def easyflow_StringToTaskMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToTaskMap__easyflow_StringToTaskMap", None)
        self.__easyflow_StringToTaskMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task17"):
                opp_val = getattr(old_value, "easyflow_Task17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task17"):
                opp_val = getattr(value, "easyflow_Task17", None)
                if opp_val is None:
                    setattr(value, "easyflow_Task17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToTaskMap108(self):
        return self.__easyflow_StringToTaskMap108

    @easyflow_StringToTaskMap108.setter
    def easyflow_StringToTaskMap108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToTaskMap__easyflow_StringToTaskMap108", None)
        self.__easyflow_StringToTaskMap108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task109"):
                opp_val = getattr(old_value, "easyflow_Task109", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Task109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task109"):
                opp_val = getattr(value, "easyflow_Task109", None)
                setattr(value, "easyflow_Task109", self)

class easyflow_StringToToolMap:

    def __init__(self, key: str, easyflow_StringToToolMap: "easyflow_Task" = None, easyflow_StringToToolMap105: "easyflow_Tool" = None):
        self.key = key
        self.easyflow_StringToToolMap = easyflow_StringToToolMap
        self.easyflow_StringToToolMap105 = easyflow_StringToToolMap105
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_StringToToolMap(self):
        return self.__easyflow_StringToToolMap

    @easyflow_StringToToolMap.setter
    def easyflow_StringToToolMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToToolMap__easyflow_StringToToolMap", None)
        self.__easyflow_StringToToolMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Task"):
                opp_val = getattr(old_value, "easyflow_Task", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Task"):
                opp_val = getattr(value, "easyflow_Task", None)
                if opp_val is None:
                    setattr(value, "easyflow_Task", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_StringToToolMap105(self):
        return self.__easyflow_StringToToolMap105

    @easyflow_StringToToolMap105.setter
    def easyflow_StringToToolMap105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_StringToToolMap__easyflow_StringToToolMap105", None)
        self.__easyflow_StringToToolMap105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool106"):
                opp_val = getattr(old_value, "easyflow_Tool106", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Tool106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool106"):
                opp_val = getattr(value, "easyflow_Tool106", None)
                setattr(value, "easyflow_Tool106", self)

class easyflow_DataFormatToTaskList:

    def __init__(self, key: str, easyflow_DataFormatToTaskList: "easyflow_Workflow" = None, easyflow_DataFormatToTaskList136: set["easyflow_Task"] = None):
        self.key = key
        self.easyflow_DataFormatToTaskList = easyflow_DataFormatToTaskList
        self.easyflow_DataFormatToTaskList136 = easyflow_DataFormatToTaskList136 if easyflow_DataFormatToTaskList136 is not None else set()
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def easyflow_DataFormatToTaskList136(self):
        return self.__easyflow_DataFormatToTaskList136

    @easyflow_DataFormatToTaskList136.setter
    def easyflow_DataFormatToTaskList136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_DataFormatToTaskList__easyflow_DataFormatToTaskList136", None)
        self.__easyflow_DataFormatToTaskList136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_Task137"):
                    opp_val = getattr(item, "easyflow_Task137", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_Task137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_Task137"):
                    opp_val = getattr(item, "easyflow_Task137", None)
                    
                    setattr(item, "easyflow_Task137", self)
                    

    @property
    def easyflow_DataFormatToTaskList(self):
        return self.__easyflow_DataFormatToTaskList

    @easyflow_DataFormatToTaskList.setter
    def easyflow_DataFormatToTaskList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_DataFormatToTaskList__easyflow_DataFormatToTaskList", None)
        self.__easyflow_DataFormatToTaskList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow14"):
                opp_val = getattr(old_value, "easyflow_Workflow14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow14"):
                opp_val = getattr(value, "easyflow_Workflow14", None)
                if opp_val is None:
                    setattr(value, "easyflow_Workflow14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class easyflow_TaskToDataProcessingType:

    pass
class easyflow_DataProcessingTypeToTask:

    pass
class easyflow_DataProcessingType:

    def __init__(self, dataFormatIn: str, dataFormatOut: str, easyflow_DataProcessingType: "easyflow_Workflow" = None, easyflow_DataProcessingType35: "easyflow_DataProcessingTypeToTask" = None, easyflow_DataProcessingType131: "easyflow_TaskToDataProcessingType" = None):
        self.dataFormatIn = dataFormatIn
        self.dataFormatOut = dataFormatOut
        self.easyflow_DataProcessingType = easyflow_DataProcessingType
        self.easyflow_DataProcessingType35 = easyflow_DataProcessingType35
        self.easyflow_DataProcessingType131 = easyflow_DataProcessingType131
        
    @property
    def dataFormatOut(self) -> str:
        return self.__dataFormatOut

    @dataFormatOut.setter
    def dataFormatOut(self, dataFormatOut: str):
        self.__dataFormatOut = dataFormatOut

    @property
    def dataFormatIn(self) -> str:
        return self.__dataFormatIn

    @dataFormatIn.setter
    def dataFormatIn(self, dataFormatIn: str):
        self.__dataFormatIn = dataFormatIn

    @property
    def easyflow_DataProcessingType(self):
        return self.__easyflow_DataProcessingType

    @easyflow_DataProcessingType.setter
    def easyflow_DataProcessingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_DataProcessingType__easyflow_DataProcessingType", None)
        self.__easyflow_DataProcessingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow8"):
                opp_val = getattr(old_value, "easyflow_Workflow8", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Workflow8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow8"):
                opp_val = getattr(value, "easyflow_Workflow8", None)
                setattr(value, "easyflow_Workflow8", self)

    @property
    def easyflow_DataProcessingType35(self):
        return self.__easyflow_DataProcessingType35

    @easyflow_DataProcessingType35.setter
    def easyflow_DataProcessingType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_DataProcessingType__easyflow_DataProcessingType35", None)
        self.__easyflow_DataProcessingType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_DataProcessingTypeToTask34"):
                opp_val = getattr(old_value, "easyflow_DataProcessingTypeToTask34", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_DataProcessingTypeToTask34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_DataProcessingTypeToTask34"):
                opp_val = getattr(value, "easyflow_DataProcessingTypeToTask34", None)
                setattr(value, "easyflow_DataProcessingTypeToTask34", self)

    @property
    def easyflow_DataProcessingType131(self):
        return self.__easyflow_DataProcessingType131

    @easyflow_DataProcessingType131.setter
    def easyflow_DataProcessingType131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_DataProcessingType__easyflow_DataProcessingType131", None)
        self.__easyflow_DataProcessingType131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_TaskToDataProcessingType130"):
                opp_val = getattr(old_value, "easyflow_TaskToDataProcessingType130", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_TaskToDataProcessingType130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_TaskToDataProcessingType130"):
                opp_val = getattr(value, "easyflow_TaskToDataProcessingType130", None)
                setattr(value, "easyflow_TaskToDataProcessingType130", self)

    def isConvertableTo(self, dataProcessingTypeOut: str) -> bool:
        # TODO: Implement isConvertableTo method
        pass

class easyflow_EasyFlowImplementationTemplate:

    def __init__(self, fileName: str, parameterConfigFileName: str, parameterConfigMap: str, jsonRootNode: str, globalOptions: str, easyflow_EasyFlowImplementationTemplate: "easyflow_Workflow" = None):
        self.fileName = fileName
        self.parameterConfigFileName = parameterConfigFileName
        self.parameterConfigMap = parameterConfigMap
        self.jsonRootNode = jsonRootNode
        self.globalOptions = globalOptions
        self.easyflow_EasyFlowImplementationTemplate = easyflow_EasyFlowImplementationTemplate
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def globalOptions(self) -> str:
        return self.__globalOptions

    @globalOptions.setter
    def globalOptions(self, globalOptions: str):
        self.__globalOptions = globalOptions

    @property
    def jsonRootNode(self) -> str:
        return self.__jsonRootNode

    @jsonRootNode.setter
    def jsonRootNode(self, jsonRootNode: str):
        self.__jsonRootNode = jsonRootNode

    @property
    def parameterConfigMap(self) -> str:
        return self.__parameterConfigMap

    @parameterConfigMap.setter
    def parameterConfigMap(self, parameterConfigMap: str):
        self.__parameterConfigMap = parameterConfigMap

    @property
    def parameterConfigFileName(self) -> str:
        return self.__parameterConfigFileName

    @parameterConfigFileName.setter
    def parameterConfigFileName(self, parameterConfigFileName: str):
        self.__parameterConfigFileName = parameterConfigFileName

    @property
    def easyflow_EasyFlowImplementationTemplate(self):
        return self.__easyflow_EasyFlowImplementationTemplate

    @easyflow_EasyFlowImplementationTemplate.setter
    def easyflow_EasyFlowImplementationTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowImplementationTemplate__easyflow_EasyFlowImplementationTemplate", None)
        self.__easyflow_EasyFlowImplementationTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow6"):
                opp_val = getattr(old_value, "easyflow_Workflow6", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Workflow6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow6"):
                opp_val = getattr(value, "easyflow_Workflow6", None)
                setattr(value, "easyflow_Workflow6", self)

    def readParameterConfig(self, toolName: str):
        # TODO: Implement readParameterConfig method
        pass

    def initJsonRootNode(self):
        # TODO: Implement initJsonRootNode method
        pass

    def templateFileParser(self, dag: str):
        # TODO: Implement templateFileParser method
        pass

class easyflow_EasyFlowMetadata:

    def __init__(self, name: str, contrast: bool, refData: str, easyflow_EasyFlowMetadata: "easyflow_Workflow" = None, easyflow_EasyFlowMetadata32: set["easyflow_StringToGroupMap"] = None, easyflow_EasyFlowMetadata55: "easyflow_GroupingCriterion" = None, easyflow_EasyFlowMetadata117: "easyflow_Job" = None):
        self.name = name
        self.contrast = contrast
        self.refData = refData
        self.easyflow_EasyFlowMetadata = easyflow_EasyFlowMetadata
        self.easyflow_EasyFlowMetadata32 = easyflow_EasyFlowMetadata32 if easyflow_EasyFlowMetadata32 is not None else set()
        self.easyflow_EasyFlowMetadata55 = easyflow_EasyFlowMetadata55
        self.easyflow_EasyFlowMetadata117 = easyflow_EasyFlowMetadata117
        
    @property
    def contrast(self) -> bool:
        return self.__contrast

    @contrast.setter
    def contrast(self, contrast: bool):
        self.__contrast = contrast

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def refData(self) -> str:
        return self.__refData

    @refData.setter
    def refData(self, refData: str):
        self.__refData = refData

    @property
    def easyflow_EasyFlowMetadata117(self):
        return self.__easyflow_EasyFlowMetadata117

    @easyflow_EasyFlowMetadata117.setter
    def easyflow_EasyFlowMetadata117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowMetadata__easyflow_EasyFlowMetadata117", None)
        self.__easyflow_EasyFlowMetadata117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Job"):
                opp_val = getattr(old_value, "easyflow_Job", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Job", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Job"):
                opp_val = getattr(value, "easyflow_Job", None)
                setattr(value, "easyflow_Job", self)

    @property
    def easyflow_EasyFlowMetadata55(self):
        return self.__easyflow_EasyFlowMetadata55

    @easyflow_EasyFlowMetadata55.setter
    def easyflow_EasyFlowMetadata55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowMetadata__easyflow_EasyFlowMetadata55", None)
        self.__easyflow_EasyFlowMetadata55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_GroupingCriterion"):
                opp_val = getattr(old_value, "easyflow_GroupingCriterion", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_GroupingCriterion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_GroupingCriterion"):
                opp_val = getattr(value, "easyflow_GroupingCriterion", None)
                setattr(value, "easyflow_GroupingCriterion", self)

    @property
    def easyflow_EasyFlowMetadata32(self):
        return self.__easyflow_EasyFlowMetadata32

    @easyflow_EasyFlowMetadata32.setter
    def easyflow_EasyFlowMetadata32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowMetadata__easyflow_EasyFlowMetadata32", None)
        self.__easyflow_EasyFlowMetadata32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToGroupMap"):
                    opp_val = getattr(item, "easyflow_StringToGroupMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToGroupMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToGroupMap"):
                    opp_val = getattr(item, "easyflow_StringToGroupMap", None)
                    
                    setattr(item, "easyflow_StringToGroupMap", self)
                    

    @property
    def easyflow_EasyFlowMetadata(self):
        return self.__easyflow_EasyFlowMetadata

    @easyflow_EasyFlowMetadata.setter
    def easyflow_EasyFlowMetadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowMetadata__easyflow_EasyFlowMetadata", None)
        self.__easyflow_EasyFlowMetadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow4"):
                opp_val = getattr(old_value, "easyflow_Workflow4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow4"):
                opp_val = getattr(value, "easyflow_Workflow4", None)
                if opp_val is None:
                    setattr(value, "easyflow_Workflow4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class easyflow_EasyFlowConfiguration:

    def __init__(self, fileName: str, configMap: str, easyflow_EasyFlowConfiguration: "easyflow_Workflow" = None):
        self.fileName = fileName
        self.configMap = configMap
        self.easyflow_EasyFlowConfiguration = easyflow_EasyFlowConfiguration
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def configMap(self) -> str:
        return self.__configMap

    @configMap.setter
    def configMap(self, configMap: str):
        self.__configMap = configMap

    @property
    def easyflow_EasyFlowConfiguration(self):
        return self.__easyflow_EasyFlowConfiguration

    @easyflow_EasyFlowConfiguration.setter
    def easyflow_EasyFlowConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowConfiguration__easyflow_EasyFlowConfiguration", None)
        self.__easyflow_EasyFlowConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow2"):
                opp_val = getattr(old_value, "easyflow_Workflow2", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Workflow2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow2"):
                opp_val = getattr(value, "easyflow_Workflow2", None)
                setattr(value, "easyflow_Workflow2", self)

    def configFileReader(self):
        # TODO: Implement configFileReader method
        pass

class easyflow_EasyFlowTemplate:

    def __init__(self, fileName: str, easyflow_EasyFlowTemplate: "easyflow_Workflow" = None, easyflow_EasyFlowTemplate29: "easyflow_Workflow" = None):
        self.fileName = fileName
        self.easyflow_EasyFlowTemplate = easyflow_EasyFlowTemplate
        self.easyflow_EasyFlowTemplate29 = easyflow_EasyFlowTemplate29
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def easyflow_EasyFlowTemplate29(self):
        return self.__easyflow_EasyFlowTemplate29

    @easyflow_EasyFlowTemplate29.setter
    def easyflow_EasyFlowTemplate29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowTemplate__easyflow_EasyFlowTemplate29", None)
        self.__easyflow_EasyFlowTemplate29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow30"):
                opp_val = getattr(old_value, "easyflow_Workflow30", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Workflow30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow30"):
                opp_val = getattr(value, "easyflow_Workflow30", None)
                setattr(value, "easyflow_Workflow30", self)

    @property
    def easyflow_EasyFlowTemplate(self):
        return self.__easyflow_EasyFlowTemplate

    @easyflow_EasyFlowTemplate.setter
    def easyflow_EasyFlowTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_EasyFlowTemplate__easyflow_EasyFlowTemplate", None)
        self.__easyflow_EasyFlowTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Workflow"):
                opp_val = getattr(old_value, "easyflow_Workflow", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Workflow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Workflow"):
                opp_val = getattr(value, "easyflow_Workflow", None)
                setattr(value, "easyflow_Workflow", self)

    def generateDAGFromTemplateFile(self) -> str:
        # TODO: Implement generateDAGFromTemplateFile method
        pass

    def generateGraphFromTemplateFile(self) -> str:
        # TODO: Implement generateGraphFromTemplateFile method
        pass

class easyflow_Task:

    def __init__(self, name: str, dataFormatIn: str, dataFormatOut: str, splitCriterion: str, contrast: bool, cardinalityIn: str, static: bool, util: bool, jexlString: str, cardinalityOut: str, dataCriterion: str, isMultipleInstancesOfDataCriterion: str, mergeCriterion: str, traversalCriterion: str, skipGroupingCriterion: str, depricated: bool, easyflow_Task: set["easyflow_StringToToolMap"] = None, easyflow_Task17: set["easyflow_StringToTaskMap"] = None, easyflow_Task19: set["easyflow_StringToGroupingCriterionMap"] = None, easyflow_Task26: "easyflow_TaskToDataProcessingType" = None, easyflow_Task21: set["easyflow_StringToTraversalCriterionMap"] = None, easyflow_Task23: set["easyflow_StringToTraversalCriterionMap"] = None, easyflow_Task38: "easyflow_DataProcessingTypeToTask" = None, easyflow_Task53: "easyflow_Tool" = None, easyflow_Task109: "easyflow_StringToTaskMap" = None, easyflow_Task119: "easyflow_ITraversal" = None, easyflow_Task122: "easyflow_SplittingEvent" = None, easyflow_Task125: "easyflow_SplittingEvent" = None, easyflow_Task128: "easyflow_SplittingEvent" = None, easyflow_Task134: "easyflow_TaskToDataProcessingType" = None, easyflow_Task137: "easyflow_DataFormatToTaskList" = None):
        self.name = name
        self.dataFormatIn = dataFormatIn
        self.dataFormatOut = dataFormatOut
        self.splitCriterion = splitCriterion
        self.contrast = contrast
        self.static = static
        self.cardinalityIn = cardinalityIn
        self.util = util
        self.jexlString = jexlString
        self.cardinalityOut = cardinalityOut
        self.dataCriterion = dataCriterion
        self.isMultipleInstancesOfDataCriterion = isMultipleInstancesOfDataCriterion
        self.mergeCriterion = mergeCriterion
        self.traversalCriterion = traversalCriterion
        self.skipGroupingCriterion = skipGroupingCriterion
        self.depricated = depricated
        self.easyflow_Task = easyflow_Task if easyflow_Task is not None else set()
        self.easyflow_Task17 = easyflow_Task17 if easyflow_Task17 is not None else set()
        self.easyflow_Task19 = easyflow_Task19 if easyflow_Task19 is not None else set()
        self.easyflow_Task26 = easyflow_Task26
        self.easyflow_Task21 = easyflow_Task21 if easyflow_Task21 is not None else set()
        self.easyflow_Task23 = easyflow_Task23 if easyflow_Task23 is not None else set()
        self.easyflow_Task38 = easyflow_Task38
        self.easyflow_Task53 = easyflow_Task53
        self.easyflow_Task109 = easyflow_Task109
        self.easyflow_Task119 = easyflow_Task119
        self.easyflow_Task122 = easyflow_Task122
        self.easyflow_Task125 = easyflow_Task125
        self.easyflow_Task128 = easyflow_Task128
        self.easyflow_Task134 = easyflow_Task134
        self.easyflow_Task137 = easyflow_Task137
        
    @property
    def splitCriterion(self) -> str:
        return self.__splitCriterion

    @splitCriterion.setter
    def splitCriterion(self, splitCriterion: str):
        self.__splitCriterion = splitCriterion

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataFormatOut(self) -> str:
        return self.__dataFormatOut

    @dataFormatOut.setter
    def dataFormatOut(self, dataFormatOut: str):
        self.__dataFormatOut = dataFormatOut

    @property
    def util(self) -> bool:
        return self.__util

    @util.setter
    def util(self, util: bool):
        self.__util = util

    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def cardinalityOut(self) -> str:
        return self.__cardinalityOut

    @cardinalityOut.setter
    def cardinalityOut(self, cardinalityOut: str):
        self.__cardinalityOut = cardinalityOut

    @property
    def dataCriterion(self) -> str:
        return self.__dataCriterion

    @dataCriterion.setter
    def dataCriterion(self, dataCriterion: str):
        self.__dataCriterion = dataCriterion

    @property
    def isMultipleInstancesOfDataCriterion(self) -> str:
        return self.__isMultipleInstancesOfDataCriterion

    @isMultipleInstancesOfDataCriterion.setter
    def isMultipleInstancesOfDataCriterion(self, isMultipleInstancesOfDataCriterion: str):
        self.__isMultipleInstancesOfDataCriterion = isMultipleInstancesOfDataCriterion

    @property
    def jexlString(self) -> str:
        return self.__jexlString

    @jexlString.setter
    def jexlString(self, jexlString: str):
        self.__jexlString = jexlString

    @property
    def contrast(self) -> bool:
        return self.__contrast

    @contrast.setter
    def contrast(self, contrast: bool):
        self.__contrast = contrast

    @property
    def mergeCriterion(self) -> str:
        return self.__mergeCriterion

    @mergeCriterion.setter
    def mergeCriterion(self, mergeCriterion: str):
        self.__mergeCriterion = mergeCriterion

    @property
    def depricated(self) -> bool:
        return self.__depricated

    @depricated.setter
    def depricated(self, depricated: bool):
        self.__depricated = depricated

    @property
    def skipGroupingCriterion(self) -> str:
        return self.__skipGroupingCriterion

    @skipGroupingCriterion.setter
    def skipGroupingCriterion(self, skipGroupingCriterion: str):
        self.__skipGroupingCriterion = skipGroupingCriterion

    @property
    def traversalCriterion(self) -> str:
        return self.__traversalCriterion

    @traversalCriterion.setter
    def traversalCriterion(self, traversalCriterion: str):
        self.__traversalCriterion = traversalCriterion

    @property
    def cardinalityIn(self) -> str:
        return self.__cardinalityIn

    @cardinalityIn.setter
    def cardinalityIn(self, cardinalityIn: str):
        self.__cardinalityIn = cardinalityIn

    @property
    def dataFormatIn(self) -> str:
        return self.__dataFormatIn

    @dataFormatIn.setter
    def dataFormatIn(self, dataFormatIn: str):
        self.__dataFormatIn = dataFormatIn

    @property
    def easyflow_Task19(self):
        return self.__easyflow_Task19

    @easyflow_Task19.setter
    def easyflow_Task19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task19", None)
        self.__easyflow_Task19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToGroupingCriterionMap"):
                    opp_val = getattr(item, "easyflow_StringToGroupingCriterionMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToGroupingCriterionMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToGroupingCriterionMap"):
                    opp_val = getattr(item, "easyflow_StringToGroupingCriterionMap", None)
                    
                    setattr(item, "easyflow_StringToGroupingCriterionMap", self)
                    

    @property
    def easyflow_Task(self):
        return self.__easyflow_Task

    @easyflow_Task.setter
    def easyflow_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task", None)
        self.__easyflow_Task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToToolMap"):
                    opp_val = getattr(item, "easyflow_StringToToolMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToToolMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToToolMap"):
                    opp_val = getattr(item, "easyflow_StringToToolMap", None)
                    
                    setattr(item, "easyflow_StringToToolMap", self)
                    

    @property
    def easyflow_Task26(self):
        return self.__easyflow_Task26

    @easyflow_Task26.setter
    def easyflow_Task26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task26", None)
        self.__easyflow_Task26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_TaskToDataProcessingType27"):
                opp_val = getattr(old_value, "easyflow_TaskToDataProcessingType27", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_TaskToDataProcessingType27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_TaskToDataProcessingType27"):
                opp_val = getattr(value, "easyflow_TaskToDataProcessingType27", None)
                setattr(value, "easyflow_TaskToDataProcessingType27", self)

    @property
    def easyflow_Task17(self):
        return self.__easyflow_Task17

    @easyflow_Task17.setter
    def easyflow_Task17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task17", None)
        self.__easyflow_Task17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToTaskMap"):
                    opp_val = getattr(item, "easyflow_StringToTaskMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToTaskMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToTaskMap"):
                    opp_val = getattr(item, "easyflow_StringToTaskMap", None)
                    
                    setattr(item, "easyflow_StringToTaskMap", self)
                    

    @property
    def easyflow_Task53(self):
        return self.__easyflow_Task53

    @easyflow_Task53.setter
    def easyflow_Task53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task53", None)
        self.__easyflow_Task53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_Tool52"):
                opp_val = getattr(old_value, "easyflow_Tool52", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_Tool52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_Tool52"):
                opp_val = getattr(value, "easyflow_Tool52", None)
                setattr(value, "easyflow_Tool52", self)

    @property
    def easyflow_Task119(self):
        return self.__easyflow_Task119

    @easyflow_Task119.setter
    def easyflow_Task119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task119", None)
        self.__easyflow_Task119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_ITraversal"):
                opp_val = getattr(old_value, "easyflow_ITraversal", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_ITraversal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_ITraversal"):
                opp_val = getattr(value, "easyflow_ITraversal", None)
                setattr(value, "easyflow_ITraversal", self)

    @property
    def easyflow_Task125(self):
        return self.__easyflow_Task125

    @easyflow_Task125.setter
    def easyflow_Task125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task125", None)
        self.__easyflow_Task125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_SplittingEvent124"):
                opp_val = getattr(old_value, "easyflow_SplittingEvent124", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_SplittingEvent124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_SplittingEvent124"):
                opp_val = getattr(value, "easyflow_SplittingEvent124", None)
                setattr(value, "easyflow_SplittingEvent124", self)

    @property
    def easyflow_Task109(self):
        return self.__easyflow_Task109

    @easyflow_Task109.setter
    def easyflow_Task109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task109", None)
        self.__easyflow_Task109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_StringToTaskMap108"):
                opp_val = getattr(old_value, "easyflow_StringToTaskMap108", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_StringToTaskMap108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_StringToTaskMap108"):
                opp_val = getattr(value, "easyflow_StringToTaskMap108", None)
                setattr(value, "easyflow_StringToTaskMap108", self)

    @property
    def easyflow_Task128(self):
        return self.__easyflow_Task128

    @easyflow_Task128.setter
    def easyflow_Task128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task128", None)
        self.__easyflow_Task128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_SplittingEvent127"):
                opp_val = getattr(old_value, "easyflow_SplittingEvent127", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_SplittingEvent127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_SplittingEvent127"):
                opp_val = getattr(value, "easyflow_SplittingEvent127", None)
                setattr(value, "easyflow_SplittingEvent127", self)

    @property
    def easyflow_Task122(self):
        return self.__easyflow_Task122

    @easyflow_Task122.setter
    def easyflow_Task122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task122", None)
        self.__easyflow_Task122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_SplittingEvent"):
                opp_val = getattr(old_value, "easyflow_SplittingEvent", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_SplittingEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_SplittingEvent"):
                opp_val = getattr(value, "easyflow_SplittingEvent", None)
                setattr(value, "easyflow_SplittingEvent", self)

    @property
    def easyflow_Task134(self):
        return self.__easyflow_Task134

    @easyflow_Task134.setter
    def easyflow_Task134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task134", None)
        self.__easyflow_Task134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_TaskToDataProcessingType133"):
                opp_val = getattr(old_value, "easyflow_TaskToDataProcessingType133", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_TaskToDataProcessingType133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_TaskToDataProcessingType133"):
                opp_val = getattr(value, "easyflow_TaskToDataProcessingType133", None)
                setattr(value, "easyflow_TaskToDataProcessingType133", self)

    @property
    def easyflow_Task137(self):
        return self.__easyflow_Task137

    @easyflow_Task137.setter
    def easyflow_Task137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task137", None)
        self.__easyflow_Task137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_DataFormatToTaskList136"):
                opp_val = getattr(old_value, "easyflow_DataFormatToTaskList136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_DataFormatToTaskList136"):
                opp_val = getattr(value, "easyflow_DataFormatToTaskList136", None)
                if opp_val is None:
                    setattr(value, "easyflow_DataFormatToTaskList136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def easyflow_Task21(self):
        return self.__easyflow_Task21

    @easyflow_Task21.setter
    def easyflow_Task21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task21", None)
        self.__easyflow_Task21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToTraversalCriterionMap"):
                    opp_val = getattr(item, "easyflow_StringToTraversalCriterionMap", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToTraversalCriterionMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToTraversalCriterionMap"):
                    opp_val = getattr(item, "easyflow_StringToTraversalCriterionMap", None)
                    
                    setattr(item, "easyflow_StringToTraversalCriterionMap", self)
                    

    @property
    def easyflow_Task23(self):
        return self.__easyflow_Task23

    @easyflow_Task23.setter
    def easyflow_Task23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task23", None)
        self.__easyflow_Task23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_StringToTraversalCriterionMap24"):
                    opp_val = getattr(item, "easyflow_StringToTraversalCriterionMap24", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_StringToTraversalCriterionMap24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_StringToTraversalCriterionMap24"):
                    opp_val = getattr(item, "easyflow_StringToTraversalCriterionMap24", None)
                    
                    setattr(item, "easyflow_StringToTraversalCriterionMap24", self)
                    

    @property
    def easyflow_Task38(self):
        return self.__easyflow_Task38

    @easyflow_Task38.setter
    def easyflow_Task38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Task__easyflow_Task38", None)
        self.__easyflow_Task38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_DataProcessingTypeToTask37"):
                opp_val = getattr(old_value, "easyflow_DataProcessingTypeToTask37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_DataProcessingTypeToTask37"):
                opp_val = getattr(value, "easyflow_DataProcessingTypeToTask37", None)
                if opp_val is None:
                    setattr(value, "easyflow_DataProcessingTypeToTask37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fitsToGroupingCriterionOf(self, task: str) -> bool:
        # TODO: Implement fitsToGroupingCriterionOf method
        pass

    def readTask(self, wtplLine: str):
        # TODO: Implement readTask method
        pass

    def getParentForTask(self, graph: str) -> str:
        # TODO: Implement getParentForTask method
        pass

    def getUniqueString(self) -> str:
        # TODO: Implement getUniqueString method
        pass

    def copy(self) -> str:
        # TODO: Implement copy method
        pass

    def getParentForTask(self, dag: str) -> str:
        # TODO: Implement getParentForTask method
        pass

    def isMarkedToSkip(self) -> bool:
        # TODO: Implement isMarkedToSkip method
        pass

    def evaluateJexlExp(self, map: str) -> bool:
        # TODO: Implement evaluateJexlExp method
        pass

    def isConvertableTo(self, dataFormat: str) -> bool:
        # TODO: Implement isConvertableTo method
        pass

    def getSampleUniqueString(self) -> str:
        # TODO: Implement getSampleUniqueString method
        pass

class easyflow_Workflow:

    def __init__(self, graph: str, name: str, dag: str, jobDag: str, easyflow_Workflow14: set["easyflow_DataFormatToTaskList"] = None, easyflow_Workflow: "easyflow_EasyFlowTemplate" = None, easyflow_Workflow2: "easyflow_EasyFlowConfiguration" = None, easyflow_Workflow4: set["easyflow_EasyFlowMetadata"] = None, easyflow_Workflow6: "easyflow_EasyFlowImplementationTemplate" = None, easyflow_Workflow8: "easyflow_DataProcessingType" = None, easyflow_Workflow10: set["easyflow_DataProcessingTypeToTask"] = None, easyflow_Workflow12: set["easyflow_TaskToDataProcessingType"] = None, easyflow_Workflow30: "easyflow_EasyFlowTemplate" = None):
        self.graph = graph
        self.name = name
        self.dag = dag
        self.jobDag = jobDag
        self.easyflow_Workflow14 = easyflow_Workflow14 if easyflow_Workflow14 is not None else set()
        self.easyflow_Workflow = easyflow_Workflow
        self.easyflow_Workflow2 = easyflow_Workflow2
        self.easyflow_Workflow4 = easyflow_Workflow4 if easyflow_Workflow4 is not None else set()
        self.easyflow_Workflow6 = easyflow_Workflow6
        self.easyflow_Workflow8 = easyflow_Workflow8
        self.easyflow_Workflow10 = easyflow_Workflow10 if easyflow_Workflow10 is not None else set()
        self.easyflow_Workflow12 = easyflow_Workflow12 if easyflow_Workflow12 is not None else set()
        self.easyflow_Workflow30 = easyflow_Workflow30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dag(self) -> str:
        return self.__dag

    @dag.setter
    def dag(self, dag: str):
        self.__dag = dag

    @property
    def graph(self) -> str:
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph

    @property
    def jobDag(self) -> str:
        return self.__jobDag

    @jobDag.setter
    def jobDag(self, jobDag: str):
        self.__jobDag = jobDag

    @property
    def easyflow_Workflow30(self):
        return self.__easyflow_Workflow30

    @easyflow_Workflow30.setter
    def easyflow_Workflow30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow30", None)
        self.__easyflow_Workflow30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowTemplate29"):
                opp_val = getattr(old_value, "easyflow_EasyFlowTemplate29", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_EasyFlowTemplate29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowTemplate29"):
                opp_val = getattr(value, "easyflow_EasyFlowTemplate29", None)
                setattr(value, "easyflow_EasyFlowTemplate29", self)

    @property
    def easyflow_Workflow4(self):
        return self.__easyflow_Workflow4

    @easyflow_Workflow4.setter
    def easyflow_Workflow4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow4", None)
        self.__easyflow_Workflow4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_EasyFlowMetadata"):
                    opp_val = getattr(item, "easyflow_EasyFlowMetadata", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_EasyFlowMetadata", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_EasyFlowMetadata"):
                    opp_val = getattr(item, "easyflow_EasyFlowMetadata", None)
                    
                    setattr(item, "easyflow_EasyFlowMetadata", self)
                    

    @property
    def easyflow_Workflow2(self):
        return self.__easyflow_Workflow2

    @easyflow_Workflow2.setter
    def easyflow_Workflow2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow2", None)
        self.__easyflow_Workflow2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowConfiguration"):
                opp_val = getattr(old_value, "easyflow_EasyFlowConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_EasyFlowConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowConfiguration"):
                opp_val = getattr(value, "easyflow_EasyFlowConfiguration", None)
                setattr(value, "easyflow_EasyFlowConfiguration", self)

    @property
    def easyflow_Workflow14(self):
        return self.__easyflow_Workflow14

    @easyflow_Workflow14.setter
    def easyflow_Workflow14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow14", None)
        self.__easyflow_Workflow14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_DataFormatToTaskList"):
                    opp_val = getattr(item, "easyflow_DataFormatToTaskList", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_DataFormatToTaskList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_DataFormatToTaskList"):
                    opp_val = getattr(item, "easyflow_DataFormatToTaskList", None)
                    
                    setattr(item, "easyflow_DataFormatToTaskList", self)
                    

    @property
    def easyflow_Workflow12(self):
        return self.__easyflow_Workflow12

    @easyflow_Workflow12.setter
    def easyflow_Workflow12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow12", None)
        self.__easyflow_Workflow12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_TaskToDataProcessingType"):
                    opp_val = getattr(item, "easyflow_TaskToDataProcessingType", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_TaskToDataProcessingType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_TaskToDataProcessingType"):
                    opp_val = getattr(item, "easyflow_TaskToDataProcessingType", None)
                    
                    setattr(item, "easyflow_TaskToDataProcessingType", self)
                    

    @property
    def easyflow_Workflow(self):
        return self.__easyflow_Workflow

    @easyflow_Workflow.setter
    def easyflow_Workflow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow", None)
        self.__easyflow_Workflow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowTemplate"):
                opp_val = getattr(old_value, "easyflow_EasyFlowTemplate", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_EasyFlowTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowTemplate"):
                opp_val = getattr(value, "easyflow_EasyFlowTemplate", None)
                setattr(value, "easyflow_EasyFlowTemplate", self)

    @property
    def easyflow_Workflow6(self):
        return self.__easyflow_Workflow6

    @easyflow_Workflow6.setter
    def easyflow_Workflow6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow6", None)
        self.__easyflow_Workflow6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_EasyFlowImplementationTemplate"):
                opp_val = getattr(old_value, "easyflow_EasyFlowImplementationTemplate", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_EasyFlowImplementationTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_EasyFlowImplementationTemplate"):
                opp_val = getattr(value, "easyflow_EasyFlowImplementationTemplate", None)
                setattr(value, "easyflow_EasyFlowImplementationTemplate", self)

    @property
    def easyflow_Workflow8(self):
        return self.__easyflow_Workflow8

    @easyflow_Workflow8.setter
    def easyflow_Workflow8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow8", None)
        self.__easyflow_Workflow8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "easyflow_DataProcessingType"):
                opp_val = getattr(old_value, "easyflow_DataProcessingType", None)
                if opp_val == self:
                    setattr(old_value, "easyflow_DataProcessingType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "easyflow_DataProcessingType"):
                opp_val = getattr(value, "easyflow_DataProcessingType", None)
                setattr(value, "easyflow_DataProcessingType", self)

    @property
    def easyflow_Workflow10(self):
        return self.__easyflow_Workflow10

    @easyflow_Workflow10.setter
    def easyflow_Workflow10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_easyflow_Workflow__easyflow_Workflow10", None)
        self.__easyflow_Workflow10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "easyflow_DataProcessingTypeToTask"):
                    opp_val = getattr(item, "easyflow_DataProcessingTypeToTask", None)
                    
                    if opp_val == self:
                        setattr(item, "easyflow_DataProcessingTypeToTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "easyflow_DataProcessingTypeToTask"):
                    opp_val = getattr(item, "easyflow_DataProcessingTypeToTask", None)
                    
                    setattr(item, "easyflow_DataProcessingTypeToTask", self)
                    

    def getTasksFromLastTaskClassMap(self, strategy: str, dataProcessingTypeIn: str):
        # TODO: Implement getTasksFromLastTaskClassMap method
        pass

    def processMetadata(self, task: str, metadata: str):
        # TODO: Implement processMetadata method
        pass

    def updateLastTaskClassMap(self, task: str, dataProcessingType: str):
        # TODO: Implement updateLastTaskClassMap method
        pass

    def iterateByGroup(self, group: str, task: str, dataCriterion: str, dag: str) -> str:
        # TODO: Implement iterateByGroup method
        pass

    def createJobDag(self):
        # TODO: Implement createJobDag method
        pass

    def getTasksFromLastTaskClass(self, dataFormatIn: str, dataFormatOut: str, strategy: str) -> str:
        # TODO: Implement getTasksFromLastTaskClass method
        pass

    def getNextSplittingEvent(self, processedTasks: str):
        # TODO: Implement getNextSplittingEvent method
        pass

    def writeAWSCloudFormation(self):
        # TODO: Implement writeAWSCloudFormation method
        pass

    def printLastTaskMap(self):
        # TODO: Implement printLastTaskMap method
        pass

    def processMetadataSet(self, task: str):
        # TODO: Implement processMetadataSet method
        pass

    def printLastTaskClassMap(self):
        # TODO: Implement printLastTaskClassMap method
        pass

    def writeMakeflow(self):
        # TODO: Implement writeMakeflow method
        pass

    def updateLastTaskClass(self, task: str, dataFormatIn: str, dataFormatOut: str):
        # TODO: Implement updateLastTaskClass method
        pass

    def createTaskDag(self):
        # TODO: Implement createTaskDag method
        pass

    def checkDag(self):
        # TODO: Implement checkDag method
        pass

    def resolveStaticDependencies(self):
        # TODO: Implement resolveStaticDependencies method
        pass
