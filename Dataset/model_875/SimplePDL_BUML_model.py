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
simplepdl_ProcessElement = Class(name="simplepdl::ProcessElement", is_abstract=True)
simplepdl_Resource = Class(name="simplepdl::Resource")
simplepdl_WorkDefinition = Class(name="simplepdl::WorkDefinition")
ProcessElement = Class(name="ProcessElement")
simplepdl_WorkSequence = Class(name="simplepdl::WorkSequence")
simplepdl_Parameter = Class(name="simplepdl::Parameter")
simplepdl_Guidance = Class(name="simplepdl::Guidance")

# simplepdl_Process class attributes and methods
simplepdl_Process_name: Property = Property(name="name", type=StringType)
simplepdl_Process_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_Process_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_Process.attributes={simplepdl_Process_min_time, simplepdl_Process_name, simplepdl_Process_max_time}

# simplepdl_ProcessElement class attributes and methods

# simplepdl_Resource class attributes and methods
simplepdl_Resource_name: Property = Property(name="name", type=StringType)
simplepdl_Resource_marking: Property = Property(name="marking", type=IntegerType)
simplepdl_Resource.attributes={simplepdl_Resource_name, simplepdl_Resource_marking}

# simplepdl_WorkDefinition class attributes and methods
simplepdl_WorkDefinition_min_time: Property = Property(name="min_time", type=IntegerType)
simplepdl_WorkDefinition_max_time: Property = Property(name="max_time", type=IntegerType)
simplepdl_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplepdl_WorkDefinition.attributes={simplepdl_WorkDefinition_name, simplepdl_WorkDefinition_min_time, simplepdl_WorkDefinition_max_time}

# ProcessElement class attributes and methods

# simplepdl_WorkSequence class attributes and methods
simplepdl_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplepdl_WorkSequence_name: Property = Property(name="name", type=StringType)
simplepdl_WorkSequence.attributes={simplepdl_WorkSequence_name, simplepdl_WorkSequence_linkType}

# simplepdl_Parameter class attributes and methods
simplepdl_Parameter_nbNeeds: Property = Property(name="nbNeeds", type=IntegerType)
simplepdl_Parameter_name: Property = Property(name="name", type=StringType)
simplepdl_Parameter.attributes={simplepdl_Parameter_nbNeeds, simplepdl_Parameter_name}

# simplepdl_Guidance class attributes and methods
simplepdl_Guidance_text: Property = Property(name="text", type=StringType)
simplepdl_Guidance.attributes={simplepdl_Guidance_text}

# Relationships
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
linksToPredecessors3: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors3",
    ends={
        Property(name="WorkSequence", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
linksToSuccessors4: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors4",
    ends={
        Property(name="WorkSequence5", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplepdl_WorkSequence, multiplicity=Multiplicity(0, 9999))
    }
)
needs6: BinaryAssociation = BinaryAssociation(
    name="needs6",
    ends={
        Property(name="Parameter", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="workDefinition", type=simplepdl_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
element10: BinaryAssociation = BinaryAssociation(
    name="element10",
    ends={
        Property(name="simplepdl_ProcessElement11", type=simplepdl_Guidance, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Guidance", type=simplepdl_ProcessElement, multiplicity=Multiplicity(0, 9999))
    }
)
resource12: BinaryAssociation = BinaryAssociation(
    name="resource12",
    ends={
        Property(name="simplepdl_Resource13", type=simplepdl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simplepdl_Parameter", type=simplepdl_Resource, multiplicity=Multiplicity(1, 1))
    }
)
workDefinition14: BinaryAssociation = BinaryAssociation(
    name="workDefinition14",
    ends={
        Property(name="WorkDefinition15", type=simplepdl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="needs", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
predecessor7: BinaryAssociation = BinaryAssociation(
    name="predecessor7",
    ends={
        Property(name="WorkDefinition", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)
successor8: BinaryAssociation = BinaryAssociation(
    name="successor8",
    ends={
        Property(name="WorkDefinition9", type=simplepdl_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplepdl_WorkDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplepdl_WorkDefinition_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkDefinition)
gen_simplepdl_WorkSequence_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_WorkSequence)
gen_simplepdl_Parameter_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Parameter)
gen_simplepdl_Guidance_ProcessElement = Generalization(general=ProcessElement, specific=simplepdl_Guidance)

# Domain Model
domain_model = DomainModel(
    name="simplepdl",
    types={simplepdl_Process, simplepdl_ProcessElement, simplepdl_Resource, simplepdl_WorkDefinition, ProcessElement, simplepdl_WorkSequence, simplepdl_Parameter, simplepdl_Guidance, WorkSequenceType},
    associations={processElements0, resources1, linksToPredecessors3, linksToSuccessors4, needs6, element10, resource12, workDefinition14, predecessor7, successor8},
    generalizations={gen_simplepdl_WorkDefinition_ProcessElement, gen_simplepdl_WorkSequence_ProcessElement, gen_simplepdl_Parameter_ProcessElement, gen_simplepdl_Guidance_ProcessElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)