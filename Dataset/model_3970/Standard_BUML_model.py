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
standard_Auxiliary = Class(name="standard_Auxiliary")
standard_Class = Class(name="standard_Class")
standard_Call = Class(name="standard_Call")
standard_Usage = Class(name="standard_Usage")
standard_Create = Class(name="standard_Create")
standard_BehavioralFeature = Class(name="standard_BehavioralFeature")
standard_Abstraction = Class(name="standard_Abstraction")
standard_Destroy = Class(name="standard_Destroy")
standard_Document = Class(name="standard_Document")
File = Class(name="File")
standard_File = Class(name="standard_File", is_abstract=True)
standard_Artifact = Class(name="standard_Artifact")
standard_Entity = Class(name="standard_Entity")
standard_Component = Class(name="standard_Component")
standard_Executable = Class(name="standard_Executable")
standard_Focus = Class(name="standard_Focus")
standard_Framework = Class(name="standard_Framework")
standard_Package = Class(name="standard_Package")
standard_Implement = Class(name="standard_Implement")
standard_Derive = Class(name="standard_Derive")
standard_ValueSpecification = Class(name="standard_ValueSpecification")
standard_ImplementationClass = Class(name="standard_ImplementationClass")
standard_Instantiate = Class(name="standard_Instantiate")
standard_Library = Class(name="standard_Library")
standard_Metaclass = Class(name="standard_Metaclass")
standard_ModelLibrary = Class(name="standard_ModelLibrary")
standard_Process = Class(name="standard_Process")
standard_Classifier = Class(name="standard_Classifier")
standard_Refine = Class(name="standard_Refine")
standard_Responsibility = Class(name="standard_Responsibility")
standard_Script = Class(name="standard_Script")
standard_Send = Class(name="standard_Send")
standard_Service = Class(name="standard_Service")
standard_Source = Class(name="standard_Source")
standard_Realization = Class(name="standard_Realization")
standard_Subsystem = Class(name="standard_Subsystem")
standard_Trace = Class(name="standard_Trace")
standard_Type = Class(name="standard_Type")
standard_Utility = Class(name="standard_Utility")
standard_BuildComponent = Class(name="standard_BuildComponent")
standard_Specification = Class(name="standard_Specification")
standard_SystemModel = Class(name="standard_SystemModel")
standard_Metamodel = Class(name="standard_Metamodel")
standard_Model = Class(name="standard_Model")

# standard_Auxiliary class attributes and methods

# standard_Class class attributes and methods

# standard_Call class attributes and methods
standard_Call_m_client_and_supplier_are_operations: Method = Method(name="client_and_supplier_are_operations", parameters={Parameter(name='standard_diagnostics', type=StringType), Parameter(name='standard_context', type=StringType)}, type=BooleanType)
standard_Call.methods={standard_Call_m_client_and_supplier_are_operations}

# standard_Usage class attributes and methods

# standard_Create class attributes and methods
standard_Create_m_client_and_supplier_are_classifiers: Method = Method(name="client_and_supplier_are_classifiers", parameters={Parameter(name='standard_diagnostics', type=StringType), Parameter(name='standard_context', type=StringType)}, type=BooleanType)
standard_Create.methods={standard_Create_m_client_and_supplier_are_classifiers}

# standard_BehavioralFeature class attributes and methods

# standard_Abstraction class attributes and methods

# standard_Destroy class attributes and methods

# standard_Document class attributes and methods

# File class attributes and methods

# standard_File class attributes and methods

# standard_Artifact class attributes and methods

# standard_Entity class attributes and methods

# standard_Component class attributes and methods

# standard_Executable class attributes and methods

# standard_Focus class attributes and methods

# standard_Framework class attributes and methods

# standard_Package class attributes and methods

# standard_Implement class attributes and methods
standard_Implement_m_implements_specification: Method = Method(name="implements_specification", parameters={Parameter(name='standard_context', type=StringType), Parameter(name='standard_diagnostics', type=StringType)}, type=BooleanType)
standard_Implement.methods={standard_Implement_m_implements_specification}

# standard_Derive class attributes and methods

# standard_ValueSpecification class attributes and methods

# standard_ImplementationClass class attributes and methods
standard_ImplementationClass_m_cannot_be_realization: Method = Method(name="cannot_be_realization", parameters={Parameter(name='standard_context', type=StringType), Parameter(name='standard_diagnostics', type=StringType)}, type=BooleanType)
standard_ImplementationClass.methods={standard_ImplementationClass_m_cannot_be_realization}

# standard_Instantiate class attributes and methods
standard_Instantiate_m_client_and_supplier_are_classifiers: Method = Method(name="client_and_supplier_are_classifiers", parameters={Parameter(name='standard_context', type=StringType), Parameter(name='standard_diagnostics', type=StringType)}, type=BooleanType)
standard_Instantiate.methods={standard_Instantiate_m_client_and_supplier_are_classifiers}

# standard_Library class attributes and methods

# standard_Metaclass class attributes and methods

# standard_ModelLibrary class attributes and methods

# standard_Process class attributes and methods

# standard_Classifier class attributes and methods

# standard_Refine class attributes and methods

# standard_Responsibility class attributes and methods

# standard_Script class attributes and methods

# standard_Send class attributes and methods
standard_Send_m_client_operation_sends_supplier_signal: Method = Method(name="client_operation_sends_supplier_signal", parameters={Parameter(name='standard_diagnostics', type=StringType), Parameter(name='standard_context', type=StringType)}, type=BooleanType)
standard_Send.methods={standard_Send_m_client_operation_sends_supplier_signal}

# standard_Service class attributes and methods

# standard_Source class attributes and methods

# standard_Realization class attributes and methods
standard_Realization_m_cannot_be_implementationClass: Method = Method(name="cannot_be_implementationClass", parameters={Parameter(name='standard_diagnostics', type=StringType), Parameter(name='standard_context', type=StringType)}, type=BooleanType)
standard_Realization.methods={standard_Realization_m_cannot_be_implementationClass}

# standard_Subsystem class attributes and methods

# standard_Trace class attributes and methods

# standard_Type class attributes and methods
standard_Type_m_cannot_be_specification: Method = Method(name="cannot_be_specification", parameters={Parameter(name='standard_diagnostics', type=StringType), Parameter(name='standard_context', type=StringType)}, type=BooleanType)
standard_Type.methods={standard_Type_m_cannot_be_specification}

# standard_Utility class attributes and methods
standard_Utility_m_is_utility: Method = Method(name="is_utility", parameters={Parameter(name='standard_diagnostics', type=StringType), Parameter(name='standard_context', type=StringType)}, type=BooleanType)
standard_Utility.methods={standard_Utility_m_is_utility}

# standard_BuildComponent class attributes and methods

# standard_Specification class attributes and methods
standard_Specification_m_cannot_be_type: Method = Method(name="cannot_be_type", parameters={Parameter(name='standard_context', type=StringType), Parameter(name='standard_diagnostics', type=StringType)}, type=BooleanType)
standard_Specification.methods={standard_Specification_m_cannot_be_type}

# standard_SystemModel class attributes and methods

# standard_Metamodel class attributes and methods

# standard_Model class attributes and methods

# Relationships
base_Class0: BinaryAssociation = BinaryAssociation(
    name="base_Class0",
    ends={
        Property(name="standard_Class", type=standard_Auxiliary, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Auxiliary", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage1: BinaryAssociation = BinaryAssociation(
    name="base_Usage1",
    ends={
        Property(name="standard_Usage", type=standard_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Call", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature2: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature2",
    ends={
        Property(name="standard_BehavioralFeature", type=standard_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Create", type=standard_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
base_Usage3: BinaryAssociation = BinaryAssociation(
    name="base_Usage3",
    ends={
        Property(name="standard_Usage5", type=standard_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Create4", type=standard_Usage, multiplicity=Multiplicity(0, 1))
    }
)
base_Abstraction7: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction7",
    ends={
        Property(name="standard_Abstraction", type=standard_Derive, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Derive8", type=standard_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_BehavioralFeature9: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature9",
    ends={
        Property(name="standard_BehavioralFeature10", type=standard_Destroy, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Destroy", type=standard_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact11: BinaryAssociation = BinaryAssociation(
    name="base_Artifact11",
    ends={
        Property(name="standard_Artifact", type=standard_File, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_File", type=standard_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Component12: BinaryAssociation = BinaryAssociation(
    name="base_Component12",
    ends={
        Property(name="standard_Component", type=standard_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Entity", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Class13: BinaryAssociation = BinaryAssociation(
    name="base_Class13",
    ends={
        Property(name="standard_Class14", type=standard_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Focus", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package15: BinaryAssociation = BinaryAssociation(
    name="base_Package15",
    ends={
        Property(name="standard_Package", type=standard_Framework, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Framework", type=standard_Package, multiplicity=Multiplicity(1, 1))
    }
)
computation6: BinaryAssociation = BinaryAssociation(
    name="computation6",
    ends={
        Property(name="standard_ValueSpecification", type=standard_Derive, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Derive", type=standard_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base_Class18: BinaryAssociation = BinaryAssociation(
    name="base_Class18",
    ends={
        Property(name="standard_Class19", type=standard_ImplementationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_ImplementationClass", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage20: BinaryAssociation = BinaryAssociation(
    name="base_Usage20",
    ends={
        Property(name="standard_Usage21", type=standard_Instantiate, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Instantiate", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Class22: BinaryAssociation = BinaryAssociation(
    name="base_Class22",
    ends={
        Property(name="standard_Class23", type=standard_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Metaclass", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package24: BinaryAssociation = BinaryAssociation(
    name="base_Package24",
    ends={
        Property(name="standard_Package25", type=standard_ModelLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_ModelLibrary", type=standard_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Component26: BinaryAssociation = BinaryAssociation(
    name="base_Component26",
    ends={
        Property(name="standard_Component27", type=standard_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Process", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Component16: BinaryAssociation = BinaryAssociation(
    name="base_Component16",
    ends={
        Property(name="standard_Component17", type=standard_Implement, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Implement", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier28: BinaryAssociation = BinaryAssociation(
    name="base_Classifier28",
    ends={
        Property(name="standard_Classifier", type=standard_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Realization", type=standard_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction29: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction29",
    ends={
        Property(name="standard_Abstraction30", type=standard_Refine, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Refine", type=standard_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage31: BinaryAssociation = BinaryAssociation(
    name="base_Usage31",
    ends={
        Property(name="standard_Usage32", type=standard_Responsibility, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Responsibility", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage33: BinaryAssociation = BinaryAssociation(
    name="base_Usage33",
    ends={
        Property(name="standard_Usage34", type=standard_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Send", type=standard_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Component35: BinaryAssociation = BinaryAssociation(
    name="base_Component35",
    ends={
        Property(name="standard_Component36", type=standard_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Service", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier37: BinaryAssociation = BinaryAssociation(
    name="base_Classifier37",
    ends={
        Property(name="standard_Classifier38", type=standard_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Specification", type=standard_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Component39: BinaryAssociation = BinaryAssociation(
    name="base_Component39",
    ends={
        Property(name="standard_Component40", type=standard_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Subsystem", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction41: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction41",
    ends={
        Property(name="standard_Abstraction42", type=standard_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Trace", type=standard_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Class43: BinaryAssociation = BinaryAssociation(
    name="base_Class43",
    ends={
        Property(name="standard_Class44", type=standard_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Type", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Class45: BinaryAssociation = BinaryAssociation(
    name="base_Class45",
    ends={
        Property(name="standard_Class46", type=standard_Utility, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Utility", type=standard_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Model50: BinaryAssociation = BinaryAssociation(
    name="base_Model50",
    ends={
        Property(name="standard_Model51", type=standard_SystemModel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_SystemModel", type=standard_Model, multiplicity=Multiplicity(1, 1))
    }
)
base_Component47: BinaryAssociation = BinaryAssociation(
    name="base_Component47",
    ends={
        Property(name="standard_Component48", type=standard_BuildComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_BuildComponent", type=standard_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Model49: BinaryAssociation = BinaryAssociation(
    name="base_Model49",
    ends={
        Property(name="standard_Model", type=standard_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="standard_Metamodel", type=standard_Model, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_standard_Document_File = Generalization(general=File, specific=standard_Document)
gen_standard_Executable_File = Generalization(general=File, specific=standard_Executable)
gen_standard_Library_File = Generalization(general=File, specific=standard_Library)
gen_standard_Script_File = Generalization(general=File, specific=standard_Script)
gen_standard_Source_File = Generalization(general=File, specific=standard_Source)

# Domain Model
domain_model = DomainModel(
    name="standard",
    types={standard_Auxiliary, standard_Class, standard_Call, standard_Usage, standard_Create, standard_BehavioralFeature, standard_Abstraction, standard_Destroy, standard_Document, File, standard_File, standard_Artifact, standard_Entity, standard_Component, standard_Executable, standard_Focus, standard_Framework, standard_Package, standard_Implement, standard_Derive, standard_ValueSpecification, standard_ImplementationClass, standard_Instantiate, standard_Library, standard_Metaclass, standard_ModelLibrary, standard_Process, standard_Classifier, standard_Refine, standard_Responsibility, standard_Script, standard_Send, standard_Service, standard_Source, standard_Realization, standard_Subsystem, standard_Trace, standard_Type, standard_Utility, standard_BuildComponent, standard_Specification, standard_SystemModel, standard_Metamodel, standard_Model},
    associations={base_Class0, base_Usage1, base_BehavioralFeature2, base_Usage3, base_Abstraction7, base_BehavioralFeature9, base_Artifact11, base_Component12, base_Class13, base_Package15, computation6, base_Class18, base_Usage20, base_Class22, base_Package24, base_Component26, base_Component16, base_Classifier28, base_Abstraction29, base_Usage31, base_Usage33, base_Component35, base_Classifier37, base_Component39, base_Abstraction41, base_Class43, base_Class45, base_Model50, base_Component47, base_Model49},
    generalizations={gen_standard_Document_File, gen_standard_Executable_File, gen_standard_Library_File, gen_standard_Script_File, gen_standard_Source_File},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)