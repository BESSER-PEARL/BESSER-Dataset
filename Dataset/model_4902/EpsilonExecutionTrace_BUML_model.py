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
base_ExecutionTrace = Class(name="base::ExecutionTrace", is_abstract=True)
base_Access = Class(name="base::Access", is_abstract=True)
base_ElementAccess = Class(name="base::ElementAccess")
Access = Class(name="Access")
base_ModelElementTrace = Class(name="base::ModelElementTrace")
base_AllInstancesAccess = Class(name="base::AllInstancesAccess")
base_ModelTypeTrace = Class(name="base::ModelTypeTrace")
base_PropertyAccess = Class(name="base::PropertyAccess")
base_PropertyTrace = Class(name="base::PropertyTrace")
base_IdElement = Class(name="base::IdElement", is_abstract=True)
base_ModuleTrace = Class(name="base::ModuleTrace", is_abstract=True)
IdElement = Class(name="IdElement")
base_ModelTrace = Class(name="base::ModelTrace")

# base_ExecutionTrace class attributes and methods

# base_Access class attributes and methods

# base_ElementAccess class attributes and methods

# Access class attributes and methods

# base_ModelElementTrace class attributes and methods
base_ModelElementTrace_uri: Property = Property(name="uri", type=StringType)
base_ModelElementTrace.attributes={base_ModelElementTrace_uri}

# base_AllInstancesAccess class attributes and methods
base_AllInstancesAccess_ofKind: Property = Property(name="ofKind", type=BooleanType)
base_AllInstancesAccess.attributes={base_AllInstancesAccess_ofKind}

# base_ModelTypeTrace class attributes and methods
base_ModelTypeTrace_name: Property = Property(name="name", type=StringType)
base_ModelTypeTrace.attributes={base_ModelTypeTrace_name}

# base_PropertyAccess class attributes and methods
base_PropertyAccess_value: Property = Property(name="value", type=StringType)
base_PropertyAccess.attributes={base_PropertyAccess_value}

# base_PropertyTrace class attributes and methods
base_PropertyTrace_name: Property = Property(name="name", type=StringType)
base_PropertyTrace.attributes={base_PropertyTrace_name}

# base_IdElement class attributes and methods
base_IdElement_id: Property = Property(name="id", type=StringType)
base_IdElement.attributes={base_IdElement_id}

# base_ModuleTrace class attributes and methods
base_ModuleTrace_source: Property = Property(name="source", type=StringType)
base_ModuleTrace.attributes={base_ModuleTrace_source}

# IdElement class attributes and methods

# base_ModelTrace class attributes and methods
base_ModelTrace_name: Property = Property(name="name", type=StringType)
base_ModelTrace.attributes={base_ModelTrace_name}

# Relationships
accesses0: BinaryAssociation = BinaryAssociation(
    name="accesses0",
    ends={
        Property(name="base_Access", type=base_ExecutionTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="base_ExecutionTrace", type=base_Access, multiplicity=Multiplicity(1, 9999))
    }
)
element1: BinaryAssociation = BinaryAssociation(
    name="element1",
    ends={
        Property(name="base_ModelElementTrace", type=base_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="base_ElementAccess", type=base_ModelElementTrace, multiplicity=Multiplicity(1, 1))
    }
)
type2: BinaryAssociation = BinaryAssociation(
    name="type2",
    ends={
        Property(name="base_ModelTypeTrace", type=base_AllInstancesAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="base_AllInstancesAccess", type=base_ModelTypeTrace, multiplicity=Multiplicity(1, 1))
    }
)
element9: BinaryAssociation = BinaryAssociation(
    name="element9",
    ends={
        Property(name="base_ModelElementTrace11", type=base_PropertyTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="base_PropertyTrace10", type=base_ModelElementTrace, multiplicity=Multiplicity(1, 1))
    }
)
property3: BinaryAssociation = BinaryAssociation(
    name="property3",
    ends={
        Property(name="base_PropertyTrace", type=base_PropertyAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="base_PropertyAccess", type=base_PropertyTrace, multiplicity=Multiplicity(1, 1))
    }
)
model4: BinaryAssociation = BinaryAssociation(
    name="model4",
    ends={
        Property(name="base_ModelTrace", type=base_ModelTypeTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="base_ModelTypeTrace5", type=base_ModelTrace, multiplicity=Multiplicity(1, 1))
    }
)
model6: BinaryAssociation = BinaryAssociation(
    name="model6",
    ends={
        Property(name="base_ModelTrace8", type=base_ModelElementTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="base_ModelElementTrace7", type=base_ModelTrace, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_base_ExecutionTrace_IdElement = Generalization(general=IdElement, specific=base_ExecutionTrace)
gen_base_Access_IdElement = Generalization(general=IdElement, specific=base_Access)
gen_base_ElementAccess_Access = Generalization(general=Access, specific=base_ElementAccess)
gen_base_AllInstancesAccess_Access = Generalization(general=Access, specific=base_AllInstancesAccess)
gen_base_PropertyAccess_Access = Generalization(general=Access, specific=base_PropertyAccess)
gen_base_ModuleTrace_IdElement = Generalization(general=IdElement, specific=base_ModuleTrace)
gen_base_PropertyTrace_IdElement = Generalization(general=IdElement, specific=base_PropertyTrace)
gen_base_ModelTrace_IdElement = Generalization(general=IdElement, specific=base_ModelTrace)
gen_base_ModelTypeTrace_IdElement = Generalization(general=IdElement, specific=base_ModelTypeTrace)
gen_base_ModelElementTrace_IdElement = Generalization(general=IdElement, specific=base_ModelElementTrace)

# Domain Model
domain_model = DomainModel(
    name="base",
    types={base_ExecutionTrace, base_Access, base_ElementAccess, Access, base_ModelElementTrace, base_AllInstancesAccess, base_ModelTypeTrace, base_PropertyAccess, base_PropertyTrace, base_IdElement, base_ModuleTrace, IdElement, base_ModelTrace},
    associations={accesses0, element1, type2, element9, property3, model4, model6},
    generalizations={gen_base_ExecutionTrace_IdElement, gen_base_Access_IdElement, gen_base_ElementAccess_Access, gen_base_AllInstancesAccess_Access, gen_base_PropertyAccess_Access, gen_base_ModuleTrace_IdElement, gen_base_PropertyTrace_IdElement, gen_base_ModelTrace_IdElement, gen_base_ModelTypeTrace_IdElement, gen_base_ModelElementTrace_IdElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)