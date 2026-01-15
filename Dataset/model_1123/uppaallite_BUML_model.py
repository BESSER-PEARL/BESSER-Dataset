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
uppaallite_UppaalDiagram = Class(name="uppaallite::UppaalDiagram")
uppaallite_TemplateType = Class(name="uppaallite::TemplateType")
uppaallite_LocationType = Class(name="uppaallite::LocationType")
uppaallite_TransitionType = Class(name="uppaallite::TransitionType")

# uppaallite_UppaalDiagram class attributes and methods
uppaallite_UppaalDiagram_declaration: Property = Property(name="declaration", type=StringType)
uppaallite_UppaalDiagram_resourceWeightDeclaration: Property = Property(name="resourceWeightDeclaration", type=StringType)
uppaallite_UppaalDiagram.attributes={uppaallite_UppaalDiagram_declaration, uppaallite_UppaalDiagram_resourceWeightDeclaration}

# uppaallite_TemplateType class attributes and methods
uppaallite_TemplateType_name: Property = Property(name="name", type=StringType)
uppaallite_TemplateType_declaration: Property = Property(name="declaration", type=StringType)
uppaallite_TemplateType.attributes={uppaallite_TemplateType_declaration, uppaallite_TemplateType_name}

# uppaallite_LocationType class attributes and methods
uppaallite_LocationType_y: Property = Property(name="y", type=IntegerType)
uppaallite_LocationType_name: Property = Property(name="name", type=StringType)
uppaallite_LocationType_urgent: Property = Property(name="urgent", type=BooleanType)
uppaallite_LocationType_committed: Property = Property(name="committed", type=BooleanType)
uppaallite_LocationType_initial: Property = Property(name="initial", type=BooleanType)
uppaallite_LocationType_id: Property = Property(name="id", type=StringType)
uppaallite_LocationType_invariant: Property = Property(name="invariant", type=StringType)
uppaallite_LocationType_cost: Property = Property(name="cost", type=StringType)
uppaallite_LocationType_x: Property = Property(name="x", type=IntegerType)
uppaallite_LocationType.attributes={uppaallite_LocationType_invariant, uppaallite_LocationType_y, uppaallite_LocationType_urgent, uppaallite_LocationType_id, uppaallite_LocationType_name, uppaallite_LocationType_cost, uppaallite_LocationType_x, uppaallite_LocationType_committed, uppaallite_LocationType_initial}

# uppaallite_TransitionType class attributes and methods
uppaallite_TransitionType_sync: Property = Property(name="sync", type=StringType)
uppaallite_TransitionType_assignment: Property = Property(name="assignment", type=StringType)
uppaallite_TransitionType_guard: Property = Property(name="guard", type=StringType)
uppaallite_TransitionType_cost: Property = Property(name="cost", type=StringType)
uppaallite_TransitionType.attributes={uppaallite_TransitionType_guard, uppaallite_TransitionType_assignment, uppaallite_TransitionType_sync, uppaallite_TransitionType_cost}

# Relationships
Template0: BinaryAssociation = BinaryAssociation(
    name="Template0",
    ends={
        Property(name="uppaallite_TemplateType", type=uppaallite_UppaalDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaallite_UppaalDiagram", type=uppaallite_TemplateType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="uppaallite_LocationType", type=uppaallite_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaallite_TransitionType", type=uppaallite_LocationType, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="uppaallite_LocationType8", type=uppaallite_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="uppaallite_TransitionType7", type=uppaallite_LocationType, multiplicity=Multiplicity(1, 1))
    }
)
container9: BinaryAssociation = BinaryAssociation(
    name="container9",
    ends={
        Property(name="TemplateType10", type=uppaallite_TransitionType, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=uppaallite_TemplateType, multiplicity=Multiplicity(1, 1))
    }
)
location1: BinaryAssociation = BinaryAssociation(
    name="location1",
    ends={
        Property(name="LocationType", type=uppaallite_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=uppaallite_LocationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition2: BinaryAssociation = BinaryAssociation(
    name="transition2",
    ends={
        Property(name="TransitionType", type=uppaallite_TemplateType, multiplicity=Multiplicity(1, 1)),
        Property(name="container3", type=uppaallite_TransitionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container4: BinaryAssociation = BinaryAssociation(
    name="container4",
    ends={
        Property(name="TemplateType", type=uppaallite_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="location", type=uppaallite_TemplateType, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="uppaallite",
    types={uppaallite_UppaalDiagram, uppaallite_TemplateType, uppaallite_LocationType, uppaallite_TransitionType},
    associations={Template0, source5, target6, container9, location1, transition2, container4},
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