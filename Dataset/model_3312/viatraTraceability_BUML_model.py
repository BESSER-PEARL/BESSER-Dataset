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
viatraTraceability_DepToGSPN = Class(name="viatraTraceability::DepToGSPN")
viatraTraceability_PetriNet = Class(name="viatraTraceability::PetriNet")
viatraTraceability_DepModel = Class(name="viatraTraceability::DepModel")
viatraTraceability_DepToGSPNTrace = Class(name="viatraTraceability::DepToGSPNTrace")
viatraTraceability_AbstractElement = Class(name="viatraTraceability::AbstractElement")
viatraTraceability_Identification = Class(name="viatraTraceability::Identification")

# viatraTraceability_DepToGSPN class attributes and methods

# viatraTraceability_PetriNet class attributes and methods

# viatraTraceability_DepModel class attributes and methods

# viatraTraceability_DepToGSPNTrace class attributes and methods

# viatraTraceability_AbstractElement class attributes and methods

# viatraTraceability_Identification class attributes and methods

# Relationships
petrinet0: BinaryAssociation = BinaryAssociation(
    name="petrinet0",
    ends={
        Property(name="viatraTraceability_PetriNet", type=viatraTraceability_DepToGSPN, multiplicity=Multiplicity(1, 1)),
        Property(name="viatraTraceability_DepToGSPN", type=viatraTraceability_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
depmodel1: BinaryAssociation = BinaryAssociation(
    name="depmodel1",
    ends={
        Property(name="viatraTraceability_DepModel", type=viatraTraceability_DepToGSPN, multiplicity=Multiplicity(1, 1)),
        Property(name="viatraTraceability_DepToGSPN2", type=viatraTraceability_DepModel, multiplicity=Multiplicity(0, 1))
    }
)
deptogspntrace3: BinaryAssociation = BinaryAssociation(
    name="deptogspntrace3",
    ends={
        Property(name="viatraTraceability_DepToGSPNTrace", type=viatraTraceability_DepToGSPN, multiplicity=Multiplicity(1, 1)),
        Property(name="viatraTraceability_DepToGSPN4", type=viatraTraceability_DepToGSPNTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractelement5: BinaryAssociation = BinaryAssociation(
    name="abstractelement5",
    ends={
        Property(name="viatraTraceability_AbstractElement", type=viatraTraceability_DepToGSPNTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viatraTraceability_DepToGSPNTrace6", type=viatraTraceability_AbstractElement, multiplicity=Multiplicity(0, 9999))
    }
)
identification7: BinaryAssociation = BinaryAssociation(
    name="identification7",
    ends={
        Property(name="viatraTraceability_Identification", type=viatraTraceability_DepToGSPNTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="viatraTraceability_DepToGSPNTrace8", type=viatraTraceability_Identification, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="viatraTraceability",
    types={viatraTraceability_DepToGSPN, viatraTraceability_PetriNet, viatraTraceability_DepModel, viatraTraceability_DepToGSPNTrace, viatraTraceability_AbstractElement, viatraTraceability_Identification},
    associations={petrinet0, depmodel1, deptogspntrace3, abstractelement5, identification7},
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