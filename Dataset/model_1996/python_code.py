from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Mode(Enum):
    Automatic = "Automatic"
    Manual = "Manual"
class Type(Enum):
    Transformation = "Transformation"
    Annotation = "Annotation"
class AbstractionLevel(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    CIM = "CIM"
    PIM = "PIM"
    PSM = "PSM"
    PDM = "PDM"
    CODE = "CODE"
    ANNOTATION = "ANNOTATION"
class ModelType(Enum):
    Source = "Source"
    Target = "Target"
    Both = "Both"
    None = "None"
class Aspect(Enum):
    Unspecified = "Unspecified"
    Architecture = "Architecture"
    Behaviour = "Behaviour"
    Content = "Content"
    Interface = "Interface"
    Quality = "Quality"
    Semantics = "Semantics"


############################################
# Definition of Classes
############################################

class TraceLinkElement:

    pass
class iTrace_Feature:

    def __init__(self, attribute: str, value: str, features: "iTrace_SpecificFeature" = None, Feature: "iTrace_SpecificFeature" = None):
        self.attribute = attribute
        self.value = value
        self.features = features
        self.Feature = Feature
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specificFeature"):
                opp_val = getattr(old_value, "specificFeature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specificFeature"):
                opp_val = getattr(value, "specificFeature", None)
                if opp_val is None:
                    setattr(value, "specificFeature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SpecificFeature25"):
                opp_val = getattr(old_value, "SpecificFeature25", None)
                if opp_val == self:
                    setattr(old_value, "SpecificFeature25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SpecificFeature25"):
                opp_val = getattr(value, "SpecificFeature25", None)
                setattr(value, "SpecificFeature25", self)

class iTrace_Block:

    def __init__(self, blockNumber: int, startLine: int, endLine: int, startColumn: int, endColumn: int, Block17: "iTrace_Code" = None, blocks: "iTrace_Code" = None, targetBlocks: "iTrace_M2TLink" = None, Block: "iTrace_M2TLink" = None):
        self.blockNumber = blockNumber
        self.startLine = startLine
        self.endLine = endLine
        self.startColumn = startColumn
        self.endColumn = endColumn
        self.Block17 = Block17
        self.blocks = blocks
        self.targetBlocks = targetBlocks
        self.Block = Block
        
    @property
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

    @property
    def startColumn(self) -> int:
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn

    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

    @property
    def endColumn(self) -> int:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn

    @property
    def blockNumber(self) -> int:
        return self.__blockNumber

    @blockNumber.setter
    def blockNumber(self, blockNumber: int):
        self.__blockNumber = blockNumber

    @property
    def Block(self):
        return self.__Block

    @Block.setter
    def Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Block__Block", None)
        self.__Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceLink13"):
                opp_val = getattr(old_value, "traceLink13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceLink13"):
                opp_val = getattr(value, "traceLink13", None)
                if opp_val is None:
                    setattr(value, "traceLink13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def targetBlocks(self):
        return self.__targetBlocks

    @targetBlocks.setter
    def targetBlocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Block__targetBlocks", None)
        self.__targetBlocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "M2TLink"):
                opp_val = getattr(old_value, "M2TLink", None)
                if opp_val == self:
                    setattr(old_value, "M2TLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "M2TLink"):
                opp_val = getattr(value, "M2TLink", None)
                setattr(value, "M2TLink", self)

    @property
    def Block17(self):
        return self.__Block17

    @Block17.setter
    def Block17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Block__Block17", None)
        self.__Block17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "code"):
                opp_val = getattr(old_value, "code", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "code"):
                opp_val = getattr(value, "code", None)
                if opp_val is None:
                    setattr(value, "code", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blocks(self):
        return self.__blocks

    @blocks.setter
    def blocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Block__blocks", None)
        self.__blocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Code"):
                opp_val = getattr(old_value, "Code", None)
                if opp_val == self:
                    setattr(old_value, "Code", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Code"):
                opp_val = getattr(value, "Code", None)
                setattr(value, "Code", self)

class iTrace_TargetElement(TraceLinkElement):

    pass
class TraceLink:

    pass
class iTrace_M2TLink(TraceLink):

    pass
class iTrace_M2MLink(TraceLink):

    pass
class iTrace_EObject:

    pass
class iTrace_TraceLinkElement(ABC):

    def __init__(self, ref: str, type: str, TraceLinkElement: "iTrace_Model" = None, elements: "iTrace_Model" = None, iTrace_TraceLinkElement: "iTrace_EObject" = None):
        self.ref = ref
        self.type = type
        self.TraceLinkElement = TraceLinkElement
        self.elements = elements
        self.iTrace_TraceLinkElement = iTrace_TraceLinkElement
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLinkElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model"):
                opp_val = getattr(old_value, "Model", None)
                if opp_val == self:
                    setattr(old_value, "Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model"):
                opp_val = getattr(value, "Model", None)
                setattr(value, "Model", self)

    @property
    def TraceLinkElement(self):
        return self.__TraceLinkElement

    @TraceLinkElement.setter
    def TraceLinkElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLinkElement__TraceLinkElement", None)
        self.__TraceLinkElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                if opp_val is None:
                    setattr(value, "model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iTrace_TraceLinkElement(self):
        return self.__iTrace_TraceLinkElement

    @iTrace_TraceLinkElement.setter
    def iTrace_TraceLinkElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLinkElement__iTrace_TraceLinkElement", None)
        self.__iTrace_TraceLinkElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTrace_EObject"):
                opp_val = getattr(old_value, "iTrace_EObject", None)
                if opp_val == self:
                    setattr(old_value, "iTrace_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTrace_EObject"):
                opp_val = getattr(value, "iTrace_EObject", None)
                setattr(value, "iTrace_EObject", self)

class Artefact:

    pass
class iTrace_Model(Artefact):

    def __init__(self, metamodel: str, Model: "iTrace_TraceLinkElement" = None, model: set["iTrace_TraceLinkElement"] = None):
        self.metamodel = metamodel
        self.Model = Model
        self.model = model if model is not None else set()
        
    @property
    def metamodel(self) -> str:
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, metamodel: str):
        self.__metamodel = metamodel

    @property
    def Model(self):
        return self.__Model

    @Model.setter
    def Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Model__Model", None)
        self.__Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Model__model", None)
        self.__model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceLinkElement"):
                    opp_val = getattr(item, "TraceLinkElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceLinkElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceLinkElement"):
                    opp_val = getattr(item, "TraceLinkElement", None)
                    
                    setattr(item, "TraceLinkElement", self)
                    

    def getModelType(self) -> str:
        # TODO: Implement getModelType method
        pass

class iTrace_Code(Artefact):

    pass
class iTrace_TraceLink(ABC):

    def __init__(self, createdOn: str, type: str, fromFileName: str, comment: str, createdBy: str, mode: str, technicalBinding: str, ruleName: str, traceLink: set["iTrace_SourceElement"] = None, traceLinks: "iTrace_iTraceModel" = None, TraceLink: "iTrace_iTraceModel" = None, TraceLink22: "iTrace_SourceElement" = None):
        self.createdOn = createdOn
        self.type = type
        self.fromFileName = fromFileName
        self.comment = comment
        self.createdBy = createdBy
        self.mode = mode
        self.technicalBinding = technicalBinding
        self.ruleName = ruleName
        self.traceLink = traceLink if traceLink is not None else set()
        self.traceLinks = traceLinks
        self.TraceLink = TraceLink
        self.TraceLink22 = TraceLink22
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def createdBy(self) -> str:
        return self.__createdBy

    @createdBy.setter
    def createdBy(self, createdBy: str):
        self.__createdBy = createdBy

    @property
    def ruleName(self) -> str:
        return self.__ruleName

    @ruleName.setter
    def ruleName(self, ruleName: str):
        self.__ruleName = ruleName

    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def createdOn(self) -> str:
        return self.__createdOn

    @createdOn.setter
    def createdOn(self, createdOn: str):
        self.__createdOn = createdOn

    @property
    def fromFileName(self) -> str:
        return self.__fromFileName

    @fromFileName.setter
    def fromFileName(self, fromFileName: str):
        self.__fromFileName = fromFileName

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def technicalBinding(self) -> str:
        return self.__technicalBinding

    @technicalBinding.setter
    def technicalBinding(self, technicalBinding: str):
        self.__technicalBinding = technicalBinding

    @property
    def TraceLink(self):
        return self.__TraceLink

    @TraceLink.setter
    def TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLink__TraceLink", None)
        self.__TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTraceModel"):
                opp_val = getattr(old_value, "iTraceModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTraceModel"):
                opp_val = getattr(value, "iTraceModel", None)
                if opp_val is None:
                    setattr(value, "iTraceModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TraceLink22(self):
        return self.__TraceLink22

    @TraceLink22.setter
    def TraceLink22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLink__TraceLink22", None)
        self.__TraceLink22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceElements"):
                opp_val = getattr(old_value, "sourceElements", None)
                if opp_val == self:
                    setattr(old_value, "sourceElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceElements"):
                opp_val = getattr(value, "sourceElements", None)
                setattr(value, "sourceElements", self)

    @property
    def traceLinks(self):
        return self.__traceLinks

    @traceLinks.setter
    def traceLinks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLink__traceLinks", None)
        self.__traceLinks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTraceModel7"):
                opp_val = getattr(old_value, "iTraceModel7", None)
                if opp_val == self:
                    setattr(old_value, "iTraceModel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTraceModel7"):
                opp_val = getattr(value, "iTraceModel7", None)
                setattr(value, "iTraceModel7", self)

    @property
    def traceLink(self):
        return self.__traceLink

    @traceLink.setter
    def traceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_TraceLink__traceLink", None)
        self.__traceLink = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SourceElement"):
                    opp_val = getattr(item, "SourceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SourceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SourceElement"):
                    opp_val = getattr(item, "SourceElement", None)
                    
                    setattr(item, "SourceElement", self)
                    

class iTrace_iTraceModel:

    def __init__(self, version: str, projectName: str, iTraceModel: set["iTrace_TraceLink"] = None, iTraceModel2: set["iTrace_Artefact"] = None, iTraceModel4: "iTrace_SpecificFeature" = None, iTraceModel7: "iTrace_TraceLink" = None, iTraceModel15: "iTrace_Artefact" = None, iTraceModel28: "iTrace_SpecificFeature" = None):
        self.version = version
        self.projectName = projectName
        self.iTraceModel = iTraceModel if iTraceModel is not None else set()
        self.iTraceModel2 = iTraceModel2 if iTraceModel2 is not None else set()
        self.iTraceModel4 = iTraceModel4
        self.iTraceModel7 = iTraceModel7
        self.iTraceModel15 = iTraceModel15
        self.iTraceModel28 = iTraceModel28
        
    @property
    def projectName(self) -> str:
        return self.__projectName

    @projectName.setter
    def projectName(self, projectName: str):
        self.__projectName = projectName

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def iTraceModel(self):
        return self.__iTraceModel

    @iTraceModel.setter
    def iTraceModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_iTraceModel__iTraceModel", None)
        self.__iTraceModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceLink"):
                    opp_val = getattr(item, "TraceLink", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceLink"):
                    opp_val = getattr(item, "TraceLink", None)
                    
                    setattr(item, "TraceLink", self)
                    

    @property
    def iTraceModel28(self):
        return self.__iTraceModel28

    @iTraceModel28.setter
    def iTraceModel28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_iTraceModel__iTraceModel28", None)
        self.__iTraceModel28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specificFeatures"):
                opp_val = getattr(old_value, "specificFeatures", None)
                if opp_val == self:
                    setattr(old_value, "specificFeatures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specificFeatures"):
                opp_val = getattr(value, "specificFeatures", None)
                setattr(value, "specificFeatures", self)

    @property
    def iTraceModel7(self):
        return self.__iTraceModel7

    @iTraceModel7.setter
    def iTraceModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_iTraceModel__iTraceModel7", None)
        self.__iTraceModel7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceLinks"):
                opp_val = getattr(old_value, "traceLinks", None)
                if opp_val == self:
                    setattr(old_value, "traceLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceLinks"):
                opp_val = getattr(value, "traceLinks", None)
                setattr(value, "traceLinks", self)

    @property
    def iTraceModel4(self):
        return self.__iTraceModel4

    @iTraceModel4.setter
    def iTraceModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_iTraceModel__iTraceModel4", None)
        self.__iTraceModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SpecificFeature"):
                opp_val = getattr(old_value, "SpecificFeature", None)
                if opp_val == self:
                    setattr(old_value, "SpecificFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SpecificFeature"):
                opp_val = getattr(value, "SpecificFeature", None)
                setattr(value, "SpecificFeature", self)

    @property
    def iTraceModel15(self):
        return self.__iTraceModel15

    @iTraceModel15.setter
    def iTraceModel15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_iTraceModel__iTraceModel15", None)
        self.__iTraceModel15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "artefacts"):
                opp_val = getattr(old_value, "artefacts", None)
                if opp_val == self:
                    setattr(old_value, "artefacts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "artefacts"):
                opp_val = getattr(value, "artefacts", None)
                setattr(value, "artefacts", self)

    @property
    def iTraceModel2(self):
        return self.__iTraceModel2

    @iTraceModel2.setter
    def iTraceModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_iTraceModel__iTraceModel2", None)
        self.__iTraceModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Artefact"):
                    opp_val = getattr(item, "Artefact", None)
                    
                    if opp_val == self:
                        setattr(item, "Artefact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Artefact"):
                    opp_val = getattr(item, "Artefact", None)
                    
                    setattr(item, "Artefact", self)
                    

class iTrace_SourceElement(TraceLinkElement):

    pass
class iTrace_SpecificFeature:

    def __init__(self, groupName: str, SpecificFeature: "iTrace_iTraceModel" = None, SpecificFeature25: "iTrace_Feature" = None, specificFeature: set["iTrace_Feature"] = None, specificFeatures: "iTrace_iTraceModel" = None):
        self.groupName = groupName
        self.SpecificFeature = SpecificFeature
        self.SpecificFeature25 = SpecificFeature25
        self.specificFeature = specificFeature if specificFeature is not None else set()
        self.specificFeatures = specificFeatures
        
    @property
    def groupName(self) -> str:
        return self.__groupName

    @groupName.setter
    def groupName(self, groupName: str):
        self.__groupName = groupName

    @property
    def specificFeature(self):
        return self.__specificFeature

    @specificFeature.setter
    def specificFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_SpecificFeature__specificFeature", None)
        self.__specificFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def SpecificFeature(self):
        return self.__SpecificFeature

    @SpecificFeature.setter
    def SpecificFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_SpecificFeature__SpecificFeature", None)
        self.__SpecificFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTraceModel4"):
                opp_val = getattr(old_value, "iTraceModel4", None)
                if opp_val == self:
                    setattr(old_value, "iTraceModel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTraceModel4"):
                opp_val = getattr(value, "iTraceModel4", None)
                setattr(value, "iTraceModel4", self)

    @property
    def SpecificFeature25(self):
        return self.__SpecificFeature25

    @SpecificFeature25.setter
    def SpecificFeature25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_SpecificFeature__SpecificFeature25", None)
        self.__SpecificFeature25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

    @property
    def specificFeatures(self):
        return self.__specificFeatures

    @specificFeatures.setter
    def specificFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_SpecificFeature__specificFeatures", None)
        self.__specificFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTraceModel28"):
                opp_val = getattr(old_value, "iTraceModel28", None)
                if opp_val == self:
                    setattr(old_value, "iTraceModel28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTraceModel28"):
                opp_val = getattr(value, "iTraceModel28", None)
                setattr(value, "iTraceModel28", self)

class iTrace_Artefact(ABC):

    def __init__(self, name: str, abstractionLevel: str, path: str, aspect: str, Artefact: "iTrace_iTraceModel" = None, artefacts: "iTrace_iTraceModel" = None):
        self.name = name
        self.abstractionLevel = abstractionLevel
        self.path = path
        self.aspect = aspect
        self.Artefact = Artefact
        self.artefacts = artefacts
        
    @property
    def aspect(self) -> str:
        return self.__aspect

    @aspect.setter
    def aspect(self, aspect: str):
        self.__aspect = aspect

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def abstractionLevel(self) -> str:
        return self.__abstractionLevel

    @abstractionLevel.setter
    def abstractionLevel(self, abstractionLevel: str):
        self.__abstractionLevel = abstractionLevel

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def artefacts(self):
        return self.__artefacts

    @artefacts.setter
    def artefacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Artefact__artefacts", None)
        self.__artefacts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTraceModel15"):
                opp_val = getattr(old_value, "iTraceModel15", None)
                if opp_val == self:
                    setattr(old_value, "iTraceModel15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTraceModel15"):
                opp_val = getattr(value, "iTraceModel15", None)
                setattr(value, "iTraceModel15", self)

    @property
    def Artefact(self):
        return self.__Artefact

    @Artefact.setter
    def Artefact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iTrace_Artefact__Artefact", None)
        self.__Artefact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iTraceModel2"):
                opp_val = getattr(old_value, "iTraceModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iTraceModel2"):
                opp_val = getattr(value, "iTraceModel2", None)
                if opp_val is None:
                    setattr(value, "iTraceModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
