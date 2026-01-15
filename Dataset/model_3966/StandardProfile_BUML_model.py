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
StandardProfile_Derive = Class(name="StandardProfile::Derive")
StandardProfile_Abstraction = Class(name="StandardProfile::Abstraction")
StandardProfile_Destroy = Class(name="StandardProfile::Destroy")
StandardProfile_Auxiliary = Class(name="StandardProfile::Auxiliary")
StandardProfile_Class = Class(name="StandardProfile::Class")
StandardProfile_Call = Class(name="StandardProfile::Call")
StandardProfile_Usage = Class(name="StandardProfile::Usage")
StandardProfile_Create = Class(name="StandardProfile::Create")
StandardProfile_BehavioralFeature = Class(name="StandardProfile::BehavioralFeature")
StandardProfile_Refine = Class(name="StandardProfile::Refine")
StandardProfile_Responsibility = Class(name="StandardProfile::Responsibility")
StandardProfile_Script = Class(name="StandardProfile::Script")
StandardProfile_Document = Class(name="StandardProfile::Document")
File = Class(name="File")
StandardProfile_File = Class(name="StandardProfile::File")
StandardProfile_Artifact = Class(name="StandardProfile::Artifact")
StandardProfile_Entity = Class(name="StandardProfile::Entity")
StandardProfile_Component = Class(name="StandardProfile::Component")
StandardProfile_Executable = Class(name="StandardProfile::Executable")
StandardProfile_Focus = Class(name="StandardProfile::Focus")
StandardProfile_Framework = Class(name="StandardProfile::Framework")
StandardProfile_Package = Class(name="StandardProfile::Package")
StandardProfile_Implement = Class(name="StandardProfile::Implement")
StandardProfile_ImplementationClass = Class(name="StandardProfile::ImplementationClass")
StandardProfile_Instantiate = Class(name="StandardProfile::Instantiate")
StandardProfile_Library = Class(name="StandardProfile::Library")
StandardProfile_Metaclass = Class(name="StandardProfile::Metaclass")
StandardProfile_ModelLibrary = Class(name="StandardProfile::ModelLibrary")
StandardProfile_Process = Class(name="StandardProfile::Process")
StandardProfile_Realization = Class(name="StandardProfile::Realization")
StandardProfile_Classifier = Class(name="StandardProfile::Classifier")
StandardProfile_Send = Class(name="StandardProfile::Send")
StandardProfile_Service = Class(name="StandardProfile::Service")
StandardProfile_Source = Class(name="StandardProfile::Source")
StandardProfile_Specification = Class(name="StandardProfile::Specification")
StandardProfile_Subsystem = Class(name="StandardProfile::Subsystem")
StandardProfile_Trace = Class(name="StandardProfile::Trace")
StandardProfile_Type = Class(name="StandardProfile::Type")
StandardProfile_Utility = Class(name="StandardProfile::Utility")
StandardProfile_BuildComponent = Class(name="StandardProfile::BuildComponent")
StandardProfile_Metamodel = Class(name="StandardProfile::Metamodel")
StandardProfile_Model = Class(name="StandardProfile::Model")
StandardProfile_SystemModel = Class(name="StandardProfile::SystemModel")

# StandardProfile_Derive class attributes and methods

# StandardProfile_Abstraction class attributes and methods

# StandardProfile_Destroy class attributes and methods

# StandardProfile_Auxiliary class attributes and methods

# StandardProfile_Class class attributes and methods

# StandardProfile_Call class attributes and methods

# StandardProfile_Usage class attributes and methods

# StandardProfile_Create class attributes and methods

# StandardProfile_BehavioralFeature class attributes and methods

# StandardProfile_Refine class attributes and methods

# StandardProfile_Responsibility class attributes and methods

# StandardProfile_Script class attributes and methods

# StandardProfile_Document class attributes and methods

# File class attributes and methods

# StandardProfile_File class attributes and methods

# StandardProfile_Artifact class attributes and methods

# StandardProfile_Entity class attributes and methods

# StandardProfile_Component class attributes and methods

# StandardProfile_Executable class attributes and methods

# StandardProfile_Focus class attributes and methods

# StandardProfile_Framework class attributes and methods

# StandardProfile_Package class attributes and methods

# StandardProfile_Implement class attributes and methods

# StandardProfile_ImplementationClass class attributes and methods

# StandardProfile_Instantiate class attributes and methods

# StandardProfile_Library class attributes and methods

# StandardProfile_Metaclass class attributes and methods

# StandardProfile_ModelLibrary class attributes and methods

# StandardProfile_Process class attributes and methods

# StandardProfile_Realization class attributes and methods

# StandardProfile_Classifier class attributes and methods

# StandardProfile_Send class attributes and methods

# StandardProfile_Service class attributes and methods

# StandardProfile_Source class attributes and methods

# StandardProfile_Specification class attributes and methods

# StandardProfile_Subsystem class attributes and methods

# StandardProfile_Trace class attributes and methods

# StandardProfile_Type class attributes and methods

# StandardProfile_Utility class attributes and methods

# StandardProfile_BuildComponent class attributes and methods

# StandardProfile_Metamodel class attributes and methods

# StandardProfile_Model class attributes and methods

# StandardProfile_SystemModel class attributes and methods

# Relationships
base_BehavioralFeature2: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature2",
    ends={
        Property(name="StandardProfile_BehavioralFeature", type=StandardProfile_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Create", type=StandardProfile_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage3: BinaryAssociation = BinaryAssociation(
    name="base_Usage3",
    ends={
        Property(name="StandardProfile_Usage5", type=StandardProfile_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Create4", type=StandardProfile_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction6: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction6",
    ends={
        Property(name="StandardProfile_Abstraction", type=StandardProfile_Derive, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Derive", type=StandardProfile_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature7: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature7",
    ends={
        Property(name="StandardProfile_BehavioralFeature8", type=StandardProfile_Destroy, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Destroy", type=StandardProfile_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Class0: BinaryAssociation = BinaryAssociation(
    name="base_Class0",
    ends={
        Property(name="StandardProfile_Class", type=StandardProfile_Auxiliary, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Auxiliary", type=StandardProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage1: BinaryAssociation = BinaryAssociation(
    name="base_Usage1",
    ends={
        Property(name="StandardProfile_Usage", type=StandardProfile_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Call", type=StandardProfile_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier26: BinaryAssociation = BinaryAssociation(
    name="base_Classifier26",
    ends={
        Property(name="StandardProfile_Classifier", type=StandardProfile_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Realization", type=StandardProfile_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction27: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction27",
    ends={
        Property(name="StandardProfile_Abstraction28", type=StandardProfile_Refine, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Refine", type=StandardProfile_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage29: BinaryAssociation = BinaryAssociation(
    name="base_Usage29",
    ends={
        Property(name="StandardProfile_Usage30", type=StandardProfile_Responsibility, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Responsibility", type=StandardProfile_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact9: BinaryAssociation = BinaryAssociation(
    name="base_Artifact9",
    ends={
        Property(name="StandardProfile_Artifact", type=StandardProfile_File, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_File", type=StandardProfile_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Component10: BinaryAssociation = BinaryAssociation(
    name="base_Component10",
    ends={
        Property(name="StandardProfile_Component", type=StandardProfile_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Entity", type=StandardProfile_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Class11: BinaryAssociation = BinaryAssociation(
    name="base_Class11",
    ends={
        Property(name="StandardProfile_Class12", type=StandardProfile_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Focus", type=StandardProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package13: BinaryAssociation = BinaryAssociation(
    name="base_Package13",
    ends={
        Property(name="StandardProfile_Package", type=StandardProfile_Framework, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Framework", type=StandardProfile_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Component14: BinaryAssociation = BinaryAssociation(
    name="base_Component14",
    ends={
        Property(name="StandardProfile_Component15", type=StandardProfile_Implement, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Implement", type=StandardProfile_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Class16: BinaryAssociation = BinaryAssociation(
    name="base_Class16",
    ends={
        Property(name="StandardProfile_Class17", type=StandardProfile_ImplementationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_ImplementationClass", type=StandardProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage18: BinaryAssociation = BinaryAssociation(
    name="base_Usage18",
    ends={
        Property(name="StandardProfile_Usage19", type=StandardProfile_Instantiate, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Instantiate", type=StandardProfile_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Class20: BinaryAssociation = BinaryAssociation(
    name="base_Class20",
    ends={
        Property(name="StandardProfile_Class21", type=StandardProfile_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Metaclass", type=StandardProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package22: BinaryAssociation = BinaryAssociation(
    name="base_Package22",
    ends={
        Property(name="StandardProfile_Package23", type=StandardProfile_ModelLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_ModelLibrary", type=StandardProfile_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Component24: BinaryAssociation = BinaryAssociation(
    name="base_Component24",
    ends={
        Property(name="StandardProfile_Component25", type=StandardProfile_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Process", type=StandardProfile_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Model48: BinaryAssociation = BinaryAssociation(
    name="base_Model48",
    ends={
        Property(name="StandardProfile_Model49", type=StandardProfile_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_SystemModel", type=StandardProfile_Model, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage31: BinaryAssociation = BinaryAssociation(
    name="base_Usage31",
    ends={
        Property(name="StandardProfile_Usage32", type=StandardProfile_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Send", type=StandardProfile_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Component33: BinaryAssociation = BinaryAssociation(
    name="base_Component33",
    ends={
        Property(name="StandardProfile_Component34", type=StandardProfile_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Service", type=StandardProfile_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier35: BinaryAssociation = BinaryAssociation(
    name="base_Classifier35",
    ends={
        Property(name="StandardProfile_Classifier36", type=StandardProfile_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Specification", type=StandardProfile_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Component37: BinaryAssociation = BinaryAssociation(
    name="base_Component37",
    ends={
        Property(name="StandardProfile_Component38", type=StandardProfile_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Subsystem", type=StandardProfile_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction39: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction39",
    ends={
        Property(name="StandardProfile_Abstraction40", type=StandardProfile_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Trace", type=StandardProfile_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Class41: BinaryAssociation = BinaryAssociation(
    name="base_Class41",
    ends={
        Property(name="StandardProfile_Class42", type=StandardProfile_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Type", type=StandardProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class43: BinaryAssociation = BinaryAssociation(
    name="base_Class43",
    ends={
        Property(name="StandardProfile_Class44", type=StandardProfile_Utility, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Utility", type=StandardProfile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Component45: BinaryAssociation = BinaryAssociation(
    name="base_Component45",
    ends={
        Property(name="StandardProfile_Component46", type=StandardProfile_BuildComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_BuildComponent", type=StandardProfile_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Model47: BinaryAssociation = BinaryAssociation(
    name="base_Model47",
    ends={
        Property(name="StandardProfile_Model", type=StandardProfile_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="StandardProfile_Metamodel", type=StandardProfile_Model, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_StandardProfile_Document_File = Generalization(general=File, specific=StandardProfile_Document)
gen_StandardProfile_Executable_File = Generalization(general=File, specific=StandardProfile_Executable)
gen_StandardProfile_Library_File = Generalization(general=File, specific=StandardProfile_Library)
gen_StandardProfile_Script_File = Generalization(general=File, specific=StandardProfile_Script)
gen_StandardProfile_Source_File = Generalization(general=File, specific=StandardProfile_Source)

# Domain Model
domain_model = DomainModel(
    name="StandardProfile",
    types={StandardProfile_Derive, StandardProfile_Abstraction, StandardProfile_Destroy, StandardProfile_Auxiliary, StandardProfile_Class, StandardProfile_Call, StandardProfile_Usage, StandardProfile_Create, StandardProfile_BehavioralFeature, StandardProfile_Refine, StandardProfile_Responsibility, StandardProfile_Script, StandardProfile_Document, File, StandardProfile_File, StandardProfile_Artifact, StandardProfile_Entity, StandardProfile_Component, StandardProfile_Executable, StandardProfile_Focus, StandardProfile_Framework, StandardProfile_Package, StandardProfile_Implement, StandardProfile_ImplementationClass, StandardProfile_Instantiate, StandardProfile_Library, StandardProfile_Metaclass, StandardProfile_ModelLibrary, StandardProfile_Process, StandardProfile_Realization, StandardProfile_Classifier, StandardProfile_Send, StandardProfile_Service, StandardProfile_Source, StandardProfile_Specification, StandardProfile_Subsystem, StandardProfile_Trace, StandardProfile_Type, StandardProfile_Utility, StandardProfile_BuildComponent, StandardProfile_Metamodel, StandardProfile_Model, StandardProfile_SystemModel},
    associations={base_BehavioralFeature2, base_Usage3, base_Abstraction6, base_BehavioralFeature7, base_Class0, base_Usage1, base_Classifier26, base_Abstraction27, base_Usage29, base_Artifact9, base_Component10, base_Class11, base_Package13, base_Component14, base_Class16, base_Usage18, base_Class20, base_Package22, base_Component24, base_Model48, base_Usage31, base_Component33, base_Classifier35, base_Component37, base_Abstraction39, base_Class41, base_Class43, base_Component45, base_Model47},
    generalizations={gen_StandardProfile_Document_File, gen_StandardProfile_Executable_File, gen_StandardProfile_Library_File, gen_StandardProfile_Script_File, gen_StandardProfile_Source_File},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)