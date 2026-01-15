####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
traceabilitymodel_ModelElementRef = Class(name="traceabilitymodel::ModelElementRef")
traceabilitymodel_MetaModel = Class(name="traceabilitymodel::MetaModel")
traceabilitymodel_Trace = Class(name="traceabilitymodel::Trace")
traceabilitymodel_TraceableSegment = Class(name="traceabilitymodel::TraceableSegment")
traceabilitymodel_TraceModel = Class(name="traceabilitymodel::TraceModel")
traceabilitymodel_File = Class(name="traceabilitymodel::File")
traceabilitymodel_Block = Class(name="traceabilitymodel::Block")

# traceabilitymodel_ModelElementRef class attributes and methods
traceabilitymodel_ModelElementRef_ID: Property = Property(name="ID", type=StringType)
traceabilitymodel_ModelElementRef_name: Property = Property(name="name", type=StringType)
traceabilitymodel_ModelElementRef_featureRef: Property = Property(name="featureRef", type=StringType)
traceabilitymodel_ModelElementRef_uri: Property = Property(name="uri", type=StringType)
traceabilitymodel_ModelElementRef.attributes={traceabilitymodel_ModelElementRef_uri, traceabilitymodel_ModelElementRef_featureRef, traceabilitymodel_ModelElementRef_name, traceabilitymodel_ModelElementRef_ID}

# traceabilitymodel_MetaModel class attributes and methods
traceabilitymodel_MetaModel_name: Property = Property(name="name", type=StringType)
traceabilitymodel_MetaModel_nsUri: Property = Property(name="nsUri", type=StringType)
traceabilitymodel_MetaModel.attributes={traceabilitymodel_MetaModel_nsUri, traceabilitymodel_MetaModel_name}

# traceabilitymodel_Trace class attributes and methods
traceabilitymodel_Trace_sourceOperationName: Property = Property(name="sourceOperationName", type=StringType)
traceabilitymodel_Trace_specificationName: Property = Property(name="specificationName", type=StringType)
traceabilitymodel_Trace_sourceOperationID: Property = Property(name="sourceOperationID", type=StringType)
traceabilitymodel_Trace.attributes={traceabilitymodel_Trace_specificationName, traceabilitymodel_Trace_sourceOperationID, traceabilitymodel_Trace_sourceOperationName}

# traceabilitymodel_TraceableSegment class attributes and methods
traceabilitymodel_TraceableSegment_startPos: Property = Property(name="startPos", type=StringType)
traceabilitymodel_TraceableSegment_endPos: Property = Property(name="endPos", type=StringType)
traceabilitymodel_TraceableSegment_startLine: Property = Property(name="startLine", type=StringType)
traceabilitymodel_TraceableSegment_endLine: Property = Property(name="endLine", type=StringType)
traceabilitymodel_TraceableSegment_startColumn: Property = Property(name="startColumn", type=StringType)
traceabilitymodel_TraceableSegment_endColumn: Property = Property(name="endColumn", type=StringType)
traceabilitymodel_TraceableSegment.attributes={traceabilitymodel_TraceableSegment_startColumn, traceabilitymodel_TraceableSegment_endColumn, traceabilitymodel_TraceableSegment_startLine, traceabilitymodel_TraceableSegment_startPos, traceabilitymodel_TraceableSegment_endPos, traceabilitymodel_TraceableSegment_endLine}

# traceabilitymodel_TraceModel class attributes and methods

# traceabilitymodel_File class attributes and methods
traceabilitymodel_File_ID: Property = Property(name="ID", type=StringType)
traceabilitymodel_File_name: Property = Property(name="name", type=StringType)
traceabilitymodel_File_URI: Property = Property(name="URI", type=StringType)
traceabilitymodel_File.attributes={traceabilitymodel_File_ID, traceabilitymodel_File_URI, traceabilitymodel_File_name}

# traceabilitymodel_Block class attributes and methods
traceabilitymodel_Block_endLine: Property = Property(name="endLine", type=StringType)
traceabilitymodel_Block_ID: Property = Property(name="ID", type=StringType)
traceabilitymodel_Block_startPos: Property = Property(name="startPos", type=StringType)
traceabilitymodel_Block_endPos: Property = Property(name="endPos", type=StringType)
traceabilitymodel_Block_protectedBlock: Property = Property(name="protectedBlock", type=BooleanType)
traceabilitymodel_Block_startLine: Property = Property(name="startLine", type=StringType)
traceabilitymodel_Block_startColumn: Property = Property(name="startColumn", type=StringType)
traceabilitymodel_Block_endColumn: Property = Property(name="endColumn", type=StringType)
traceabilitymodel_Block.attributes={traceabilitymodel_Block_startPos, traceabilitymodel_Block_endPos, traceabilitymodel_Block_startLine, traceabilitymodel_Block_endColumn, traceabilitymodel_Block_endLine, traceabilitymodel_Block_ID, traceabilitymodel_Block_startColumn, traceabilitymodel_Block_protectedBlock}

# Relationships
originatinElement2: BinaryAssociation = BinaryAssociation(
    name="originatinElement2",
    ends={
        Property(name="traceabilitymodel_ModelElementRef4", type=traceabilitymodel_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_Trace3", type=traceabilitymodel_ModelElementRef, multiplicity=Multiplicity(1, 1))
    }
)
metaModel0: BinaryAssociation = BinaryAssociation(
    name="metaModel0",
    ends={
        Property(name="traceabilitymodel_MetaModel", type=traceabilitymodel_ModelElementRef, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_ModelElementRef", type=traceabilitymodel_MetaModel, multiplicity=Multiplicity(0, 1))
    }
)
segment1: BinaryAssociation = BinaryAssociation(
    name="segment1",
    ends={
        Property(name="traceabilitymodel_TraceableSegment", type=traceabilitymodel_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_Trace", type=traceabilitymodel_TraceableSegment, multiplicity=Multiplicity(1, 1))
    }
)
trace7: BinaryAssociation = BinaryAssociation(
    name="trace7",
    ends={
        Property(name="traceabilitymodel_Trace8", type=traceabilitymodel_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_TraceModel", type=traceabilitymodel_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files9: BinaryAssociation = BinaryAssociation(
    name="files9",
    ends={
        Property(name="traceabilitymodel_File", type=traceabilitymodel_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_TraceModel10", type=traceabilitymodel_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElementRefs11: BinaryAssociation = BinaryAssociation(
    name="modelElementRefs11",
    ends={
        Property(name="traceabilitymodel_ModelElementRef13", type=traceabilitymodel_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_TraceModel12", type=traceabilitymodel_ModelElementRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaModels14: BinaryAssociation = BinaryAssociation(
    name="metaModels14",
    ends={
        Property(name="traceabilitymodel_MetaModel16", type=traceabilitymodel_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_TraceModel15", type=traceabilitymodel_MetaModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceablesegment5: BinaryAssociation = BinaryAssociation(
    name="traceablesegment5",
    ends={
        Property(name="traceabilitymodel_TraceableSegment6", type=traceabilitymodel_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_Block", type=traceabilitymodel_TraceableSegment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
blocks17: BinaryAssociation = BinaryAssociation(
    name="blocks17",
    ends={
        Property(name="traceabilitymodel_Block19", type=traceabilitymodel_File, multiplicity=Multiplicity(1, 1)),
        Property(name="traceabilitymodel_File18", type=traceabilitymodel_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="traceabilitymodel",
    types={traceabilitymodel_ModelElementRef, traceabilitymodel_MetaModel, traceabilitymodel_Trace, traceabilitymodel_TraceableSegment, traceabilitymodel_TraceModel, traceabilitymodel_File, traceabilitymodel_Block},
    associations={originatinElement2, metaModel0, segment1, trace7, files9, modelElementRefs11, metaModels14, traceablesegment5, blocks17},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)