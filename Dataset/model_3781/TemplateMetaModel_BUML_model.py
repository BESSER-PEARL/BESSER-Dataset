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
product_Product = Class(name="product::Product")
product_ProductImplementationElements = Class(name="product::ProductImplementationElements")
product_ProductFeaturesConfiguration = Class(name="product::ProductFeaturesConfiguration")
product_ProductDomainModels = Class(name="product::ProductDomainModels")
product_ProductContainer = Class(name="product::ProductContainer")
product_ProductFragmentContainer = Class(name="product::ProductFragmentContainer")
product_ProductResourcesContainer = Class(name="product::ProductResourcesContainer")
product_ProductComponent = Class(name="product::ProductComponent")
product_ProductFolder = Class(name="product::ProductFolder")
product_ProductFile = Class(name="product::ProductFile")
product_ProductTemplate = Class(name="product::ProductTemplate")
product_ProductEntity = Class(name="product::ProductEntity")
ProductEntity = Class(name="ProductEntity")
product_ProductClass = Class(name="product::ProductClass")
product_ProductAspect = Class(name="product::ProductAspect")
product_ProductFragment = Class(name="product::ProductFragment")
product_ProductFeatureConfiguration = Class(name="product::ProductFeatureConfiguration")
product_ProductDomainModel = Class(name="product::ProductDomainModel")

# product_Product class attributes and methods

# product_ProductImplementationElements class attributes and methods

# product_ProductFeaturesConfiguration class attributes and methods
product_ProductFeaturesConfiguration_name: Property = Property(name="name", type=StringType)
product_ProductFeaturesConfiguration_attribute: Property = Property(name="attribute", type=StringType)
product_ProductFeaturesConfiguration.attributes={product_ProductFeaturesConfiguration_name, product_ProductFeaturesConfiguration_attribute}

# product_ProductDomainModels class attributes and methods

# product_ProductContainer class attributes and methods
product_ProductContainer_name: Property = Property(name="name", type=StringType)
product_ProductContainer.attributes={product_ProductContainer_name}

# product_ProductFragmentContainer class attributes and methods
product_ProductFragmentContainer_name: Property = Property(name="name", type=StringType)
product_ProductFragmentContainer.attributes={product_ProductFragmentContainer_name}

# product_ProductResourcesContainer class attributes and methods
product_ProductResourcesContainer_name: Property = Property(name="name", type=StringType)
product_ProductResourcesContainer.attributes={product_ProductResourcesContainer_name}

# product_ProductComponent class attributes and methods

# product_ProductFolder class attributes and methods

# product_ProductFile class attributes and methods

# product_ProductTemplate class attributes and methods
product_ProductTemplate_generateToPath: Property = Property(name="generateToPath", type=StringType)
product_ProductTemplate.attributes={product_ProductTemplate_generateToPath}

# product_ProductEntity class attributes and methods
product_ProductEntity_name: Property = Property(name="name", type=StringType)
product_ProductEntity_path: Property = Property(name="path", type=StringType)
product_ProductEntity.attributes={product_ProductEntity_path, product_ProductEntity_name}

# ProductEntity class attributes and methods

# product_ProductClass class attributes and methods

# product_ProductAspect class attributes and methods

# product_ProductFragment class attributes and methods
product_ProductFragment_content: Property = Property(name="content", type=StringType)
product_ProductFragment.attributes={product_ProductFragment_content}

# product_ProductFeatureConfiguration class attributes and methods
product_ProductFeatureConfiguration_name: Property = Property(name="name", type=StringType)
product_ProductFeatureConfiguration_attribute: Property = Property(name="attribute", type=StringType)
product_ProductFeatureConfiguration_max: Property = Property(name="max", type=IntegerType)
product_ProductFeatureConfiguration_min: Property = Property(name="min", type=IntegerType)
product_ProductFeatureConfiguration_isSelected: Property = Property(name="isSelected", type=BooleanType)
product_ProductFeatureConfiguration.attributes={product_ProductFeatureConfiguration_min, product_ProductFeatureConfiguration_attribute, product_ProductFeatureConfiguration_isSelected, product_ProductFeatureConfiguration_name, product_ProductFeatureConfiguration_max}

# product_ProductDomainModel class attributes and methods
product_ProductDomainModel_name: Property = Property(name="name", type=StringType)
product_ProductDomainModel_elements: Property = Property(name="elements", type=StringType)
product_ProductDomainModel.attributes={product_ProductDomainModel_name, product_ProductDomainModel_elements}

# Relationships
productImplementationElements0: BinaryAssociation = BinaryAssociation(
    name="productImplementationElements0",
    ends={
        Property(name="product_ProductImplementationElements", type=product_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="product_Product", type=product_ProductImplementationElements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
productFeatures1: BinaryAssociation = BinaryAssociation(
    name="productFeatures1",
    ends={
        Property(name="product_ProductFeaturesConfiguration", type=product_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="product_Product2", type=product_ProductFeaturesConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domainModels3: BinaryAssociation = BinaryAssociation(
    name="domainModels3",
    ends={
        Property(name="product_ProductDomainModels", type=product_Product, multiplicity=Multiplicity(1, 1)),
        Property(name="product_Product4", type=product_ProductDomainModels, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containers5: BinaryAssociation = BinaryAssociation(
    name="containers5",
    ends={
        Property(name="product_ProductContainer", type=product_ProductImplementationElements, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductImplementationElements6", type=product_ProductContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragmentContainers7: BinaryAssociation = BinaryAssociation(
    name="fragmentContainers7",
    ends={
        Property(name="product_ProductFragmentContainer", type=product_ProductImplementationElements, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductImplementationElements8", type=product_ProductFragmentContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceContainers9: BinaryAssociation = BinaryAssociation(
    name="resourceContainers9",
    ends={
        Property(name="product_ProductResourcesContainer", type=product_ProductImplementationElements, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductImplementationElements10", type=product_ProductResourcesContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components11: BinaryAssociation = BinaryAssociation(
    name="components11",
    ends={
        Property(name="product_ProductComponent", type=product_ProductContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductContainer12", type=product_ProductComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
folders13: BinaryAssociation = BinaryAssociation(
    name="folders13",
    ends={
        Property(name="product_ProductFolder", type=product_ProductResourcesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductResourcesContainer14", type=product_ProductFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files15: BinaryAssociation = BinaryAssociation(
    name="files15",
    ends={
        Property(name="product_ProductFile", type=product_ProductResourcesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductResourcesContainer16", type=product_ProductFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templates17: BinaryAssociation = BinaryAssociation(
    name="templates17",
    ends={
        Property(name="product_ProductTemplate", type=product_ProductResourcesContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductResourcesContainer18", type=product_ProductTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes19: BinaryAssociation = BinaryAssociation(
    name="classes19",
    ends={
        Property(name="product_ProductClass", type=product_ProductComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductComponent20", type=product_ProductClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aspects21: BinaryAssociation = BinaryAssociation(
    name="aspects21",
    ends={
        Property(name="product_ProductAspect", type=product_ProductComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductComponent22", type=product_ProductAspect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files23: BinaryAssociation = BinaryAssociation(
    name="files23",
    ends={
        Property(name="product_ProductFile25", type=product_ProductComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductComponent24", type=product_ProductFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templates26: BinaryAssociation = BinaryAssociation(
    name="templates26",
    ends={
        Property(name="product_ProductTemplate28", type=product_ProductComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductComponent27", type=product_ProductTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subComponents30: BinaryAssociation = BinaryAssociation(
    name="subComponents30",
    ends={
        Property(name="product_ProductComponent31", type=product_ProductComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductComponent29", type=product_ProductComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subFolders33: BinaryAssociation = BinaryAssociation(
    name="subFolders33",
    ends={
        Property(name="product_ProductFolder34", type=product_ProductFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductFolder32", type=product_ProductFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files35: BinaryAssociation = BinaryAssociation(
    name="files35",
    ends={
        Property(name="product_ProductFile37", type=product_ProductFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductFolder36", type=product_ProductFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templates38: BinaryAssociation = BinaryAssociation(
    name="templates38",
    ends={
        Property(name="product_ProductTemplate40", type=product_ProductFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductFolder39", type=product_ProductTemplate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments41: BinaryAssociation = BinaryAssociation(
    name="fragments41",
    ends={
        Property(name="product_ProductFragment", type=product_ProductFragmentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductFragmentContainer42", type=product_ProductFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features43: BinaryAssociation = BinaryAssociation(
    name="features43",
    ends={
        Property(name="product_ProductFeatureConfiguration", type=product_ProductFeaturesConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductFeaturesConfiguration44", type=product_ProductFeatureConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features46: BinaryAssociation = BinaryAssociation(
    name="features46",
    ends={
        Property(name="product_ProductFeatureConfiguration47", type=product_ProductFeatureConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductFeatureConfiguration45", type=product_ProductFeatureConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domainModel48: BinaryAssociation = BinaryAssociation(
    name="domainModel48",
    ends={
        Property(name="product_ProductDomainModel", type=product_ProductDomainModels, multiplicity=Multiplicity(1, 1)),
        Property(name="product_ProductDomainModels49", type=product_ProductDomainModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_product_ProductComponent_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductComponent)
gen_product_ProductClass_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductClass)
gen_product_ProductAspect_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductAspect)
gen_product_ProductFile_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductFile)
gen_product_ProductFolder_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductFolder)
gen_product_ProductTemplate_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductTemplate)
gen_product_ProductFragment_ProductEntity = Generalization(general=ProductEntity, specific=product_ProductFragment)

# Domain Model
domain_model = DomainModel(
    name="product",
    types={product_Product, product_ProductImplementationElements, product_ProductFeaturesConfiguration, product_ProductDomainModels, product_ProductContainer, product_ProductFragmentContainer, product_ProductResourcesContainer, product_ProductComponent, product_ProductFolder, product_ProductFile, product_ProductTemplate, product_ProductEntity, ProductEntity, product_ProductClass, product_ProductAspect, product_ProductFragment, product_ProductFeatureConfiguration, product_ProductDomainModel},
    associations={productImplementationElements0, productFeatures1, domainModels3, containers5, fragmentContainers7, resourceContainers9, components11, folders13, files15, templates17, classes19, aspects21, files23, templates26, subComponents30, subFolders33, files35, templates38, fragments41, features43, features46, domainModel48},
    generalizations={gen_product_ProductComponent_ProductEntity, gen_product_ProductClass_ProductEntity, gen_product_ProductAspect_ProductEntity, gen_product_ProductFile_ProductEntity, gen_product_ProductFolder_ProductEntity, gen_product_ProductTemplate_ProductEntity, gen_product_ProductFragment_ProductEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)