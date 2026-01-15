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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Double"),
			EnumerationLiteral(name="Void")
    }
)

# Classes
architecture_Component = Class(name="architecture::Component")
architecture_Architecture = Class(name="architecture::Architecture")
architecture_Model = Class(name="architecture::Model")
architecture_DomainDeclaration = Class(name="architecture::DomainDeclaration")
architecture_AbstractModel = Class(name="architecture::AbstractModel")
architecture_Import = Class(name="architecture::Import")
architecture_Binding = Class(name="architecture::Binding")
architecture_Operation = Class(name="architecture::Operation")
architecture_Variable = Class(name="architecture::Variable")
architecture_AtomicType = Class(name="architecture::AtomicType")

# architecture_Component class attributes and methods
architecture_Component_name: Property = Property(name="name", type=StringType)
architecture_Component.attributes={architecture_Component_name}

# architecture_Architecture class attributes and methods

# architecture_Model class attributes and methods

# architecture_DomainDeclaration class attributes and methods
architecture_DomainDeclaration_name: Property = Property(name="name", type=StringType)
architecture_DomainDeclaration.attributes={architecture_DomainDeclaration_name}

# architecture_AbstractModel class attributes and methods

# architecture_Import class attributes and methods
architecture_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
architecture_Import.attributes={architecture_Import_importedNamespace}

# architecture_Binding class attributes and methods

# architecture_Operation class attributes and methods
architecture_Operation_name: Property = Property(name="name", type=StringType)
architecture_Operation.attributes={architecture_Operation_name}

# architecture_Variable class attributes and methods
architecture_Variable_name: Property = Property(name="name", type=StringType)
architecture_Variable.attributes={architecture_Variable_name}

# architecture_AtomicType class attributes and methods
architecture_AtomicType_atomType: Property = Property(name="atomType", type=StringType)
architecture_AtomicType.attributes={architecture_AtomicType_atomType}

# Relationships
imp3: BinaryAssociation = BinaryAssociation(
    name="imp3",
    ends={
        Property(name="architecture_AbstractModel4", type=architecture_Import, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="architecture_Import", type=architecture_AbstractModel, multiplicity=Multiplicity(1, 1))
    }
)
comp5: BinaryAssociation = BinaryAssociation(
    name="comp5",
    ends={
        Property(name="architecture_Component", type=architecture_AbstractModel, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_AbstractModel6", type=architecture_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arch7: BinaryAssociation = BinaryAssociation(
    name="arch7",
    ends={
        Property(name="architecture_Architecture", type=architecture_AbstractModel, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_AbstractModel8", type=architecture_Architecture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="architecture_DomainDeclaration", type=architecture_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Model", type=architecture_DomainDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="architecture_AbstractModel", type=architecture_DomainDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_DomainDeclaration2", type=architecture_AbstractModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bind19: BinaryAssociation = BinaryAssociation(
    name="bind19",
    ends={
        Property(name="architecture_Binding", type=architecture_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Architecture20", type=architecture_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
provider21: BinaryAssociation = BinaryAssociation(
    name="provider21",
    ends={
        Property(name="architecture_Variable23", type=architecture_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Binding22", type=architecture_Variable, multiplicity=Multiplicity(0, 1))
    }
)
proMember24: BinaryAssociation = BinaryAssociation(
    name="proMember24",
    ends={
        Property(name="architecture_Operation26", type=architecture_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Binding25", type=architecture_Operation, multiplicity=Multiplicity(0, 1))
    }
)
ops9: BinaryAssociation = BinaryAssociation(
    name="ops9",
    ends={
        Property(name="architecture_Operation", type=architecture_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Component10", type=architecture_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
opsReq11: BinaryAssociation = BinaryAssociation(
    name="opsReq11",
    ends={
        Property(name="architecture_Operation13", type=architecture_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Component12", type=architecture_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
operations14: BinaryAssociation = BinaryAssociation(
    name="operations14",
    ends={
        Property(name="architecture_Operation16", type=architecture_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Component15", type=architecture_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vars17: BinaryAssociation = BinaryAssociation(
    name="vars17",
    ends={
        Property(name="architecture_Variable", type=architecture_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Architecture18", type=architecture_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="architecture_AtomicType40", type=architecture_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Operation39", type=architecture_AtomicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compType41: BinaryAssociation = BinaryAssociation(
    name="compType41",
    ends={
        Property(name="architecture_Component43", type=architecture_AtomicType, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_AtomicType42", type=architecture_Component, multiplicity=Multiplicity(0, 1))
    }
)
receiver27: BinaryAssociation = BinaryAssociation(
    name="receiver27",
    ends={
        Property(name="architecture_Variable29", type=architecture_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Binding28", type=architecture_Variable, multiplicity=Multiplicity(0, 1))
    }
)
recMember30: BinaryAssociation = BinaryAssociation(
    name="recMember30",
    ends={
        Property(name="architecture_Operation32", type=architecture_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Binding31", type=architecture_Operation, multiplicity=Multiplicity(0, 1))
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="architecture_AtomicType", type=architecture_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Variable34", type=architecture_AtomicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arg35: BinaryAssociation = BinaryAssociation(
    name="arg35",
    ends={
        Property(name="architecture_Variable37", type=architecture_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="architecture_Operation36", type=architecture_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="architecture",
    types={architecture_Component, architecture_Architecture, architecture_Model, architecture_DomainDeclaration, architecture_AbstractModel, architecture_Import, architecture_Binding, architecture_Operation, architecture_Variable, architecture_AtomicType, Type},
    associations={imp3, comp5, arch7, package0, elements1, bind19, provider21, proMember24, ops9, opsReq11, operations14, vars17, type38, compType41, receiver27, recMember30, type33, arg35},
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