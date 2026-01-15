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
graphDsl_Graph = Class(name="graphDsl::Graph")
graphDsl_ComponentOrFacet = Class(name="graphDsl::ComponentOrFacet")
graphDsl_Component = Class(name="graphDsl::Component")
graphDsl_Facet = Class(name="graphDsl::Facet")
graphDsl_ComponentProperties = Class(name="graphDsl::ComponentProperties")
graphDsl_FacetProperties = Class(name="graphDsl::FacetProperties")
graphDsl_OptionalProperty = Class(name="graphDsl::OptionalProperty")
graphDsl_InstallerProperty = Class(name="graphDsl::InstallerProperty")
graphDsl_FacetProperty = Class(name="graphDsl::FacetProperty")
graphDsl_ChildrenProperty = Class(name="graphDsl::ChildrenProperty")
graphDsl_ExportsProperty = Class(name="graphDsl::ExportsProperty")
graphDsl_ImportsProperty = Class(name="graphDsl::ImportsProperty")
graphDsl_FacetsProperty = Class(name="graphDsl::FacetsProperty")
graphDsl_ExtendsProperty = Class(name="graphDsl::ExtendsProperty")
graphDsl_ExportsVariable = Class(name="graphDsl::ExportsVariable")
graphDsl_ImportsVariable = Class(name="graphDsl::ImportsVariable")

# graphDsl_Graph class attributes and methods
graphDsl_Graph_comments: Property = Property(name="comments", type=StringType)
graphDsl_Graph.attributes={graphDsl_Graph_comments}

# graphDsl_ComponentOrFacet class attributes and methods

# graphDsl_Component class attributes and methods
graphDsl_Component_name: Property = Property(name="name", type=StringType)
graphDsl_Component.attributes={graphDsl_Component_name}

# graphDsl_Facet class attributes and methods
graphDsl_Facet_name: Property = Property(name="name", type=StringType)
graphDsl_Facet.attributes={graphDsl_Facet_name}

# graphDsl_ComponentProperties class attributes and methods

# graphDsl_FacetProperties class attributes and methods

# graphDsl_OptionalProperty class attributes and methods

# graphDsl_InstallerProperty class attributes and methods
graphDsl_InstallerProperty_name: Property = Property(name="name", type=StringType)
graphDsl_InstallerProperty.attributes={graphDsl_InstallerProperty_name}

# graphDsl_FacetProperty class attributes and methods

# graphDsl_ChildrenProperty class attributes and methods
graphDsl_ChildrenProperty_name: Property = Property(name="name", type=StringType)
graphDsl_ChildrenProperty.attributes={graphDsl_ChildrenProperty_name}

# graphDsl_ExportsProperty class attributes and methods

# graphDsl_ImportsProperty class attributes and methods

# graphDsl_FacetsProperty class attributes and methods
graphDsl_FacetsProperty_facetsNames: Property = Property(name="facetsNames", type=StringType)
graphDsl_FacetsProperty.attributes={graphDsl_FacetsProperty_facetsNames}

# graphDsl_ExtendsProperty class attributes and methods
graphDsl_ExtendsProperty_extendsNames: Property = Property(name="extendsNames", type=StringType)
graphDsl_ExtendsProperty.attributes={graphDsl_ExtendsProperty_extendsNames}

# graphDsl_ExportsVariable class attributes and methods
graphDsl_ExportsVariable_name: Property = Property(name="name", type=StringType)
graphDsl_ExportsVariable_intValue: Property = Property(name="intValue", type=IntegerType)
graphDsl_ExportsVariable_strValue: Property = Property(name="strValue", type=StringType)
graphDsl_ExportsVariable.attributes={graphDsl_ExportsVariable_name, graphDsl_ExportsVariable_strValue, graphDsl_ExportsVariable_intValue}

# graphDsl_ImportsVariable class attributes and methods
graphDsl_ImportsVariable_isExternal: Property = Property(name="isExternal", type=BooleanType)
graphDsl_ImportsVariable_componentName: Property = Property(name="componentName", type=StringType)
graphDsl_ImportsVariable_componentProperty: Property = Property(name="componentProperty", type=StringType)
graphDsl_ImportsVariable_isOptional: Property = Property(name="isOptional", type=BooleanType)
graphDsl_ImportsVariable.attributes={graphDsl_ImportsVariable_isExternal, graphDsl_ImportsVariable_componentName, graphDsl_ImportsVariable_isOptional, graphDsl_ImportsVariable_componentProperty}

# Relationships
properties7: BinaryAssociation = BinaryAssociation(
    name="properties7",
    ends={
        Property(name="graphDsl_FacetProperties", type=graphDsl_Facet, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_Facet8", type=graphDsl_FacetProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="graphDsl_ComponentOrFacet", type=graphDsl_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_Graph", type=graphDsl_ComponentOrFacet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
component1: BinaryAssociation = BinaryAssociation(
    name="component1",
    ends={
        Property(name="graphDsl_Component", type=graphDsl_ComponentOrFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_ComponentOrFacet2", type=graphDsl_Component, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facet3: BinaryAssociation = BinaryAssociation(
    name="facet3",
    ends={
        Property(name="graphDsl_Facet", type=graphDsl_ComponentOrFacet, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_ComponentOrFacet4", type=graphDsl_Facet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties5: BinaryAssociation = BinaryAssociation(
    name="properties5",
    ends={
        Property(name="graphDsl_ComponentProperties", type=graphDsl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_Component6", type=graphDsl_ComponentProperties, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optionalProperties9: BinaryAssociation = BinaryAssociation(
    name="optionalProperties9",
    ends={
        Property(name="graphDsl_OptionalProperty", type=graphDsl_ComponentProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_ComponentProperties10", type=graphDsl_OptionalProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
installerProperty11: BinaryAssociation = BinaryAssociation(
    name="installerProperty11",
    ends={
        Property(name="graphDsl_InstallerProperty", type=graphDsl_ComponentProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_ComponentProperties12", type=graphDsl_InstallerProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties13: BinaryAssociation = BinaryAssociation(
    name="properties13",
    ends={
        Property(name="graphDsl_FacetProperty", type=graphDsl_FacetProperties, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_FacetProperties14", type=graphDsl_FacetProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenProperty15: BinaryAssociation = BinaryAssociation(
    name="childrenProperty15",
    ends={
        Property(name="graphDsl_ChildrenProperty", type=graphDsl_FacetProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_FacetProperty16", type=graphDsl_ChildrenProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exportsProperty17: BinaryAssociation = BinaryAssociation(
    name="exportsProperty17",
    ends={
        Property(name="graphDsl_ExportsProperty", type=graphDsl_FacetProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_FacetProperty18", type=graphDsl_ExportsProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childrenProperty19: BinaryAssociation = BinaryAssociation(
    name="childrenProperty19",
    ends={
        Property(name="graphDsl_ChildrenProperty21", type=graphDsl_OptionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_OptionalProperty20", type=graphDsl_ChildrenProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exportsProperty22: BinaryAssociation = BinaryAssociation(
    name="exportsProperty22",
    ends={
        Property(name="graphDsl_ExportsProperty24", type=graphDsl_OptionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_OptionalProperty23", type=graphDsl_ExportsProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importsProperty25: BinaryAssociation = BinaryAssociation(
    name="importsProperty25",
    ends={
        Property(name="graphDsl_ImportsProperty", type=graphDsl_OptionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_OptionalProperty26", type=graphDsl_ImportsProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
facetsProperty27: BinaryAssociation = BinaryAssociation(
    name="facetsProperty27",
    ends={
        Property(name="graphDsl_FacetsProperty", type=graphDsl_OptionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_OptionalProperty28", type=graphDsl_FacetsProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendsProperty29: BinaryAssociation = BinaryAssociation(
    name="extendsProperty29",
    ends={
        Property(name="graphDsl_ExtendsProperty", type=graphDsl_OptionalProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_OptionalProperty30", type=graphDsl_ExtendsProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exportsVariables31: BinaryAssociation = BinaryAssociation(
    name="exportsVariables31",
    ends={
        Property(name="graphDsl_ExportsVariable", type=graphDsl_ExportsProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_ExportsProperty32", type=graphDsl_ExportsVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importsVariables33: BinaryAssociation = BinaryAssociation(
    name="importsVariables33",
    ends={
        Property(name="graphDsl_ImportsVariable", type=graphDsl_ImportsProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="graphDsl_ImportsProperty34", type=graphDsl_ImportsVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="graphDsl",
    types={graphDsl_Graph, graphDsl_ComponentOrFacet, graphDsl_Component, graphDsl_Facet, graphDsl_ComponentProperties, graphDsl_FacetProperties, graphDsl_OptionalProperty, graphDsl_InstallerProperty, graphDsl_FacetProperty, graphDsl_ChildrenProperty, graphDsl_ExportsProperty, graphDsl_ImportsProperty, graphDsl_FacetsProperty, graphDsl_ExtendsProperty, graphDsl_ExportsVariable, graphDsl_ImportsVariable},
    associations={properties7, components0, component1, facet3, properties5, optionalProperties9, installerProperty11, properties13, childrenProperty15, exportsProperty17, childrenProperty19, exportsProperty22, importsProperty25, facetsProperty27, extendsProperty29, exportsVariables31, importsVariables33},
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