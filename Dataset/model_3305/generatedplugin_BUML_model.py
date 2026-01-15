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
generatedplugin_DublinCore = Class(name="generatedplugin::DublinCore")
generatedplugin_Extension = Class(name="generatedplugin::Extension")
generatedplugin_StemCategory = Class(name="generatedplugin::StemCategory")
generatedplugin_Plugin = Class(name="generatedplugin::Plugin")

# generatedplugin_DublinCore class attributes and methods
generatedplugin_DublinCore_bibliographicCitation: Property = Property(name="bibliographicCitation", type=StringType)
generatedplugin_DublinCore_contributor: Property = Property(name="contributor", type=StringType)
generatedplugin_DublinCore_coverage: Property = Property(name="coverage", type=StringType)
generatedplugin_DublinCore_created: Property = Property(name="created", type=StringType)
generatedplugin_DublinCore_creator: Property = Property(name="creator", type=StringType)
generatedplugin_DublinCore_date: Property = Property(name="date", type=StringType)
generatedplugin_DublinCore_description: Property = Property(name="description", type=StringType)
generatedplugin_DublinCore_format: Property = Property(name="format", type=StringType)
generatedplugin_DublinCore_identifier: Property = Property(name="identifier", type=StringType)
generatedplugin_DublinCore_categoryId: Property = Property(name="categoryId", type=StringType)
generatedplugin_DublinCore_license: Property = Property(name="license", type=StringType)
generatedplugin_DublinCore_publisher: Property = Property(name="publisher", type=StringType)
generatedplugin_DublinCore_relation: Property = Property(name="relation", type=StringType)
generatedplugin_DublinCore_requires: Property = Property(name="requires", type=StringType)
generatedplugin_DublinCore_rights: Property = Property(name="rights", type=StringType)
generatedplugin_DublinCore_source: Property = Property(name="source", type=StringType)
generatedplugin_DublinCore_spatial: Property = Property(name="spatial", type=StringType)
generatedplugin_DublinCore_subject: Property = Property(name="subject", type=StringType)
generatedplugin_DublinCore_language: Property = Property(name="language", type=StringType)
generatedplugin_DublinCore_title: Property = Property(name="title", type=StringType)
generatedplugin_DublinCore_type: Property = Property(name="type", type=StringType)
generatedplugin_DublinCore_valid: Property = Property(name="valid", type=StringType)
generatedplugin_DublinCore.attributes={generatedplugin_DublinCore_date, generatedplugin_DublinCore_created, generatedplugin_DublinCore_license, generatedplugin_DublinCore_coverage, generatedplugin_DublinCore_contributor, generatedplugin_DublinCore_language, generatedplugin_DublinCore_categoryId, generatedplugin_DublinCore_source, generatedplugin_DublinCore_spatial, generatedplugin_DublinCore_rights, generatedplugin_DublinCore_publisher, generatedplugin_DublinCore_relation, generatedplugin_DublinCore_requires, generatedplugin_DublinCore_format, generatedplugin_DublinCore_description, generatedplugin_DublinCore_valid, generatedplugin_DublinCore_title, generatedplugin_DublinCore_identifier, generatedplugin_DublinCore_creator, generatedplugin_DublinCore_bibliographicCitation, generatedplugin_DublinCore_subject, generatedplugin_DublinCore_type}

# generatedplugin_Extension class attributes and methods
generatedplugin_Extension_point: Property = Property(name="point", type=StringType)
generatedplugin_Extension.attributes={generatedplugin_Extension_point}

# generatedplugin_StemCategory class attributes and methods
generatedplugin_StemCategory_id: Property = Property(name="id", type=StringType)
generatedplugin_StemCategory_name: Property = Property(name="name", type=StringType)
generatedplugin_StemCategory_parentId: Property = Property(name="parentId", type=StringType)
generatedplugin_StemCategory.attributes={generatedplugin_StemCategory_name, generatedplugin_StemCategory_id, generatedplugin_StemCategory_parentId}

# generatedplugin_Plugin class attributes and methods

# Relationships
categories0: BinaryAssociation = BinaryAssociation(
    name="categories0",
    ends={
        Property(name="generatedplugin_StemCategory", type=generatedplugin_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedplugin_Extension", type=generatedplugin_StemCategory, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dublinCores1: BinaryAssociation = BinaryAssociation(
    name="dublinCores1",
    ends={
        Property(name="generatedplugin_DublinCore", type=generatedplugin_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedplugin_Extension2", type=generatedplugin_DublinCore, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionelement3: BinaryAssociation = BinaryAssociation(
    name="extensionelement3",
    ends={
        Property(name="generatedplugin_Extension4", type=generatedplugin_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="generatedplugin_Plugin", type=generatedplugin_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="generatedplugin",
    types={generatedplugin_DublinCore, generatedplugin_Extension, generatedplugin_StemCategory, generatedplugin_Plugin},
    associations={categories0, dublinCores1, extensionelement3},
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