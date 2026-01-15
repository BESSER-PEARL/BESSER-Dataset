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
EsmLayoutDirection: Enumeration = Enumeration(
    name="EsmLayoutDirection",
    literals={
            EnumerationLiteral(name="DOWN"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="RIGHT"),
			EnumerationLiteral(name="DEFAULT")
    }
)

EsmStateKind: Enumeration = Enumeration(
    name="EsmStateKind",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="INITIAL"),
			EnumerationLiteral(name="FINAL")
    }
)

# Classes
esm_EsmEntityStateModel = Class(name="esm::EsmEntityStateModel")
DModel = Class(name="DModel")
esm_DState = Class(name="esm::DState")
esm_DRichText = Class(name="esm::DRichText")
IEsmStateModel = Class(name="IEsmStateModel")
INavigableMemberContainer = Class(name="INavigableMemberContainer")
IStaticReferenceTarget = Class(name="IStaticReferenceTarget")
IDiagramRoot = Class(name="IDiagramRoot")
esm_DEntityType = Class(name="esm::DEntityType")
esm_IEsmLayout = Class(name="esm::IEsmLayout", is_abstract=True)
esm_IEsmStateModel = Class(name="esm::IEsmStateModel", is_abstract=True)
IEsmLayout = Class(name="IEsmLayout")
esm_IEsmState = Class(name="esm::IEsmState", is_abstract=True)
esm_EsmTransition = Class(name="esm::EsmTransition")
esm_DStateEvent = Class(name="esm::DStateEvent")
esm_EsmState = Class(name="esm::EsmState")
IEsmState = Class(name="IEsmState")
esm_EsmDerivedState = Class(name="esm::EsmDerivedState")
EsmState = Class(name="EsmState")
esm_DExpression = Class(name="esm::DExpression")
esm_EsmCompositeState = Class(name="esm::EsmCompositeState")
esm_EsmConcurrentState = Class(name="esm::EsmConcurrentState")
esm_EsmSubStateModel = Class(name="esm::EsmSubStateModel")

# esm_EsmEntityStateModel class attributes and methods

# DModel class attributes and methods

# esm_DState class attributes and methods

# esm_DRichText class attributes and methods

# IEsmStateModel class attributes and methods

# INavigableMemberContainer class attributes and methods

# IStaticReferenceTarget class attributes and methods

# IDiagramRoot class attributes and methods

# esm_DEntityType class attributes and methods

# esm_IEsmLayout class attributes and methods
esm_IEsmLayout_direction: Property = Property(name="direction", type=StringType)
esm_IEsmLayout.attributes={esm_IEsmLayout_direction}

# esm_IEsmStateModel class attributes and methods

# IEsmLayout class attributes and methods

# esm_IEsmState class attributes and methods
esm_IEsmState_kind: Property = Property(name="kind", type=StringType)
esm_IEsmState.attributes={esm_IEsmState_kind}

# esm_EsmTransition class attributes and methods

# esm_DStateEvent class attributes and methods

# esm_EsmState class attributes and methods

# IEsmState class attributes and methods

# esm_EsmDerivedState class attributes and methods

# EsmState class attributes and methods

# esm_DExpression class attributes and methods

# esm_EsmCompositeState class attributes and methods

# esm_EsmConcurrentState class attributes and methods

# esm_EsmSubStateModel class attributes and methods

# Relationships
state4: BinaryAssociation = BinaryAssociation(
    name="state4",
    ends={
        Property(name="esm_DState", type=esm_IEsmState, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_IEsmState5", type=esm_DState, multiplicity=Multiplicity(0, 1))
    }
)
forType0: BinaryAssociation = BinaryAssociation(
    name="forType0",
    ends={
        Property(name="esm_DEntityType", type=esm_EsmEntityStateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmEntityStateModel", type=esm_DEntityType, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="esm_IEsmState", type=esm_IEsmStateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_IEsmStateModel", type=esm_IEsmState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="esm_EsmTransition", type=esm_IEsmStateModel, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_IEsmStateModel3", type=esm_EsmTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from10: BinaryAssociation = BinaryAssociation(
    name="from10",
    ends={
        Property(name="esm_DState12", type=esm_EsmTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmTransition11", type=esm_DState, multiplicity=Multiplicity(0, 1))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="esm_DState15", type=esm_EsmTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmTransition14", type=esm_DState, multiplicity=Multiplicity(0, 1))
    }
)
event16: BinaryAssociation = BinaryAssociation(
    name="event16",
    ends={
        Property(name="esm_DStateEvent", type=esm_EsmTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmTransition17", type=esm_DStateEvent, multiplicity=Multiplicity(0, 1))
    }
)
guard18: BinaryAssociation = BinaryAssociation(
    name="guard18",
    ends={
        Property(name="esm_DExpression20", type=esm_EsmTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmTransition19", type=esm_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description6: BinaryAssociation = BinaryAssociation(
    name="description6",
    ends={
        Property(name="esm_DRichText", type=esm_IEsmState, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_IEsmState7", type=esm_DRichText, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression8: BinaryAssociation = BinaryAssociation(
    name="expression8",
    ends={
        Property(name="esm_DExpression", type=esm_EsmDerivedState, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmDerivedState", type=esm_DExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subStates9: BinaryAssociation = BinaryAssociation(
    name="subStates9",
    ends={
        Property(name="esm_EsmSubStateModel", type=esm_EsmConcurrentState, multiplicity=Multiplicity(1, 1)),
        Property(name="esm_EsmConcurrentState", type=esm_EsmSubStateModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_esm_EsmEntityStateModel_DModel = Generalization(general=DModel, specific=esm_EsmEntityStateModel)
gen_esm_EsmEntityStateModel_IEsmStateModel = Generalization(general=IEsmStateModel, specific=esm_EsmEntityStateModel)
gen_esm_EsmEntityStateModel_INavigableMemberContainer = Generalization(general=INavigableMemberContainer, specific=esm_EsmEntityStateModel)
gen_esm_EsmEntityStateModel_IStaticReferenceTarget = Generalization(general=IStaticReferenceTarget, specific=esm_EsmEntityStateModel)
gen_esm_EsmEntityStateModel_IDiagramRoot = Generalization(general=IDiagramRoot, specific=esm_EsmEntityStateModel)
gen_esm_IEsmStateModel_IEsmLayout = Generalization(general=IEsmLayout, specific=esm_IEsmStateModel)
gen_esm_EsmState_IEsmState = Generalization(general=IEsmState, specific=esm_EsmState)
gen_esm_EsmDerivedState_EsmState = Generalization(general=EsmState, specific=esm_EsmDerivedState)
gen_esm_EsmCompositeState_IEsmState = Generalization(general=IEsmState, specific=esm_EsmCompositeState)
gen_esm_EsmCompositeState_IEsmStateModel = Generalization(general=IEsmStateModel, specific=esm_EsmCompositeState)
gen_esm_EsmConcurrentState_IEsmState = Generalization(general=IEsmState, specific=esm_EsmConcurrentState)
gen_esm_EsmSubStateModel_IEsmStateModel = Generalization(general=IEsmStateModel, specific=esm_EsmSubStateModel)
gen_esm_EsmTransition_IEsmLayout = Generalization(general=IEsmLayout, specific=esm_EsmTransition)

# Domain Model
domain_model = DomainModel(
    name="esm",
    types={esm_EsmEntityStateModel, DModel, esm_DState, esm_DRichText, IEsmStateModel, INavigableMemberContainer, IStaticReferenceTarget, IDiagramRoot, esm_DEntityType, esm_IEsmLayout, esm_IEsmStateModel, IEsmLayout, esm_IEsmState, esm_EsmTransition, esm_DStateEvent, esm_EsmState, IEsmState, esm_EsmDerivedState, EsmState, esm_DExpression, esm_EsmCompositeState, esm_EsmConcurrentState, esm_EsmSubStateModel, EsmLayoutDirection, EsmStateKind},
    associations={state4, forType0, states1, transitions2, from10, to13, event16, guard18, description6, expression8, subStates9},
    generalizations={gen_esm_EsmEntityStateModel_DModel, gen_esm_EsmEntityStateModel_IEsmStateModel, gen_esm_EsmEntityStateModel_INavigableMemberContainer, gen_esm_EsmEntityStateModel_IStaticReferenceTarget, gen_esm_EsmEntityStateModel_IDiagramRoot, gen_esm_IEsmStateModel_IEsmLayout, gen_esm_EsmState_IEsmState, gen_esm_EsmDerivedState_EsmState, gen_esm_EsmCompositeState_IEsmState, gen_esm_EsmCompositeState_IEsmStateModel, gen_esm_EsmConcurrentState_IEsmState, gen_esm_EsmSubStateModel_IEsmStateModel, gen_esm_EsmTransition_IEsmLayout},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)