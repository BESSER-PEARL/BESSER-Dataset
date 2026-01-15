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
standard_Auxiliary = Class(name="standard::Auxiliary")
standard_ModelLibrary = Class(name="standard::ModelLibrary")
standard_Class = Class(name="standard::Class")
standard_BuildComponent = Class(name="standard::BuildComponent")
standard_Component = Class(name="standard::Component")
standard_Create = Class(name="standard::Create")
standard_BehavioralFeature = Class(name="standard::BehavioralFeature")
standard_Usage = Class(name="standard::Usage")
standard_Call = Class(name="standard::Call")
standard_Derive = Class(name="standard::Derive")
standard_Abstraction = Class(name="standard::Abstraction")
standard_Destroy = Class(name="standard::Destroy")
standard_Focus = Class(name="standard::Focus")
standard_Framework = Class(name="standard::Framework")
standard_Package = Class(name="standard::Package")
standard_Implement = Class(name="standard::Implement")
standard_ImplementationClass = Class(name="standard::ImplementationClass")
standard_Instantiate = Class(name="standard::Instantiate")
standard_Metaclass = Class(name="standard::Metaclass")
standard_Service = Class(name="standard::Service")
standard_Refine = Class(name="standard::Refine")
standard_Responsibility = Class(name="standard::Responsibility")
standard_Script = Class(name="standard::Script")
standard_Artifact = Class(name="standard::Artifact")
standard_Send = Class(name="standard::Send")
standard_Trace = Class(name="standard::Trace")
standard_Type = Class(name="standard::Type")
standard_Utility = Class(name="standard::Utility")
standard_Document = Class(name="standard::Document")
standard_Entity = Class(name="standard::Entity")
standard_Executable = Class(name="standard::Executable")
standard_File = Class(name="standard::File")
standard_Library = Class(name="standard::Library")
standard_Process = Class(name="standard::Process")
standard_Realization = Class(name="standard::Realization")
standard_Classifier = Class(name="standard::Classifier")
standard_Source = Class(name="standard::Source")
standard_Specification = Class(name="standard::Specification")
standard_Subsystem = Class(name="standard::Subsystem")
standard_Metamodel = Class(name="standard::Metamodel")
standard_Model = Class(name="standard::Model")
standard_SystemModel = Class(name="standard::SystemModel")

# standard_Auxiliary class attributes and methods

# standard_ModelLibrary class attributes and methods

# standard_Class class attributes and methods

# standard_BuildComponent class attributes and methods

# standard_Component class attributes and methods

# standard_Create class attributes and methods

# standard_BehavioralFeature class attributes and methods

# standard_Usage class attributes and methods

# standard_Call class attributes and methods

# standard_Derive class attributes and methods

# standard_Abstraction class attributes and methods

# standard_Destroy class attributes and methods

# standard_Focus class attributes and methods

# standard_Framework class attributes and methods

# standard_Package class attributes and methods

# standard_Implement class attributes and methods

# standard_ImplementationClass class attributes and methods

# standard_Instantiate class attributes and methods

# standard_Metaclass class attributes and methods

# standard_Service class attributes and methods

# standard_Refine class attributes and methods

# standard_Responsibility class attributes and methods

# standard_Script class attributes and methods

# standard_Artifact class attributes and methods

# standard_Send class attributes and methods

# standard_Trace class attributes and methods

# standard_Type class attributes and methods

# standard_Utility class attributes and methods

# standard_Document class attributes and methods

# standard_Entity class attributes and methods

# standard_Executable class attributes and methods

# standard_File class attributes and methods

# standard_Library class attributes and methods

# standard_Process class attributes and methods

# standard_Realization class attributes and methods

# standard_Classifier class attributes and methods

# standard_Source class attributes and methods

# standard_Specification class attributes and methods

# standard_Subsystem class attributes and methods

# standard_Metamodel class attributes and methods

# standard_Model class attributes and methods

# standard_SystemModel class attributes and methods

# Relationships
base_Class0: BinaryAssociation = BinaryAssociation(
    name="base_Class0",
    ends={
        Property(name="standard_Class", type=standard_Auxiliary, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Auxiliary", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Component1: BinaryAssociation = BinaryAssociation(
    name="base_Component1",
    ends={
        Property(name="standard_Component", type=standard_BuildComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_BuildComponent", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature2: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature2",
    ends={
        Property(name="standard_BehavioralFeature", type=standard_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Create", type=standard_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage3: BinaryAssociation = BinaryAssociation(
    name="base_Usage3",
    ends={
        Property(name="standard_Usage", type=standard_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Create4", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage5: BinaryAssociation = BinaryAssociation(
    name="base_Usage5",
    ends={
        Property(name="standard_Usage6", type=standard_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Call", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction7: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction7",
    ends={
        Property(name="standard_Abstraction", type=standard_Derive, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Derive", type=standard_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature8: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature8",
    ends={
        Property(name="standard_BehavioralFeature9", type=standard_Destroy, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Destroy", type=standard_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Class10: BinaryAssociation = BinaryAssociation(
    name="base_Class10",
    ends={
        Property(name="standard_Class11", type=standard_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Focus", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package12: BinaryAssociation = BinaryAssociation(
    name="base_Package12",
    ends={
        Property(name="standard_Package", type=standard_Framework, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Framework", type=standard_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Component13: BinaryAssociation = BinaryAssociation(
    name="base_Component13",
    ends={
        Property(name="standard_Component14", type=standard_Implement, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Implement", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Class15: BinaryAssociation = BinaryAssociation(
    name="base_Class15",
    ends={
        Property(name="standard_Class16", type=standard_ImplementationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_ImplementationClass", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage17: BinaryAssociation = BinaryAssociation(
    name="base_Usage17",
    ends={
        Property(name="standard_Usage18", type=standard_Instantiate, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Instantiate", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Class19: BinaryAssociation = BinaryAssociation(
    name="base_Class19",
    ends={
        Property(name="standard_Class20", type=standard_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Metaclass", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier48: BinaryAssociation = BinaryAssociation(
    name="base_Classifier48",
    ends={
        Property(name="standard_Realization", type=standard_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Classifier", type=standard_Realization, multiplicity=Multiplicity(1, 1))
    }
)
base_Package21: BinaryAssociation = BinaryAssociation(
    name="base_Package21",
    ends={
        Property(name="standard_Package22", type=standard_ModelLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_ModelLibrary", type=standard_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction23: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction23",
    ends={
        Property(name="standard_Abstraction24", type=standard_Refine, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Refine", type=standard_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage25: BinaryAssociation = BinaryAssociation(
    name="base_Usage25",
    ends={
        Property(name="standard_Usage26", type=standard_Responsibility, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Responsibility", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact27: BinaryAssociation = BinaryAssociation(
    name="base_Artifact27",
    ends={
        Property(name="standard_Artifact", type=standard_Script, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Script", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage28: BinaryAssociation = BinaryAssociation(
    name="base_Usage28",
    ends={
        Property(name="standard_Usage29", type=standard_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Send", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction30: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction30",
    ends={
        Property(name="standard_Abstraction31", type=standard_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Trace", type=standard_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Class32: BinaryAssociation = BinaryAssociation(
    name="base_Class32",
    ends={
        Property(name="standard_Class33", type=standard_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Type", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class34: BinaryAssociation = BinaryAssociation(
    name="base_Class34",
    ends={
        Property(name="standard_Class35", type=standard_Utility, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Utility", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact36: BinaryAssociation = BinaryAssociation(
    name="base_Artifact36",
    ends={
        Property(name="standard_Artifact37", type=standard_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Document", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Component38: BinaryAssociation = BinaryAssociation(
    name="base_Component38",
    ends={
        Property(name="standard_Component39", type=standard_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Entity", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact40: BinaryAssociation = BinaryAssociation(
    name="base_Artifact40",
    ends={
        Property(name="standard_Artifact41", type=standard_Executable, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Executable", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact42: BinaryAssociation = BinaryAssociation(
    name="base_Artifact42",
    ends={
        Property(name="standard_Artifact43", type=standard_File, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_File", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact44: BinaryAssociation = BinaryAssociation(
    name="base_Artifact44",
    ends={
        Property(name="standard_Artifact45", type=standard_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Library", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Component46: BinaryAssociation = BinaryAssociation(
    name="base_Component46",
    ends={
        Property(name="standard_Component47", type=standard_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Process", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Component49: BinaryAssociation = BinaryAssociation(
    name="base_Component49",
    ends={
        Property(name="standard_Component50", type=standard_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Service", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact51: BinaryAssociation = BinaryAssociation(
    name="base_Artifact51",
    ends={
        Property(name="standard_Artifact52", type=standard_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Source", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier53: BinaryAssociation = BinaryAssociation(
    name="base_Classifier53",
    ends={
        Property(name="standard_Classifier54", type=standard_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Specification", type=standard_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Component55: BinaryAssociation = BinaryAssociation(
    name="base_Component55",
    ends={
        Property(name="standard_Component56", type=standard_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Subsystem", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Model57: BinaryAssociation = BinaryAssociation(
    name="base_Model57",
    ends={
        Property(name="standard_Model", type=standard_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Metamodel", type=standard_Model, multiplicity=Multiplicity(1, 1))
    }
)
base_Model58: BinaryAssociation = BinaryAssociation(
    name="base_Model58",
    ends={
        Property(name="standard_Model59", type=standard_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SystemModel", type=standard_Model, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="standard",
    types={standard_Auxiliary, standard_ModelLibrary, standard_Class, standard_BuildComponent, standard_Component, standard_Create, standard_BehavioralFeature, standard_Usage, standard_Call, standard_Derive, standard_Abstraction, standard_Destroy, standard_Focus, standard_Framework, standard_Package, standard_Implement, standard_ImplementationClass, standard_Instantiate, standard_Metaclass, standard_Service, standard_Refine, standard_Responsibility, standard_Script, standard_Artifact, standard_Send, standard_Trace, standard_Type, standard_Utility, standard_Document, standard_Entity, standard_Executable, standard_File, standard_Library, standard_Process, standard_Realization, standard_Classifier, standard_Source, standard_Specification, standard_Subsystem, standard_Metamodel, standard_Model, standard_SystemModel},
    associations={base_Class0, base_Component1, base_BehavioralFeature2, base_Usage3, base_Usage5, base_Abstraction7, base_BehavioralFeature8, base_Class10, base_Package12, base_Component13, base_Class15, base_Usage17, base_Class19, base_Classifier48, base_Package21, base_Abstraction23, base_Usage25, base_Artifact27, base_Usage28, base_Abstraction30, base_Class32, base_Class34, base_Artifact36, base_Component38, base_Artifact40, base_Artifact42, base_Artifact44, base_Component46, base_Component49, base_Artifact51, base_Classifier53, base_Component55, base_Model57, base_Model58},
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