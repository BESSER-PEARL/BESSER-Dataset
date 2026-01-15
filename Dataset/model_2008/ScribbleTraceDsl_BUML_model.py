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
scribbleTraceDsl_Trace = Class(name="scribbleTraceDsl::Trace")
scribbleTraceDsl_Stepdefn = Class(name="scribbleTraceDsl::Stepdefn")
scribbleTraceDsl_Messagetransfer = Class(name="scribbleTraceDsl::Messagetransfer")
Stepdefn = Class(name="Stepdefn")
scribbleTraceDsl_Parameter = Class(name="scribbleTraceDsl::Parameter")

# scribbleTraceDsl_Trace class attributes and methods
scribbleTraceDsl_Trace_roles: Property = Property(name="roles", type=StringType)
scribbleTraceDsl_Trace.attributes={scribbleTraceDsl_Trace_roles}

# scribbleTraceDsl_Stepdefn class attributes and methods

# scribbleTraceDsl_Messagetransfer class attributes and methods

# Stepdefn class attributes and methods

# scribbleTraceDsl_Parameter class attributes and methods
scribbleTraceDsl_Parameter_type: Property = Property(name="type", type=StringType)
scribbleTraceDsl_Parameter_value: Property = Property(name="value", type=StringType)
scribbleTraceDsl_Parameter.attributes={scribbleTraceDsl_Parameter_type, scribbleTraceDsl_Parameter_value}

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="scribbleTraceDsl_Stepdefn", type=scribbleTraceDsl_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="scribbleTraceDsl_Trace", type=scribbleTraceDsl_Stepdefn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="scribbleTraceDsl_Parameter", type=scribbleTraceDsl_Messagetransfer, multiplicity=Multiplicity(1, 1)),
        Property(name="scribbleTraceDsl_Messagetransfer", type=scribbleTraceDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_scribbleTraceDsl_Messagetransfer_Stepdefn = Generalization(general=Stepdefn, specific=scribbleTraceDsl_Messagetransfer)

# Domain Model
domain_model = DomainModel(
    name="scribbleTraceDsl",
    types={scribbleTraceDsl_Trace, scribbleTraceDsl_Stepdefn, scribbleTraceDsl_Messagetransfer, Stepdefn, scribbleTraceDsl_Parameter},
    associations={steps0, parameters1},
    generalizations={gen_scribbleTraceDsl_Messagetransfer_Stepdefn},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)