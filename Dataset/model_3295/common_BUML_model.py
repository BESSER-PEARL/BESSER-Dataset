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
common_Identifiable = Class(name="common::Identifiable", is_abstract=True)
common_Comparable = Class(name="common::Comparable", is_abstract=True)
common_IdentifiableFilter = Class(name="common::IdentifiableFilter")
common_DoubleValueList = Class(name="common::DoubleValueList")
common_DublinCore = Class(name="common::DublinCore")
common_DoubleValue = Class(name="common::DoubleValue")
common_DoubleValueMatrix = Class(name="common::DoubleValueMatrix")
Modifiable = Class(name="Modifiable")
common_StringValueList = Class(name="common::StringValueList")
common_StringValue = Class(name="common::StringValue")

# common_Identifiable class attributes and methods
common_Identifiable_uRI: Property = Property(name="uRI", type=StringType)
common_Identifiable_typeURI: Property = Property(name="typeURI", type=StringType)
common_Identifiable_m_sane: Method = Method(name="sane", parameters={}, type=BooleanType)
common_Identifiable.attributes={common_Identifiable_typeURI, common_Identifiable_uRI}
common_Identifiable.methods={common_Identifiable_m_sane}

# common_Comparable class attributes and methods

# common_IdentifiableFilter class attributes and methods

# common_DoubleValueList class attributes and methods
common_DoubleValueList_identifier: Property = Property(name="identifier", type=StringType)
common_DoubleValueList.attributes={common_DoubleValueList_identifier}

# common_DublinCore class attributes and methods
common_DublinCore_publisher: Property = Property(name="publisher", type=StringType)
common_DublinCore_coverage: Property = Property(name="coverage", type=StringType)
common_DublinCore_contributor: Property = Property(name="contributor", type=StringType)
common_DublinCore_relation: Property = Property(name="relation", type=StringType)
common_DublinCore_rights: Property = Property(name="rights", type=StringType)
common_DublinCore_source: Property = Property(name="source", type=StringType)
common_DublinCore_subject: Property = Property(name="subject", type=StringType)
common_DublinCore_type: Property = Property(name="type", type=StringType)
common_DublinCore_language: Property = Property(name="language", type=StringType)
common_DublinCore_bibliographicCitation: Property = Property(name="bibliographicCitation", type=StringType)
common_DublinCore_created: Property = Property(name="created", type=StringType)
common_DublinCore_license: Property = Property(name="license", type=StringType)
common_DublinCore_required: Property = Property(name="required", type=StringType)
common_DublinCore_spatial: Property = Property(name="spatial", type=StringType)
common_DublinCore_valid: Property = Property(name="valid", type=StringType)
common_DublinCore_title: Property = Property(name="title", type=StringType)
common_DublinCore_identifier: Property = Property(name="identifier", type=StringType)
common_DublinCore_description: Property = Property(name="description", type=StringType)
common_DublinCore_creator: Property = Property(name="creator", type=StringType)
common_DublinCore_date: Property = Property(name="date", type=StringType)
common_DublinCore_format: Property = Property(name="format", type=StringType)
common_DublinCore_m_populate: Method = Method(name="populate", parameters={}, type=StringType)
common_DublinCore.attributes={common_DublinCore_valid, common_DublinCore_spatial, common_DublinCore_format, common_DublinCore_bibliographicCitation, common_DublinCore_created, common_DublinCore_contributor, common_DublinCore_required, common_DublinCore_rights, common_DublinCore_language, common_DublinCore_coverage, common_DublinCore_description, common_DublinCore_publisher, common_DublinCore_identifier, common_DublinCore_relation, common_DublinCore_source, common_DublinCore_type, common_DublinCore_license, common_DublinCore_title, common_DublinCore_creator, common_DublinCore_subject, common_DublinCore_date}
common_DublinCore.methods={common_DublinCore_m_populate}

# common_DoubleValue class attributes and methods
common_DoubleValue_identifier: Property = Property(name="identifier", type=StringType)
common_DoubleValue_value: Property = Property(name="value", type=FloatType)
common_DoubleValue.attributes={common_DoubleValue_identifier, common_DoubleValue_value}

# common_DoubleValueMatrix class attributes and methods

# Modifiable class attributes and methods

# common_StringValueList class attributes and methods

# common_StringValue class attributes and methods
common_StringValue_value: Property = Property(name="value", type=StringType)
common_StringValue.attributes={common_StringValue_value}

# Relationships
dublinCore0: BinaryAssociation = BinaryAssociation(
    name="dublinCore0",
    ends={
        Property(name="common_DublinCore", type=common_Identifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="common_Identifiable", type=common_DublinCore, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values1: BinaryAssociation = BinaryAssociation(
    name="values1",
    ends={
        Property(name="common_DoubleValue", type=common_DoubleValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="common_DoubleValueList", type=common_DoubleValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueLists2: BinaryAssociation = BinaryAssociation(
    name="valueLists2",
    ends={
        Property(name="common_DoubleValueList3", type=common_DoubleValueMatrix, multiplicity=Multiplicity(1, 1)),
        Property(name="common_DoubleValueMatrix", type=common_DoubleValueList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values4: BinaryAssociation = BinaryAssociation(
    name="values4",
    ends={
        Property(name="common_StringValue", type=common_StringValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="common_StringValueList", type=common_StringValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_common_DoubleValue_Modifiable = Generalization(general=Modifiable, specific=common_DoubleValue)
gen_common_StringValue_Modifiable = Generalization(general=Modifiable, specific=common_StringValue)

# Domain Model
domain_model = DomainModel(
    name="common",
    types={common_Identifiable, common_Comparable, common_IdentifiableFilter, common_DoubleValueList, common_DublinCore, common_DoubleValue, common_DoubleValueMatrix, Modifiable, common_StringValueList, common_StringValue},
    associations={dublinCore0, values1, valueLists2, values4},
    generalizations={gen_common_DoubleValue_Modifiable, gen_common_StringValue_Modifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)