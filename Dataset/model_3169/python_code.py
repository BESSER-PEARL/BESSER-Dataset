from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traceabilitymodel_Block:

    def __init__(self, endLine: str, ID: str, startPos: str, endPos: str, protectedBlock: bool, startLine: str, startColumn: str, endColumn: str, traceabilitymodel_Block: set["traceabilitymodel_TraceableSegment"] = None, traceabilitymodel_Block19: "traceabilitymodel_File" = None):
        self.endLine = endLine
        self.ID = ID
        self.startPos = startPos
        self.endPos = endPos
        self.protectedBlock = protectedBlock
        self.startLine = startLine
        self.startColumn = startColumn
        self.endColumn = endColumn
        self.traceabilitymodel_Block = traceabilitymodel_Block if traceabilitymodel_Block is not None else set()
        self.traceabilitymodel_Block19 = traceabilitymodel_Block19
        
    @property
    def startPos(self) -> str:
        return self.__startPos

    @startPos.setter
    def startPos(self, startPos: str):
        self.__startPos = startPos

    @property
    def endPos(self) -> str:
        return self.__endPos

    @endPos.setter
    def endPos(self, endPos: str):
        self.__endPos = endPos

    @property
    def startLine(self) -> str:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: str):
        self.__startLine = startLine

    @property
    def endColumn(self) -> str:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: str):
        self.__endColumn = endColumn

    @property
    def endLine(self) -> str:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: str):
        self.__endLine = endLine

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def startColumn(self) -> str:
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: str):
        self.__startColumn = startColumn

    @property
    def protectedBlock(self) -> bool:
        return self.__protectedBlock

    @protectedBlock.setter
    def protectedBlock(self, protectedBlock: bool):
        self.__protectedBlock = protectedBlock

    @property
    def traceabilitymodel_Block19(self):
        return self.__traceabilitymodel_Block19

    @traceabilitymodel_Block19.setter
    def traceabilitymodel_Block19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_Block__traceabilitymodel_Block19", None)
        self.__traceabilitymodel_Block19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_File18"):
                opp_val = getattr(old_value, "traceabilitymodel_File18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_File18"):
                opp_val = getattr(value, "traceabilitymodel_File18", None)
                if opp_val is None:
                    setattr(value, "traceabilitymodel_File18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceabilitymodel_Block(self):
        return self.__traceabilitymodel_Block

    @traceabilitymodel_Block.setter
    def traceabilitymodel_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_Block__traceabilitymodel_Block", None)
        self.__traceabilitymodel_Block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceabilitymodel_TraceableSegment6"):
                    opp_val = getattr(item, "traceabilitymodel_TraceableSegment6", None)
                    
                    if opp_val == self:
                        setattr(item, "traceabilitymodel_TraceableSegment6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceabilitymodel_TraceableSegment6"):
                    opp_val = getattr(item, "traceabilitymodel_TraceableSegment6", None)
                    
                    setattr(item, "traceabilitymodel_TraceableSegment6", self)
                    

class traceabilitymodel_File:

    def __init__(self, ID: str, name: str, URI: str, traceabilitymodel_File: "traceabilitymodel_TraceModel" = None, traceabilitymodel_File18: set["traceabilitymodel_Block"] = None):
        self.ID = ID
        self.name = name
        self.URI = URI
        self.traceabilitymodel_File = traceabilitymodel_File
        self.traceabilitymodel_File18 = traceabilitymodel_File18 if traceabilitymodel_File18 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traceabilitymodel_File18(self):
        return self.__traceabilitymodel_File18

    @traceabilitymodel_File18.setter
    def traceabilitymodel_File18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_File__traceabilitymodel_File18", None)
        self.__traceabilitymodel_File18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceabilitymodel_Block19"):
                    opp_val = getattr(item, "traceabilitymodel_Block19", None)
                    
                    if opp_val == self:
                        setattr(item, "traceabilitymodel_Block19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceabilitymodel_Block19"):
                    opp_val = getattr(item, "traceabilitymodel_Block19", None)
                    
                    setattr(item, "traceabilitymodel_Block19", self)
                    

    @property
    def traceabilitymodel_File(self):
        return self.__traceabilitymodel_File

    @traceabilitymodel_File.setter
    def traceabilitymodel_File(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_File__traceabilitymodel_File", None)
        self.__traceabilitymodel_File = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_TraceModel10"):
                opp_val = getattr(old_value, "traceabilitymodel_TraceModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_TraceModel10"):
                opp_val = getattr(value, "traceabilitymodel_TraceModel10", None)
                if opp_val is None:
                    setattr(value, "traceabilitymodel_TraceModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traceabilitymodel_TraceModel:

    pass
class traceabilitymodel_TraceableSegment:

    def __init__(self, startPos: str, endPos: str, startLine: str, endLine: str, startColumn: str, endColumn: str, traceabilitymodel_TraceableSegment: "traceabilitymodel_Trace" = None, traceabilitymodel_TraceableSegment6: "traceabilitymodel_Block" = None):
        self.startPos = startPos
        self.endPos = endPos
        self.startLine = startLine
        self.endLine = endLine
        self.startColumn = startColumn
        self.endColumn = endColumn
        self.traceabilitymodel_TraceableSegment = traceabilitymodel_TraceableSegment
        self.traceabilitymodel_TraceableSegment6 = traceabilitymodel_TraceableSegment6
        
    @property
    def startColumn(self) -> str:
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: str):
        self.__startColumn = startColumn

    @property
    def endColumn(self) -> str:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: str):
        self.__endColumn = endColumn

    @property
    def startLine(self) -> str:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: str):
        self.__startLine = startLine

    @property
    def startPos(self) -> str:
        return self.__startPos

    @startPos.setter
    def startPos(self, startPos: str):
        self.__startPos = startPos

    @property
    def endPos(self) -> str:
        return self.__endPos

    @endPos.setter
    def endPos(self, endPos: str):
        self.__endPos = endPos

    @property
    def endLine(self) -> str:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: str):
        self.__endLine = endLine

    @property
    def traceabilitymodel_TraceableSegment(self):
        return self.__traceabilitymodel_TraceableSegment

    @traceabilitymodel_TraceableSegment.setter
    def traceabilitymodel_TraceableSegment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_TraceableSegment__traceabilitymodel_TraceableSegment", None)
        self.__traceabilitymodel_TraceableSegment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_Trace"):
                opp_val = getattr(old_value, "traceabilitymodel_Trace", None)
                if opp_val == self:
                    setattr(old_value, "traceabilitymodel_Trace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_Trace"):
                opp_val = getattr(value, "traceabilitymodel_Trace", None)
                setattr(value, "traceabilitymodel_Trace", self)

    @property
    def traceabilitymodel_TraceableSegment6(self):
        return self.__traceabilitymodel_TraceableSegment6

    @traceabilitymodel_TraceableSegment6.setter
    def traceabilitymodel_TraceableSegment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_TraceableSegment__traceabilitymodel_TraceableSegment6", None)
        self.__traceabilitymodel_TraceableSegment6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_Block"):
                opp_val = getattr(old_value, "traceabilitymodel_Block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_Block"):
                opp_val = getattr(value, "traceabilitymodel_Block", None)
                if opp_val is None:
                    setattr(value, "traceabilitymodel_Block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traceabilitymodel_Trace:

    def __init__(self, sourceOperationName: str, specificationName: str, sourceOperationID: str, traceabilitymodel_Trace3: "traceabilitymodel_ModelElementRef" = None, traceabilitymodel_Trace: "traceabilitymodel_TraceableSegment" = None, traceabilitymodel_Trace8: "traceabilitymodel_TraceModel" = None):
        self.sourceOperationName = sourceOperationName
        self.specificationName = specificationName
        self.sourceOperationID = sourceOperationID
        self.traceabilitymodel_Trace3 = traceabilitymodel_Trace3
        self.traceabilitymodel_Trace = traceabilitymodel_Trace
        self.traceabilitymodel_Trace8 = traceabilitymodel_Trace8
        
    @property
    def specificationName(self) -> str:
        return self.__specificationName

    @specificationName.setter
    def specificationName(self, specificationName: str):
        self.__specificationName = specificationName

    @property
    def sourceOperationID(self) -> str:
        return self.__sourceOperationID

    @sourceOperationID.setter
    def sourceOperationID(self, sourceOperationID: str):
        self.__sourceOperationID = sourceOperationID

    @property
    def sourceOperationName(self) -> str:
        return self.__sourceOperationName

    @sourceOperationName.setter
    def sourceOperationName(self, sourceOperationName: str):
        self.__sourceOperationName = sourceOperationName

    @property
    def traceabilitymodel_Trace(self):
        return self.__traceabilitymodel_Trace

    @traceabilitymodel_Trace.setter
    def traceabilitymodel_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_Trace__traceabilitymodel_Trace", None)
        self.__traceabilitymodel_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_TraceableSegment"):
                opp_val = getattr(old_value, "traceabilitymodel_TraceableSegment", None)
                if opp_val == self:
                    setattr(old_value, "traceabilitymodel_TraceableSegment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_TraceableSegment"):
                opp_val = getattr(value, "traceabilitymodel_TraceableSegment", None)
                setattr(value, "traceabilitymodel_TraceableSegment", self)

    @property
    def traceabilitymodel_Trace8(self):
        return self.__traceabilitymodel_Trace8

    @traceabilitymodel_Trace8.setter
    def traceabilitymodel_Trace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_Trace__traceabilitymodel_Trace8", None)
        self.__traceabilitymodel_Trace8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_TraceModel"):
                opp_val = getattr(old_value, "traceabilitymodel_TraceModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_TraceModel"):
                opp_val = getattr(value, "traceabilitymodel_TraceModel", None)
                if opp_val is None:
                    setattr(value, "traceabilitymodel_TraceModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceabilitymodel_Trace3(self):
        return self.__traceabilitymodel_Trace3

    @traceabilitymodel_Trace3.setter
    def traceabilitymodel_Trace3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_Trace__traceabilitymodel_Trace3", None)
        self.__traceabilitymodel_Trace3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_ModelElementRef4"):
                opp_val = getattr(old_value, "traceabilitymodel_ModelElementRef4", None)
                if opp_val == self:
                    setattr(old_value, "traceabilitymodel_ModelElementRef4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_ModelElementRef4"):
                opp_val = getattr(value, "traceabilitymodel_ModelElementRef4", None)
                setattr(value, "traceabilitymodel_ModelElementRef4", self)

class traceabilitymodel_MetaModel:

    def __init__(self, name: str, nsUri: str, traceabilitymodel_MetaModel: "traceabilitymodel_ModelElementRef" = None, traceabilitymodel_MetaModel16: "traceabilitymodel_TraceModel" = None):
        self.name = name
        self.nsUri = nsUri
        self.traceabilitymodel_MetaModel = traceabilitymodel_MetaModel
        self.traceabilitymodel_MetaModel16 = traceabilitymodel_MetaModel16
        
    @property
    def nsUri(self) -> str:
        return self.__nsUri

    @nsUri.setter
    def nsUri(self, nsUri: str):
        self.__nsUri = nsUri

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def traceabilitymodel_MetaModel(self):
        return self.__traceabilitymodel_MetaModel

    @traceabilitymodel_MetaModel.setter
    def traceabilitymodel_MetaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_MetaModel__traceabilitymodel_MetaModel", None)
        self.__traceabilitymodel_MetaModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_ModelElementRef"):
                opp_val = getattr(old_value, "traceabilitymodel_ModelElementRef", None)
                if opp_val == self:
                    setattr(old_value, "traceabilitymodel_ModelElementRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_ModelElementRef"):
                opp_val = getattr(value, "traceabilitymodel_ModelElementRef", None)
                setattr(value, "traceabilitymodel_ModelElementRef", self)

    @property
    def traceabilitymodel_MetaModel16(self):
        return self.__traceabilitymodel_MetaModel16

    @traceabilitymodel_MetaModel16.setter
    def traceabilitymodel_MetaModel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_MetaModel__traceabilitymodel_MetaModel16", None)
        self.__traceabilitymodel_MetaModel16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_TraceModel15"):
                opp_val = getattr(old_value, "traceabilitymodel_TraceModel15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_TraceModel15"):
                opp_val = getattr(value, "traceabilitymodel_TraceModel15", None)
                if opp_val is None:
                    setattr(value, "traceabilitymodel_TraceModel15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class traceabilitymodel_ModelElementRef:

    def __init__(self, ID: str, name: str, featureRef: str, uri: str, traceabilitymodel_ModelElementRef4: "traceabilitymodel_Trace" = None, traceabilitymodel_ModelElementRef: "traceabilitymodel_MetaModel" = None, traceabilitymodel_ModelElementRef13: "traceabilitymodel_TraceModel" = None):
        self.ID = ID
        self.name = name
        self.featureRef = featureRef
        self.uri = uri
        self.traceabilitymodel_ModelElementRef4 = traceabilitymodel_ModelElementRef4
        self.traceabilitymodel_ModelElementRef = traceabilitymodel_ModelElementRef
        self.traceabilitymodel_ModelElementRef13 = traceabilitymodel_ModelElementRef13
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def featureRef(self) -> str:
        return self.__featureRef

    @featureRef.setter
    def featureRef(self, featureRef: str):
        self.__featureRef = featureRef

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def traceabilitymodel_ModelElementRef13(self):
        return self.__traceabilitymodel_ModelElementRef13

    @traceabilitymodel_ModelElementRef13.setter
    def traceabilitymodel_ModelElementRef13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_ModelElementRef__traceabilitymodel_ModelElementRef13", None)
        self.__traceabilitymodel_ModelElementRef13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_TraceModel12"):
                opp_val = getattr(old_value, "traceabilitymodel_TraceModel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_TraceModel12"):
                opp_val = getattr(value, "traceabilitymodel_TraceModel12", None)
                if opp_val is None:
                    setattr(value, "traceabilitymodel_TraceModel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceabilitymodel_ModelElementRef4(self):
        return self.__traceabilitymodel_ModelElementRef4

    @traceabilitymodel_ModelElementRef4.setter
    def traceabilitymodel_ModelElementRef4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_ModelElementRef__traceabilitymodel_ModelElementRef4", None)
        self.__traceabilitymodel_ModelElementRef4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_Trace3"):
                opp_val = getattr(old_value, "traceabilitymodel_Trace3", None)
                if opp_val == self:
                    setattr(old_value, "traceabilitymodel_Trace3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_Trace3"):
                opp_val = getattr(value, "traceabilitymodel_Trace3", None)
                setattr(value, "traceabilitymodel_Trace3", self)

    @property
    def traceabilitymodel_ModelElementRef(self):
        return self.__traceabilitymodel_ModelElementRef

    @traceabilitymodel_ModelElementRef.setter
    def traceabilitymodel_ModelElementRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceabilitymodel_ModelElementRef__traceabilitymodel_ModelElementRef", None)
        self.__traceabilitymodel_ModelElementRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceabilitymodel_MetaModel"):
                opp_val = getattr(old_value, "traceabilitymodel_MetaModel", None)
                if opp_val == self:
                    setattr(old_value, "traceabilitymodel_MetaModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceabilitymodel_MetaModel"):
                opp_val = getattr(value, "traceabilitymodel_MetaModel", None)
                setattr(value, "traceabilitymodel_MetaModel", self)
