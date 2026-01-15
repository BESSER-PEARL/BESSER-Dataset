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
TraceMetamodel_TraceModel = Class(name="TraceMetamodel::TraceModel")
TraceMetamodel_TraceLink = Class(name="TraceMetamodel::TraceLink")
TraceMetamodel_TraceLinkEnd = Class(name="TraceMetamodel::TraceLinkEnd")
TraceMetamodel_EObject = Class(name="TraceMetamodel::EObject")

# TraceMetamodel_TraceModel class attributes and methods
TraceMetamodel_TraceModel_name: Property = Property(name="name", type=StringType)
TraceMetamodel_TraceModel.attributes={TraceMetamodel_TraceModel_name}

# TraceMetamodel_TraceLink class attributes and methods
TraceMetamodel_TraceLink_name: Property = Property(name="name", type=StringType)
TraceMetamodel_TraceLink_trule: Property = Property(name="trule", type=StringType)
TraceMetamodel_TraceLink_id: Property = Property(name="id", type=StringType)
TraceMetamodel_TraceLink_isPartial: Property = Property(name="isPartial", type=BooleanType)
TraceMetamodel_TraceLink_isNonInjective: Property = Property(name="isNonInjective", type=BooleanType)
TraceMetamodel_TraceLink.attributes={TraceMetamodel_TraceLink_id, TraceMetamodel_TraceLink_isNonInjective, TraceMetamodel_TraceLink_name, TraceMetamodel_TraceLink_isPartial, TraceMetamodel_TraceLink_trule}

# TraceMetamodel_TraceLinkEnd class attributes and methods
TraceMetamodel_TraceLinkEnd_name: Property = Property(name="name", type=StringType)
TraceMetamodel_TraceLinkEnd_type: Property = Property(name="type", type=StringType)
TraceMetamodel_TraceLinkEnd.attributes={TraceMetamodel_TraceLinkEnd_name, TraceMetamodel_TraceLinkEnd_type}

# TraceMetamodel_EObject class attributes and methods

# Relationships
traceLinks0: BinaryAssociation = BinaryAssociation(
    name="traceLinks0",
    ends={
        Property(name="TraceMetamodel_TraceLink", type=TraceMetamodel_TraceModel, multiplicity=Multiplicity(1, 1)),
        Property(name="TraceMetamodel_TraceModel", type=TraceMetamodel_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightLinkEnd1: BinaryAssociation = BinaryAssociation(
    name="rightLinkEnd1",
    ends={
        Property(name="TraceMetamodel_TraceLinkEnd", type=TraceMetamodel_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="TraceMetamodel_TraceLink2", type=TraceMetamodel_TraceLinkEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftLinkEnd3: BinaryAssociation = BinaryAssociation(
    name="leftLinkEnd3",
    ends={
        Property(name="TraceMetamodel_TraceLinkEnd5", type=TraceMetamodel_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="TraceMetamodel_TraceLink4", type=TraceMetamodel_TraceLinkEnd, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceElement6: BinaryAssociation = BinaryAssociation(
    name="traceElement6",
    ends={
        Property(name="TraceMetamodel_EObject", type=TraceMetamodel_TraceLinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="TraceMetamodel_TraceLinkEnd7", type=TraceMetamodel_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TraceMetamodel",
    types={TraceMetamodel_TraceModel, TraceMetamodel_TraceLink, TraceMetamodel_TraceLinkEnd, TraceMetamodel_EObject},
    associations={traceLinks0, rightLinkEnd1, leftLinkEnd3, traceElement6},
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