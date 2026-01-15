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
archDSL_UncertainConnector = Class(name="archDSL::UncertainConnector")
archDSL_Connector = Class(name="archDSL::Connector")
archDSL_Model = Class(name="archDSL::Model")
archDSL_Interface = Class(name="archDSL::Interface")
archDSL_UncertainInterface = Class(name="archDSL::UncertainInterface")
archDSL_Behavior = Class(name="archDSL::Behavior")
archDSL_SuperMethod = Class(name="archDSL::SuperMethod")
archDSL_AltMethod = Class(name="archDSL::AltMethod")
archDSL_OptMethod = Class(name="archDSL::OptMethod")
archDSL_Method = Class(name="archDSL::Method")
SuperMethod = Class(name="SuperMethod")
archDSL_Param = Class(name="archDSL::Param")
archDSL_UncertainBehavior = Class(name="archDSL::UncertainBehavior")
archDSL_SuperCall = Class(name="archDSL::SuperCall")
archDSL_CertainCall = Class(name="archDSL::CertainCall")
SuperCall = Class(name="SuperCall")
archDSL_OptCall = Class(name="archDSL::OptCall")
archDSL_AltCall = Class(name="archDSL::AltCall")

# archDSL_UncertainConnector class attributes and methods
archDSL_UncertainConnector_name: Property = Property(name="name", type=StringType)
archDSL_UncertainConnector.attributes={archDSL_UncertainConnector_name}

# archDSL_Connector class attributes and methods
archDSL_Connector_name: Property = Property(name="name", type=StringType)
archDSL_Connector.attributes={archDSL_Connector_name}

# archDSL_Model class attributes and methods

# archDSL_Interface class attributes and methods
archDSL_Interface_name: Property = Property(name="name", type=StringType)
archDSL_Interface.attributes={archDSL_Interface_name}

# archDSL_UncertainInterface class attributes and methods
archDSL_UncertainInterface_name: Property = Property(name="name", type=StringType)
archDSL_UncertainInterface.attributes={archDSL_UncertainInterface_name}

# archDSL_Behavior class attributes and methods

# archDSL_SuperMethod class attributes and methods
archDSL_SuperMethod_name: Property = Property(name="name", type=StringType)
archDSL_SuperMethod.attributes={archDSL_SuperMethod_name}

# archDSL_AltMethod class attributes and methods
archDSL_AltMethod_type: Property = Property(name="type", type=StringType)
archDSL_AltMethod_a_name: Property = Property(name="a_name", type=StringType)
archDSL_AltMethod.attributes={archDSL_AltMethod_type, archDSL_AltMethod_a_name}

# archDSL_OptMethod class attributes and methods
archDSL_OptMethod_type: Property = Property(name="type", type=StringType)
archDSL_OptMethod.attributes={archDSL_OptMethod_type}

# archDSL_Method class attributes and methods
archDSL_Method_type: Property = Property(name="type", type=StringType)
archDSL_Method.attributes={archDSL_Method_type}

# SuperMethod class attributes and methods

# archDSL_Param class attributes and methods
archDSL_Param_type: Property = Property(name="type", type=StringType)
archDSL_Param_name: Property = Property(name="name", type=StringType)
archDSL_Param.attributes={archDSL_Param_type, archDSL_Param_name}

# archDSL_UncertainBehavior class attributes and methods
archDSL_UncertainBehavior_name: Property = Property(name="name", type=StringType)
archDSL_UncertainBehavior.attributes={archDSL_UncertainBehavior_name}

# archDSL_SuperCall class attributes and methods

# archDSL_CertainCall class attributes and methods

# SuperCall class attributes and methods

# archDSL_OptCall class attributes and methods

# archDSL_AltCall class attributes and methods
archDSL_AltCall_opt: Property = Property(name="opt", type=BooleanType)
archDSL_AltCall.attributes={archDSL_AltCall_opt}

# Relationships
u_connectors5: BinaryAssociation = BinaryAssociation(
    name="u_connectors5",
    ends={
        Property(name="archDSL_UncertainConnector", type=archDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Model6", type=archDSL_UncertainConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors7: BinaryAssociation = BinaryAssociation(
    name="connectors7",
    ends={
        Property(name="archDSL_Connector", type=archDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Model8", type=archDSL_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterface9: BinaryAssociation = BinaryAssociation(
    name="superInterface9",
    ends={
        Property(name="archDSL_Interface11", type=archDSL_UncertainInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainInterface10", type=archDSL_Interface, multiplicity=Multiplicity(0, 1))
    }
)
interfaces0: BinaryAssociation = BinaryAssociation(
    name="interfaces0",
    ends={
        Property(name="archDSL_Interface", type=archDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Model", type=archDSL_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
u_interfaces1: BinaryAssociation = BinaryAssociation(
    name="u_interfaces1",
    ends={
        Property(name="archDSL_UncertainInterface", type=archDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Model2", type=archDSL_UncertainInterface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviors3: BinaryAssociation = BinaryAssociation(
    name="behaviors3",
    ends={
        Property(name="archDSL_Behavior", type=archDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Model4", type=archDSL_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
call29: BinaryAssociation = BinaryAssociation(
    name="call29",
    ends={
        Property(name="archDSL_Behavior30", type=archDSL_Method, multiplicity=Multiplicity(0, 9999)),
        Property(name="archDSL_Method31", type=archDSL_Behavior, multiplicity=Multiplicity(1, 1))
    }
)
end32: BinaryAssociation = BinaryAssociation(
    name="end32",
    ends={
        Property(name="archDSL_Interface34", type=archDSL_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Behavior33", type=archDSL_Interface, multiplicity=Multiplicity(0, 1))
    }
)
param35: BinaryAssociation = BinaryAssociation(
    name="param35",
    ends={
        Property(name="archDSL_Param", type=archDSL_SuperMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_SuperMethod", type=archDSL_Param, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
altmethods12: BinaryAssociation = BinaryAssociation(
    name="altmethods12",
    ends={
        Property(name="archDSL_AltMethod", type=archDSL_UncertainInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainInterface13", type=archDSL_AltMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optmethods14: BinaryAssociation = BinaryAssociation(
    name="optmethods14",
    ends={
        Property(name="archDSL_OptMethod", type=archDSL_UncertainInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainInterface15", type=archDSL_OptMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods16: BinaryAssociation = BinaryAssociation(
    name="methods16",
    ends={
        Property(name="archDSL_Method", type=archDSL_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Interface17", type=archDSL_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviors18: BinaryAssociation = BinaryAssociation(
    name="behaviors18",
    ends={
        Property(name="archDSL_Behavior20", type=archDSL_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Connector19", type=archDSL_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterface21: BinaryAssociation = BinaryAssociation(
    name="superInterface21",
    ends={
        Property(name="archDSL_Interface23", type=archDSL_UncertainConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainConnector22", type=archDSL_Interface, multiplicity=Multiplicity(0, 1))
    }
)
u_behaviors24: BinaryAssociation = BinaryAssociation(
    name="u_behaviors24",
    ends={
        Property(name="archDSL_UncertainBehavior", type=archDSL_UncertainConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainConnector25", type=archDSL_UncertainBehavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interface26: BinaryAssociation = BinaryAssociation(
    name="interface26",
    ends={
        Property(name="archDSL_Interface28", type=archDSL_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_Behavior27", type=archDSL_Interface, multiplicity=Multiplicity(0, 1))
    }
)
call36: BinaryAssociation = BinaryAssociation(
    name="call36",
    ends={
        Property(name="archDSL_SuperCall", type=archDSL_UncertainBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainBehavior37", type=archDSL_SuperCall, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end38: BinaryAssociation = BinaryAssociation(
    name="end38",
    ends={
        Property(name="archDSL_Interface40", type=archDSL_UncertainBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_UncertainBehavior39", type=archDSL_Interface, multiplicity=Multiplicity(0, 1))
    }
)
a_name41: BinaryAssociation = BinaryAssociation(
    name="a_name41",
    ends={
        Property(name="archDSL_SuperMethod42", type=archDSL_AltCall, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_AltCall", type=archDSL_SuperMethod, multiplicity=Multiplicity(0, 9999))
    }
)
name43: BinaryAssociation = BinaryAssociation(
    name="name43",
    ends={
        Property(name="archDSL_SuperMethod45", type=archDSL_SuperCall, multiplicity=Multiplicity(1, 1)),
        Property(name="archDSL_SuperCall44", type=archDSL_SuperMethod, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_archDSL_Method_SuperMethod = Generalization(general=SuperMethod, specific=archDSL_Method)
gen_archDSL_AltMethod_SuperMethod = Generalization(general=SuperMethod, specific=archDSL_AltMethod)
gen_archDSL_OptMethod_SuperMethod = Generalization(general=SuperMethod, specific=archDSL_OptMethod)
gen_archDSL_CertainCall_SuperCall = Generalization(general=SuperCall, specific=archDSL_CertainCall)
gen_archDSL_OptCall_SuperCall = Generalization(general=SuperCall, specific=archDSL_OptCall)
gen_archDSL_AltCall_SuperCall = Generalization(general=SuperCall, specific=archDSL_AltCall)

# Domain Model
domain_model = DomainModel(
    name="archDSL",
    types={archDSL_UncertainConnector, archDSL_Connector, archDSL_Model, archDSL_Interface, archDSL_UncertainInterface, archDSL_Behavior, archDSL_SuperMethod, archDSL_AltMethod, archDSL_OptMethod, archDSL_Method, SuperMethod, archDSL_Param, archDSL_UncertainBehavior, archDSL_SuperCall, archDSL_CertainCall, SuperCall, archDSL_OptCall, archDSL_AltCall},
    associations={u_connectors5, connectors7, superInterface9, interfaces0, u_interfaces1, behaviors3, call29, end32, param35, altmethods12, optmethods14, methods16, behaviors18, superInterface21, u_behaviors24, interface26, call36, end38, a_name41, name43},
    generalizations={gen_archDSL_Method_SuperMethod, gen_archDSL_AltMethod_SuperMethod, gen_archDSL_OptMethod_SuperMethod, gen_archDSL_CertainCall_SuperCall, gen_archDSL_OptCall_SuperCall, gen_archDSL_AltCall_SuperCall},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)