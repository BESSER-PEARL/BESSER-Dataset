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

# Enumerations
Mode: Enumeration = Enumeration(
    name="Mode",
    literals={
            EnumerationLiteral(name="Manual"),
			EnumerationLiteral(name="Automatic")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="Transformation"),
			EnumerationLiteral(name="Annotation")
    }
)

ModelType: Enumeration = Enumeration(
    name="ModelType",
    literals={
            EnumerationLiteral(name="Source"),
			EnumerationLiteral(name="Target"),
			EnumerationLiteral(name="Both"),
			EnumerationLiteral(name="None")
    }
)

AbstractionLevel: Enumeration = Enumeration(
    name="AbstractionLevel",
    literals={
            EnumerationLiteral(name="UNSPECIFIED"),
			EnumerationLiteral(name="CIM"),
			EnumerationLiteral(name="PIM"),
			EnumerationLiteral(name="PSM"),
			EnumerationLiteral(name="PDM"),
			EnumerationLiteral(name="CODE"),
			EnumerationLiteral(name="ANNOTATION")
    }
)

Aspect: Enumeration = Enumeration(
    name="Aspect",
    literals={
            EnumerationLiteral(name="Unspecified"),
			EnumerationLiteral(name="Architecture"),
			EnumerationLiteral(name="Behaviour"),
			EnumerationLiteral(name="Content"),
			EnumerationLiteral(name="Interface"),
			EnumerationLiteral(name="Quality"),
			EnumerationLiteral(name="Semantics")
    }
)

# Classes
iTrace_Artefact = Class(name="iTrace::Artefact", is_abstract=True)
iTrace_SpecificFeature = Class(name="iTrace::SpecificFeature")
iTrace_SourceElement = Class(name="iTrace::SourceElement")
iTrace_TraceLinkElement = Class(name="iTrace::TraceLinkElement", is_abstract=True)
iTrace_Model = Class(name="iTrace::Model")
iTrace_iTraceModel = Class(name="iTrace::iTraceModel")
iTrace_TraceLink = Class(name="iTrace::TraceLink", is_abstract=True)
iTrace_Code = Class(name="iTrace::Code")
Artefact = Class(name="Artefact")
TraceLinkElement = Class(name="TraceLinkElement")
iTrace_EObject = Class(name="iTrace::EObject")
iTrace_M2MLink = Class(name="iTrace::M2MLink")
TraceLink = Class(name="TraceLink")
iTrace_TargetElement = Class(name="iTrace::TargetElement")
iTrace_M2TLink = Class(name="iTrace::M2TLink")
iTrace_Block = Class(name="iTrace::Block")
iTrace_Feature = Class(name="iTrace::Feature")

# iTrace_Artefact class attributes and methods
iTrace_Artefact_aspect: Property = Property(name="aspect", type=StringType)
iTrace_Artefact_name: Property = Property(name="name", type=StringType)
iTrace_Artefact_abstractionLevel: Property = Property(name="abstractionLevel", type=StringType)
iTrace_Artefact_path: Property = Property(name="path", type=StringType)
iTrace_Artefact.attributes={iTrace_Artefact_name, iTrace_Artefact_abstractionLevel, iTrace_Artefact_aspect, iTrace_Artefact_path}

# iTrace_SpecificFeature class attributes and methods
iTrace_SpecificFeature_groupName: Property = Property(name="groupName", type=StringType)
iTrace_SpecificFeature.attributes={iTrace_SpecificFeature_groupName}

# iTrace_SourceElement class attributes and methods

# iTrace_TraceLinkElement class attributes and methods
iTrace_TraceLinkElement_ref: Property = Property(name="ref", type=StringType)
iTrace_TraceLinkElement_name: Property = Property(name="name", type=StringType)
iTrace_TraceLinkElement_type: Property = Property(name="type", type=StringType)
iTrace_TraceLinkElement.attributes={iTrace_TraceLinkElement_type, iTrace_TraceLinkElement_name, iTrace_TraceLinkElement_ref}

# iTrace_Model class attributes and methods
iTrace_Model_metamodel: Property = Property(name="metamodel", type=StringType)
iTrace_Model_m_getModelType: Method = Method(name="getModelType", parameters={}, type=StringType)
iTrace_Model.attributes={iTrace_Model_metamodel}
iTrace_Model.methods={iTrace_Model_m_getModelType}

# iTrace_iTraceModel class attributes and methods
iTrace_iTraceModel_version: Property = Property(name="version", type=StringType)
iTrace_iTraceModel_projectName: Property = Property(name="projectName", type=StringType)
iTrace_iTraceModel.attributes={iTrace_iTraceModel_version, iTrace_iTraceModel_projectName}

# iTrace_TraceLink class attributes and methods
iTrace_TraceLink_createdOn: Property = Property(name="createdOn", type=StringType)
iTrace_TraceLink_type: Property = Property(name="type", type=StringType)
iTrace_TraceLink_fromFileName: Property = Property(name="fromFileName", type=StringType)
iTrace_TraceLink_comment: Property = Property(name="comment", type=StringType)
iTrace_TraceLink_createdBy: Property = Property(name="createdBy", type=StringType)
iTrace_TraceLink_mode: Property = Property(name="mode", type=StringType)
iTrace_TraceLink_technicalBinding: Property = Property(name="technicalBinding", type=StringType)
iTrace_TraceLink_ruleName: Property = Property(name="ruleName", type=StringType)
iTrace_TraceLink.attributes={iTrace_TraceLink_ruleName, iTrace_TraceLink_mode, iTrace_TraceLink_createdOn, iTrace_TraceLink_createdBy, iTrace_TraceLink_comment, iTrace_TraceLink_technicalBinding, iTrace_TraceLink_type, iTrace_TraceLink_fromFileName}

# iTrace_Code class attributes and methods

# Artefact class attributes and methods

# TraceLinkElement class attributes and methods

# iTrace_EObject class attributes and methods

# iTrace_M2MLink class attributes and methods

# TraceLink class attributes and methods

# iTrace_TargetElement class attributes and methods

# iTrace_M2TLink class attributes and methods

# iTrace_Block class attributes and methods
iTrace_Block_blockNumber: Property = Property(name="blockNumber", type=IntegerType)
iTrace_Block_startLine: Property = Property(name="startLine", type=IntegerType)
iTrace_Block_endLine: Property = Property(name="endLine", type=IntegerType)
iTrace_Block_startColumn: Property = Property(name="startColumn", type=IntegerType)
iTrace_Block_endColumn: Property = Property(name="endColumn", type=IntegerType)
iTrace_Block.attributes={iTrace_Block_endLine, iTrace_Block_endColumn, iTrace_Block_blockNumber, iTrace_Block_startLine, iTrace_Block_startColumn}

# iTrace_Feature class attributes and methods
iTrace_Feature_attribute: Property = Property(name="attribute", type=StringType)
iTrace_Feature_value: Property = Property(name="value", type=StringType)
iTrace_Feature.attributes={iTrace_Feature_attribute, iTrace_Feature_value}

# Relationships
traceLinks0: BinaryAssociation = BinaryAssociation(
    name="traceLinks0",
    ends={
        Property(name="TraceLink", type=iTrace_iTraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="iTraceModel", type=iTrace_TraceLink, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
artefacts1: BinaryAssociation = BinaryAssociation(
    name="artefacts1",
    ends={
        Property(name="Artefact", type=iTrace_iTraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="iTraceModel2", type=iTrace_Artefact, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
specificFeatures3: BinaryAssociation = BinaryAssociation(
    name="specificFeatures3",
    ends={
        Property(name="SpecificFeature", type=iTrace_iTraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="iTraceModel4", type=iTrace_SpecificFeature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceElements5: BinaryAssociation = BinaryAssociation(
    name="sourceElements5",
    ends={
        Property(name="SourceElement", type=iTrace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="traceLink", type=iTrace_SourceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iTraceModel6: BinaryAssociation = BinaryAssociation(
    name="iTraceModel6",
    ends={
        Property(name="iTraceModel7", type=iTrace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="traceLinks", type=iTrace_iTraceModel, multiplicity=Multiplicity(1, 1))
    }
)
model8: BinaryAssociation = BinaryAssociation(
    name="model8",
    ends={
        Property(name="Model", type=iTrace_TraceLinkElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=iTrace_Model, multiplicity=Multiplicity(1, 1))
    }
)
iTraceModel14: BinaryAssociation = BinaryAssociation(
    name="iTraceModel14",
    ends={
        Property(name="iTraceModel15", type=iTrace_Artefact, multiplicity=Multiplicity(1, 1)),
        Property(name="artefacts", type=iTrace_iTraceModel, multiplicity=Multiplicity(1, 1))
    }
)
blocks16: BinaryAssociation = BinaryAssociation(
    name="blocks16",
    ends={
        Property(name="Block17", type=iTrace_Code, multiplicity=Multiplicity(1, 1)),
        Property(name="code", type=iTrace_Block, multiplicity=Multiplicity(0, 9999))
    }
)
code18: BinaryAssociation = BinaryAssociation(
    name="code18",
    ends={
        Property(name="Code", type=iTrace_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="blocks", type=iTrace_Code, multiplicity=Multiplicity(1, 1))
    }
)
traceLink19: BinaryAssociation = BinaryAssociation(
    name="traceLink19",
    ends={
        Property(name="M2TLink", type=iTrace_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="targetBlocks", type=iTrace_M2TLink, multiplicity=Multiplicity(1, 1))
    }
)
elements20: BinaryAssociation = BinaryAssociation(
    name="elements20",
    ends={
        Property(name="TraceLinkElement", type=iTrace_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=iTrace_TraceLinkElement, multiplicity=Multiplicity(0, 9999))
    }
)
traceLink21: BinaryAssociation = BinaryAssociation(
    name="traceLink21",
    ends={
        Property(name="TraceLink22", type=iTrace_SourceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceElements", type=iTrace_TraceLink, multiplicity=Multiplicity(1, 1))
    }
)
object9: BinaryAssociation = BinaryAssociation(
    name="object9",
    ends={
        Property(name="iTrace_EObject", type=iTrace_TraceLinkElement, multiplicity=Multiplicity(1, 1)),
        Property(name="iTrace_TraceLinkElement", type=iTrace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
targetElements10: BinaryAssociation = BinaryAssociation(
    name="targetElements10",
    ends={
        Property(name="TargetElement", type=iTrace_M2MLink, multiplicity=Multiplicity(1, 1)),
        Property(name="traceLink11", type=iTrace_TargetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetBlocks12: BinaryAssociation = BinaryAssociation(
    name="targetBlocks12",
    ends={
        Property(name="Block", type=iTrace_M2TLink, multiplicity=Multiplicity(1, 1)),
        Property(name="traceLink13", type=iTrace_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificFeature24: BinaryAssociation = BinaryAssociation(
    name="specificFeature24",
    ends={
        Property(name="SpecificFeature25", type=iTrace_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=iTrace_SpecificFeature, multiplicity=Multiplicity(1, 1))
    }
)
features26: BinaryAssociation = BinaryAssociation(
    name="features26",
    ends={
        Property(name="Feature", type=iTrace_SpecificFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specificFeature", type=iTrace_Feature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
iTraceModel27: BinaryAssociation = BinaryAssociation(
    name="iTraceModel27",
    ends={
        Property(name="iTraceModel28", type=iTrace_SpecificFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specificFeatures", type=iTrace_iTraceModel, multiplicity=Multiplicity(1, 1))
    }
)
traceLink23: BinaryAssociation = BinaryAssociation(
    name="traceLink23",
    ends={
        Property(name="M2MLink", type=iTrace_TargetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="targetElements", type=iTrace_M2MLink, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_iTrace_Code_Artefact = Generalization(general=Artefact, specific=iTrace_Code)
gen_iTrace_Model_Artefact = Generalization(general=Artefact, specific=iTrace_Model)
gen_iTrace_SourceElement_TraceLinkElement = Generalization(general=TraceLinkElement, specific=iTrace_SourceElement)
gen_iTrace_M2MLink_TraceLink = Generalization(general=TraceLink, specific=iTrace_M2MLink)
gen_iTrace_M2TLink_TraceLink = Generalization(general=TraceLink, specific=iTrace_M2TLink)
gen_iTrace_TargetElement_TraceLinkElement = Generalization(general=TraceLinkElement, specific=iTrace_TargetElement)

# Domain Model
domain_model = DomainModel(
    name="iTrace",
    types={iTrace_Artefact, iTrace_SpecificFeature, iTrace_SourceElement, iTrace_TraceLinkElement, iTrace_Model, iTrace_iTraceModel, iTrace_TraceLink, iTrace_Code, Artefact, TraceLinkElement, iTrace_EObject, iTrace_M2MLink, TraceLink, iTrace_TargetElement, iTrace_M2TLink, iTrace_Block, iTrace_Feature, Mode, Type, ModelType, AbstractionLevel, Aspect},
    associations={traceLinks0, artefacts1, specificFeatures3, sourceElements5, iTraceModel6, model8, iTraceModel14, blocks16, code18, traceLink19, elements20, traceLink21, object9, targetElements10, targetBlocks12, specificFeature24, features26, iTraceModel27, traceLink23},
    generalizations={gen_iTrace_Code_Artefact, gen_iTrace_Model_Artefact, gen_iTrace_SourceElement_TraceLinkElement, gen_iTrace_M2MLink_TraceLink, gen_iTrace_M2TLink_TraceLink, gen_iTrace_TargetElement_TraceLinkElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)