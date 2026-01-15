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
extended_Import = Class(name="extended::Import")
extended_Domainmodel = Class(name="extended::Domainmodel")
extended_AbstractElement = Class(name="extended::AbstractElement")
extended_PackageDeclaration = Class(name="extended::PackageDeclaration")
AbstractElement = Class(name="AbstractElement")
extended_Page = Class(name="extended::Page")
extended_AbstractType = Class(name="extended::AbstractType")
extended_DataType = Class(name="extended::DataType")
AbstractType = Class(name="AbstractType")
extended_EntityType = Class(name="extended::EntityType")
extended_Entity = Class(name="extended::Entity")
extended_Feature = Class(name="extended::Feature")
extended_FormTypes = Class(name="extended::FormTypes")
extended_Form = Class(name="extended::Form")
FormTypes = Class(name="FormTypes")
extended_FormNewEntityOnly = Class(name="extended::FormNewEntityOnly")
extended_FormReport = Class(name="extended::FormReport")

# extended_Import class attributes and methods
extended_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
extended_Import.attributes={extended_Import_importedNamespace}

# extended_Domainmodel class attributes and methods
extended_Domainmodel_nomeProj: Property = Property(name="nomeProj", type=StringType)
extended_Domainmodel.attributes={extended_Domainmodel_nomeProj}

# extended_AbstractElement class attributes and methods

# extended_PackageDeclaration class attributes and methods
extended_PackageDeclaration_name: Property = Property(name="name", type=StringType)
extended_PackageDeclaration.attributes={extended_PackageDeclaration_name}

# AbstractElement class attributes and methods

# extended_Page class attributes and methods
extended_Page_name: Property = Property(name="name", type=StringType)
extended_Page_title: Property = Property(name="title", type=StringType)
extended_Page_header: Property = Property(name="header", type=StringType)
extended_Page_footer: Property = Property(name="footer", type=StringType)
extended_Page.attributes={extended_Page_title, extended_Page_header, extended_Page_footer, extended_Page_name}

# extended_AbstractType class attributes and methods

# extended_DataType class attributes and methods
extended_DataType_name: Property = Property(name="name", type=StringType)
extended_DataType.attributes={extended_DataType_name}

# AbstractType class attributes and methods

# extended_EntityType class attributes and methods

# extended_Entity class attributes and methods
extended_Entity_name: Property = Property(name="name", type=StringType)
extended_Entity.attributes={extended_Entity_name}

# extended_Feature class attributes and methods
extended_Feature_required: Property = Property(name="required", type=StringType)
extended_Feature_min: Property = Property(name="min", type=IntegerType)
extended_Feature_max: Property = Property(name="max", type=IntegerType)
extended_Feature_name: Property = Property(name="name", type=StringType)
extended_Feature.attributes={extended_Feature_name, extended_Feature_required, extended_Feature_max, extended_Feature_min}

# extended_FormTypes class attributes and methods
extended_FormTypes_name: Property = Property(name="name", type=StringType)
extended_FormTypes.attributes={extended_FormTypes_name}

# extended_Form class attributes and methods
extended_Form_get: Property = Property(name="get", type=StringType)
extended_Form_post: Property = Property(name="post", type=StringType)
extended_Form_put: Property = Property(name="put", type=StringType)
extended_Form_delete: Property = Property(name="delete", type=StringType)
extended_Form.attributes={extended_Form_delete, extended_Form_post, extended_Form_put, extended_Form_get}

# FormTypes class attributes and methods

# extended_FormNewEntityOnly class attributes and methods

# extended_FormReport class attributes and methods
extended_FormReport_filter: Property = Property(name="filter", type=StringType)
extended_FormReport_order: Property = Property(name="order", type=StringType)
extended_FormReport_pagination: Property = Property(name="pagination", type=StringType)
extended_FormReport.attributes={extended_FormReport_filter, extended_FormReport_pagination, extended_FormReport_order}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="extended_AbstractElement", type=extended_Domainmodel, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_Domainmodel", type=extended_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="extended_AbstractElement2", type=extended_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_PackageDeclaration", type=extended_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity3: BinaryAssociation = BinaryAssociation(
    name="entity3",
    ends={
        Property(name="extended_Entity", type=extended_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_EntityType", type=extended_Entity, multiplicity=Multiplicity(0, 1))
    }
)
superType5: BinaryAssociation = BinaryAssociation(
    name="superType5",
    ends={
        Property(name="extended_Entity6", type=extended_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_Entity4", type=extended_Entity, multiplicity=Multiplicity(0, 1))
    }
)
features7: BinaryAssociation = BinaryAssociation(
    name="features7",
    ends={
        Property(name="extended_Feature", type=extended_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_Entity8", type=extended_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="extended_AbstractType", type=extended_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_Feature10", type=extended_AbstractType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forms11: BinaryAssociation = BinaryAssociation(
    name="forms11",
    ends={
        Property(name="extended_FormTypes", type=extended_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_Page", type=extended_FormTypes, multiplicity=Multiplicity(0, 9999))
    }
)
entity12: BinaryAssociation = BinaryAssociation(
    name="entity12",
    ends={
        Property(name="extended_Entity14", type=extended_FormTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="extended_FormTypes13", type=extended_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_extended_Import_AbstractElement = Generalization(general=AbstractElement, specific=extended_Import)
gen_extended_PackageDeclaration_AbstractElement = Generalization(general=AbstractElement, specific=extended_PackageDeclaration)
gen_extended_Page_AbstractElement = Generalization(general=AbstractElement, specific=extended_Page)
gen_extended_DataType_AbstractType = Generalization(general=AbstractType, specific=extended_DataType)
gen_extended_EntityType_AbstractType = Generalization(general=AbstractType, specific=extended_EntityType)
gen_extended_Entity_AbstractElement = Generalization(general=AbstractElement, specific=extended_Entity)
gen_extended_FormTypes_AbstractElement = Generalization(general=AbstractElement, specific=extended_FormTypes)
gen_extended_Form_FormTypes = Generalization(general=FormTypes, specific=extended_Form)
gen_extended_FormNewEntityOnly_FormTypes = Generalization(general=FormTypes, specific=extended_FormNewEntityOnly)
gen_extended_FormReport_FormTypes = Generalization(general=FormTypes, specific=extended_FormReport)

# Domain Model
domain_model = DomainModel(
    name="extended",
    types={extended_Import, extended_Domainmodel, extended_AbstractElement, extended_PackageDeclaration, AbstractElement, extended_Page, extended_AbstractType, extended_DataType, AbstractType, extended_EntityType, extended_Entity, extended_Feature, extended_FormTypes, extended_Form, FormTypes, extended_FormNewEntityOnly, extended_FormReport},
    associations={elements0, elements1, entity3, superType5, features7, type9, forms11, entity12},
    generalizations={gen_extended_Import_AbstractElement, gen_extended_PackageDeclaration_AbstractElement, gen_extended_Page_AbstractElement, gen_extended_DataType_AbstractType, gen_extended_EntityType_AbstractType, gen_extended_Entity_AbstractElement, gen_extended_FormTypes_AbstractElement, gen_extended_Form_FormTypes, gen_extended_FormNewEntityOnly_FormTypes, gen_extended_FormReport_FormTypes},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)