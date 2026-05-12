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
sql_SqlProvides = Class(name="sql_SqlProvides")
Provides = Class(name="Provides")

# sql_SqlProvides class attributes and methods
sql_SqlProvides_maxActive: Property = Property(name="maxActive", type=StringType)
sql_SqlProvides_url: Property = Property(name="url", type=StringType)
sql_SqlProvides_user: Property = Property(name="user", type=StringType)
sql_SqlProvides_password: Property = Property(name="password", type=StringType)
sql_SqlProvides_driver: Property = Property(name="driver", type=StringType)
sql_SqlProvides_storedProcedure: Property = Property(name="storedProcedure", type=StringType)
sql_SqlProvides_maxIdle: Property = Property(name="maxIdle", type=StringType)
sql_SqlProvides_minIdle: Property = Property(name="minIdle", type=StringType)
sql_SqlProvides_maxWait: Property = Property(name="maxWait", type=StringType)
sql_SqlProvides_timeBetweenEvictionRunsMillis: Property = Property(name="timeBetweenEvictionRunsMillis", type=StringType)
sql_SqlProvides_metadata: Property = Property(name="metadata", type=StringType)
sql_SqlProvides.attributes={sql_SqlProvides_password, sql_SqlProvides_maxActive, sql_SqlProvides_metadata, sql_SqlProvides_maxWait, sql_SqlProvides_url, sql_SqlProvides_minIdle, sql_SqlProvides_timeBetweenEvictionRunsMillis, sql_SqlProvides_user, sql_SqlProvides_storedProcedure, sql_SqlProvides_maxIdle, sql_SqlProvides_driver}

# Provides class attributes and methods

# Generalizations
gen_sql_SqlProvides_Provides = Generalization(general=Provides, specific=sql_SqlProvides)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_SqlProvides, Provides},
    associations={},
    generalizations={gen_sql_SqlProvides_Provides},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)