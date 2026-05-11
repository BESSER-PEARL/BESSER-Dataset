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
etrace_AbstractLink = Class(name="etrace_AbstractLink", is_abstract=True)
etrace_EObject = Class(name="etrace_EObject")
etrace_LinkType = Class(name="etrace_LinkType")
etrace_CompositeLink = Class(name="etrace_CompositeLink")
AbstractLink = Class(name="AbstractLink")
etrace_Link = Class(name="etrace_Link")
etrace_ETrace = Class(name="etrace_ETrace")
CompositeLink = Class(name="CompositeLink")

# etrace_AbstractLink class attributes and methods

# etrace_EObject class attributes and methods

# etrace_LinkType class attributes and methods
etrace_LinkType_description: Property = Property(name="description", type=StringType)
etrace_LinkType_purpose: Property = Property(name="purpose", type=StringType)
etrace_LinkType_uses: Property = Property(name="uses", type=StringType)
etrace_LinkType_example: Property = Property(name="example", type=StringType)
etrace_LinkType_name: Property = Property(name="name", type=StringType)
etrace_LinkType.attributes={etrace_LinkType_example, etrace_LinkType_uses, etrace_LinkType_purpose, etrace_LinkType_description, etrace_LinkType_name}

# etrace_CompositeLink class attributes and methods
etrace_CompositeLink_m_createLink: Method = Method(name="createLink", parameters={}, type=StringType)
etrace_CompositeLink_m_createLink: Method = Method(name="createLink", parameters={Parameter(name='etrace_target', type=StringType), Parameter(name='etrace_source', type=StringType), Parameter(name='etrace_type', type=StringType)}, type=StringType)
etrace_CompositeLink_m_createCompositeLink: Method = Method(name="createCompositeLink", parameters={}, type=CompositeLink)
etrace_CompositeLink_m_createCompositeLink: Method = Method(name="createCompositeLink", parameters={Parameter(name='etrace_type', type=StringType), Parameter(name='etrace_target', type=StringType), Parameter(name='etrace_source', type=StringType)}, type=CompositeLink)
etrace_CompositeLink_m_createCompositeLink: Method = Method(name="createCompositeLink", parameters={Parameter(name='etrace_target', type=StringType), Parameter(name='etrace_type', type=StringType), Parameter(name='etrace_links', type=StringType), Parameter(name='etrace_source', type=StringType)}, type=CompositeLink)
etrace_CompositeLink.methods={etrace_CompositeLink_m_createLink, etrace_CompositeLink_m_createLink, etrace_CompositeLink_m_createCompositeLink, etrace_CompositeLink_m_createCompositeLink, etrace_CompositeLink_m_createCompositeLink}

# AbstractLink class attributes and methods

# etrace_Link class attributes and methods

# etrace_ETrace class attributes and methods
etrace_ETrace_name: Property = Property(name="name", type=StringType)
etrace_ETrace.attributes={etrace_ETrace_name}

# CompositeLink class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="etrace_EObject", type=etrace_AbstractLink, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_AbstractLink", type=etrace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="etrace_EObject3", type=etrace_AbstractLink, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_AbstractLink2", type=etrace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="etrace_LinkType", type=etrace_AbstractLink, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_AbstractLink5", type=etrace_LinkType, multiplicity=Multiplicity(1, 1))
    }
)
subType7: BinaryAssociation = BinaryAssociation(
    name="subType7",
    ends={
        Property(name="LinkType", type=etrace_LinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="superType", type=etrace_LinkType, multiplicity=Multiplicity(0, 9999))
    }
)
externalElement16: BinaryAssociation = BinaryAssociation(
    name="externalElement16",
    ends={
        Property(name="etrace_EObject18", type=etrace_ETrace, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_ETrace17", type=etrace_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children19: BinaryAssociation = BinaryAssociation(
    name="children19",
    ends={
        Property(name="etrace_AbstractLink20", type=etrace_CompositeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_CompositeLink", type=etrace_AbstractLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType9: BinaryAssociation = BinaryAssociation(
    name="superType9",
    ends={
        Property(name="LinkType10", type=etrace_LinkType, multiplicity=Multiplicity(1, 1)),
        Property(name="subType", type=etrace_LinkType, multiplicity=Multiplicity(0, 1))
    }
)
typeList11: BinaryAssociation = BinaryAssociation(
    name="typeList11",
    ends={
        Property(name="etrace_LinkType12", type=etrace_ETrace, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_ETrace", type=etrace_LinkType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deletedElement13: BinaryAssociation = BinaryAssociation(
    name="deletedElement13",
    ends={
        Property(name="etrace_EObject15", type=etrace_ETrace, multiplicity=Multiplicity(1, 1)),
        Property(name="etrace_ETrace14", type=etrace_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_etrace_CompositeLink_AbstractLink = Generalization(general=AbstractLink, specific=etrace_CompositeLink)
gen_etrace_Link_AbstractLink = Generalization(general=AbstractLink, specific=etrace_Link)
gen_etrace_ETrace_CompositeLink = Generalization(general=CompositeLink, specific=etrace_ETrace)

# Domain Model
domain_model = DomainModel(
    name="etrace",
    types={etrace_AbstractLink, etrace_EObject, etrace_LinkType, etrace_CompositeLink, AbstractLink, etrace_Link, etrace_ETrace, CompositeLink},
    associations={source0, target1, type4, subType7, externalElement16, children19, superType9, typeList11, deletedElement13},
    generalizations={gen_etrace_CompositeLink_AbstractLink, gen_etrace_Link_AbstractLink, gen_etrace_ETrace_CompositeLink},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)