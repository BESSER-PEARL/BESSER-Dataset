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
configDsl_Config = Class(name="configDsl::Config")
configDsl_Generator = Class(name="configDsl::Generator")

# configDsl_Config class attributes and methods
configDsl_Config_appName: Property = Property(name="appName", type=StringType)
configDsl_Config_mainClass: Property = Property(name="mainClass", type=StringType)
configDsl_Config_srcFolder: Property = Property(name="srcFolder", type=StringType)
configDsl_Config_outFolder: Property = Property(name="outFolder", type=StringType)
configDsl_Config.attributes={configDsl_Config_outFolder, configDsl_Config_srcFolder, configDsl_Config_mainClass, configDsl_Config_appName}

# configDsl_Generator class attributes and methods
configDsl_Generator_name: Property = Property(name="name", type=StringType)
configDsl_Generator_bundle: Property = Property(name="bundle", type=StringType)
configDsl_Generator_genClass: Property = Property(name="genClass", type=StringType)
configDsl_Generator.attributes={configDsl_Generator_bundle, configDsl_Generator_name, configDsl_Generator_genClass}

# Relationships
selectors0: BinaryAssociation = BinaryAssociation(
    name="selectors0",
    ends={
        Property(name="configDsl_Generator", type=configDsl_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="configDsl_Config", type=configDsl_Generator, multiplicity=Multiplicity(0, 9999))
    }
)
generators1: BinaryAssociation = BinaryAssociation(
    name="generators1",
    ends={
        Property(name="configDsl_Generator3", type=configDsl_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="configDsl_Config2", type=configDsl_Generator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="configDsl",
    types={configDsl_Config, configDsl_Generator},
    associations={selectors0, generators1},
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