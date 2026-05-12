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
build_OptionInstance = Class(name="build_OptionInstance")
build_Build = Class(name="build_Build")
build_Configuration = Class(name="build_Configuration")
build_ModuleInstance = Class(name="build_ModuleInstance")
Instance = Class(name="Instance")
build_ModuleType = Class(name="build_ModuleType")
build_Include = Class(name="build_Include")
build_FileName = Class(name="build_FileName")
OptionBinding = Class(name="OptionBinding")

# build_OptionInstance class attributes and methods

# build_Build class attributes and methods

# build_Configuration class attributes and methods

# build_ModuleInstance class attributes and methods

# Instance class attributes and methods

# build_ModuleType class attributes and methods

# build_Include class attributes and methods

# build_FileName class attributes and methods

# OptionBinding class attributes and methods

# Relationships
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="build_ModuleInstance", type=build_ModuleType, multiplicity=Multiplicity(0, 1)),
        Property(name="build_ModuleType", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1))
    }
)
allTypes4: BinaryAssociation = BinaryAssociation(
    name="allTypes4",
    ends={
        Property(name="build_ModuleType6", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ModuleInstance5", type=build_ModuleType, multiplicity=Multiplicity(0, 9999))
    }
)
dependent8: BinaryAssociation = BinaryAssociation(
    name="dependent8",
    ends={
        Property(name="ModuleInstance9", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="depends", type=build_ModuleInstance, multiplicity=Multiplicity(0, 9999))
    }
)
depends11: BinaryAssociation = BinaryAssociation(
    name="depends11",
    ends={
        Property(name="ModuleInstance12", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="dependent", type=build_ModuleInstance, multiplicity=Multiplicity(0, 9999))
    }
)
contents14: BinaryAssociation = BinaryAssociation(
    name="contents14",
    ends={
        Property(name="ModuleInstance15", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=build_ModuleInstance, multiplicity=Multiplicity(0, 9999))
    }
)
container17: BinaryAssociation = BinaryAssociation(
    name="container17",
    ends={
        Property(name="ModuleInstance18", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=build_ModuleInstance, multiplicity=Multiplicity(0, 1))
    }
)
options19: BinaryAssociation = BinaryAssociation(
    name="options19",
    ends={
        Property(name="OptionInstance", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=build_OptionInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
afterDepends21: BinaryAssociation = BinaryAssociation(
    name="afterDepends21",
    ends={
        Property(name="build_ModuleInstance22", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ModuleInstance20", type=build_ModuleInstance, multiplicity=Multiplicity(0, 9999))
    }
)
configuration0: BinaryAssociation = BinaryAssociation(
    name="configuration0",
    ends={
        Property(name="build_Configuration", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build_Build", type=build_Configuration, multiplicity=Multiplicity(0, 1))
    }
)
modules1: BinaryAssociation = BinaryAssociation(
    name="modules1",
    ends={
        Property(name="ModuleInstance", type=build_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build", type=build_ModuleInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
build2: BinaryAssociation = BinaryAssociation(
    name="build2",
    ends={
        Property(name="Build", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="modules", type=build_Build, multiplicity=Multiplicity(0, 1))
    }
)
includeMember23: BinaryAssociation = BinaryAssociation(
    name="includeMember23",
    ends={
        Property(name="build_Include", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ModuleInstance24", type=build_Include, multiplicity=Multiplicity(0, 1))
    }
)
sources25: BinaryAssociation = BinaryAssociation(
    name="sources25",
    ends={
        Property(name="build_FileName", type=build_ModuleInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="build_ModuleInstance26", type=build_FileName, multiplicity=Multiplicity(0, 9999))
    }
)
module27: BinaryAssociation = BinaryAssociation(
    name="module27",
    ends={
        Property(name="ModuleInstance28", type=build_OptionInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="options", type=build_ModuleInstance, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_build_ModuleInstance_Instance = Generalization(general=Instance, specific=build_ModuleInstance)
gen_build_OptionInstance_OptionBinding = Generalization(general=OptionBinding, specific=build_OptionInstance)

# Domain Model
domain_model = DomainModel(
    name="build",
    types={build_OptionInstance, build_Build, build_Configuration, build_ModuleInstance, Instance, build_ModuleType, build_Include, build_FileName, OptionBinding},
    associations={type3, allTypes4, dependent8, depends11, contents14, container17, options19, afterDepends21, configuration0, modules1, build2, includeMember23, sources25, module27},
    generalizations={gen_build_ModuleInstance_Instance, gen_build_OptionInstance_OptionBinding},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)