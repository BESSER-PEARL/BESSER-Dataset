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
UIElementType: Enumeration = Enumeration(
    name="UIElementType",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output")
    }
)

# Classes
webapp_Named = Class(name="webapp::Named", is_abstract=True)
webapp_WebApp = Class(name="webapp::WebApp")
Named = Class(name="Named")
webapp_ClientPage = Class(name="webapp::ClientPage")
webapp_Attribute = Class(name="webapp::Attribute")
webapp_UIElement = Class(name="webapp::UIElement")
webapp_ServerPage = Class(name="webapp::ServerPage")
webapp_DataStructure = Class(name="webapp::DataStructure")
webapp_DataSourceManager = Class(name="webapp::DataSourceManager")
webapp_Form = Class(name="webapp::Form")
UIElement = Class(name="UIElement")
webapp_ImageViewer = Class(name="webapp::ImageViewer")
webapp_TextArea = Class(name="webapp::TextArea")
webapp_Table = Class(name="webapp::Table")

# webapp_Named class attributes and methods
webapp_Named_name: Property = Property(name="name", type=StringType)
webapp_Named.attributes={webapp_Named_name}

# webapp_WebApp class attributes and methods

# Named class attributes and methods

# webapp_ClientPage class attributes and methods

# webapp_Attribute class attributes and methods
webapp_Attribute_type: Property = Property(name="type", type=StringType)
webapp_Attribute.attributes={webapp_Attribute_type}

# webapp_UIElement class attributes and methods
webapp_UIElement_type: Property = Property(name="type", type=StringType)
webapp_UIElement.attributes={webapp_UIElement_type}

# webapp_ServerPage class attributes and methods
webapp_ServerPage_m_response: Method = Method(name="response", parameters={})
webapp_ServerPage_m_request: Method = Method(name="request", parameters={})
webapp_ServerPage.methods={webapp_ServerPage_m_response, webapp_ServerPage_m_request}

# webapp_DataStructure class attributes and methods

# webapp_DataSourceManager class attributes and methods

# webapp_Form class attributes and methods

# UIElement class attributes and methods

# webapp_ImageViewer class attributes and methods

# webapp_TextArea class attributes and methods

# webapp_Table class attributes and methods

# Relationships
clientPages0: BinaryAssociation = BinaryAssociation(
    name="clientPages0",
    ends={
        Property(name="webapp_ClientPage", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp", type=webapp_ClientPage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
generates7: BinaryAssociation = BinaryAssociation(
    name="generates7",
    ends={
        Property(name="ClientPage", type=webapp_ServerPage, multiplicity=Multiplicity(1, 1)),
        Property(name="connectsTo", type=webapp_ClientPage, multiplicity=Multiplicity(1, 1))
    }
)
getContents8: BinaryAssociation = BinaryAssociation(
    name="getContents8",
    ends={
        Property(name="DataSourceManager", type=webapp_ServerPage, multiplicity=Multiplicity(1, 1)),
        Property(name="providesContent", type=webapp_DataSourceManager, multiplicity=Multiplicity(1, 9999))
    }
)
manages9: BinaryAssociation = BinaryAssociation(
    name="manages9",
    ends={
        Property(name="DataStructure", type=webapp_ServerPage, multiplicity=Multiplicity(1, 1)),
        Property(name="managedBy", type=webapp_DataStructure, multiplicity=Multiplicity(1, 9999))
    }
)
managedBy10: BinaryAssociation = BinaryAssociation(
    name="managedBy10",
    ends={
        Property(name="ServerPage", type=webapp_DataStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="manages", type=webapp_ServerPage, multiplicity=Multiplicity(1, 9999))
    }
)
parentOf11: BinaryAssociation = BinaryAssociation(
    name="parentOf11",
    ends={
        Property(name="Attribute", type=webapp_DataStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeOf", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkedTo12: BinaryAssociation = BinaryAssociation(
    name="linkedTo12",
    ends={
        Property(name="Attribute13", type=webapp_DataStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="linkedBy", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
providesContent14: BinaryAssociation = BinaryAssociation(
    name="providesContent14",
    ends={
        Property(name="ServerPage15", type=webapp_DataSourceManager, multiplicity=Multiplicity(1, 1)),
        Property(name="getContents", type=webapp_ServerPage, multiplicity=Multiplicity(1, 9999))
    }
)
attributeOf16: BinaryAssociation = BinaryAssociation(
    name="attributeOf16",
    ends={
        Property(name="DataStructure17", type=webapp_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="parentOf", type=webapp_DataStructure, multiplicity=Multiplicity(1, 1))
    }
)
linkedBy18: BinaryAssociation = BinaryAssociation(
    name="linkedBy18",
    ends={
        Property(name="DataStructure19", type=webapp_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="linkedTo", type=webapp_DataStructure, multiplicity=Multiplicity(0, 9999))
    }
)
composedOf20: BinaryAssociation = BinaryAssociation(
    name="composedOf20",
    ends={
        Property(name="webapp_UIElement", type=webapp_ClientPage, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_ClientPage21", type=webapp_UIElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serverPages1: BinaryAssociation = BinaryAssociation(
    name="serverPages1",
    ends={
        Property(name="webapp_ServerPage", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp2", type=webapp_ServerPage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entities3: BinaryAssociation = BinaryAssociation(
    name="entities3",
    ends={
        Property(name="webapp_DataStructure", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp4", type=webapp_DataStructure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentProviders5: BinaryAssociation = BinaryAssociation(
    name="contentProviders5",
    ends={
        Property(name="webapp_DataSourceManager", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp6", type=webapp_DataSourceManager, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectsTo22: BinaryAssociation = BinaryAssociation(
    name="connectsTo22",
    ends={
        Property(name="ServerPage23", type=webapp_ClientPage, multiplicity=Multiplicity(1, 1)),
        Property(name="generates", type=webapp_ServerPage, multiplicity=Multiplicity(1, 1))
    }
)
content24: BinaryAssociation = BinaryAssociation(
    name="content24",
    ends={
        Property(name="webapp_DataStructure26", type=webapp_UIElement, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_UIElement25", type=webapp_DataStructure, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_webapp_WebApp_Named = Generalization(general=Named, specific=webapp_WebApp)
gen_webapp_DataStructure_Named = Generalization(general=Named, specific=webapp_DataStructure)
gen_webapp_DataSourceManager_Named = Generalization(general=Named, specific=webapp_DataSourceManager)
gen_webapp_Attribute_Named = Generalization(general=Named, specific=webapp_Attribute)
gen_webapp_ClientPage_Named = Generalization(general=Named, specific=webapp_ClientPage)
gen_webapp_ServerPage_Named = Generalization(general=Named, specific=webapp_ServerPage)
gen_webapp_UIElement_Named = Generalization(general=Named, specific=webapp_UIElement)
gen_webapp_Form_UIElement = Generalization(general=UIElement, specific=webapp_Form)
gen_webapp_ImageViewer_UIElement = Generalization(general=UIElement, specific=webapp_ImageViewer)
gen_webapp_TextArea_UIElement = Generalization(general=UIElement, specific=webapp_TextArea)
gen_webapp_Table_UIElement = Generalization(general=UIElement, specific=webapp_Table)

# Domain Model
domain_model = DomainModel(
    name="webapp",
    types={webapp_Named, webapp_WebApp, Named, webapp_ClientPage, webapp_Attribute, webapp_UIElement, webapp_ServerPage, webapp_DataStructure, webapp_DataSourceManager, webapp_Form, UIElement, webapp_ImageViewer, webapp_TextArea, webapp_Table, UIElementType},
    associations={clientPages0, generates7, getContents8, manages9, managedBy10, parentOf11, linkedTo12, providesContent14, attributeOf16, linkedBy18, composedOf20, serverPages1, entities3, contentProviders5, connectsTo22, content24},
    generalizations={gen_webapp_WebApp_Named, gen_webapp_DataStructure_Named, gen_webapp_DataSourceManager_Named, gen_webapp_Attribute_Named, gen_webapp_ClientPage_Named, gen_webapp_ServerPage_Named, gen_webapp_UIElement_Named, gen_webapp_Form_UIElement, gen_webapp_ImageViewer_UIElement, gen_webapp_TextArea_UIElement, gen_webapp_Table_UIElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)