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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
    }
)

# Classes
domainmodel_DomainModel = Class(name="domainmodel::DomainModel")
domainmodel_AbstractElement = Class(name="domainmodel::AbstractElement")
domainmodel_Import = Class(name="domainmodel::Import")
AbstractElement = Class(name="AbstractElement")
domainmodel_PackageDeclaration = Class(name="domainmodel::PackageDeclaration")
domainmodel_Type = Class(name="domainmodel::Type")
domainmodel_Feature = Class(name="domainmodel::Feature")
TypedElement = Class(name="TypedElement")
domainmodel_StructuralFeature = Class(name="domainmodel::StructuralFeature")
Feature = Class(name="Feature")
domainmodel_Attribute = Class(name="domainmodel::Attribute")
StructuralFeature = Class(name="StructuralFeature")
domainmodel_Reference = Class(name="domainmodel::Reference")
domainmodel_Operation = Class(name="domainmodel::Operation")
domainmodel_Parameter = Class(name="domainmodel::Parameter")
domainmodel_TypedElement = Class(name="domainmodel::TypedElement")
domainmodel_TypeRef = Class(name="domainmodel::TypeRef")
domainmodel_DataType = Class(name="domainmodel::DataType")
Type = Class(name="Type")
domainmodel_Entity = Class(name="domainmodel::Entity")

# domainmodel_DomainModel class attributes and methods

# domainmodel_AbstractElement class attributes and methods

# domainmodel_Import class attributes and methods
domainmodel_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
domainmodel_Import.attributes={domainmodel_Import_importedNamespace}

# AbstractElement class attributes and methods

# domainmodel_PackageDeclaration class attributes and methods
domainmodel_PackageDeclaration_name: Property = Property(name="name", type=StringType)
domainmodel_PackageDeclaration.attributes={domainmodel_PackageDeclaration_name}

# domainmodel_Type class attributes and methods
domainmodel_Type_name: Property = Property(name="name", type=StringType)
domainmodel_Type.attributes={domainmodel_Type_name}

# domainmodel_Feature class attributes and methods

# TypedElement class attributes and methods

# domainmodel_StructuralFeature class attributes and methods

# Feature class attributes and methods

# domainmodel_Attribute class attributes and methods

# StructuralFeature class attributes and methods

# domainmodel_Reference class attributes and methods

# domainmodel_Operation class attributes and methods
domainmodel_Operation_visibility: Property = Property(name="visibility", type=StringType)
domainmodel_Operation.attributes={domainmodel_Operation_visibility}

# domainmodel_Parameter class attributes and methods

# domainmodel_TypedElement class attributes and methods
domainmodel_TypedElement_name: Property = Property(name="name", type=StringType)
domainmodel_TypedElement.attributes={domainmodel_TypedElement_name}

# domainmodel_TypeRef class attributes and methods
domainmodel_TypeRef_multi: Property = Property(name="multi", type=BooleanType)
domainmodel_TypeRef.attributes={domainmodel_TypeRef_multi}

# domainmodel_DataType class attributes and methods

# Type class attributes and methods

# domainmodel_Entity class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="domainmodel_AbstractElement", type=domainmodel_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_DomainModel", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="domainmodel_AbstractElement2", type=domainmodel_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_PackageDeclaration", type=domainmodel_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="domainmodel_Entity", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity3", type=domainmodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="domainmodel_Feature", type=domainmodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Entity6", type=domainmodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opposite8: BinaryAssociation = BinaryAssociation(
    name="opposite8",
    ends={
        Property(name="domainmodel_Reference", type=domainmodel_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Reference7", type=domainmodel_Reference, multiplicity=Multiplicity(0, 1))
    }
)
params9: BinaryAssociation = BinaryAssociation(
    name="params9",
    ends={
        Property(name="domainmodel_Parameter", type=domainmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_Operation", type=domainmodel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="domainmodel_TypeRef", type=domainmodel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_TypedElement", type=domainmodel_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referenced11: BinaryAssociation = BinaryAssociation(
    name="referenced11",
    ends={
        Property(name="domainmodel_Type", type=domainmodel_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="domainmodel_TypeRef12", type=domainmodel_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_domainmodel_Import_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_Import)
gen_domainmodel_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_PackageDeclaration)
gen_domainmodel_Type_AbstractElement = Generalization(general=AbstractElement, specific=domainmodel_Type)
gen_domainmodel_Feature_TypedElement = Generalization(general=TypedElement, specific=domainmodel_Feature)
gen_domainmodel_StructuralFeature_Feature = Generalization(general=Feature, specific=domainmodel_StructuralFeature)
gen_domainmodel_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=domainmodel_Attribute)
gen_domainmodel_Reference_StructuralFeature = Generalization(general=StructuralFeature, specific=domainmodel_Reference)
gen_domainmodel_Operation_Feature = Generalization(general=Feature, specific=domainmodel_Operation)
gen_domainmodel_Parameter_TypedElement = Generalization(general=TypedElement, specific=domainmodel_Parameter)
gen_domainmodel_DataType_Type = Generalization(general=Type, specific=domainmodel_DataType)
gen_domainmodel_Entity_Type = Generalization(general=Type, specific=domainmodel_Entity)

# Domain Model
domain_model = DomainModel(
    name="domainmodel",
    types={domainmodel_DomainModel, domainmodel_AbstractElement, domainmodel_Import, AbstractElement, domainmodel_PackageDeclaration, domainmodel_Type, domainmodel_Feature, TypedElement, domainmodel_StructuralFeature, Feature, domainmodel_Attribute, StructuralFeature, domainmodel_Reference, domainmodel_Operation, domainmodel_Parameter, domainmodel_TypedElement, domainmodel_TypeRef, domainmodel_DataType, Type, domainmodel_Entity, Visibility},
    associations={elements0, elements1, superType4, features5, opposite8, params9, type10, referenced11},
    generalizations={gen_domainmodel_Import_AbstractElement, gen_domainmodel_PackageDeclaration_AbstractElement, gen_domainmodel_Type_AbstractElement, gen_domainmodel_Feature_TypedElement, gen_domainmodel_StructuralFeature_Feature, gen_domainmodel_Attribute_StructuralFeature, gen_domainmodel_Reference_StructuralFeature, gen_domainmodel_Operation_Feature, gen_domainmodel_Parameter_TypedElement, gen_domainmodel_DataType_Type, gen_domainmodel_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)