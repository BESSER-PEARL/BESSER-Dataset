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
textlink_ModelLocation = Class(name="textlink_ModelLocation", is_abstract=True)
textlink_Trace = Class(name="textlink_Trace")
textlink_TraceLink = Class(name="textlink_TraceLink")
textlink_TextLocation = Class(name="textlink_TextLocation")
textlink_TraceLinkEnd = Class(name="textlink_TraceLinkEnd", is_abstract=True)
TraceLinkEnd = Class(name="TraceLinkEnd")
textlink_EmfModelLocation = Class(name="textlink_EmfModelLocation")
ModelLocation = Class(name="ModelLocation")
textlink_EObject = Class(name="textlink_EObject")
textlink_Region = Class(name="textlink_Region")

# textlink_ModelLocation class attributes and methods
textlink_ModelLocation_propertyName: Property = Property(name="propertyName", type=StringType)
textlink_ModelLocation.attributes={textlink_ModelLocation_propertyName}

# textlink_Trace class attributes and methods

# textlink_TraceLink class attributes and methods

# textlink_TextLocation class attributes and methods
textlink_TextLocation_resource: Property = Property(name="resource", type=StringType)
textlink_TextLocation.attributes={textlink_TextLocation_resource}

# textlink_TraceLinkEnd class attributes and methods

# TraceLinkEnd class attributes and methods

# textlink_EmfModelLocation class attributes and methods

# ModelLocation class attributes and methods

# textlink_EObject class attributes and methods

# textlink_Region class attributes and methods
textlink_Region_offset: Property = Property(name="offset", type=StringType)
textlink_Region_length: Property = Property(name="length", type=StringType)
textlink_Region.attributes={textlink_Region_length, textlink_Region_offset}

# Relationships
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="textlink_ModelLocation", type=textlink_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="textlink_TraceLink2", type=textlink_ModelLocation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traceLinks0: BinaryAssociation = BinaryAssociation(
    name="traceLinks0",
    ends={
        Property(name="textlink_TraceLink", type=textlink_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="textlink_Trace", type=textlink_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destination3: BinaryAssociation = BinaryAssociation(
    name="destination3",
    ends={
        Property(name="textlink_TextLocation", type=textlink_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="textlink_TraceLink4", type=textlink_TextLocation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelElement5: BinaryAssociation = BinaryAssociation(
    name="modelElement5",
    ends={
        Property(name="textlink_EObject", type=textlink_EmfModelLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="textlink_EmfModelLocation", type=textlink_EObject, multiplicity=Multiplicity(1, 1))
    }
)
region6: BinaryAssociation = BinaryAssociation(
    name="region6",
    ends={
        Property(name="textlink_Region", type=textlink_TextLocation, multiplicity=Multiplicity(1, 1)),
        Property(name="textlink_TextLocation7", type=textlink_Region, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_textlink_ModelLocation_TraceLinkEnd = Generalization(general=TraceLinkEnd, specific=textlink_ModelLocation)
gen_textlink_EmfModelLocation_ModelLocation = Generalization(general=ModelLocation, specific=textlink_EmfModelLocation)
gen_textlink_TextLocation_TraceLinkEnd = Generalization(general=TraceLinkEnd, specific=textlink_TextLocation)

# Domain Model
domain_model = DomainModel(
    name="textlink",
    types={textlink_ModelLocation, textlink_Trace, textlink_TraceLink, textlink_TextLocation, textlink_TraceLinkEnd, TraceLinkEnd, textlink_EmfModelLocation, ModelLocation, textlink_EObject, textlink_Region},
    associations={source1, traceLinks0, destination3, modelElement5, region6},
    generalizations={gen_textlink_ModelLocation_TraceLinkEnd, gen_textlink_EmfModelLocation_ModelLocation, gen_textlink_TextLocation_TraceLinkEnd},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)