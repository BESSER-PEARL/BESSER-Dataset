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
attributes_A = Class(name="attributes_A")
attributes_R = Class(name="attributes_R")
attributes_DocumentRoot = Class(name="attributes_DocumentRoot")
attributes_EStringToStringMapEntry = Class(name="attributes_EStringToStringMapEntry")

# attributes_A class attributes and methods
attributes_A_name: Property = Property(name="name", type=StringType)
attributes_A_b: Property = Property(name="b", type=StringType)
attributes_A_c: Property = Property(name="c", type=StringType)
attributes_A_comment: Property = Property(name="comment", type=StringType)
attributes_A_id: Property = Property(name="id", type=StringType)
attributes_A_d: Property = Property(name="d", type=StringType)
attributes_A.attributes={attributes_A_d, attributes_A_b, attributes_A_c, attributes_A_comment, attributes_A_name, attributes_A_id}

# attributes_R class attributes and methods
attributes_R_name: Property = Property(name="name", type=StringType)
attributes_R.attributes={attributes_R_name}

# attributes_DocumentRoot class attributes and methods
attributes_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
attributes_DocumentRoot_comment: Property = Property(name="comment", type=StringType)
attributes_DocumentRoot.attributes={attributes_DocumentRoot_comment, attributes_DocumentRoot_mixed}

# attributes_EStringToStringMapEntry class attributes and methods

# Relationships
myR0: BinaryAssociation = BinaryAssociation(
    name="myR0",
    ends={
        Property(name="attributes_R", type=attributes_A, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes_A", type=attributes_R, multiplicity=Multiplicity(0, 1))
    }
)
xMLNSPrefixMap1: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap1",
    ends={
        Property(name="attributes_EStringToStringMapEntry", type=attributes_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes_DocumentRoot", type=attributes_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation2: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation2",
    ends={
        Property(name="attributes_EStringToStringMapEntry4", type=attributes_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes_DocumentRoot3", type=attributes_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="attributes",
    types={attributes_A, attributes_R, attributes_DocumentRoot, attributes_EStringToStringMapEntry},
    associations={myR0, xMLNSPrefixMap1, xSISchemaLocation2},
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