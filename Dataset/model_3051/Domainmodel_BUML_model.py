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
domainmodel_PackageDeclaration = Class(name="domainmodel_PackageDeclaration")
domainmodel_Entity = Class(name="domainmodel_Entity")
domainmodel_Feature = Class(name="domainmodel_Feature")
domainmodel_JvmParameterizedTypeReference = Class(name="domainmodel_JvmParameterizedTypeReference")
domainmodel_DomainModel = Class(name="domainmodel_DomainModel")
domainmodel_AbstractElement = Class(name="domainmodel_AbstractElement")
domainmodel_Import = Class(name="domainmodel_Import")
AbstractElement = Class(name="AbstractElement")
domainmodel_JvmTypeReference = Class(name="domainmodel_JvmTypeReference")
domainmodel_Property = Class(name="domainmodel_Property")
Feature = Class(name="Feature")
domainmodel_Operation = Class(name="domainmodel_Operation")
domainmodel_JvmFormalParameter = Class(name="domainmodel_JvmFormalParameter")
domainmodel_XExpression = Class(name="domainmodel_XExpression")

# domainmodel_PackageDeclaration class attributes and methods
domainmodel_PackageDeclaration_name: Property = Property(name="name", type=StringType)
domainmodel_PackageDeclaration.attributes={domainmodel_PackageDeclaration_name}

# domainmodel_Entity class attributes and methods
domainmodel_Entity_name: Property = Property(name="name", type=StringType)
domainmodel_Entity.attributes={domainmodel_Entity_name}

# domainmodel_Feature class attributes and methods
domainmodel_Feature_name: Property = Property(name="name", type=StringType)
domainmodel_Feature.attributes={domainmodel_Feature_name}

# domainmodel_JvmParameterizedTypeReference class attributes and methods

# domainmodel_DomainModel class attributes and methods

# domainmodel_AbstractElement class attributes and methods

# domainmodel_Import class attributes and methods
domainmodel_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
domainmodel_Import.attributes={domainmodel_Import_importedNamespace}

# AbstractElement class attributes and methods

# domainmodel_JvmTypeReference class attributes and methods

# domainmodel_Property class attributes and methods

# Feature class attributes and methods

# domainmodel_Operation class attributes and methods

# domainmodel_JvmFormalParameter class attributes and methods

# domainmodel_XExpression class attributes and methods

# Relationships
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="domainmodel_AbstractElement2", type=domainmodel_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_PackageDeclaration", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="domainmodel_Feature", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity", type=domainmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="domainmodel_JvmParameterizedTypeReference", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity5", type=domainmodel_JvmParameterizedTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainmodel_AbstractElement", type=domainmodel_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_DomainModel", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="domainmodel_JvmTypeReference", type=domainmodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Feature7", type=domainmodel_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mappedBy9: BinaryAssociation = BinaryAssociation(
    name="mappedBy9",
    ends={
        Property(name="domainmodel_Property", type=domainmodel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Property8", type=domainmodel_Property, multiplicity=Multiplicity(0, 1))
    }
)
reflectsOn11: BinaryAssociation = BinaryAssociation(
    name="reflectsOn11",
    ends={
        Property(name="domainmodel_Property12", type=domainmodel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Property10", type=domainmodel_Property, multiplicity=Multiplicity(0, 1))
    }
)
params13: BinaryAssociation = BinaryAssociation(
    name="params13",
    ends={
        Property(name="domainmodel_JvmFormalParameter", type=domainmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Operation", type=domainmodel_JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body14: BinaryAssociation = BinaryAssociation(
    name="body14",
    ends={
        Property(name="domainmodel_XExpression", type=domainmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Operation15", type=domainmodel_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_domainmodel_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_PackageDeclaration)
gen_domainmodel_Entity_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_Entity)
gen_domainmodel_Import_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_Import)
gen_domainmodel_Property_Feature = Generalization(general=Feature, specific=domainmodel_Property)
gen_domainmodel_Operation_Feature = Generalization(general=Feature, specific=domainmodel_Operation)

# Domain Model
domain_model = DomainModel(
    name="domainmodel",
    types={domainmodel_PackageDeclaration, domainmodel_Entity, domainmodel_Feature, domainmodel_JvmParameterizedTypeReference, domainmodel_DomainModel, domainmodel_AbstractElement, domainmodel_Import, AbstractElement, domainmodel_JvmTypeReference, domainmodel_Property, Feature, domainmodel_Operation, domainmodel_JvmFormalParameter, domainmodel_XExpression},
    associations={elements1, features3, superType4, elements0, type6, mappedBy9, reflectsOn11, params13, body14},
    generalizations={gen_domainmodel_PackageDeclaration_AbstractElement, gen_domainmodel_Entity_AbstractElement, gen_domainmodel_Import_AbstractElement, gen_domainmodel_Property_Feature, gen_domainmodel_Operation_Feature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)