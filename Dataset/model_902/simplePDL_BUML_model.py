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
			EnumerationLiteral(name="finishTofinish")
    }
)

ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout")
    }
)

# Classes
simplePDL_Process = Class(name="simplePDL::Process")
simplePDL_WorkDefinition = Class(name="simplePDL::WorkDefinition", is_abstract=True)
simplePDL_WorkSequence = Class(name="simplePDL::WorkSequence")
simplePDL_WorkDefinitionParameter = Class(name="simplePDL::WorkDefinitionParameter")
simplePDL_WorkProduct = Class(name="simplePDL::WorkProduct")
simplePDL_SubProcess = Class(name="simplePDL::SubProcess")
WorkDefinition = Class(name="WorkDefinition")
simplePDL_Activity = Class(name="simplePDL::Activity")

# simplePDL_Process class attributes and methods
simplePDL_Process_name: Property = Property(name="name", type=StringType)
simplePDL_Process.attributes={simplePDL_Process_name}

# simplePDL_WorkDefinition class attributes and methods
simplePDL_WorkDefinition_name: Property = Property(name="name", type=StringType)
simplePDL_WorkDefinition.attributes={simplePDL_WorkDefinition_name}

# simplePDL_WorkSequence class attributes and methods
simplePDL_WorkSequence_linkType: Property = Property(name="linkType", type=StringType)
simplePDL_WorkSequence.attributes={simplePDL_WorkSequence_linkType}

# simplePDL_WorkDefinitionParameter class attributes and methods
simplePDL_WorkDefinitionParameter_parameterKind: Property = Property(name="parameterKind", type=StringType)
simplePDL_WorkDefinitionParameter.attributes={simplePDL_WorkDefinitionParameter_parameterKind}

# simplePDL_WorkProduct class attributes and methods
simplePDL_WorkProduct_name: Property = Property(name="name", type=StringType)
simplePDL_WorkProduct.attributes={simplePDL_WorkProduct_name}

# simplePDL_SubProcess class attributes and methods

# WorkDefinition class attributes and methods

# simplePDL_Activity class attributes and methods

# Relationships
activities0: BinaryAssociation = BinaryAssociation(
    name="activities0",
    ends={
        Property(name="simplePDL_WorkDefinition", type=simplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplePDL_Process", type=simplePDL_WorkDefinition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
workSequences1: BinaryAssociation = BinaryAssociation(
    name="workSequences1",
    ends={
        Property(name="simplePDL_WorkSequence", type=simplePDL_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="simplePDL_Process2", type=simplePDL_WorkSequence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor3: BinaryAssociation = BinaryAssociation(
    name="predecessor3",
    ends={
        Property(name="WorkSequence", type=simplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessors", type=simplePDL_WorkSequence, multiplicity=Multiplicity(1, 1))
    }
)
successor4: BinaryAssociation = BinaryAssociation(
    name="successor4",
    ends={
        Property(name="WorkSequence5", type=simplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessors", type=simplePDL_WorkSequence, multiplicity=Multiplicity(1, 1))
    }
)
linksToSuccessors8: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessors8",
    ends={
        Property(name="WorkDefinition", type=simplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=simplePDL_WorkDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
linksToPredecessors9: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessors9",
    ends={
        Property(name="WorkDefinition10", type=simplePDL_WorkSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=simplePDL_WorkDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
parameterType11: BinaryAssociation = BinaryAssociation(
    name="parameterType11",
    ends={
        Property(name="simplePDL_WorkProduct", type=simplePDL_WorkDefinitionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simplePDL_WorkDefinitionParameter12", type=simplePDL_WorkProduct, multiplicity=Multiplicity(1, 1))
    }
)
parameters6: BinaryAssociation = BinaryAssociation(
    name="parameters6",
    ends={
        Property(name="simplePDL_WorkDefinitionParameter", type=simplePDL_WorkDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplePDL_WorkDefinition7", type=simplePDL_WorkDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simplePDL_SubProcess_WorkDefinition = Generalization(general=WorkDefinition, specific=simplePDL_SubProcess)
gen_simplePDL_Activity_WorkDefinition = Generalization(general=WorkDefinition, specific=simplePDL_Activity)

# Domain Model
domain_model = DomainModel(
    name="simplePDL",
    types={simplePDL_Process, simplePDL_WorkDefinition, simplePDL_WorkSequence, simplePDL_WorkDefinitionParameter, simplePDL_WorkProduct, simplePDL_SubProcess, WorkDefinition, simplePDL_Activity, WorkSequenceType, ParameterDirectionKind},
    associations={activities0, workSequences1, predecessor3, successor4, linksToSuccessors8, linksToPredecessors9, parameterType11, parameters6},
    generalizations={gen_simplePDL_SubProcess_WorkDefinition, gen_simplePDL_Activity_WorkDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)