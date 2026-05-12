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
QuotaType: Enumeration = Enumeration(
    name="QuotaType",
    literals={
            
    }
)

# Classes
Quota = Class(name="Quota")
QuotaItem = Class(name="QuotaItem")

# Quota class attributes and methods
Quota_id: Property = Property(name="id", type=StringType)
Quota_quotaName: Property = Property(name="quotaName", type=StringType)
Quota_current: Property = Property(name="current", type=IntegerType)
Quota_max: Property = Property(name="max", type=IntegerType)
Quota_comment: Property = Property(name="comment", type=StringType)
Quota.attributes={Quota_id, Quota_max, Quota_quotaName, Quota_comment, Quota_current}

# QuotaItem class attributes and methods
QuotaItem_id: Property = Property(name="id", type=StringType)
QuotaItem_quotaItemName: Property = Property(name="quotaItemName", type=StringType)
QuotaItem_amount: Property = Property(name="amount", type=IntegerType)
QuotaItem_comment: Property = Property(name="comment", type=StringType)
QuotaItem_createdOn: Property = Property(name="createdOn", type=StringType)
QuotaItem_type: Property = Property(name="type", type=QuotaType)
QuotaItem_sueprClassId: Property = Property(name="sueprClassId", type=StringType)
QuotaItem.attributes={QuotaItem_comment, QuotaItem_amount, QuotaItem_quotaItemName, QuotaItem_type, QuotaItem_sueprClassId, QuotaItem_id, QuotaItem_createdOn}

# Relationships
Quota_QuotaItem: BinaryAssociation = BinaryAssociation(
    name="Quota_QuotaItem",
    ends={
        Property(name="quotaItem0", type=QuotaItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="quota1", type=Quota, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_n7RpQM3NEeeMV96X50GAvA",
    types={Quota, QuotaItem, QuotaType},
    associations={Quota_QuotaItem},
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