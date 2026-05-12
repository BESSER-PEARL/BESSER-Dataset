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
Tenses: Enumeration = Enumeration(
    name="Tenses",
    literals={
            EnumerationLiteral(name="both"),
			EnumerationLiteral(name="present")
    }
)

ActionTypeStatus: Enumeration = Enumeration(
    name="ActionTypeStatus",
    literals={
            EnumerationLiteral(name="resolved"),
			EnumerationLiteral(name="unresolved")
    }
)

# Classes
schema_StorySchemaCatalog = Class(name="schema_StorySchemaCatalog")
ResourceAware = Class(name="ResourceAware")
BundleAware = Class(name="BundleAware")
NsPrefixable = Class(name="NsPrefixable")
schema_StoryType = Class(name="schema_StoryType")
schema_ActionType = Class(name="schema_ActionType")
schema_AggregationType = Class(name="schema_AggregationType")
schema_TargetType = Class(name="schema_TargetType")
schema_TargetTypeRef = Class(name="schema_TargetTypeRef")
schema_EPackage = Class(name="schema_EPackage")
schema_EFactory = Class(name="schema_EFactory")
schema_ActionLike = Class(name="schema_ActionLike", is_abstract=True)
NameContainer = Class(name="NameContainer")

# schema_StorySchemaCatalog class attributes and methods
schema_StorySchemaCatalog_generatedPackageName: Property = Property(name="generatedPackageName", type=StringType)
schema_StorySchemaCatalog_xmiUrl: Property = Property(name="xmiUrl", type=StringType)
schema_StorySchemaCatalog_ecoreUrl: Property = Property(name="ecoreUrl", type=StringType)
schema_StorySchemaCatalog_m_createAction: Method = Method(name="createAction", parameters={Parameter(name='schema_targetClass', type=StringType)})
schema_StorySchemaCatalog.attributes={schema_StorySchemaCatalog_generatedPackageName, schema_StorySchemaCatalog_ecoreUrl, schema_StorySchemaCatalog_xmiUrl}
schema_StorySchemaCatalog.methods={schema_StorySchemaCatalog_m_createAction}

# ResourceAware class attributes and methods

# BundleAware class attributes and methods

# NsPrefixable class attributes and methods

# schema_StoryType class attributes and methods

# schema_ActionType class attributes and methods
schema_ActionType_status: Property = Property(name="status", type=StringType)
schema_ActionType_m_create: Method = Method(name="create", parameters={}, type=StringType)
schema_ActionType.attributes={schema_ActionType_status}
schema_ActionType.methods={schema_ActionType_m_create}

# schema_AggregationType class attributes and methods
schema_AggregationType_m_create: Method = Method(name="create", parameters={}, type=StringType)
schema_AggregationType.methods={schema_AggregationType_m_create}

# schema_TargetType class attributes and methods

# schema_TargetTypeRef class attributes and methods

# schema_EPackage class attributes and methods

# schema_EFactory class attributes and methods

# schema_ActionLike class attributes and methods
schema_ActionLike_tenses: Property = Property(name="tenses", type=StringType)
schema_ActionLike_pastTense: Property = Property(name="pastTense", type=StringType)
schema_ActionLike_pluralPastTense: Property = Property(name="pluralPastTense", type=StringType)
schema_ActionLike_presentTense: Property = Property(name="presentTense", type=StringType)
schema_ActionLike_pluralPresentTense: Property = Property(name="pluralPresentTense", type=StringType)
schema_ActionLike_imperativeTense: Property = Property(name="imperativeTense", type=StringType)
schema_ActionLike.attributes={schema_ActionLike_pastTense, schema_ActionLike_pluralPastTense, schema_ActionLike_pluralPresentTense, schema_ActionLike_tenses, schema_ActionLike_presentTense, schema_ActionLike_imperativeTense}

# NameContainer class attributes and methods

# Relationships
aggregationTypes3: BinaryAssociation = BinaryAssociation(
    name="aggregationTypes3",
    ends={
        Property(name="schema_StorySchemaCatalog4", type=schema_AggregationType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="schema_AggregationType", type=schema_StorySchemaCatalog, multiplicity=Multiplicity(1, 1))
    }
)
storyTypes0: BinaryAssociation = BinaryAssociation(
    name="storyTypes0",
    ends={
        Property(name="schema_StoryType", type=schema_StorySchemaCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="schema_StorySchemaCatalog", type=schema_StoryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionTypes1: BinaryAssociation = BinaryAssociation(
    name="actionTypes1",
    ends={
        Property(name="schema_ActionType", type=schema_StorySchemaCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="schema_StorySchemaCatalog2", type=schema_ActionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resolvedSubjectTypes9: BinaryAssociation = BinaryAssociation(
    name="resolvedSubjectTypes9",
    ends={
        Property(name="schema_TargetType", type=schema_ActionType, multiplicity=Multiplicity(1, 1)),
        Property(name="schema_ActionType10", type=schema_TargetType, multiplicity=Multiplicity(0, 9999))
    }
)
subjectTypes11: BinaryAssociation = BinaryAssociation(
    name="subjectTypes11",
    ends={
        Property(name="schema_TargetTypeRef", type=schema_ActionType, multiplicity=Multiplicity(1, 1)),
        Property(name="schema_ActionType12", type=schema_TargetTypeRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ePackage5: BinaryAssociation = BinaryAssociation(
    name="ePackage5",
    ends={
        Property(name="schema_EPackage", type=schema_StorySchemaCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="schema_StorySchemaCatalog6", type=schema_EPackage, multiplicity=Multiplicity(0, 1))
    }
)
eFactory7: BinaryAssociation = BinaryAssociation(
    name="eFactory7",
    ends={
        Property(name="schema_EFactory", type=schema_StorySchemaCatalog, multiplicity=Multiplicity(1, 1)),
        Property(name="schema_StorySchemaCatalog8", type=schema_EFactory, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_schema_StorySchemaCatalog_ResourceAware = Generalization(general=ResourceAware, specific=schema_StorySchemaCatalog)
gen_schema_StorySchemaCatalog_BundleAware = Generalization(general=BundleAware, specific=schema_StorySchemaCatalog)
gen_schema_StorySchemaCatalog_NsPrefixable = Generalization(general=NsPrefixable, specific=schema_StorySchemaCatalog)
gen_schema_TargetTypeRef_NsPrefixable = Generalization(general=NsPrefixable, specific=schema_TargetTypeRef)
gen_schema_TargetTypeRef_NameContainer = Generalization(general=NameContainer, specific=schema_TargetTypeRef)

# Domain Model
domain_model = DomainModel(
    name="schema",
    types={schema_StorySchemaCatalog, ResourceAware, BundleAware, NsPrefixable, schema_StoryType, schema_ActionType, schema_AggregationType, schema_TargetType, schema_TargetTypeRef, schema_EPackage, schema_EFactory, schema_ActionLike, NameContainer, Tenses, ActionTypeStatus},
    associations={aggregationTypes3, storyTypes0, actionTypes1, resolvedSubjectTypes9, subjectTypes11, ePackage5, eFactory7},
    generalizations={gen_schema_StorySchemaCatalog_ResourceAware, gen_schema_StorySchemaCatalog_BundleAware, gen_schema_StorySchemaCatalog_NsPrefixable, gen_schema_TargetTypeRef_NsPrefixable, gen_schema_TargetTypeRef_NameContainer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)