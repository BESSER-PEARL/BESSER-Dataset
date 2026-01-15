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
l2_BehavioralFeature = Class(name="l2::BehavioralFeature")
l2_Derive = Class(name="l2::Derive")
l2_Abstraction = Class(name="l2::Abstraction")
l2_Auxiliary = Class(name="l2::Auxiliary")
l2_Class = Class(name="l2::Class")
l2_Call = Class(name="l2::Call")
l2_Usage = Class(name="l2::Usage")
l2_Create = Class(name="l2::Create")
l2_Framework = Class(name="l2::Framework")
l2_Package = Class(name="l2::Package")
l2_Implement = Class(name="l2::Implement")
l2_ValueSpecification = Class(name="l2::ValueSpecification")
l2_Destroy = Class(name="l2::Destroy")
l2_Document = Class(name="l2::Document")
File = Class(name="File")
l2_File = Class(name="l2::File", is_abstract=True)
l2_Artifact = Class(name="l2::Artifact")
l2_Entity = Class(name="l2::Entity")
l2_Component = Class(name="l2::Component")
l2_Executable = Class(name="l2::Executable")
l2_Focus = Class(name="l2::Focus")
l2_Metaclass = Class(name="l2::Metaclass")
l2_ModelLibrary = Class(name="l2::ModelLibrary")
l2_Process = Class(name="l2::Process")
l2_ImplementationClass = Class(name="l2::ImplementationClass")
l2_Instantiate = Class(name="l2::Instantiate")
l2_Library = Class(name="l2::Library")
l2_Service = Class(name="l2::Service")
l2_Source = Class(name="l2::Source")
l2_Realization = Class(name="l2::Realization")
l2_Classifier = Class(name="l2::Classifier")
l2_Refine = Class(name="l2::Refine")
l2_Responsibility = Class(name="l2::Responsibility")
l2_Script = Class(name="l2::Script")
l2_Send = Class(name="l2::Send")
l2_Utility = Class(name="l2::Utility")
l2_Specification = Class(name="l2::Specification")
l2_Subsystem = Class(name="l2::Subsystem")
l2_Trace = Class(name="l2::Trace")
l2_Type = Class(name="l2::Type")

# l2_BehavioralFeature class attributes and methods

# l2_Derive class attributes and methods

# l2_Abstraction class attributes and methods

# l2_Auxiliary class attributes and methods

# l2_Class class attributes and methods

# l2_Call class attributes and methods
l2_Call_m_client_and_supplier_are_operations: Method = Method(name="client_and_supplier_are_operations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
l2_Call.methods={l2_Call_m_client_and_supplier_are_operations}

# l2_Usage class attributes and methods

# l2_Create class attributes and methods
l2_Create_m_client_and_supplier_are_classifiers: Method = Method(name="client_and_supplier_are_classifiers", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
l2_Create.methods={l2_Create_m_client_and_supplier_are_classifiers}

# l2_Framework class attributes and methods

# l2_Package class attributes and methods

# l2_Implement class attributes and methods
l2_Implement_m_implements_specification: Method = Method(name="implements_specification", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
l2_Implement.methods={l2_Implement_m_implements_specification}

# l2_ValueSpecification class attributes and methods

# l2_Destroy class attributes and methods

# l2_Document class attributes and methods

# File class attributes and methods

# l2_File class attributes and methods

# l2_Artifact class attributes and methods

# l2_Entity class attributes and methods

# l2_Component class attributes and methods

# l2_Executable class attributes and methods

# l2_Focus class attributes and methods

# l2_Metaclass class attributes and methods

# l2_ModelLibrary class attributes and methods

# l2_Process class attributes and methods

# l2_ImplementationClass class attributes and methods
l2_ImplementationClass_m_cannot_be_realization: Method = Method(name="cannot_be_realization", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
l2_ImplementationClass.methods={l2_ImplementationClass_m_cannot_be_realization}

# l2_Instantiate class attributes and methods
l2_Instantiate_m_client_and_supplier_are_classifiers: Method = Method(name="client_and_supplier_are_classifiers", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
l2_Instantiate.methods={l2_Instantiate_m_client_and_supplier_are_classifiers}

# l2_Library class attributes and methods

# l2_Service class attributes and methods

# l2_Source class attributes and methods

# l2_Realization class attributes and methods
l2_Realization_m_cannot_be_implementationClass: Method = Method(name="cannot_be_implementationClass", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
l2_Realization.methods={l2_Realization_m_cannot_be_implementationClass}

# l2_Classifier class attributes and methods

# l2_Refine class attributes and methods

# l2_Responsibility class attributes and methods

# l2_Script class attributes and methods

# l2_Send class attributes and methods
l2_Send_m_client_operation_sends_supplier_signal: Method = Method(name="client_operation_sends_supplier_signal", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
l2_Send.methods={l2_Send_m_client_operation_sends_supplier_signal}

# l2_Utility class attributes and methods
l2_Utility_m_is_utility: Method = Method(name="is_utility", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
l2_Utility.methods={l2_Utility_m_is_utility}

# l2_Specification class attributes and methods
l2_Specification_m_cannot_be_type: Method = Method(name="cannot_be_type", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
l2_Specification.methods={l2_Specification_m_cannot_be_type}

# l2_Subsystem class attributes and methods

# l2_Trace class attributes and methods

# l2_Type class attributes and methods
l2_Type_m_cannot_be_specification: Method = Method(name="cannot_be_specification", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
l2_Type.methods={l2_Type_m_cannot_be_specification}

# Relationships
base_BehavioralFeature2: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature2",
    ends={
        Property(name="l2_BehavioralFeature", type=l2_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Create", type=l2_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
base_Usage3: BinaryAssociation = BinaryAssociation(
    name="base_Usage3",
    ends={
        Property(name="l2_Usage5", type=l2_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Create4", type=l2_Usage, multiplicity=Multiplicity(0, 1))
    }
)
base_Class0: BinaryAssociation = BinaryAssociation(
    name="base_Class0",
    ends={
        Property(name="l2_Class", type=l2_Auxiliary, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Auxiliary", type=l2_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage1: BinaryAssociation = BinaryAssociation(
    name="base_Usage1",
    ends={
        Property(name="l2_Usage", type=l2_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Call", type=l2_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Class13: BinaryAssociation = BinaryAssociation(
    name="base_Class13",
    ends={
        Property(name="l2_Class14", type=l2_Focus, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Focus", type=l2_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package15: BinaryAssociation = BinaryAssociation(
    name="base_Package15",
    ends={
        Property(name="l2_Package", type=l2_Framework, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Framework", type=l2_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction6: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction6",
    ends={
        Property(name="l2_Abstraction", type=l2_Derive, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Derive", type=l2_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
computation7: BinaryAssociation = BinaryAssociation(
    name="computation7",
    ends={
        Property(name="l2_ValueSpecification", type=l2_Derive, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Derive8", type=l2_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base_BehavioralFeature9: BinaryAssociation = BinaryAssociation(
    name="base_BehavioralFeature9",
    ends={
        Property(name="l2_BehavioralFeature10", type=l2_Destroy, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Destroy", type=l2_BehavioralFeature, multiplicity=Multiplicity(1, 1))
    }
)
base_Artifact11: BinaryAssociation = BinaryAssociation(
    name="base_Artifact11",
    ends={
        Property(name="l2_Artifact", type=l2_File, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_File", type=l2_Artifact, multiplicity=Multiplicity(1, 1))
    }
)
base_Component12: BinaryAssociation = BinaryAssociation(
    name="base_Component12",
    ends={
        Property(name="l2_Component", type=l2_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Entity", type=l2_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Class22: BinaryAssociation = BinaryAssociation(
    name="base_Class22",
    ends={
        Property(name="l2_Class23", type=l2_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Metaclass", type=l2_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package24: BinaryAssociation = BinaryAssociation(
    name="base_Package24",
    ends={
        Property(name="l2_Package25", type=l2_ModelLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_ModelLibrary", type=l2_Package, multiplicity=Multiplicity(1, 1))
    }
)
base_Component26: BinaryAssociation = BinaryAssociation(
    name="base_Component26",
    ends={
        Property(name="l2_Component27", type=l2_Process, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Process", type=l2_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Component16: BinaryAssociation = BinaryAssociation(
    name="base_Component16",
    ends={
        Property(name="l2_Component17", type=l2_Implement, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Implement", type=l2_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Class18: BinaryAssociation = BinaryAssociation(
    name="base_Class18",
    ends={
        Property(name="l2_Class19", type=l2_ImplementationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_ImplementationClass", type=l2_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage20: BinaryAssociation = BinaryAssociation(
    name="base_Usage20",
    ends={
        Property(name="l2_Usage21", type=l2_Instantiate, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Instantiate", type=l2_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage33: BinaryAssociation = BinaryAssociation(
    name="base_Usage33",
    ends={
        Property(name="l2_Usage34", type=l2_Send, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Send", type=l2_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Component35: BinaryAssociation = BinaryAssociation(
    name="base_Component35",
    ends={
        Property(name="l2_Component36", type=l2_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Service", type=l2_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier28: BinaryAssociation = BinaryAssociation(
    name="base_Classifier28",
    ends={
        Property(name="l2_Classifier", type=l2_Realization, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Realization", type=l2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction29: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction29",
    ends={
        Property(name="l2_Abstraction30", type=l2_Refine, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Refine", type=l2_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Usage31: BinaryAssociation = BinaryAssociation(
    name="base_Usage31",
    ends={
        Property(name="l2_Usage32", type=l2_Responsibility, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Responsibility", type=l2_Usage, multiplicity=Multiplicity(1, 1))
    }
)
base_Class43: BinaryAssociation = BinaryAssociation(
    name="base_Class43",
    ends={
        Property(name="l2_Class44", type=l2_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Type", type=l2_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Classifier37: BinaryAssociation = BinaryAssociation(
    name="base_Classifier37",
    ends={
        Property(name="l2_Classifier38", type=l2_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Specification", type=l2_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
base_Component39: BinaryAssociation = BinaryAssociation(
    name="base_Component39",
    ends={
        Property(name="l2_Component40", type=l2_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Subsystem", type=l2_Component, multiplicity=Multiplicity(1, 1))
    }
)
base_Abstraction41: BinaryAssociation = BinaryAssociation(
    name="base_Abstraction41",
    ends={
        Property(name="l2_Abstraction42", type=l2_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Trace", type=l2_Abstraction, multiplicity=Multiplicity(1, 1))
    }
)
base_Class45: BinaryAssociation = BinaryAssociation(
    name="base_Class45",
    ends={
        Property(name="l2_Class46", type=l2_Utility, multiplicity=Multiplicity(1, 1)),
        Property(name="l2_Utility", type=l2_Class, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_l2_Document_File = Generalization(general=File, specific=l2_Document)
gen_l2_Executable_File = Generalization(general=File, specific=l2_Executable)
gen_l2_Library_File = Generalization(general=File, specific=l2_Library)
gen_l2_Source_File = Generalization(general=File, specific=l2_Source)
gen_l2_Script_File = Generalization(general=File, specific=l2_Script)

# Domain Model
domain_model = DomainModel(
    name="l2",
    types={l2_BehavioralFeature, l2_Derive, l2_Abstraction, l2_Auxiliary, l2_Class, l2_Call, l2_Usage, l2_Create, l2_Framework, l2_Package, l2_Implement, l2_ValueSpecification, l2_Destroy, l2_Document, File, l2_File, l2_Artifact, l2_Entity, l2_Component, l2_Executable, l2_Focus, l2_Metaclass, l2_ModelLibrary, l2_Process, l2_ImplementationClass, l2_Instantiate, l2_Library, l2_Service, l2_Source, l2_Realization, l2_Classifier, l2_Refine, l2_Responsibility, l2_Script, l2_Send, l2_Utility, l2_Specification, l2_Subsystem, l2_Trace, l2_Type},
    associations={base_BehavioralFeature2, base_Usage3, base_Class0, base_Usage1, base_Class13, base_Package15, base_Abstraction6, computation7, base_BehavioralFeature9, base_Artifact11, base_Component12, base_Class22, base_Package24, base_Component26, base_Component16, base_Class18, base_Usage20, base_Usage33, base_Component35, base_Classifier28, base_Abstraction29, base_Usage31, base_Class43, base_Classifier37, base_Component39, base_Abstraction41, base_Class45},
    generalizations={gen_l2_Document_File, gen_l2_Executable_File, gen_l2_Library_File, gen_l2_Source_File, gen_l2_Script_File},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)