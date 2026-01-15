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
WorkSequenceType: Enumeration = Enumeration(
    name="WorkSequenceType",
    literals={
            EnumerationLiteral(name="startToStart"),
			EnumerationLiteral(name="finishToStart"),
			EnumerationLiteral(name="startToFinish"),
			EnumerationLiteral(name="finishToFinish")
    }
)

# Classes
simplepdl_Process = Class(name="simplepdl::Process")
simplepdl_SubWorkDefinition = Class(name="simplepdl::SubWorkDefinition")
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
Activities = Class(name="Activities")
simplepdl_ParameterWD = Class(name="simplepdl::ParameterWD")
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_Resource = Class(name="simplepdl::Resource")
simplepdl_Guidance = Class(name="simplepdl::Guidance")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_Activities = Class(name="simplepdl::Activities", is_abstract=True)
simplepdl_ParameterSWD = Class(name="simplepdl::ParameterSWD")
simplepdl_Parameter = Class(name="simplepdl::Parameter", is_abstract=True)
Parameter_ = Class(name="Parameter")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_Process_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_Process.attributes={simplepdl_Process_max_time, simplepdl_Process_name, simplepdl_Process_min_time}

# simplepdl_SubWorkDefinition class attributes and methods

# simplepdl_WorkDefinition class attributes and methods

# Activities class attributes and methods

# simplepdl_ParameterWD class attributes and methods

# simplepdl_ProcessElement class attributes and methods

# simplepdl_Resource class attributes and methods
simplepdl_Resource_name: Property = Property(name="name", type=StringType)
simplepdl_Resource_marking: Property = Property(name="marking", type=IntegerType)
simplepdl_Resource.attributes={simplepdl_Resource_name, simplepdl_Resource_marking}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_name: Property = Property(name="name", type=StringType)
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_linkType, simplepdl_WorkSequence_name}

# simplepdl_Activities class attributes and methods
simplepdl_Activities_name: Property = Property(name="name", type=StringType)
simplepdl_Activities_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_Activities_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_Activities.attributes={simplepdl_Activities_max_time, simplepdl_Activities_name, simplepdl_Activities_min_time}

# simplepdl_ParameterSWD class attributes and methods

# simplepdl_Parameter class attributes and methods
simplepdl_Parameter_name: Property = Property(name="name", type=StringType)
simplepdl_Parameter_nbNeeds: Property = Property(name="nbNeeds", type=IntegerType)
simplepdl_Parameter.attributes={simplepdl_Parameter_nbNeeds, simplepdl_Parameter_name}

# Parameter class attributes and methods

# Relationships
successor6: BinaryAssociation = BinaryAssociation(
    name="successor6",
    ends={
        Property(name="Activities7", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_Activities, multiplicity=Multiplicity(1, 1))
    }
)
linksToPredecessors8: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors8",
    ends={
        Property(name="WorkSequence", type=simplepdl_Activities, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors9: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors9",
    ends={
        Property(name="WorkSequence10", type=simplepdl_Activities, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
children11: BinaryAssociation = BinaryAssociation(
    name="children11",
    ends={
        Property(name="SubWorkDefinition", type=simplepdl_Activities, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=simplepdl_SubWorkDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
needsWD12: BinaryAssociation = BinaryAssociation(
    name="needsWD12",
    ends={
        Property(name="ParameterWD", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workDefinition", type=simplepdl_ParameterWD, multiplicity=Multiplicity(0, 9999))
    }
)
processElements0: BinaryAssociation = BinaryAssociation(
    name="processElements0",
    ends={
        Property(name="simplepdl_ProcessElement", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources1: BinaryAssociation = BinaryAssociation(
    name="resources1",
    ends={
        Property(name="simplepdl_Resource", type=simplepdl_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Process2", type=simplepdl_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element3: BinaryAssociation = BinaryAssociation(
    name="element3",
    ends={
        Property(name="simplepdl_ProcessElement4", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor5: BinaryAssociation = BinaryAssociation(
    name="predecessor5",
    ends={
        Property(name="Activities", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_Activities, multiplicity=Multiplicity(1, 1))
    }
)
subWorkDefinition21: BinaryAssociation = BinaryAssociation(
    name="subWorkDefinition21",
    ends={
        Property(name="simplepdl_SubWorkDefinition23", type=simplepdl_ParameterSWD, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_ParameterSWD22", type=simplepdl_SubWorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parent13: BinaryAssociation = BinaryAssociation(
    name="parent13",
    ends={
        Property(name="Activities14", type=simplepdl_SubWorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=simplepdl_Activities, multiplicity=Multiplicity(1, 1))
    }
)
needsSWD15: BinaryAssociation = BinaryAssociation(
    name="needsSWD15",
    ends={
        Property(name="simplepdl_ParameterSWD", type=simplepdl_SubWorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_SubWorkDefinition", type=simplepdl_ParameterSWD, multiplicity=Multiplicity(0, 9999))
    }
)
resource16: BinaryAssociation = BinaryAssociation(
    name="resource16",
    ends={
        Property(name="simplepdl_Resource17", type=simplepdl_ParameterWD, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_ParameterWD", type=simplepdl_Resource, multiplicity=Multiplicity(1, 1))
    }
)
workDefinition18: BinaryAssociation = BinaryAssociation(
    name="workDefinition18",
    ends={
        Property(name="WorkDefinition", type=simplepdl_ParameterWD, multiplicity=Multiplicity(1, 1)),
        Property(name="needsWD", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
internResource19: BinaryAssociation = BinaryAssociation(
    name="internResource19",
    ends={
        Property(name="simplepdl_Parameter", type=simplepdl_ParameterSWD, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_ParameterSWD20", type=simplepdl_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_Activities_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Activities)
gen_simplepdl_WorkDefinition_Activities = Generalization(general=Activities, specific=simplepdl_WorkDefinition)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_SubWorkDefinition_Activities = Generalization(general=Activities, specific=simplepdl_SubWorkDefinition)
gen_simplepdl_Parameter_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Parameter)
gen_simplepdl_ParameterWD_Parameter = Generalization(general=Parameter_, specific=simplepdl_ParameterWD)
gen_simplepdl_ParameterSWD_Parameter = Generalization(general=Parameter_, specific=simplepdl_ParameterSWD)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_SubWorkDefinition, simplepdl_WorkDefinition, Activities, simplepdl_ParameterWD, simplepdl_ProcessElement, simplepdl_Resource, simplepdl_Guidance, ProcessElement, simplepdl_WorkSequence, simplepdl_Activities, simplepdl_ParameterSWD, simplepdl_Parameter, Parameter_, WorkSequenceType},
    associations={successor6, linksToPredecessors8, linksToSuccessors9, children11, needsWD12, processElements0, resources1, element3, predecessor5, subWorkDefinition21, parent13, needsSWD15, resource16, workDefinition18, internResource19},
    generalizations={gen_simplepdl_Activities_ProcessElement, gen_simplepdl_WorkDefinition_Activities, gen_simplepdl_Guidance_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_SubWorkDefinition_Activities, gen_simplepdl_Parameter_ProcessElement, gen_simplepdl_ParameterWD_Parameter, gen_simplepdl_ParameterSWD_Parameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)