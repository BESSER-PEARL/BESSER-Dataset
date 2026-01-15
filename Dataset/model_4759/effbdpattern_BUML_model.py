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
FunctionDomain: Enumeration = Enumeration(
    name="FunctionDomain",
    literals={
            EnumerationLiteral(name="time"),
			EnumerationLiteral(name="space"),
			EnumerationLiteral(name="form")
    }
)

# Classes
effbdpattern_Flow = Class(name="effbdpattern::Flow")
effbdpattern_OutputPort = Class(name="effbdpattern::OutputPort")
effbdpattern_InputPort = Class(name="effbdpattern::InputPort")
effbdpattern_Description = Class(name="effbdpattern::Description")
effbdpattern_Token = Class(name="effbdpattern::Token")
effbdpattern_FunctionProperty = Class(name="effbdpattern::FunctionProperty")
effbdpattern_Function = Class(name="effbdpattern::Function")
SequenceNode = Class(name="SequenceNode")
ModelElement = Class(name="ModelElement")
effbdpattern_Sequence = Class(name="effbdpattern::Sequence", is_abstract=True)
effbdpattern_Final = Class(name="effbdpattern::Final")
effbdpattern_SequenceNode = Class(name="effbdpattern::SequenceNode", is_abstract=True)
effbdpattern_And = Class(name="effbdpattern::And")
Sequence = Class(name="Sequence")
effbdpattern_Or = Class(name="effbdpattern::Or")
effbdpattern_Start = Class(name="effbdpattern::Start")
effbdpattern_Item = Class(name="effbdpattern::Item")
effbdpattern_Loop = Class(name="effbdpattern::Loop")
Port = Class(name="Port")
effbdpattern_Port = Class(name="effbdpattern::Port", is_abstract=True)
effbdpattern_PatternCatalog = Class(name="effbdpattern::PatternCatalog")
effbdpattern_LoopExit = Class(name="effbdpattern::LoopExit")
effbdpattern_Iteration = Class(name="effbdpattern::Iteration")
effbdpattern_Indexable = Class(name="effbdpattern::Indexable", is_abstract=True)
effbdpattern_SystemPattern = Class(name="effbdpattern::SystemPattern")
effbdpattern_Workbench = Class(name="effbdpattern::Workbench")
effbdpattern_Problem = Class(name="effbdpattern::Problem")
effbdpattern_Domain = Class(name="effbdpattern::Domain")
effbdpattern_Keyword = Class(name="effbdpattern::Keyword")
effbdpattern_Feature = Class(name="effbdpattern::Feature")
effbdpattern_Condition = Class(name="effbdpattern::Condition")
effbdpattern_Context = Class(name="effbdpattern::Context")
effbdpattern_Model = Class(name="effbdpattern::Model")
effbdpattern_Allocation = Class(name="effbdpattern::Allocation")
effbdpattern_ModelElement = Class(name="effbdpattern::ModelElement", is_abstract=True)
Indexable = Class(name="Indexable")
effbdpattern_AbstractModel = Class(name="effbdpattern::AbstractModel", is_abstract=True)
effbdpattern_Parameter = Class(name="effbdpattern::Parameter")
effbdpattern_PatternModel = Class(name="effbdpattern::PatternModel")
AbstractModel = Class(name="AbstractModel")
effbdpattern_Component = Class(name="effbdpattern::Component")
effbdpattern_Impact = Class(name="effbdpattern::Impact")
effbdpattern_Force = Class(name="effbdpattern::Force")

# effbdpattern_Flow class attributes and methods
effbdpattern_Flow_flowName: Property = Property(name="flowName", type=StringType)
effbdpattern_Flow.attributes={effbdpattern_Flow_flowName}

# effbdpattern_OutputPort class attributes and methods

# effbdpattern_InputPort class attributes and methods

# effbdpattern_Description class attributes and methods
effbdpattern_Description_content: Property = Property(name="content", type=StringType)
effbdpattern_Description.attributes={effbdpattern_Description_content}

# effbdpattern_Token class attributes and methods

# effbdpattern_FunctionProperty class attributes and methods
effbdpattern_FunctionProperty_description: Property = Property(name="description", type=StringType)
effbdpattern_FunctionProperty.attributes={effbdpattern_FunctionProperty_description}

# effbdpattern_Function class attributes and methods
effbdpattern_Function_domain: Property = Property(name="domain", type=StringType)
effbdpattern_Function.attributes={effbdpattern_Function_domain}

# SequenceNode class attributes and methods

# ModelElement class attributes and methods

# effbdpattern_Sequence class attributes and methods

# effbdpattern_Final class attributes and methods

# effbdpattern_SequenceNode class attributes and methods
effbdpattern_SequenceNode_name: Property = Property(name="name", type=StringType)
effbdpattern_SequenceNode_tMin: Property = Property(name="tMin", type=IntegerType)
effbdpattern_SequenceNode_tMax: Property = Property(name="tMax", type=IntegerType)
effbdpattern_SequenceNode.attributes={effbdpattern_SequenceNode_name, effbdpattern_SequenceNode_tMax, effbdpattern_SequenceNode_tMin}

# effbdpattern_And class attributes and methods

# Sequence class attributes and methods

# effbdpattern_Or class attributes and methods

# effbdpattern_Start class attributes and methods

# effbdpattern_Item class attributes and methods
effbdpattern_Item_name: Property = Property(name="name", type=StringType)
effbdpattern_Item.attributes={effbdpattern_Item_name}

# effbdpattern_Loop class attributes and methods

# Port class attributes and methods

# effbdpattern_Port class attributes and methods
effbdpattern_Port_id: Property = Property(name="id", type=StringType)
effbdpattern_Port.attributes={effbdpattern_Port_id}

# effbdpattern_PatternCatalog class attributes and methods
effbdpattern_PatternCatalog_id: Property = Property(name="id", type=StringType)
effbdpattern_PatternCatalog.attributes={effbdpattern_PatternCatalog_id}

# effbdpattern_LoopExit class attributes and methods

# effbdpattern_Iteration class attributes and methods

# effbdpattern_Indexable class attributes and methods

# effbdpattern_SystemPattern class attributes and methods
effbdpattern_SystemPattern_patternId: Property = Property(name="patternId", type=IntegerType)
effbdpattern_SystemPattern_name: Property = Property(name="name", type=StringType)
effbdpattern_SystemPattern_alias: Property = Property(name="alias", type=StringType)
effbdpattern_SystemPattern_challeng: Property = Property(name="challeng", type=StringType)
effbdpattern_SystemPattern_description: Property = Property(name="description", type=StringType)
effbdpattern_SystemPattern_creationDate: Property = Property(name="creationDate", type=DateType)
effbdpattern_SystemPattern_knownApplications: Property = Property(name="knownApplications", type=StringType)
effbdpattern_SystemPattern.attributes={effbdpattern_SystemPattern_name, effbdpattern_SystemPattern_challeng, effbdpattern_SystemPattern_description, effbdpattern_SystemPattern_patternId, effbdpattern_SystemPattern_creationDate, effbdpattern_SystemPattern_alias, effbdpattern_SystemPattern_knownApplications}

# effbdpattern_Workbench class attributes and methods

# effbdpattern_Problem class attributes and methods
effbdpattern_Problem_name: Property = Property(name="name", type=StringType)
effbdpattern_Problem_description: Property = Property(name="description", type=StringType)
effbdpattern_Problem.attributes={effbdpattern_Problem_description, effbdpattern_Problem_name}

# effbdpattern_Domain class attributes and methods
effbdpattern_Domain_name: Property = Property(name="name", type=StringType)
effbdpattern_Domain_description: Property = Property(name="description", type=StringType)
effbdpattern_Domain.attributes={effbdpattern_Domain_name, effbdpattern_Domain_description}

# effbdpattern_Keyword class attributes and methods
effbdpattern_Keyword_value: Property = Property(name="value", type=StringType)
effbdpattern_Keyword.attributes={effbdpattern_Keyword_value}

# effbdpattern_Feature class attributes and methods
effbdpattern_Feature_name: Property = Property(name="name", type=StringType)
effbdpattern_Feature_description: Property = Property(name="description", type=StringType)
effbdpattern_Feature.attributes={effbdpattern_Feature_description, effbdpattern_Feature_name}

# effbdpattern_Condition class attributes and methods
effbdpattern_Condition_name: Property = Property(name="name", type=StringType)
effbdpattern_Condition.attributes={effbdpattern_Condition_name}

# effbdpattern_Context class attributes and methods
effbdpattern_Context_description: Property = Property(name="description", type=StringType)
effbdpattern_Context.attributes={effbdpattern_Context_description}

# effbdpattern_Model class attributes and methods

# effbdpattern_Allocation class attributes and methods
effbdpattern_Allocation_id: Property = Property(name="id", type=StringType)
effbdpattern_Allocation_redundant: Property = Property(name="redundant", type=BooleanType)
effbdpattern_Allocation.attributes={effbdpattern_Allocation_id, effbdpattern_Allocation_redundant}

# effbdpattern_ModelElement class attributes and methods
effbdpattern_ModelElement_modelId: Property = Property(name="modelId", type=IntegerType)
effbdpattern_ModelElement_modelName: Property = Property(name="modelName", type=StringType)
effbdpattern_ModelElement.attributes={effbdpattern_ModelElement_modelId, effbdpattern_ModelElement_modelName}

# Indexable class attributes and methods

# effbdpattern_AbstractModel class attributes and methods
effbdpattern_AbstractModel_name: Property = Property(name="name", type=StringType)
effbdpattern_AbstractModel_version: Property = Property(name="version", type=StringType)
effbdpattern_AbstractModel.attributes={effbdpattern_AbstractModel_name, effbdpattern_AbstractModel_version}

# effbdpattern_Parameter class attributes and methods
effbdpattern_Parameter_name: Property = Property(name="name", type=StringType)
effbdpattern_Parameter.attributes={effbdpattern_Parameter_name}

# effbdpattern_PatternModel class attributes and methods

# AbstractModel class attributes and methods

# effbdpattern_Component class attributes and methods

# effbdpattern_Impact class attributes and methods
effbdpattern_Impact_value: Property = Property(name="value", type=IntegerType)
effbdpattern_Impact_scale: Property = Property(name="scale", type=IntegerType)
effbdpattern_Impact.attributes={effbdpattern_Impact_scale, effbdpattern_Impact_value}

# effbdpattern_Force class attributes and methods
effbdpattern_Force_value: Property = Property(name="value", type=IntegerType)
effbdpattern_Force_scale: Property = Property(name="scale", type=IntegerType)
effbdpattern_Force_description: Property = Property(name="description", type=StringType)
effbdpattern_Force.attributes={effbdpattern_Force_scale, effbdpattern_Force_value, effbdpattern_Force_description}

# Relationships
flows3: BinaryAssociation = BinaryAssociation(
    name="flows3",
    ends={
        Property(name="effbdpattern_Flow", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function4", type=effbdpattern_Flow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputPorts5: BinaryAssociation = BinaryAssociation(
    name="outputPorts5",
    ends={
        Property(name="effbdpattern_OutputPort", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function6", type=effbdpattern_OutputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts7: BinaryAssociation = BinaryAssociation(
    name="inputPorts7",
    ends={
        Property(name="effbdpattern_InputPort", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function8", type=effbdpattern_InputPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptions9: BinaryAssociation = BinaryAssociation(
    name="descriptions9",
    ends={
        Property(name="effbdpattern_Description", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function10", type=effbdpattern_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens11: BinaryAssociation = BinaryAssociation(
    name="tokens11",
    ends={
        Property(name="effbdpattern_Token", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function12", type=effbdpattern_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property13: BinaryAssociation = BinaryAssociation(
    name="property13",
    ends={
        Property(name="effbdpattern_FunctionProperty", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function14", type=effbdpattern_FunctionProperty, multiplicity=Multiplicity(0, 9999))
    }
)
parent16: BinaryAssociation = BinaryAssociation(
    name="parent16",
    ends={
        Property(name="Function17", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="decompositions", type=effbdpattern_Function, multiplicity=Multiplicity(0, 1))
    }
)
decompositions1: BinaryAssociation = BinaryAssociation(
    name="decompositions1",
    ends={
        Property(name="Function", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=effbdpattern_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceNodes2: BinaryAssociation = BinaryAssociation(
    name="sequenceNodes2",
    ends={
        Property(name="effbdpattern_Sequence", type=effbdpattern_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Function", type=effbdpattern_Sequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlFlowEdge19: BinaryAssociation = BinaryAssociation(
    name="controlFlowEdge19",
    ends={
        Property(name="effbdpattern_SequenceNode", type=effbdpattern_SequenceNode, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SequenceNode18", type=effbdpattern_SequenceNode, multiplicity=Multiplicity(0, 9999))
    }
)
delegate21: BinaryAssociation = BinaryAssociation(
    name="delegate21",
    ends={
        Property(name="effbdpattern_Port", type=effbdpattern_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Port20", type=effbdpattern_Port, multiplicity=Multiplicity(0, 1))
    }
)
parent31: BinaryAssociation = BinaryAssociation(
    name="parent31",
    ends={
        Property(name="effbdpattern_FunctionProperty32", type=effbdpattern_FunctionProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_FunctionProperty30", type=effbdpattern_FunctionProperty, multiplicity=Multiplicity(0, 1))
    }
)
patterns33: BinaryAssociation = BinaryAssociation(
    name="patterns33",
    ends={
        Property(name="effbdpattern_Function34", type=effbdpattern_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_PatternCatalog", type=effbdpattern_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputflowEdge22: BinaryAssociation = BinaryAssociation(
    name="inputflowEdge22",
    ends={
        Property(name="effbdpattern_InputPort24", type=effbdpattern_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Flow23", type=effbdpattern_InputPort, multiplicity=Multiplicity(0, 9999))
    }
)
items25: BinaryAssociation = BinaryAssociation(
    name="items25",
    ends={
        Property(name="effbdpattern_Item", type=effbdpattern_Flow, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Flow26", type=effbdpattern_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputflowEdge27: BinaryAssociation = BinaryAssociation(
    name="outputflowEdge27",
    ends={
        Property(name="effbdpattern_Flow29", type=effbdpattern_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_OutputPort28", type=effbdpattern_Flow, multiplicity=Multiplicity(0, 9999))
    }
)
pattern58: BinaryAssociation = BinaryAssociation(
    name="pattern58",
    ends={
        Property(name="SystemPattern", type=effbdpattern_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="modelElement", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 1))
    }
)
systemPatterns35: BinaryAssociation = BinaryAssociation(
    name="systemPatterns35",
    ends={
        Property(name="effbdpattern_SystemPattern", type=effbdpattern_PatternCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_PatternCatalog36", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionProperties37: BinaryAssociation = BinaryAssociation(
    name="functionProperties37",
    ends={
        Property(name="effbdpattern_FunctionProperty38", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench", type=effbdpattern_FunctionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
problems39: BinaryAssociation = BinaryAssociation(
    name="problems39",
    ends={
        Property(name="effbdpattern_Problem", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench40", type=effbdpattern_Problem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains41: BinaryAssociation = BinaryAssociation(
    name="domains41",
    ends={
        Property(name="effbdpattern_Domain", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench42", type=effbdpattern_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keywords43: BinaryAssociation = BinaryAssociation(
    name="keywords43",
    ends={
        Property(name="effbdpattern_Keyword", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench44", type=effbdpattern_Keyword, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features45: BinaryAssociation = BinaryAssociation(
    name="features45",
    ends={
        Property(name="effbdpattern_Feature", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench46", type=effbdpattern_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions47: BinaryAssociation = BinaryAssociation(
    name="conditions47",
    ends={
        Property(name="effbdpattern_Condition", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench48", type=effbdpattern_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contexts49: BinaryAssociation = BinaryAssociation(
    name="contexts49",
    ends={
        Property(name="effbdpattern_Context", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench50", type=effbdpattern_Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
workingModels51: BinaryAssociation = BinaryAssociation(
    name="workingModels51",
    ends={
        Property(name="effbdpattern_Model", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench52", type=effbdpattern_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patternCatalog53: BinaryAssociation = BinaryAssociation(
    name="patternCatalog53",
    ends={
        Property(name="effbdpattern_PatternCatalog55", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench54", type=effbdpattern_PatternCatalog, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allocations56: BinaryAssociation = BinaryAssociation(
    name="allocations56",
    ends={
        Property(name="effbdpattern_Allocation", type=effbdpattern_Workbench, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Workbench57", type=effbdpattern_Allocation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalPattern70: BinaryAssociation = BinaryAssociation(
    name="physicalPattern70",
    ends={
        Property(name="effbdpattern_Component", type=effbdpattern_PatternModel, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_PatternModel71", type=effbdpattern_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decompositions73: BinaryAssociation = BinaryAssociation(
    name="decompositions73",
    ends={
        Property(name="Component", type=effbdpattern_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="parent74", type=effbdpattern_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent76: BinaryAssociation = BinaryAssociation(
    name="parent76",
    ends={
        Property(name="Component78", type=effbdpattern_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="decompositions77", type=effbdpattern_Component, multiplicity=Multiplicity(0, 1))
    }
)
keywords59: BinaryAssociation = BinaryAssociation(
    name="keywords59",
    ends={
        Property(name="effbdpattern_Keyword60", type=effbdpattern_Indexable, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Indexable", type=effbdpattern_Keyword, multiplicity=Multiplicity(0, 9999))
    }
)
patternRole61: BinaryAssociation = BinaryAssociation(
    name="patternRole61",
    ends={
        Property(name="effbdpattern_ModelElement", type=effbdpattern_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Parameter", type=effbdpattern_ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
concreteRole62: BinaryAssociation = BinaryAssociation(
    name="concreteRole62",
    ends={
        Property(name="effbdpattern_ModelElement64", type=effbdpattern_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Parameter63", type=effbdpattern_ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
conditions65: BinaryAssociation = BinaryAssociation(
    name="conditions65",
    ends={
        Property(name="effbdpattern_Condition67", type=effbdpattern_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Context66", type=effbdpattern_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
functionalPattern68: BinaryAssociation = BinaryAssociation(
    name="functionalPattern68",
    ends={
        Property(name="effbdpattern_Function69", type=effbdpattern_PatternModel, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_PatternModel", type=effbdpattern_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
useCasesBeforePattern90: BinaryAssociation = BinaryAssociation(
    name="useCasesBeforePattern90",
    ends={
        Property(name="effbdpattern_PatternModel92", type=effbdpattern_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Problem91", type=effbdpattern_PatternModel, multiplicity=Multiplicity(0, 9999))
    }
)
featuresToOptimize93: BinaryAssociation = BinaryAssociation(
    name="featuresToOptimize93",
    ends={
        Property(name="effbdpattern_Feature95", type=effbdpattern_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Problem94", type=effbdpattern_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
forces96: BinaryAssociation = BinaryAssociation(
    name="forces96",
    ends={
        Property(name="Force", type=effbdpattern_Problem, multiplicity=Multiplicity(1, 1)),
        Property(name="problem", type=effbdpattern_Force, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature97: BinaryAssociation = BinaryAssociation(
    name="feature97",
    ends={
        Property(name="effbdpattern_Feature98", type=effbdpattern_Impact, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Impact", type=effbdpattern_Feature, multiplicity=Multiplicity(0, 1))
    }
)
pattern99: BinaryAssociation = BinaryAssociation(
    name="pattern99",
    ends={
        Property(name="SystemPattern100", type=effbdpattern_Impact, multiplicity=Multiplicity(1, 1)),
        Property(name="impacts", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 1))
    }
)
domain79: BinaryAssociation = BinaryAssociation(
    name="domain79",
    ends={
        Property(name="effbdpattern_Domain80", type=effbdpattern_AbstractModel, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_AbstractModel", type=effbdpattern_Domain, multiplicity=Multiplicity(0, 1))
    }
)
parent82: BinaryAssociation = BinaryAssociation(
    name="parent82",
    ends={
        Property(name="AbstractModel", type=effbdpattern_AbstractModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=effbdpattern_AbstractModel, multiplicity=Multiplicity(0, 1))
    }
)
fragments84: BinaryAssociation = BinaryAssociation(
    name="fragments84",
    ends={
        Property(name="AbstractModel86", type=effbdpattern_AbstractModel, multiplicity=Multiplicity(1, 1)),
        Property(name="parent85", type=effbdpattern_AbstractModel, multiplicity=Multiplicity(0, 9999))
    }
)
parameters101: BinaryAssociation = BinaryAssociation(
    name="parameters101",
    ends={
        Property(name="effbdpattern_Parameter103", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern102", type=effbdpattern_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context104: BinaryAssociation = BinaryAssociation(
    name="context104",
    ends={
        Property(name="effbdpattern_Context106", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern105", type=effbdpattern_Context, multiplicity=Multiplicity(0, 1))
    }
)
problem107: BinaryAssociation = BinaryAssociation(
    name="problem107",
    ends={
        Property(name="effbdpattern_Problem109", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern108", type=effbdpattern_Problem, multiplicity=Multiplicity(0, 1))
    }
)
domain110: BinaryAssociation = BinaryAssociation(
    name="domain110",
    ends={
        Property(name="effbdpattern_Domain112", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern111", type=effbdpattern_Domain, multiplicity=Multiplicity(0, 1))
    }
)
antiPatterns114: BinaryAssociation = BinaryAssociation(
    name="antiPatterns114",
    ends={
        Property(name="effbdpattern_SystemPattern115", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern113", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 9999))
    }
)
problem87: BinaryAssociation = BinaryAssociation(
    name="problem87",
    ends={
        Property(name="Problem", type=effbdpattern_Force, multiplicity=Multiplicity(1, 1)),
        Property(name="forces", type=effbdpattern_Problem, multiplicity=Multiplicity(0, 1))
    }
)
condition88: BinaryAssociation = BinaryAssociation(
    name="condition88",
    ends={
        Property(name="effbdpattern_Condition89", type=effbdpattern_Force, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Force", type=effbdpattern_Condition, multiplicity=Multiplicity(0, 1))
    }
)
patternModel125: BinaryAssociation = BinaryAssociation(
    name="patternModel125",
    ends={
        Property(name="effbdpattern_PatternModel127", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern126", type=effbdpattern_PatternModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
impacts128: BinaryAssociation = BinaryAssociation(
    name="impacts128",
    ends={
        Property(name="Impact", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=effbdpattern_Impact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElement129: BinaryAssociation = BinaryAssociation(
    name="modelElement129",
    ends={
        Property(name="ModelElement", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern130", type=effbdpattern_ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
versionBeforePattern132: BinaryAssociation = BinaryAssociation(
    name="versionBeforePattern132",
    ends={
        Property(name="effbdpattern_Model133", type=effbdpattern_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Model131", type=effbdpattern_Model, multiplicity=Multiplicity(0, 1))
    }
)
functionalArchitecture134: BinaryAssociation = BinaryAssociation(
    name="functionalArchitecture134",
    ends={
        Property(name="effbdpattern_Function136", type=effbdpattern_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Model135", type=effbdpattern_Function, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
physicalArchitecture137: BinaryAssociation = BinaryAssociation(
    name="physicalArchitecture137",
    ends={
        Property(name="effbdpattern_Component139", type=effbdpattern_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Model138", type=effbdpattern_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fromFunction140: BinaryAssociation = BinaryAssociation(
    name="fromFunction140",
    ends={
        Property(name="effbdpattern_Function142", type=effbdpattern_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Allocation141", type=effbdpattern_Function, multiplicity=Multiplicity(0, 1))
    }
)
toComponent143: BinaryAssociation = BinaryAssociation(
    name="toComponent143",
    ends={
        Property(name="effbdpattern_Component145", type=effbdpattern_Allocation, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_Allocation144", type=effbdpattern_Component, multiplicity=Multiplicity(0, 1))
    }
)
requestedPatterns117: BinaryAssociation = BinaryAssociation(
    name="requestedPatterns117",
    ends={
        Property(name="effbdpattern_SystemPattern118", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern116", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 9999))
    }
)
relatedPatterns120: BinaryAssociation = BinaryAssociation(
    name="relatedPatterns120",
    ends={
        Property(name="effbdpattern_SystemPattern121", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern119", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 9999))
    }
)
equivalentPatterns123: BinaryAssociation = BinaryAssociation(
    name="equivalentPatterns123",
    ends={
        Property(name="effbdpattern_SystemPattern124", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="effbdpattern_SystemPattern122", type=effbdpattern_SystemPattern, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_effbdpattern_Function_SequenceNode = Generalization(general=SequenceNode, specific=effbdpattern_Function)
gen_effbdpattern_Function_ModelElement = Generalization(general=ModelElement, specific=effbdpattern_Function)
gen_effbdpattern_Final_Sequence = Generalization(general=Sequence, specific=effbdpattern_Final)
gen_effbdpattern_Sequence_SequenceNode = Generalization(general=SequenceNode, specific=effbdpattern_Sequence)
gen_effbdpattern_And_Sequence = Generalization(general=Sequence, specific=effbdpattern_And)
gen_effbdpattern_Or_Sequence = Generalization(general=Sequence, specific=effbdpattern_Or)
gen_effbdpattern_Start_Sequence = Generalization(general=Sequence, specific=effbdpattern_Start)
gen_effbdpattern_Loop_Sequence = Generalization(general=Sequence, specific=effbdpattern_Loop)
gen_effbdpattern_InputPort_Port = Generalization(general=Port, specific=effbdpattern_InputPort)
gen_effbdpattern_OutputPort_Port = Generalization(general=Port, specific=effbdpattern_OutputPort)
gen_effbdpattern_LoopExit_Sequence = Generalization(general=Sequence, specific=effbdpattern_LoopExit)
gen_effbdpattern_Iteration_Sequence = Generalization(general=Sequence, specific=effbdpattern_Iteration)
gen_effbdpattern_ModelElement_Indexable = Generalization(general=Indexable, specific=effbdpattern_ModelElement)
gen_effbdpattern_Component_ModelElement = Generalization(general=ModelElement, specific=effbdpattern_Component)
gen_effbdpattern_Domain_Indexable = Generalization(general=Indexable, specific=effbdpattern_Domain)
gen_effbdpattern_AbstractModel_Indexable = Generalization(general=Indexable, specific=effbdpattern_AbstractModel)
gen_effbdpattern_Context_Indexable = Generalization(general=Indexable, specific=effbdpattern_Context)
gen_effbdpattern_PatternModel_AbstractModel = Generalization(general=AbstractModel, specific=effbdpattern_PatternModel)
gen_effbdpattern_SystemPattern_Indexable = Generalization(general=Indexable, specific=effbdpattern_SystemPattern)
gen_effbdpattern_Problem_Indexable = Generalization(general=Indexable, specific=effbdpattern_Problem)
gen_effbdpattern_Model_AbstractModel = Generalization(general=AbstractModel, specific=effbdpattern_Model)

# Domain Model
domain_model = DomainModel(
    name="effbdpattern",
    types={effbdpattern_Flow, effbdpattern_OutputPort, effbdpattern_InputPort, effbdpattern_Description, effbdpattern_Token, effbdpattern_FunctionProperty, effbdpattern_Function, SequenceNode, ModelElement, effbdpattern_Sequence, effbdpattern_Final, effbdpattern_SequenceNode, effbdpattern_And, Sequence, effbdpattern_Or, effbdpattern_Start, effbdpattern_Item, effbdpattern_Loop, Port, effbdpattern_Port, effbdpattern_PatternCatalog, effbdpattern_LoopExit, effbdpattern_Iteration, effbdpattern_Indexable, effbdpattern_SystemPattern, effbdpattern_Workbench, effbdpattern_Problem, effbdpattern_Domain, effbdpattern_Keyword, effbdpattern_Feature, effbdpattern_Condition, effbdpattern_Context, effbdpattern_Model, effbdpattern_Allocation, effbdpattern_ModelElement, Indexable, effbdpattern_AbstractModel, effbdpattern_Parameter, effbdpattern_PatternModel, AbstractModel, effbdpattern_Component, effbdpattern_Impact, effbdpattern_Force, FunctionDomain},
    associations={flows3, outputPorts5, inputPorts7, descriptions9, tokens11, property13, parent16, decompositions1, sequenceNodes2, controlFlowEdge19, delegate21, parent31, patterns33, inputflowEdge22, items25, outputflowEdge27, pattern58, systemPatterns35, functionProperties37, problems39, domains41, keywords43, features45, conditions47, contexts49, workingModels51, patternCatalog53, allocations56, physicalPattern70, decompositions73, parent76, keywords59, patternRole61, concreteRole62, conditions65, functionalPattern68, useCasesBeforePattern90, featuresToOptimize93, forces96, feature97, pattern99, domain79, parent82, fragments84, parameters101, context104, problem107, domain110, antiPatterns114, problem87, condition88, patternModel125, impacts128, modelElement129, versionBeforePattern132, functionalArchitecture134, physicalArchitecture137, fromFunction140, toComponent143, requestedPatterns117, relatedPatterns120, equivalentPatterns123},
    generalizations={gen_effbdpattern_Function_SequenceNode, gen_effbdpattern_Function_ModelElement, gen_effbdpattern_Final_Sequence, gen_effbdpattern_Sequence_SequenceNode, gen_effbdpattern_And_Sequence, gen_effbdpattern_Or_Sequence, gen_effbdpattern_Start_Sequence, gen_effbdpattern_Loop_Sequence, gen_effbdpattern_InputPort_Port, gen_effbdpattern_OutputPort_Port, gen_effbdpattern_LoopExit_Sequence, gen_effbdpattern_Iteration_Sequence, gen_effbdpattern_ModelElement_Indexable, gen_effbdpattern_Component_ModelElement, gen_effbdpattern_Domain_Indexable, gen_effbdpattern_AbstractModel_Indexable, gen_effbdpattern_Context_Indexable, gen_effbdpattern_PatternModel_AbstractModel, gen_effbdpattern_SystemPattern_Indexable, gen_effbdpattern_Problem_Indexable, gen_effbdpattern_Model_AbstractModel},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)