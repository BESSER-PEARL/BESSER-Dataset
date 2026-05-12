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
Home__Component = Class(name="Home__Component")
Case_index_Component = Class(name="Case_index_Component")
Case_Create_Component = Class(name="Case_Create_Component")
Case_Details_Component = Class(name="Case_Details_Component")
Case_Edit_Component = Class(name="Case_Edit_Component")
User = Class(name="User")
Case_Index = Class(name="Case_Index")
RestServices = Class(name="RestServices")
Data_Basse = Class(name="Data_Basse")

# Home__Component class attributes and methods

# Case_index_Component class attributes and methods

# Case_Create_Component class attributes and methods

# Case_Details_Component class attributes and methods

# Case_Edit_Component class attributes and methods

# User class attributes and methods
User__scope_user___PA_SA: Property = Property(name="_scope_user___PA_SA", type=StringType)
User.attributes={User__scope_user___PA_SA}

# Case_Index class attributes and methods
Case_Index__scope_cases: Property = Property(name="_scope_cases", type=StringType)
Case_Index.attributes={Case_Index__scope_cases}

# RestServices class attributes and methods
RestServices_base_url: Property = Property(name="base_url", type=StringType)
RestServices.attributes={RestServices_base_url}

# Data_Basse class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_otEjkCdnEeiYD9TOdwevwA",
    types={Home__Component, Case_index_Component, Case_Create_Component, Case_Details_Component, Case_Edit_Component, User, Case_Index, RestServices, Data_Basse},
    associations={},
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