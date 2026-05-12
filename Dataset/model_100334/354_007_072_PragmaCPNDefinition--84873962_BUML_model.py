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
pragmacpndefinition_PetriNet = Class(name="pragmacpndefinition_PetriNet")
pragmacpndefinition_PragmaCPN = Class(name="pragmacpndefinition_PragmaCPN")
CPN = Class(name="CPN")
pragmacpndefinition_Place = Class(name="pragmacpndefinition_Place")
Place = Class(name="Place")
OntologyMember = Class(name="OntologyMember")
pragmacpndefinition_Pragma = Class(name="pragmacpndefinition_Pragma")
Label = Class(name="Label")
pragmacpndefinition_OntologyDocument = Class(name="pragmacpndefinition_OntologyDocument")
pragmacpndefinition_PragmaticsOntology = Class(name="pragmacpndefinition_PragmaticsOntology")
PetriNet = Class(name="PetriNet")
pragmacpndefinition_OntologyMember = Class(name="pragmacpndefinition_OntologyMember", is_abstract=True)
pragmacpndefinition_Transition = Class(name="pragmacpndefinition_Transition")
Transition = Class(name="Transition")
pragmacpndefinition_Arc = Class(name="pragmacpndefinition_Arc")
Arc = Class(name="Arc")
pragmacpndefinition_Page = Class(name="pragmacpndefinition_Page")
Page = Class(name="Page")

# pragmacpndefinition_PetriNet class attributes and methods

# pragmacpndefinition_PragmaCPN class attributes and methods

# CPN class attributes and methods

# pragmacpndefinition_Place class attributes and methods

# Place class attributes and methods

# OntologyMember class attributes and methods

# pragmacpndefinition_Pragma class attributes and methods
pragmacpndefinition_Pragma_text: Property = Property(name="text", type=StringType)
pragmacpndefinition_Pragma.attributes={pragmacpndefinition_Pragma_text}

# Label class attributes and methods

# pragmacpndefinition_OntologyDocument class attributes and methods
pragmacpndefinition_OntologyDocument_iri: Property = Property(name="iri", type=StringType)
pragmacpndefinition_OntologyDocument_path: Property = Property(name="path", type=StringType)
pragmacpndefinition_OntologyDocument.attributes={pragmacpndefinition_OntologyDocument_path, pragmacpndefinition_OntologyDocument_iri}

# pragmacpndefinition_PragmaticsOntology class attributes and methods
pragmacpndefinition_PragmaticsOntology_manager: Property = Property(name="manager", type=StringType)
pragmacpndefinition_PragmaticsOntology_m_addOntologyFromFile: Method = Method(name="addOntologyFromFile", parameters={Parameter(name='pragmacpndefinition_file', type=StringType)})
pragmacpndefinition_PragmaticsOntology_m_getValidPragmatics: Method = Method(name="getValidPragmatics", parameters={Parameter(name='pragmacpndefinition_object', type=StringType)}, type=StringType)
pragmacpndefinition_PragmaticsOntology.attributes={pragmacpndefinition_PragmaticsOntology_manager}
pragmacpndefinition_PragmaticsOntology.methods={pragmacpndefinition_PragmaticsOntology_m_getValidPragmatics, pragmacpndefinition_PragmaticsOntology_m_addOntologyFromFile}

# PetriNet class attributes and methods

# pragmacpndefinition_OntologyMember class attributes and methods
pragmacpndefinition_OntologyMember_m_getOWLClass: Method = Method(name="getOWLClass", parameters={}, type=StringType)
pragmacpndefinition_OntologyMember.methods={pragmacpndefinition_OntologyMember_m_getOWLClass}

# pragmacpndefinition_Transition class attributes and methods

# Transition class attributes and methods

# pragmacpndefinition_Arc class attributes and methods

# Arc class attributes and methods

# pragmacpndefinition_Page class attributes and methods

# Page class attributes and methods

# Relationships
net2: BinaryAssociation = BinaryAssociation(
    name="net2",
    ends={
        Property(name="PetriNet", type=pragmacpndefinition_PragmaticsOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="ontology3", type=pragmacpndefinition_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
ontology0: BinaryAssociation = BinaryAssociation(
    name="ontology0",
    ends={
        Property(name="PragmaticsOntology", type=pragmacpndefinition_OntologyDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="documents", type=pragmacpndefinition_PragmaticsOntology, multiplicity=Multiplicity(0, 1))
    }
)
documents1: BinaryAssociation = BinaryAssociation(
    name="documents1",
    ends={
        Property(name="OntologyDocument", type=pragmacpndefinition_PragmaticsOntology, multiplicity=Multiplicity(1, 1)),
        Property(name="ontology", type=pragmacpndefinition_OntologyDocument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ontology4: BinaryAssociation = BinaryAssociation(
    name="ontology4",
    ends={
        Property(name="PragmaticsOntology5", type=pragmacpndefinition_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=pragmacpndefinition_PragmaticsOntology, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Annotation6: BinaryAssociation = BinaryAssociation(
    name="Annotation6",
    ends={
        Property(name="pragmacpndefinition_Pragma", type=pragmacpndefinition_OntologyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="pragmacpndefinition_OntologyMember", type=pragmacpndefinition_Pragma, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_pragmacpndefinition_PragmaCPN_CPN = Generalization(general=CPN, specific=pragmacpndefinition_PragmaCPN)
gen_pragmacpndefinition_Place_Place = Generalization(general=Place, specific=pragmacpndefinition_Place)
gen_pragmacpndefinition_Place_OntologyMember = Generalization(general=OntologyMember, specific=pragmacpndefinition_Place)
gen_pragmacpndefinition_Pragma_Label = Generalization(general=Label, specific=pragmacpndefinition_Pragma)
gen_pragmacpndefinition_PragmaticsOntology_Label = Generalization(general=Label, specific=pragmacpndefinition_PragmaticsOntology)
gen_pragmacpndefinition_PetriNet_PetriNet = Generalization(general=PetriNet, specific=pragmacpndefinition_PetriNet)
gen_pragmacpndefinition_Transition_Transition = Generalization(general=Transition, specific=pragmacpndefinition_Transition)
gen_pragmacpndefinition_Transition_OntologyMember = Generalization(general=OntologyMember, specific=pragmacpndefinition_Transition)
gen_pragmacpndefinition_Arc_Arc = Generalization(general=Arc, specific=pragmacpndefinition_Arc)
gen_pragmacpndefinition_Arc_OntologyMember = Generalization(general=OntologyMember, specific=pragmacpndefinition_Arc)
gen_pragmacpndefinition_Page_Page = Generalization(general=Page, specific=pragmacpndefinition_Page)
gen_pragmacpndefinition_Page_OntologyMember = Generalization(general=OntologyMember, specific=pragmacpndefinition_Page)

# Domain Model
domain_model = DomainModel(
    name="pragmacpndefinition",
    types={pragmacpndefinition_PetriNet, pragmacpndefinition_PragmaCPN, CPN, pragmacpndefinition_Place, Place, OntologyMember, pragmacpndefinition_Pragma, Label, pragmacpndefinition_OntologyDocument, pragmacpndefinition_PragmaticsOntology, PetriNet, pragmacpndefinition_OntologyMember, pragmacpndefinition_Transition, Transition, pragmacpndefinition_Arc, Arc, pragmacpndefinition_Page, Page},
    associations={net2, ontology0, documents1, ontology4, Annotation6},
    generalizations={gen_pragmacpndefinition_PragmaCPN_CPN, gen_pragmacpndefinition_Place_Place, gen_pragmacpndefinition_Place_OntologyMember, gen_pragmacpndefinition_Pragma_Label, gen_pragmacpndefinition_PragmaticsOntology_Label, gen_pragmacpndefinition_PetriNet_PetriNet, gen_pragmacpndefinition_Transition_Transition, gen_pragmacpndefinition_Transition_OntologyMember, gen_pragmacpndefinition_Arc_Arc, gen_pragmacpndefinition_Arc_OntologyMember, gen_pragmacpndefinition_Page_Page, gen_pragmacpndefinition_Page_OntologyMember},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)