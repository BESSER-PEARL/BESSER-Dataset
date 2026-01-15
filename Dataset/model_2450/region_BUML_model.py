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
region_RgRegion = Class(name="region::RgRegion")
ModelRoot = Class(name="ModelRoot")
region_RgInitialPseudostate = Class(name="region::RgInitialPseudostate")
region_RgState = Class(name="region::RgState")
Named = Class(name="Named")
region_RgTransition = Class(name="region::RgTransition")
Referenced = Class(name="Referenced")

# region_RgRegion class attributes and methods
region_RgRegion_containerClass: Property = Property(name="containerClass", type=StringType)
region_RgRegion.attributes={region_RgRegion_containerClass}

# ModelRoot class attributes and methods

# region_RgInitialPseudostate class attributes and methods

# region_RgState class attributes and methods
region_RgState_entry: Property = Property(name="entry", type=StringType)
region_RgState_exit: Property = Property(name="exit", type=StringType)
region_RgState_isFinal: Property = Property(name="isFinal", type=BooleanType)
region_RgState.attributes={region_RgState_entry, region_RgState_exit, region_RgState_isFinal}

# Named class attributes and methods

# region_RgTransition class attributes and methods
region_RgTransition_message: Property = Property(name="message", type=StringType)
region_RgTransition_effect: Property = Property(name="effect", type=StringType)
region_RgTransition_event: Property = Property(name="event", type=StringType)
region_RgTransition.attributes={region_RgTransition_effect, region_RgTransition_event, region_RgTransition_message}

# Referenced class attributes and methods

# Relationships
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="region_RgTransition7", type=region_RgState, multiplicity=Multiplicity(1, 1)),
        Property(name="region_RgState6", type=region_RgTransition, multiplicity=Multiplicity(0, 9999))
    }
)
initialPseudostate0: BinaryAssociation = BinaryAssociation(
    name="initialPseudostate0",
    ends={
        Property(name="region_RgInitialPseudostate", type=region_RgRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="region_RgRegion", type=region_RgInitialPseudostate, multiplicity=Multiplicity(1, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="region_RgState", type=region_RgRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="region_RgRegion2", type=region_RgState, multiplicity=Multiplicity(1, 9999))
    }
)
initialTransition3: BinaryAssociation = BinaryAssociation(
    name="initialTransition3",
    ends={
        Property(name="region_RgTransition", type=region_RgInitialPseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="region_RgInitialPseudostate4", type=region_RgTransition, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="region_RgState10", type=region_RgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="region_RgTransition9", type=region_RgState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_region_RgState_Named = Generalization(general=Named, specific=region_RgState)
gen_region_RgRegion_ModelRoot = Generalization(general=ModelRoot, specific=region_RgRegion)
gen_region_RgInitialPseudostate_Named = Generalization(general=Named, specific=region_RgInitialPseudostate)
gen_region_RgTransition_Referenced = Generalization(general=Referenced, specific=region_RgTransition)

# Domain Model
domain_model = DomainModel(
    name="region",
    types={region_RgRegion, ModelRoot, region_RgInitialPseudostate, region_RgState, Named, region_RgTransition, Referenced},
    associations={transitions5, initialPseudostate0, states1, initialTransition3, target8},
    generalizations={gen_region_RgState_Named, gen_region_RgRegion_ModelRoot, gen_region_RgInitialPseudostate_Named, gen_region_RgTransition_Referenced},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)