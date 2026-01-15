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
expansionmodel_Representation = Class(name="expansionmodel::Representation")
AbstractRepresentation = Class(name="AbstractRepresentation")
expansionmodel_InducedRepresentation = Class(name="expansionmodel::InducedRepresentation")
expansionmodel_AbstractRepresentation = Class(name="expansionmodel::AbstractRepresentation", is_abstract=True)
expansionmodel_RepresentationKind = Class(name="expansionmodel::RepresentationKind")
expansionmodel_UseContext = Class(name="expansionmodel::UseContext")
expansionmodel_GraphicalElementLibrary = Class(name="expansionmodel::GraphicalElementLibrary")
expansionmodel_GMFT_BasedRepresentation = Class(name="expansionmodel::GMFT::BasedRepresentation")
Representation = Class(name="Representation")
expansionmodel_DiagramExpansion = Class(name="expansionmodel::DiagramExpansion")

# expansionmodel_Representation class attributes and methods
expansionmodel_Representation_graphicalElementType: Property = Property(name="graphicalElementType", type=StringType)
expansionmodel_Representation.attributes={expansionmodel_Representation_graphicalElementType}

# AbstractRepresentation class attributes and methods

# expansionmodel_InducedRepresentation class attributes and methods
expansionmodel_InducedRepresentation_hint: Property = Property(name="hint", type=StringType)
expansionmodel_InducedRepresentation.attributes={expansionmodel_InducedRepresentation_hint}

# expansionmodel_AbstractRepresentation class attributes and methods
expansionmodel_AbstractRepresentation_editPartQualifiedName: Property = Property(name="editPartQualifiedName", type=StringType)
expansionmodel_AbstractRepresentation_name: Property = Property(name="name", type=StringType)
expansionmodel_AbstractRepresentation_viewFactory: Property = Property(name="viewFactory", type=StringType)
expansionmodel_AbstractRepresentation_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
expansionmodel_AbstractRepresentation.attributes={expansionmodel_AbstractRepresentation_viewFactory, expansionmodel_AbstractRepresentation_editPartQualifiedName, expansionmodel_AbstractRepresentation_name}
expansionmodel_AbstractRepresentation.methods={expansionmodel_AbstractRepresentation_m_validate}

# expansionmodel_RepresentationKind class attributes and methods
expansionmodel_RepresentationKind_editPartQualifiedName: Property = Property(name="editPartQualifiedName", type=StringType)
expansionmodel_RepresentationKind_name: Property = Property(name="name", type=StringType)
expansionmodel_RepresentationKind_viewFactory: Property = Property(name="viewFactory", type=StringType)
expansionmodel_RepresentationKind.attributes={expansionmodel_RepresentationKind_name, expansionmodel_RepresentationKind_editPartQualifiedName, expansionmodel_RepresentationKind_viewFactory}

# expansionmodel_UseContext class attributes and methods
expansionmodel_UseContext_diagramType: Property = Property(name="diagramType", type=StringType)
expansionmodel_UseContext_name: Property = Property(name="name", type=StringType)
expansionmodel_UseContext.attributes={expansionmodel_UseContext_diagramType, expansionmodel_UseContext_name}

# expansionmodel_GraphicalElementLibrary class attributes and methods
expansionmodel_GraphicalElementLibrary_name: Property = Property(name="name", type=StringType)
expansionmodel_GraphicalElementLibrary.attributes={expansionmodel_GraphicalElementLibrary_name}

# expansionmodel_GMFT_BasedRepresentation class attributes and methods
expansionmodel_GMFT_BasedRepresentation_reusedID: Property = Property(name="reusedID", type=StringType)
expansionmodel_GMFT_BasedRepresentation.attributes={expansionmodel_GMFT_BasedRepresentation_reusedID}

# Representation class attributes and methods

# expansionmodel_DiagramExpansion class attributes and methods
expansionmodel_DiagramExpansion_ID: Property = Property(name="ID", type=StringType)
expansionmodel_DiagramExpansion.attributes={expansionmodel_DiagramExpansion_ID}

# Relationships
inducedRepresentations0: BinaryAssociation = BinaryAssociation(
    name="inducedRepresentations0",
    ends={
        Property(name="expansionmodel_InducedRepresentation", type=expansionmodel_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_Representation", type=expansionmodel_InducedRepresentation, multiplicity=Multiplicity(0, 9999))
    }
)
subRepresentations2: BinaryAssociation = BinaryAssociation(
    name="subRepresentations2",
    ends={
        Property(name="expansionmodel_Representation3", type=expansionmodel_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_Representation1", type=expansionmodel_Representation, multiplicity=Multiplicity(0, 9999))
    }
)
kind4: BinaryAssociation = BinaryAssociation(
    name="kind4",
    ends={
        Property(name="expansionmodel_RepresentationKind", type=expansionmodel_AbstractRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_AbstractRepresentation", type=expansionmodel_RepresentationKind, multiplicity=Multiplicity(0, 1))
    }
)
children5: BinaryAssociation = BinaryAssociation(
    name="children5",
    ends={
        Property(name="expansionmodel_Representation7", type=expansionmodel_InducedRepresentation, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_InducedRepresentation6", type=expansionmodel_Representation, multiplicity=Multiplicity(0, 9999))
    }
)
representationkinds8: BinaryAssociation = BinaryAssociation(
    name="representationkinds8",
    ends={
        Property(name="expansionmodel_RepresentationKind9", type=expansionmodel_GraphicalElementLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_GraphicalElementLibrary", type=expansionmodel_RepresentationKind, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representations10: BinaryAssociation = BinaryAssociation(
    name="representations10",
    ends={
        Property(name="expansionmodel_AbstractRepresentation12", type=expansionmodel_GraphicalElementLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_GraphicalElementLibrary11", type=expansionmodel_AbstractRepresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
representations13: BinaryAssociation = BinaryAssociation(
    name="representations13",
    ends={
        Property(name="expansionmodel_Representation14", type=expansionmodel_UseContext, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_UseContext", type=expansionmodel_Representation, multiplicity=Multiplicity(1, 9999))
    }
)
gmftRepresentations15: BinaryAssociation = BinaryAssociation(
    name="gmftRepresentations15",
    ends={
        Property(name="expansionmodel_GMFT_BasedRepresentation", type=expansionmodel_UseContext, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_UseContext16", type=expansionmodel_GMFT_BasedRepresentation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usages17: BinaryAssociation = BinaryAssociation(
    name="usages17",
    ends={
        Property(name="expansionmodel_UseContext18", type=expansionmodel_DiagramExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_DiagramExpansion", type=expansionmodel_UseContext, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries19: BinaryAssociation = BinaryAssociation(
    name="libraries19",
    ends={
        Property(name="expansionmodel_GraphicalElementLibrary21", type=expansionmodel_DiagramExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="expansionmodel_DiagramExpansion20", type=expansionmodel_GraphicalElementLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_expansionmodel_Representation_AbstractRepresentation = Generalization(general=AbstractRepresentation, specific=expansionmodel_Representation)
gen_expansionmodel_InducedRepresentation_AbstractRepresentation = Generalization(general=AbstractRepresentation, specific=expansionmodel_InducedRepresentation)
gen_expansionmodel_GMFT_BasedRepresentation_Representation = Generalization(general=Representation, specific=expansionmodel_GMFT_BasedRepresentation)

# Domain Model
domain_model = DomainModel(
    name="expansionmodel",
    types={expansionmodel_Representation, AbstractRepresentation, expansionmodel_InducedRepresentation, expansionmodel_AbstractRepresentation, expansionmodel_RepresentationKind, expansionmodel_UseContext, expansionmodel_GraphicalElementLibrary, expansionmodel_GMFT_BasedRepresentation, Representation, expansionmodel_DiagramExpansion},
    associations={inducedRepresentations0, subRepresentations2, kind4, children5, representationkinds8, representations10, representations13, gmftRepresentations15, usages17, libraries19},
    generalizations={gen_expansionmodel_Representation_AbstractRepresentation, gen_expansionmodel_InducedRepresentation_AbstractRepresentation, gen_expansionmodel_GMFT_BasedRepresentation_Representation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)