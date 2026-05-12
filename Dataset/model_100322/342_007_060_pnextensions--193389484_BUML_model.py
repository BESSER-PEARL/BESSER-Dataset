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
ToolInfoConstants: Enumeration = Enumeration(
    name="ToolInfoConstants",
    literals={
            EnumerationLiteral(name="toolName"),
			EnumerationLiteral(name="toolVersion"),
			EnumerationLiteral(name="uri")
    }
)

TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="Immediate"),
			EnumerationLiteral(name="Exponential"),
			EnumerationLiteral(name="Deterministic")
    }
)

ServerType: Enumeration = Enumeration(
    name="ServerType",
    literals={
            EnumerationLiteral(name="InfiniteServer"),
			EnumerationLiteral(name="OneServer"),
			EnumerationLiteral(name="LoadDependent"),
			EnumerationLiteral(name="MarkingDependent")
    }
)

# Classes
pnextensions_pnutils_DataTypeUtils = Class(name="pnextensions_pnutils_DataTypeUtils")
pnextensions_pnutils_ToolInfoUtils = Class(name="pnextensions_pnutils_ToolInfoUtils")
pnextensions_pnutils_PnUtils = Class(name="pnextensions_pnutils_PnUtils")

# pnextensions_pnutils_DataTypeUtils class attributes and methods
pnextensions_pnutils_DataTypeUtils_m_createURI: Method = Method(name="createURI", parameters={Parameter(name='pnextensions_stringUri', type=StringType)}, type=StringType)
pnextensions_pnutils_DataTypeUtils_m_createLongString: Method = Method(name="createLongString", parameters={Parameter(name='pnextensions_string', type=StringType)}, type=StringType)
pnextensions_pnutils_DataTypeUtils.methods={pnextensions_pnutils_DataTypeUtils_m_createURI, pnextensions_pnutils_DataTypeUtils_m_createLongString}

# pnextensions_pnutils_ToolInfoUtils class attributes and methods
pnextensions_pnutils_ToolInfoUtils_m_isEObjectValidPnObject: Method = Method(name="isEObjectValidPnObject", parameters={Parameter(name='pnextensions_eObject', type=StringType)}, type=BooleanType)
pnextensions_pnutils_ToolInfoUtils_m_isEObjectValidTransition: Method = Method(name="isEObjectValidTransition", parameters={Parameter(name='pnextensions_eObject', type=StringType)}, type=BooleanType)
pnextensions_pnutils_ToolInfoUtils_m_setTransitionKind: Method = Method(name="setTransitionKind", parameters={Parameter(name='pnextensions_transition', type=StringType), Parameter(name='pnextensions_value', type=StringType), Parameter(name='pnextensions_transitionKind', type=StringType)})
pnextensions_pnutils_ToolInfoUtils_m_setTransitionServerType: Method = Method(name="setTransitionServerType", parameters={Parameter(name='pnextensions_value', type=StringType), Parameter(name='pnextensions_transition', type=StringType), Parameter(name='pnextensions_serverType', type=StringType)})
pnextensions_pnutils_ToolInfoUtils_m_getTransitionRate: Method = Method(name="getTransitionRate", parameters={Parameter(name='pnextensions_transition', type=StringType)}, type=StringType)
pnextensions_pnutils_ToolInfoUtils_m_getToolInfoEntryByGrammarUri: Method = Method(name="getToolInfoEntryByGrammarUri", parameters={Parameter(name='pnextensions_uri', type=StringType), Parameter(name='pnextensions_pnObject', type=StringType)}, type=StringType)
pnextensions_pnutils_ToolInfoUtils_m_deleteToolInfoEntryByGrammarUri: Method = Method(name="deleteToolInfoEntryByGrammarUri", parameters={Parameter(name='pnextensions_pnObject', type=StringType), Parameter(name='pnextensions_uri', type=StringType)}, type=StringType)
pnextensions_pnutils_ToolInfoUtils_m_setToolInfoEntryByGrammarUri: Method = Method(name="setToolInfoEntryByGrammarUri", parameters={Parameter(name='pnextensions_value', type=StringType), Parameter(name='pnextensions_uri', type=StringType), Parameter(name='pnextensions_pnObject', type=StringType)})
pnextensions_pnutils_ToolInfoUtils_m_isTransitionKind: Method = Method(name="isTransitionKind", parameters={Parameter(name='pnextensions_transitionKind', type=StringType), Parameter(name='pnextensions_transition', type=StringType)}, type=BooleanType)
pnextensions_pnutils_ToolInfoUtils_m_isTransitionServerType: Method = Method(name="isTransitionServerType", parameters={Parameter(name='pnextensions_transition', type=StringType), Parameter(name='pnextensions_serverType', type=StringType)}, type=BooleanType)
pnextensions_pnutils_ToolInfoUtils.methods={pnextensions_pnutils_ToolInfoUtils_m_getToolInfoEntryByGrammarUri, pnextensions_pnutils_ToolInfoUtils_m_setTransitionKind, pnextensions_pnutils_ToolInfoUtils_m_isTransitionKind, pnextensions_pnutils_ToolInfoUtils_m_setTransitionServerType, pnextensions_pnutils_ToolInfoUtils_m_isTransitionServerType, pnextensions_pnutils_ToolInfoUtils_m_deleteToolInfoEntryByGrammarUri, pnextensions_pnutils_ToolInfoUtils_m_setToolInfoEntryByGrammarUri, pnextensions_pnutils_ToolInfoUtils_m_getTransitionRate, pnextensions_pnutils_ToolInfoUtils_m_isEObjectValidPnObject, pnextensions_pnutils_ToolInfoUtils_m_isEObjectValidTransition}

# pnextensions_pnutils_PnUtils class attributes and methods
pnextensions_pnutils_PnUtils_m_layout: Method = Method(name="layout", parameters={Parameter(name='pnextensions_petriNet', type=StringType)})
pnextensions_pnutils_PnUtils.methods={pnextensions_pnutils_PnUtils_m_layout}

# Domain Model
domain_model = DomainModel(
    name="pnextensions",
    types={pnextensions_pnutils_DataTypeUtils, pnextensions_pnutils_ToolInfoUtils, pnextensions_pnutils_PnUtils, ToolInfoConstants, TransitionKind, ServerType},
    associations={},
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